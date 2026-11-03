// Confere a planilha contra a página do dashboard (as mesmas contas que o dashboard faz).
// Uso: node conferir-dados.js ferramentas-painel/dashboard/index.html <pasta>/rows.json
// (o rows.json sai do preparar_csv.py). Mostra: total de vídeos, ids repetidos ou vazios e os 12 últimos de cada rede.
const fs = require('fs');
const [,, htmlPath, rowsPath] = process.argv;
const html = fs.readFileSync(htmlPath, 'utf8');
const rows = JSON.parse(fs.readFileSync(rowsPath, 'utf8'));
const calcs = {};
const dash = { calc: (id, o) => { calcs[id] = o; } };
const s1 = html.split('<script>')[1].split('</script>')[0];
new Function('dash', s1)(dash);
const videos = calcs.videos.fn(rows);
const resumo = calcs.resumo.fn(videos);
const ids = new Set(); let dup = 0; videos.forEach(v => { if (ids.has(v.id)) dup++; ids.add(v.id); });
console.log('videos', videos.length, 'ids duplicados', dup, 'sem id', videos.filter(v => !v.id).length);
for (const rede of ['Instagram', 'Facebook']) {
  const r = videos.filter(v => v.rede === rede && v.ordem >= 25).sort((a, b) => a.ordem - b.ordem);
  console.log('\n' + rede + ' (nora25+):');
  r.slice(-12).forEach(v => console.log(v.id.padEnd(16), 'views', String(v.views).padStart(5), 'ret3s', String(v.ret3s).padStart(5), 'tempo', String(v.tempo).padStart(4), 'india', String(v.india).padStart(5), 'pais1', v.pais1, '| lido', v.lido));
  console.log('resumo', JSON.stringify(resumo.find(x => x.rede === rede)));
}
