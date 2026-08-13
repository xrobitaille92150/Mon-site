# -*- coding: utf-8 -*-
"""Genere les deux sites de la maison d'edition, une marque par domaine.

  actuarius/        -> Editions Actuarius (FR) -> editionsactuarius.com
  actuarius-press/  -> Actuarius Press    (EN) -> actuariuspress.com

Deploiement : deux sites Netlify sur le meme repo, publish directory =
"actuarius" et "actuarius-press".

Conformite charte (brand kit v1.3, 00_Knowledge/Inputs/11 - Editions
Actuarius Brand Kit) :
  - ACTUARIUS est toujours en PREMIERE ligne du logo, le descripteur
    (EDITIONS / PRESS) en seconde.
  - Le 2e A et le I d'ACTUARIUS sont en Rich Gold.
  - Les logos ne sont pas reconstruits en CSS : les SVG du kit sont
    copies dans brand_assets/actuarius/ et inlines tels quels.

Les liens d'achat viennent du dict SHOP de publications_data.py.
"""
import os, sys, json, html

sys.path.insert(0, os.path.dirname(__file__))
from publications_data import UI, BOOKS, SHOP, IMPRINT_OF
from build_publications import (cover_svg, buy_buttons, shop_of, LEMON_JS,
                                flipbook_pages, PUB_CSS, FLIP_JS, esc as _esc)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, 'brand_assets', 'actuarius')
MAIN = "https://www.myxavier.finance"


def asset(name):
    """Lit un asset du brand kit importe dans le repo."""
    with open(os.path.join(ASSETS, name), encoding='utf-8') as f:
        return f.read()


# --- Les deux marques ---------------------------------------------------
# Une marque = un domaine = une langue = un repertoire de publication.
BRANDS = {
 'editions': dict(
    key='editions', lang='fr', outdir='actuarius',
    name="Éditions Actuarius",
    base="https://www.editionsactuarius.com",
    logo='editions-stacked-inverse.svg',
    og='og-editions.png',
    sister_url="https://www.actuariuspress.com",
    sister_label="Books in English — Actuarius Press",
    empty_t="Les premiers titres sont en préparation",
    empty_b='Le catalogue s\'ouvrira ici. En attendant, nos ouvrages en anglais '
            'paraissent chez <a href="https://www.actuariuspress.com">Actuarius Press</a>.',
    title="Éditions Actuarius — Traités techniques finance & assurance",
    desc="Éditions Actuarius publie des traités techniques de référence en "
         "finance et assurance : comptabilité des placements, prudentiel, "
         "contrôles. PDF, papier et Kindle.",
    tagline="Parutions spécialisées dans les domaines de la Finance "
            "et de l'Assurance",
    intro="L'<em>actuarius</em> tenait les registres et les comptes de Rome. "
          "Éditions Actuarius publie des ouvrages basés sur l'expérience "
          "pratique de leurs auteurs : gestion et comptabilité des placements, "
          "comptabilité technique d'assurance, reportings prudentiels, contrôle "
          "interne, projets d'implémentation… Ils incluent des schémas "
          "comptables et des exemples chiffrés, des lexiques des termes "
          "techniques et des acronymes spécifiques au secteur, ainsi que des "
          "listes de contrôles directement applicables.",
    extract="Lire les premières pages",
    upcoming="Bientôt disponible ici",
    author_t="Nos auteurs",
    author_b="<strong>Xavier Robitaille</strong> conseille assureurs et "
             "institutions financières sur leurs sujets finance, comptabilité, "
             "investissements et réglementaire. Profil complet sur "
             '<a href="%s/fr/">myxavier.finance</a>.' % MAIN,
    legal="Éditions Actuarius est la marque d'édition de Xavier Advisory.",
    contact="Contact",
    back_shop="Tous les ouvrages",
    thanks_seg="merci",
 ),
 'press': dict(
    key='press', lang='en', outdir='actuarius-press',
    name="Actuarius Press",
    base="https://www.actuariuspress.com",
    logo='press-stacked-inverse.svg',
    og='og-press.png',
    sister_url="https://www.editionsactuarius.com",
    sister_label="Livres en français — Éditions Actuarius",
    empty_t="First titles in preparation",
    empty_b='Actuarius Press is building an English-language list written from '
            'practice. It is not a translation of the French catalogue: French '
            'GAAP has little to say to an international readership, so these '
            'books are written for it from the start. Our French titles are '
            'published by <a href="https://www.editionsactuarius.com">Éditions '
            'Actuarius</a>.',
    title="Actuarius Press — Technical books on finance & insurance",
    desc="Actuarius Press publishes reference technical books on finance and "
         "insurance: investment accounting, prudential rules, controls. "
         "PDF, paperback and Kindle.",
    tagline="Specialist publications in Finance and Insurance",
    intro="The <em>actuarius</em> kept Rome's registers and accounts. "
          "Actuarius Press publishes books grounded in their authors' working "
          "experience: investment management and accounting, insurance "
          "technical accounting, prudential reporting, internal control, "
          "implementation programmes… They include accounting schemes and "
          "worked figures, glossaries of technical terms and sector acronyms, "
          "and control checklists ready to apply.",
    extract="Read the first pages",
    upcoming="Coming soon to this shop",
    author_t="Our authors",
    author_b="<strong>Xavier Robitaille</strong> advises insurers and financial "
             "institutions on finance, accounting, investment and regulatory "
             'topics. Full profile at <a href="%s/">myxavier.finance</a>.' % MAIN,
    legal="Actuarius Press is the publishing imprint of Xavier Advisory.",
    contact="Contact",
    back_shop="All books",
    thanks_seg="thank-you",
 ),
}

