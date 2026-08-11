# -*- coding: utf-8 -*-
# Génère le site boutique Éditions Actuarius dans actuarius/ (FR à la racine, EN sous /en/).
# Déploiement : second site Netlify sur le même repo, publish directory = "actuarius",
# domaine = www.editionsactuarius.fr (+ actuariuspress.com en alias/redirection).
# Les liens d'achat viennent du dict SHOP de publications_data.py (source unique).
import os, sys, json, html
sys.path.insert(0, os.path.dirname(__file__))
from publications_data import UI, BOOKS, SHOP
from build_publications import cover_svg, buy_buttons, shop_of, LEMON_JS, ACT_MARK_INV

ACT_BASE = "https://www.editionsactuarius.fr"
MAIN = "https://www.myxavier.finance"

ACT = {
 'fr': dict(
    lang='fr', dir='', other='/en/', other_label='EN',
    title="Éditions Actuarius — Traités techniques finance & assurance",
    desc="Éditions Actuarius publie des traités techniques de référence en finance et assurance : comptabilité des placements, prudentiel, contrôles. PDF, papier et Kindle.",
    tagline="Traités techniques finance &amp; assurance",
    intro="L'<em>actuarius</em> tenait les registres et les comptes de Rome. Éditions Actuarius publie des traités écrits depuis la pratique : comptabilité des placements, règles prudentielles et contrôles, avec écritures complètes et dossiers chiffrés.",
    extract="Lire les premières pages",
    upcoming="Bientôt disponible ici",
    author_t="L'auteur",
    author_b='Xavier Robitaille conseille assureurs et institutions financières sur leurs sujets finance, comptabilité, investissements et réglementaire. Profil complet sur <a href="%s/fr/">myxavier.finance</a>.' % MAIN,
    legal="Éditions Actuarius est la marque d'édition de Xavier Advisory.",
    contact="Contact",
 ),
 'en': dict(
    lang='en', dir='en/', other='/', other_label='FR',
    title="Éditions Actuarius — Technical books on finance & insurance",
    desc="Éditions Actuarius publishes reference technical books on finance and insurance: investment accounting, prudential rules, controls. PDF, paperback and Kindle.",
    tagline="Technical books on finance &amp; insurance",
    intro="The <em>actuarius</em> kept Rome's registers and accounts. Éditions Actuarius publishes books written from practice: investment accounting, prudential rules and controls, with full accounting entries and worked cases.",
    extract="Read the first pages",
    upcoming="Coming soon to this shop",
    author_t="The author",
    author_b='Xavier Robitaille advises insurers and financial institutions on finance, accounting, investment and regulatory topics. Full profile at <a href="%s/">myxavier.finance</a>.' % MAIN,
    legal="Éditions Actuarius is the publishing imprint of Xavier Advisory.",
    contact="Contact",
 ),
}

CSS = """
:root{--primary:#0B1530;--gold:#C79A3B;--text:#2A3345;--gray:#6B7280;--light:#F5F2EB;--white:#fff}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',Arial,sans-serif;color:var(--text);background:var(--light);line-height:1.6}
.wrap{max-width:1080px;margin:0 auto;padding:0 1.4rem}
a{color:var(--gold)}
header.hero{background:var(--primary);color:#F5F2EB;padding:4.2rem 0 3.6rem;text-align:center}
.wordmark .wm-l1{font-size:.82rem;letter-spacing:.55em;color:var(--gold);text-transform:uppercase;padding-left:.55em}
.wordmark .wm-rule{width:170px;height:1px;background:var(--gold);margin:.8rem auto}
.wordmark .wm-l2{font-family:'EB Garamond',Georgia,serif;font-size:clamp(2.3rem,6vw,3.4rem);font-weight:600;letter-spacing:.14em;color:#F5F2EB;padding-left:.14em}
.hero .tagline{margin-top:1.1rem;font-size:.95rem;color:#C7CCD6;letter-spacing:.04em}
.hero .langsw{position:absolute;top:1.2rem;right:1.6rem}
.hero .langsw a{color:#C7CCD6;text-decoration:none;font-size:.8rem;letter-spacing:.1em}
.hero{position:relative}
.intro{max-width:720px;margin:2.6rem auto 0;text-align:center;font-size:1rem;line-height:1.8}
.intro em{font-family:'EB Garamond',Georgia,serif}
.shop{padding:3.4rem 0 4rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:2rem}
.bk{background:var(--white);border-top:3px solid var(--gold);box-shadow:0 8px 24px rgba(11,21,48,.07);padding:1.6rem;display:flex;flex-direction:column;gap:1rem}
.bk .cw{display:flex;justify-content:center;background:var(--light);padding:1.4rem 0}
.bk .cw svg{width:210px;height:auto;box-shadow:0 12px 28px rgba(11,21,48,.3)}
.bk h3{font-family:'EB Garamond',Georgia,serif;font-size:1.22rem;color:var(--primary);line-height:1.25}
.bk p{font-size:.88rem;line-height:1.65;color:#4B5364}
.bk .extract{font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;margin-top:auto}
.btn-gold{display:inline-block;background:var(--gold);color:#fff;text-decoration:none;padding:.75rem 1.4rem;border-radius:3px;font-weight:700;font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;transition:transform .2s}
.btn-gold:hover{transform:translateY(-2px)}
.btn-buy2{display:inline-block;background:transparent;color:var(--primary);text-decoration:none;padding:.68rem 1.2rem;border:1.5px solid var(--primary);border-radius:3px;font-weight:700;font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;transition:transform .2s,background .2s,color .2s}
.btn-buy2:hover{background:var(--primary);color:#fff;transform:translateY(-2px)}
.btn-gold:focus-visible,.btn-buy2:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.buy-row{display:flex;gap:.6rem;flex-wrap:wrap}
.buy-price{font-weight:800;margin-left:.4rem}
.buy-note{font-size:.74rem;color:var(--gray);margin-top:.5rem}
.upcoming{font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold)}
.author{background:var(--white);padding:3rem 0}
.author h2{font-family:'EB Garamond',Georgia,serif;color:var(--primary);margin-bottom:.8rem}
.author p{max-width:680px}
footer{background:var(--primary);color:#C7CCD6;padding:2rem 0;font-size:.8rem}
footer .wrap{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap}
footer a{color:#C7CCD6}
"""

