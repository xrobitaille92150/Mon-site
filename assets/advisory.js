(() => {
  'use strict';
  const fr = document.documentElement.lang === 'fr';
  if (/(?:^#|&)(confirmation_token|recovery_token|invite_token|access_token)=/.test(location.hash) && !document.querySelector('#auth-form')) {
    location.replace((fr?'/fr/abonnes/':'/members/')+location.hash);
    return;
  }
  const say = (a,b) => fr ? a : b;
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#navigation');
  const closeMenu = () => { nav?.classList.remove('open'); menu?.setAttribute('aria-expanded','false'); };
  menu?.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('open',open);
  });
  nav?.querySelectorAll('a').forEach(a => a.addEventListener('click',closeMenu));
  document.addEventListener('keydown', event => { if (event.key === 'Escape') { closeMenu(); menu?.focus(); } });
  const consent = document.querySelector('#consent');
  const consentKey = 'xa-audience-v1';
  let analyticsLoaded = false;
  const readChoice = () => { try { const c=JSON.parse(localStorage.getItem(consentKey)); return c && c.until>Date.now()?c:null; } catch { return null; } };
  const analytics = () => {
    if (analyticsLoaded || !['www.myxavier.finance','myxavier.finance'].includes(location.hostname)) return;
    analyticsLoaded=true;
    const s=document.createElement('script'); s.src='https://cloud.umami.is/script.js';s.defer=true;
    s.dataset.websiteId='ca7b8fbb-2534-4848-83ef-28415b404c16'; s.dataset.doNotTrack='true';s.dataset.domains='www.myxavier.finance';
    document.head.append(s);
  };
  const saved = readChoice();
  if (!saved && consent) consent.hidden=false;
  if (saved?.choice==='yes') analytics();
  document.querySelectorAll('[data-consent]').forEach(button=>button.addEventListener('click',()=>{
    const choice=button.dataset.consent;
    try { localStorage.setItem(consentKey,JSON.stringify({choice,until:Date.now()+180*86400000})); } catch {}
    consent.hidden=true;
    // Reload after withdrawal to remove any running analytics instance.
    if(choice==='yes') analytics(); else if(analyticsLoaded) location.reload();
  }));
  document.querySelector('[data-consent-settings]')?.addEventListener('click',()=>{consent.hidden=false;consent.querySelector('button').focus();});
  const cards = [...document.querySelectorAll('#case-list .case-card')];
  let activeFilter='all';
  const search=document.querySelector('#case-search');
  const normalise = s=>s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  const filter=()=>{
    const query=normalise(search?.value||'');let count=0;
    cards.forEach(card=>{const ok=(activeFilter==='all'||card.dataset.tags.split(' ').includes(activeFilter))&&normalise(card.dataset.search).includes(query);card.hidden=!ok;if(ok)count++;});
    const counter=document.querySelector('#case-count');if(counter)counter.textContent=`${count} ${say(count>1?'missions':'mission',count>1?'assignments':'assignment')}`;
    const empty=document.querySelector('#case-list .empty');if(empty)empty.hidden=count!==0;
  };
  document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{
    activeFilter=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));filter();
  }));search?.addEventListener('input',filter);if(cards.length)filter();
  const demo=document.querySelector('#reconciliation-demo');
  if(demo){
    const datasets={
      mixed:[['Bond A',1000,1000,99.5,99.5],['Fund B',500,480,124.2,124.2],['Bond C',2000,2000,102.3,103.4]],
      clean:[['Bond A',1000,1000,99.5,99.5],['Fund B',500,500,124.2,124.2],['Bond C',2000,2000,102.3,102.3]],
      missing:[['Bond A',1000,1000,99.5,99.5],['Fund B',500,null,124.2,null],['Bond C',2000,2000,102.3,102.3]]
    };
    const draw=()=>{
      const scenario=demo.querySelector('#demo-scenario').value;
      const raw=Number(demo.querySelector('#demo-tolerance').value);
      const tolerance=Number.isFinite(raw)?Math.max(0,Math.min(10,raw)):0.5;
      const tbody=demo.querySelector('#demo-rows');tbody.replaceChildren();let exceptions=0;const reasons=[];
      datasets[scenario].forEach(([name,qbo,qc,pbo,pc])=>{
        const missing=qc===null;const qty=!missing&&qbo!==qc;
        // Relative price difference uses the custodian price as the reference.
        const price=!missing && Math.abs(pbo-pc)/Math.abs(pc)*100>tolerance+1e-12;
        const problem=missing||qty||price;if(problem)exceptions++;
        const message=missing?say('Position absente','Missing position'):qty?say('Quantité à rapprocher','Quantity exception'):price?say('Prix à vérifier','Price exception'):say('Rapproché','Matched');
        const tr=document.createElement('tr');
        [name,`${qbo} / ${qc??'—'}`,`${pbo} / ${pc??'—'}`,message].forEach((value,i)=>{const td=document.createElement('td');td.textContent=value;if(i===3)td.className=problem?'error-value':'ok-value';tr.append(td);});tbody.append(tr);
        if(problem)reasons.push(`${name} : ${missing?say('vérifier le périmètre et la date des extractions.','check extraction scope and dates.'):qty?say('vérifier les transactions en cours de règlement et les dates de valeur.','check unsettled trades and value dates.'):say('comparer la source de prix, l’heure de valorisation et la convention de prix.','compare price source, valuation time and price convention.')}`);
      });
      const output=demo.querySelector('#demo-output');output.replaceChildren();
      const p=document.createElement('p');p.textContent=say(`${exceptions} exception(s) sur trois positions. Seuil de prix : ${tolerance.toLocaleString('fr-FR')} %.`,`${exceptions} exception(s) across three positions. Price tolerance: ${tolerance}%.`);output.append(p);
      reasons.forEach(reason=>{const p=document.createElement('p');p.textContent=reason;output.append(p);});
      if(!exceptions){const p=document.createElement('p');p.textContent=say('Les quantités concordent et les prix respectent le seuil choisi. La complétude des extractions et les autres contrôles de clôture restent à valider.','Quantities agree and prices meet the selected tolerance. Extraction completeness and the remaining close controls still require review.');output.append(p);}
    };demo.querySelectorAll('select,input').forEach(x=>x.addEventListener('input',draw));draw();
  }
})();
