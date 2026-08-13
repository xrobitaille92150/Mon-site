# -*- coding: utf-8 -*-
"""Pages légales des deux sites de la maison d'édition.

  Éditions Actuarius (FR) : /mentions-legales/  /confidentialite/  /cgv/
  Actuarius Press    (EN) : /legal/             /privacy/          /terms/

Particularité du schéma de vente : les PDF sont vendus par Lemon
Squeezy, LLC en qualité de revendeur officiel (merchant of record) ;
les éditions papier et Kindle par Amazon. Le contrat de vente est donc
conclu avec la plateforme, et les CGV articulent ce partage plutôt que
de singer des CGV de vente directe.

Données société : legal_data.py (source unique).
"""
from legal_data import (COMPANY as C, HOST, UPDATED_FR, UPDATED_EN)

# CSS des pages légales, tokens de la charte Actuarius.
LEGAL_CSS = """
.legal{max-width:760px;margin:0 auto;padding:2.8rem 0 3.4rem}
.legal h2{font-family:var(--act-font-display);font-size:1.3rem;
          color:var(--act-deep-navy);margin:2rem 0 .6rem}
.legal h2:first-child{margin-top:0}
.legal p,.legal ul{line-height:1.75;margin-bottom:.9rem;font-size:.94rem}
.legal ul{margin-left:1.2rem}
.legal li{margin-bottom:.35rem}
.legal .updated{font-size:.8rem;color:var(--gray);margin-top:2.2rem}
.notify-rgpd{max-width:560px;margin:.9rem auto 0;font-size:.74rem;
             line-height:1.6;color:var(--gray);text-align:center}
.notify-rgpd a{color:var(--act-rich-gold)}
"""

# Segments d'URL par langue.
SEGS = {
 'fr': dict(mentions='mentions-legales', privacy='confidentialite', cgv='cgv'),
 'en': dict(mentions='legal', privacy='privacy', cgv='terms'),
}

LABELS = {
 'fr': dict(mentions="Mentions légales", privacy="Confidentialité",
            cgv="CGV"),
 'en': dict(mentions="Legal notice", privacy="Privacy", cgv="Terms of sale"),
}

TITLES = {
 'fr': dict(mentions="Mentions légales", privacy="Politique de confidentialité",
            cgv="Conditions générales de vente"),
 'en': dict(mentions="Legal notice", privacy="Privacy policy",
            cgv="Terms of sale"),
}


def footer_links(b_):
    """Ancres légales du footer, dans la langue de la marque."""
    seg, lab = SEGS[b_['lang']], LABELS[b_['lang']]
    return ''.join(f'<a href="/{seg[k]}/">{lab[k]}</a>'
                   for k in ('mentions', 'privacy', 'cgv'))


def notify_notice(b_):
    """Mention RGPD affichée sous le formulaire « être prévenu »."""
    seg = SEGS[b_['lang']]['privacy']
    if b_['lang'] == 'fr':
        return (f'<p class="notify-rgpd">Votre email est utilisé par '
                f'{C["name"]} ({b_["name"]}) dans un seul but&nbsp;: vous '
                f'prévenir de la parution de cet ouvrage. Il n\'est ni '
                f'partagé ni utilisé à d\'autres fins, et il est supprimé '
                f'après l\'envoi. Vous pouvez retirer votre consentement à '
                f'tout moment&nbsp;: <a href="mailto:{C["email"]}">'
                f'{C["email"]}</a> &mdash; <a href="/{seg}/">politique de '
                f'confidentialité</a>.</p>')
    return (f'<p class="notify-rgpd">Your email is used by {C["name"]} '
            f'({b_["name"]}) for one purpose only: letting you know when '
            f'this book is released. It is neither shared nor used for '
            f'anything else, and it is deleted after the notification is '
            f'sent. You may withdraw consent at any time: '
            f'<a href="mailto:{C["email"]}">{C["email"]}</a> &mdash; '
            f'<a href="/{seg}/">privacy policy</a>.</p>')


# --- Corps des pages ----------------------------------------------------

