"""Export and update a skill installation with explicit file boundaries."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
import zipfile
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple


_TOP_LEVEL_FILES = {
    "SKILL.md",
    "README.md",
    "README.zh.md",
    "README.en.md",
    "LICENSE",
    "CONTRIBUTING.md",
    ".gitignore",
}
_TOP_LEVEL_DIRS = {"references", "scripts", "templates"}
_EXTRA_FILES = {".github/banner.png"}
_DIRECTORY_SUFFIXES = {
    "references": {".md"},
    "scripts": {".py"},
    "templates": {".md"},
}
_TEMP_MARKERS = (".tmp-", ".tmp.")


def _resolved_dir(value: Path, label: str) -> Path:
    path = Path(value)
    if path.is_symlink() or not path.is_dir():
        raise ValueError(f"{label} must be a real directory: {path}")
    return path.resolve()


def _inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _reject_symlinks(paths: Iterable[Path]) -> None:
    for root in paths:
        if root.is_symlink():
            raise ValueError(f"symlink entries are not allowed: {root}")
        if not root.is_dir():
            continue
        for current, dirs, files in os.walk(root, followlinks=False):
            current_path = Path(current)
            for name in list(dirs) + list(files):
                item = current_path / name
                if item.is_symlink():
                    raise ValueError(f"symlink entries are not allowed: {item}")


def _validate_relative_path(root: Path, relative: str, require_directory: bool = False) -> None:
    """Reject symlinked or special ancestors before reading or writing a path."""
    current = root
    parts = Path(relative).parts
    for index, part in enumerate(parts):
        current = current / part
        if os.path.lexists(current):
            if current.is_symlink():
                raise ValueError(f"symlink entries are not allowed: {current}")
            if index < len(parts) - 1 and not current.is_dir():
                raise ValueError(f"maintained parent is not a directory: {current}")
            if index == len(parts) - 1 and require_directory and not current.is_dir():
                raise ValueError(f"maintained path is not a directory: {current}")


def _maintained_roots(root: Path) -> List[Path]:
    paths = [root / name for name in _TOP_LEVEL_FILES | _EXTRA_FILES]
    paths.extend(root / name for name in _TOP_LEVEL_DIRS)
    return [path for path in paths if os.path.lexists(path)]


def _maintained_files(root: Path) -> List[Tuple[Path, str]]:
    """Return the explicit public file allowlist and its archive names."""
    selected: List[Tuple[Path, str]] = []
    for name in sorted(_TOP_LEVEL_FILES | _EXTRA_FILES):
        item = root / name
        if os.path.lexists(item):
            _validate_relative_path(root, name)
            if item.is_symlink():
                raise ValueError(f"symlink entries are not allowed: {item}")
            if not item.is_file():
                raise ValueError(f"maintained path is not a file: {item}")
            selected.append((item, name))
    for directory in sorted(_TOP_LEVEL_DIRS):
        base = root / directory
        if not os.path.lexists(base):
            continue
        _validate_relative_path(root, directory, require_directory=True)
        if base.is_symlink():
            raise ValueError(f"symlink entries are not allowed: {base}")
        if not base.is_dir():
            raise ValueError(f"maintained path is not a directory: {base}")
        for item in sorted(base.rglob("*")):
            if item.is_file():
                if item.suffix.lower() in _DIRECTORY_SUFFIXES[directory]:
                    selected.append((item, item.relative_to(root).as_posix()))
            elif not item.is_dir():
                raise ValueError(f"maintained path is not a regular file: {item}")
    return selected


def _memory_files(root: Path) -> List[Tuple[Path, str]]:
    memory = root / "memory"
    if not os.path.lexists(memory):
        return []
    if memory.is_symlink() or not memory.is_dir():
        raise ValueError(f"memory must be a real directory: {memory}")
    selected: List[Tuple[Path, str]] = []
    for item in sorted(memory.rglob("*")):
        relative = item.relative_to(memory)
        if (
            item.name == ".write.lock"
            or item.name.endswith(".tmp")
            or any(marker in item.name for marker in _TEMP_MARKERS)
        ):
            continue
        if item.is_symlink():
            raise ValueError(f"symlink entries are not allowed: {item}")
        if item.is_file():
            selected.append((item, (Path("memory") / relative).as_posix()))
        elif not item.is_dir():
            raise ValueError(f"memory entry is not a regular file: {item}")
    return selected


def _exclusive_zip(output: Path, entries: Sequence[Tuple[Path, str]]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(str(output), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = -1
            with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                for source, archive_name in entries:
                    archive.write(source, archive_name)
    except Exception:
        if descriptor != -1:
            os.close(descriptor)
        try:
            output.unlink()
        except FileNotFoundError:
            pass
        raise


def export_skill(skill_root: Path, output: Path, include_memory: bool = False) -> dict:
    """Create an exclusive ZIP from maintained files.

    ``include_memory`` is reserved for an explicit private backup. Public
    exports use the default and never include generated memory or local data.
    """
    root = _resolved_dir(Path(skill_root), "skill root")
    destination = Path(output).absolute()
    if _inside(destination.resolve(), root):
        raise ValueError("output must be outside the skill root")
    _reject_symlinks(_maintained_roots(root))
    entries = _maintained_files(root)
    if include_memory:
        memory = root / "memory"
        if os.path.lexists(memory):
            if __package__:
                from .style_memory import MemoryStore
            else:
                from style_memory import MemoryStore
            with MemoryStore(root).lock():
                _reject_symlinks([memory])
                entries = entries + _memory_files(root)
                _exclusive_zip(destination, entries)
        else:
            _exclusive_zip(destination, entries)
    else:
        _exclusive_zip(destination, entries)
    return {
        "created": str(destination),
        "files": [archive_name for _, archive_name in entries],
        "include_memory": bool(include_memory),
    }


def _skill_name(root: Path) -> str:
    skill_file = root / "SKILL.md"
    if not skill_file.is_file() or skill_file.is_symlink():
        raise ValueError(f"missing SKILL.md: {root}")
    text = skill_file.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"SKILL.md has no frontmatter: {root}")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"SKILL.md has unclosed frontmatter: {root}") from exc
    matches = [re.fullmatch(r"name:\s*([^\s#]+)\s*", line) for line in lines[1:end]]
    matches = [match for match in matches if match]
    if len(matches) != 1:
        raise ValueError(f"SKILL.md has no name: {root}")
    return matches[0].group(1)


def _atomic_copy(source: Path, target: Path) -> None:
    data = source.read_bytes()
    temporary = target.with_name(f".{target.name}.skill-update-{os.getpid()}-{time.time_ns()}.tmp")
    try:
        with temporary.open("wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        shutil.copystat(source, temporary)
        os.replace(str(temporary), str(target))
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def update_skill(skill_root: Path, source: Path) -> dict:
    """Update maintained program files while preserving local memory."""
    target = _resolved_dir(Path(skill_root), "target skill root")
    incoming = _resolved_dir(Path(source), "source skill root")
    if target == incoming or _inside(target, incoming) or _inside(incoming, target):
        raise ValueError("source and target skill roots must be separate")
    _reject_symlinks(_maintained_roots(target))
    _reject_symlinks(_maintained_roots(incoming))
    if _skill_name(target) != _skill_name(incoming):
        raise ValueError("source and target skills have different names")
    source_files = _maintained_files(incoming)
    backup_files: List[str] = []
    updated_files: List[str] = []
    backup_root = target / ".local" / "updates" / str(time.time_ns())
    for source_file, relative in source_files:
        target_file = target / relative
        _validate_relative_path(target, relative)
        if os.path.lexists(target_file) and (target_file.is_symlink() or not target_file.is_file()):
            raise ValueError(f"target maintained path is not a file: {target_file}")
    _validate_relative_path(target, ".local/updates", require_directory=True)
    for source_file, relative in source_files:
        target_file = target / relative
        if target_file.exists() and target_file.read_bytes() == source_file.read_bytes():
            continue
        if target_file.exists():
            backup_file = backup_root / relative
            backup_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target_file, backup_file)
            backup_files.append(str(backup_file))
        target_file.parent.mkdir(parents=True, exist_ok=True)
        _atomic_copy(source_file, target_file)
        updated_files.append(relative)
    return {
        "updated": updated_files,
        "backups": backup_files,
        "preserved_memory": True,
    }


def _main(argv: Optional[Iterable[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    export_parser = subparsers.add_parser("export")
    export_parser.add_argument("--output", required=True, type=Path)
    backup_parser = subparsers.add_parser("backup")
    backup_parser.add_argument("--output", required=True, type=Path)
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--source", required=True, type=Path)
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent.parent
    try:
        if args.command == "export":
            result = export_skill(root, args.output)
        elif args.command == "backup":
            result = export_skill(root, args.output, include_memory=True)
        else:
            result = update_skill(root, args.source)
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