# --- Feuille de style : tokens du kit, pas de valeurs en dur -------------
CSS = """
:root{
  --act-deep-navy:#0B1530;--act-rich-gold:#C79A3B;--act-ivory:#F5F2EB;
  --act-white:#FFFFFF;--act-light-grey:#E6E8EC;
  --act-font-display:'EB Garamond',Georgia,serif;
  --act-font-interface:Inter,Arial,sans-serif;
  --act-radius-sm:6px;--act-radius-md:12px;
  --act-space-3:16px;--act-space-4:24px;--act-space-5:32px;--act-space-6:48px;
  --text:#2A3345;--gray:#6B7280;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:var(--act-font-interface);color:var(--text);
     background:var(--act-ivory);line-height:1.6}
.wrap{max-width:1080px;margin:0 auto;padding:0 1.4rem}
a{color:var(--act-rich-gold)}
/* Empreinte mesuree : marges larges, grille stable, hierarchie nette. */
header.hero{background:var(--act-deep-navy);color:var(--act-ivory);
            padding:4.4rem 0 3.6rem;text-align:center;position:relative}
.hero .logo{width:230px;margin:0 auto}
.hero .logo svg{width:100%;height:auto;display:block}
/* Baseline : 24px plancher, jamais moins. */
.hero .tagline{margin:1.6rem auto 0;max-width:760px;
               font-family:var(--act-font-display);
               font-size:clamp(1.5rem,2.6vw,1.85rem);line-height:1.35;
               color:var(--act-ivory);letter-spacing:.01em}
.hero .sister{position:absolute;top:1.2rem;right:1.6rem}
.hero .sister a{color:#C7CCD6;text-decoration:none;font-size:.78rem;
                letter-spacing:.08em}
.hero .sister a:hover{color:var(--act-rich-gold)}
.intro{max-width:720px;margin:2.6rem auto 0;font-size:1rem;line-height:1.8}
/* EB Garamond a une hauteur d'x plus basse qu'Inter : a taille nominale
   egale il parait plus petit. Le 1.14em compense optiquement. */
.intro em{font-family:var(--act-font-display);font-size:1.14em;
          color:var(--act-rich-gold);font-style:italic}
.shop{padding:var(--act-space-6) 0 4rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
      gap:2rem}
.bk{background:var(--act-white);border-top:3px solid var(--act-rich-gold);
    box-shadow:0 8px 24px rgba(11,21,48,.07);padding:1.6rem;display:flex;
    flex-direction:column;gap:1rem}
.bk .cw{display:flex;justify-content:center;background:var(--act-ivory);
        padding:1.4rem 0}
.bk .cw svg{width:210px;height:auto;box-shadow:0 12px 28px rgba(11,21,48,.3)}
.bk h3{font-family:var(--act-font-display);font-size:1.22rem;
       color:var(--act-deep-navy);line-height:1.25}
.bk p{font-size:.88rem;line-height:1.65;color:#4B5364}
.bk .extract{font-size:.78rem;font-weight:700;letter-spacing:.08em;
             text-transform:uppercase;text-decoration:none;margin-top:auto}
.btn-gold{display:inline-block;background:var(--act-rich-gold);color:#fff;
          text-decoration:none;padding:.75rem 1.4rem;border-radius:3px;
          font-weight:700;font-size:.78rem;letter-spacing:.1em;
          text-transform:uppercase;transition:transform .2s}
.btn-gold:hover{transform:translateY(-2px)}
.btn-buy2{display:inline-block;background:transparent;
          color:var(--act-deep-navy);text-decoration:none;padding:.68rem 1.2rem;
          border:1.5px solid var(--act-deep-navy);border-radius:3px;
          font-weight:700;font-size:.78rem;letter-spacing:.1em;
          text-transform:uppercase;
          transition:transform .2s,background .2s,color .2s}
.btn-buy2:hover{background:var(--act-deep-navy);color:#fff;
                transform:translateY(-2px)}
.btn-gold:focus-visible,.btn-buy2:focus-visible{
  outline:2px solid var(--act-rich-gold);outline-offset:2px}
.buy-row{display:flex;gap:.6rem;flex-wrap:wrap}
.buy-price{font-weight:800;margin-left:.4rem}
.buy-note{font-size:.74rem;color:var(--gray);margin-top:.5rem}
.upcoming{font-size:.72rem;font-weight:700;letter-spacing:.1em;
          text-transform:uppercase;color:var(--act-rich-gold)}
.author{background:var(--act-white);padding:3rem 0}
.author h2{font-family:var(--act-font-display);color:var(--act-deep-navy);
           margin-bottom:.8rem}
.author p{max-width:680px}
footer{background:var(--act-deep-navy);color:#C7CCD6;padding:2rem 0;
       font-size:.8rem}
footer .wrap{display:flex;justify-content:space-between;gap:1rem;
             flex-wrap:wrap;align-items:center}
footer a{color:#C7CCD6}
footer a:hover{color:var(--act-rich-gold)}
@media(max-width:640px){.hero .logo{width:180px}
  .hero .sister{position:static;display:block;margin-bottom:1.4rem}}
"""


