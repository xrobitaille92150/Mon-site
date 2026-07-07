# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages_data import PAGES

BASE = "https://www.myxavier.finance"
MARK = '<svg class="xa-mark" viewBox="0 0 1000 1000" aria-hidden="true"><polygon points="880,145.79 722.57,145.79 559.71,371.07 714.43,371.07" fill="var(--gold)"/><polygon points="426.71,623.5 277.43,623.5 120,851.5 261.14,851.5" fill="var(--gold)"/><polygon points="128.14,148.5 679.14,851.5 855.57,854.21 312.71,148.5" fill="currentColor"/></svg>'
WORD = '<span class="xa-word"><span class="xa-name">X<em>A</em>V<em>I</em>ER</span><small><span>A</span><span>D</span><span>V</span><span>I</span><span>S</span><span>O</span><span>R</span><span>Y</span></small></span>'

CSS = """
:root { --primary:#0B1530; --text:#0B1530; --gold:#C79A3B; --gold-light:#D9A24A; --light-bg:#F5F2EB; --white:#FFF; --gray:#6B7280; --border:rgba(11,21,48,0.1); }
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box} html{scroll-behavior:smooth}
body{font-family:'Montserrat',sans-serif;color:var(--text);background:var(--light-bg);-webkit-font-smoothing:antialiased}
h1,h2{font-family:'Playfair Display',serif}
nav{position:sticky;top:0;z-index:100;background:var(--primary);padding:1.1rem 0}
.nav-inner{max-width:1080px;margin:0 auto;padding:0 2rem;display:flex;align-items:center;justify-content:space-between}
.nav-logo{display:inline-flex;align-items:center;gap:.7rem;color:#fff;text-decoration:none}
.xa-mark{height:46px;width:46px;display:block;flex-shrink:0}
.xa-word{display:flex;flex-direction:column;line-height:1;font-family:'Playfair Display',serif;font-weight:600;font-size:1.15rem;letter-spacing:.28em;color:#fff}
.xa-name{display:block;white-space:nowrap;margin-right:-.28em}
.xa-word em{font-style:normal;color:var(--gold)}
.xa-word small{font-family:'Montserrat',sans-serif;font-size:.55rem;font-weight:500;letter-spacing:0;margin-top:4px;color:rgba(255,255,255,.72);display:flex;justify-content:space-between}
.nav-right{display:flex;align-items:center;gap:1.4rem}
.nav-right a{color:rgba(255,255,255,.75);text-decoration:none;font-size:.78rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase}
.nav-right a:hover,.nav-right a:focus-visible{color:#fff}
.nav-cta{background:var(--gold);color:#fff !important;padding:.55rem 1.2rem;border-radius:3px}
.hero{background:var(--primary);color:#fff;padding:4.5rem 0 4rem}
.wrap{max-width:1080px;margin:0 auto;padding:0 2rem}
.label{display:inline-flex;align-items:center;gap:.6rem;font-size:.7rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
.label::before{content:"";width:26px;height:2px;background:var(--gold)}
.hero h1{font-size:clamp(2.1rem,4.5vw,3.4rem);font-weight:700;line-height:1.12;letter-spacing:-.01em;margin:.9rem 0 1.2rem}
.hero p{max-width:640px;font-size:1.02rem;line-height:1.7;color:rgba(255,255,255,.82)}
section{padding:3.6rem 0}
section h2{font-size:clamp(1.5rem,2.6vw,2.1rem);font-weight:700;margin-bottom:1.3rem}
.prose p{max-width:680px;line-height:1.75;margin-bottom:1rem;color:#2A3345}
ul.deliver{list-style:none;max-width:720px}
ul.deliver li{padding:.9rem 0 .9rem 1.6rem;border-bottom:1px solid var(--border);line-height:1.65;color:#2A3345;position:relative}
ul.deliver li::before{content:"";position:absolute;left:0;top:1.45rem;width:9px;height:9px;background:var(--gold)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.2rem;margin-top:1.4rem}
.card{background:var(--white);border-top:3px solid var(--gold);padding:1.4rem 1.5rem;box-shadow:0 8px 24px rgba(11,21,48,.07)}
.card h3{font-size:.98rem;font-weight:700;margin-bottom:.55rem;color:var(--primary)}
.card p{font-size:.88rem;line-height:1.65;color:#4B5364}
.cta{background:var(--primary);color:#fff;text-align:center;padding:4rem 0}
.cta h2{color:#fff}
.cta p{color:rgba(255,255,255,.8);max-width:560px;margin:0 auto 1.6rem;line-height:1.7}
.btn-gold{display:inline-block;background:var(--gold);color:#fff;text-decoration:none;padding:.9rem 2rem;border-radius:3px;font-weight:700;font-size:.85rem;letter-spacing:.1em;text-transform:uppercase;transition:transform .2s}
.btn-gold:hover{transform:translateY(-2px)}
.cta .alt{display:block;margin-top:1.1rem;color:rgba(255,255,255,.7);font-size:.9rem}
.cta .alt a{color:var(--gold-light)}
footer{background:var(--primary);border-top:1px solid rgba(255,255,255,.12);padding:1.6rem 0;color:rgba(255,255,255,.6);font-size:.8rem}
footer .wrap{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap}
footer a{color:rgba(255,255,255,.75);text-decoration:none;margin-left:1.2rem}
.breadcrumb{font-size:.78rem;margin-bottom:1rem}
.breadcrumb a{color:rgba(255,255,255,.6);text-decoration:none}
.breadcrumb a:hover{color:#fff}
@media (max-width:640px){.nav-right a.nav-link{display:none}}
"""