def mentions_body(b_):
    if b_['lang'] == 'fr':
        return f"""
<h2>1. Éditeur du site</h2>
<p>Le site <strong>{b_['base'].replace('https://', '')}</strong> est
édité par <strong>{C['name']}</strong>, {C['forme']} au capital de
{C['capital']}, dont le siège social est situé {C['siege']},
immatriculée au {C['rcs']} (SIRET {C['siret']}), n° de TVA
intracommunautaire {C['tva']}.</p>
<p><strong>{b_['name']}</strong> est une marque d'édition d'{C['name']},
qui exerce par ailleurs son activité de conseil sous le nom commercial
Xavier Advisory.</p>
<p>Email : <a href="mailto:{C['email']}">{C['email']}</a> &mdash;
Téléphone : {C['tel']}.</p>
<h2>2. Directeur de la publication</h2>
<p>{C['directeur']}.</p>
<h2>3. Hébergeur</h2>
<p>{HOST['name']}, {HOST['addr']} &mdash;
<a href="{HOST['url']}">{HOST['url']}</a> &mdash;
<a href="mailto:{HOST['email']}">{HOST['email']}</a>.</p>
<h2>4. Propriété intellectuelle</h2>
<p>Les ouvrages présentés, leurs extraits, les couvertures, les textes
et les éléments graphiques de ce site sont protégés par le Code de la
propriété intellectuelle. Toute reproduction, représentation ou
diffusion, totale ou partielle, sans autorisation écrite préalable de
l'éditeur est interdite.</p>
<h2>5. Responsabilité</h2>
<p>L'éditeur s'efforce d'assurer l'exactitude des informations
diffusées, sans pouvoir en garantir l'exhaustivité. Les ouvrages ont un
caractère documentaire et pédagogique&nbsp;: ils ne constituent ni un
conseil professionnel ni une recommandation applicable sans analyse de
la situation particulière du lecteur.</p>
<h2>6. Données personnelles</h2>
<p>Le traitement des données personnelles est décrit dans la
<a href="/confidentialite/">politique de confidentialité</a>.</p>
<p class="updated">Dernière mise à jour : {UPDATED_FR}</p>"""
    return f"""
<h2>1. Site publisher</h2>
<p><strong>{b_['base'].replace('https://', '')}</strong> is published by
<strong>{C['name']}</strong>, an {C['forme_en']} with a share capital of
{C['capital_en']}, registered office at {C['siege']}, registered with
the {C['rcs_en']} (SIRET {C['siret']}), EU VAT number {C['tva']}.</p>
<p><strong>{b_['name']}</strong> is a publishing imprint of {C['name']},
which also carries out its advisory business under the trade name
Xavier Advisory.</p>
<p>Email: <a href="mailto:{C['email']}">{C['email']}</a> &mdash;
Phone: {C['tel']}.</p>
<h2>2. Publication director</h2>
<p>{C['directeur_en']}.</p>
<h2>3. Hosting provider</h2>
<p>{HOST['name']}, {HOST['addr_en']} &mdash;
<a href="{HOST['url']}">{HOST['url']}</a> &mdash;
<a href="mailto:{HOST['email']}">{HOST['email']}</a>.</p>
<h2>4. Intellectual property</h2>
<p>The books presented, their extracts, the covers, the texts and the
graphic elements of this site are protected by intellectual property
law. Any total or partial reproduction, representation or distribution
without the publisher's prior written consent is prohibited.</p>
<h2>5. Liability</h2>
<p>The publisher strives to keep the information published accurate but
cannot guarantee its completeness. The books are documentary and
educational in nature: they constitute neither professional advice nor
a recommendation applicable without an analysis of the reader's
specific situation.</p>
<h2>6. Personal data</h2>
<p>The processing of personal data is described in the
<a href="/privacy/">privacy policy</a>.</p>
<p class="updated">Last updated: {UPDATED_EN}</p>"""


