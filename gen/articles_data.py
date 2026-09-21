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

NAV_EN_BODY = """
<p>Insurers have invested in private equity for many years. What is more recent, and particularly interesting in a recent <em>Financial Times</em> article, is that insurers' investment constraints are beginning to influence the way some private equity financing is structured.</p>
<p>The objective is relatively straightforward: to transform part of the risk associated with private equity assets into debt instruments whose characteristics may be more suitable for institutional investors, including insurers.</p>
<p>The mechanics are worth understanding. They also deserve careful scrutiny, because several layers of leverage can ultimately sit underneath a senior tranche carrying a strong credit rating.</p>

<h2>From portfolio value to NAV loans</h2>
<p>Consider a private equity fund holding stakes in several companies.</p>
<p>Those companies will typically have debt of their own. That does not, of course, mean that the fund's investments have negative value. If a portfolio company has an enterprise value of &euro;150 million and net debt of &euro;60 million, its equity is worth approximately &euro;90 million.</p>
<p>By aggregating the value of its investments and taking account of the fund's other assets and liabilities, we arrive at its <strong>NAV &mdash; Net Asset Value</strong>.</p>
<p>A fund can then borrow against this NAV and the cash flows expected from its portfolio. This is the basic principle of a <strong>NAV loan</strong>.</p>
<p>Importantly, this borrowing sits at fund level. It therefore represents an additional layer of debt above the leverage already carried by the underlying portfolio companies.</p>
<p>That distinction matters when assessing the risk.</p>

<h2>When the debt itself is tranched</h2>
<p>The development described by the <em>Financial Times</em> goes one step further.</p>
<p>Some financing structures can be divided into different tranches. A junior tranche absorbs the first losses, providing additional protection to the senior tranche.</p>
<p>The senior tranche can consequently have a significantly lower risk profile and potentially obtain a credit rating compatible with the investment constraints of certain insurers.</p>
<p>The principle is familiar from structured finance. Its application to private markets is nevertheless particularly interesting.</p>
<p>The FT highlights the growth of <strong>Collateralised Fund Obligations (CFOs)</strong>, with issuance by secondaries funds increasing from just over <strong>$400 million in 2021 to $6.5 billion in 2025</strong>.</p>
<p>CFOs and NAV loans are not the same instrument. However, they illustrate a broader development: financial structuring is increasingly being used to reshape the risk and return characteristics of private-market assets.</p>
<p>For insurers, this may provide indirect exposure to those assets through instruments that behave more like conventional fixed income.</p>

<h2>What happens to the underlying risk?</h2>
<p>Structuring redistributes risk between investors. It does not eliminate it.</p>
<p>Consider again our company with an enterprise value of &euro;150 million and net debt of &euro;60 million. The equity is worth &euro;90 million.</p>
<p>Now assume that its enterprise value falls by 20%, to &euro;120 million. If debt remains at &euro;60 million, the value of the equity falls to &euro;60 million.</p>
<p>A <strong>20% decline in enterprise value has therefore produced a 33% decline in equity value</strong>.</p>
<p>That is the effect of leverage.</p>
<p>The decline feeds through into the NAV of the private equity fund. And that NAV is precisely what supports the NAV loan.</p>
<p>Several layers can therefore sit on top of one another:</p>
<p><strong>portfolio-company debt &rarr; value of the fund's investments &rarr; fund NAV &rarr; NAV loan &rarr; senior and junior tranches</strong></p>
<p>The junior tranche protects the senior tranche against the first losses. But the ability of the overall structure to service its debt ultimately remains dependent on the valuations and cash flows generated by the companies held in the underlying funds.</p>
<p>For an institutional investor, this distinction is important. <strong>The legal seniority of a tranche and its credit rating do not remove the need to understand the economic risk several layers beneath it.</strong></p>

<h2>Is there a lesson from the subprime crisis?</h2>
<p>Comparisons with the structured products that played a role in the 2008 financial crisis need to be made carefully. The underlying assets, structures, liquidity characteristics and risks are different.</p>
<p>Nevertheless, the subprime experience provides one useful reminder.</p>
<p>Financial engineering can redistribute risk and create tranches with very different levels of seniority. A strong rating on a senior tranche may be entirely justified by the amount of subordination beneath it.</p>
<p>But structuring does not change the nature of the assets and cash flows at the beginning of the chain.</p>
<p>This becomes particularly important when several layers of leverage accumulate.</p>
<p>The relevant analysis should therefore include scenarios in which several adverse developments occur at the same time: falling private-equity valuations, slower distributions from funds, difficulties affecting several portfolio companies, tighter liquidity and more expensive refinancing.</p>
<p>These are precisely the circumstances in which apparently separate layers of risk can become correlated.</p>

<h2>Insurers need to look beyond the rating</h2>
<p>For an insurer considering this type of investment, I therefore think the analysis needs to go beyond the rating assigned to the senior tranche.</p>
<p>Several factors deserve particular attention:</p>
<ul>
<li>the leverage carried by the underlying portfolio companies;</li>
<li>the actual diversification of the portfolio;</li>
<li>the methodology used to determine NAV;</li>
<li>the size of the NAV loan relative to that NAV;</li>
<li>the effective subordination provided by the junior tranches;</li>
<li>the covenants and events that could trigger restrictions or repayment;</li>
<li>the liquidity of the instrument;</li>
<li>and, importantly, how the entire structure behaves when valuations and distributions fall simultaneously.</li>
</ul>
<p>The development of these instruments is potentially attractive for insurers because it can broaden the range of private-market exposures available in a debt-like format.</p>
<p>However, the greater the financial transformation between the original economic assets and the security ultimately held by the insurer, <strong>the more important it becomes to work back through the entire structure and understand where the risk ultimately sits</strong>.</p>
<p>That is probably the most useful point I take away from this article.</p>
"""

