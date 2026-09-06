#!/usr/bin/env python3
"""Build a deterministic, self-contained PLS release bundle.

The command line form is intended for a clean checkout.  ``build_release`` is
also available for tests and other narrow callers that already know the source
root, release version, commit, and final output directory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Iterable
import zipfile


REPOSITORY = "brightskye/pls"
SKILL_SOURCE = Path("src") / "pls"
INSTALLER_SOURCE = Path("tools") / "pls_skill.py"
LICENSE_SOURCE = Path("LICENSE")
ZIP_NAME = "pls.zip"
HASH_NAME = "pls.zip.sha256"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
COMMIT_PATTERN = re.compile(r"[0-9a-f]{40}\Z")
VERSION_PATTERN = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+\Z")


class BundleError(Exception):
    """The release could not be built safely."""


def _read_frontmatter(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise BundleError(f"Cannot read bundled standard: {path}") from error
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise BundleError(f"Bundled standard has no frontmatter: {path}")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise BundleError(f"Bundled standard frontmatter is not closed: {path}") from error
    values: dict[str, str] = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        if not separator or not key.strip() or not value.strip():
            continue
        values[key.strip()] = value.strip().strip("'\"")
    return values


def _validate_release_version(root: Path, version: str) -> None:
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:-draft\.[0-9]+)?", version):
        raise BundleError(f"Invalid release version: {version}")
    standard_path = root / SKILL_SOURCE / "references" / "PLS.md"
    frontmatter = _read_frontmatter(standard_path)
    standard_version = frontmatter.get("version", "")
    status = frontmatter.get("status", "")
    if not VERSION_PATTERN.fullmatch(standard_version):
        raise BundleError("Bundled standard has an invalid version")
    if status == "working":
        expected = rf"{re.escape(standard_version)}-draft\.[0-9]+"
        if not re.fullmatch(expected, version):
            raise BundleError(
                f"Working PLS {standard_version} releases must use "
                f"{standard_version}-draft.N (got {version})"
            )
    elif status == "stable":
        if version != standard_version:
            raise BundleError(
                f"Stable PLS {standard_version} releases must use {standard_version}"
            )
    else:
        raise BundleError(f"Unsupported bundled PLS status: {status or '<missing>'}")


def _validate_commit(commit: str) -> None:
    if not COMMIT_PATTERN.fullmatch(commit):
        raise BundleError("Commit must be a 40-character lowercase hexadecimal SHA")


def _reject_private_or_special(path: Path, relative: Path) -> None:
    if any(part.startswith(".") for part in relative.parts):
        raise BundleError(f"Refusing private file in bundle source: {path}")
    if any(part == "__pycache__" for part in relative.parts):
        raise BundleError(f"Refusing generated cache in bundle source: {path}")
    if path.is_symlink():
        raise BundleError(f"Refusing symlink in bundle source: {path}")


def _source_files(directory: Path) -> Iterable[tuple[str, Path]]:
    if directory.is_symlink():
        raise BundleError(f"Refusing symlink in bundle source: {directory}")
    if not directory.is_dir():
        raise BundleError(f"Missing bundle source directory: {directory}")
    paths = sorted(directory.rglob("*"), key=lambda path: path.relative_to(directory).as_posix())
    found = False
    for path in paths:
        relative = path.relative_to(directory)
        _reject_private_or_special(path, relative)
        if path.is_dir():
            continue
        if not path.is_file():
            raise BundleError(f"Unsupported file in bundle source: {path}")
        found = True
        yield (Path("skills") / "pls" / relative).as_posix(), path
    if not found:
        raise BundleError(f"Bundle source directory is empty: {directory}")


def _required_file(root: Path, relative: Path) -> Path:
    path = root / relative
    if path.is_symlink():
        raise BundleError(f"Refusing symlink in bundle source: {path}")
    if not path.is_file():
        raise BundleError(f"Missing required bundle file: {path}")
    if path.name.startswith("."):
        raise BundleError(f"Refusing private file in bundle source: {path}")
    return path


def _read_sources(root: Path) -> dict[str, bytes]:
    source_dir = root / SKILL_SOURCE
    files = dict(_read_file(path, arcname) for arcname, path in _source_files(source_dir))
    if not files.get("skills/pls/SKILL.md") or not files.get("skills/pls/references/PLS.md"):
        raise BundleError("PLS skill must contain SKILL.md and references/PLS.md")
    installer = _required_file(root, INSTALLER_SOURCE)
    license_file = _required_file(root, LICENSE_SOURCE)
    files["install.py"] = installer.read_bytes()
    files["LICENSE"] = license_file.read_bytes()
    return files


def _read_file(path: Path, archive_name: str) -> tuple[str, bytes]:
    try:
        return archive_name, path.read_bytes()
    except (OSError, UnicodeError) as error:
        raise BundleError(f"Cannot read bundle file: {path}") from error


def _readme(version: str) -> bytes:
    standard_version = version.split("-", 1)[0]
    status = "working draft" if "-draft." in version else "stable standard"
    text = f"""# PLS {version}