def privacy_body(b_):
    if b_['lang'] == 'fr':
        return f"""
<h2>1. Responsable du traitement</h2>
<p><strong>{C['name']}</strong> ({b_['name']}), {C['forme']},
{C['siege']} &mdash; <a href="mailto:{C['email']}">{C['email']}</a>.</p>
<h2>2. Formulaire « être prévenu de la parution »</h2>
<p>Lorsque vous le remplissez, nous traitons votre <strong>adresse
email</strong> et le <strong>titre de l'ouvrage</strong> concerné.</p>
<ul>
<li><strong>Finalité</strong>&nbsp;: vous informer de la parution de
l'ouvrage. Aucun autre usage&nbsp;: pas de newsletter, pas de
prospection, pas de partage.</li>
<li><strong>Base légale</strong>&nbsp;: votre consentement
(art. 6.1.a RGPD), que vous pouvez retirer à tout moment en écrivant à
<a href="mailto:{C['email']}">{C['email']}</a>.</li>
<li><strong>Destinataire</strong>&nbsp;: le formulaire est traité par
notre hébergeur {HOST['name']} (Netlify Forms, États-Unis).</li>
<li><strong>Durée</strong>&nbsp;: votre email est supprimé après l'envoi
de l'information de parution, et au plus tard 2 ans après la
collecte.</li>
</ul>
<h2>3. Navigation</h2>
<ul>
<li><strong>Journaux de l'hébergeur</strong> ({HOST['name']})&nbsp;:
adresse IP, horodatage, pages consultées. Finalité&nbsp;:
fonctionnement et sécurité. Base légale&nbsp;: intérêt légitime
(art. 6.1.f RGPD). Durée&nbsp;: 30 jours au plus.</li>
<li><strong>Ressources tierces</strong>&nbsp;: les polices sont chargées
depuis Google Fonts et le composant de feuilletage depuis le CDN
jsDelivr&nbsp;; votre adresse IP leur est transmise lors du chargement.
Aucun cookie n'est déposé par ces services.</li>
</ul>
<h2>4. Cookies</h2>
<p>Ce site ne dépose <strong>aucun cookie</strong> soumis à
consentement (pas de mesure d'audience, pas de traceur
publicitaire)&nbsp;: c'est pourquoi aucune bannière n'est affichée. Si
un module de paiement ou de mesure venait à être ajouté, cette
politique et le recueil du consentement seraient mis à jour au
préalable.</p>
<h2>5. Achats</h2>
<p>Les achats s'effectuent auprès de plateformes partenaires (Lemon
Squeezy pour les PDF, Amazon pour le papier et le Kindle), qui agissent
en qualité de responsables de leurs propres traitements&nbsp;: les
données de commande et de paiement sont régies par leurs politiques de
confidentialité. Nous ne recevons jamais vos données de paiement.</p>
<h2>6. Transferts hors UE</h2>
<p>Nos sous-traitants d'hébergement et d'infrastructure ({HOST['name']},
Google, jsDelivr) sont en partie établis aux États-Unis. Ces transferts
sont encadrés par les clauses contractuelles types de la Commission
européenne et, le cas échéant, par la certification des prestataires au
Data Privacy Framework.</p>
<h2>7. Vos droits</h2>
<p>Conformément aux articles 15 à 22 du RGPD, vous disposez des droits
d'accès, de rectification, d'effacement, de limitation, d'opposition et
de portabilité&nbsp;: <a href="mailto:{C['email']}">{C['email']}</a>.
Vous pouvez introduire une réclamation auprès de la CNIL
(<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
<p class="updated">Dernière mise à jour : {UPDATED_FR}</p>"""
    return f"""
<h2>1. Data controller</h2>
<p><strong>{C['name']}</strong> ({b_['name']}), {C['forme_en']},
{C['siege']} &mdash; <a href="mailto:{C['email']}">{C['email']}</a>.</p>
<h2>2. Release notification form</h2>
<p>When you fill it in, we process your <strong>email address</strong>
and the <strong>title of the book</strong> concerned.</p>
<ul>
<li><strong>Purpose</strong>: letting you know when the book is
released. No other use: no newsletter, no prospecting, no sharing.</li>
<li><strong>Legal basis</strong>: your consent (art. 6(1)(a) GDPR),
which you may withdraw at any time by writing to
<a href="mailto:{C['email']}">{C['email']}</a>.</li>
<li><strong>Recipient</strong>: the form is processed by our hosting
provider {HOST['name']} (Netlify Forms, United States).</li>
<li><strong>Retention</strong>: your email is deleted once the release
notification has been sent, and at the latest 2 years after
collection.</li>
</ul>
<h2>3. Browsing</h2>
<ul>
<li><strong>Hosting logs</strong> ({HOST['name']}): IP address,
timestamp, pages viewed. Purpose: operation and security. Legal basis:
legitimate interest (art. 6(1)(f) GDPR). Retention: up to 30 days.</li>
<li><strong>Third-party resources</strong>: fonts are loaded from
Google Fonts and the page-flip component from the jsDelivr CDN; your IP
address is transmitted to them on loading. These services set no
cookies.</li>
</ul>
<h2>4. Cookies</h2>
<p>This site sets <strong>no cookies</strong> requiring consent (no
analytics, no advertising tracers), which is why no consent banner is
displayed. Should a payment or analytics module be added, this policy
and the collection of consent would be updated beforehand.</p>
<h2>5. Purchases</h2>
<p>Purchases are made from partner platforms (Lemon Squeezy for PDFs,
Amazon for paperback and Kindle editions), which act as controllers of
their own processing: order and payment data are governed by their
privacy policies. We never receive your payment data.</p>
<h2>6. Transfers outside the EU</h2>
<p>Our hosting and infrastructure providers ({HOST['name']}, Google,
jsDelivr) are partly established in the United States. These transfers
are governed by the European Commission's standard contractual clauses
and, where applicable, the providers' certification under the Data
Privacy Framework.</p>
<h2>7. Your rights</h2>
<p>Under articles 15 to 22 GDPR you have the rights of access,
rectification, erasure, restriction, objection and portability:
<a href="mailto:{C['email']}">{C['email']}</a>. You may lodge a
complaint with the French supervisory authority, the CNIL
(<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
<p class="updated">Last updated: {UPDATED_EN}</p>"""