def esc(s):
    return html.escape(s, quote=False)


def page(brand):
    b_ = BRANDS[brand]
    lang = b_['lang']
    ui = UI[lang]
    url_self = b_['base'] + '/'
    ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": b_['name'],
        "url": b_['base'],
        "logo": b_['base'] + '/logo.svg',
        "parentOrganization": {"@type": "Organization",
                               "name": "Xavier Advisory", "url": MAIN},
        "founder": {"@type": "Person", "name": "Xavier Robitaille"},
    }, ensure_ascii=False)

    # Un ouvrage ne parait que sur le site de sa marque.
    catalogue = [(s, b) for s, b in BOOKS.items()
                 if IMPRINT_OF.get(s) == brand]

    cards = ''
    for slug, bk in catalogue:
        desc = bk['en_desc'] if lang == 'en' else bk['fr_desc']
        preview = f"/{slug}/"      # l'apercu vit desormais sur le site de la marque
        buy = buy_buttons(slug, ui) or \
            f'<span class="upcoming">{b_["upcoming"]}</span>'
        cards += f"""<div class="bk">
  <div class="cw">{cover_svg(bk, slug)}</div>
  <h3>{esc(bk['name'])}</h3>
  <p>{esc(desc)}</p>
  <a class="extract" href="{preview}">{b_['extract']} &rarr;</a>
  {buy}
</div>\n"""

    lemon = LEMON_JS if any(shop_of(s) and SHOP[s].get('ls') for s in BOOKS) else ''

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{b_['title']}</title>
<meta name="description" content="{b_['desc']}">
<link rel="canonical" href="{url_self}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{b_['name']}">
<meta property="og:title" content="{b_['title']}">
<meta property="og:description" content="{b_['desc']}">
<meta property="og:url" content="{url_self}">
<meta property="og:image" content="{b_['base']}/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="alternate icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&family=EB+Garamond:ital,wght@0,500;0,600;0,700;1,500&display=swap" rel="stylesheet">
<script type="application/ld+json">{ld}</script>
<style>{CSS}</style>{lemon}
</head>
<body>
<header class="hero"><div class="wrap">
  <p class="sister"><a href="{b_['sister_url']}">{b_['sister_label']} &rarr;</a></p>
  <div class="logo">{asset(b_['logo'])}</div>
  <p class="tagline">{b_['tagline']}</p>
  <p class="intro">{b_['intro']}</p>
