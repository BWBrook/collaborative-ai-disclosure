"""Shared, standard-library-only helpers for local repository maintenance.

Exclusions reduce accidental disclosure. They are not a complete secret scanner.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from pathlib import Path, PurePosixPath
from typing import Any

EXCLUDED_PARTS = {
    '.git', '.venv', 'venv', '__pycache__', '.pytest_cache', '.cache',
    'build', 'dist', 'private', '.private', 'local', '.codex', '.claude',
    '.sessions', 'raw-transcripts', 'node_modules',
}
EXCLUDED_SUFFIXES = {'.pyc', '.pyo', '.zip', '.pem', '.key', '.p12', '.pfx', '.log'}


def load_json(path: Path) -> dict[str, Any]:
    """Read a JSON object with a helpful error on invalid or non-object input."""
    try:
        obj = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f'{path}: {exc}') from exc
    if not isinstance(obj, dict):
        raise ValueError(f'{path}: expected a JSON object')
    return obj


def safe_relative(path: str) -> bool:
    parts = PurePosixPath(path).parts
    return bool(parts) and not path.startswith('/') and '\\' not in path and all(
        p not in {'..', '.'} and not any(ord(c) < 32 for c in p) for p in parts
    ) and ':' not in path


def excluded(path: str) -> bool:
    """Conservative filename exclusions, applied even to tracked files."""
    p = PurePosixPath(path.lower())
    if any(part in EXCLUDED_PARTS for part in p.parts):
        return True
    name = p.name
    return (
        name in {'manifest.sha256', '.ds_store', 'thumbs.db', 'id_rsa', 'id_ed25519'}
        or name.startswith('.env')
        or 'credentials' in name or 'secrets' in name
        or name.endswith('.zip.sha256') or p.suffix in EXCLUDED_SUFFIXES
    )


def git_top(root: Path) -> Path | None:
    """Return the enclosing Git root; a nested project is not silently accepted."""
    if shutil.which('git') is None:
        if (root / '.git').exists():
            raise ValueError('This directory has .git but Git is unavailable.')
        return None
    result = subprocess.run(
        ['git', '-C', str(root), 'rev-parse', '--show-toplevel'],
        capture_output=True, text=True, check=False, timeout=15,
    )
    if result.returncode != 0:
        if (root / '.git').exists():
            raise ValueError('Git could not inspect this repository: ' + result.stderr.strip())
        return None
    return Path(result.stdout.strip()).resolve()


def collect_public_files(root: Path) -> tuple[list[Path], str]:
    """Select tracked files in Git, or explicitly allowed roots for a fresh ZIP.

    Current file bytes are selected, including unstaged edits to tracked files.
    Unknown untracked files are never added merely because they sit in a Git tree.
    """
    root = root.resolve()
    top = git_top(root)
    candidates: list[str] = []
    if top is not None:
        if top != root:
            raise ValueError('Project is inside another Git repository; use its own workspace.')
        result = subprocess.run(
            ['git', '-C', str(root), 'ls-files', '-z'],
            capture_output=True, check=True, timeout=15,
        )
        candidates = [x.decode('utf-8') for x in result.stdout.split(b'\0') if x]
        mode = 'git-tracked-current-bytes'
    else:
        config = load_json(root / 'repo_config.json')
        roots = config.get('public_roots')
        if not isinstance(roots, list) or not roots or not all(isinstance(x, str) for x in roots):
            raise ValueError('repo_config.json needs a non-empty public_roots string list.')
        for item in roots:
            if not safe_relative(item):
                raise ValueError(f'Unsafe public_roots entry: {item!r}')
            entry = root / item
            if entry.is_symlink():
                raise ValueError(f'Symlinks are not packaged: {item}')
            if entry.is_file():
                candidates.append(item)
            elif entry.is_dir():
                for current, directories, files in os.walk(entry, followlinks=False):
                    current_path = Path(current)
                    for name in list(directories):
                        child = current_path / name
                        rel = child.relative_to(root).as_posix()
                        if excluded(rel):
                            directories.remove(name)
                        elif child.is_symlink():
                            raise ValueError(f'Symlinks are not packaged: {rel}')
                    candidates.extend((current_path / name).relative_to(root).as_posix() for name in files)
        mode = 'explicit-public-roots'
    selected = []
    for item in sorted(set(candidates)):
        if not safe_relative(item):
            raise ValueError(f'Unsafe public path: {item!r}')
        if excluded(item):
            continue
        target = root / item
        # Check every component so a tracked path under a symlink cannot escape.
        cursor = root
        for part in PurePosixPath(item).parts:
            cursor = cursor / part
            if cursor.is_symlink():
                raise ValueError(f'Symlinks are not packaged: {item}')
        if not target.is_file():
            raise ValueError(f'Selected file missing or not a regular file: {item}')
        selected.append(target)
    if not selected:
        raise ValueError('No public files selected. In Git, stage intended public files first.')
    return selected, mode


def valid_slug(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', value) is not None