def cgv_body(b_):
    if b_['lang'] == 'fr':
        return f"""
<h2>Article 1 &mdash; Objet</h2>
<p>Les présentes conditions encadrent la présentation et la vente des
ouvrages publiés par <strong>{b_['name']}</strong>, marque d'édition
d'{C['name']}, {C['forme']} au capital de {C['capital']}, {C['siege']},
{C['rcs']}, TVA {C['tva']}.</p>
<h2>Article 2 &mdash; Produits</h2>
<p>Les ouvrages sont proposés en trois formats&nbsp;: PDF
(téléchargement), broché (impression à la demande) et Kindle. Les
caractéristiques essentielles (contenu, pagination, langue, extrait)
figurent sur la fiche de chaque ouvrage.</p>
<h2>Article 3 &mdash; Vendeurs</h2>
<p>Ce site est une vitrine&nbsp;: la vente est conclue avec la
plateforme partenaire vers laquelle renvoie chaque bouton d'achat.</p>
<ul>
<li><strong>PDF</strong>&nbsp;: vendus par <strong>Lemon Squeezy,
LLC</strong>, en qualité de revendeur officiel (<em>merchant of
record</em>). Le contrat de vente, l'encaissement, la facturation et la
collecte de la TVA relèvent de Lemon Squeezy et de ses conditions
générales, présentées avant paiement.</li>
<li><strong>Broché et Kindle</strong>&nbsp;: vendus par
<strong>Amazon</strong>, selon ses propres conditions générales de
vente.</li>
</ul>
<h2>Article 4 &mdash; Prix</h2>
<p>Les prix sont affichés en euros, toutes taxes comprises. La TVA
applicable aux livres (5,5&nbsp;% en France, art. 278-0 bis du Code
général des impôts) est appliquée et collectée par la plateforme
vendeuse selon le pays de l'acheteur. Le prix facturé est celui affiché
au moment de la commande.</p>
<h2>Article 5 &mdash; Livraison</h2>
<p>Le PDF est remis en téléchargement immédiatement après paiement, via
le lien fourni par Lemon Squeezy. Les éditions brochées sont imprimées
à la demande et expédiées par Amazon dans les délais indiqués sur la
fiche produit&nbsp;; l'édition Kindle est livrée sur l'appareil ou
l'application du lecteur.</p>
<h2>Article 6 &mdash; Droit de rétractation</h2>
<p>Pour le livre broché, l'acheteur consommateur dispose du délai de
rétractation de 14 jours prévu à l'article L.&nbsp;221-18 du Code de la
consommation, exercé selon les modalités du vendeur (Amazon). Pour le
PDF, contenu numérique fourni immédiatement, le droit de rétractation
ne peut plus être exercé une fois le téléchargement commencé avec
l'accord exprès de l'acheteur et sa renonciation expresse à ce droit
(art. L.&nbsp;221-28, 13° du Code de la consommation)&nbsp;; ce
consentement est recueilli par la plateforme lors du paiement.</p>
<h2>Article 7 &mdash; Garanties légales</h2>
<p>L'acheteur consommateur bénéficie de la garantie légale de
conformité (art. L.&nbsp;217-3 et suivants du Code de la consommation,
et art. L.&nbsp;224-25-12 et suivants pour les contenus numériques) et
de la garantie des vices cachés (art. 1641 et suivants du Code civil),
mises en œuvre auprès du vendeur concerné. En cas de fichier illisible
ou défectueux, l'éditeur remplace le fichier sur simple demande à
<a href="mailto:{C['email']}">{C['email']}</a>.</p>
<h2>Article 8 &mdash; Licence d'utilisation des PDF</h2>
<p>Le PDF acheté est concédé pour un <strong>usage personnel et
professionnel individuel</strong>. Sont interdits&nbsp;: la revente, le
prêt numérique, la diffusion, le partage sur un réseau interne ou
public, et la reproduction au-delà des exceptions légales (art.
L.&nbsp;122-5 du Code de la propriété intellectuelle). Pour un usage
multi-lecteurs (équipe, formation), contactez l'éditeur.</p>
<h2>Article 9 &mdash; Réclamations et médiation</h2>
<p>Pour toute question ou réclamation&nbsp;:
<a href="mailto:{C['email']}">{C['email']}</a> (réponse sous 5 jours
ouvrés). Les achats étant conclus avec la plateforme vendeuse, les
dispositifs de réclamation et de médiation de celle-ci s'appliquent au
contrat de vente. Conformément à l'article L.&nbsp;612-1 du Code de la
consommation, l'éditeur adhérera à un dispositif de médiation de la
consommation avant toute mise en place de vente directe.</p>
<h2>Article 10 &mdash; Droit applicable</h2>
<p>Les présentes conditions sont soumises au droit français, sans
préjudice des dispositions impératives de protection du consommateur du
pays de résidence de l'acheteur.</p>
<p class="updated">Dernière mise à jour : {UPDATED_FR}</p>"""
    return f"""
<h2>Article 1 &mdash; Purpose</h2>
<p>These terms govern the presentation and sale of the books published
by <strong>{b_['name']}</strong>, a publishing imprint of {C['name']},
an {C['forme_en']} with a share capital of {C['capital_en']},
{C['siege']}, {C['rcs_en']}, VAT {C['tva']}.</p>
<h2>Article 2 &mdash; Products</h2>
<p>Books are offered in three formats: PDF (download), paperback
(print on demand) and Kindle. The essential characteristics (contents,
page count, language, extract) appear on each book's page.</p>
<h2>Article 3 &mdash; Sellers</h2>
<p>This site is a showcase: the sale is concluded with the partner
platform each purchase button links to.</p>
<ul>
<li><strong>PDF</strong>: sold by <strong>Lemon Squeezy, LLC</strong>
as merchant of record. The contract of sale, payment collection,
invoicing and VAT collection are handled by Lemon Squeezy under its own
terms, presented before payment.</li>
<li><strong>Paperback and Kindle</strong>: sold by
<strong>Amazon</strong> under its own terms of sale.</li>
</ul>
<h2>Article 4 &mdash; Prices</h2>
<p>Prices are displayed in euros, all taxes included. The VAT
applicable to books is applied and collected by the selling platform
according to the buyer's country. The price charged is the price
displayed at the time of the order.</p>
<h2>Article 5 &mdash; Delivery</h2>
<p>The PDF is delivered for download immediately after payment, via the
link provided by Lemon Squeezy. Paperback editions are printed on
demand and shipped by Amazon within the timeframe shown on the product
page; the Kindle edition is delivered to the reader's device or app.</p>
<h2>Article 6 &mdash; Right of withdrawal</h2>
<p>For paperback books, consumers in the European Union have the
14-day right of withdrawal provided by consumer law, exercised through
the seller (Amazon). For PDFs — digital content supplied immediately —
the right of withdrawal lapses once the download has begun with the
buyer's express consent and express waiver of that right; this consent
is collected by the platform at checkout.</p>
<h2>Article 7 &mdash; Legal guarantees</h2>
<p>Consumers benefit from the legal guarantees applicable in their
country of residence (conformity of goods and of digital content),
exercised against the relevant seller. If a file is unreadable or
defective, the publisher will replace it on request at
<a href="mailto:{C['email']}">{C['email']}</a>.</p>
<h2>Article 8 &mdash; PDF licence</h2>
<p>The purchased PDF is licensed for <strong>individual personal and
professional use</strong>. Resale, digital lending, distribution,
sharing on an internal or public network, and reproduction beyond
statutory exceptions are prohibited. For multi-reader use (teams,
training), contact the publisher.</p>
<h2>Article 9 &mdash; Complaints</h2>
<p>For any question or complaint:
<a href="mailto:{C['email']}">{C['email']}</a> (answer within 5
business days). As purchases are concluded with the selling platform,
its complaint and dispute-resolution schemes apply to the contract of
sale.</p>
<h2>Article 10 &mdash; Governing law</h2>
<p>These terms are governed by French law, without prejudice to the
mandatory consumer-protection provisions of the buyer's country of
residence.</p>
<p class="updated">Last updated: {UPDATED_EN}</p>"""


BODIES = dict(mentions=mentions_body, privacy=privacy_body, cgv=cgv_body)
