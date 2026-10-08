import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from style_memory import MemoryError, MemoryStore


def profile(language='zh', scenario='chat', body='Prefer concise sentences.'):
    return f'---\nschema_version: 1\nlanguage: {language}\nscenario: {scenario}\n---\n# Style\n\n{body}\n'


class MemoryStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.skill = Path(self.temp.name)
        self.store = MemoryStore(self.skill)

    def save(self, language='zh', scenario='chat', body='Prefer concise sentences.', revision='missing'):
        return self.store.save(language, scenario, profile(language, scenario, body), revision)

    def test_missing_read_is_read_only(self):
        result = self.store.read('zh', 'chat')
        self.assertEqual(result['profiles'], [])
        self.assertEqual(result['target_revision'], 'missing')
        self.assertFalse(self.store.root.exists())

    def test_reads_only_same_language_common_and_exact_scope(self):
        self.save('zh', 'common', 'Common preference')
        exact = self.save('zh', 'chat', 'Chat preference')
        self.save('zh', 'academic-paper', 'Unrelated Chinese paper')
        self.save('en', 'chat', 'Unrelated English chat')
        result = self.store.read('zh', 'chat')
        self.assertEqual([p['scope'] for p in result['profiles']], ['common', 'chat'])
        self.assertEqual(result['target_revision'], exact['revision'])
        self.assertNotIn('Unrelated', str(result))
        self.assertEqual([p['scope'] for p in self.store.read('zh', 'unlisted')['profiles']], ['common'])
        self.assertEqual(len(self.store.read('zh', 'common')['profiles']), 1)

    def test_save_verifies_bytes_and_backs_up_prior_revision(self):
        first = self.save(body='Old preference')
        previous = Path(first['path']).read_bytes()
        second = self.save(body='New preference', revision=first['revision'])
        self.assertTrue(second['saved'])
        self.assertEqual(Path(second['backup']).read_bytes(), previous)
        self.assertEqual(second['revision'], hashlib.sha256(Path(second['path']).read_bytes()).hexdigest())
        self.assertIn('New preference', self.store.read('zh', 'chat')['profiles'][0]['content'])
        self.assertIn('zh/chat.md', (self.store.root / 'index.md').read_text())
        self.assertFalse((self.store.root / '.write.lock').exists())

    def test_stale_writer_and_create_collision_do_not_overwrite(self):
        first = self.save()
        second = self.save(body='A second writer', revision=first['revision'])
        for stale in ['missing', first['revision']]:
            with self.assertRaisesRegex(MemoryError, '[Cc]onflict|revision'):
                self.save(body='Stale writer', revision=stale)
        self.assertEqual(Path(second['path']).read_text(), profile(body='A second writer'))
        self.assertEqual(len(list((self.store.root / '.backups').rglob('*.md'))), 1)

    def test_invalid_metadata_scope_and_content_make_no_files(self):
        invalid = [
            ('zh', 'chat', profile('en', 'chat')),
            ('zh', 'chat', profile('zh', 'work-message')),
            ('zh', 'unknown', profile('zh', 'unknown')),
            ('zh', '../chat', profile()),
            ('fr', 'chat', profile('fr', 'chat')),
            ('zh', 'chat', profile().replace('schema_version: 1', 'schema_version: 2')),
            ('zh', 'chat', profile().replace('language: zh', 'language: zh\nlanguage: en')),
            ('zh', 'chat', profile().replace('language: zh', 'language: zh\nextra: value')),
            ('zh', 'chat', '---\nschema_version: 1\nlanguage: zh\nscenario: chat\n---\n'),
            ('zh', 'chat', profile(body='x' * 65536)),
        ]
        for language, scenario, content in invalid:
            with self.subTest(language=language, scenario=scenario, content=content[:60]):
                with self.assertRaises(MemoryError):
                    self.store.save(language, scenario, content, 'missing')
        with self.assertRaises(MemoryError):
            self.save(revision='anything')
        self.assertFalse(self.store.root.exists())

    def test_lock_rejects_another_writer_and_preserves_owner(self):
        with self.store.lock():
            lock = self.store.root / '.write.lock'
            owner = lock.read_bytes()
            with self.assertRaisesRegex(MemoryError, '[Ll]ock'):
                self.save()
            self.assertEqual(lock.read_bytes(), owner)
        self.save()

    def test_lock_initialization_failure_cleans_up_owned_lock(self):
        for failure in ('os.fdopen', 'os.fsync'):
            with self.subTest(failure=failure):
                with mock.patch('style_memory.' + failure, side_effect=OSError('injected initialization failure')):
                    with self.assertRaises(MemoryError):
                        self.save()
                self.assertFalse((self.store.root / '.write.lock').exists())
        self.save()

    @unittest.skipIf(sys.platform == 'win32', 'POSIX directory modes')
    def test_save_makes_existing_private_directories_owner_only(self):
        self.store.root.mkdir(mode=0o755)
        (self.store.root / 'zh').mkdir(mode=0o755)
        first = self.save()
        second = self.save(body='Updated', revision=first['revision'])
        for directory in [self.store.root, self.store.root / 'zh', Path(second['backup']).parent]:
            self.assertEqual(directory.stat().st_mode & 0o777, 0o700)

    def test_failed_atomic_replace_retains_old_profile(self):
        first = self.save(body='Old content')
        with mock.patch('style_memory.os.replace', side_effect=OSError('injected replace failure')):
            with self.assertRaises(MemoryError):
                self.save(body='New content', revision=first['revision'])
        self.assertEqual(Path(first['path']).read_text(), profile(body='Old content'))
        self.assertFalse((self.store.root / '.write.lock').exists())
        self.assertEqual(list(self.store.root.rglob('*.tmp')), [])

    def test_backup_failure_keeps_old_profile(self):
        first = self.save(body='Old content')
        (self.store.root / '.backups').write_text('not a directory')
        with self.assertRaises(MemoryError):
            self.save(body='New content', revision=first['revision'])
        self.assertEqual(Path(first['path']).read_text(), profile(body='Old content'))

    def test_index_failure_reports_successful_profile_commit(self):
        with mock.patch.object(self.store, '_refresh_index', side_effect=OSError('injected index failure')):
            result = self.save()
        self.assertTrue(result['saved'])
        self.assertTrue(result['warnings'])
        self.assertEqual(self.store.read('zh', 'chat')['target_revision'], result['revision'])

    def test_corrupt_selected_file_is_reported_not_loaded(self):
        self.save('zh', 'common', 'Common preference')
        item = self.save()
        Path(item['path']).write_text('damaged')
        (self.store.root / 'index.md').write_text('stale, wrong index')
        result = self.store.read('zh', 'chat')
        self.assertEqual([p['scope'] for p in result['profiles']], ['common'])
        self.assertTrue(result['warnings'])
        self.assertEqual(result['target_revision'], hashlib.sha256(b'damaged').hexdigest())

    def test_unreadable_selected_file_reports_warning(self):
        self.save()
        original = Path.read_bytes
        def unavailable(path):
            if path.name == 'chat.md':
                raise PermissionError('injected permission failure')
            return original(path)
        with mock.patch.object(Path, 'read_bytes', unavailable):
            result = self.store.read('zh', 'chat')
        self.assertEqual(result['profiles'], [])
        self.assertTrue(result['warnings'])
        self.assertIsNone(result['target_revision'])

    def test_symlinked_memory_root_is_rejected(self):
        external = self.skill / 'external'
        external.mkdir()
        self.store.root.symlink_to(external, target_is_directory=True)
        with self.assertRaises(MemoryError):
            self.save()
        with self.assertRaises(MemoryError):
            self.store.read('zh', 'chat')
        self.assertEqual(list(external.iterdir()), [])

    def test_symlinked_profile_is_neither_read_nor_overwritten(self):
        self.store.root.mkdir()
        (self.store.root / 'zh').mkdir()
        external = self.skill / 'external.md'
        external.write_text('external secret')
        (self.store.root / 'zh' / 'chat.md').symlink_to(external)
        result = self.store.read('zh', 'chat')
        self.assertEqual(result['profiles'], [])
        self.assertNotIn('external secret', str(result))
        with self.assertRaises(MemoryError):
            self.save()
        self.assertEqual(external.read_text(), 'external secret')

    def test_default_cli_root_is_installation_not_cwd(self):
        scripts = self.skill / 'scripts'
        scripts.mkdir()
        scripts.joinpath('style_memory.py').write_bytes(Path(__file__).resolve().parents[1].joinpath('scripts/style_memory.py').read_bytes())
        item = self.save(body='Installed preference')
        with tempfile.TemporaryDirectory() as other:
            result = subprocess.run([sys.executable, str(scripts / 'style_memory.py'), 'read', '--language', 'zh', '--scenario', 'chat'], cwd=other, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(item['revision'], result.stdout)
        self.assertIn('Installed preference', result.stdout)


if __name__ == '__main__':
    unittest.main()
