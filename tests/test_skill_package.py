import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock


class SkillPackageTests(unittest.TestCase):
    def make_skill(self, root: Path, name="context-aware-humanizer"):
        (root / "references" / "chat").mkdir(parents=True)
        (root / "scripts").mkdir()
        (root / "templates").mkdir()
        (root / "SKILL.md").write_text(
            f"---\nname: {name}\n---\n# Skill\n", encoding="utf-8"
        )
        (root / "README.md").write_text("readme", encoding="utf-8")
        (root / "references" / "chat" / "en.md").write_text("guide", encoding="utf-8")
        (root / "scripts" / "runtime.py").write_text("runtime = 1\n", encoding="utf-8")
        (root / "templates" / "style-memory.md").write_text("template", encoding="utf-8")

    def copy_cli(self, root: Path):
        scripts = root / "scripts"
        source_scripts = Path(__file__).parents[1] / "scripts"
        shutil.copy2(source_scripts / "skill_package.py", scripts / "skill_package.py")
        shutil.copy2(source_scripts / "style_memory.py", scripts / "style_memory.py")

    def run_cli(self, root: Path, *args):
        return subprocess.run(
            [sys.executable, str(root / "scripts" / "skill_package.py"), *args],
            cwd=str(root), text=True, capture_output=True,
        )

    def test_public_export_excludes_private_and_unlisted_files(self):
        from scripts.skill_package import export_skill

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "skill"
            root.mkdir()
            self.make_skill(root)
            (root / ".github").mkdir()
            (root / ".github" / "banner.png").write_bytes(b"png")
            (root / ".github" / "secret.txt").write_text("private", encoding="utf-8")
            (root / "memory" / "zh").mkdir(parents=True)
            (root / "memory" / "zh" / "chat.md").write_text("private", encoding="utf-8")
            (root / ".local").mkdir()
            (root / ".local" / "note").write_text("local", encoding="utf-8")
            (root / "secret.txt").write_text("secret", encoding="utf-8")
            output = Path(temp) / "public.zip"
            result = export_skill(root, output)
            self.assertTrue(result["created"])
            with zipfile.ZipFile(output) as archive:
                names = set(archive.namelist())
            self.assertIn("SKILL.md", names)
            self.assertIn("references/chat/en.md", names)
            self.assertIn(".github/banner.png", names)
            self.assertNotIn(".github/secret.txt", names)
            self.assertNotIn("memory/zh/chat.md", names)
            self.assertNotIn(".local/note", names)
            self.assertNotIn("secret.txt", names)

    def test_private_backup_includes_memory_but_excludes_lock_and_temp(self):
        from scripts.skill_package import export_skill

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "skill"
            root.mkdir()
            self.make_skill(root)
            memory = root / "memory"
            (memory / ".backups").mkdir(parents=True)
            (memory / "zh").mkdir()
            (memory / "zh" / "chat.md").write_text("private", encoding="utf-8")
            (memory / ".backups" / "old.md").write_text("old", encoding="utf-8")
            (memory / ".chat.md.tmp-1").write_text("temp", encoding="utf-8")
            output = Path(temp) / "private.zip"
            export_skill(root, output, include_memory=True)
            with zipfile.ZipFile(output) as archive:
                names = set(archive.namelist())
            self.assertIn("memory/zh/chat.md", names)
            self.assertIn("memory/.backups/old.md", names)
            self.assertNotIn("memory/.write.lock", names)
            self.assertNotIn("memory/.chat.md.tmp-1", names)

    def test_export_rejects_existing_or_nested_output(self):
        from scripts.skill_package import export_skill

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "skill"
            root.mkdir()
            self.make_skill(root)
            existing = Path(temp) / "existing.zip"
            existing.write_bytes(b"keep")
            with self.assertRaises(FileExistsError):
                export_skill(root, existing)
            with self.assertRaises(ValueError):
                export_skill(root, root / "nested.zip")

    def test_update_preserves_memory_and_backs_up_overwritten_program_files(self):
        from scripts.skill_package import update_skill

        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "target"
            source = Path(temp) / "source"
            target.mkdir(); source.mkdir()
            self.make_skill(target); self.make_skill(source)
            (target / "scripts" / "runtime.py").write_text("old\n", encoding="utf-8")
            (source / "scripts" / "runtime.py").write_text("new\n", encoding="utf-8")
            (target / "memory" / "zh").mkdir(parents=True)
            memory_file = target / "memory" / "zh" / "chat.md"
            memory_file.write_text("keep", encoding="utf-8")
            result = update_skill(target, source)
            self.assertEqual((target / "scripts" / "runtime.py").read_text(), "new\n")
            self.assertEqual(memory_file.read_text(), "keep")
            self.assertTrue(result["preserved_memory"])
            backups = list((target / ".local" / "updates").rglob("runtime.py"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(), "old\n")

    def test_update_rejects_wrong_identity_without_mutation(self):
        from scripts.skill_package import update_skill

        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "target"; source = Path(temp) / "source"
            target.mkdir(); source.mkdir()
            self.make_skill(target, "same")
            self.make_skill(source, "different")
            original = (target / "scripts" / "runtime.py").read_bytes()
            with self.assertRaises(ValueError):
                update_skill(target, source)
            self.assertEqual((target / "scripts" / "runtime.py").read_bytes(), original)

    def test_update_rejects_unclosed_source_frontmatter_without_mutation(self):
        from scripts.skill_package import update_skill

        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "target"; source = Path(temp) / "source"
            target.mkdir(); source.mkdir()
            self.make_skill(target); self.make_skill(source)
            (source / "SKILL.md").write_text("---\nname: context-aware-humanizer\n", encoding="utf-8")
            original = (target / "scripts" / "runtime.py").read_bytes()
            with self.assertRaises(ValueError):
                update_skill(target, source)
            self.assertEqual((target / "scripts" / "runtime.py").read_bytes(), original)

    def test_update_preflights_updates_directory_before_any_copy(self):
        from scripts.skill_package import update_skill

        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "target"; source = Path(temp) / "source"
            target.mkdir(); source.mkdir()
            self.make_skill(target); self.make_skill(source)
            (source / ".gitignore").write_text("generated\n", encoding="utf-8")
            (target / ".local").mkdir()
            (target / ".local" / "updates").write_text("not-a-directory", encoding="utf-8")
            original = (target / "scripts" / "runtime.py").read_bytes()
            with self.assertRaises(ValueError):
                update_skill(target, source)
            self.assertEqual((target / "scripts" / "runtime.py").read_bytes(), original)
            self.assertFalse((target / ".gitignore").exists())

    def test_update_atomic_replace_failure_retains_old_target_bytes(self):
        from scripts.skill_package import update_skill

        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "target"; source = Path(temp) / "source"
            target.mkdir(); source.mkdir()
            self.make_skill(target); self.make_skill(source)
            (target / "scripts" / "runtime.py").write_text("old\n", encoding="utf-8")
            (source / "scripts" / "runtime.py").write_text("new\n", encoding="utf-8")
            with mock.patch("scripts.skill_package.os.replace", side_effect=OSError("injected replace failure")):
                with self.assertRaises(OSError):
                    update_skill(target, source)
            self.assertEqual((target / "scripts" / "runtime.py").read_text(), "old\n")

    def test_export_rejects_symlink_in_maintained_tree(self):
        from scripts.skill_package import export_skill

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "skill"; root.mkdir()
            self.make_skill(root)
            external = Path(temp) / "outside.md"; external.write_text("outside", encoding="utf-8")
            (root / "references" / "chat" / "link.md").symlink_to(external)
            with self.assertRaises(ValueError):
                export_skill(root, Path(temp) / "out.zip")

    def test_export_rejects_symlinked_maintained_parent(self):
        from scripts.skill_package import export_skill

        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "skill"; root.mkdir()
            self.make_skill(root)
            external = base / "external"; external.mkdir()
            (external / "banner.png").write_bytes(b"outside")
            shutil.rmtree(root / ".github", ignore_errors=True)
            (root / ".github").symlink_to(external, target_is_directory=True)
            with self.assertRaises(ValueError):
                export_skill(root, base / "out.zip")

    def test_cli_export_backup_and_update_use_real_script_entrypoint(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            target = base / "target"; source = base / "source"
            target.mkdir(); source.mkdir()
            self.make_skill(target); self.make_skill(source)
            self.copy_cli(target)
            (target / "memory" / "zh").mkdir(parents=True)
            (target / "memory" / "zh" / "chat.md").write_text("private", encoding="utf-8")
            public = base / "public.zip"; private = base / "private.zip"
            exported = self.run_cli(target, "export", "--output", str(public))
            self.assertEqual(exported.returncode, 0, exported.stderr)
            self.assertEqual(json.loads(exported.stdout)["created"], str(public))
            backed = self.run_cli(target, "backup", "--output", str(private))
            self.assertEqual(backed.returncode, 0, backed.stderr)
            with zipfile.ZipFile(private) as archive:
                self.assertIn("memory/zh/chat.md", archive.namelist())
            (source / "scripts" / "runtime.py").write_text("changed\n", encoding="utf-8")
            updated = self.run_cli(target, "update", "--source", str(source))
            self.assertEqual(updated.returncode, 0, updated.stderr)

    def test_cli_lock_conflict_returns_json_error_without_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "skill"; root.mkdir()
            self.make_skill(root); self.copy_cli(root)
            memory = root / "memory"; memory.mkdir()
            (memory / ".write.lock").write_text("held", encoding="utf-8")
            output = Path(temp) / "private.zip"
            result = self.run_cli(root, "backup", "--output", str(output))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("locked", json.loads(result.stderr)["error"])
            self.assertNotIn("Traceback", result.stderr)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
