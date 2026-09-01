# -*- coding: utf-8 -*-
# Données de la page Publications. Les sommaires viennent de books_toc.json
# (extraits des .docx du Drive — régénérer via le script d'extraction si les livres évoluent).

UI = {
 'en': dict(
    title="Publications — Insurance Finance Books & White Papers | Xavier Advisory",
    desc="Professional books on insurance finance by Xavier Robitaille: repos, bond management, hedging, 2027-2028 regulatory agenda. Free extracts and white paper.",
    label="Publications", h1="Publications",
    intro="Professional books written from practice: investment accounting, prudential rules and controls, with full accounting entries and worked cases. Published in French. Each book below opens on its first pages: title and full table of contents.",
    free_title="Free documentation",
    free_wp_t="White paper — Insurers: the consolidated 2027-2028 reform calendar",
    free_wp_b="The fifteen reforms of 2027-2028 in one consolidated calendar: what is certain, what is not, and the decisions each deadline forces. Available at publication.",
    free_wp_badge="Coming — September 2026",
    free_ex_t="Free extracts",
    free_ex_b="For each book: the title page and the complete table of contents, free to read.",
    free_ins_t="Insights articles",
    free_ins_b="Technical articles on IFRS 9, investment accounting and platform implementations, free of charge.",
    free_ins_link='<a href="/insights/">Read the articles &rarr;</a>',
    shop_title="Bookshop",
    shop_sub="Four professional books. Written in French. Click a cover to read the first pages: title and full table of contents.",
    release="Forthcoming",
    view="First pages &rarr;",
    preview_label="Preview",
    preview_note="End of preview. The complete book is forthcoming.",
    notify="Get notified at publication",
    mail_ph="Your work email",
    thanks_title="Thank you",
    thanks_body="Your address has been recorded. You will be notified at publication.",
    backcover_title="Back cover",
    thanks_back='<a href="/publications/">&larr; Back to Publications</a>',
    back="&larr; Publications", backhref="/publications/",
    toc_title="Table of contents",
    annexes="Appendices",
    in_french="Book written in French.",
    hint="Click or drag a page corner to turn the pages — or use the arrows.",
    pg_prev="Previous page", pg_next="Next page",
    buy_pdf="Buy the PDF",
    buy_paper="Paperback",
    buy_kindle="Kindle edition",
    buy_note="Secure payment. Invoice and EU VAT handled at checkout. Immediate PDF delivery.",
    preview_note_sale="End of preview. The complete book is available in PDF and paperback.",
 ),
 'fr': dict(
    title="Publications — Ouvrages et livres blancs finance assurance | Xavier Advisory",
    desc="Ouvrages professionnels de Xavier Robitaille : opérations de pension, gestion obligataire, couvertures, chantiers réglementaires 2027-2028. Extraits gratuits et livre blanc.",
    label="Publications", h1="Publications",
    intro="Des ouvrages professionnels écrits depuis la pratique : comptabilité des placements, prudentiel et contrôles, avec écritures comptables complètes et dossiers chiffrés. Chaque ouvrage ci-dessous s'ouvre sur ses premières pages : le titre et la table des matières complète.",
    free_title="Documentation gratuite",
    free_wp_t="Livre blanc — Assureurs : le calendrier consolidé des réformes 2027-2028",
    free_wp_b="Les quinze réformes de 2027-2028 dans un seul calendrier consolidé : ce qui est certain, ce qui ne l'est pas, et les décisions que chaque échéance impose. Disponible à la parution.",
    free_wp_badge="À paraître — septembre 2026",
    free_ex_t="Extraits gratuits",
    free_ex_b="Pour chaque ouvrage : la page de titre et la table des matières complète, en lecture libre.",
    free_ins_t="Articles Décryptages",
    free_ins_b="Des articles techniques sur IFRS 9, la comptabilité des placements et les implémentations de plateformes, en accès libre.",
    free_ins_link='<a href="/fr/insights/">Lire les articles &rarr;</a>',
    shop_title="Boutique",
    shop_sub="Quatre ouvrages professionnels. Cliquez sur une couverture pour lire les premières pages : le titre et la table des matières complète.",
    release="À paraître",
    view="Premières pages &rarr;",
    preview_label="Aperçu",
    preview_note="Fin de l'aperçu. L'ouvrage complet est à paraître.",
    notify="Être prévenu de la parution",
    mail_ph="Votre email professionnel",
    thanks_title="Merci",
    thanks_body="Votre adresse est enregistrée. Vous serez prévenu à la parution.",
    thanks_back='<a href="/fr/publications/">&larr; Retour aux Publications</a>',
    back="&larr; Publications", backhref="/fr/publications/",
    toc_title="Table des matières",
    annexes="Annexes",
    in_french="",
    hint="Cliquez ou faites glisser le coin d'une page pour la tourner — ou utilisez les flèches.",
    pg_prev="Page précédente", pg_next="Page suivante",
    buy_pdf="Acheter le PDF",
    buy_paper="Version papier",
    buy_kindle="Édition Kindle",
    buy_note="Paiement sécurisé. Facture et TVA UE gérées au paiement. PDF livré immédiatement.",
    preview_note_sale="Fin de l'aperçu. L'ouvrage complet est disponible en PDF et en version papier.",
 ),
}

