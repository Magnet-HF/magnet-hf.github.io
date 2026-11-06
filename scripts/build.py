"""Build the MagNet library from Markdown. Run with Python 3.11+."""
from pathlib import Path
import html
import json
import re
import shutil
import sys
from urllib.parse import urlparse, unquote
from html.parser import HTMLParser
import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
REPO = 'https://github.com/Magnet-HF/magnet-hf.github.io'
NAV = [('Start here','/start-here/'),('Software','/software/'),
       ('Operational guidance','/operational-guidance/'),('Radio setup','/radio-configurations/'),
       ('Resources','/resources/'),('Contribute','/contribute/')]

def read_page(path):
    text = path.read_text()
    if not text.startswith('---\n'):
        raise ValueError(f'{path}: missing JSON metadata block')
    _, header, body = text.split('---', 2)
    meta = json.loads(header)
    for key in ('title', 'description', 'section', 'updated'):
        if not meta.get(key):
            raise ValueError(f'{path}: missing {key}')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', meta['updated']):
        raise ValueError(f'{path}: updated must be YYYY-MM-DD')
    return meta, body

def card(p):
    m = p['meta']
    badge = f'<span class="badge">{html.escape(m.get("kind",m["section"]))}</span>'
    return f'<a class="card" href="{p["url"]}">{badge}<h3>{html.escape(m["title"])}</h3><p>{html.escape(m["description"])}</p><span class="card-link">Explore <span aria-hidden="true">↗</span></span></a>'

def render(p, pages):
    m = p['meta']
    body = markdown.markdown(p['body'], extensions=['tables','fenced_code','toc','sane_lists'])
    collection = m.get('collection')
    if collection:
        chosen = [x for x in pages if x['meta'].get('section') == collection and x['url'] != p['url'] and x['meta'].get('listed',True)]
        chosen.sort(key=lambda x:(x['meta'].get('order',100),x['meta']['title'].lower()))
        body += '<div class="card-grid">'+''.join(card(x) for x in chosen)+'</div>'
    home = p['url'] == '/'
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if p['url'].startswith(url) else '')+f'>{label}</a>' for label,url in NAV)
    edit = f'{REPO}/edit/main/content/{p["relative"]}'
    title = html.escape(m['title']); desc = html.escape(m['description'],quote=True)
    hero = '' if not home else '<div class="hero-actions"><a class="button" href="/software/">Find software <span aria-hidden="true">→</span></a><a class="button secondary" href="/operational-guidance/">Set up your station</a></div><div class="home-stats"><span>11 tool pages</span><span>Official sources</span><span>Community guidance</span></div>'
    kicker = 'TOOLS & GUIDES' if home else m['section'].replace('-',' ').upper()
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · MagNet</title><meta name="description" content="{desc}">
<link rel="icon" href="/assets/magnet-logo.png" type="image/png"><link rel="stylesheet" href="/assets/site.css">
<script src="/assets/site.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="header-inner">
<a class="brand" href="/" aria-label="MagNet Tools and Guides home"><img src="/assets/magnet-logo.png" width="88" height="88" alt="MagNet — Mutual Assistance Group Network"><span><small>MAGNET HF</small>Tools & Guides</span></a>
<nav class="top-links" aria-label="External"><a href="https://magnethf.com/">MagNet website ↗</a><a href="https://github.com/Magnet-HF">GitHub ↗</a></nav></div></header>
<div class="site-shell"><aside class="sidebar"><p class="nav-label">RESOURCE LIBRARY</p><nav aria-label="Main">{nav}</nav>
<div class="sidebar-note"><span class="signal-dot"></span> Built for operators<p>Software, station setup, and guidance in one place.</p><a href="/software/spotterx/">SpotterX project →</a></div></aside>
<main id="main"><div class="eyebrow">MAGNET HF <span>/</span> {html.escape(kicker)}</div>
<section class="page-heading {'home-heading' if home else ''}"><h1>{title}</h1><p class="lead">{desc}</p>{hero}</section>
<article class="prose">{body}</article>
<div class="page-meta"><span>Page updated {m['updated']}</span><a href="{edit}">Suggest an edit ↗</a></div></main></div>
<footer><span>MAGNET HF · Tools & Guides</span><span><a href="/contribute/">Help improve this library</a> · <a href="https://magnethf.com/contact-us/">Contact MagNet</a></span></footer></body></html>'''

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='a' and a.get('href'): self.links.append(a['href'])
        if tag in ('img','script') and a.get('src'): self.links.append(a['src'])
        if tag=='link' and a.get('href'): self.links.append(a['href'])

def validate():
    errors=[]
    for file in OUT.rglob('*.html'):
        parser=Links(); parser.feed(file.read_text())
        for href in parser.links:
            u=urlparse(href)
            if u.scheme or u.netloc: continue
            target=(OUT/unquote(u.path).lstrip('/')) if u.path.startswith('/') else file.parent/unquote(u.path)
            if not u.path: target=file
            if target.is_dir(): target=target/'index.html'
            if not target.exists(): errors.append(f'{file.relative_to(OUT)} → {href}')
            elif u.fragment and target.suffix=='.html':
                dest=Links(); dest.feed(target.read_text())
                if unquote(u.fragment) not in dest.ids: errors.append(f'Unknown anchor: {file.relative_to(OUT)} → {href}')
    if errors: raise ValueError('Broken internal links:\n'+'\n'.join(errors))

def build():
    pages=[]
    for path in sorted((ROOT/'content').rglob('*.md')):
        meta,body=read_page(path)
        relative=path.relative_to(ROOT/'content')
        url='/' + str(relative.parent).replace('\\','/')+'/' if relative.name=='index.md' else '/'+str(relative.with_suffix(''))+'/'
        url=url.replace('/./','/')
        pages.append(dict(meta=meta,body=body,url=url,relative=relative.as_posix()))
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    for folder in ('assets','documents'):
        if (ROOT/folder).exists(): shutil.copytree(ROOT/folder,OUT/folder)
    for p in pages:
        dest=OUT/p['url'].lstrip('/')/'index.html'; dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(render(p,pages))
    (OUT/'search.json').write_text(json.dumps([{'title':p['meta']['title'],'description':p['meta']['description'],'url':p['url'],'section':p['meta']['section']} for p in pages if p['meta'].get('listed',True)]))
    (OUT/'.nojekyll').touch()
    (OUT/'404.html').write_text((OUT/'help/index.html').read_text().replace('<h1>Help & troubleshooting</h1>','<h1>Page not found</h1>'))
    validate()
    print(f'Built {len(pages)} pages; all internal links and anchors passed.')

if __name__=='__main__': build()
