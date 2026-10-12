#!/usr/bin/env python3
"""Build a complete Officecraft candidate in a new output directory; retain all prior releases."""
import argparse, hashlib, json, os, tempfile
from pathlib import Path
from archive_paths import assert_chain, check_tree, check_members, atomic_zip
from verify_customer_release import verify
ROOT=Path(__file__).resolve().parents[1]
SKILLS=('owen-burnett-officecraft','officecraft-reviewer')
ROOT_FILES=('.gitattributes','README.md','START-HERE.md','LICENSE.md','RELEASE-NOTES.md','CHANGELOG.md','HOST-MATRIX.md','SUPPORT.md','SECURITY.md','CONTRIBUTING.md','requirements-docs.txt','VERSION')
SOURCE_DIRS=('codex','docs','tools','scripts','tests','.github')


def selected(root):
    return check_tree(root,[p for p in root.rglob('*')if p.is_file()and '__pycache__'not in p.parts and p.suffix not in ('.pyc','.pyo')])


def sha(data):return hashlib.sha256(data).hexdigest()


def build(output, root=ROOT):
    root=assert_chain(root);output=assert_chain(output,allow_missing=True)
    if os.path.lexists(output):raise ValueError('Output already exists; use a new candidate directory')
    if not output.is_relative_to(root) or output==root or any(output.is_relative_to(root/n)for n in SOURCE_DIRS):raise ValueError('Output must be a new repository directory outside maintained source trees')
    version=(root/'VERSION').read_text(encoding='utf-8-sig').strip()
    if version!='0.2.1':raise ValueError('Review release identity before changing version')
    source=[]
    for n in ROOT_FILES:
        p=assert_chain(root/n);source.append((n,p.read_bytes()))
    for directory in SOURCE_DIRS:
        source.extend((directory+'/'+n,b)for n,b in selected(root/directory))
    check_members(source)
    source_prefix='source/owen-burnett-officecraft-v'+version
    files=[(source_prefix+'/'+n,b)for n,b in source]
    files.extend((n,(root/'tools'/n.split('/')[-1]).read_bytes())for n in ['tools/archive_paths.py','tools/verify_customer_release.py'])
    skills={}
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.officecraft-candidate-',dir=output.parent)as tmp:
        stage=Path(tmp);candidate=stage/'candidate';candidate.mkdir();package=candidate/'package';package.mkdir()
        for skill in SKILLS:
            runtime=selected(root/'codex'/skill);files.extend(('codex/'+skill+'/'+n,b)for n,b in runtime)
            name='claude/'+skill+'-v'+version+'.zip';archive=stage/name
            atomic_zip([(skill+'/'+n,b)for n,b in runtime],archive);payload=archive.read_bytes();files.append((name,payload));skills[skill]={'file_count':len(runtime),'claude_zip':name,'claude_sha256':sha(payload)}
        guide='# Owen Burnett Officecraft '+version+'\n\nThis folder, containing release-manifest.json, is the package root. Install both matched folders from codex/ for Codex, or upload both intact archives from claude/ for Claude. Detailed guidance is in ['+source_prefix+'/START-HERE.md]('+source_prefix+'/START-HERE.md); its source documentation is nested, while the Claude archives remain here at the package root. From this package root, run python tools/verify_customer_release.py --root . after extraction. Extract into a short directory path of at most 70 UTF-16 code units. Preserve existing Officefiles; use the copy-first migration guide for older records.\n\nPackage verification proves byte custody and matched channels. It does not prove native rendering, calculation, host discovery or readiness for a particular use.\n'
        files.extend([('START-HERE.md',guide.encode()),('LICENSE.md',(root/'LICENSE.md').read_bytes())])
        sums=''.join(sha(b)+'  '+n+'\n'for n,b in sorted(files)if n.startswith(('codex/','claude/')));files.append(('SHA256SUMS.txt',sums.encode()))
        manifest={'schema':'collaborative-dynamics.customer-skill-family/v3','slug':'owen-burnett-officecraft','version':version,'skills':skills,'source':{'path':source_prefix,'file_count':len(source)},'files':[{'path':n,'bytes':len(b),'sha256':sha(b)}for n,b in sorted(files)]}
        files.append(('release-manifest.json',(json.dumps(manifest,indent=2)+'\n').encode()));prefix='Owen-Burnett-Officecraft-v'+version;check_members([(prefix+'/'+n,b)for n,b in files])
        for n,b in files:
            p=package/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
        proof=verify(package);outer=candidate/(prefix+'.zip');atomic_zip([(prefix+'/'+n,b)for n,b in files],outer)
        digest=sha(outer.read_bytes());(candidate/(outer.name+'.sha256')).write_text(digest+'  '+outer.name+'\n',encoding='utf-8',newline='\n')
        receipt={'version':version,'archive':outer.name,'sha256':digest,'runtime_files':sum(x['file_count']for x in skills.values()),'verification':proof};(candidate/'build-record.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
        assert_chain(output.parent)
        if os.path.lexists(output):raise ValueError('Output appeared during build; preserving it')
        os.rename(candidate,output)
    return {'output':str(output),**receipt}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output-dir',required=True,type=Path);a=p.parse_args()
    try:print(json.dumps(build(a.output_dir),indent=2));return 0
    except (OSError,ValueError,KeyError,TypeError)as exc:print('Candidate not built: '+str(exc));return 2
if __name__=='__main__':raise SystemExit(main())