NAV_EN_REF = """Article analysed: <a href="https://www.ft.com/content/9c6fac10-9f3f-4503-9765-b9e29e18c68d" target="_blank" rel="noopener"><em>Private equity turns to financial engineering to lure insurance billions</em></a>, Alexandra Heal, <em>Financial Times</em>, 18 September 2026."""

NAV_FR_BODY = """
<p>Les assureurs investissent dans le private equity depuis longtemps. Ce qui est plus nouveau, et que décrit un article récent du <em>Financial Times</em>, c'est que leurs contraintes commencent à influencer la manière dont certains financements de private equity sont structurés.</p>
<p>L'objectif est assez simple : transformer une partie du risque lié à des actifs de private equity en instruments de dette présentant un profil susceptible de convenir à des investisseurs institutionnels, notamment aux assureurs.</p>
<p>Le mécanisme est intéressant. Il mérite aussi d'être regardé avec attention, car plusieurs niveaux d'endettement peuvent se superposer derrière une tranche senior bénéficiant d'une bonne notation.</p>

<h2>De la valeur des participations au NAV loan</h2>
<p>Prenons un fonds de private equity qui détient plusieurs entreprises.</p>
<p>Ces entreprises sont généralement endettées. Pour autant, la valeur de la participation du fonds n'est évidemment pas négative tant que la valeur de l'entreprise reste supérieure à sa dette nette.</p>
<p>Une entreprise valorisée 150&nbsp;M&euro;, avec 60&nbsp;M&euro; de dette nette, représente ainsi une valeur de 90&nbsp;M&euro; pour ses actionnaires. En agrégeant la valeur des différentes participations et en tenant compte des autres actifs et passifs du fonds, on obtient sa NAV &mdash; Net Asset Value, ou valeur nette d'actif.</p>
<p>Le fonds peut ensuite emprunter en s'appuyant sur cette NAV et sur les cash-flows attendus de son portefeuille. C'est le principe du NAV loan.</p>
<p>Ce financement se situe au niveau du fonds. Il vient donc s'ajouter à la dette déjà portée par les sociétés détenues.</p>
<p>C'est un premier point important pour analyser le risque.</p>

<h2>Une dette qui peut elle-même être structurée</h2>
<p>L'évolution décrite par le <em>Financial Times</em> va un cran plus loin.</p>
<p>Certains financements peuvent désormais être découpés en plusieurs tranches. La tranche junior absorbe les premières pertes. La tranche senior bénéficie de cette subordination et présente donc un risque plus faible.</p>
<p>Elle peut alors obtenir une notation suffisamment élevée pour intéresser des investisseurs aux contraintes de risque plus fortes, parmi lesquels les assureurs.</p>
<p>Le principe est connu en finance structurée. Son application aux marchés privés est en revanche particulièrement intéressante.</p>
<p>Le FT cite notamment le développement des Collateralised Fund Obligations (CFO), dont les émissions par les fonds de secondaries seraient passées d'un peu plus de 400&nbsp;M$ en 2021 à 6,5&nbsp;Md$ en 2025. Les CFO et les NAV loans ne sont pas le même instrument, mais ils participent d'une même évolution : utiliser la structuration financière pour transformer les caractéristiques de risque et de rendement d'actifs privés.</p>
<p>Pour un assureur, cela peut permettre d'accéder indirectement à ces actifs sous la forme d'un instrument qui ressemble davantage à une obligation traditionnelle.</p>

<h2>Quid du risque sous-jacent ?</h2>
<p>La structuration permet de répartir le risque entre différents investisseurs. Elle ne le fait pas disparaître.</p>
<p>Reprenons notre entreprise valorisée 150&nbsp;M&euro;, avec 60&nbsp;M&euro; de dette nette. La participation du fonds vaut 90&nbsp;M&euro;.</p>
<p>Si la valeur de l'entreprise baisse de 20&nbsp;%, à 120&nbsp;M&euro;, la dette reste dans un premier temps à 60&nbsp;M&euro;. La valeur des actions tombe donc à 60&nbsp;M&euro;.</p>
<p>Une baisse de 20&nbsp;% de la valeur d'entreprise entraîne ici une baisse de 33&nbsp;% de la valeur des actions.</p>
<p>Cet effet de levier se retrouve dans la NAV du fonds. Or c'est précisément cette NAV qui sert de support au NAV loan.</p>
<p>On peut ainsi avoir plusieurs étages successifs :</p>
<p><strong>dette des sociétés du portefeuille &rarr; valeur des participations &rarr; NAV du fonds &rarr; NAV loan &rarr; tranches senior et junior.</strong></p>
<p>La tranche junior protège la tranche senior contre les premières pertes. Mais la capacité de remboursement de l'ensemble reste finalement liée aux valorisations et aux cash-flows des entreprises détenues par les fonds.</p>
<p>Cette distinction me paraît essentielle pour un investisseur institutionnel : la qualité juridique d'une tranche senior et sa notation ne dispensent pas d'analyser le risque économique qui se trouve plusieurs étages en dessous.</p>

<h2>Le précédent des subprimes : un parallèle à manier avec précaution</h2>
<p>Il serait excessif d'assimiler ces structures aux produits titrisés qui ont joué un rôle dans la crise financière de 2008. Les actifs, les mécanismes, la liquidité des marchés et les structures sont différents.</p>
<p>Mais l'expérience des subprimes rappelle un principe qui reste valable.</p>
<p>La structuration permet de redistribuer le risque et de créer des tranches présentant des niveaux de séniorité très différents. Une notation élevée sur une tranche senior peut être parfaitement justifiée compte tenu de sa subordination.</p>
<p>Elle ne modifie cependant pas la nature des actifs et des cash-flows qui se trouvent au début de la chaîne.</p>
<p>Lorsque plusieurs niveaux de levier s'accumulent, il devient donc particulièrement important de comprendre comment l'ensemble se comporte dans des scénarios moins favorables : baisse simultanée des valorisations, ralentissement des distributions, difficultés de plusieurs participations, besoins de liquidité ou refinancement plus coûteux.</p>

<h2>Pour les assureurs, regarder au-delà du rating</h2>
<p>Avant d'investir dans ce type de structure, l'analyse devrait donc, à mon sens, aller au-delà de la notation de la tranche senior.</p>
<p>Plusieurs éléments méritent notamment d'être examinés :</p>
<ul>
<li>l'endettement des entreprises sous-jacentes ;</li>
<li>la diversification réelle du portefeuille ;</li>
<li>les méthodes utilisées pour déterminer la NAV ;</li>
<li>le montant du NAV loan rapporté à cette NAV ;</li>
<li>la subordination effective des différentes tranches ;</li>
<li>les covenants et événements susceptibles de déclencher un remboursement ou une restriction ;</li>
<li>la liquidité de l'instrument ;</li>
<li>la sensibilité de la structure à une baisse simultanée des valorisations et des distributions.</li>
</ul>
<p>Le développement de ces instruments est intéressant pour les assureurs puisqu'il élargit potentiellement l'univers des placements accessibles sous une forme obligataire.</p>
<p>Mais plus la transformation financière entre l'actif économique initial et le titre finalement détenu est importante, plus l'analyse doit remonter toute la chaîne jusqu'aux actifs sous-jacents.</p>
<p>C'est probablement le principal enseignement que je retiens de cet article.</p>
"""

