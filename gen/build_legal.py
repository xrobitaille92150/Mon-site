# -*- coding: utf-8 -*-
"""Pages légales du site vitrine myxavier.finance (LCEN art. 6-III, RGPD).

  /legal/                  Legal notice (EN)
  /privacy/                Privacy policy (EN)
  /fr/mentions-legales/    Mentions légales (FR)
  /fr/confidentialite/     Politique de confidentialité (FR)

Le site vitrine ne collecte aucune donnée via formulaire : le contact
passe par mailto et Calendly. La politique couvre donc les logs
d'hébergement, la préférence de langue (localStorage) et les ressources
tierces (Google Fonts). Pas de cookie soumis à consentement : pas de
bannière (délibération CNIL n° 2020-091, art. 82 loi Informatique et
Libertés — traceurs strictement fonctionnels exemptés).

Données société : legal_data.py (source unique).
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_pages import CSS, MARK, WORD, STR, BASE, navlinks_html, legal_links
from legal_data import (COMPANY as C, HOST, BRANDS_NOTE_FR, BRANDS_NOTE_EN,
                        UPDATED_FR, UPDATED_EN)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSS additionnel : prose longue à sous-titres nombreux.
LEGAL_CSS = """
.legal h2{font-size:1.25rem;margin:2.2rem 0 .7rem;color:var(--primary)}
.legal h2:first-child{margin-top:0}
.legal p,.legal ul{max-width:720px;line-height:1.75;margin-bottom:.9rem;color:#2A3345}
.legal ul{margin-left:1.2rem}
.legal li{margin-bottom:.35rem}
.legal .updated{font-size:.8rem;color:var(--gray);margin-top:2.4rem}
"""

PAGES = {
 'mentions': dict(
    path_en='legal', path_fr='fr/mentions-legales',
    title_en="Legal notice | Xavier Advisory",
    title_fr="Mentions légales | Xavier Advisory",
    desc_en="Legal notice of myxavier.finance — publisher, publication "
            "director, hosting provider, intellectual property.",
    desc_fr="Mentions légales de myxavier.finance — éditeur, directeur de "
            "la publication, hébergeur, propriété intellectuelle.",
    h1_en="Legal notice", h1_fr="Mentions légales",
    label_en="Legal", label_fr="Informations réglementaires",
 ),
 'privacy': dict(
    path_en='privacy', path_fr='fr/confidentialite',
    title_en="Privacy policy | Xavier Advisory",
    title_fr="Politique de confidentialité | Xavier Advisory",
    desc_en="How myxavier.finance processes personal data: hosting logs, "
            "language preference, third-party resources, your rights (GDPR).",
    desc_fr="Traitement des données personnelles sur myxavier.finance : "
            "logs d'hébergement, préférence de langue, ressources tierces, "
            "vos droits (RGPD).",
    h1_en="Privacy policy", h1_fr="Politique de confidentialité",
    label_en="Privacy", label_fr="Données personnelles",
 ),
}


def mentions_body(lang):
    if lang == 'fr':
        return f"""
<h2>1. Éditeur du site</h2>
<p>Le site <strong>www.myxavier.finance</strong> est édité par
<strong>{C['name']}</strong>, {C['forme']} au capital de {C['capital']},
dont le siège social est situé {C['siege']}, immatriculée au
{C['rcs']} (SIRET {C['siret']}), n° de TVA intracommunautaire
{C['tva']}.</p>
<p>Email : <a href="mailto:{C['email']}">{C['email']}</a> &mdash;
Téléphone : {C['tel']}.</p>
<p>{BRANDS_NOTE_FR}</p>
<h2>2. Directeur de la publication</h2>
<p>{C['directeur']}.</p>
<h2>3. Hébergeur</h2>
<p>{HOST['name']}, {HOST['addr']} &mdash;
<a href="{HOST['url']}">{HOST['url']}</a> &mdash;
<a href="mailto:{HOST['email']}">{HOST['email']}</a>.</p>
<h2>4. Propriété intellectuelle</h2>
<p>L'ensemble du contenu de ce site (textes, logos, marques, éléments
graphiques) est protégé par le Code de la propriété intellectuelle.
Toute reproduction ou représentation, totale ou partielle, sans
autorisation écrite préalable de l'éditeur est interdite. Les marques et
logos de tiers cités sur ce site restent la propriété de leurs titulaires
respectifs.</p>
<h2>5. Responsabilité</h2>
<p>L'éditeur s'efforce d'assurer l'exactitude et la mise à jour des
informations diffusées, sans pouvoir en garantir l'exhaustivité. Les
contenus publiés ont un caractère informatif général et ne constituent
ni un conseil professionnel ni une recommandation d'investissement. Le
site peut contenir des liens vers des sites tiers dont l'éditeur ne
contrôle pas le contenu.</p>
<h2>6. Données personnelles</h2>
<p>Le traitement des données personnelles est décrit dans la
<a href="/fr/confidentialite/">politique de confidentialité</a>.</p>
<p class="updated">Dernière mise à jour : {UPDATED_FR}</p>"""
    return f"""
