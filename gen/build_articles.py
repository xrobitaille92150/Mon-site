# -*- coding: utf-8 -*-
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from build_pages import (CSS, MARK, WORD, STR, NAV_LINKS, BASE,
                         navlinks_html, legal_links)

ART_CSS = """
.byline{display:flex;gap:1rem;align-items:center;font-size:.8rem;color:rgba(255,255,255,.65);margin-top:1.2rem}
.byline strong{color:rgba(255,255,255,.9)}
article{max-width:760px}
article h2{font-size:1.55rem;margin:2.6rem 0 1rem}
article h3{font-family:'Inter',Arial,sans-serif;font-size:1.02rem;font-weight:700;color:var(--primary);margin:1.8rem 0 .6rem}
article p{line-height:1.75;margin-bottom:1rem;color:#2A3345}
article ul{margin:0 0 1rem 1.2rem;line-height:1.7;color:#2A3345}
article li{margin-bottom:.4rem}
article blockquote{border-left:3px solid var(--gold);padding:.6rem 0 .6rem 1.2rem;margin:1.2rem 0;color:#4B5364;font-style:italic}
article table{width:100%;border-collapse:collapse;margin:1.4rem 0;font-size:.88rem}
article th{background:var(--primary);color:#fff;text-align:left;padding:.6rem .8rem;font-weight:600}
article td{padding:.55rem .8rem;border-bottom:1px solid var(--border);color:#2A3345;vertical-align:top}
article .refnote{font-size:.8rem;color:var(--gray);border-top:1px solid var(--border);padding-top:1rem;margin-top:2.4rem}
article a{color:var(--gold);text-decoration:none}
article a:hover{text-decoration:underline}
.related{background:var(--white);border-top:3px solid var(--gold);padding:1.2rem 1.4rem;margin:2.4rem 0;box-shadow:0 8px 24px rgba(11,21,48,.07)}
.related strong{display:block;margin-bottom:.4rem;color:var(--primary)}
.idx-card{display:block;background:var(--white);border-top:3px solid var(--gold);padding:1.5rem 1.6rem;margin-bottom:1.2rem;box-shadow:0 8px 24px rgba(11,21,48,.07);text-decoration:none;color:inherit;transition:transform .2s}
.idx-card:hover{transform:translateY(-2px)}
.idx-card h2{font-size:1.25rem;color:var(--primary);margin-bottom:.5rem}
.idx-card p{color:#4B5364;line-height:1.65;font-size:.92rem}
.idx-card .meta{font-size:.75rem;color:var(--gray);margin-top:.7rem;display:block}
"""

def head(title, desc, url_self, url_en, url_fr, lang, ld):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url_self}">
<link rel="alternate" hreflang="en" href="{url_en}">
<link rel="alternate" hreflang="fr" href="{url_fr}">
<link rel="alternate" hreflang="x-default" href="{url_en}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Xavier Advisory">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url_self}">
<meta property="og:image" content="{BASE}/brand_assets/og-image.jpg">
<link rel="icon" type="image/svg+xml" href="/brand_assets/xa-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=EB+Garamond:ital,wght@0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet">
<script type="application/ld+json">{ld}</script>
<style>{CSS}{ART_CSS}</style>
</head>"""

def nav(lang, s, url_other, other_label):
    links = navlinks_html(lang, '/insights/' if lang == 'en' else '/fr/insights/')
    return f"""<nav><div class="nav-inner">
  <a class="nav-logo" href="{s['home']}" aria-label="Xavier Advisory">{MARK}{WORD}</a>
  <div class="nav-right">{links}<a class="nav-cta" href="{s['home']}#contact">{s['contact']}</a><a href="{url_other}" rel="alternate">{other_label}</a></div>
</div></nav>"""

def cta_footer(s):
    return f"""<section class="cta"><div class="wrap">
  <h2>{s['cta_h']}</h2><p>{s['cta_p']}</p>
  <a class="btn-gold" href="https://calendly.com/xrobitaille/1h" target="_blank" rel="noopener">{s['cta_btn']}</a>
  <span class="alt">{s['cta_alt']}</span>
