#!/usr/bin/env python3
"""Scoped, private Markdown style memory. Python 3.9+, standard library only."""

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import uuid

LANGUAGES = ('zh', 'en')
SCENARIOS = frozenset((
    'chat', 'work-message', 'xiaohongshu', 'x-post', 'wechat-article',
    'documentation', 'grant-proposal', 'academic-talk', 'academic-slides',
    'academic-paper', 'peer-review', 'reviewer-response',
))
MAX_PROFILE_BYTES = 64 * 1024


class MemoryError(Exception):
    """An actionable memory-storage error, safe to report without profile content."""


def revision(data):
    return hashlib.sha256(data).hexdigest()


def validate_scope(language, scenario, saving=False):
    if language not in LANGUAGES:
        raise MemoryError('Language must be zh or en.')
    if not isinstance(scenario, str) or not re.fullmatch(r'[a-z][a-z0-9-]{0,63}', scenario):
        raise MemoryError('Invalid scenario name.')
    if saving and scenario not in SCENARIOS and scenario != 'common':
        raise MemoryError('Save requires common or a supported scenario.')


def validate_profile(content, language, scenario):
    """Validate storage metadata, not the truth of style observations."""
    try:
        data = content.encode('utf-8')
    except (AttributeError, UnicodeError) as exc:
        raise MemoryError('Profile must be UTF-8 text.') from exc
    if len(data) > MAX_PROFILE_BYTES:
        raise MemoryError('Profile exceeds 64 KiB; consolidate its observations first.')
    lines = content.splitlines()
    if not lines or lines[0] != '---':
        raise MemoryError('Profile requires restricted frontmatter.')
    try:
        end = lines.index('---', 1)
    except ValueError as exc:
        raise MemoryError('Profile frontmatter is not closed.') from exc
    fields = {}
    for line in lines[1:end]:
        match = re.fullmatch(r'([a-z_]+):[ \t]*([^\s]+)[ \t]*', line)
        if not match or match[1] in fields:
            raise MemoryError('Invalid or duplicate profile metadata.')
        fields[match[1]] = match[2]
    expected = {'schema_version': '1', 'language': language, 'scenario': scenario}
    if fields != expected:
        raise MemoryError('Profile metadata must match schema_version 1 and the requested language/scenario.')
    if not '\n'.join(lines[end + 1:]).strip():
        raise MemoryError('Profile body must not be empty.')
    return data


