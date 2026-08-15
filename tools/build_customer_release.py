#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,shutil,subprocess,zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[1]; V='0.1.1'; SLUG='owen-burnett-officecraft'; TITLE='Owen Burnett Officecraft'; STAMP=(2026,8,14,0,0,0)
SKILLS=('owen-burnett-officecraft','officecraft-reviewer'); EX=('.github/','tools/','release-v','release-assets/','verification/')
def sha(b): return hashlib.sha256(b).hexdigest()
def fs(r): return sorted((p for p in r.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.pyo'}),key=lambda p:p.relative_to(r).as_posix())
def inv(r): return [{'path':p.relative_to(r).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in fs(r)]
def tree(r): return sha(json.dumps(inv(r),sort_keys=True,separators=(',',':')).encode())
def wr(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s,encoding='utf-8',newline='\n')
def ziptree(out,root,prefix=''):
 with zipfile.ZipFile(out,'w',zipfile.ZIP_STORED) as z:
  for p in fs(root):
   n=p.relative_to(root).as_posix(); i=zipfile.ZipInfo(f'{prefix}/{n}' if prefix else n,STAMP); i.compress_type=zipfile.ZIP_STORED;i.external_attr=0o100644<<16;i.create_system=3;z.writestr(i,p.read_bytes())
def reset(p,parent):
 if p.resolve().parent!=parent.resolve(): raise RuntimeError(p)
 if p.exists(): shutil.rmtree(p)
 p.mkdir(parents=True)
def copytree(src,dst): shutil.copytree(src,dst,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.pyo'))
def main():
 rel=R/f'release-v{V}'; reset(rel,R)
 codex=rel/'codex'; codex.mkdir()
 for s in SKILLS: copytree(R/'codex'/s,codex/s)
 claude=rel/'claude'; claude.mkdir()
 for s in SKILLS:
  stage=R/f'.stage-{s}';
  if stage.exists(): shutil.rmtree(stage)
  copytree(R/'codex'/s,stage/s); ziptree(claude/f'{s}-v{V}.zip',stage); shutil.rmtree(stage)
 source=rel/'source'/f'{SLUG}-v{V}'; source.mkdir(parents=True)
 for name in subprocess.check_output(['git','ls-files'],cwd=R,text=True).splitlines():
  q=name.replace('\\','/')
  if q.startswith(EX): continue
  p=R/name
  if p.is_file(): d=source/name;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,d)
 shutil.copy2(R/'LICENSE.md',rel/'LICENSE.md')
 wr(rel/'README.md',f'# {TITLE} v{V}\n\nThis is the complete public customer package. Start with [START-HERE.md](START-HERE.md). Install only the two Codex skill folders or the two matched Claude ZIPs; source and release records are custody material.\n')
 wr(rel/'START-HERE.md',f'# Start here\n\n1. Read the maintained [orientation](source/{SLUG}-v{V}/README.md) and [installation guide](source/{SLUG}-v{V}/START-HERE.md).\n2. Install both folders under `codex/`, or both untouched archives under `claude/`.\n3. Restart the host, confirm discovery, invoke Owen explicitly, and run a small low-risk job.\n4. Keep operator and reviewer on the same version. Do not install source, manifests, or checksums as runtime cargo.\n')
 wr(rel/'HOST-MATRIX.md',f'# Host matrix\n\n| Host | Distribution | Exact evidence | Live evidence |\n| --- | --- | --- | --- |\n| Codex | `codex/{SLUG}/` plus `codex/officecraft-reviewer/` | Complete and byte-bound | Fresh-host discovery and invocation untested |\n| Claude | Two matched `claude/*-v{V}.zip` archives | Byte-identical to Codex runtimes | Fresh-host discovery and invocation untested |\n| Chat-only | Maintained fallback material | Present in operator runtime | Attachment behavior varies |\n')
 wr(rel/'PROVENANCE.md',f'# Provenance\n\n- Repository: https://github.com/Stunspot/{SLUG}\n- Later maintained main before reconciliation: `69e27712b4da01312a66876b085dbb0dda58d39c`\n- Release version: `{V}`\n- Maintained source snapshot: `source/{SLUG}-v{V}/`\n- Both Codex/Claude runtime pairs have exact byte parity.\n\nThe v0.1.0 release is retained historical evidence; it predates the merged customer-documentation and public-presentation work.\n')
 shutil.copy2(R/'RELEASE-NOTES.md',rel/f'RELEASE-NOTES-v{V}.md')
 wr(rel/'PACKAGE-REFERENCE.md',f'# Package reference\n\n- `codex/`: matched operator and reviewer skill roots.\n- `claude/`: matched one-root skill archives.\n- `source/{SLUG}-v{V}/`: maintained source snapshot.\n- `release-manifest.json`: exact file custody.\n- `SHA256SUMS.txt`: runtime and archive digests.\n')
 sums=[]
 for s in SKILLS: sums += [(tree(codex/s),f'codex/{s}/'),(sha((claude/f'{s}-v{V}.zip').read_bytes()),f'claude/{s}-v{V}.zip')]
 wr(rel/'SHA256SUMS.txt',''.join(f'{h}  {p}\n' for h,p in sums))
 manifest={'schema':'collaborative-dynamics.customer-skill-family/v2','product':TITLE,'slug':SLUG,'version':V,'source_repository':f'https://github.com/Stunspot/{SLUG}','source_basis_commit':'69e27712b4da01312a66876b085dbb0dda58d39c','claim_boundary':'Exact static package custody; live hosts, office applications, people, and Discord require separate observation.','skills':{},'source':{'path':f'source/{SLUG}-v{V}','file_count':len(fs(source)),'tree_sha256':tree(source)}}
 for s in SKILLS: manifest['skills'][s]={'codex_tree_sha256':tree(codex/s),'file_count':len(fs(codex/s)),'claude_zip':f'claude/{s}-v{V}.zip','claude_sha256':sha((claude/f'{s}-v{V}.zip').read_bytes())}
 manifest['files']=inv(rel); wr(rel/'release-manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 assets=R/'release-assets'/f'v{V}'; reset(assets,R/'release-assets'); outer=assets/f'Owen-Burnett-Officecraft-v{V}.zip'; ziptree(outer,rel,f'Owen-Burnett-Officecraft-v{V}'); dig=sha(outer.read_bytes());wr(assets/f'{outer.name}.sha256',f'{dig}  {outer.name}\n');wr(assets/'receipt.json',json.dumps({'schema':'cd-settled-family-build-receipt/v1','family':SLUG,'version':V,'status':'canonical-built-backup-pending','canonical_zip':outer.name,'canonical_zip_sha256':dig,'canonical_zip_member_count':len(zipfile.ZipFile(outer).infolist()),'backup':None},indent=2)+'\n');print(json.dumps({'archive':str(outer),'sha256':dig,'members':len(zipfile.ZipFile(outer).infolist()),'source_files':len(fs(source)),'runtime_files':sum(len(fs(codex/s)) for s in SKILLS)},indent=2))
if __name__=='__main__': raise SystemExit(main())