<h2>1. Site publisher</h2>
<p><strong>www.myxavier.finance</strong> is published by
<strong>{C['name']}</strong>, an {C['forme_en']} with a share capital of
{C['capital_en']}, registered office at {C['siege']}, registered with the
{C['rcs_en']} (SIRET {C['siret']}), EU VAT number {C['tva']}.</p>
<p>Email: <a href="mailto:{C['email']}">{C['email']}</a> &mdash;
Phone: {C['tel']}.</p>
<p>{BRANDS_NOTE_EN}</p>
<h2>2. Publication director</h2>
<p>{C['directeur_en']}.</p>
<h2>3. Hosting provider</h2>
<p>{HOST['name']}, {HOST['addr_en']} &mdash;
<a href="{HOST['url']}">{HOST['url']}</a> &mdash;
<a href="mailto:{HOST['email']}">{HOST['email']}</a>.</p>
<h2>4. Intellectual property</h2>
<p>All content on this site (texts, logos, trademarks, graphic elements)
is protected by intellectual property law. Any total or partial
reproduction or representation without the publisher's prior written
consent is prohibited. Third-party trademarks and logos mentioned on
this site remain the property of their respective owners.</p>
<h2>5. Liability</h2>
<p>The publisher strives to keep the information published accurate and
up to date but cannot guarantee its completeness. Content is provided
for general information purposes and constitutes neither professional
advice nor an investment recommendation. The site may contain links to
third-party websites whose content the publisher does not control.</p>
<h2>6. Personal data</h2>
<p>The processing of personal data is described in the
<a href="/privacy/">privacy policy</a>.</p>
<p class="updated">Last updated: {UPDATED_EN}</p>"""


def privacy_body(lang):
    if lang == 'fr':
        return f"""
