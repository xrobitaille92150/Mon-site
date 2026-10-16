import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, extname } from 'node:path';
import assert from 'node:assert/strict';
const root='dist-advisory';
const walk=dir=>readdirSync(dir,{withFileTypes:true}).flatMap(x=>x.isDirectory()?walk(join(dir,x.name)):[join(dir,x.name)]);
const pages=walk(root).filter(p=>p.endsWith('/index.html'));
const errors=[];const titles=new Set();let links=0;let schemas=0;
for(const path of pages){
 const html=readFileSync(path,'utf8');
 const title=html.match(/<title>(.*?)<\/title>/s)?.[1];
 if(!title)errors.push(path+': missing title');
 if(titles.has(title))errors.push(path+': duplicated title');titles.add(title);
 if((html.match(/<h1\b/g)||[]).length!==1)errors.push(path+': expected one h1');
 if(!html.includes('name="description"'))errors.push(path+': missing description');
 if(!html.includes('rel="canonical"'))errors.push(path+': missing canonical');
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
if(errors.length){console.error(errors.join('\n'));process.exit(1);}
console.log(JSON.stringify({pages:pages.length,links,schemas,status:'PASS'}));
