import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';

const pages={fr:readFileSync('dist-advisory/fr/index.html','utf8'),en:readFileSync('dist-advisory/index.html','utf8')};
const text=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/\s+/g,' ');
// Regression checks for the user's 20 annotated changes, in both languages.
const annotations=[
 [1,'25 ans dans l’assurance et la gestion d’actifs.','25 years in insurance and asset management.'],
 [2,'expertise projet, ESCP.','project expertise and ESCP.'],
 [3,'la totalité des métiers du chiffre d’une compagnie d’assurance et le management de programmes complexes.','the full range of financial disciplines within an insurance company and the management of complex programmes.'],
 [4,'Assurance, Finance & Gestion de Projets','Insurance, Finance & Project Management Expertise'],
 [5,'Mes clients','My clients'],
 [6,'La complémentarité d’une expertise technique, d’expériences opérationnelles et de la conduite de projets complexes.','Technical expertise, operational experience and the management of complex projects.'],
 [7,'Mon parcours réunit audit financier, management d’équipes, production comptable, financière ou réglementaire, accompagnement des évolutions normatives.','My background combines financial audit, team management, accounting operations, financial and regulatory reporting, and the implementation of accounting and regulatory changes.'],
 [8,'Comptabilité & provisionnement','Accounting & reserving'],
 [9,'Schémas comptables French GAAP et IFRS, provisionnement, consolidation et communication financière, états réglementaires.','French GAAP and IFRS accounting schemes, reserving, consolidation and financial disclosures, regulatory reporting.'],
 [10,'Back et Middle Office titres, parfaite maîtrise d’IFRS 9 (bucketisation, test SPPI, ECL), comptabilisation des opérations de couverture, des repos et des produits structurés.','Investment Back and Middle Office, expert command of IFRS 9 (classification, SPPI testing, ECL), accounting for hedging transactions, repos and structured products.'],
 [11,'Outils de place et data management','Industry platforms and data management'],
 [12,'Automatisation du traitement des données par l’utilisation de l’IA.','AI-assisted automation of data processing.'],
 [13,'Expressions de besoins, sélection, spécifications fonctionnelles, recettes, migrations, change management.','Requirements, solution selection, functional specifications, acceptance testing, migrations and change management.'],
 [14,'Maîtrise d’ouvrage et Gestion de projets','Business analysis and project management'],
 [15,'Typologie des missions que je peux réaliser pour vous.','Types of assignments I can undertake for you.'],
 [16,'Des usages adaptés à votre politique de protection des données, à vos modes de travail et toujours sous supervision humaine.','Use cases adapted to your data protection policy and ways of working, always under human supervision.'],
 [17,'Une palette d’outils éprouvés pour répondre à vos besoins.','Proven tools to meet your needs.'],
 [19,'J’ai créé une maison d’édition professionnelle (Éditions Actuarius / Actuarius Press) pour prolonger mon travail de conseil par des analyses, des cas chiffrés et des outils de contrôle.','I created a professional publishing house (Éditions Actuarius / Actuarius Press) to extend my consulting work through analysis, worked cases and control tools.'],
 [20,'Vous souhaitez écrire un livre sur votre domaine de compétence dans les domaines de l’assurance ou de la finance ?','Would you like to write a book about your area of expertise in insurance or finance?']
];
for(const [lang,html] of Object.entries(pages)){
 const rendered=text(html);
 const icons=[...html.matchAll(/<svg class="domain-glyph" data-icon="([^"]+)"[^>]*>(.*?)<\/svg>/gs)];
 assert.equal(icons.length,7,'Seven discipline icons: '+lang);
 assert.equal(new Set(icons.map(x=>x[1])).size,7,'One icon ID per discipline: '+lang);
 assert.equal(new Set(icons.map(x=>x[2])).size,7,'Each discipline has a distinct drawing: '+lang);
 assert.deepEqual(icons.map(x=>x[1]),['investments','technical','reporting','programme','management','standards','ai'],'Semantic icon order: '+lang);
 for(const [svg] of icons)assert(svg.includes('aria-hidden="true"')&&svg.includes('focusable="false"'),'Decorative icon accessibility: '+lang);
 for(const [id,fr,en] of annotations)assert(rendered.includes(lang==='fr'?fr:en),`Annotation ${id} (${lang})`);
 const cards=[...html.matchAll(/<article class="expertise-item">(.*?)<\/article>/gs)].map(x=>text(x[1]));
 const updatedCards=lang==='fr'?[
  ['Comptabilité des placements : French GAAP & IFRS 9','ICNE','PRE, PDD, réserve de capitalisation','résultats réalisés et latents'],
  ['Comptabilité technique : vie et non-vie','PSAP, PNA, PREC, IBNR, PM, PGG','IFRS 17','nouveaux produits','AP/AR'],
  ['fiabilisation des clôtures','VarCap, TFT','production des QRT'],
  ['RFI/RFP','lotissement','UAT','instances projet'],
  ['Remplacement au pied levé','qualité, délais','Management des équipes','amélioration des processus'],
  ['Veille normative et mise en œuvre de nouvelles normes','gap analysis','formation des équipes']
 ]:[
  ['Investment accounting: French GAAP & IFRS 9','accrued interest','PRE, PDD, capitalisation reserve','realised and unrealised gains and losses'],
  ['Insurance technical accounting: life and non-life','PSAP, PNA, PREC, IBNR, PM, PGG','IFRS 17','new products','AP/AR'],
  ['financial closes','changes in equity and cash flows','QRT production'],
  ['RFI/RFP','work packages','UAT','project governance bodies'],
  ['short notice','quality and deadlines','Team management','process documentation and improvement'],
  ['Accounting and regulatory monitoring & implementation','gap analysis','team training']
 ];
 updatedCards.forEach((terms,index)=>terms.forEach(term=>assert(cards[index].includes(term),`Updated discipline ${index+1} (${lang}): ${term}`)));
 assert(!cards.join(' ').includes(lang==='fr'?'Outils de place & projets métier':'Industry platforms & business projects'),'Replaced duplicate systems discipline: '+lang);
 const prefix=lang==='fr'?'fr/':'';
 const standards=readFileSync(`dist-advisory/${prefix}expertise/accounting-regulatory-change/index.html`,'utf8');
 for(const slug of ['ifrs9-assureur-credit','transformation-finance-assureur-iard'])assert(standards.includes(slug),'Standards linked to relevant experience: '+lang);
 const redirects=readFileSync('dist-advisory/_redirects','utf8');
 assert(redirects.includes(`/${prefix}expertise/investment-systems-business-projects/ /${prefix}expertise/accounting-regulatory-change/ 301!`),'Old competence URL preserved: '+lang);
 const profile=html.match(/<section class="section" id="profile">(.*?)<\/section>/s)[1];
 assert.equal((profile.match(/class="cross-row"/g)||[]).length,4,'Four expertise blocks: '+lang);
 assert(!/\bSAS\b/.test(profile),'SAS removed from the annotated platform list: '+lang);
 assert(profile.includes('RACI')&&profile.includes('CxO')&&profile.includes('PMO'),'PMO detail: '+lang);
 const clients=html.match(/<div class="trust" id="clients">(.*?)<\/span><\/div><\/div><\/div>/s)[1];
 const ordered=lang==='fr'?['Assureurs IARD','Assureurs Vie','Réassureurs','Gestionnaires d’actifs','Éditeurs de logiciels']:['P&C insurers','Life insurers','Reinsurers','Asset managers','Software vendors'];
 let offset=-1;
 for(const client of ordered){const index=clients.indexOf(client);assert(index>offset,`Client order (${lang}): ${client}`);offset=index;}
 assert(/class="publishing-invitation"[^]*?<a href="mailto:xro@xavier-robitaille.com">/.test(html),'Author contact link: '+lang);
}
const css=readFileSync('dist-advisory/assets/advisory.css','utf8');
assert(/\.book-scene img\{[^}]*height:auto;[^}]*aspect-ratio:7\/10;[^}]*object-fit:contain;[^}]*transform:none;/.test(css),'Annotation 18: undistorted 7:10 cover');
assert(!/rotateY\(/.test(css),'No perspective distortion on the cover');
console.log(JSON.stringify({annotations:20,languages:2,profileBlocks:4,coverRatio:'7:10',status:'PASS'}));
