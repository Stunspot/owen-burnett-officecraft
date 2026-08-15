#!/usr/bin/env python3
import argparse,hashlib,json
from datetime import datetime,timezone
from pathlib import Path
R=Path(__file__).resolve().parents[1];V='0.1.1'
ROOT=['README.md','START-HERE.md','HOST-MATRIX.md','CHANGELOG.md','RELEASE-NOTES.md','CONTRIBUTING.md','LICENSE.md','SECURITY.md','SUPPORT.md']
SITE=[p.relative_to(R).as_posix() for p in sorted((R/'docs').rglob('*')) if p.is_file()]
PACKAGE=[f'release-v{V}/{x}' for x in ['README.md','START-HERE.md','HOST-MATRIX.md','PROVENANCE.md','PACKAGE-REFERENCE.md',f'RELEASE-NOTES-v{V}.md']]
PATHS=sorted(ROOT+SITE+PACKAGE)
def canon(p):
 b=p.read_bytes();return b if p.suffix.lower() in {'.png','.jpg','.jpeg','.gif','.webp'} else b.replace(b'\r\n',b'\n').replace(b'\r',b'\n')
def main():
 a=argparse.ArgumentParser();a.add_argument('--check',action='store_true');o=a.parse_args();rows=[{'path':x,'sha256':hashlib.sha256(canon(R/x)).hexdigest()} for x in PATHS];h=hashlib.sha256()
 for x in rows:h.update(x['path'].encode()+b'\0'+x['sha256'].encode()+b'\n')
 result={'format':'officecraft-documentation-fingerprint/v1','generated_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),'product_version':V,'aggregate_sha256':h.hexdigest(),'files':rows,'algorithm':'sha256 over sorted path NUL canonical file-sha256 records; text line endings normalized to LF'};targets=[R/'verification'/'documentation-fingerprint.json',R/'verification'/f'documentation-fingerprint-v{V}.json']
 if o.check:
  bad=[str(x.relative_to(R)) for x in targets if (lambda q:q.get('files')!=rows or q.get('aggregate_sha256')!=result['aggregate_sha256'])(json.loads(x.read_text()))];print(json.dumps({'ok':not bad,'files':len(rows),'aggregate_sha256':result['aggregate_sha256'],'mismatches':bad},indent=2));return 0 if not bad else 1
 t=json.dumps(result,indent=2)+'\n'
 for x in targets:x.write_text(t,encoding='utf-8',newline='\n')
 print(json.dumps({'files':len(rows),'aggregate_sha256':result['aggregate_sha256']},indent=2));return 0
if __name__=='__main__':raise SystemExit(main())