class MemoryStore:
    def __init__(self, skill_root):
        self.skill_root = Path(skill_root).resolve()
        self.root = self.skill_root / 'memory'

    def _safe(self, path):
        """Reject symlinked components within the user-owned memory subtree."""
        path = Path(path)
        try:
            parts = path.relative_to(self.root).parts
        except ValueError as exc:
            raise MemoryError('Memory path is outside the installation.') from exc
        current = self.root
        for part in (None,) + parts:
            if part is not None:
                current = current / part
            if current.is_symlink():
                raise MemoryError('Symlinked memory paths are not supported: ' + str(current))
        return path

    def _directory(self, path):
        self._safe(path)
        current = self.root
        for part in (None,) + path.relative_to(self.root).parts:
            if part is not None:
                current = current / part
            current.mkdir(mode=0o700, exist_ok=True)
            if not current.is_dir():
                raise MemoryError('Expected a memory directory: ' + str(current))
            current.chmod(0o700)

    @contextmanager
    def lock(self):
        """Exclusive cooperating-writer lock; never break another owner's lock."""
        token = json.dumps({'pid': os.getpid(), 'token': uuid.uuid4().hex})
        lock_path = self.root / '.write.lock'
        try:
            self._directory(self.root)
            self._safe(lock_path)
            fd = os.open(str(lock_path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError as exc:
            raise MemoryError('Memory is locked. Wait for the writer; after a crash, verify it has stopped before removing .write.lock.') from exc
        except OSError as exc:
            raise MemoryError('Cannot acquire memory lock: ' + str(exc)) from exc
        identity = os.fstat(fd)
        initialized = False
        try:
            handle = os.fdopen(fd, 'w', encoding='utf-8')
            fd = None  # The handle now owns the descriptor, including on failure.
            with handle:
                handle.write(token)
                handle.flush()
                os.fsync(handle.fileno())
            initialized = True
            yield
        finally:
            if fd is not None:
                os.close(fd)
            try:
                current = lock_path.lstat()
                owned = (current.st_dev, current.st_ino) == (identity.st_dev, identity.st_ino)
                if owned and not lock_path.is_symlink() and (
                        not initialized or lock_path.read_text(encoding='utf-8') == token):
                    lock_path.unlink()
            except OSError:
                # Do not remove a lock whose ownership cannot be established.
                pass

    def _atomic_write(self, path, data):
        self._safe(path)
        self._directory(path.parent)
        temp_path = None
        try:
            with tempfile.NamedTemporaryFile(prefix='.style-memory-', suffix='.tmp', dir=path.parent, delete=False) as handle:
                temp_path = Path(handle.name)
                os.chmod(temp_path, 0o600)
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            self._safe(path)
            os.replace(str(temp_path), str(path))
            temp_path = None
            if path.read_bytes() != data:
                raise MemoryError('File was replaced but persisted-byte verification failed: ' + str(path))
        finally:
            if temp_path is not None:
                temp_path.unlink(missing_ok=True)

    def read(self, language, scenario):
        validate_scope(language, scenario)
        self._safe(self.root)
        result = {'language': language, 'scenario': scenario, 'profiles': [],
                  'target_revision': 'missing', 'warnings': []}
        scopes = ['common']
        if scenario in SCENARIOS:
            scopes.append(scenario)
        for scope in scopes:
            path = self.root / language / (scope + '.md')
            is_target = scope == scenario
            try:
                self._safe(path)
                if not path.exists():
                    continue
                if is_target:
                    result['target_revision'] = None
                if not path.is_file():
                    raise MemoryError('Expected a profile file.')
                if path.stat().st_size > MAX_PROFILE_BYTES:
                    raise MemoryError('Profile exceeds 64 KiB.')
                data = path.read_bytes()
                current_revision = revision(data)
                if is_target:
                    result['target_revision'] = current_revision
                content = data.decode('utf-8')
                validate_profile(content, language, scope)
                result['profiles'].append({'scope': scope, 'path': str(path),
                                           'revision': current_revision, 'content': content})
            except (OSError, UnicodeError, MemoryError) as exc:
                if is_target and result['target_revision'] == 'missing':
                    result['target_revision'] = None
                result['warnings'].append(str(path) + ': ' + str(exc))
        return result

    def _refresh_index(self):
        rows = ['# Writing style memory index', '',
                'Generated for browsing. Reads select language/scope files directly.', '',
                '| Language | Scenario | File |', '|---|---|---|']
        warnings = []
        for language in LANGUAGES:
            for scope in sorted(SCENARIOS | {'common'}):
                path = self.root / language / (scope + '.md')
                try:
                    self._safe(path)
                    if not path.exists():
                        continue
                    if path.stat().st_size > MAX_PROFILE_BYTES:
                        raise MemoryError('Profile exceeds 64 KiB.')
                    validate_profile(path.read_text(encoding='utf-8'), language, scope)
                    relative = path.relative_to(self.root).as_posix()
                    rows.append(f'| {language} | {scope} | [{relative}]({relative}) |')
                except (OSError, UnicodeError, MemoryError) as exc:
                    warnings.append('Index skipped ' + str(path) + ': ' + str(exc))
        self._atomic_write(self.root / 'index.md', ('\n'.join(rows) + '\n').encode('utf-8'))
        return warnings

    def save(self, language, scenario, content, expected_revision):
        validate_scope(language, scenario, saving=True)
        data = validate_profile(content, language, scenario)
        if not isinstance(expected_revision, str) or not (
                expected_revision == 'missing' or re.fullmatch(r'[0-9a-f]{64}', expected_revision)):
            raise MemoryError('Expected revision must be missing or a SHA-256 from read.')
        path = self.root / language / (scenario + '.md')
        backup = None
        try:
            with self.lock():
                self._safe(path)
                old = path.read_bytes() if path.exists() else None
                actual_revision = revision(old) if old is not None else 'missing'
                if actual_revision != expected_revision:
                    raise MemoryError('Revision conflict: reread the profile and reconsider the merge before saving.')
                if old == data:
                    return {'saved': True, 'path': str(path), 'revision': actual_revision,
                            'backup': None, 'warnings': [], 'unchanged': True}
                if old is not None:
                    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
                    backup = self.root / '.backups' / language / scenario / (stamp + '-' + uuid.uuid4().hex[:8] + '.md')
                    self._atomic_write(backup, old)
                self._atomic_write(path, data)
                warnings = []
                try:
                    warnings.extend(self._refresh_index())
                except (OSError, UnicodeError, MemoryError) as exc:
                    warnings.append('Profile saved, but index refresh failed: ' + str(exc))
                return {'saved': True, 'path': str(path), 'revision': revision(data),
                        'backup': str(backup) if backup else None, 'warnings': warnings}
        except OSError as exc:
            raise MemoryError('Memory save failed: ' + str(exc)) from exc


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('read', 'save'):
        command = commands.add_parser(name)
        command.add_argument('--language', required=True, choices=LANGUAGES)
        command.add_argument('--scenario', required=True)
        if name == 'save':
            command.add_argument('--input', required=True, type=Path)
            command.add_argument('--expected-revision', required=True)
    args = parser.parse_args(argv)
    store = MemoryStore(Path(__file__).resolve().parents[1])
    try:
        if args.command == 'read':
            result = store.read(args.language, args.scenario)
        else:
            if args.input.stat().st_size > MAX_PROFILE_BYTES:
                raise MemoryError('Input profile exceeds 64 KiB.')
            result = store.save(args.language, args.scenario,
                                args.input.read_text(encoding='utf-8'), args.expected_revision)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (MemoryError, OSError, UnicodeError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
