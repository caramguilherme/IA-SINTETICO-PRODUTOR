// Abre os painéis no Chromium e diz se o pacote carregou (o conferir-painel.js não pega o erro de validação do PAINEL-MODELO).
// Uso (raiz do repositório): node ferramentas-painel/abrir-painel.js 85 86   ->   'falha: false' e 'tela de colar: false' = o painel abriu.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const n of process.argv.slice(2)) {
    const p = await b.newPage({ viewport: { width: 900, height: 1400 } });
    const erros = [];
    p.on('pageerror', e => erros.push(String(e)));
    await p.goto('file:///workspace/IA-SINTETICO-PRODUTOR/PAINEL-NORA' + n + '.html');
    await p.waitForTimeout(1200);
    const txt = await p.evaluate(() => document.body.innerText);
    const falha = /Não consegui ler/.test(txt);
    const cola = /COLE O PACOTE/.test(txt) && txt.indexOf('COLE O PACOTE') < 200;
    console.log(n, 'falha:', falha, '| tela de colar:', cola, '| erros JS:', erros.length, '| tamanho do texto:', txt.length, '| imagens:', (txt.match(/leitura-IMG-[A-G]/g) || []).length);
    if (n === '86') await p.screenshot({ path: "/tmp/painel-" + n + ".png", fullPage: false });
  }
  await b.close();
})();