<h2>1. Responsable du traitement</h2>
<p><strong>{C['name']}</strong>, {C['forme']}, {C['siege']}, agissant sous
le nom commercial Xavier Advisory &mdash;
<a href="mailto:{C['email']}">{C['email']}</a>.</p>
<h2>2. Données traitées</h2>
<p>Ce site ne comporte ni formulaire, ni création de compte, ni
newsletter&nbsp;: aucune donnée n'y est saisie par le visiteur.
Les seuls traitements sont les suivants&nbsp;:</p>
<ul>
<li><strong>Journaux de l'hébergeur</strong> ({HOST['name']})&nbsp;:
adresse IP, horodatage, pages consultées, navigateur. Finalité&nbsp;:
fonctionnement et sécurité du site. Base légale&nbsp;: intérêt légitime
(art. 6.1.f RGPD). Durée&nbsp;: 30 jours au plus par l'hébergeur.</li>
<li><strong>Préférence de langue</strong>&nbsp;: enregistrée dans le
localStorage de votre navigateur, jamais transmise à un serveur. Traceur
strictement fonctionnel, exempté de consentement (art. 82 de la loi
Informatique et Libertés).</li>
<li><strong>Emails et prises de rendez-vous</strong>&nbsp;: si vous nous
écrivez ou réservez un créneau via Calendly, les données transmises
(nom, email, objet) servent uniquement à traiter votre demande.
Base légale&nbsp;: mesures précontractuelles (art. 6.1.b RGPD).
Durée&nbsp;: la durée de la relation, au plus 3 ans après le dernier
contact. Calendly LLC traite vos données selon sa propre politique de
confidentialité.</li>
</ul>
<h2>3. Ressources tierces</h2>
<p>Les polices de caractères sont chargées depuis Google Fonts&nbsp;: à
cette occasion, votre adresse IP est transmise à Google Ireland Ltd /
Google LLC (États-Unis). Aucun cookie n'est déposé par ce service.</p>
<h2>4. Cookies</h2>
<p>Ce site ne dépose <strong>aucun cookie</strong> soumis à consentement
(pas de mesure d'audience, pas de traceur publicitaire)&nbsp;: c'est
pourquoi aucune bannière de consentement n'est affichée.</p>
<h2>5. Destinataires et transferts hors UE</h2>
<p>Les données décrites ci-dessus sont traitées par nos sous-traitants
d'hébergement et d'infrastructure ({HOST['name']}, Calendly LLC, Google),
établis en partie aux États-Unis. Ces transferts sont encadrés par les
clauses contractuelles types de la Commission européenne et, le cas
échéant, par la certification des prestataires au Data Privacy
Framework. Aucune donnée n'est vendue ni transmise à des fins
commerciales.</p>
<h2>6. Vos droits</h2>
<p>Conformément aux articles 15 à 22 du RGPD, vous disposez des droits
d'accès, de rectification, d'effacement, de limitation, d'opposition et
de portabilité sur vos données. Pour les exercer&nbsp;:
<a href="mailto:{C['email']}">{C['email']}</a>. Vous pouvez introduire
une réclamation auprès de la CNIL
(<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
<p class="updated">Dernière mise à jour : {UPDATED_FR}</p>"""
    return f"""
<h2>1. Data controller</h2>
<p><strong>{C['name']}</strong>, {C['forme_en']}, {C['siege']}, trading
as Xavier Advisory &mdash;
<a href="mailto:{C['email']}">{C['email']}</a>.</p>
<h2>2. Data we process</h2>
<p>This site has no forms, no accounts and no newsletter: visitors do
not enter any data on it. The only processing is the following:</p>
<ul>
<li><strong>Hosting logs</strong> ({HOST['name']}): IP address,
timestamp, pages viewed, browser. Purpose: operation and security of
the site. Legal basis: legitimate interest (art. 6(1)(f) GDPR).
Retention: up to 30 days by the hosting provider.</li>
<li><strong>Language preference</strong>: stored in your browser's
localStorage, never sent to a server. A strictly functional tracer,
exempt from consent requirements.</li>
<li><strong>Emails and meeting bookings</strong>: if you write to us or
book a slot via Calendly, the data you provide (name, email, subject)
is used solely to handle your request. Legal basis: pre-contractual
steps (art. 6(1)(b) GDPR). Retention: the duration of our exchange, at
most 3 years after the last contact. Calendly LLC processes your data
under its own privacy policy.</li>
</ul>
<h2>3. Third-party resources</h2>
<p>Fonts are loaded from Google Fonts; when they load, your IP address
is transmitted to Google Ireland Ltd / Google LLC (United States). This
service sets no cookies.</p>
<h2>4. Cookies</h2>
<p>This site sets <strong>no cookies</strong> requiring consent (no
analytics, no advertising tracers), which is why no consent banner is
displayed.</p>
<h2>5. Recipients and transfers outside the EU</h2>
<p>The data described above is processed by our hosting and
infrastructure providers ({HOST['name']}, Calendly LLC, Google), partly
established in the United States. These transfers are governed by the
European Commission's standard contractual clauses and, where
applicable, the providers' certification under the Data Privacy
Framework. No data is sold or shared for commercial purposes.</p>
<h2>6. Your rights</h2>
<p>Under articles 15 to 22 GDPR you have the rights of access,
rectification, erasure, restriction, objection and portability. To
exercise them: <a href="mailto:{C['email']}">{C['email']}</a>. You may
lodge a complaint with the French supervisory authority, the CNIL
(<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
<p class="updated">Last updated: {UPDATED_EN}</p>"""


BODY = {'mentions': mentions_body, 'privacy': privacy_body}


def page(key, lang):
    d = PAGES[key]
    s = STR[lang]
    other = 'fr' if lang == 'en' else 'en'
    url_en = f"{BASE}/{d['path_en']}/"
    url_fr = f"{BASE}/{d['path_fr']}/"
    url_self = url_en if lang == 'en' else url_fr
    url_other = url_fr if lang == 'en' else url_en
    title = d['title_en'] if lang == 'en' else d['title_fr']
    desc = d['desc_en'] if lang == 'en' else d['desc_fr']
    h1 = d['h1_en'] if lang == 'en' else d['h1_fr']
    label = d['label_en'] if lang == 'en' else d['label_fr']
    navlinks = navlinks_html(lang)
    body = BODY[key](lang)
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
<meta name="robots" content="noindex, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Xavier Advisory">
<meta property="og:title" content="{title}">
<meta property="og:url" content="{url_self}">
<link rel="icon" type="image/svg+xml" href="/brand_assets/xa-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=EB+Garamond:ital,wght@0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet">
<style>{CSS}{LEGAL_CSS}</style>
</head>
<body>
<nav><div class="nav-inner">
  <a class="nav-logo" href="{s['home']}" aria-label="Xavier Advisory">{MARK}{WORD}</a>
  <div class="nav-right">{navlinks}<a class="nav-cta" href="{s['home']}#contact">{s['contact']}</a><a href="{url_other}" rel="alternate" hreflang="{other}">{s['lang_link_label']}</a></div>
</div></nav>
<header class="hero"><div class="wrap">
  <div class="label">{label}</div>
  <h1>{h1}</h1>
</div></header>
<section><div class="wrap legal">{body}</div></section>
<footer><div class="wrap">
  <span>&copy; 2026 Xavier Advisory</span>
  <span><a href="{s['home']}">Xavier Advisory</a><a href="mailto:welcome@myxavier.finance">welcome@myxavier.finance</a>{legal_links(s)}</span>
</div></footer>
</body>
</html>
"""


if __name__ == '__main__':
    os.chdir(ROOT)
    n = 0
    for key, d in PAGES.items():
        for lang in ('en', 'fr'):
            path = d['path_en'] if lang == 'en' else d['path_fr']
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, 'index.html'), 'w',
                      encoding='utf-8') as f:
                f.write(page(key, lang))
            n += 1
    print(f"{n} pages légales générées (site vitrine)")