This bundle contains the PLS v{standard_version} {status} and its Python installer.
The release version identifies the exact packaged rules and installer.

## Install

From the target project's root, run:

```bash
python3 /path/to/pls/install.py install
```

The skill, rules, updater, instructions, release metadata, and license are
copied together to `.agents/skills/pls/`. Use `--dest` with the parent skills
directory when a different managed location is needed. This Python route needs
no PLS checkout, Node.js, or third-party Python packages. The extracted bundle
is no longer needed after installation.
Python 3.10 or newer is required. Installation uses the local bundle offline.

The installed directory contains the skill, rules, updater, instructions,
license, release metadata, and `.pls-install.json` receipt. The receipt records
hashes for every installed bundle file and detects local edits before updates.

## Update

Run the installed updater from any working directory:

```bash
python3 /absolute/path/to/project/.agents/skills/pls/install.py update
```

It asks for the latest published bundle and updates every managed file,
including `install.py` itself. Use `--dest` with the parent skills directory to
override the managed location.
For an explicitly offline update, provide an extracted bundle directory:

```bash
python3 /absolute/path/to/project/.agents/skills/pls/install.py update --bundle /path/to/extracted/pls
```

The extracted update bundle is no longer needed after the update. An unchanged
Python installation from `v0.3.0-draft.1` can be migrated once with the new
downloaded installer:

```bash
python3 /path/to/new/pls/install.py update --bundle /path/to/new/pls
```

Installing the skill does not adopt PLS or reorganize a project. Human
adoption and layout decisions remain separate.
"""
    return text.encode("utf-8")


def _release_metadata(version: str, commit: str) -> bytes:
    metadata = {
        "format": 1,
        "repository": REPOSITORY,
        "version": version,
        "commit": commit,
    }
    return (json.dumps(metadata, indent=2) + "\n").encode("utf-8")


def _write_zip(path: Path, files: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_STORED) as bundle:
        for name in sorted(files):
            if not name.startswith("pls/") or name.endswith("/"):
                raise BundleError(f"Invalid archive path: {name}")
            info = zipfile.ZipInfo(name, date_time=ZIP_TIMESTAMP)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            bundle.writestr(info, files[name])


def build_release(root: Path | str, version: str, commit: str, output: Path | str) -> tuple[Path, Path]:
    """Build one release into an explicit, version-specific output directory.

    ``output`` is the final directory that will contain ``pls.zip`` and its
    checksum.  It must not already exist.  No Git commands are run here, which
    lets tests and narrowly scoped callers supply an explicit commit.
    """
    root = Path(root).expanduser().absolute()
    output = Path(output).expanduser().absolute()
    _validate_commit(commit)
    _validate_release_version(root, version)
    files = _read_sources(root)
    files["README.md"] = _readme(version)
    files["release.json"] = _release_metadata(version, commit)
    archive_files = {f"pls/{name}": data for name, data in files.items()}

    if output.exists() or output.is_symlink():
        raise BundleError(f"Release output already exists: {output}")
    parent = output.parent
    parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{version}-", dir=parent) as temporary:
        stage = Path(temporary) / output.name
        stage.mkdir()
        archive = stage / ZIP_NAME
        _write_zip(archive, archive_files)
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        (stage / HASH_NAME).write_text(f"{digest}  {ZIP_NAME}\n", encoding="ascii")
        if output.exists() or output.is_symlink():
            raise BundleError(f"Release output already exists: {output}")
        stage.rename(output)
    return output / ZIP_NAME, output / HASH_NAME


def _git_output(root: Path, *arguments: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise BundleError(f"Cannot inspect Git checkout: {' '.join(arguments)}") from error
    return result.stdout.strip()


def _checkout_commit(root: Path) -> str:
    status = _git_output(root, "status", "--porcelain", "--untracked-files=all")
    if status:
        raise BundleError("Release builds require a clean Git checkout")
    commit = _git_output(root, "rev-parse", "HEAD")
    _validate_commit(commit)
    return commit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="versioned release name")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="parent directory for versioned output (default: releases)",
    )
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    output_parent = args.output_dir or root / "releases"
    try:
        commit = _checkout_commit(root)
        archive, checksum = build_release(root, args.version, commit, output_parent / args.version)
    except (BundleError, OSError) as error:
        print(f"PLS: {error}", file=sys.stderr)
        return 1
    print(f"Built {archive}")
    print(f"SHA-256 {checksum}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
