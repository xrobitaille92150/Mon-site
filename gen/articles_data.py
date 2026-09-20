# -*- coding: utf-8 -*-

EN_BODY = """
<h2>The question</h2>
<p>A recurring debate in investment accounting teams: can bond premiums and discounts be amortised with a straight-line or interpolated method rather than the effective interest rate (EIR)? The shortcut is tempting. Linear interpolation between present values is easy to build in a spreadsheet, easy to explain, and tolerated in some cases under US&nbsp;GAAP.</p>
<p>For a European insurer, the answer is no. The obligation to amortise at the effective rate is written into IFRS, French statutory accounting, French tax law and supervisory practice. This note assembles the references, because the debate usually dies the moment they are on the table.</p>

<h2>The European regulatory base</h2>
<h3>IFRS 9: the effective interest method is the method</h3>
<p>IFRS 9 §5.4.1: "Interest revenue shall be calculated by using the effective interest method." Appendix A defines the effective interest rate as the rate that exactly discounts estimated future contractual cash flows through the expected life of the financial asset to its gross carrying amount. An interpolated approximation does not meet that definition, even in simplified implementations.</p>
<h3>Solvency II: market-consistent logic</h3>
<p>Directive 2009/138/EC and Delegated Regulation (EU) 2015/35 require market-consistent valuation. Where amortised cost feeds prudential figures, the amortisation must follow the yield determined at acquisition: actuarial logic, consistent with IFRS 9 and national GAAP.</p>
<h3>French statutory accounts: ANC 2015-11 and the true and fair view</h3>
<p>ANC Regulation 2015-11 (Article 122-1) requires the difference between redemption price and acquisition price of fixed-income securities to be spread over their remaining life. The article does not name the method; it does not authorise one that distorts economic reality either. A linear interpolation between spot present values fails to preserve the time value of money across periods, which puts it at odds with the true and fair view required by Article L.123-14 of the Code de commerce.</p>
<h3>French tax law: the explicit rule</h3>
<p>For insurers, Article 38 bis B bis of the Code général des impôts sets an explicitly actuarial rule: the spreading must be such that the book value of the securities equals their present value discounted at the yield-to-maturity determined at acquisition. The tax administration's doctrine (BOFiP, BOI-BIC-PDSTK-10-20-100) applies this to insurance and capitalisation companies. A non-actuarial method exposes the insurer to reclassification of taxable income.</p>

<h2>Across national GAAPs</h2>
<table>
<tr><th>Country</th><th>Basis</th><th>Position</th></tr>
<tr><td>France</td><td>ANC 2015-11 art. 122-1; CGI art. 38 bis B bis</td><td>Actuarial method explicitly required on the tax side; statutory accounts must reflect economic reality.</td></tr>
<tr><td>Germany</td><td>HGB; BaFin circulars</td><td>Premiums and discounts amortised at the effective rate; supervisory guidance anchors actuarial assumptions in HGB figures.</td></tr>
<tr><td>Switzerland</td><td>Swiss GAAP FER (incl. FER 40)</td><td>Amortised cost applied with an actuarial method in insurance practice.</td></tr>
<tr><td>Netherlands</td><td>Dutch GAAP (Title 9, Book 2)</td><td>Converged with IFRS on financial instruments; EIR is standard practice.</td></tr>
<tr><td>Italy, Belgium, Luxembourg</td><td>OIC / Royal Decree 1992 / CAA framework</td><td>Local texts are less explicit; supervisory practice and IFRS consolidation push the same actuarial logic.</td></tr>
</table>
<p>The pattern is consistent: where the text is explicit, it requires the effective rate; where it is silent, supervisory practice and the IFRS anchor leave no room for interpolation in statutory or prudential reporting.</p>

<h2>What the platforms enforce</h2>
<p>Every major investment accounting platform used by European insurers amortises at the effective rate by default: SimCorp Dimension, Clearwater Analytics, NeoXam GP, SAP FAM, Eagle, Aladdin. None of them offers linear interpolation as a statutory amortisation mode. Having implemented SimCorp Dimension and Clearwater Analytics end to end, I have never seen a compliant configuration built on interpolation. When interpolation appears, it lives in a side spreadsheet, and that is where audit findings start.</p>

<h2>Where linear interpolation breaks</h2>
<ul>
<li><strong>Compliance</strong>: it satisfies neither IFRS 9, nor the French tax rule, nor supervisory expectations under Solvency II.</li>
<li><strong>Reporting</strong>: it distorts the interest margin between periods and breaks the matching of income with the economic yield of the instrument.</li>
<li><strong>Technique</strong>: it does not preserve the internal rate of return, and the distortion grows with maturity, coupon structure and rate levels. On long-dated or structured bonds the gap becomes material.</li>
</ul>

<h2>The US GAAP counter-argument</h2>
<p>Under ASC 320, a straight-line method is tolerated when the difference from the effective interest method is immaterial. No equivalent materiality clause exists under IFRS or under the French texts cited above. A method imported from a US parent or a US-built tool does not survive contact with ACPR, BaFin or a French tax audit.</p>

<h2>In practice</h2>
<ul>
<li>Fix the effective rate at acquisition and document it: it is the anchor for accounting, tax and prudential figures.</li>
<li>Keep amortisation in the accounting engine, not in satellite spreadsheets: one calculation, one audit trail.</li>
<li>On migrations, recompute EIR schedules from acquisition data rather than importing residual amortisation balances: this is where historic distortions surface.</li>
<li>Reconcile amortised cost against the custodian at each closing; divergences are usually a symptom of methodology gaps, not data gaps.</li>
</ul>
"""

