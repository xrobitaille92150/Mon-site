# -*- coding: utf-8 -*-
"""Pages d'apercu (« lire les premieres pages ») sur les sites de la maison.

Elles vivaient sur myxavier.finance et portaient le chrome Xavier Advisory.
Elles vivent desormais sous le domaine de leur marque, avec son logo, sa
palette et son formulaire : l'acheteur ne quitte plus la boutique.

Le corps du feuilletable vient de build_publications.flipbook_pages() :
les deux sites servent exactement le meme apercu.
"""
import json, os
import actuarius_legal as AL

# CSS propre a l'apercu, en complement de la feuille de la boutique.
PREVIEW_CSS = """
header.sub{background:var(--act-deep-navy);color:var(--act-ivory);
           padding:2.4rem 0 2rem;text-align:center}
header.sub .logo{width:120px;margin:0 auto 1.4rem}
header.sub .logo svg{width:100%;height:auto;display:block}
header.sub .crumb{font-size:.78rem;letter-spacing:.08em;margin-bottom:1rem}
header.sub .crumb a{color:#C7CCD6;text-decoration:none}
header.sub .crumb a:hover{color:var(--act-rich-gold)}
header.sub .label{font-size:.72rem;font-weight:700;letter-spacing:.16em;
                  text-transform:uppercase;color:var(--act-rich-gold);
                  margin-bottom:.7rem}
header.sub h1{font-family:var(--act-font-display);
              font-size:clamp(1.6rem,3.4vw,2.4rem);line-height:1.2;
              color:var(--act-ivory);max-width:820px;margin:0 auto}
header.sub p.desc{max-width:720px;margin:1rem auto 0;font-size:.92rem;
                  color:#C7CCD6;line-height:1.7}
.pv{padding:2.6rem 0 3.4rem}
.preview-note{text-align:center;font-size:.82rem;color:var(--gray);
              margin-bottom:1.4rem}
.preview-actions{margin-top:2rem;text-align:center}
.notify-form{display:flex;gap:.6rem;justify-content:center;flex-wrap:wrap}
.notify-mail{padding:.75rem 1rem;border:1.5px solid var(--act-light-grey);
             border-radius:3px;min-width:270px;font-family:inherit;
             font-size:.9rem}
.notify-mail:focus-visible{outline:2px solid var(--act-rich-gold);
                           outline-offset:1px}
"""


def head(b_, title, desc, url_self, ld, extra=''):
    return f"""<!DOCTYPE html>
<html lang="{b_['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url_self}">
<meta property="og:type" content="book">
<meta property="og:site_name" content="{b_['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url_self}">
<meta property="og:image" content="{b_['base']}/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="alternate icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&family=EB+Garamond:ital,wght@0,500;0,600;0,700;1,500&display=swap" rel="stylesheet">
<script type="application/ld+json">{ld}</script>
</head>"""


def footer(b_):
    return f"""<footer><div class="wrap">
  <span>&copy; 2026 {b_['name']}</span>
  <span>{AL.footer_links(b_)}<a href="mailto:welcome@myxavier.finance">{b_['contact']}</a></span>
</div></footer>
</body></html>"""


def preview_page(b_, slug, bk, ui, css, pages, flip_js, buy_html, esc):
    """Page « lire les premieres pages » d'un ouvrage, sous sa marque."""
    url_self = f"{b_['base']}/{slug}/"
    desc = bk['en_desc'] if b_['lang'] == 'en' else bk['fr_desc']
    title = f"{bk['name']} — {b_['name']}"
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Book",
        "name": bk['name'],
        "author": {"@type": "Person", "name": "Xavier Robitaille"},
        "inLanguage": b_['lang'],
        "datePublished": "2026-08",
        "publisher": {"@type": "Organization", "name": b_['name'],
                      "url": b_['base']},
        "url": url_self, "description": desc,
    }, ensure_ascii=False)

    note = f'<p class="preview-note">{ui["in_french"]}</p>' if ui['in_french'] else ''

    return f"""{head(b_, esc(title), esc(desc), url_self, ld)}
<body>
<header class="sub"><div class="wrap">
  <div class="logo"><a href="/">{b_['logo_svg']}</a></div>
  <p class="crumb"><a href="/">&larr; {b_['back_shop']}</a></p>
  <div class="label">{ui['preview_label']} &mdash; {ui['release']}</div>
  <h1>{esc(bk['name'])}</h1>
  <p class="desc">{esc(desc)}</p>
</div></header>
<section class="pv"><div class="wrap">
  {note}
  <div class="fb-stage">
    <div id="flipbook">{''.join(pages)}</div>
    <div class="fb-controls">
      <button class="fb-btn" id="fb-prev" aria-label="{ui['pg_prev']}">&larr;</button>
      <span class="fb-count" id="fb-count"></span>
      <button class="fb-btn" id="fb-next" aria-label="{ui['pg_next']}">&rarr;</button>
    </div>
    <p class="fb-hint">{ui['hint']}</p>
  </div>
  <div class="preview-actions">{buy_html}</div>
</div></section>
{flip_js}
{footer(b_)}"""


def notify_form(b_, bk, ui, esc):
    """Formulaire « etre prevenu », rattache au site Netlify de la marque."""
    return f"""<form class="notify-form" name="notify-parution" method="POST"
      action="/{b_['thanks_seg']}/" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="notify-parution">
  <input type="hidden" name="livre" value="{esc(bk['name'])}">
  <p style="display:none"><label>Ne pas remplir : <input name="bot-field"></label></p>
  <input class="notify-mail" type="email" name="email" required
         placeholder="{ui['mail_ph']}" aria-label="Email">
  <button class="btn-gold" type="submit">{ui['notify']}</button>
</form>
{AL.notify_notice(b_)}"""


def thanks_page(b_, ui, esc):
    """Page d'arrivee du formulaire, sur le domaine de la marque."""
    url_self = f"{b_['base']}/{b_['thanks_seg']}/"
    ld = json.dumps({"@context": "https://schema.org", "@type": "WebPage",
                     "name": ui['thanks_title'], "url": url_self},
                    ensure_ascii=False)
    return f"""{head(b_, esc(ui['thanks_title']) + ' — ' + b_['name'],
                     esc(ui['thanks_body']), url_self, ld)}
<body>
<header class="sub"><div class="wrap">
  <div class="logo"><a href="/">{b_['logo_svg']}</a></div>
  <h1>{esc(ui['thanks_title'])}</h1>
  <p class="desc">{esc(ui['thanks_body'])}</p>
  <p class="crumb" style="margin-top:1.6rem">
    <a href="/">&larr; {b_['back_shop']}</a></p>
</div></header>
{footer(b_)}"""
