"""Checks for the self-contained PLS release bundle builder."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_release", ROOT / "tools" / "build_release.py")
builder = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(builder)

COMMIT = "0123456789abcdef" * 2 + "01234567"
VERSION = "0.3.0-draft.3"


class ReleaseBundleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "project"
        (self.root / "src" / "pls" / "references").mkdir(parents=True)
        (self.root / "tools").mkdir()
        (self.root / "src" / "pls" / "SKILL.md").write_text(
            "---\nname: pls\n---\n\n# Use PLS\n", encoding="utf-8"
        )
        (self.root / "src" / "pls" / "references" / "PLS.md").write_text(
            "---\nversion: 0.3.0\nstatus: working\n---\n\n# PLS\n",
            encoding="utf-8",
        )
        (self.root / "src" / "pls" / "references" / "guide.md").write_text(
            "Bundled guidance.\n", encoding="utf-8"
        )
        (self.root / "src" / "design-writing" / "references").mkdir(parents=True)
        (self.root / "src" / "design-writing" / "SKILL.md").write_text(
            "---\nname: design-writing\n---\n\n# Design writing\n", encoding="utf-8"
        )
        (self.root / "src" / "design-writing" / "references" / "design-writing.md").write_bytes(
            "# Design writing\r\n\r\nWrite the user's goal → operating behavior.\r\n".encode("utf-8")
        )
        (self.root / "tools" / "pls_skill.py").write_text(
            "#!/usr/bin/env python3\nprint('installer')\n", encoding="utf-8"
        )
        (self.root / "LICENSE").write_text("MIT License\n", encoding="utf-8")
        self.output = Path(self.temporary.name) / "releases" / VERSION

    def build(self, output=None, version=VERSION, commit=COMMIT):
        return builder.build_release(self.root, version, commit, output or self.output)

    def read_bundle(self, archive):
        with zipfile.ZipFile(archive) as bundle:
            return {info.filename: bundle.read(info) for info in bundle.infolist()}, bundle

    def test_payload_installer_license_instructions_and_metadata(self):
        archive, checksum = self.build()
        members, bundle = self.read_bundle(archive)
        expected = {
            "pls/LICENSE",
            "pls/README.md",
            "pls/install.py",
            "pls/release.json",
            "pls/skills/design-writing/SKILL.md",
            "pls/skills/design-writing/references/design-writing.md",
            "pls/skills/pls/SKILL.md",
            "pls/skills/pls/references/PLS.md",
            "pls/skills/pls/references/guide.md",
        }
        self.assertEqual(set(members), expected)
        self.assertEqual(list(members), sorted(members))
        self.assertTrue(all(name.startswith("pls/") for name in members))
        for skill in ("pls", "design-writing"):
            source = self.root / "src" / skill
            for path in source.rglob("*"):
                if path.is_file():
                    member = f"pls/skills/{skill}/{path.relative_to(source).as_posix()}"
                    self.assertEqual(members[member], path.read_bytes(), member)
        self.assertEqual(members["pls/install.py"], (self.root / "tools" / "pls_skill.py").read_bytes())
        self.assertEqual(members["pls/LICENSE"], b"MIT License\n")
        readme = members["pls/README.md"].decode("utf-8")
        for phrase in (
            "python3 /path/to/pls/install.py install",
            "python3 /path/to/pls/install.py install --skill design-writing",
            "`.agents/skills/design-writing/`",
            "default command installs only `pls`",
            "Updating one skill leaves the other",
            "python3 /absolute/path/to/project/.agents/skills/design-writing/install.py update",
            "--dest",
            "latest published bundle",
            "update --bundle /path/to/extracted/pls",
            "no PLS checkout, Node.js",
            "Human\nadoption",
        ):
            self.assertIn(phrase, readme)
        self.assertEqual(
            json.loads(members["pls/release.json"]),
            {
                "format": 1,
                "repository": "brightskye/pls",
                "version": VERSION,
                "commit": COMMIT,
            },
        )
        self.assertEqual(
            checksum.read_text(encoding="ascii"),
            f"{hashlib.sha256(archive.read_bytes()).hexdigest()}  pls.zip\n",
        )
        for info in bundle.infolist():
            self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
            self.assertFalse(stat.S_ISLNK(info.external_attr >> 16))

    def test_same_inputs_produce_same_zip_and_hash(self):
        first = self.build()
        for skill in ("pls", "design-writing"):
            path = self.root / "src" / skill / "SKILL.md"
            os.utime(path, (1_600_000_000, 1_600_000_000))
            path.chmod(0o744)
        second = self.build(output=Path(self.temporary.name) / "other" / VERSION)
        self.assertEqual(first[0].read_bytes(), second[0].read_bytes())
        self.assertEqual(first[1].read_bytes(), second[1].read_bytes())

    def test_empty_skill_is_not_packaged(self):
        (self.root / "src" / "pls" / "SKILL.md").write_bytes(b"")
        with self.assertRaisesRegex(builder.BundleError, "must contain"):
            self.build()
        self.assertFalse(self.output.exists())

    def test_companion_requires_its_skill_and_guide(self):
        for name in ("SKILL.md", "references/design-writing.md"):
            path = self.root / "src" / "design-writing" / name
            original = path.read_bytes()
            for content in (None, b""):
                with self.subTest(name=name, content=content):
                    if content is None:
                        path.unlink()
                    else:
                        path.write_bytes(content)
                    try:
                        with self.assertRaisesRegex(builder.BundleError, "design-writing skill must contain"):
                            self.build()
                        self.assertFalse(self.output.exists())
                    finally:
                        path.write_bytes(original)

    def test_missing_companion_directory_is_not_packaged(self):
        source = self.root / "src" / "design-writing"
        source.rename(source.with_name("companion-away"))
        with self.assertRaisesRegex(builder.BundleError, "Missing bundle source directory"):
            self.build()
        self.assertFalse(self.output.exists())

    def test_refuses_overwrite_and_preserves_existing_output(self):
        archive, checksum = self.build()
        before_archive = archive.read_bytes()
        before_checksum = checksum.read_bytes()
        with self.assertRaisesRegex(builder.BundleError, "already exists"):
            self.build()
        self.assertEqual(archive.read_bytes(), before_archive)
        self.assertEqual(checksum.read_bytes(), before_checksum)

    def test_release_version_matches_working_standard(self):
        for version in ("0.3.0", "0.3.1-draft.1", "v0.3.0-draft.1", "0.3.0-rc.1"):
            with self.subTest(version=version), self.assertRaises(builder.BundleError):
                self.build(version=version, output=Path(self.temporary.name) / version)

    def test_rejects_symlink_and_private_source_files(self):
        hidden = self.root / "src" / "pls" / ".private"
        hidden.write_text("secret", encoding="utf-8")
        with self.assertRaisesRegex(builder.BundleError, "private"):
            self.build(output=Path(self.temporary.name) / "private" / VERSION)
        hidden.unlink()
        link = self.root / "src" / "pls" / "link.md"
        try:
            link.symlink_to(self.root / "src" / "pls" / "SKILL.md")
        except (OSError, NotImplementedError):
            self.skipTest("symbolic links are unavailable")
        with self.assertRaisesRegex(builder.BundleError, "symlink"):
            self.build(output=Path(self.temporary.name) / "symlink" / VERSION)

    def test_rejects_private_and_cache_files_in_companion(self):
        source = self.root / "src" / "design-writing"
        for name, error in ((".private", "private"), ("__pycache__/cache.pyc", "cache")):
            with self.subTest(name=name):
                path = source / name
                path.parent.mkdir(exist_ok=True)
                path.write_bytes(b"not release content")
                try:
                    with self.assertRaisesRegex(builder.BundleError, error):
                        self.build()
                    self.assertFalse(self.output.exists())
                finally:
                    path.unlink()

    def test_rejects_companion_symlinks(self):
        source = self.root / "src" / "design-writing"
        link = source / "outside.md"
        try:
            link.symlink_to(self.root / "LICENSE")
        except (OSError, NotImplementedError):
            self.skipTest("symbolic links are unavailable")
        with self.assertRaisesRegex(builder.BundleError, "symlink"):
            self.build()
        self.assertFalse(self.output.exists())
        link.unlink()
        moved = source.with_name("companion-away")
        source.rename(moved)
        source.symlink_to(moved, target_is_directory=True)
        with self.assertRaisesRegex(builder.BundleError, "symlink"):
            self.build()
        self.assertFalse(self.output.exists())

    def test_cli_checkout_must_be_clean_but_direct_build_has_explicit_commit(self):
        with patch.object(builder, "_git_output", side_effect=[" M README.md", COMMIT]):
            with self.assertRaisesRegex(builder.BundleError, "clean Git checkout"):
                builder._checkout_commit(self.root)
        with patch.object(builder, "_git_output", side_effect=["", COMMIT]):
            self.assertEqual(builder._checkout_commit(self.root), COMMIT)
        archive, _ = self.build(output=Path(self.temporary.name) / "explicit" / VERSION)
        self.assertTrue(archive.is_file())


if __name__ == "__main__":
    unittest.main()
