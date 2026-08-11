# -*- coding: utf-8 -*-
# Génère /publications/ + /fr/publications/ + une page d'aperçu par livre :
# un livre animé (tourne-pages) contenant couverture, page de titre,
# table des matières complète et introduction.
import os, sys, json, re, html, math
sys.path.insert(0, os.path.dirname(__file__))
from build_pages import CSS, MARK, WORD, STR, NAV_LINKS, BASE, navlinks_html
from publications_data import UI, BOOKS, SHOP, IMPRINT_OF


def books_for(lang):
    """Le catalogue de chaque langue.

    Un ouvrage appartient a une seule marque d'edition, donc a une seule
    langue : le catalogue anglais n'est pas une traduction du francais.
    Presenter un traite de normes francaises a un lecteur anglophone n'a
    pas de sens, et inversement.
    """
    want = 'press' if lang == 'en' else 'editions'
    return [(s, b) for s, b in BOOKS.items()
            if IMPRINT_OF.get(s, 'editions') == want]

TOC = json.load(open(os.path.join(os.path.dirname(__file__), 'books_toc.json'), encoding='utf-8'))

FLIP_JS_CDN = "https://cdn.jsdelivr.net/npm/page-flip@2.0.7/dist/js/page-flip.browser.js"
LEMON_JS = '\n<script src="https://assets.lemonsqueezy.com/lemon.js" defer></script>'

# Monogramme Actuarius (compas + arc), variante inversée pour fonds marine.
ACT_MARK = open(os.path.join(os.path.dirname(__file__), '..', 'brand_assets', 'actuarius-mark.svg'), encoding='utf-8').read()
ACT_MARK_INV = ACT_MARK.replace('#0B1530', '#F5F2EB')

def shop_of(slug):
    sh = SHOP.get(slug) or {}
    return sh if any(sh.get(k) for k in ('ls', 'paper', 'kindle')) else None