EN_REF = """Primary sources: <a href="https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/" target="_blank" rel="noopener">IFRS 9, Financial Instruments</a> (§5.4.1 and Appendix A) · <a href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009L0138" target="_blank" rel="noopener">Directive 2009/138/EC (Solvency II)</a> and Delegated Regulation (EU) 2015/35 · ANC Regulation 2015-11, Article 122-1 · <a href="https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034388048" target="_blank" rel="noopener">CGI, Article 38 bis B bis</a> · <a href="https://bofip.impots.gouv.fr/bofip/1996-PGP.html/identifiant=BOI-BIC-PDSTK-10-20-100-20120912" target="_blank" rel="noopener">BOFiP BOI-BIC-PDSTK-10-20-100</a> · Code de commerce, Article L.123-14."""

FR_BODY = """
<h2>La question</h2>
<p>Débat récurrent dans les équipes de comptabilité des placements : peut-on amortir les primes et décotes obligataires avec une méthode linéaire ou interpolée plutôt qu'au taux d'intérêt effectif (TIE) ? Le raccourci est tentant. L'interpolation linéaire entre valeurs actuelles se construit facilement dans un tableur, s'explique facilement, et reste tolérée dans certains cas en US&nbsp;GAAP.</p>
<p>Pour un assureur européen, la réponse est non. L'obligation d'amortir au taux effectif est écrite dans les IFRS, dans le référentiel comptable français, dans la loi fiscale et dans la pratique prudentielle. Cette note rassemble les références, parce que le débat s'éteint en général dès qu'elles sont sur la table.</p>

<h2>Le socle réglementaire européen</h2>
<h3>IFRS 9 : la méthode du taux d'intérêt effectif est la méthode</h3>
<p>IFRS 9 §5.4.1 : « Interest revenue shall be calculated by using the effective interest method. » L'Appendix A définit le taux d'intérêt effectif comme le taux qui actualise exactement les flux de trésorerie contractuels futurs estimés sur la durée de vie attendue de l'actif financier, à sa valeur comptable brute. Une approximation interpolée ne répond pas à cette définition, même dans les implémentations simplifiées.</p>
<h3>Solvabilité II : logique market-consistent</h3>
<p>La directive 2009/138/CE et le règlement délégué (UE) 2015/35 imposent une valorisation market-consistent. Quand le coût amorti alimente les chiffres prudentiels, l'amortissement doit suivre le rendement déterminé à l'acquisition : une logique actuarielle, cohérente avec IFRS 9 et les référentiels nationaux.</p>
<h3>Comptes sociaux français : ANC 2015-11 et image fidèle</h3>
<p>Le règlement ANC 2015-11 (article 122-1) impose d'étaler la différence entre prix de remboursement et prix d'acquisition des titres à revenu fixe sur leur durée de vie résiduelle. L'article ne nomme pas la méthode ; il n'en autorise pas non plus une qui déforme la réalité économique. Une interpolation linéaire entre valeurs actuelles ne préserve pas la valeur temps de l'argent d'une période à l'autre, ce qui la met en contradiction avec l'image fidèle exigée par l'article L.123-14 du Code de commerce.</p>
<h3>Le droit fiscal français : la règle explicite</h3>
<p>Pour les assureurs, l'article 38 bis B bis du Code général des impôts pose une règle explicitement actuarielle : l'étalement doit être tel que la valeur comptable des titres soit égale à leur valeur actuelle, actualisée au taux de rendement actuariel déterminé à l'acquisition. La doctrine administrative (BOFiP, BOI-BIC-PDSTK-10-20-100) l'applique aux entreprises d'assurance et de capitalisation. Une méthode non actuarielle expose l'assureur à un redressement.</p>

<h2>Le tour des référentiels nationaux</h2>
<table>
<tr><th>Pays</th><th>Base</th><th>Position</th></tr>
<tr><td>France</td><td>ANC 2015-11 art. 122-1 ; CGI art. 38 bis B bis</td><td>Méthode actuarielle explicitement requise côté fiscal ; les comptes sociaux doivent refléter la réalité économique.</td></tr>
<tr><td>Allemagne</td><td>HGB ; circulaires BaFin</td><td>Primes et décotes amorties au taux effectif ; la doctrine prudentielle ancre les hypothèses actuarielles dans les chiffres HGB.</td></tr>
<tr><td>Suisse</td><td>Swiss GAAP FER (dont FER 40)</td><td>Coût amorti appliqué avec une méthode actuarielle dans la pratique assurantielle.</td></tr>
<tr><td>Pays-Bas</td><td>Dutch GAAP (Title 9, Book 2)</td><td>Convergé avec les IFRS sur les instruments financiers ; le TIE est la pratique standard.</td></tr>
<tr><td>Italie, Belgique, Luxembourg</td><td>OIC / arrêté royal 1992 / cadre CAA</td><td>Textes locaux moins explicites ; la pratique prudentielle et la consolidation IFRS imposent la même logique actuarielle.</td></tr>
</table>
<p>Le motif est constant : là où le texte est explicite, il exige le taux effectif ; là où il est muet, la pratique prudentielle et l'ancrage IFRS ne laissent aucune place à l'interpolation dans le reporting statutaire ou prudentiel.</p>

<h2>Ce que les plateformes imposent</h2>
<p>Toutes les grandes plateformes de comptabilité des placements utilisées par les assureurs européens amortissent au taux effectif par défaut : SimCorp Dimension, Clearwater Analytics, NeoXam GP, SAP FAM, Eagle, Aladdin. Aucune ne propose l'interpolation linéaire comme mode d'amortissement statutaire. Pour avoir implémenté SimCorp Dimension et Clearwater Analytics de bout en bout, je n'ai jamais vu une configuration conforme construite sur de l'interpolation. Quand elle existe, elle vit dans un tableur satellite, et c'est là que commencent les constats d'audit.</p>

<h2>Où l'interpolation linéaire casse</h2>
<ul>
<li><strong>Conformité</strong> : elle ne satisfait ni IFRS 9, ni la règle fiscale française, ni les attentes prudentielles sous Solvabilité II.</li>
<li><strong>Reporting</strong> : elle déforme la marge d'intérêt entre les périodes et rompt le rattachement des produits au rendement économique de l'instrument.</li>
<li><strong>Technique</strong> : elle ne préserve pas le taux de rendement interne, et l'écart grandit avec la maturité, la structure de coupon et le niveau des taux. Sur les obligations longues ou structurées, l'écart devient significatif.</li>
</ul>

<h2>Le contre-argument US GAAP</h2>
<p>Sous ASC 320, une méthode linéaire est tolérée quand l'écart avec la méthode du taux effectif n'est pas significatif. Aucune clause de matérialité équivalente n'existe dans les IFRS ni dans les textes français cités plus haut. Une méthode importée d'une maison mère américaine ou d'un outil construit pour le marché US ne survit pas au contact de l'ACPR, de la BaFin ou d'un contrôle fiscal français.</p>

<h2>En pratique</h2>
<ul>
<li>Figer le taux effectif à l'acquisition et le documenter : c'est l'ancre des chiffres comptables, fiscaux et prudentiels.</li>
<li>Garder l'amortissement dans le moteur comptable, pas dans des tableurs satellites : un seul calcul, une seule piste d'audit.</li>
<li>En migration, recalculer les échéanciers TIE depuis les données d'acquisition plutôt que d'importer des soldes d'amortissement résiduels : c'est là que remontent les distorsions historiques.</li>
<li>Réconcilier le coût amorti avec le dépositaire à chaque clôture ; les écarts sont en général un symptôme de méthode, pas de données.</li>
</ul>
"""

