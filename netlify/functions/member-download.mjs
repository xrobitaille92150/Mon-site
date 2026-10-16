import { getUser } from '@netlify/identity';
import { getStore } from '@netlify/blobs';

export const config = { rateLimit: { windowLimit: 40, windowSize: 60, aggregateBy: ['ip','domain'] } };
const resources=new Set(['close-checklist','test-matrix','programme-raid','ai-assessment']);
export default async function handler(request) {
 const headers={'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff','Vary':'Cookie, Authorization'};
 if(request.method!=='GET')return new Response('Method not allowed',{status:405,headers:{...headers,Allow:'GET'}});
 const user=await getUser();
 if(!user)return new Response('Authentication required',{status:401,headers});
 // Recheck with Identity: do not trust a stale or revoked client session.
 const token=request.headers.get('cookie')?.match(/(?:^|;\s*)nf_jwt=([^;]+)/)?.[1];
 if(!token)return new Response('Authentication required',{status:401,headers});
 let verification;
 try {verification=await fetch('https://www.myxavier.finance/.netlify/identity/user',{headers:{Authorization:`Bearer ${decodeURIComponent(token)}`},signal:AbortSignal.timeout(8000)});}catch{return new Response('Authentication unavailable',{status:503,headers});}
 if(!verification.ok)return new Response('Authentication required',{status:401,headers});
 const verified=await verification.json();
 if(!verified.confirmed_at||verified.id!==user.id)return new Response('Confirmed account required',{status:401,headers});
 const params=new URL(request.url).searchParams;const id=params.get('id');const lang=params.get('lang')==='fr'?'fr':'en';
 if(!resources.has(id))return new Response('Not found',{status:404,headers});
 // Private site-wide store. No files or encoded contents in the public source repository.
 let file;
 try {file=await getStore('xa-member-templates-v1').get(`${id}-${lang}.xlsx`,{type:'arrayBuffer',consistency:'strong'});}catch{return new Response('File unavailable',{status:503,headers});}
 if(!file)return new Response('File unavailable',{status:503,headers});
 return new Response(file,{status:200,headers:{...headers,'Content-Type':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','Content-Disposition':`attachment; filename="xavier-advisory-${id}-${lang}.xlsx"`}});
}
