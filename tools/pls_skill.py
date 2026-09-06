#!/usr/bin/env python3
"""Install or update the public PLS skill with Python 3.10+ and no dependencies.

The default installation is .agents/skills/pls in the current project. It
contains the skill, rules, installer, and release information. Run its installed
install.py to update that same directory from published release bundles.
--bundle selects an offline bundle and --release pins a published release.
--ref retains the development-only Git source route. Local edits are preserved.
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
BUNDLE_FILES = ("release.json", "install.py", "README.md", "LICENSE")


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


def read_skill(archive: bytes, skill_path: str = SKILL_PATH) -> dict[str, bytes]:
    """Read only the self-contained skill; never extract repository paths."""
    files = {}
    total_size = 0
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for entry in bundle.infolist():
            parts = entry.filename.split("/")
            if parts[1:3] != skill_path.split("/"):
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
        raise InstallError(f"This revision does not contain a complete {skill_path} skill.")
    return files


def bundle_metadata(data: bytes) -> dict:
    metadata = json.loads(data)
    if (not isinstance(metadata, dict) or metadata.get("format") != 1
            or metadata.get("repository") != REPOSITORY
            or not re.fullmatch(r"[0-9a-f]{40}", str(metadata.get("commit", "")))
            or not re.fullmatch(r"\d+\.\d+\.\d+(?:-[a-z0-9.]+)?", str(metadata.get("version", "")))):
        raise InstallError("Invalid PLS release metadata.")
    return metadata


def read_bundle(archive: bytes) -> tuple[dict, dict[str, bytes]]:
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        roots = {entry.filename.split("/", 1)[0] for entry in bundle.infolist()}
        if len(roots) != 1 or not next(iter(roots)):
            raise InstallError("The release bundle must have one root folder.")
        prefix = next(iter(roots)) + "/"
        support = {}
        for name in BUNDLE_FILES:
            if bundle.namelist().count(prefix + name) != 1:
                raise InstallError(f"The release bundle needs exactly one {name} file.")
            entry = bundle.getinfo(prefix + name)
            if (stat.S_ISLNK(entry.external_attr >> 16) or entry.is_dir()
                    or not 0 < entry.file_size <= MAX_DOWNLOAD):
                raise InstallError(f"The release bundle needs a regular, nonempty {name} file.")
            support[name] = bundle.read(entry)
        if bundle.getinfo(prefix + "release.json").file_size > 16384:
            raise InstallError("Release metadata is too large.")
        metadata = bundle_metadata(support["release.json"])
    return metadata, complete_payload(read_skill(archive, "skills/pls"), support)


def complete_payload(skill: dict[str, bytes], support: dict[str, bytes]) -> dict[str, bytes]:
    if skill.keys() & support.keys():
        raise InstallError("The skill contains a reserved installer or release file.")
    files = {**skill, **support}
    if sum(map(len, files.values())) > MAX_DOWNLOAD:
        raise InstallError("The complete release exceeds the installation size limit.")
    return files


def load_bundle(path: Path) -> tuple[dict, dict[str, bytes]]:
    path = path.expanduser()
    if path.is_symlink() or (path / "skills").is_symlink():
        raise InstallError("The release bundle must not redirect to linked directories.")
    if path.is_file():
        if path.stat().st_size > MAX_DOWNLOAD:
            raise InstallError("The release bundle exceeds the 20 MiB limit.")
        return read_bundle(path.read_bytes())
    for name in BUNDLE_FILES:
        if not (path / name).is_file() or (path / name).is_symlink():
            raise InstallError(f"The release bundle is missing a regular {name} file.")
        if not 0 < (path / name).stat().st_size <= MAX_DOWNLOAD:
            raise InstallError(f"The release bundle has an empty or oversized {name} file.")
    metadata = bundle_metadata((path / "release.json").read_bytes())
    if (path / RECEIPT).exists():
        load_receipt(path)
        return metadata, installed_files(path)
    skill = path / "skills" / "pls"
    if skill.is_symlink() or not skill.is_dir():
        raise InstallError("The release bundle needs a regular skills/pls directory.")
    files = installed_files(skill)
    if not files.get("SKILL.md") or not files.get("references/PLS.md"):
        raise InstallError("The release bundle contains an incomplete PLS skill.")
    support = {name: (path / name).read_bytes() for name in BUNDLE_FILES}
    return metadata, complete_payload(files, support)


def fetch_release(selection: str) -> tuple[dict, dict[str, bytes]]:
    if selection == "latest":
        releases = json.loads(download(f"https://api.github.com/repos/{REPOSITORY}/releases?per_page=100"))
        candidates = [release for release in releases if not release.get("draft")
                      and any(asset.get("name") == "pls.zip" for asset in release.get("assets", []))]
        if not candidates:
            raise InstallError("No published PLS release bundles are available.")
        release = max(candidates, key=lambda item: item.get("published_at") or "")
        tag = release["tag_name"]
    else:
        tag = selection
    if not re.fullmatch(r"v\d+\.\d+\.\d+(?:-[a-z0-9.]+)?", tag):
        raise InstallError("Use a PLS release tag such as v0.3.0-draft.1, or latest.")
    base = f"https://github.com/{REPOSITORY}/releases/download/{quote(tag, safe='')}/"
    archive = download(base + "pls.zip")
    checksum = download(base + "pls.zip.sha256").decode("ascii").split()
    if not checksum or checksum[0] != hashlib.sha256(archive).hexdigest():
        raise InstallError("The downloaded release bundle failed its checksum check.")
    metadata, files = read_bundle(archive)
    if metadata["version"] != tag[1:]:
        raise InstallError("The release bundle version does not match its GitHub tag.")
    return metadata, files


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


def install(action: str, skills_dir: Path, ref: str | None = None,
            bundle: Path | None = None, release: str | None = None) -> str:
    destination = skills_dir.expanduser().absolute() / "pls"
    previous = None
    if action == "install":
        if destination.exists() or destination.is_symlink():
            raise InstallError(f"Destination already exists: {destination}. Use update for a managed installation.")
    else:
        previous = load_receipt(destination)
    bundled_root = Path(__file__).resolve().parent
    selection = release or (previous.get("release_ref", "latest") if previous else "latest")
    use_releases = release is not None or (previous and previous.get("source") == "bundle" and ref is None)
    metadata = None
    if bundle is not None:
        metadata, files = load_bundle(bundle)
    elif use_releases:
        metadata, files = fetch_release(selection)
    elif ref is None and (bundled_root / "release.json").is_file():
        metadata, files = load_bundle(bundled_root)
    else:
        selected_ref = ref if ref is not None else (previous["ref"] if previous else "main")
        if not selected_ref.strip():
            raise InstallError("The Git ref must not be empty.")
        commit, files = fetch_skill(selected_ref)
    if metadata is not None:
        selected_ref = "v" + metadata["version"]
        commit = metadata["commit"]
        if bundle is not None and selection != "latest":
            selection = selected_ref
    receipt = {"format": 1, "repository": REPOSITORY, "ref": selected_ref,
               "commit": commit, "files": hashes(files)}
    if metadata is not None:
        receipt.update(source="bundle", version=metadata["version"], release_ref=selection)
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
    return f"PLS {'installed' if previous is None else 'updated'} in {destination}\nVersion/ref: {selected_ref}\nCommit: {commit}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("install", "update"))
    parser.add_argument("--dest", type=Path,
                        help="parent skills directory (install: current project's .agents/skills; installed update: this copy)")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--bundle", type=Path, help="install/update from an extracted bundle or ZIP without network access")
    source.add_argument("--release", help="published release tag, or latest (includes published working drafts)")
    source.add_argument("--ref", help="development Git source: branch, tag, or commit")
    args = parser.parse_args(argv)
    skills_dir = args.dest
    if skills_dir is None:
        script_dir = Path(__file__).absolute().parent
        if args.action == "update" and ((script_dir / RECEIPT).exists()
                                        or (script_dir / "SKILL.md").is_file()):
            skills_dir = script_dir.parent
        else:
            skills_dir = Path.cwd() / ".agents" / "skills"
    try:
        print(install(args.action, skills_dir, args.ref, args.bundle, args.release))
    except (InstallError, OSError, URLError, ValueError, zipfile.BadZipFile) as error:
        print(f"PLS: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