FR_REF = """Sources : <a href="https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/" target="_blank" rel="noopener">IFRS 9, Financial Instruments</a> (§5.4.1 et Appendix A) · <a href="https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32009L0138" target="_blank" rel="noopener">Directive 2009/138/CE (Solvabilité II)</a> et règlement délégué (UE) 2015/35 · Règlement ANC 2015-11, article 122-1 · <a href="https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034388048" target="_blank" rel="noopener">CGI, article 38 bis B bis</a> · <a href="https://bofip.impots.gouv.fr/bofip/1996-PGP.html/identifiant=BOI-BIC-PDSTK-10-20-100-20120912" target="_blank" rel="noopener">BOFiP BOI-BIC-PDSTK-10-20-100</a> · Code de commerce, article L.123-14."""

ARTICLES = {
 'effective-interest-rate-bond-amortisation': {
  'en': dict(
    title="Effective Interest Rate vs Linear Amortisation in Europe",
    desc="Why the effective interest rate is mandatory for bond premium and discount amortisation at European insurers: IFRS 9, Solvency II, ANC 2015-11, French tax law.",
    label="Investment Accounting",
    h1="Bond Premium and Discount Amortisation: Why the Effective Interest Rate Is Mandatory in Europe",
    h1_plain="Bond premium and discount amortisation: why the effective interest rate is mandatory in Europe",
    standfirst="Linear interpolation is tolerated in some US GAAP setups. For a European insurer it fails IFRS 9, French statutory and tax rules, and supervisory practice. The references, assembled.",
    date_iso="2026-07-03", date_h="3 July 2026", readtime="7 min read",
    body=EN_BODY,
    rel_t="Related expertise",
    rel_b='This note draws on engagements covered in <a href="/expertise/investment-accounting-reporting/">Investment Accounting &amp; Reporting</a> and <a href="/expertise/simcorp-clearwater/">SimCorp Dimension &amp; Clearwater Analytics</a>.',
    refnote=EN_REF,
  ),
  'fr': dict(
    title="TIE ou amortissement linéaire : ce qu'impose la réglementation",
    desc="Pourquoi le taux d'intérêt effectif (TIE) s'impose pour amortir primes et décotes obligataires des assureurs : IFRS 9, Solvabilité II, ANC 2015-11, CGI.",
    label="Comptabilité des investissements",
    h1="Amortissement des primes et décotes obligataires : pourquoi le taux d'intérêt effectif s'impose en Europe",
    h1_plain="Amortissement des primes et décotes obligataires : pourquoi le taux d'intérêt effectif s'impose en Europe",
    standfirst="L'interpolation linéaire est tolérée dans certains montages US GAAP. Pour un assureur européen, elle échoue face à IFRS 9, aux règles comptables et fiscales françaises et à la pratique prudentielle. Les références, rassemblées.",
    date_iso="2026-07-03", date_h="3 juillet 2026", readtime="7 min de lecture",
    body=FR_BODY,
    rel_t="Expertise associée",
    rel_b="Cette note s'appuie sur les missions couvertes dans <a href=\"/fr/expertise/investment-accounting-reporting/\">Comptabilité &amp; Reporting des Investissements</a> et <a href=\"/fr/expertise/simcorp-clearwater/\">SimCorp Dimension &amp; Clearwater Analytics</a>.",
    refnote=FR_REF,
  ),
 },
}
