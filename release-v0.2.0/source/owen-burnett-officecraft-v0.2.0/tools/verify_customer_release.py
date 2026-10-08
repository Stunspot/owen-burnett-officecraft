#!/usr/bin/env python3
"""Verify extracted Officecraft package custody and matched runtime pairs only."""
import argparse, hashlib, io, json, zipfile
from pathlib import Path
from archive_paths import assert_unlinked, check_members


def verify(root):
    root=assert_unlinked(root)
    m=json.loads((root/'release-manifest.json').read_text(encoding='utf-8'))
    if m.get('schema')!='collaborative-dynamics.customer-skill-family/v3' or m.get('slug')!='owen-burnett-officecraft':
        raise ValueError('Unexpected package identity')
    expected={x['path']:x['sha256']for x in m['files']}
    actual={p.relative_to(root).as_posix():p.read_bytes()for p in root.rglob('*')if p.is_file()and '__pycache__'not in p.parts and p.suffix not in ('.pyc','.pyo')and p.relative_to(root).as_posix()!='release-manifest.json'}
    if len(expected)!=len(m['files']) or set(actual)!=set(expected):raise ValueError('Package file set differs')
    check_members(list(actual.items()))
    for n,b in actual.items():
        if hashlib.sha256(b).hexdigest()!=expected[n]:raise ValueError('Package bytes differ: '+n)
    for skill in m['skills']:
        prefix='codex/'+skill+'/'
        files={n[len(prefix):]:b for n,b in actual.items()if n.startswith(prefix)}
        source_prefix=m['source']['path']+'/'+prefix
        if files!={n[len(source_prefix):]:b for n,b in actual.items()if n.startswith(source_prefix)}:raise ValueError('Maintained source differs: '+skill)
        with zipfile.ZipFile(io.BytesIO(actual[m['skills'][skill]['claude_zip']]))as z:
            entries=[(i.filename,z.read(i))for i in z.infolist()if not i.is_dir()];check_members(entries)
            if any(not n.startswith(skill+'/')for n,b in entries)or {n[len(skill)+1:]:b for n,b in entries}!=files:raise ValueError('Runtime pair differs: '+skill)
    return {'valid':True,'files':len(actual),'skills':list(m['skills']),'boundary':'Exact static package bytes and runtime/source parity; not native office app, content, host activation or approval proof.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args()
    try:print(json.dumps(verify(a.root),indent=2));return 0
    except (OSError,ValueError,KeyError,TypeError,zipfile.BadZipFile)as exc:print('Invalid package: '+str(exc));return 2
if __name__=='__main__':raise SystemExit(main())