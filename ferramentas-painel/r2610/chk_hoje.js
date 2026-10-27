const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({executablePath: require('fs').existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined});
  for (const n of ['34','35','36','37']) {
    const p = await b.newPage({viewport:{width:1200,height:900}});
    const errs=[]; p.on('pageerror', e=>errs.push(e.message)); p.on('console', m=>{if(m.type()==='error')errs.push(m.text())});
    await p.goto('file:///home/user/IA-SINTETICO-PRODUTOR/PAINEL-NORA'+n+'.html');
    await p.waitForTimeout(500);
    const r = await p.evaluate(()=>({
      painel: !document.getElementById('painel').classList.contains('hide'),
      entrada: !document.getElementById('entrada').classList.contains('hide'),
      msg: document.getElementById('msg').textContent,
      toc: [...document.querySelectorAll('#tocLinks a')].map(a=>a.textContent),
      pre: document.querySelectorAll('#preBox .item').length,
      cenas: document.querySelectorAll('#listaCenas input[data-id]').length,
      prog: document.getElementById('progtxt').textContent,
      title: document.title
    }));
    console.log('nora'+n, JSON.stringify(r), errs.length? 'ERROS '+errs.join(' | '):'sem erros');
    await p.screenshot({path:'shot_n'+n+'.png', fullPage:false});
    await p.close();
  }
  await b.close();
})();
