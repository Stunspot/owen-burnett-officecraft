#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,io,json,re,zipfile
from pathlib import Path,PurePosixPath
SKILLS=('owen-burnett-officecraft','officecraft-reviewer'); PRIVATE=re.compile(r'(?i)(?:C:[\\/]+Users[\\/]+user|E:[\\/]+(?:Github|Indranet))'); FORBIDDEN=re.compile(r'(?i)(?:^|/)(?:__pycache__(?:/|$)|[^/]+\.(?:pyc|pyo)$)')
def sha(b):return hashlib.sha256(b).hexdigest()
def inv(r):return [{'path':p.relative_to(r).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sorted((x for x in r.rglob('*') if x.is_file()),key=lambda x:x.relative_to(r).as_posix())]
def safe(n):return bool(n) and '\\' not in n and not n.startswith('/') and '\x00' not in n and all(x not in {'','.','..'} and ':' not in x for x in PurePosixPath(n).parts)
def inspect(data,label,out):
 try:
  with zipfile.ZipFile(io.BytesIO(data)) as z:
   ns=z.namelist()
   if len(ns)!=len({n.casefold() for n in ns}):out.append(f'{label}: duplicate/case collision')
   for i in z.infolist():
    if not safe(i.filename):out.append(f'{label}: unsafe {i.filename}')
    if FORBIDDEN.search(i.filename):out.append(f'{label}: generated cargo {i.filename}')
    try:
     if PRIVATE.search(z.read(i).decode()):out.append(f'{label}: private topology {i.filename}')
    except UnicodeDecodeError:pass
   return len(ns)
 except Exception as e:out.append(f'{label}: {e}');return 0
def verify(root,outer):
 out=[];m=json.loads((root/'release-manifest.json').read_text());v=m['version']; expected={x['path']:x for x in m['files']};actual={x['path']:x for x in inv(root) if x['path']!='release-manifest.json'}
 if expected!=actual:out.append('manifest inventory differs')
 source=root/'source'/f'owen-burnett-officecraft-v{v}'; count=0
 for s in SKILLS:
  codex={p.relative_to(root/'codex'/s).as_posix():p.read_bytes() for p in (root/'codex'/s).rglob('*') if p.is_file()}; src={p.relative_to(source/'codex'/s).as_posix():p.read_bytes() for p in (source/'codex'/s).rglob('*') if p.is_file()}
  if codex!=src:out.append(f'{s}: source/Codex differs')
  cz=root/'claude'/f'{s}-v{v}.zip';count+=inspect(cz.read_bytes(),f'{s} Claude ZIP',out)
  with zipfile.ZipFile(cz) as z: archived={n[len(s)+1:]:z.read(n) for n in z.namelist() if n.startswith(s+'/')}
  if archived!=codex:out.append(f'{s}: Claude/Codex differs')
 count+=inspect(outer.read_bytes(),'outer ZIP',out);prefix=f'Owen-Burnett-Officecraft-v{v}/'
 with zipfile.ZipFile(outer) as z: archived={n[len(prefix):]:z.read(n) for n in z.namelist() if n.startswith(prefix)}
 expanded={p.relative_to(root).as_posix():p.read_bytes() for p in root.rglob('*') if p.is_file()}
 if archived!=expanded:out.append('outer/expanded differs')
 return {'schema':'cd-officecraft-release-verification/v1','ok':not out,'counts':{'manifest_files':len(actual),'runtime_files':sum(m['skills'][s]['file_count'] for s in SKILLS),'zip_members':count},'findings':sorted(set(out))}
def main():
 p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('--outer',type=Path,required=True);a=p.parse_args();r=verify(a.root.resolve(),a.outer.resolve());print(json.dumps(r,indent=2));return 0 if r['ok'] else 1
if __name__=='__main__':raise SystemExit(main())