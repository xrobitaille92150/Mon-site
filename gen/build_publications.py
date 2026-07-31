# -*- coding: utf-8 -*-
# Génère /publications/ + /fr/publications/ + une page d'aperçu par livre
# (page de titre + table des matières = les premières pages de l'ouvrage).
import os, sys, json, re, html
sys.path.insert(0, os.path.dirname(__file__))
from build_pages import CSS, MARK, WORD, STR, NAV_LINKS, BASE, navlinks_html
from publications_data import UI, BOOKS

TOC = json.load(open(os.path.join(os.path.dirname(__file__), 'books_toc.json'), encoding='utf-8'))

PUB_CSS = """
.pub-section{padding:3.6rem 0}
.pub-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:2rem;margin-top:1.6rem}
.bookcard{background:var(--white);box-shadow:0 8px 24px rgba(11,21,48,.07);border-top:3px solid var(--gold);padding:1.6rem;display:flex;flex-direction:column;gap:1rem;text-decoration:none;color:inherit;transition:transform .2s,box-shadow .2s}
.bookcard:hover{transform:translateY(-4px);box-shadow:0 16px 40px rgba(11,21,48,.13)}
.coverwrap{position:relative;display:flex;justify-content:center;background:var(--light-bg);padding:1.4rem 0}
.coverwrap svg{width:210px;height:auto;display:block;box-shadow:0 12px 28px rgba(11,21,48,.3)}
.release-badge{position:absolute;top:.8rem;right:.8rem;background:var(--gold);color:#fff;font-size:.62rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.35rem .7rem;border-radius:2px}
.bookcard h3{font-family:'EB Garamond',Georgia,serif;font-size:1.22rem;font-weight:700;color:var(--primary);line-height:1.25}
.bookcard p{font-size:.88rem;line-height:1.65;color:#4B5364}
.bookcard .view{margin-top:auto;color:var(--gold);font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.sheets{max-width:760px;margin:0 auto}
.sheet{background:#fff;box-shadow:0 10px 30px rgba(11,21,48,.12);padding:3.2rem 3.4rem;margin-bottom:1.6rem;position:relative}
.sheet .pageno{position:absolute;bottom:1rem;right:1.4rem;font-size:.72rem;color:var(--gray)}
.sheet-title{display:flex;flex-direction:column;align-items:center;text-align:center;min-height:560px;justify-content:space-between;padding-top:1.4rem}
.st-coll{font-size:.72rem;font-weight:700;letter-spacing:.28em;color:var(--gold);text-transform:uppercase;line-height:1.8}
.st-rule{width:110px;height:1px;background:var(--gold);margin:1.2rem auto}
.st-t1{font-family:'EB Garamond',Georgia,serif;font-size:2rem;font-weight:700;color:var(--primary);line-height:1.22}
.st-t2{font-family:'EB Garamond',Georgia,serif;font-size:1.25rem;font-style:italic;color:var(--primary);margin-top:.7rem}
.st-sub{font-size:.9rem;color:#4B5364;margin-top:1.4rem;line-height:1.6}
.st-ref{font-size:.76rem;color:var(--gold);letter-spacing:.04em;margin-top:1.6rem}
.st-author{font-size:.95rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--primary)}
.st-site{font-size:.74rem;color:var(--gray);margin-top:.5rem}
.sheet h2.toch{font-size:1.35rem;margin-bottom:1.4rem}
.toc-h{font-weight:700;color:var(--primary);margin:1.1rem 0 .4rem;font-size:.95rem}
.toc-part{font-size:.78rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin:1.3rem 0 .5rem}
.toc-ch{font-size:.9rem;line-height:1.5;color:#2A3345;padding:.22rem 0 .22rem 1.6rem;text-indent:-1.6rem}
.toc-ch b{color:var(--primary);font-weight:600}
.toc-ax{font-size:.88rem;line-height:1.5;color:#2A3345;padding:.2rem 0}
.preview-note{max-width:760px;margin:0 auto 2rem;font-size:.88rem;color:var(--gray);font-style:italic}
.preview-actions{max-width:760px;margin:0 auto;display:flex;gap:1rem;flex-wrap:wrap}
@media(max-width:640px){.sheet{padding:2rem 1.4rem}.sheet-title{min-height:480px}}
"""

