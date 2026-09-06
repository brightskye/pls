"""Installer behavior, using real skill archives and isolated destinations."""

import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("pls_skill", ROOT / "tools" / "pls_skill.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)
FIRST = "a" * 40
SECOND = "b" * 40


def archive(files):
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as bundle:
        for name, content in files.items():
            bundle.writestr(name, content)
    return data.getvalue()


def release_archive(payload, version="0.3.0-draft.1", commit=FIRST):
    files = {"pls/skills/pls/" + name: data for name, data in payload.items()}
    files.update({"pls/install.py": b"# installer", "pls/README.md": b"Instructions",
                  "pls/LICENSE": b"MIT", "pls/release.json": json.dumps({
                      "format": 1, "repository": installer.REPOSITORY,
                      "version": version, "commit": commit}).encode()})
    return archive(files)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.project = Path(self.temporary.name)
        self.skills = self.project / ".agents" / "skills"
        self.destination = self.skills / "pls"
        self.payload = {
            "SKILL.md": (ROOT / "src" / "pls" / "SKILL.md").read_bytes(),
            "references/PLS.md": (ROOT / "src" / "pls" / "references" / "PLS.md").read_bytes(),
        }

    def run_install(self, action="install", ref=None, commit=FIRST, payload=None):
        with patch.object(installer, "fetch_skill", return_value=(commit, payload or self.payload)) as fetch:
            message = installer.install(action, self.skills, ref)
        return message, fetch.call_args.args[0]

    def receipt(self):
        return json.loads((self.destination / installer.RECEIPT).read_text())

    def test_install_only_skill_and_matching_receipt(self):
        marker = self.project / "README.md"
        marker.write_text("Project layout standard: PLS 0.2\n")
        self.run_install()
        for name, contents in self.payload.items():
            self.assertEqual((self.destination / name).read_bytes(), contents)
            self.assertEqual(self.receipt()["files"][name], hashlib.sha256(contents).hexdigest())
        self.assertEqual(self.receipt()["ref"], "main")
        self.assertEqual(self.receipt()["commit"], FIRST)
        self.assertEqual(marker.read_text(), "Project layout standard: PLS 0.2\n")

    def test_update_changes_both_files_and_keeps_selected_ref(self):
        self.run_install(ref="v0.3.0-test")
        changed = {name: contents + b"\nUpdated.\n" for name, contents in self.payload.items()}
        _, ref = self.run_install("update", commit=SECOND, payload=changed)
        self.assertEqual(ref, "v0.3.0-test")
        self.assertEqual(installer.installed_files(self.destination), changed)
        self.assertEqual(self.receipt()["commit"], SECOND)
        self.assertEqual(list(self.skills.iterdir()), [self.destination])

    def test_explicit_ref_change_and_unchanged_update(self):
        self.run_install(ref=FIRST)
        _, ref = self.run_install("update", ref="main", commit=SECOND)
        self.assertEqual(ref, "main")
        before = (self.destination / installer.RECEIPT).stat().st_mtime_ns
        message, _ = self.run_install("update", commit=SECOND)
        self.assertIn("already up to date", message)
        self.assertEqual((self.destination / installer.RECEIPT).stat().st_mtime_ns, before)

    def test_refuses_overwrite_and_unmanaged_update(self):
        self.destination.mkdir(parents=True)
        note = self.destination / "SKILL.md"
        note.write_text("Owner's skill")
        for action in ("install", "update"):
            with self.subTest(action=action), self.assertRaises(installer.InstallError):
                self.run_install(action)
        self.assertEqual(note.read_text(), "Owner's skill")

    def test_local_edits_added_files_and_missing_files_are_preserved(self):
        self.run_install()
        path = self.destination / "SKILL.md"
        original = path.read_bytes()
        path.write_bytes(b"Local edit")
        with self.assertRaisesRegex(installer.InstallError, "local changes"):
            self.run_install("update")
        self.assertEqual(path.read_bytes(), b"Local edit")
        path.write_bytes(original)
        added = self.destination / "references" / installer.RECEIPT
        added.write_text("Local note")
        with self.assertRaisesRegex(installer.InstallError, "local changes"):
            self.run_install("update")
        added.unlink()
        path.unlink()
        with self.assertRaisesRegex(installer.InstallError, "local changes"):
            self.run_install("update")

    def test_refuses_symlink_destination(self):
        target = self.project / "source"
        target.mkdir()
        self.skills.mkdir(parents=True)
        self.destination.symlink_to(target, target_is_directory=True)
        for action in ("install", "update"):
            with self.subTest(action=action), self.assertRaises(installer.InstallError):
                self.run_install(action)
        self.assertTrue(self.destination.is_symlink())
        self.assertEqual(list(target.iterdir()), [])

    def test_failed_download_keeps_installation(self):
        self.run_install()
        before = self.receipt()
        with patch.object(installer, "fetch_skill", side_effect=URLError("offline")):
            with self.assertRaises(URLError):
                installer.install("update", self.skills)
        self.assertEqual(self.receipt(), before)
        self.assertEqual(installer.installed_files(self.destination), self.payload)

    def test_failed_replacement_restores_installation(self):
        self.run_install()
        real_rename = Path.rename

        def fail_replacement(path, target):
            if path.parent.name.startswith(".pls-stage-") and path.name == "pls":
                raise OSError("simulated publish failure")
            return real_rename(path, target)

        with patch.object(Path, "rename", fail_replacement):
            with self.assertRaisesRegex(OSError, "simulated publish failure"):
                self.run_install("update", commit=SECOND)
        self.assertEqual(self.receipt()["commit"], FIRST)
        self.assertEqual(installer.installed_files(self.destination), self.payload)

    def test_download_resolves_ref_and_extracts_only_skill(self):
        files = {"pls-sha/src/pls/" + name: data for name, data in self.payload.items()}
        files["pls-sha/README.md"] = b"Repository docs"
        with patch.object(installer, "download", side_effect=[
            json.dumps({"sha": FIRST}).encode(), archive(files)
        ]) as download:
            commit, payload = installer.fetch_skill("feature/rules")
        self.assertEqual(commit, FIRST)
        self.assertEqual(payload, self.payload)
        self.assertTrue(download.call_args_list[0].args[0].endswith("feature%2Frules"))
        self.assertTrue(download.call_args_list[1].args[0].endswith(FIRST))

    def test_rejects_incomplete_or_unsafe_archives(self):
        base = {"pls-sha/src/pls/" + name: data for name, data in self.payload.items()}
        for name in ("../../outside", "/outside", "folder\\outside", installer.RECEIPT,
                     "./SKILL.md", "references//PLS.md"):
            with self.subTest(name=name), self.assertRaises(installer.InstallError):
                installer.read_skill(archive({**base, "pls-sha/src/pls/" + name: b"bad"}))
        with self.assertRaisesRegex(installer.InstallError, "complete"):
            installer.read_skill(archive({"pls-sha/src/pls/SKILL.md": b"Incomplete"}))
        data = io.BytesIO()
        with zipfile.ZipFile(data, "w") as bundle:
            link = zipfile.ZipInfo("pls-sha/src/pls/link")
            link.create_system = 3
            link.external_attr = (stat.S_IFLNK | 0o777) << 16
            bundle.writestr(link, "../../outside")
        with self.assertRaisesRegex(installer.InstallError, "unsafe"):
            installer.read_skill(data.getvalue())

    def test_cli_default_destination_and_error_status(self):
        with patch.object(Path, "cwd", return_value=self.project):
            with patch.object(installer, "fetch_skill", return_value=(FIRST, self.payload)):
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(installer.main(["install"]), 0)
            with contextlib.redirect_stderr(io.StringIO()) as error:
                self.assertEqual(installer.main(["install"]), 1)
        self.assertIn("already exists", error.getvalue())
        self.assertTrue(self.destination.is_dir())

    def test_bundle_install_is_offline_and_updates_use_release_bundles(self):
        bundle = self.project / "pls.zip"
        bundle.write_bytes(release_archive(self.payload))
        with patch.object(installer, "download", side_effect=AssertionError("offline install used network")):
            installer.install("install", self.skills, bundle=bundle)
        self.assertEqual(self.receipt()["source"], "bundle")
        self.assertEqual(self.receipt()["release_ref"], "latest")
        self.assertEqual(installer.installed_files(self.destination), self.payload)
        changed = {name: data + b"\nNew release.\n" for name, data in self.payload.items()}
        metadata, files = installer.read_bundle(release_archive(changed, "0.3.0-draft.2", SECOND))
        with patch.object(installer, "fetch_release", return_value=(metadata, files)) as fetch:
            with patch.object(installer, "fetch_skill", side_effect=AssertionError("release update read Git source")):
                installer.install("update", self.skills)
        fetch.assert_called_once_with("latest")
        self.assertEqual(self.receipt()["version"], "0.3.0-draft.2")
        self.assertEqual(installer.installed_files(self.destination), changed)

    def test_pinned_release_stays_pinned_and_offline_update_works(self):
        metadata, files = installer.read_bundle(release_archive(self.payload))
        with patch.object(installer, "fetch_release", return_value=(metadata, files)) as fetch:
            installer.install("install", self.skills, release="v0.3.0-draft.1")
            installer.install("update", self.skills)
        self.assertEqual([call.args[0] for call in fetch.call_args_list], ["v0.3.0-draft.1"] * 2)
        bundle = self.project / "pls.zip"
        bundle.write_bytes(release_archive(self.payload, "0.3.0-draft.2", SECOND))
        with patch.object(installer, "download", side_effect=AssertionError("offline update used network")):
            installer.install("update", self.skills, bundle=bundle)
        self.assertEqual(self.receipt()["version"], "0.3.0-draft.2")
        self.assertEqual(self.receipt()["release_ref"], "v0.3.0-draft.2")

    def test_release_download_checks_checksum_and_uses_published_bundle(self):
        package = release_archive(self.payload)
        checksum = (hashlib.sha256(package).hexdigest() + "  pls.zip\n").encode()
        releases = [{"draft": True, "published_at": "2026-09-07", "tag_name": "v0.3.0-draft.9", "assets": [{"name": "pls.zip"}]},
                    {"draft": False, "prerelease": True, "published_at": "2026-09-06", "tag_name": "v0.3.0-draft.1", "assets": [{"name": "pls.zip"}]}]
        with patch.object(installer, "download", side_effect=[json.dumps(releases).encode(), package, checksum]) as download:
            metadata, files = installer.fetch_release("latest")
        self.assertEqual(metadata["version"], "0.3.0-draft.1")
        self.assertEqual(files, self.payload)
        self.assertIn("/releases/download/v0.3.0-draft.1/pls.zip", download.call_args_list[1].args[0])
        with patch.object(installer, "download", side_effect=[package, b"wrong checksum"]):
            with self.assertRaisesRegex(installer.InstallError, "checksum"):
                installer.fetch_release("v0.3.0-draft.1")

    def test_bundle_validation_and_local_edits_preserved(self):
        bundle = self.project / "pls.zip"
        bundle.write_bytes(release_archive(self.payload))
        installer.install("install", self.skills, bundle=bundle)
        skill = self.destination / "SKILL.md"
        skill.write_text("Local changes")
        with self.assertRaisesRegex(installer.InstallError, "local changes"):
            installer.install("update", self.skills, bundle=bundle)
        self.assertEqual(skill.read_text(), "Local changes")
        for payload in [b"{}", b"[]", b'{"format": 2}']:
            with self.assertRaises(installer.InstallError):
                installer.bundle_metadata(payload)
        with self.assertRaises(installer.InstallError):
            installer.read_bundle(archive({"pls/release.json": b"{}"}))


if __name__ == "__main__":
    unittest.main()