# Ordre d'affichage = ordre du dict.
# Marque d'edition de chaque ouvrage. 'editions' = Editions Actuarius (FR),
# 'press' = Actuarius Press (EN). Le catalogue anglais n'est PAS une traduction
# du francais : les normes francaises n'interessent pas le lectorat anglo-saxon.
# Un ouvrage ne parait que sur le site de sa marque.
IMPRINT_OF = {
 'chantiers-2027-2028':     'editions',
 'operations-de-pension':   'editions',
 'gestion-obligataire':     'editions',
 'operations-de-couverture': 'editions',
 's4hana-fr':               'editions',
 's4hana-en':               'press',
 '2027-2028-agenda':        'press',
}

# La collection remplace l'etiquette de genre « TRAITE » (decision de format
# du 03/08/2026). Deux lignes pour la composition de couverture.
COLL_FR = ["LES CLÉS DE L'ASSURANCE", "ET DE LA FINANCE"]
COLL_EN = ["THE ESSENTIALS OF INSURANCE", "& FINANCE"]

BOOKS = {
 'chantiers-2027-2028': dict(
    src='transformations',
    collection=COLL_FR,
    # Ce titre a une date de parution annoncee ; les autres sont « a paraitre ».
    release="Parution septembre 2026",
    preview_note="Fin de l'aperçu. L'ouvrage complet paraît en septembre 2026.",
    date_published="2026-09",
    t1=["Organismes d'assurance :", "vos chantiers", "de 2027-2028"],
    t2=["Avez-vous anticipé ces 15 réformes ?"],
    sub=[],
    ref=["Solvabilité II révisée · IFRS 18 · IRRD · DORA", "AI Act · Omnibus · fins de support éditeurs"],
    name="Organismes d'assurance : vos chantiers de 2027-2028",
    # Couverture reelle (version finale navy 1b, Claude Design 31/08/2026),
    # servie depuis brand_assets/actuarius/covers/ ; remplace le SVG fictif.
    cover_img='chantiers-2027-2028-recto.jpg',
    back_img='chantiers-2027-2028-4e.jpg',
    og_img='chantiers-2027-2028-og.jpg',
    # Quatrieme de couverture — texte final de Xavier (31/08/2026), source :
    # 10_Work/Livres/transformations_2027-2028/ENSEIGNEMENTS_4E_2026-08-31.md
    backcover=dict(
        paras=[
            "En 2023, un directeur financier d'assurance pouvait résumer sa feuille de route en un seul sigle : IFRS 17. À l'opposé, en 2027 et 2028, la difficulté sera tout autre : pas moins d'une quinzaine de transformations majeures qui devront être conduites sur cette courte période.",
            "Solvabilité II révisée, IFRS 18, AI Act, lutte contre le blanchiment, DORA, NIS2, Cyber Resilience Act, durabilité, facturation électronique, transparence salariale : ces textes pris isolément n'ont que peu de rapport entre eux. Pour autant, leur mise en œuvre mobilisera souvent les mêmes équipes, les mêmes données et les mêmes systèmes d'information. Certains de ces systèmes entreront eux-mêmes en fin de support au moment où la charge de transformation atteindra son maximum.",
            "Pour un assureur, l'enjeu ne se limite pas à respecter les textes qui lui sont directement applicables. Il doit aussi mesurer comment les réformes, qui concernent ses assurés, ses fournisseurs et ses partenaires, modifient sa propre exposition aux risques, ses règles de souscription, sa tarification et ses dispositifs de contrôle.",
        ],
        pivot="Ce livre n'est pas un ouvrage de veille réglementaire de plus.",
        promise="Son objectif est bien plus large : transformer le calendrier réglementaire en programme d'action. Aussi chaque évolution est-elle examinée selon ses effets sur :",
        grid=[
            "la stratégie et la gouvernance ;",
            "la finance, la comptabilité et le reporting ;",
            "les risques, le capital et la solvabilité ;",
            "les produits, la souscription et la gestion des contrats ;",
            "les processus, les données et les systèmes ;",
            "le contrôle interne, l'audit et les relations avec les partenaires.",
        ],
        deliverables="Le lecteur y trouvera une chronologie consolidée, une matrice générale des impacts, une matrice normes-processus-systèmes, des fiches d'impact, des checklists de préparation et une revue des points restant à valider.",
        closing="Un ouvrage indispensable pour éclairer les décisions des Directions Générales, Directions Financières, des Risques, de l'Actuariat et des DSI du secteur de l'assurance.",
    ),
    fr_desc="Quinze réformes simultanées lues deux fois : ce qui s'applique à toute société française, puis l'effet propre chez l'assureur. Impacts sur le compte de résultat, le bilan, le prudentiel, les systèmes et le contrôle interne.",
    en_desc="Fifteen simultaneous reforms read twice: what applies to any French company, then the insurer-specific effect. Impacts on P&L, balance sheet, prudential figures, systems and internal control.",
 ),
 'operations-de-pension': dict(
    src='pension',
    collection=COLL_FR,
    t1=["Les opérations", "de pension"],
    t2=["dans les organismes d'assurance"],
    sub=["Aspects juridiques, économiques, comptables,", "prudentiels et opérationnels"],
    ref=["Normes françaises · IFRS · Solvabilité II"],
    name="Les opérations de pension dans les organismes d'assurance",
    fr_desc="Le repo du point de vue de l'assureur : nature juridique, marché, comptabilité en normes françaises et IFRS, prudentiel, cycle de vie opérationnel et contrôles. Avec dossiers comptables chiffrés.",
    en_desc="Repos from the insurer's standpoint: legal nature, market practice, French GAAP and IFRS accounting, prudential treatment, operational life cycle and controls. With worked accounting cases.",
 ),
 'gestion-obligataire': dict(
    src='obligations',
    collection=COLL_FR,
    t1=["La gestion", "obligataire"],
    t2=["dans l'assurance non-vie"],
    sub=["Instruments, marchés, gestion de portefeuille,", "comptabilité, prudentiel et contrôles"],
    ref=["Normes françaises (ANC 2015-11) · IFRS 9 · Solvabilité II"],
    name="La gestion obligataire dans l'assurance non-vie",
    fr_desc="La gestion obligataire du point de vue de l'assureur non-vie : instruments, marchés, gestion de portefeuille, comptabilité en normes françaises et IFRS 9, Solvabilité II et contrôles.",
    en_desc="Bond portfolio management from the non-life insurer's standpoint: instruments, markets, portfolio management, French GAAP and IFRS 9 accounting, Solvency II and controls.",
 ),
 'operations-de-couverture': dict(
    src='couvertures',
    collection=COLL_FR,
    t1=["Les opérations", "de couverture"],
    t2=["dans les organismes d'assurance"],
    sub=["Change, taux, indices — instruments, stratégies,", "comptabilité, prudentiel et contrôles"],
    ref=["Normes françaises (CRC 2002-09) · IFRS 9 / IAS 39 · Solvabilité II"],
    name="Les opérations de couverture dans les organismes d'assurance",
    fr_desc="Les couvertures de l'assureur : instruments et cadre juridique, stratégies, comptabilité en normes françaises et IFRS, Solvabilité II, gestion et contrôles. Avec dossiers comptables chiffrés.",
    en_desc="Insurers' hedging operations: instruments and legal framework, strategies, French GAAP and IFRS accounting, Solvency II, management and controls. With worked accounting cases.",
 ),
 # Le S/4HANA existe en deux editions distinctes, pas en version bilingue :
 # une fiche par marque, chacune sur le site de sa langue.
 's4hana-fr': dict(
    src='s4hana-fr',
    collection=COLL_FR,
    t1=["Implémenter un ERP", "comptable"],
    t2=["dans une entité d'assurance"],
    sub=["Le cas particulier de", "SAP S/4HANA"],
    ref=["SAP S/4HANA · IFRS 17 / IFRS 9 · Solvabilité II", "Reporting réglementaire"],
    name="Implémenter un ERP comptable dans une entité d'assurance",
    fr_desc="Le remplacement du cœur comptable vu comme une refonte du processus de production financière, pas comme un projet informatique : technologie, cœur financier, éditions et licences, trajectoires de migration, architecture assurance et conduite de programme.",
    en_desc="Replacing the accounting core seen as a redesign of the financial reporting process rather than an IT project: technology, finance core, editions and licensing, migration paths, insurance architecture and programme delivery.",
 ),
 's4hana-en': dict(
    src='s4hana-en',
    collection=COLL_EN,
    t1=["Implementing", "an Accounting ERP"],
    t2=["in an Insurance Entity"],
    sub=["The specific case of", "SAP S/4HANA"],
    ref=["SAP S/4HANA · IFRS 17 / IFRS 9 · Solvency II", "Regulatory reporting"],
    name="Implementing an Accounting ERP in an Insurance Entity",
    fr_desc="Le remplacement du cœur comptable vu comme une refonte du processus de production financière, pas comme un projet informatique. Édition anglaise, publiée par Actuarius Press.",
    en_desc="Replacing the accounting core is a redesign of the financial reporting process, not an IT project. Technology, finance core, editions and licensing, migration paths, insurance architecture and programme delivery.",
 ),
 '2027-2028-agenda': dict(
    src='transformations-en',
    collection=COLL_EN,
    release="Published September 2026",
    preview_note="End of preview. The complete book is published in September 2026.",
    date_published="2026-09",
    t1=["Insurance Organisations:", "Your 2027\u20132028 Transformation", "Agenda"],
    t2=["Have you anticipated these 15 reforms?"],
    sub=[],
    ref=["Solvency II · IFRS 18 · AI Act", "AMLR · DORA · CSRD"],
    name="Insurance Organisations: Your 2027\u20132028 Transformation Agenda",
    # Couverture anglaise reelle (livree par Xavier le 01/09/2026), version navy,
    # servie depuis brand_assets/actuarius/covers/ ; remplace le SVG fictif.
    cover_img='2027-2028-agenda-recto.jpg',
    back_img='2027-2028-agenda-4e.jpg',
    og_img='2027-2028-agenda-og.jpg',
    # Quatrieme de couverture anglaise, transcrite de la couverture livree.
    backcover=dict(
        paras=[
            "In 2023, an insurance CFO could summarise his or her roadmap in a single acronym: IFRS 17. By contrast, 2027 and 2028 will present a very different challenge: no fewer than fifteen major transformations will need to be delivered within this short timeframe.",
            "The revised Solvency II framework, IFRS 18, the AI Act, anti-money-laundering requirements, DORA, NIS2, the Cyber Resilience Act, sustainability, e-invoicing and pay transparency: taken individually, these texts may appear unrelated.",
            "Yet their implementation will often involve the same teams, the same data and the same information systems. Some of these systems will themselves reach the end of their support lifecycle precisely when the transformation workload peaks.",
            "For an insurer, the challenge is not limited to complying with the rules that directly apply to it. The insurer must also assess how reforms affecting policyholders, suppliers and business partners alter its own risk exposure, underwriting rules, pricing practices and control framework.",
        ],
        pivot="This book is not simply another regulatory-monitoring publication.",
        promise="Its purpose is much broader: to turn the regulatory calendar into an actionable programme. Each development is therefore examined in terms of its impact on:",
        grid=[
            "strategy and governance;",
            "finance, accounting and reporting;",
            "risk, capital and solvency;",
            "products, underwriting and policy administration;",
            "processes, data and systems;",
            "internal control, audit and relationships with business partners.",
        ],
        deliverables="Readers will find a consolidated timeline, an overall impact matrix, a regulation-process-systems matrix, impact sheets, preparation checklists and a review of the issues that remain to be resolved.",
        closing="An essential guide to supporting decision-making by General Management, Finance, Risk, Actuarial and IT Departments in the insurance sector.",
    ),
    fr_desc="Édition anglaise du livre « Organismes d'assurance : vos chantiers de 2027-2028 », publiée par Actuarius Press.",
    en_desc="Fifteen simultaneous reforms read twice: what applies to any French company, then the insurer-specific effect. Impacts on P&L, balance sheet, prudential figures, systems and internal control.",
 ),
}