def esc(s): return html.escape(s, quote=False)

def cover_svg(b):
    """Couverture fictive aux couleurs de la charte (inline SVG, polices du document)."""
    serif = "'EB Garamond',Georgia,serif"; sans = "'Inter',Arial,sans-serif"
    y = 62; parts = []
    parts.append('<svg viewBox="0 0 400 580" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">' % esc(b['name']))
    parts.append('<rect width="400" height="580" fill="#0B1530"/>')
    parts.append('<rect x="16" y="16" width="368" height="548" fill="none" stroke="#C79A3B" stroke-width="1.4"/>')
    parts.append('<rect x="22" y="22" width="356" height="536" fill="none" stroke="#C79A3B" stroke-width="0.4" opacity="0.5"/>')
    for line in b['collection']:
        parts.append('<text x="200" y="%d" text-anchor="middle" font-family="%s" font-size="11" letter-spacing="3.5" fill="#C79A3B">%s</text>' % (y, sans, esc(line))); y += 17
    parts.append('<line x1="145" y1="%d" x2="255" y2="%d" stroke="#C79A3B" stroke-width="1"/>' % (y+8, y+8))
    y += 62
    for line in b['t1']:
        parts.append('<text x="200" y="%d" text-anchor="middle" font-family="%s" font-size="27" font-weight="600" fill="#F5F2EB">%s</text>' % (y, serif, esc(line))); y += 36
    y += 6
    for line in b['t2']:
        parts.append('<text x="200" y="%d" text-anchor="middle" font-family="%s" font-size="16.5" font-style="italic" fill="#F5F2EB">%s</text>' % (y, serif, esc(line))); y += 24
    y += 22
    for line in b['sub']:
        parts.append('<text x="200" y="%d" text-anchor="middle" font-family="%s" font-size="11" fill="#C7CCD6">%s</text>' % (y, sans, esc(line))); y += 17
    ry = 462
    for line in b['ref']:
        parts.append('<text x="200" y="%d" text-anchor="middle" font-family="%s" font-size="9" fill="#C79A3B">%s</text>' % (ry, sans, esc(line))); ry += 14
    parts.append('<text x="200" y="516" text-anchor="middle" font-family="%s" font-size="12.5" letter-spacing="2.5" fill="#FFFFFF">XAVIER ROBITAILLE</text>' % sans)
    parts.append('<text x="200" y="542" text-anchor="middle" font-family="%s" font-size="9" fill="#C7CCD6">www.myxavier.fr</text>' % sans)
    parts.append('</svg>')
    return ''.join(parts)

def toc_entries(src, ui):
    """Aplati le sommaire extrait du docx : intro/parties/chapitres, puis annexes (Titre7 après le dernier chapitre)."""
    seq = TOC[src]['toc']
    last_ch = max((i for i, (s, _) in enumerate(seq) if s == 'Titre2'), default=-1)
    out = []
    started = annexes_started = False
    pending_part = prefix = pending_ax = None
    for i, (s, t) in enumerate(seq):
        t = t.strip()
        if s == 'Titre6':
            started = True
            out.append(('h', t.capitalize() if t.isupper() else t))
            if t.upper().startswith('ANNEXE'): annexes_started = True
        elif s == 'NumroPartie':
            if t.upper().startswith('PARTIE'): started = True; pending_part = t
        elif s == 'Titre1' and started and pending_part:
            out.append(('part', pending_part + ' — ' + t)); pending_part = None
        elif s == 'NumroChapitre':
            m_num = re.search(r'(\d+)', t)
            m_ax = re.fullmatch(r'ANNEXE\s+([A-Z])', t, re.I)
            if m_ax: pending_ax = 'Annexe ' + m_ax.group(1) + ' — '
            elif m_num: prefix = m_num.group(1) + '. '
            else: prefix = t.capitalize().replace('Synthese', 'Synthèse') + ' — '
        elif s == 'Titre2' and started:
            out.append(('ch', (prefix or '') + t)); prefix = None
        elif s == 'Titre7' and i > last_ch:
            if not annexes_started: out.append(('h', ui['annexes'])); annexes_started = True
            out.append(('ax', (pending_ax or '') + t)); pending_ax = None
    return out

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
<meta property="og:type" content="website">
<meta property="og:site_name" content="Xavier Advisory">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url_self}">
<meta property="og:image" content="{BASE}/brand_assets/og-image.jpg">
<link rel="icon" type="image/svg+xml" href="/brand_assets/xa-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=EB+Garamond:ital,wght@0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet">
<script type="application/ld+json">{ld}</script>
<style>{CSS}{PUB_CSS}</style>
</head>"""

def nav(lang, s, url_other, other_label):
    links = navlinks_html(lang, '/publications/' if lang == 'en' else '/fr/publications/')
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
<footer><div class="wrap"><span>&copy; 2026 Xavier Advisory</span><span><a href="{s['home']}">Xavier Advisory</a><a href="mailto:welcome@myxavier.finance">welcome@myxavier.finance</a></span></div></footer>
</body></html>"""