NAV_FR_REF = """Article analysé : <a href="https://www.ft.com/content/9c6fac10-9f3f-4503-9765-b9e29e18c68d" target="_blank" rel="noopener"><em>Private equity turns to financial engineering to lure insurance billions</em></a>, Alexandra Heal, <em>Financial Times</em>, 18 septembre 2026."""

DETTE_FR_BODY = """
<p>Le <em>Financial Times</em> s'intéresse à un chiffre assez vertigineux : <strong>plus de 2&nbsp;000 milliards de dollars.</strong></p>
<p>C'est désormais, selon le journal, la facture annuelle des intérêts payés par les États de l'OCDE sur leur dette.</p>
<p>Mais ce n'est pas vraiment ce chiffre qui rend l'article intéressant.</p>
<p>Le sujet de fond est ailleurs : <strong>qui va acheter toute la dette que les États vont devoir émettre dans les prochaines années &mdash; et à quel prix&nbsp;?</strong></p>
<p>Pendant longtemps, une partie importante de cette dette trouvait assez naturellement preneur auprès des banques centrales, des banques, des assureurs, des fonds de pension et d'autres investisseurs institutionnels.</p>
<p>Or cet équilibre évolue.</p>
<p>Dans le même temps, les besoins de financement restent considérables.</p>
<p>Et cela change la nature du problème.</p>

<h2>Rembourser ou se refinancer</h2>
<p><strong>La question n'est pas nécessairement : «&nbsp;Les États pourront-ils rembourser leur dette&nbsp;?&nbsp;»</strong></p>
<p>Elle devient progressivement :</p>
<p><strong>«&nbsp;À quel taux trouveront-ils suffisamment d'investisseurs pour continuer à la financer&nbsp;?&nbsp;»</strong></p>
<p>La nuance est importante.</p>
<p>Prenons un exemple très simplifié.</p>
<p>Un État doit refinancer 100 milliards d'euros de dette.</p>
<p>À 3&nbsp;%, il trouve suffisamment d'acheteurs pour absorber l'émission.</p>
<p>Mais supposons que certains investisseurs structurels réduisent leurs achats.</p>
<p>L'État reste parfaitement capable de rembourser sa dette. Il n'est pas «&nbsp;insolvable&nbsp;».</p>
<p>Simplement, à 3&nbsp;%, il n'y a plus assez d'acheteurs.</p>
<p>Il faudra peut-être offrir 3,5&nbsp;%, 4&nbsp;% ou davantage pour faire revenir la demande.</p>
<p><strong>La dette reste finançable. Mais elle devient plus chère à financer.</strong></p>
<p>Et c'est là que commence le mécanisme potentiellement dangereux.</p>
<p>Des taux plus élevés augmentent progressivement la charge d'intérêt.</p>
<p>Une charge d'intérêt plus importante détériore le déficit.</p>
<p>Un déficit plus important oblige à émettre davantage de dette.</p>
<p>Ces émissions supplémentaires doivent à leur tour trouver des acheteurs.</p>
<p>Et si les investisseurs demandent une rémunération plus élevée pour les absorber, la charge d'intérêt augmente encore.</p>
<p><strong>Taux &rarr; intérêts &rarr; déficit &rarr; émissions &rarr; taux.</strong></p>
<p>Ce n'est pas nécessairement une crise brutale.</p>
<p>Cela peut être une dégradation lente de l'équation budgétaire.</p>

<h2>Le cas français</h2>
<p>Et c'est évidemment là que <strong>le cas français devient particulièrement intéressant</strong>.</p>
<p>La question de la soutenabilité de la dette française est souvent présentée sous la forme d'un seuil :</p>
<blockquote>À partir de quel ratio dette/PIB la dette devient-elle insoutenable&nbsp;?</blockquote>
<p>Je pense que ce n'est plus la seule bonne question.</p>
<p>Il faut aussi regarder <strong>la dynamique du refinancement</strong> :</p>
<p>Qui achète les OAT&nbsp;?</p>
<p>Quelle quantité de dette nouvelle le marché doit-il absorber&nbsp;?</p>
<p>Quelle prime les investisseurs exigent-ils par rapport au Bund allemand&nbsp;?</p>
<p>Comment évolue le coût moyen du stock de dette à mesure que les anciennes obligations arrivent à échéance et sont refinancées aux taux actuels&nbsp;?</p>
<p>Et surtout : <strong>à partir de quand la hausse de la charge d'intérêt réduit-elle suffisamment les marges de manœuvre budgétaires pour modifier la perception du risque français&nbsp;?</strong></p>
<p>C'est beaucoup plus subtil qu'un simple scénario de défaut souverain.</p>

<h2>Ce que cela change pour les assureurs</h2>
<p>Pour les investisseurs institutionnels &mdash; et notamment les assureurs &mdash; le sujet est tout aussi important.</p>
<p>Car derrière une discussion apparemment macroéconomique sur les finances publiques se cachent des conséquences très concrètes :</p>
<p><strong>courbe des taux, spreads souverains, valorisation des portefeuilles obligataires, rendement des réinvestissements, ALM, allocation d'actifs, solvabilité.</strong></p>
<p>Autrement dit, le problème des États et l'opportunité des investisseurs peuvent être les deux faces du même phénomène.</p>
<p>Des taux durablement plus élevés compliquent sérieusement l'équation budgétaire des gouvernements.</p>
<p>Mais ils redonnent également aux investisseurs de long terme accès à des rendements obligataires que l'on n'avait plus vus depuis longtemps.</p>
<p>C'est précisément cette interaction entre <strong>dette publique, marchés obligataires et comportement des investisseurs</strong> qui rend cet article particulièrement intéressant.</p>
<p>Mon principal enseignement après lecture tient finalement en une question :</p>
<p><strong>Le véritable risque sur la dette souveraine européenne est-il aujourd'hui que les États ne puissent plus rembourser&hellip; ou qu'ils doivent progressivement payer beaucoup plus cher pour convaincre le marché de continuer à les financer&nbsp;?</strong></p>
<p>La seconde hypothèse est probablement moins spectaculaire.</p>
<p>Elle pourrait être beaucoup plus importante.</p>
"""