NAV_LINKS = {
 'en': [('Expertise','/#expertise'),('Profile','/#profile'),('Approach','/#approach'),('Insights','/insights/'),('Training','/formation/')],
 'fr': [('Expertise','/fr/#expertise'),('Profil','/fr/#profile'),('Approche','/fr/#approach'),('D&eacute;cryptages','/fr/insights/'),('Formation','/fr/formation/')],
}

def base_path(slug):
    return slug if slug == 'formation' else f"expertise/{slug}"
STR = {
 'en': dict(home='/', contact='Contact', cta_h="Available now for new mandates", cta_p="Full remote, hybrid or on-site, in France and internationally. French and English.", cta_btn="Book a call &rarr;", cta_alt='or write to <a href="mailto:welcome@myxavier.finance">welcome@myxavier.finance</a>', back="&larr; All expertise", lang_link_label="FR", crumb="Expertise"),
 'fr': dict(home='/fr/', contact='Contact', cta_h="Disponible imm&eacute;diatement pour de nouvelles missions", cta_p="Remote, hybride ou sur site, en France et &agrave; l'international. Fran&ccedil;ais et anglais.", cta_btn="R&eacute;server un appel &rarr;", cta_alt='ou &eacute;crivez &agrave; <a href="mailto:welcome@myxavier.finance">welcome@myxavier.finance</a>', back="&larr; Toute l'expertise", lang_link_label="EN", crumb="Expertise"),
}

def jsonld(slug, lang, d):
    url = f"{BASE}/{base_path(slug)}/" if lang=='en' else f"{BASE}/fr/{base_path(slug)}/"
    import json
    return json.dumps({
      "@context":"https://schema.org","@type":"Service",
      "@id":url+"#service",
      "name":d['title'].split(' | ')[0],
      "description":d['desc'],
      "url":url,
      "inLanguage":"en" if lang=='en' else "fr",
      "provider":{"@type":"ProfessionalService","name":"Xavier Advisory","url":BASE+"/", "founder":{"@type":"Person","name":"Xavier Robitaille"}},
      "areaServed":["FR","EU","International"]
    }, ensure_ascii=False)

def page(slug, lang, d):
    s = STR[lang]
    other = 'fr' if lang=='en' else 'en'
    url_en = f"{BASE}/{base_path(slug)}/"
    url_fr = f"{BASE}/fr/{base_path(slug)}/"
    url_self = url_en if lang=='en' else url_fr
    url_other = url_fr if lang=='en' else url_en
    navlinks = ''.join(f'<a class="nav-link" href="{h}">{t}</a>' for t,h in NAV_LINKS[lang])
    cards = ''.join(f'<div class="card"><h3>{t}</h3><p>{b}</p></div>' for t,b in d['s3'])
    prose1 = ''.join(f'<p>{p}</p>' for p in d['s1'])
    deliver = ''.join(f'<li>{p}</li>' for p in d['s2'])
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['title']}</title>
<meta name="description" content="{d['desc']}">
<link rel="canonical" href="{url_self}">
<link rel="alternate" hreflang="en" href="{url_en}">
<link rel="alternate" hreflang="fr" href="{url_fr}">
<link rel="alternate" hreflang="x-default" href="{url_en}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Xavier Advisory">
<meta property="og:title" content="{d['title']}">
<meta property="og:description" content="{d['desc']}">
<meta property="og:url" content="{url_self}">
<meta property="og:image" content="{BASE}/brand_assets/og-image.jpg">
<link rel="icon" type="image/svg+xml" href="/brand_assets/xa-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet">
<script type="application/ld+json">{jsonld(slug, lang, d)}</script>
<style>{CSS}</style>
</head>
<body>
<nav><div class="nav-inner">
  <a class="nav-logo" href="{s['home']}" aria-label="Xavier Advisory">{MARK}{WORD}</a>
  <div class="nav-right">{navlinks}<a class="nav-cta" href="{s['home']}#contact">{s['contact']}</a><a href="{url_other}" rel="alternate" hreflang="{other}">{s['lang_link_label']}</a></div>
</div></nav>
<header class="hero"><div class="wrap">
  <div class="breadcrumb"><a href="{d.get('backhref', s['home'] + '#expertise')}">{d.get('back', s['back'])}</a></div>
  <div class="label">{d['label']}</div>
  <h1>{d['h1']}</h1>
  <p>{d['intro']}</p>
</div></header>
<section><div class="wrap prose"><h2>{d['s1title']}</h2>{prose1}</div></section>
<section style="background:var(--white)"><div class="wrap"><h2>{d['s2title']}</h2><ul class="deliver">{deliver}</ul></div></section>
<section><div class="wrap"><h2>{d['s3title']}</h2><div class="cards">{cards}</div></div></section>
<section class="cta"><div class="wrap">
  <h2>{s['cta_h']}</h2>
  <p>{s['cta_p']}</p>
  <a class="btn-gold" href="https://calendly.com/xrobitaille/1h" target="_blank" rel="noopener">{s['cta_btn']}</a>
  <span class="alt">{s['cta_alt']}</span>
</div></section>
<footer><div class="wrap">
  <span>&copy; 2026 Xavier Advisory</span>
  <span><a href="{s['home']}">Xavier Advisory</a><a href="mailto:welcome@myxavier.finance">welcome@myxavier.finance</a></span>
</div></footer>
</body>
</html>
"""

count = 0
for slug, langs in PAGES.items():
    for lang, d in langs.items():
        path = (base_path(slug) if lang=='en' else f"fr/{base_path(slug)}")
        os.makedirs(path, exist_ok=True)
        with open(f"{path}/index.html", "w", encoding="utf-8") as f:
            f.write(page(slug, lang, d))
        count += 1
print(f"{count} pages générées")
