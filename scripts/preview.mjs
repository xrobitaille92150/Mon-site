// Static review only. Never serves repository sources or private member files.
import {createServer} from 'node:http';
import {readFile,stat,realpath} from 'node:fs/promises';
import {resolve,extname,sep} from 'node:path';

const root=await realpath('dist-advisory');
const port=Number(process.env.ADVISORY_PREVIEW_PORT||3000);
if(!Number.isInteger(port)||port<1024||port>65535)throw new Error('Invalid preview port');
const types={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.webp':'image/webp','.woff2':'font/woff2','.xml':'application/xml','.txt':'text/plain; charset=utf-8','.ico':'image/x-icon'};
const server=createServer(async(req,res)=>{
 res.setHeader('Cache-Control','no-store');
 res.setHeader('X-Content-Type-Options','nosniff');
 if(!['GET','HEAD'].includes(req.method)){res.writeHead(405,{Allow:'GET, HEAD'});res.end();return;}
 try{
  const pathname=decodeURIComponent(new URL(req.url,'http://127.0.0.1').pathname);
  let path=resolve(root,'.'+pathname);
  if(path!==root&&!path.startsWith(root+sep)){res.writeHead(403);res.end();return;}
  if((await stat(path)).isDirectory())path=resolve(path,'index.html');
  path=await realpath(path);
  if(!path.startsWith(root+sep)){res.writeHead(403);res.end();return;}
  const content=await readFile(path);
  res.writeHead(200,{'Content-Type':types[extname(path)]||'application/octet-stream','Content-Length':content.length});
  res.end(req.method==='HEAD'?undefined:content);
 }catch(error){
  res.writeHead(error instanceof URIError?400:404);res.end();
 }
});
server.on('error',error=>{console.error(error.code==='EADDRINUSE'?`Port ${port} already in use; reuse the existing preview.`:error.message);process.exitCode=1;});
server.listen(port,'127.0.0.1',()=>{
 console.log(`Aperçu local : http://127.0.0.1:${port}/fr/#expertise`);
 console.log('Lecture seule, sans publication Netlify. Relancer npm run build après une correction, puis actualiser la page.');
 console.log('La connexion abonné et les fonctions serveur ne sont pas exécutées par cet aperçu statique.');
});
for(const signal of ['SIGINT','SIGTERM'])process.on(signal,()=>server.close(()=>process.exit(0)));
