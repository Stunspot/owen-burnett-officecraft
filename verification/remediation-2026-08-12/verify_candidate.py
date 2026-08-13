#!/usr/bin/env python3
"""Reproduce the bounded local verification for the Officecraft documentation candidate."""
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.request import urlopen
import argparse, subprocess, threading, os, hashlib, json, struct, re

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    root=Path(__file__).resolve().parents[2]; docs=root/'docs'
    result={'format':'cd-testforge-local-evidence/v1','target_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'executions':[]}
    def run(eid,cmd):
        p=subprocess.run(cmd,cwd=root,text=True,capture_output=True)
        result['executions'].append({'id':eid,'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
        if p.returncode: raise RuntimeError(f'{eid} failed')
    run('E-001',['python','-B','-m','unittest','discover','-s','codex/owen-burnett-officecraft/tests','-p','test_*.py','-v'])
    run('E-002A',['python','-B','scripts/build_pages.py']); one={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(docs.glob('*.html'))}
    run('E-002B',['python','-B','scripts/build_pages.py']); two={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(docs.glob('*.html'))}
    result['pages_determinism']={'status':'PASS' if one==two else 'FAIL','route_count':len(one),'changed':[k for k in one if one[k]!=two[k]]}
    class Quiet(SimpleHTTPRequestHandler):
        def log_message(self,*args): pass
    old=Path.cwd(); os.chdir(docs); srv=ThreadingHTTPServer(('127.0.0.1',0),Quiet); threading.Thread(target=srv.serve_forever,daemon=True).start(); base=f'http://127.0.0.1:{srv.server_address[1]}/'; routes={}
    try:
        for p in sorted(docs.glob('*.html')):
            with urlopen(base+p.name,timeout=5) as response:
                body=response.read(); routes[p.name]={'status':response.status,'bytes':len(body),'page_not_found_text':b'Page not found' in body}
    finally: srv.shutdown(); srv.server_close(); os.chdir(old)
    result['local_http']={'routes':routes,'all_200':all(v['status']==200 for v in routes.values()),'custom_404_direct':routes.get('404.html')}
    assets={}
    for key,name in [('readme','officecraft-readme-hero.png'),('pages','officecraft-pages-hero.png'),('social','officecraft-social-card.jpg')]:
        p=docs/'assets'/name; data=p.read_bytes()
        if data[:8]==b'\x89PNG\r\n\x1a\n': width,height=struct.unpack('>II',data[16:24])
        else:
            if data[:2]!=b'\xff\xd8': raise RuntimeError(f'unsupported image format: {p}')
            offset=2; sof={0xC0,0xC1,0xC2,0xC3,0xC5,0xC6,0xC7,0xC9,0xCA,0xCB,0xCD,0xCE,0xCF}
            while offset+3<len(data):
                if data[offset]!=0xFF: offset+=1; continue
                while offset<len(data) and data[offset]==0xFF: offset+=1
                marker=data[offset]; offset+=1
                if marker in {0xD8,0xD9}: continue
                length=struct.unpack('>H',data[offset:offset+2])[0]
                if marker in sof: height,width=struct.unpack('>HH',data[offset+3:offset+7]); break
                offset+=length
            else: raise RuntimeError(f'JPEG dimensions not found: {p}')
        assets[key]={'path':p.relative_to(root).as_posix(),'width':width,'height':height,'sha256':hashlib.sha256(data).hexdigest()}
    result['assets']=assets; result['asset_distinct']={'hashes':len({v['sha256'] for v in assets.values()})==3,'ratios':len({round(v['width']/v['height'],6) for v in assets.values()})==3}
    workflows={}
    for p in sorted((root/'.github/workflows').glob('*.yml')):
        text=p.read_text('utf-8'); workflows[p.name]={'push':bool(re.search(r'^\s+push:',text,re.M)),'pull_request':bool(re.search(r'^\s+pull_request:',text,re.M)),'schedule':bool(re.search(r'^\s+schedule:',text,re.M)),'workflow_dispatch':bool(re.search(r'^\s+workflow_dispatch:',text,re.M))}
    result['workflows']=workflows
    names=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard'],cwd=root,text=True,encoding='utf-8').splitlines(); paths=sorted({p.replace('\\','/') for p in names if p and not p.replace('\\','/').startswith('verification/remediation-2026-08-12/') and (root/p).is_file()}); aggregate=hashlib.sha256()
    for rel in paths:
        digest=hashlib.sha256((root/rel).read_bytes()).digest(); aggregate.update(rel.encode()); aggregate.update(b'\0'); aggregate.update(digest); aggregate.update(b'\n')
    result['governed_candidate']={'file_count':len(paths),'fingerprint':aggregate.hexdigest()}; result['governed_worktree_clean']=subprocess.run(['git','diff','--quiet','HEAD','--','.github','README.md','CONTRIBUTING.md','docs','requirements-docs.txt','scripts'],cwd=root).returncode==0
    checks=[one==two,len(routes)==19,result['local_http']['all_200'],routes['404.html']['page_not_found_text'],result['asset_distinct']['hashes'],result['asset_distinct']['ratios'],(not workflows.get('line-ending-policy.yml',{}).get('push')) and workflows.get('line-ending-policy.yml',{}).get('pull_request') and (not workflows.get('line-ending-policy.yml',{}).get('schedule')) and workflows.get('line-ending-policy.yml',{}).get('workflow_dispatch') and workflows.get('deploy-pages.yml',{}).get('push') and (not workflows.get('deploy-pages.yml',{}).get('pull_request')) and (not workflows.get('deploy-pages.yml',{}).get('schedule')) and workflows.get('deploy-pages.yml',{}).get('workflow_dispatch'),result['governed_candidate']=={'file_count':123,'fingerprint':'bd5768c530d3d643d6258366db9b9c085f7d030124ae2951d372a5668df97ec8'},result['governed_worktree_clean']]
    result['unresolved_live_oracle']='GitHub Pages missing-route dispatch and current live bytes are verified only after publication'; result['status']='PASS' if all(checks) else 'FAIL'; Path(args.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n'); print(json.dumps({'status':result['status'],'commit':result['target_commit'],'routes':len(routes),'fingerprint':result['governed_candidate']},indent=2)); return 0 if result['status']=='PASS' else 1
if __name__=='__main__': raise SystemExit(main())
