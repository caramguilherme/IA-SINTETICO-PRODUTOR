// Abre cada painel no Chromium e mostra os erros da página ("nenhum" = o painel abre certo).
// Uso, na pasta do repositório: node ferramentas-painel/conferir-painel.js PAINEL-NORA47.html PAINEL-NORA48.html
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const f of process.argv.slice(2)){const pg=await b.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await pg.goto('file://'+process.cwd()+'/'+f);await pg.waitForTimeout(200);console.log(f,'ERR:',errs.join('|')||'nenhum');await pg.close();}
await b.close();})();
