const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const k of ['30','31','32','33']){
const pg=await b.newPage({viewport:{width:430,height:900}});
const errs=[];pg.on('pageerror',e=>errs.push(String(e)));
await pg.goto('file:///home/user/IA-SINTETICO-PRODUTOR/PAINEL-NORA'+k+'.html');await pg.waitForTimeout(800);
const t=await pg.evaluate(()=>document.body.innerText);
console.log(k,errs,t.length,t.includes('Não gere imagem'),(t.match(/reutilizar/g)||[]).length);
}
await b.close()})();
