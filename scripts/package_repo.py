"""Create a portable source ZIP and SHA-256 receipts without Git history.

Only explicitly selected public files are included. Review contents before
sharing: path exclusions do not prove absence of confidential text or secrets.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys
import tempfile
import zipfile
from pathlib import Path

from repo_utils import collect_public_files, load_json, valid_slug

ROOT = Path(__file__).resolve().parents[1]


def build_archive(root: Path, output: Path, force: bool = False) -> tuple[int, str, str]:
    root = root.resolve()
    output = output.expanduser().absolute()
    if output.is_symlink():
        raise ValueError('Archive output must not be a symlink.')
    output = output.resolve()
    if output.is_relative_to(root):
        raise ValueError('Write the ZIP outside the project directory.')
    receipt = output.with_suffix(output.suffix + '.sha256')
    if receipt.is_symlink():
        raise ValueError('Checksum output must not be a symlink.')
    if not force and (output.exists() or receipt.exists()):
        raise ValueError('Output or checksum already exists; choose a new name or use --force.')
    config = load_json(root / 'repo_config.json')
    slug = config.get('slug')
    if not valid_slug(slug):
        raise ValueError('Invalid project slug in repo_config.json.')
    paths, mode = collect_public_files(root)
    # Snapshot each selected file once; all recorded hashes match archived bytes.
    payload = {}
    for path in paths:
        raw = path.read_bytes()
        raw.decode('utf-8')  # This text-only scaffold rejects unexpected binary material.
        if b'\r' in raw or b'\0' in raw:
            raise ValueError(f'Expected LF text without NUL bytes: {path.relative_to(root)}')
        payload[path.relative_to(root).as_posix()] = raw
    manifest = ''.join(f'{hashlib.sha256(raw).hexdigest()}  {name}\n' for name, raw in sorted(payload.items()))
    payload['MANIFEST.sha256'] = manifest.encode('utf-8')
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=output.parent, suffix='.zip.tmp', delete=False) as handle:
            temporary = Path(handle.name)
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for name, raw in sorted(payload.items()):
                info = zipfile.ZipInfo(f'{slug}/{name}', date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = (0o100644 << 16)
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, raw, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        digest = hashlib.sha256(temporary.read_bytes()).hexdigest()
        os.replace(temporary, output)
        receipt.write_text(f'{digest}  {output.name}\n', encoding='utf-8', newline='\n')
        return len(paths), digest, mode
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--force', action='store_true', help='Replace only the specified ZIP and checksum.')
    args = parser.parse_args()
    try:
        count, digest, mode = build_archive(args.root, args.output, args.force)
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print(f'Packaged {count} source files plus MANIFEST.sha256 ({mode}).')
    print(f'ZIP: {args.output.resolve()}')
    print(f'SHA-256: {digest}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
