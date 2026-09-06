#!/usr/bin/env python3
"""Install or update the public PLS skill with Python 3.10+ and no dependencies.

The default destination is .agents/skills/pls in the current project. --dest
selects another host's skills directory. Updates follow the saved Git ref;
--ref explicitly changes it. Existing unmanaged or edited skills are preserved.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
from urllib.error import URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
import zipfile


REPOSITORY = "brightskye/pls"
SKILL_PATH = "src/pls"
RECEIPT = ".pls-install.json"
MAX_DOWNLOAD = 20 * 1024 * 1024


class InstallError(Exception):
    """An installation could not be completed safely."""


def download(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "pls-skill-installer"})
    with urlopen(request, timeout=30) as response:
        payload = response.read(MAX_DOWNLOAD + 1)
    if len(payload) > MAX_DOWNLOAD:
        raise InstallError("GitHub response exceeds the 20 MiB download limit.")
    return payload


def fetch_skill(ref: str) -> tuple[str, dict[str, bytes]]:
    # Resolve once, so the downloaded files and recorded revision agree even
    # when a branch moves between the two requests.
    commit = json.loads(download(
        f"https://api.github.com/repos/{REPOSITORY}/commits/{quote(ref, safe='')}"
    )).get("sha", "")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise InstallError("GitHub did not return a valid commit.")
    archive = download(f"https://codeload.github.com/{REPOSITORY}/zip/{commit}")
    return commit, read_skill(archive)


def read_skill(archive: bytes) -> dict[str, bytes]:
    """Read only the self-contained skill; never extract repository paths."""
    files = {}
    total_size = 0
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for entry in bundle.infolist():
            parts = entry.filename.split("/")
            if parts[1:3] != SKILL_PATH.split("/"):
                continue
            relative = "/".join(parts[3:]).rstrip("/")
            if not relative:
                continue
            path = PurePosixPath(relative)
            if (path.is_absolute() or ".." in path.parts or relative != path.as_posix()
                    or "\\" in relative or ":" in relative
                    or stat.S_ISLNK(entry.external_attr >> 16)):
                raise InstallError("The skill archive contains an unsafe path.")
            if entry.is_dir():
                continue
            if relative == RECEIPT or relative in files:
                raise InstallError("The skill archive contains a reserved or duplicate file.")
            total_size += entry.file_size
            if total_size > MAX_DOWNLOAD or len(files) >= 1000:
                raise InstallError("The skill archive exceeds the installation size limit.")
            files[relative] = bundle.read(entry)
    if not files.get("SKILL.md") or not files.get("references/PLS.md"):
        raise InstallError(f"This revision does not contain a complete {SKILL_PATH} skill.")
    return files


def hashes(files: dict[str, bytes]) -> dict[str, str]:
    return {name: hashlib.sha256(data).hexdigest() for name, data in sorted(files.items())}


def installed_files(destination: Path) -> dict[str, bytes]:
    files = {}
    for path in destination.rglob("*"):
        if path.is_symlink():
            raise InstallError("The installed skill contains a symlink; preserve and inspect it first.")
        if path.is_file() and path != destination / RECEIPT:
            files[path.relative_to(destination).as_posix()] = path.read_bytes()
        elif not path.is_file() and not path.is_dir():
            raise InstallError("The installed skill contains an unsupported file type.")
    return files


def load_receipt(destination: Path) -> dict:
    if destination.is_symlink():
        raise InstallError("The destination is a symlink. Update it through its original installation method.")
    path = destination / RECEIPT
    if not path.is_file() or path.is_symlink():
        raise InstallError("This skill is not managed by this Python tool. Use its original installer to update it.")
    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
        valid = (isinstance(receipt, dict) and receipt.get("format") == 1
                 and receipt.get("repository") == REPOSITORY
                 and isinstance(receipt.get("ref"), str) and receipt["ref"]
                 and isinstance(receipt.get("files"), dict))
    except (ValueError, UnicodeError):
        valid = False
    if not valid:
        raise InstallError("The installation receipt is invalid; preserve and inspect this installation.")
    if hashes(installed_files(destination)) != receipt["files"]:
        raise InstallError("The installed skill has local changes. Preserve them before updating.")
    return receipt


def install(action: str, skills_dir: Path, ref: str | None = None) -> str:
    destination = skills_dir.expanduser().absolute() / "pls"
    previous = None
    if action == "install":
        if destination.exists() or destination.is_symlink():
            raise InstallError(f"Destination already exists: {destination}. Use update for a managed installation.")
    else:
        previous = load_receipt(destination)
    selected_ref = ref if ref is not None else (previous["ref"] if previous else "main")
    if not selected_ref.strip():
        raise InstallError("The Git ref must not be empty.")
    commit, files = fetch_skill(selected_ref)
    receipt = {"format": 1, "repository": REPOSITORY, "ref": selected_ref,
               "commit": commit, "files": hashes(files)}
    if previous == receipt:
        return f"PLS is already up to date at {commit} ({selected_ref})."

    destination.parent.mkdir(parents=True, exist_ok=True)
    # Stage on the destination filesystem. Keep the old directory until the
    # complete replacement is ready, and restore it if publication fails.
    with tempfile.TemporaryDirectory(prefix=".pls-stage-", dir=destination.parent) as temporary:
        stage = Path(temporary) / "pls"
        stage.mkdir()
        for name, data in files.items():
            path = stage / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        (stage / RECEIPT).write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        if previous is not None:
            if load_receipt(destination) != previous:
                raise InstallError("The installed skill changed during the download. Retry after checking it.")
            # The backup stays outside the temporary folder until publication
            # succeeds, so even a failed restore leaves the original recoverable.
            backup = destination.parent / (Path(temporary).name + "-previous")
            destination.rename(backup)
            try:
                stage.rename(destination)
            except OSError:
                try:
                    backup.rename(destination)
                except OSError as restore_error:
                    raise InstallError(f"Replacement failed. Original skill is preserved at {backup}.") from restore_error
                raise
            backup.rename(Path(temporary) / "previous")
        else:
            # A concurrent install or newly created local directory must not
            # be overwritten, even when it is empty.
            if destination.exists() or destination.is_symlink():
                raise InstallError(f"Destination was created during the download: {destination}.")
            stage.rename(destination)
    return f"PLS {'installed' if previous is None else 'updated'} in {destination}\nGit ref: {selected_ref}\nCommit: {commit}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("install", "update"))
    parser.add_argument("--dest", type=Path, default=Path.cwd() / ".agents" / "skills",
                        help="skills directory (default: .agents/skills in the current directory)")
    parser.add_argument("--ref", help="Git branch, tag, or commit (install: main; update: saved ref)")
    args = parser.parse_args(argv)
    try:
        print(install(args.action, args.dest, args.ref))
    except (InstallError, OSError, URLError, ValueError, zipfile.BadZipFile) as error:
        print(f"PLS: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
