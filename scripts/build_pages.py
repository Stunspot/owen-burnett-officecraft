#!/usr/bin/env python3
"""Build committed static documentation pages without network or GitHub Actions."""
from pathlib import Path
import re
from markdown_it import MarkdownIt

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
SOURCES=[p for p in sorted(DOCS.glob('*.md')) if p.name!='SITE-SOURCE.md']
md=MarkdownIt('commonmark',{'html':True}).enable('table')

def title(text):
    m=re.search(r'^#\s+(.+)$',text,re.M)
    return m.group(1).strip() if m else 'Officecraft documentation'

def links(text):
    text=re.sub(r'\(([^)]+)\.md(#[^)]+)?\)',lambda m:'('+m.group(1)+'.html'+(m.group(2) or '')+')',text)
    text=text.replace('(../SUPPORT.html)','(SUPPORT.html)').replace('(../SECURITY.html)','(SECURITY.html)')
    text=text.replace('(../LICENSE.html)','(https://github.com/Stunspot/owen-burnett-officecraft/blob/main/LICENSE.md)')
    return text

def shell(page_title,body):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{page_title} | Owen Burnett Officecraft</title><meta name="description" content="Customer documentation for coherent documents, decks, workbooks, PDFs, and office packets.">
<meta name="theme-color" content="#08141d"><link rel="stylesheet" href="style.css">
<meta property="og:type" content="website"><meta property="og:site_name" content="Owen Burnett Officecraft"><meta property="og:title" content="{page_title} | Owen Burnett Officecraft"><meta property="og:description" content="Documents, decks, workbooks, and PDFs that still agree."><meta property="og:image" content="https://stunspot.github.io/owen-burnett-officecraft/assets/officecraft-social-card.jpg"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Owen Burnett Officecraft. Documents, decks, workbooks, and PDFs that still agree."><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://stunspot.github.io/owen-burnett-officecraft/assets/officecraft-social-card.jpg"><meta name="twitter:image:alt" content="Owen Burnett Officecraft. Documents, decks, workbooks, and PDFs that still agree.">
</head><body><a class="skip-link" href="#main">Skip to content</a><header class="site-header"><nav aria-label="Primary"><a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">OB</span><span>Officecraft</span></a><div class="nav-links"><a href="START-HERE.html">Start</a><a href="FIRST-JOB.html">First job</a><a href="OFFICEFILE-AND-RESUME.html">Officefile</a><a href="TRUST-PRIVACY-AND-LIMITS.html">Trust</a><a href="TROUBLESHOOTING.html">Recover</a><a href="README.html">All docs</a></div></nav></header><main id="main" class="doc-page">{body}</main><footer><p><strong>Owen Burnett Officecraft</strong> · Collaborative Dynamics · Free dual-host occupational Augment.</p><p><a href="index.html">Product site</a> · <a href="SUPPORT.html">Support</a> · <a href="https://github.com/Stunspot/owen-burnett-officecraft">GitHub</a> · <a href="https://github.com/Stunspot/owen-burnett-officecraft/blob/main/LICENSE.md">MIT License</a></p></footer></body></html>'''

def main():
    built=[]
    for source in SOURCES:
        text=source.read_text(encoding='utf-8')
        target=source.with_suffix('.html')
        target.write_text(shell(title(text),md.render(links(text))),encoding='utf-8',newline='\n')
        built.append(target.name)
    print({'status':'PASS','pages':len(built),'built':built})
if __name__=='__main__': main()