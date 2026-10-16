import { signup, login, logout, getUser, handleAuthCallback, requestPasswordRecovery, recoverPassword } from '@netlify/identity';

const fr=document.documentElement.lang==='fr';
const t=(a,b)=>fr?a:b;
const auth=document.querySelector('#member-auth');
const library=document.querySelector('#member-library');
const form=document.querySelector('#auth-form');
const status=document.querySelector('#auth-status');
const submit=document.querySelector('#auth-submit');
let mode='signup';let recoveryToken=null;
const message=s=>{status.textContent=s;status.hidden=false;};
const showUser=async()=>{const u=await getUser();auth.hidden=Boolean(u);library.hidden=!u;return u;};
const setMode=m=>{
 mode=m;
 document.querySelectorAll('[data-auth-mode]').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.authMode===m)));
 document.querySelector('#privacy-field').hidden=m!=='signup';
 document.querySelector('#member-privacy').required=m==='signup';
 const pass=document.querySelector('#member-password');pass.autocomplete=m==='login'?'current-password':'new-password';pass.minLength=m==='login'?1:12;
 document.querySelector('#member-email').required=m!=='recovery';
 document.querySelector('#member-email').closest('.field').hidden=m==='recovery';
 submit.textContent=m==='signup'?t('Créer mon accès gratuit','Create my free account'):m==='login'?t('Se connecter','Log in'):t('Enregistrer le nouveau mot de passe','Save new password');
 status.hidden=true;
};
document.querySelectorAll('[data-auth-mode]').forEach(b=>b.addEventListener('click',()=>setMode(b.dataset.authMode)));
const handleError=error=>{
 const code=error?.status||error?.statusCode;
 if(code===429)message(t('Trop de tentatives. Patientez quelques minutes avant de réessayer.','Too many attempts. Please wait a few minutes before trying again.'));
 else if(mode==='login')message(t('Connexion impossible. Vérifiez votre adresse et votre mot de passe, puis la confirmation reçue par email.','Unable to log in. Check your email and password, and your email confirmation.'));
 else message(t('L’opération n’a pas abouti. Si vous avez déjà un compte, utilisez « Se connecter ». Sinon, réessayez dans quelques minutes ou écrivez à Xavier.','The request could not be completed. If you already have an account, use “Log in”. Otherwise, try again in a few minutes or email Xavier.'));
};
form.addEventListener('submit',async ev=>{
 ev.preventDefault();submit.disabled=true;message(t('Traitement en cours…','Processing…'));
 try{
  const email=document.querySelector('#member-email').value.trim();const password=document.querySelector('#member-password').value;
  if(mode==='signup'){
   await signup(email,password,{language:fr?'fr':'en',privacy_version:'2026-10-16',privacy_accepted_at:new Date().toISOString()});
   message(t('Consultez votre boîte email et confirmez votre adresse pour accéder à la bibliothèque. Regardez aussi les courriers indésirables.','Check your email and confirm your address to access the library. Please also check your spam folder.'));
  }else if(mode==='recovery'){
   await recoverPassword(recoveryToken,password);recoveryToken=null;history.replaceState(null,'',location.pathname);await showUser();
  }else{await login(email,password);await showUser();}
  document.querySelector('#member-password').value='';
 }catch(error){handleError(error);}finally{submit.disabled=false;}
});
document.querySelector('#auth-recover').addEventListener('click',async()=>{
 const email=document.querySelector('#member-email');
 if(!email.checkValidity()){email.reportValidity();return;}
 try{await requestPasswordRecovery(email.value.trim());message(t('Si un compte correspond à cette adresse, vous recevrez un lien pour réinitialiser le mot de passe.','If an account matches that email, you will receive a password reset link.'));}catch{message(t('La demande n’a pas abouti. Réessayez dans quelques minutes.','The request could not be completed. Please try again in a few minutes.'));}
});
document.querySelector('#auth-logout').addEventListener('click',async()=>{await logout();await showUser();setMode('login');});
document.querySelectorAll('[data-download]').forEach(button=>button.addEventListener('click',async()=>{
 const out=document.querySelector('#download-status');out.hidden=false;out.textContent=t('Préparation du fichier…','Preparing your file…');button.disabled=true;
 try{
  const response=await fetch(`/.netlify/functions/member-download?id=${encodeURIComponent(button.dataset.download)}&lang=${fr?'fr':'en'}`,{credentials:'same-origin',cache:'no-store'});
  if(response.status===401){await logout();await showUser();setMode('login');message(t('Votre session a expiré. Reconnectez-vous pour télécharger les modèles.','Your session has expired. Log in again to download templates.'));return;}
  if(!response.ok)throw new Error('download');
  const file=await response.blob();const url=URL.createObjectURL(file);const a=document.createElement('a');a.href=url;a.download=`xavier-advisory-${button.dataset.download}-${fr?'fr':'en'}.xlsx`;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);out.textContent=t('Le téléchargement est lancé.','Your download has started.');
 }catch{out.textContent=t('Le téléchargement n’a pas abouti. Réessayez ou contactez Xavier.','The download could not be completed. Try again or contact Xavier.');}finally{button.disabled=false;}
}));

// Confirmation emails may return to the home page: advisory.js routes those hashes here.
try{
 const hash=new URLSearchParams(location.hash.slice(1));
 recoveryToken=hash.get('recovery_token');
 if(recoveryToken){setMode('recovery');message(t('Choisissez votre nouveau mot de passe.','Choose your new password.'));}
 else{await handleAuthCallback();await showUser();}
}catch{message(t('Ce lien de confirmation est invalide ou expiré. Essayez de vous connecter ou demandez un nouveau lien.','This confirmation link is invalid or expired. Try logging in or request a new link.'));}
