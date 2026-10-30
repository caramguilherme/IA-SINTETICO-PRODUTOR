const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 900, height: 800 } });
  const errs = [];
  p.on('pageerror', e => errs.push(String(e)));
  await p.goto('file://' + process.argv[2]);
  await p.screenshot({ path: process.argv[3], fullPage: true });
  console.log('errors:', errs);
  await b.close();
})();