def book_url(slug, lang):
    return (f"{BASE}/publications/{slug}/" if lang == 'en' else f"{BASE}/fr/publications/{slug}/")

def index_page(lang):
    s, ui = STR[lang], UI[lang]
    url_en, url_fr = f"{BASE}/publications/", f"{BASE}/fr/publications/"
    url_self = url_en if lang == 'en' else url_fr
    url_other = url_fr if lang == 'en' else url_en
    ld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage",
                     "name": "Publications", "url": url_self,
                     "author": {"@type": "Person", "name": "Xavier Robitaille"}}, ensure_ascii=False)
    ex_links = ' &middot; '.join(
        f'<a href="{"/publications/" if lang=="en" else "/fr/publications/"}{slug}/">{esc(b["name"])}</a>'
        for slug, b in BOOKS.items())
    cards = ''
    for slug, b in BOOKS.items():
        href = (f"/publications/{slug}/" if lang == 'en' else f"/fr/publications/{slug}/")
        desc = b['en_desc'] if lang == 'en' else b['fr_desc']
        cards += f"""<a class="bookcard" href="{href}">
  <div class="coverwrap">{cover_svg(b)}<span class="release-badge">{ui['release']}</span></div>
  <h3>{esc(b['name'])}</h3>
  <p>{esc(desc)}</p>
  <span class="view">{ui['view']}</span>
</a>\n"""
    return f"""{head(ui['title'], ui['desc'], url_self, url_en, url_fr, lang, ld)}
<body>
{nav(lang, s, url_other, 'FR' if lang=='en' else 'EN')}
<header class="hero"><div class="wrap">
  <div class="label">{ui['label']}</div>
  <h1>{ui['h1']}</h1>
  <p>{ui['intro']}</p>
</div></header>
<section class="pub-section"><div class="wrap">
  <h2>{ui['free_title']}</h2>
  <div class="cards">
    <div class="card"><h3>{ui['free_wp_t']}</h3><p>{ui['free_wp_b']}</p><p style="margin-top:.7rem"><span class="release-badge" style="position:static">{ui['free_wp_badge']}</span></p></div>
    <div class="card"><h3>{ui['free_ex_t']}</h3><p>{ui['free_ex_b']}</p><p style="margin-top:.7rem;font-size:.85rem;line-height:1.7">{ex_links}</p></div>
    <div class="card"><h3>{ui['free_ins_t']}</h3><p>{ui['free_ins_b']}</p><p style="margin-top:.7rem;font-size:.85rem">{ui['free_ins_link']}</p></div>
  </div>
</div></section>
<section class="pub-section" style="background:var(--white)"><div class="wrap">
  <h2>{ui['shop_title']}</h2>
  <p style="max-width:680px;line-height:1.7;color:#2A3345;margin-top:.6rem">{ui['shop_sub']}</p>
  <div class="pub-grid">{cards}</div>
</div></section>
{cta_footer(s)}"""

