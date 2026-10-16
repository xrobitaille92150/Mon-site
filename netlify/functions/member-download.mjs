import { getUser } from '@netlify/identity';
import workbooks from '../private-resources/workbooks.mjs';

export const config = { rateLimit: { windowLimit: 40, windowSize: 60, aggregateBy: ['ip','domain'] } };

// The files are bundled in this function, never placed in the static publish folder.
const content = {
 'close-checklist': {
  fr:[['Étape','Contrôle','Responsable','Échéance','Preuve attendue','Statut','Commentaire'],['Instructions','Modèle original. Exemples fictifs : adapter les seuils et échéances à votre organisation.','','','','',''],['Données','Vérifier la complétude des fichiers dépositaires','À désigner','À définir','Inventaire des fichiers et horodatage','À faire',''],['Positions','Rapprocher quantités et nominal BO / dépositaire','À désigner','À définir','État des écarts revu','À faire',''],['Valorisation','Comparer les prix et justifier les écarts significatifs','À désigner','À définir','Sources de prix et seuil approuvé','À faire',''],['Comptabilité','Rapprocher comptabilité auxiliaire et grand livre','À désigner','À définir','Balance rapprochée et écarts documentés','À faire',''],['Validation','Revoir les suspens et approuver les ajustements','À désigner','À définir','Revue datée avec valideur','À faire','']],
  en:[['Stage','Control','Owner','Deadline','Expected evidence','Status','Comment'],['Instructions','Original template. Fictional examples: adapt thresholds and dates to your organisation.','','','','',''],['Data','Check completeness of custodian files','Assign owner','Define','File inventory and timestamps','To do',''],['Positions','Reconcile quantities and nominal BO / custodian','Assign owner','Define','Reviewed exception report','To do',''],['Valuation','Compare prices and explain material differences','Assign owner','Define','Price sources and approved threshold','To do',''],['Accounting','Reconcile investment subledger and general ledger','Assign owner','Define','Reconciled trial balance and documented exceptions','To do',''],['Approval','Review suspense accounts and approve adjustments','Assign owner','Define','Dated review with approver','To do','']]
 },
 'test-matrix': {
  fr:[['Identifiant','Instrument fictif','Événement','Référentiel','Entrée','Résultat attendu','Contrôle','Statut','Anomalie'],['Instructions','Modèle original : compléter les schémas attendus selon les règles approuvées.','','','','','','',''],['TEST-01','Obligation A','Acquisition','IFRS','Nominal et prix documentés','Écriture conforme au schéma validé','Débit = crédit ; rapprochement source','À faire',''],['TEST-02','Obligation A','Coupon','IFRS','Échéancier validé','Extinction du coupon couru et encaissement selon schéma','Rapprochement cash et courus','À faire',''],['TEST-03','Fonds B','Valorisation','Normes locales','Valeur liquidative fictive','Valorisation selon méthode approuvée','Rapprochement source de valeur liquidative','À faire',''],['TEST-04','Titre C','Annulation','IFRS','Transaction initiale identifiée','Extourne conforme et traçable','Rapprochement de la transaction et de l’extourne','À faire','']],
  en:[['Identifier','Fictional instrument','Event','Framework','Input','Expected result','Control','Status','Issue'],['Instructions','Original template: complete expected postings using approved rules.','','','','','','',''],['TEST-01','Bond A','Acquisition','IFRS','Documented nominal and price','Posting follows approved scheme','Debits = credits; source reconciliation','To do',''],['TEST-02','Bond A','Coupon','IFRS','Validated schedule','Accrual reversal and cash receipt per approved scheme','Cash and accrual reconciliation','To do',''],['TEST-03','Fund B','Valuation','Local GAAP','Fictional net asset value','Valuation follows approved method','NAV source reconciliation','To do',''],['TEST-04','Security C','Cancellation','IFRS','Original trade identified','Correct and traceable reversal','Original trade and reversal reconciled','To do','']]
 },
 'programme-raid': {
  fr:[['Identifiant','Type','Description fictive','Impact','Responsable','Action','Échéance','Décision attendue','Statut'],['Instructions','Modèle original','Remplacer les exemples fictifs et convenir des règles d’escalade.','','','','','',''],['PRG-01','Dépendance','Format d’interface à valider','Recette différée','À désigner','Faire valider la spécification','À définir','Approbation du format','Ouvert'],['PRG-02','Risque','Données de migration incomplètes','Écarts au rapprochement','À désigner','Mesurer la complétude et définir les corrections','À définir','Arbitrage du périmètre','Ouvert'],['PRG-03','Décision','Date de bascule à confirmer','Mobilisation des équipes','À désigner','Consolider les critères de préparation','À définir','Accord de bascule ou report','À préparer']],
  en:[['Identifier','Type','Fictional description','Impact','Owner','Action','Deadline','Decision needed','Status'],['Instructions','Original template','Replace fictional examples and agree escalation rules.','','','','','',''],['PRG-01','Dependency','Interface format awaiting approval','Testing delayed','Assign owner','Approve the specification','Define','Format approval','Open'],['PRG-02','Risk','Incomplete migration data','Reconciliation exceptions','Assign owner','Measure completeness and define corrections','Define','Scope decision','Open'],['PRG-03','Decision','Cutover date to confirm','Team availability','Assign owner','Consolidate readiness criteria','Define','Go or no-go','To prepare']]
 },
 'ai-assessment': {
  fr:[['Domaine','Question','Réponse','Responsable','Preuve','Action restante'],['Instructions','Modèle original : cadrage opérationnel, à compléter selon votre environnement et les règles applicables.','','','',''],['Besoin','Quel travail précis doit être produit ?','','','',''],['Données','Quelles sources sont autorisées et quelles données doivent être exclues ?','','','',''],['Environnement','Où les données sont-elles traitées et conservées ?','','','',''],['Qualité','Quel jeu de test et quels critères valident le résultat ?','','','',''],['Contrôle','Qui vérifie le résultat et traite les exceptions ?','','','',''],['Traçabilité','Comment conserver sources, versions et validations ?','','','',''],['Exploitation','Comment arrêter le traitement et reprendre manuellement ?','','','',''],['Résultat','Quel temps et quelle qualité sont mesurés avant et après ?','','','','']],
  en:[['Area','Question','Answer','Owner','Evidence','Remaining action'],['Instructions','Original template: operational scoping, to complete for your environment and applicable rules.','','','',''],['Need','What specific work must be produced?','','','',''],['Data','Which sources are authorised and which data must be excluded?','','','',''],['Environment','Where are data processed and retained?','','','',''],['Quality','Which test set and acceptance criteria validate the result?','','','',''],['Control','Who reviews the output and handles exceptions?','','','',''],['Traceability','How are sources, versions and approvals retained?','','','',''],['Operation','How can processing stop and manual work resume?','','','',''],['Results','Which time and quality measures are recorded before and after?','','','','']]
 }
};
const csv = rows => '\uFEFF'+rows.map(row=>row.map(x=>'"'+String(x).replaceAll('"','""')+'"').join(';')).join('\r\n')+'\r\n';
export default async function handler(request) {
 const headers={'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff','Vary':'Cookie, Authorization'};
 if(request.method!=='GET')return new Response('Method not allowed',{status:405,headers:{...headers,Allow:'GET'}});
 const user=await getUser();
 if(!user)return new Response('Authentication required',{status:401,headers});
 // Verify with Identity itself as well, so a stale or revoked session cannot download.
 const token=request.headers.get('cookie')?.match(/(?:^|;\s*)nf_jwt=([^;]+)/)?.[1];
 if(!token)return new Response('Authentication required',{status:401,headers});
 let verification;
 try {verification=await fetch('https://www.myxavier.finance/.netlify/identity/user',{headers:{Authorization:`Bearer ${decodeURIComponent(token)}`},signal:AbortSignal.timeout(8000)});}catch{return new Response('Authentication unavailable',{status:503,headers});}
 if(!verification.ok)return new Response('Authentication required',{status:401,headers});
 const verified=await verification.json();
 if(!verified.confirmed_at||verified.id!==user.id)return new Response('Confirmed account required',{status:401,headers});
 const params=new URL(request.url).searchParams;const id=params.get('id');const lang=params.get('lang')==='fr'?'fr':'en';
 if(!Object.hasOwn(content,id))return new Response('Not found',{status:404,headers});
 if(params.get('format')!=='csv'){
  const encoded=workbooks[`${id}-${lang}`];
  if(!encoded)return new Response('File unavailable',{status:503,headers});
  return new Response(Buffer.from(encoded,'base64'),{status:200,headers:{...headers,'Content-Type':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','Content-Disposition':`attachment; filename="xavier-advisory-${id}-${lang}.xlsx"`}});
 }
 return new Response(csv(content[id][lang]),{status:200,headers:{...headers,'Content-Type':'text/csv; charset=utf-8','Content-Disposition':`attachment; filename="xavier-advisory-${id}-${lang}.csv"`}});
}