</div></header>
<section class="shop"><div class="wrap">
  <div class="grid">{cards}</div>
</div></section>
<section class="author"><div class="wrap">
  <h2>{b_['author_t']}</h2>
  <p>{b_['author_b']}</p>
</div></section>
<footer><div class="wrap">
  <span>&copy; 2026 {b_['name']}</span>
  <span><a href="mailto:welcome@myxavier.finance">{b_['contact']}</a></span>
</div></footer>
</body></html>"""


def write_previews(brand, out):
    """Une page d'apercu par ouvrage de la marque, plus sa page de merci."""
    import actuarius_preview as AP
    b_ = dict(BRANDS[brand])
    b_['logo_svg'] = asset(b_['logo'])
    ui = UI[b_['lang']]
    css = f"<style>{CSS}{PUB_CSS}{AP.PREVIEW_CSS}</style>"
    n = 0
    for slug, bk in BOOKS.items():
        if IMPRINT_OF.get(slug) != brand:
            continue
        pages = flipbook_pages(slug, bk, ui)
        buy = buy_buttons(slug, ui) or AP.notify_form(b_, bk, ui, _esc)
        html_ = AP.preview_page(b_, slug, bk, ui, css, pages, FLIP_JS, buy, _esc)
        html_ = html_.replace('</head>', css + '\n</head>')
        d = os.path.join(out, slug)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html_)
        n += 1
    # Page de remerciement du formulaire.
    t = AP.thanks_page(b_, ui, _esc).replace('</head>', css + '\n</head>')
    d = os.path.join(out, b_['thanks_seg'])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(t)
    return n


if __name__ == '__main__':
    import shutil
    for key, b_ in BRANDS.items():
        out = os.path.join(ROOT, b_['outdir'])
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(page(key))
        n_prev = write_previews(key, out)
        # Assets servis a la racine du domaine.
        shutil.copy(os.path.join(ASSETS, 'favicon.svg'), out)
        shutil.copy(os.path.join(ASSETS, 'favicon.ico'), out)
        shutil.copy(os.path.join(ASSETS, 'apple-touch-icon.png'), out)
        shutil.copy(os.path.join(ASSETS, b_['og']), os.path.join(out, 'og.png'))
        shutil.copy(os.path.join(ASSETS, b_['logo']), os.path.join(out, 'logo.svg'))
        print("%-20s -> %s/  (%s)  %d apercu(s)"
              % (b_['name'], b_['outdir'], b_['base'], n_prev))
