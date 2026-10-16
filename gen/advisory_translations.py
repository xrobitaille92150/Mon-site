"""English editions of previously French-only analysis. Original publication dates retained."""
EN_AI_BODY = '''
<h2>Overview</h2>
<p>Regulation (EU) 2024/1689 has applied since 2 August 2026, subject to the specific dates in Article 113. The transparency obligations in Article 50 also started to apply on that date, with transitional provisions to assess for existing systems.</p>
<p>For insurers, the main extension concerns the high-risk systems listed in Annex III. Sections 1 to 3 of Chapter III apply to those systems from 2 December 2027. Annex III, point 5(c), expressly covers AI systems intended for risk assessment and pricing in relation to natural persons in life and health insurance.</p>
<p>Insurers should use this period to classify their use cases, establish their role under the regulation and adapt their controls. An inventory, a documented assessment for each system and a high-risk compliance plan are practical starting points.</p>
<h2>1. Application dates</h2>
<div class="table-scroll"><table><tr><th>Date</th><th>Provisions</th><th>Operational consequence</th></tr>
<tr><td>2 February 2025</td><td>Chapters I and II, including Article 4</td><td>Define appropriate AI literacy and training measures.</td></tr>
<tr><td>2 August 2025</td><td>Governance and general-purpose AI models</td><td>Identify models used in internal or purchased systems.</td></tr>
<tr><td>2 August 2026</td><td>General application date; Article 50</td><td>Review interfaces, generated content and information provided.</td></tr>
<tr><td>2 December 2027</td><td>Chapter III, sections 1 to 3, Annex III</td><td>Bring relevant systems, including certain life and health systems, into compliance.</td></tr>
<tr><td>2 August 2028</td><td>Chapter III, sections 1 to 3, Annex I</td><td>Examine regulated products and their safety components.</td></tr></table></div>
<p>The AI Omnibus entered into force on 27 July 2026. The European Commission confirms the extended dates for Annex III and Annex I high-risk systems. Specific transitional provisions still need to be checked for each system.</p>
<h2>2. Classifying use cases</h2>
<p>The inventory should cover production systems, pilots, purchased solutions and local developments that may meet the definition of an AI system. Each record should identify the intended purpose, the decisions made or supported, the people concerned, the data used, the responsible legal entity and any provider.</p>
<p>For Annex III use cases, Article 6(3) provides an exception where the system does not pose a significant risk of harm to health, safety or fundamental rights and does not materially influence the outcome of decision-making. The provision identifies four situations:</p>
<ul><li>a narrow procedural task;</li><li>improving the result of a previously completed human activity;</li><li>detecting patterns or deviations, subject to appropriate human review;</li><li>a preparatory task for an assessment covered by Annex III.</li></ul>
<p>An Annex III system that profiles natural persons remains high-risk. A provider relying on the exception must document its assessment before placing the system on the market or putting it into service, and register the system in the EU database.</p>
<p>Classification therefore belongs at use-case level. One technical solution may have different intended purposes and classifications depending on the entity using it and the decision it supports.</p>
<h2>3. Other insurance AI use cases</h2>
<p>P&amp;C pricing, fraud detection, claims processing, document analysis, employee assistants and customer-service tools do not automatically fall under Annex III, point 5(c). Some uses may fall under another Annex III category, including recruitment, task allocation or employee assessment.</p>
<p>EIOPA’s Opinion of 6 August 2025 covers insurance AI systems that are neither prohibited nor high-risk under the AI Act. It addresses national supervisors and does not create new requirements. It explains how existing insurance governance and risk-management requirements apply to these uses.</p>
<p>The proportionate assessment considers:</p>
<ul><li>the nature, volume and sensitivity of data;</li><li>the number of customers concerned, including vulnerable customers;</li><li>system autonomy and influence on decisions;</li><li>effects on customers, business continuity and financial position;</li><li>the ability to explain output, monitor changes and handle complaints.</li></ul>
<p>These activities can fit existing risk management, model management, Product Oversight and Governance, internal control and outsourcing processes.</p>
<h2>4. Provider and deployer responsibilities</h2>
<p>An insurer’s role depends on what it does with the system. Under Article 25(1), a deployer can become the provider of a high-risk system by placing its own name or trademark on it, making a substantial modification or changing the intended purpose so that the system becomes high-risk.</p>
<p>Contracts with software vendors should therefore establish regulatory responsibilities and access to technical documentation, known limitations, testing conditions, version changes, incidents and logs.</p>
<p>For high-risk systems, Article 26 gives deployers operational obligations:</p>
<ul><li>follow the instructions for use;</li><li>assign human oversight to people with appropriate competence, training and authority;</li><li>check input-data relevance and representativeness where the deployer controls the input;</li><li>monitor operation and handle incidents;</li><li>retain logs under their control for an appropriate period, at least six months unless other rules apply;</li><li>inform people when an Annex III system makes or supports decisions concerning them.</li></ul>
<p>For financial institutions, some controls and logs can be included in governance and documentation already required by EU financial-services law.</p>
<h2>5. Documentation</h2>
<p>Keep documentation by system, including the history of classification decisions. The working file should include:</p>
<ol><li>system identification and intended purpose;</li><li>scope and risk-classification assessment;</li><li>roles of the insurer, vendor and other providers;</li><li>data, quality controls and known limitations;</li><li>human oversight and escalation procedures;</li><li>test plan, test results and acceptance record;</li><li>versions, incidents, drift and corrective actions;</li><li>available logs and retention periods;</li><li>information provided to users, customers and authorities.</li></ol>
<p>For Annex III, point 5(c), Article 27 also requires a fundamental-rights impact assessment before first deployment. Existing data-protection impact assessment work can be reused or cross-referenced where it covers the relevant issues.</p>
<h2>6. An initial 90-day programme</h2>
<div class="table-scroll"><table><tr><th>Period</th><th>Action</th><th>Purpose</th><th>Suggested owner</th></tr>
<tr><td>Days 1–15</td><td>Define inventory scope and appoint its owner.</td><td>Establish coverage for classification and deadlines.</td><td>Sponsor; data or transformation lead.</td></tr>
<tr><td>Days 16–45</td><td>Assess each use case and document the conclusion.</td><td>Account for purpose, entity role and profiling.</td><td>Business, Compliance, Legal, IT and Data.</td></tr>
<tr><td>Days 46–75</td><td>Test the process on two different systems.</td><td>Review classification, vendor documentation, human oversight and acceptance testing.</td><td>Business, Actuarial where relevant, Risk, Compliance and IT.</td></tr>
<tr><td>Days 76–90</td><td>Approve classifications, control gaps and remediation.</td><td>Assign responsibilities, budget and deadlines.</td><td>Relevant existing committee.</td></tr></table></div>
<p>At the end of this first cycle, management should have an initial inventory, reasoned classifications, assigned responsibilities, identified control gaps and a plan for systems subject to the 2 December 2027 deadline.</p>
'''
EN_DEBT_BODY = '''
<p>The Financial Times reported an annual interest bill of more than $2 trillion for OECD governments. The operational question behind that figure is who will buy the debt governments need to issue, and at what yield.</p>
<p>Central banks, banks, insurers, pension funds and other institutional investors have long been significant buyers. Their demand changes while financing needs remain substantial. The price at which a government can refinance matters alongside its outstanding debt.</p>
<h2>Repayment and refinancing costs</h2>
<p>Consider a deliberately simplified example: a government needs to refinance €100bn. At 3%, demand is sufficient to absorb the issue. If some buyers reduce their purchases, the same amount may require a yield of 3.5%, 4% or more.</p>
<p>The government may still be able to repay its debt. The increase in the cost of replacement funding nevertheless changes its budget over time. Higher yields increase interest expense as outstanding bonds mature. Interest expense increases the deficit, which can require further borrowing. New issues then need to attract investors.</p>
<p>This process can produce a gradual deterioration in the budget equation. It does not require a sudden default event.</p>
<h2>The French case</h2>
<p>French debt sustainability is often discussed in terms of a debt-to-GDP threshold. Refinancing dynamics require additional questions:</p>
<ul><li>Who buys French government bonds?</li><li>How much new debt must the market absorb?</li><li>What yield premium do investors require over German Bunds?</li><li>How does the average cost of the outstanding stock change when older bonds mature and are replaced at current yields?</li><li>When does increasing interest expense constrain the budget enough to change perceptions of French risk?</li></ul>
<p>These questions concern the path of funding costs and the ability to maintain demand across successive issues.</p>
<h2>Consequences for insurers</h2>
<p>For institutional investors, including insurers, the implications include the yield curve, sovereign spreads, bond valuations, reinvestment yields, asset-liability management, asset allocation and solvency.</p>
<p>Persistently higher yields make the government’s funding equation more difficult. They can also increase the income available on new long-term investments. The outcome for an insurer depends on its existing assets, liability profile, liquidity needs and reinvestment horizon.</p>
<p>Monitoring sovereign debt therefore includes both repayment risk and the progressive cost of persuading investors to keep funding it.</p>
'''