def esc(s): return html.escape(s, quote=False)

def page(lang):
    a, ui = ACT[lang], UI[lang]
    url_self = ACT_BASE + '/' + a['dir']
    url_fr, url_en = ACT_BASE + '/', ACT_BASE + '/en/'
    ld = json.dumps({"@context": "https://schema.org", "@type": "Organization",
                     "name": "Éditions Actuarius", "url": ACT_BASE,
                     "parentOrganization": {"@type": "Organization", "name": "Xavier Advisory", "url": MAIN},
                     "founder": {"@type": "Person", "name": "Xavier Robitaille"}}, ensure_ascii=False)
    cards = ''
    for slug, b in BOOKS.items():
        desc = b['en_desc'] if lang == 'en' else b['fr_desc']
        preview = f"{MAIN}{'/publications/' if lang == 'en' else '/fr/publications/'}{slug}/"
        buy = buy_buttons(slug, ui) or f'<span class="upcoming">{a["upcoming"]}</span>'
        cards += f"""<div class="bk">
  <div class="cw">{cover_svg(b)}</div>
  <h3>{esc(b['name'])}</h3>
  <p>{esc(desc)}</p>
  <a class="extract" href="{preview}">{a['extract']} &rarr;</a>
  {buy}
</div>\n"""
    lemon = LEMON_JS if any(shop_of(sl) and SHOP[sl].get('ls') for sl in BOOKS) else ''
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{a['title']}</title>
<meta name="description" content="{a['desc']}">
<link rel="canonical" href="{url_self}">
<link rel="alternate" hreflang="fr" href="{url_fr}">
<link rel="alternate" hreflang="en" href="{url_en}">
<link rel="alternate" hreflang="x-default" href="{url_fr}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Éditions Actuarius">
<meta property="og:title" content="{a['title']}">
<meta property="og:description" content="{a['desc']}">
<meta property="og:url" content="{url_self}">
<link rel="icon" type="image/svg+xml" href="/actuarius-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&family=EB+Garamond:ital,wght@0,500;0,600;0,700;1,500&display=swap" rel="stylesheet">
<script type="application/ld+json">{ld}</script>
<style>{CSS}</style>{lemon}
</head>
<body>
<header class="hero"><div class="wrap">
  <div class="langsw"><a href="{a['other']}" rel="alternate">{a['other_label']}</a></div>
  <div class="wordmark">
    <div style="width:88px;margin:0 auto .9rem">{ACT_MARK_INV}</div>
    <div class="wm-l1">Éditions</div>
    <div class="wm-rule"></div>
    <div class="wm-l2">ACTUARIUS</div>
  </div>
  <p class="tagline">{a['tagline']}</p>
  <p class="intro">{a['intro']}</p>
</div></header>
<section class="shop"><div class="wrap">
  <div class="grid">{cards}</div>
</div></section>
<section class="author"><div class="wrap">
  <h2>{a['author_t']}</h2>
  <p>{a['author_b']}</p>
</div></section>
<footer><div class="wrap">
  <span>&copy; 2026 Éditions Actuarius &mdash; {a['legal']}</span>
  <span><a href="mailto:welcome@myxavier.finance">{a['contact']}</a></span>
</div></footer>
</body></html>"""

if __name__ == '__main__':
    import shutil
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, 'actuarius')
    os.makedirs(os.path.join(out, 'en'), exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page('fr'))
    open(os.path.join(out, 'en', 'index.html'), 'w', encoding='utf-8').write(page('en'))
    shutil.copy(os.path.join(root, 'brand_assets', 'actuarius-mark.svg'), out)
    print("Site Actuarius généré (fr + en)")