DETTE_FR_REF = """Article analysé : <a href="https://www.ft.com/content/4f28ef6c-f727-4d36-88a3-bbdbd13ddfbf" target="_blank" rel="noopener"><em>The world's $2tn interest bill</em></a>, <em>Financial Times</em>, 8 septembre 2026."""

ARTICLES = {
 'dette-souveraine-refinancement': {
  'fr': dict(
    category='analysis',
    title="Dette souveraine : le vrai risque est celui du refinancement",
    desc="2 000 milliards de dollars d'intérêts par an pour les États de l'OCDE. Pourquoi le risque tient au prix du refinancement plus qu'au défaut, et ce que cela change pour les assureurs.",
    label="Analyse d'articles de fond",
    h1="Dette souveraine : ne plus pouvoir rembourser, ou payer toujours plus cher pour se refinancer&nbsp;?",
    h1_plain="Dette souveraine : ne plus pouvoir rembourser, ou payer toujours plus cher pour se refinancer ?",
    standfirst="La facture d'intérêts des États de l'OCDE dépasse 2 000 milliards de dollars par an. Lecture d'un article récent du Financial Times, et du mécanisme de refinancement qui relie dette publique, marchés obligataires et assureurs.",
    date_iso="2026-09-21", date_h="21 septembre 2026", readtime="4 min de lecture",
    body=DETTE_FR_BODY,
    rel_t="Expertise associée",
    rel_b="Cette analyse se rattache aux missions couvertes dans <a href=\"/fr/expertise/investment-accounting-reporting/\">Comptabilité &amp; Reporting des Investissements</a> et <a href=\"/fr/expertise/ifrs-17-ifrs-9-solvency-ii/\">IFRS 17, IFRS 9 &amp; Solvabilité II</a>.",
    refnote=DETTE_FR_REF,
  ),
 },
 'nav-loans-private-equity-insurers': {
  'en': dict(
    category='analysis',
    title="NAV Loans and Private Equity: What Insurers Should Check",
    desc="How tranched NAV loans and collateralised fund obligations bring private equity risk to insurers in a debt format, and what to analyse beneath the senior rating.",
    label="Analysis of in-depth articles",
    h1="Private Equity: How Financial Engineering Is Bringing NAV Loans onto Insurers' Radar",
    h1_plain="Private equity: how financial engineering is bringing NAV loans onto insurers' radar",
    standfirst="Insurers' investment constraints are starting to shape how some private equity financing is structured. A reading of a recent Financial Times article, and of the layers of leverage that can sit beneath a well-rated senior tranche.",
    date_iso="2026-09-21", date_h="21 September 2026", readtime="5 min read",
    body=NAV_EN_BODY,
    rel_t="Related expertise",
    rel_b='This analysis relates to the work covered in <a href="/expertise/investment-accounting-reporting/">Investment Accounting &amp; Reporting</a> and <a href="/expertise/ifrs-17-ifrs-9-solvency-ii/">IFRS 17, IFRS 9 &amp; Solvency II</a>.',
    refnote=NAV_EN_REF,
  ),
  'fr': dict(
    category='analysis',
    title="NAV loans et private equity : ce que l'assureur doit regarder",
    desc="Comment les NAV loans découpés en tranches et les CFO amènent le risque du private equity chez les assureurs sous forme de dette, et quoi analyser sous la notation senior.",
    label="Analyse d'articles de fond",
    h1="Private equity : quand la structuration financière rapproche les NAV loans des assureurs",
    h1_plain="Private equity : quand la structuration financière rapproche les NAV loans des assureurs",
    standfirst="Les contraintes des assureurs commencent à influencer la manière dont certains financements de private equity sont structurés. Lecture d'un article récent du Financial Times, et des niveaux d'endettement qui peuvent se superposer derrière une tranche senior bien notée.",
    date_iso="2026-09-21", date_h="21 septembre 2026", readtime="5 min de lecture",
    body=NAV_FR_BODY,
    rel_t="Expertise associée",
    rel_b="Cette analyse se rattache aux missions couvertes dans <a href=\"/fr/expertise/investment-accounting-reporting/\">Comptabilité &amp; Reporting des Investissements</a> et <a href=\"/fr/expertise/ifrs-17-ifrs-9-solvency-ii/\">IFRS 17, IFRS 9 &amp; Solvabilité II</a>.",
    refnote=NAV_FR_REF,
  ),
 },
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