</div></section>
<footer><div class="wrap"><span>&copy; 2026 Xavier Advisory</span><span><a href="{s['home']}">Xavier Advisory</a><a href="mailto:welcome@myxavier.finance">welcome@myxavier.finance</a>{legal_links(s)}</span></div></footer>
</body></html>"""

def article_page(slug, lang, a):
    s = STR[lang]
    url_en = f"{BASE}/insights/{slug}/"
    url_fr = f"{BASE}/fr/insights/{slug}/"
    url_self = url_en if lang == 'en' else url_fr
    url_other = url_fr if lang == 'en' else url_en
    idx = '/insights/' if lang == 'en' else '/fr/insights/'
    back = '&larr; Insights' if lang == 'en' else '&larr; D&eacute;cryptages'
    ld = json.dumps({"@context": "https://schema.org", "@type": "Article",
        "headline": a['h1_plain'], "description": a['desc'],
        "datePublished": a['date_iso'], "inLanguage": lang,
        "author": {"@type": "Person", "name": "Xavier Robitaille"},
        "publisher": {"@type": "Organization", "name": "Xavier Advisory", "url": BASE + "/"},
        "mainEntityOfPage": url_self}, ensure_ascii=False)
    return f"""{head(a['title'], a['desc'], url_self, url_en, url_fr, lang, ld)}
<body>
{nav(lang, s, url_other, 'FR' if lang=='en' else 'EN')}
<header class="hero"><div class="wrap">
  <div class="breadcrumb"><a href="{idx}">{back}</a></div>
  <div class="label">{a['label']}</div>
  <h1 style="font-size:clamp(1.8rem,3.6vw,2.7rem)">{a['h1']}</h1>
  <p>{a['standfirst']}</p>
  <div class="byline"><strong>Xavier Robitaille</strong><span>{a['date_h']}</span><span>{a['readtime']}</span></div>
</div></header>
<section><div class="wrap"><article>
{a['body']}
<div class="related"><strong>{a['rel_t']}</strong>{a['rel_b']}</div>
<p class="refnote">{a['refnote']}</p>
</article></div></section>
{cta_footer(s)}"""

def index_page(lang, arts):
    s = STR[lang]
    url_en, url_fr = f"{BASE}/insights/", f"{BASE}/fr/insights/"
    url_self = url_en if lang == 'en' else url_fr
    url_other = url_fr if lang == 'en' else url_en
    t = 'Insights' if lang == 'en' else 'D&eacute;cryptages'
    title = ("Insights — Insurance Finance, Investment Accounting & Regulation | Xavier Advisory" if lang == 'en'
             else "Décryptages — Finance assurance, comptabilité des investissements | Xavier Advisory")
    desc = ("Technical articles on insurance finance: IFRS 9 and IFRS 17, investment accounting, Solvency II, platform implementations. By Xavier Robitaille." if lang == 'en'
            else "Articles techniques sur la finance assurance : IFRS 9 et IFRS 17, comptabilité des investissements, Solvabilité II, implémentations. Par Xavier Robitaille.")
    intro = ("Working notes from the field: regulation, investment accounting and systems, written from delivered engagements." if lang == 'en'
             else "Notes de terrain : réglementation, comptabilité des investissements et systèmes, écrites depuis des missions livrées.")
    cards = ''
    for slug, a in arts:
        href = (f"/insights/{slug}/" if lang == 'en' else f"/fr/insights/{slug}/")
        cards += f'<a class="idx-card" href="{href}"><h2>{a["h1"]}</h2><p>{a["desc"]}</p><span class="meta">Xavier Robitaille · {a["date_h"]} · {a["readtime"]}</span></a>\n'
    ld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": t, "url": url_self}, ensure_ascii=False)
    return f"""{head(title, desc, url_self, url_en, url_fr, lang, ld)}
<body>
{nav(lang, s, url_other, 'FR' if lang=='en' else 'EN')}
<header class="hero"><div class="wrap">
  <div class="label">Xavier Advisory</div>
  <h1>{t}</h1>
  <p>{intro}</p>
</div></header>
<section><div class="wrap" style="max-width:800px">
{cards}
</div></section>
{cta_footer(s)}"""

if __name__ == '__main__':
    from articles_data import ARTICLES
    order = sorted(ARTICLES.items(), key=lambda kv: kv[1]['en']['date_iso'], reverse=True)
    for slug, langs in ARTICLES.items():
        for lang, a in langs.items():
            path = f"insights/{slug}" if lang == 'en' else f"fr/insights/{slug}"
            os.makedirs(path, exist_ok=True)
            open(f"{path}/index.html", 'w', encoding='utf-8').write(article_page(slug, lang, a))
    for lang in ('en', 'fr'):
        path = 'insights' if lang == 'en' else 'fr/insights'
        os.makedirs(path, exist_ok=True)
        arts = [(slug, langs[lang]) for slug, langs in order]
        open(f"{path}/index.html", 'w', encoding='utf-8').write(index_page(lang, arts))
    print(f"OK: {len(ARTICLES)*2} articles + 2 index")