def preview_page(slug, b, lang):
    s, ui = STR[lang], UI[lang]
    url_en, url_fr = book_url(slug, 'en'), book_url(slug, 'fr')
    url_self = url_en if lang == 'en' else url_fr
    url_other = url_fr if lang == 'en' else url_en
    desc = (b['en_desc'] if lang == 'en' else b['fr_desc'])
    title = esc(b['name']) + (" — Preview | Xavier Advisory" if lang == 'en' else " — Aperçu | Xavier Advisory")
    ld = json.dumps({"@context": "https://schema.org", "@type": "Book",
                     "name": b['name'], "author": {"@type": "Person", "name": "Xavier Robitaille"},
                     "inLanguage": "fr", "datePublished": "2026-08",
                     "publisher": {"@type": "Organization", "name": "Xavier Advisory"},
                     "url": url_self, "description": desc}, ensure_ascii=False)
    entries = toc_entries(b['src'], UI['fr'])
    n = len(entries); per = -(-n // 4)  # 4 pages de sommaire au plus
    chunks = [entries[i:i+per] for i in range(0, n, per)][:4]
    tp = ['<div class="sheet"><div class="sheet-title">',
          '<div><div class="st-coll">' + '<br>'.join(esc(x) for x in b['collection']) + '</div><div class="st-rule"></div></div>',
          '<div><div class="st-t1">' + '<br>'.join(esc(x) for x in b['t1']) + '</div>']
    if b['t2']: tp.append('<div class="st-t2">' + '<br>'.join(esc(x) for x in b['t2']) + '</div>')
    if b['sub']: tp.append('<div class="st-sub">' + '<br>'.join(esc(x) for x in b['sub']) + '</div>')
    tp.append('<div class="st-ref">' + '<br>'.join(esc(x) for x in b['ref']) + '</div></div>')
    tp.append('<div><div class="st-author">Xavier Robitaille</div><div class="st-site">www.myxavier.fr</div></div>')
    tp.append('</div><span class="pageno">1</span></div>')
    sheets = [''.join(tp)]
    for ci, chunk in enumerate(chunks):
        rows = []
        if ci == 0: rows.append(f'<h2 class="toch">{ui["toc_title"]}</h2>')
        for kind, txt in chunk:
            txt = esc(txt)
            if kind == 'h': rows.append(f'<div class="toc-h">{txt}</div>')
            elif kind == 'part': rows.append(f'<div class="toc-part">{txt}</div>')
            elif kind == 'ch':
                m = re.match(r'(\d+\.) (.*)', txt)
                rows.append(f'<div class="toc-ch"><b>{m.group(1)}</b> {m.group(2)}</div>' if m else f'<div class="toc-ch">{txt}</div>')
            else: rows.append(f'<div class="toc-ax">{txt}</div>')
        sheets.append(f'<div class="sheet">{"".join(rows)}<span class="pageno">{ci+2}</span></div>')
    lang_note = f'<p class="preview-note">{ui["in_french"]}</p>' if ui['in_french'] else ''
    return f"""{head(title, esc(desc), url_self, url_en, url_fr, lang, ld)}
<body>
{nav(lang, s, url_other, 'FR' if lang=='en' else 'EN')}
<header class="hero"><div class="wrap">
  <div class="breadcrumb"><a href="{ui['backhref']}">{ui['back']}</a></div>
  <div class="label">{ui['preview_label']} &mdash; {ui['release']}</div>
  <h1 style="font-size:clamp(1.7rem,3.4vw,2.5rem)">{esc(b['name'])}</h1>
  <p>{esc(desc)}</p>
</div></header>
<section class="pub-section"><div class="wrap">
  {lang_note}
  <div class="sheets">{''.join(sheets)}</div>
  <p class="preview-note">{ui['preview_note']}</p>
  <div class="preview-actions">
    <a class="btn-gold" href="{ui['notify_href']}">{ui['notify']}</a>
  </div>
</div></section>
{cta_footer(s)}"""

if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    count = 0
    for lang in ('en', 'fr'):
        base = 'publications' if lang == 'en' else 'fr/publications'
        os.makedirs(os.path.join(root, base), exist_ok=True)
        open(os.path.join(root, base, 'index.html'), 'w', encoding='utf-8').write(index_page(lang)); count += 1
        for slug, b in BOOKS.items():
            d = os.path.join(root, base, slug)
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(preview_page(slug, b, lang)); count += 1
    print(f"{count} pages publications générées")
