# -*- coding: utf-8 -*-
"""Génère sitemap.xml pour www.myxavier.finance à partir des pages réellement servies.

Règles :
- une URL par index.html du site racine (les sites éditeur actuarius/ et actuarius-press/
  ont leur propre domaine et ne sont pas listés) ;
- les pages en noindex (mentions légales, confidentialité, merci) sont exclues ;
- les URL redirigées par _redirects (pages livres → sites éditeur) ne sont jamais listées ;
- lastmod = date du dernier commit git touchant le fichier (sinon date du jour) ;
- les alternates hreflang sont relus dans le <head> de chaque page (source unique).

Usage : python3 gen/build_sitemap.py
"""
import os, re, subprocess, datetime, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://www.myxavier.finance"
EXCLUDE_DIRS = {'actuarius', 'actuarius-press', 'brand_assets', 'gen', 'node_modules',
                'Business', 'Website building', '01 Daily Logs', '.git', '.netlify'}

def redirected_prefixes():
    """Chemins qui font l'objet d'une règle 301 dans _redirects (préfixe sans le /*)."""
    out = []
    path = os.path.join(ROOT, '_redirects')
    if not os.path.exists(path):
        return out
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) >= 3 and parts[2].startswith('301') and parts[0].startswith('/'):
            out.append(parts[0].rstrip('*'))
    return out

def lastmod(path):
    try:
        d = subprocess.check_output(['git', 'log', '-1', '--format=%cs', '--', path],
                                    cwd=ROOT, stderr=subprocess.DEVNULL).decode().strip()
        if d:
            return d
    except Exception:
        pass
    return datetime.date.today().isoformat()

def pages():
    redir = redirected_prefixes()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT)
        top = rel.split(os.sep)[0]
        if top in EXCLUDE_DIRS:
            dirnames[:] = []
            continue
        if 'index.html' not in filenames:
            continue
        url_path = '/' if rel == '.' else '/' + rel.replace(os.sep, '/') + '/'
        if any(url_path.startswith(p) for p in redir):
            continue
        html = open(os.path.join(dirpath, 'index.html'), encoding='utf-8').read()
        if re.search(r'<meta name="robots" content="[^"]*noindex', html):
            continue
        alts = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', html)
        yield url_path, os.path.join(rel, 'index.html') if rel != '.' else 'index.html', alts

def build():
    entries = sorted(pages(), key=lambda e: (e[0].count('/'), e[0]))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
             '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url_path, file, alts in entries:
        lines.append('  <url>')
        lines.append(f'    <loc>{BASE}{url_path}</loc>')
        for lang, href in alts:
            lines.append(f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}"/>')
        lines.append(f'    <lastmod>{lastmod(file)}</lastmod>')
        lines.append('  </url>')
    lines.append('</urlset>')
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    return len(entries)

if __name__ == '__main__':
    n = build()
    print(f"sitemap.xml : {n} URL")