def buy_buttons(slug, ui, compact=False):
    """Rangée de boutons d'achat. Vide si aucune URL renseignée dans SHOP."""
    sh = shop_of(slug)
    if not sh: return ''
    btns = []
    if sh.get('ls'):
        price = f' <span class="buy-price">{esc(sh["price"])}</span>' if sh.get('price') else ''
        btns.append(f'<a class="btn-gold lemonsqueezy-button" href="{sh["ls"]}">{ui["buy_pdf"]}{price}</a>')
    if sh.get('paper'):
        btns.append(f'<a class="btn-buy2" href="{sh["paper"]}" target="_blank" rel="noopener">{ui["buy_paper"]}</a>')
    if sh.get('kindle'):
        btns.append(f'<a class="btn-buy2" href="{sh["kindle"]}" target="_blank" rel="noopener">{ui["buy_kindle"]}</a>')
    note = '' if compact else f'<p class="buy-note">{ui["buy_note"]}</p>'
    return f'<div class="buy-row">{"".join(btns)}</div>{note}'

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
/* ── Livre animé ── */
.fb-stage{max-width:860px;margin:0 auto;padding:1rem 0}
#flipbook{margin:0 auto}
.fb-page{width:400px;height:580px;background:#FDFCF8;overflow:hidden;box-shadow:inset -6px 0 14px -8px rgba(11,21,48,.14)}
body:not(.flip-on) #flipbook{display:flex;flex-direction:column;align-items:center;gap:1.4rem}
body:not(.flip-on) .fb-page{box-shadow:0 10px 30px rgba(11,21,48,.14)}
.fb-inner{padding:30px 28px;height:100%;box-sizing:border-box;position:relative}
.fb-cover{background:#0B1530}
.fb-cover svg{width:100%;height:100%;display:block}
.fb-folio{position:absolute;bottom:11px;right:16px;font-size:9px;color:#9AA1AE}
.fb-h{font-family:'EB Garamond',Georgia,serif;font-size:1.2rem;font-weight:700;color:var(--primary);margin:0 0 .7rem}
.fb-toc-h{font-weight:700;color:var(--primary);margin:.55rem 0 .2rem;font-size:11.5px}
.fb-toc-part{font-size:9.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin:.65rem 0 .25rem}
.fb-toc-ch{font-size:10.5px;line-height:1.45;color:#2A3345;padding:.12rem 0 .12rem 1.1rem;text-indent:-1.1rem}
.fb-toc-ch b{color:var(--primary);font-weight:600}
.fb-toc-ax{font-size:10.5px;line-height:1.45;color:#2A3345;padding:.1rem 0}
.fb-p{font-size:12.5px;line-height:1.62;color:#2A3345;margin:0 0 .55rem;text-align:justify}
.fb-li{font-size:12.5px;line-height:1.55;color:#2A3345;margin:0 0 .15rem;padding-left:1rem;position:relative}
.fb-li::before{content:"—";position:absolute;left:0;color:var(--gold);font-size:10px}
.fb-q{font-size:12.5px;line-height:1.6;color:#4B5364;font-style:italic;border-left:2px solid var(--gold);padding-left:.8rem;margin:0 0 .7rem}
.fb-ih{font-family:'EB Garamond',Georgia,serif;font-size:14.5px;font-weight:700;color:var(--primary);margin:.7rem 0 .4rem}
.fb-title{display:flex;flex-direction:column;justify-content:space-between;align-items:center;text-align:center;height:100%}
.fb-title .st-coll{font-size:.6rem;font-weight:700;letter-spacing:.24em;color:var(--gold);text-transform:uppercase;line-height:1.8}
.fb-title .st-rule{width:90px;height:1px;background:var(--gold);margin:.9rem auto}
.fb-title .st-t1{font-family:'EB Garamond',Georgia,serif;font-size:1.55rem;font-weight:700;color:var(--primary);line-height:1.25}
.fb-title .st-t2{font-family:'EB Garamond',Georgia,serif;font-size:1.05rem;font-style:italic;color:var(--primary);margin-top:.55rem}
.fb-title .st-sub{font-size:.72rem;color:#4B5364;margin-top:1.1rem;line-height:1.6}
.fb-title .st-ref{font-size:.62rem;color:var(--gold);letter-spacing:.03em;margin-top:1.2rem}
.fb-title .st-author{font-size:.78rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--primary)}
.fb-title .st-site{font-size:.62rem;color:var(--gray);margin-top:.4rem}
.fb-end{background:#0B1530;color:#fff}
.fb-end .fb-inner{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:1.1rem}
.fb-end .e1{font-family:'EB Garamond',Georgia,serif;font-size:1.35rem;font-weight:700;line-height:1.3}
.fb-end .e2{font-size:.78rem;color:rgba(255,255,255,.65);line-height:1.7;max-width:270px}
.fb-end .e3{font-size:.68rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.fb-controls{display:flex;align-items:center;justify-content:center;gap:1.1rem;margin-top:1.4rem}
.fb-btn{background:var(--primary);color:#fff;border:none;width:40px;height:40px;border-radius:50%;cursor:pointer;font-size:1.05rem;line-height:1;transition:background .2s,transform .2s}
.fb-btn:hover{background:var(--gold);transform:translateY(-1px)}
.fb-count{font-size:.8rem;color:var(--gray);min-width:70px;text-align:center}
.fb-hint{text-align:center;font-size:.78rem;color:var(--gray);margin-top:.6rem;font-style:italic}
.preview-note{max-width:760px;margin:1.6rem auto 0;font-size:.88rem;color:var(--gray);font-style:italic;text-align:center}
.preview-actions{display:flex;gap:1rem;flex-wrap:wrap;justify-content:center;margin-top:1.4rem}
.notify-form{display:flex;gap:.6rem;flex-wrap:wrap;justify-content:center;align-items:stretch}
.notify-mail{padding:.8rem 1rem;border:1px solid rgba(11,21,48,.3);border-radius:3px;min-width:270px;font-family:'Inter',Arial,sans-serif;font-size:.9rem;color:var(--text);background:#fff}
.notify-mail:focus-visible{outline:2px solid var(--gold)}
@media(max-width:480px){.fb-btn{width:36px;height:36px}}
/* ── Boutique ── */
.buy-row{display:flex;gap:.8rem;flex-wrap:wrap;align-items:center;justify-content:center}
.buy-price{font-weight:800;margin-left:.45rem;letter-spacing:0}
.btn-buy2{display:inline-block;background:transparent;color:var(--primary);text-decoration:none;padding:.82rem 1.6rem;border:1.5px solid var(--primary);border-radius:3px;font-weight:700;font-size:.85rem;letter-spacing:.1em;text-transform:uppercase;transition:transform .2s,background .2s,color .2s}
.btn-buy2:hover{background:var(--primary);color:#fff;transform:translateY(-2px)}
.btn-buy2:focus-visible,.buy-row .btn-gold:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.buy-note{text-align:center;font-size:.78rem;color:var(--gray);margin-top:.8rem}
.bookcard .buy-row{justify-content:flex-start;margin-top:.2rem;gap:.6rem}
.bookcard .btn-gold{padding:.65rem 1.2rem;font-size:.72rem}
.bookcard .btn-buy2{padding:.6rem 1.1rem;font-size:.72rem}
.bookcard-link{display:flex;flex-direction:column;gap:1rem;text-decoration:none;color:inherit;flex:1}
"""

def esc(s): return html.escape(s, quote=False)

IMPRINT_LABEL = {'editions': '&#201;DITIONS ACTUARIUS', 'press': 'ACTUARIUS PRESS'}


def cover_svg(b, slug=None):
    """Couverture fictive aux couleurs de la charte (inline SVG, polices du document).

    La signature de bas de couverture porte la marque d'edition de l'ouvrage :
    un livre anglais ne porte jamais « EDITIONS », et inversement.
    """
    serif = "'EB Garamond',Georgia,serif"; sans = "'Inter',Arial,sans-serif"
    y = 62; parts = []
    parts.append('<svg viewBox="0 0 400 580" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s" preserveAspectRatio="xMidYMid meet">' % esc(b['name']))
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
    imprint = IMPRINT_LABEL[IMPRINT_OF.get(slug, 'editions')]
    parts.append('<text x="200" y="542" text-anchor="middle" font-family="%s" font-size="9" letter-spacing="2.2" fill="#C79A3B">%s</text>' % (sans, imprint))
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
            if re.match(r'ANNEXE?S?\b|APPENDI(X|CES)\b', t, re.I): annexes_started = True
        elif s == 'NumroPartie':
            # « PARTIE » (FR) ou « PART » (EN) — les deux marques coexistent.
            if re.match(r'PART(IE)?\b', t, re.I): started = True; pending_part = t
        elif s == 'Titre1' and started and pending_part:
            out.append(('part', pending_part + ' — ' + t)); pending_part = None
        elif s == 'NumroChapitre':
            m_num = re.search(r'(\d+)', t)
            m_ax = re.fullmatch(r'(?:ANNEXE|APPENDIX)\s+([A-Z])', t, re.I)
            if m_ax: pending_ax = ('Appendix ' if t.upper().startswith('APPENDIX')
                                   else 'Annexe ') + m_ax.group(1) + ' — '
            elif m_num: prefix = m_num.group(1) + '. '
            else: prefix = t.capitalize().replace('Synthese', 'Synthèse') + ' — '
        elif s == 'Titre2' and started:
            out.append(('ch', (prefix or '') + t)); prefix = None
        elif s == 'Titre7' and i > last_ch:
            if not annexes_started: out.append(('h', ui['annexes'])); annexes_started = True
            out.append(('ax', (pending_ax or '') + t)); pending_ax = None
    return out

# ── Pagination : découpe le contenu en pages de hauteur fixe (estimation en pixels) ──
PAGE_BUDGET = 495

def _lines(t, cpl): return max(1, math.ceil(len(t) / cpl))

def _toc_height(kind, t):
    if kind == 'h': return 28
    if kind == 'part': return 32
    return _lines(t, 58) * 15 + 4

def _intro_height(kind, t):
    if kind == 'h': return 34
    if kind == 'q': return _lines(t, 50) * 20 + 12
    if t.rstrip().endswith((';', ':')) and len(t) < 120: return _lines(t, 52) * 19 + 3
    return _lines(t, 52) * 20 + 9

def paginate(blocks, height_fn, header_h):
    pages, cur, used = [], [], header_h
    for b in blocks:
        h = height_fn(b[0], b[1])
        if cur and used + h > PAGE_BUDGET:
            pages.append(cur); cur, used = [], 0
        cur.append(b); used += h
    if cur: pages.append(cur)
    return pages

def head(title, desc, url_self, url_en, url_fr, lang, ld, extra_head=''):
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
<style>{CSS}{PUB_CSS}</style>{extra_head}
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
        for slug, b in books_for(lang))
    cards = ''
    for slug, b in books_for(lang):
        href = (f"/publications/{slug}/" if lang == 'en' else f"/fr/publications/{slug}/")
        desc = b['en_desc'] if lang == 'en' else b['fr_desc']
        buy = buy_buttons(slug, ui, compact=True)
        cards += f"""<div class="bookcard">
  <a class="bookcard-link" href="{href}">
    <div class="coverwrap">{cover_svg(b, slug)}<span class="release-badge">{ui['release']}</span></div>
    <h3>{esc(b['name'])}</h3>
    <p>{esc(desc)}</p>
    <span class="view">{ui['view']}</span>
  </a>
  {buy}
</div>\n"""
    lemon = LEMON_JS if any(shop_of(sl) and SHOP[sl].get('ls')
                            for sl, _ in books_for(lang)) else ''
    return f"""{head(ui['title'], ui['desc'], url_self, url_en, url_fr, lang, ld, extra_head=lemon)}
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

def _render_toc_rows(chunk):
    rows = []
    for kind, txt in chunk:
        txt = esc(txt)
        if kind == 'h': rows.append(f'<div class="fb-toc-h">{txt}</div>')
        elif kind == 'part': rows.append(f'<div class="fb-toc-part">{txt}</div>')
        elif kind == 'ch':
            m = re.match(r'(\d+\.) (.*)', txt)
            rows.append(f'<div class="fb-toc-ch"><b>{m.group(1)}</b> {m.group(2)}</div>' if m else f'<div class="fb-toc-ch">{txt}</div>')
        else: rows.append(f'<div class="fb-toc-ax">{txt}</div>')
    return ''.join(rows)

def _render_intro_rows(chunk):
    rows = []
    for kind, txt in chunk:
        t = esc(txt)
        if kind == 'h': rows.append(f'<div class="fb-ih">{t}</div>')
        elif kind == 'q': rows.append(f'<div class="fb-q">{t}</div>')
        elif txt.rstrip().endswith(';') and len(txt) < 120:
            rows.append(f'<div class="fb-li">{t}</div>')
        else: rows.append(f'<p class="fb-p">{t}</p>')
    return ''.join(rows)

def preview_page(slug, b, lang):
    s, ui = STR[lang], UI[lang]
    url_en, url_fr = book_url(slug, 'en'), book_url(slug, 'fr')
    url_self = url_en if lang == 'en' else url_fr
    url_other = url_fr if lang == 'en' else url_en
    desc = (b['en_desc'] if lang == 'en' else b['fr_desc'])
    title = esc(b['name']) + (" — Preview | Xavier Advisory" if lang == 'en' else " — Aperçu | Xavier Advisory")
    ld_obj = {"@context": "https://schema.org", "@type": "Book",
              "name": b['name'], "author": {"@type": "Person", "name": "Xavier Robitaille"},
              "inLanguage": "fr", "datePublished": "2026-08",
              "publisher": {"@type": "Organization", "name": "Xavier Advisory"},
              "url": url_self, "description": desc}
    sh = shop_of(slug)
    if sh and sh.get('ls'):
        m = re.match(r'([\d.,]+)', sh.get('price', ''))
        offer = {"@type": "Offer", "url": sh['ls'], "availability": "https://schema.org/InStock",
                 "priceCurrency": "EUR"}
        if m: offer["price"] = m.group(1).replace(',', '.')
        ld_obj["bookFormat"] = "https://schema.org/EBook"
        ld_obj["offers"] = offer
    ld = json.dumps(ld_obj, ensure_ascii=False)

    pages = []
    folio = [0]

    # 1. Couverture
    pages.append(f'<div class="fb-page fb-cover" data-density="hard">{cover_svg(b, slug)}</div>'); folio[0] += 1
    # 2. Page de titre
    tp = ['<div class="fb-inner"><div class="fb-title">',
          '<div><div class="st-coll">' + '<br>'.join(esc(x) for x in b['collection']) + '</div><div class="st-rule"></div></div>',
          '<div><div class="st-t1">' + '<br>'.join(esc(x) for x in b['t1']) + '</div>']
    if b['t2']: tp.append('<div class="st-t2">' + '<br>'.join(esc(x) for x in b['t2']) + '</div>')
    if b['sub']: tp.append('<div class="st-sub">' + '<br>'.join(esc(x) for x in b['sub']) + '</div>')
    tp.append('<div class="st-ref">' + '<br>'.join(esc(x) for x in b['ref']) + '</div></div>')
    imprint_name = ('Actuarius Press' if IMPRINT_OF.get(slug) == 'press'
                    else 'Éditions Actuarius')
    tp.append('<div><div class="st-author">Xavier Robitaille</div><div class="st-site">' + imprint_name + '</div></div>')
    tp.append('</div></div>')
    folio[0] += 1
    pages.append(f'<div class="fb-page">{"".join(tp)}<span class="fb-folio">{folio[0]}</span></div>')
    # 3+. Table des matières
    # La TdM suit la langue de l'ouvrage, pas celle de la page qui l'affiche :
    # l'intitule « Annexes / Appendices » doit rester celui du livre.
    book_ui = UI['en'] if IMPRINT_OF.get(slug) == 'press' else UI['fr']
    entries = toc_entries(b['src'], book_ui)
    for i, chunk in enumerate(paginate(entries, _toc_height, 40)):
        h = f'<div class="fb-h">{ui["toc_title"]}</div>' if i == 0 else ''
        folio[0] += 1
        pages.append(f'<div class="fb-page"><div class="fb-inner">{h}{_render_toc_rows(chunk)}</div><span class="fb-folio">{folio[0]}</span></div>')
    # Introduction
    intro = TOC[b['src']].get('intro') or []
    for i, chunk in enumerate(paginate(intro, _intro_height, 44)):
        h = f'<div class="fb-h">Introduction</div>' if i == 0 else ''
        folio[0] += 1
        pages.append(f'<div class="fb-page"><div class="fb-inner">{h}{_render_intro_rows(chunk)}</div><span class="fb-folio">{folio[0]}</span></div>')
    # Dernière page
    on_sale = shop_of(slug) is not None
    end_note = ui['preview_note_sale'] if on_sale else ui['preview_note']
    pages.append(f'''<div class="fb-page fb-end" data-density="hard"><div class="fb-inner">
      <div class="e3">{ui['release']}</div>
      <div class="e1">{esc(b['name'])}</div>
      <div class="e2">{end_note}</div>
      <div style="width:96px">{ACT_MARK_INV}</div>
    </div></div>''')

    lang_note = f'<p class="preview-note">{ui["in_french"]}</p>' if ui['in_french'] else ''
    flip_js = f"""
<script src="{FLIP_JS_CDN}"></script>
<script>
(function() {{
  var el = document.getElementById('flipbook');
  if (!el || typeof St === 'undefined') return;
  try {{
    var pf = new St.PageFlip(el, {{
      width: 400, height: 580, size: 'stretch',
      minWidth: 280, maxWidth: 460, minHeight: 406, maxHeight: 667,
      showCover: true, maxShadowOpacity: 0.4, mobileScrollSupport: false, flippingTime: 800
    }});
    pf.loadFromHTML(document.querySelectorAll('.fb-page'));
    document.body.classList.add('flip-on');
    var total = pf.getPageCount();
    var count = document.getElementById('fb-count');
    function upd() {{ count.textContent = (pf.getCurrentPageIndex() + 1) + ' / ' + total; }}
    upd();
    pf.on('flip', function() {{ setTimeout(upd, 50); }});
    document.getElementById('fb-prev').addEventListener('click', function() {{ pf.flipPrev(); }});
    document.getElementById('fb-next').addEventListener('click', function() {{ pf.flipNext(); }});
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'ArrowLeft') pf.flipPrev();
      if (e.key === 'ArrowRight') pf.flipNext();
    }});
  }} catch (e) {{ /* les pages restent affichées empilées */ }}
}})();
</script>"""
    lemon = LEMON_JS if (sh and sh.get('ls')) else ''
    return f"""{head(title, esc(desc), url_self, url_en, url_fr, lang, ld, extra_head=lemon)}
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
  <div class="fb-stage">
    <div id="flipbook">{''.join(pages)}</div>
    <div class="fb-controls">
      <button class="fb-btn" id="fb-prev" aria-label="{ui['pg_prev']}">&larr;</button>
      <span class="fb-count" id="fb-count"></span>
      <button class="fb-btn" id="fb-next" aria-label="{ui['pg_next']}">&rarr;</button>
    </div>
    <p class="fb-hint">{ui['hint']}</p>
  </div>
  <div class="preview-actions">
    {buy_buttons(slug, ui) if on_sale else f'''<form class="notify-form" name="notify-parution" method="POST" action="{'/publications/thank-you/' if lang == 'en' else '/fr/publications/merci/'}" data-netlify="true" netlify-honeypot="bot-field">
      <input type="hidden" name="form-name" value="notify-parution">
      <input type="hidden" name="livre" value="{esc(b['name'])}">
      <p style="display:none"><label>Ne pas remplir : <input name="bot-field"></label></p>
      <input class="notify-mail" type="email" name="email" required placeholder="{ui['mail_ph']}" aria-label="Email">
      <button class="btn-gold" type="submit">{ui['notify']}</button>
    </form>'''}
  </div>
</div></section>
{flip_js}
{cta_footer(s)}"""

def thanks_page(lang):
    s, ui = STR[lang], UI[lang]
    seg = 'thank-you' if lang == 'en' else 'merci'
    url_en, url_fr = f"{BASE}/publications/thank-you/", f"{BASE}/fr/publications/merci/"
    url_self = url_en if lang == 'en' else url_fr
    url_other = url_fr if lang == 'en' else url_en
    title = f"{ui['thanks_title']} | Xavier Advisory"
    h = head(title, ui['thanks_body'], url_self, url_en, url_fr, lang, '{}',
             extra_head='\n<meta name="robots" content="noindex">')
    return f"""{h}
<body>
{nav(lang, s, url_other, 'FR' if lang=='en' else 'EN')}
<header class="hero"><div class="wrap">
  <div class="label">Publications</div>
  <h1>{ui['thanks_title']}</h1>
  <p>{ui['thanks_body']}</p>
  <p style="margin-top:1.2rem"><span style="color:rgba(245,242,235,.85)">{ui['thanks_back']}</span></p>
</div></header>
{cta_footer(s)}"""

if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    count = 0
    for lang in ('en', 'fr'):
        base = 'publications' if lang == 'en' else 'fr/publications'
        os.makedirs(os.path.join(root, base), exist_ok=True)
        open(os.path.join(root, base, 'index.html'), 'w', encoding='utf-8').write(index_page(lang)); count += 1
        for slug, b in books_for(lang):
            d = os.path.join(root, base, slug)
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(preview_page(slug, b, lang)); count += 1
        seg = 'thank-you' if lang == 'en' else 'merci'
        d = os.path.join(root, base, seg)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(thanks_page(lang)); count += 1
    print(f"{count} pages publications générées")