def add_english(articles):
    a=articles['ai-act-tarification-vie-sante-haut-risque']['fr']
    articles['ai-act-tarification-vie-sante-haut-risque']['en']={**a,
      'title':'AI Act: life and health insurance pricing among high-risk uses | Xavier Advisory',
      'desc':'AI Act classification, provider and deployer roles, documentation and a 90-day work programme for insurance AI systems.',
      'h1':'AI Act: life and health pricing among high-risk uses',
      'h1_plain':'AI Act: life and health pricing among high-risk uses',
      'standfirst':'Classify systems, establish provider and deployer obligations, and prepare controls for the applicable high-risk requirements.',
      'date_h':'22 September 2026','readtime':'Six-minute read','body':EN_AI_BODY,
      'refnote':'Sources: <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj">Regulation (EU) 2024/1689</a>, Articles 6, 25, 26, 27, 50 and 113, Annex III; <a href="https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force">European Commission, AI Omnibus entry into force</a>; <a href="https://www.eiopa.europa.eu/eiopa-publishes-opinion-ai-governance-and-risk-management-2025-08-06_en">EIOPA Opinion, 6 August 2025</a>.<br><br>This scoping analysis retains its original publication date. The English edition and the main application dates were reviewed on 16 October 2026. Specific use cases require their own legal assessment.'}
    a=articles['dette-souveraine-refinancement']['fr']
    articles['dette-souveraine-refinancement']['en']={**a,
      'title':'Sovereign debt: the cost of refinancing | Xavier Advisory',
      'desc':'How refinancing costs connect public debt, bond markets and insurers: yields, interest expense, reinvestment and asset-liability management.',
      'h1':'Sovereign debt and the cost of refinancing',
      'h1_plain':'Sovereign debt and the cost of refinancing',
      'standfirst':'Who will buy the debt governments need to issue, and at what yield? An English adaptation of the French analysis, with implications for insurers.',
      'date_h':'21 September 2026','readtime':'Four-minute read','body':EN_DEBT_BODY,
      'refnote':'Article discussed: <a href="https://www.ft.com/content/4f28ef6c-f727-4d36-88a3-bbdbd13ddfbf">The world’s $2tn interest bill</a>, Financial Times, 8 September 2026. The €100bn refinancing example is illustrative, not a forecast. English adaptation published on 16 October 2026; original French publication date retained.'}
