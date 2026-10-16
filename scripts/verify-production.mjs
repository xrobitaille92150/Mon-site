import {readFileSync,readdirSync} from 'node:fs';
import {join} from 'node:path';
import assert from 'node:assert/strict';
const base='https://www.myxavier.finance';
const root='dist-advisory';
const walk=dir=>readdirSync(dir,{withFileTypes:true}).flatMap(x=>x.isDirectory()?walk(join(dir,x.name)):[join(dir,x.name)]);
const pages=walk(root).filter(p=>p.endsWith('/index.html'));
const results=[];
for(let i=0;i<pages.length;i+=6){
 await Promise.all(pages.slice(i,i+6).map(async file=>{
  const url=file.slice(root.length).replace(/index\.html$/,'');
  const expectedHtml=readFileSync(file,'utf8');
  const expected=expectedHtml.match(/<title>(.*?)<\/title>/s)[1];
  const response=await fetch(base+url,{signal:AbortSignal.timeout(20000)});
  const body=await response.text();
  assert.equal(response.status,200,url);
  assert(body.includes('<title>'+expected+'</title>'),'Stale page: '+url);
  assert(body.includes(expectedHtml.match(/<main id="main">(.*?)<\/main>/s)[0]),'Stale page content: '+url);
  assert(body.includes('rel="canonical" href="'+base+url+'"'),'Canonical: '+url);
  results.push({url,status:response.status});
 }));
}
const anon=await fetch(base+'/.netlify/functions/member-download?id=close-checklist&lang=fr');
assert.equal(anon.status,401,'Anonymous download must be refused');
const forged=await fetch(base+'/.netlify/functions/member-download?id=close-checklist&lang=fr',{headers:{Cookie:'nf_jwt=forged.invalid.session'}});
assert.equal(forged.status,401,'Forged session must be refused');
for(const path of ['/assets/members.source.js','/netlify/private-resources/workbooks.mjs','/gen/build_advisory.py','/README.md','/brand_assets/logos/client-1.png','/brand_assets/logos/client-19.png']){
 const response=await fetch(base+path);assert.equal(response.status,404,'Internal file exposed: '+path);
}
const book=await fetch(base+'/fr/publications/chantiers-2027-2028/',{redirect:'manual'});
assert.equal(book.status,301);assert(book.headers.get('location').startsWith('https://www.editionsactuarius.com/chantiers-2027-2028/'));
const legacy=readFileSync(join(root,'_redirects'),'utf8').split('\n').filter(line=>/^\/(?:fr\/)?(?:missions|assignments|expertise)\//.test(line));
await Promise.all(legacy.map(async line=>{
 const [from,to]=line.trim().split(/\s+/);
 const response=await fetch(base+from,{redirect:'manual',signal:AbortSignal.timeout(20000)});
 assert.equal(response.status,301,'Legacy page must redirect: '+from);
 assert.equal(new URL(response.headers.get('location'),base).pathname,to,'Anonymous destination: '+from);
}));
console.log(JSON.stringify({base,pages:results.length,anonymous:anon.status,forged:forged.status,internalFiles:'not exposed',legacyBookRedirect:book.status,anonymousRedirects:legacy.length,status:'PASS'},null,2));
