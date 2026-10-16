import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, extname } from 'node:path';
import assert from 'node:assert/strict';
const root='dist-advisory';
const walk=dir=>readdirSync(dir,{withFileTypes:true}).flatMap(x=>x.isDirectory()?walk(join(dir,x.name)):[join(dir,x.name)]);
const pages=walk(root).filter(p=>p.endsWith('/index.html'));
const errors=[];const titles=new Set();let links=0;let schemas=0;
const clientNames=/\b(?:Coface|CNP|SCOR|AXA|CACEIS|BPSS|Primexis|Luxempart|CCR)\b/i;
const caseVendors=/\b(?:Clearwater|SimCorp|Bloomberg|Linedata|Chorus|NeoXam|SAP|PeopleSoft|Monday|SAS|Power BI|Palladio|CODA|LPx|TSOX)\b/i;
for(const path of pages){
 const html=readFileSync(path,'utf8');
 if(clientNames.test(html))errors.push(path+': named client or third party');
 if(/\/(?:missions|assignments)\/.+\/index\.html$/.test(path)&&caseVendors.test(html))errors.push(path+': named vendor in case study');
 const title=html.match(/<title>(.*?)<\/title>/s)?.[1];
 if(!title)errors.push(path+': missing title');
 if(titles.has(title))errors.push(path+': duplicated title');titles.add(title);
 if((html.match(/<h1\b/g)||[]).length!==1)errors.push(path+': expected one h1');
 if(!html.includes('name="description"'))errors.push(path+': missing description');
 if(!html.includes('rel="canonical"'))errors.push(path+': missing canonical');
 for(const tag of html.matchAll(/<img\b[^>]*>/g))if(!/\balt="[^"]*"/.test(tag[0]))errors.push(path+': image without alt');
 for(const tag of html.matchAll(/<(?:input|select|textarea)\b[^>]*>/g)){
  if(/type="hidden"/.test(tag[0]))continue;
  const id=tag[0].match(/\bid="([^"]+)"/)?.[1];
  if(!id||!html.includes('for="'+id+'"'))errors.push(path+': form control without label');
 }
 for(const match of html.matchAll(/href="([^" ]*#[^" ]+)"/g)){
  let [url,fragment]=match[1].split('#');
  if(url.startsWith('https://www.myxavier.finance'))url=url.replace('https://www.myxavier.finance','');
  if(url&&!url.startsWith('/'))continue;
  const target=url?join(root,url,url.endsWith('/')?'index.html':''):path;
  if(existsSync(target)){
   const targetHtml=target===path?html:readFileSync(target,'utf8');
   if(!targetHtml.includes('id="'+fragment+'"')&&!targetHtml.includes('name="'+fragment+'"'))errors.push(path+': missing anchor '+match[1]);
  }
 }
 for(const match of html.matchAll(/<script type="application\/ld\+json">(.*?)<\/script>/gs)){try{JSON.parse(match[1]);schemas++;}catch{errors.push(path+': invalid JSON-LD');}}
 for(const match of html.matchAll(/(?:href|src)="([^"#]*)/g)){
  let url=match[1];if(!url.startsWith('/')&&!url.startsWith('https://www.myxavier.finance/'))continue;
  url=url.replace('https://www.myxavier.finance','').split(/[?#]/)[0];
  if(!url||url.startsWith('/.netlify/'))continue;
  const target=join(root,decodeURIComponent(url),url.endsWith('/')?'index.html':'');
  if(!existsSync(target)&&!url.includes('/publications/chantiers-2027-2028/')&&!url.includes('/publications/operations-')&&!url.includes('/publications/gestion-obligataire/')&&!url.includes('/publications/s4hana-'))errors.push(path+': missing '+url);
  links++;
 }
}
assert(!walk(root).some(p=>/node_modules|CV_XRO|CLAUDE|\.env$|\/gen\/|\.source\.js$/.test(p)),'Internal files in publish directory');
assert(!walk(root).some(p=>p.endsWith('.csv')),'Member downloads must not be public static files');
assert(!existsSync(join(root,'brand_assets/logos')),'Client logos must not be published');
const casePages=pages.filter(p=>/\/(?:missions|assignments)\/.+\/index\.html$/.test(p));
assert.equal(casePages.length,18,'Nine bilingual anonymised case studies');
for(const prefix of ['fr/','']){
 for(const slug of ['investment-accounting-ifrs9','insurance-technical-accounting-ifrs17','consolidation-financial-regulatory-reporting'])assert(existsSync(join(root,prefix,'expertise',slug,'index.html')),'Missing distinct expertise: '+slug);
 const reporting=readFileSync(join(root,prefix,'expertise/consolidation-financial-regulatory-reporting/index.html'),'utf8').split('Des missions associées.')[0].split('Related assignments.')[0];
 assert(/Solvabilité II|Solvency II/.test(reporting)&&/Clôtures|Close/.test(reporting),'Closes and Solvency II belong in reporting');
}
assert(readFileSync(join(root,'fr/index.html'),'utf8').includes('Consultant Expert en <em>Assurance, Finance, Investissement &amp; Gestion de Projets</em>'),'Homepage headline includes project management');
assert(!readFileSync(join(root,'sitemap.xml'),'utf8').match(/coface|cnp|scor|axa|clearwater|simcorp/i),'No client or vendor named case URLs in sitemap');
if(errors.length){console.error(errors.join('\n'));process.exit(1);}
console.log(JSON.stringify({pages:pages.length,links,schemas,status:'PASS'}));