# ── Boutique ────────────────────────────────────────────────────────────────
# Un bouton n'apparaît sur le site QUE si son URL est renseignée ci-dessous.
# Tant qu'un livre n'a aucune URL, la page conserve le formulaire
# « être prévenu de la parution ». Aucun lien cassé possible.
#
#   price  : prix TTC affiché pour le PDF, ex. "89 €" (affiché seulement si
#            au moins une URL est renseignée)
#   ls     : URL de checkout Lemon Squeezy du PDF
#            (Store → Products → Share → Checkout link,
#             ex. https://xavieradvisory.lemonsqueezy.com/buy/xxxxxxxx)
#            L'overlay lemon.js s'active automatiquement : l'acheteur paie
#            sans quitter le site.
#   paper  : URL de la fiche produit papier (Amazon KDP / BoD)
#   kindle : URL de l'édition Kindle / ePub
SHOP = {
 'chantiers-2027-2028':     dict(price="", ls="", paper="", kindle=""),
 'operations-de-pension':   dict(price="", ls="", paper="", kindle=""),
 'gestion-obligataire':     dict(price="", ls="", paper="", kindle=""),
 'operations-de-couverture': dict(price="", ls="", paper="", kindle=""),
 's4hana-fr':               dict(price="", ls="", paper="", kindle=""),
 's4hana-en':               dict(price="", ls="", paper="", kindle=""),
 '2027-2028-agenda':        dict(price="", ls="", paper="", kindle=""),
}
