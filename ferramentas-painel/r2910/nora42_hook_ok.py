# 29/10/2026 ~17h50: nora42-PRE-IMG, nora42-PRE-FIM e o clipe de 4 s aprovados. O 1º segundo do clipe ficou quase parado
# (ela só segura a fita): no CapCut o hook começa em 0,7 s e vai até o fim (~3,3 s), terminando com a fita colada.
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'
f = f'{BASE}/PAINEL-NORA42.html'
s = open(f, encoding='utf-8').read()
m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
p = json.loads(m.group(1))
g = p['pre_gancho']
g['montagem'] = ('1) nora42-PRE: corte o começo quase parado e use de 0,7 s até o fim (~3,3 s; termina com a fita colada e os dedos nas pontas).\n'
    '2) Corte seco para o corpo cortado (nora42-cortado: o Take 1 novo + as cópias dos takes 2 a 12 do nora40).\n'
    '3) A caixa do topo já entra no primeiro quadro do hook. Deixe o som do hook (a fita rasgando).')
for it in p['pecas']['lista']:
    if it['nome'] in ('nora42-PRE-IMG', 'nora42-PRE-FIM', 'nora42-PRE'):
        it['status'] = 'feito'
p['pecas']['decisao'].insert(0, 'Hook conferido (29/10 ~17h50): grafia certa (GEMINI, LIBRA, AQUARIUS / 29, 30 AND 31 OF OCTOBER), a Nora certa, uma tira só, sem voz, termina com a fita colada. O 1º segundo ficou quase parado: começa em 0,7 s.')
e = p['edicao_linha']
e[0]['texto'] = 'Hook da fita na boca (nora42-PRE, de 0,7 s ao fim, ~3,3 s)'
open(f, 'w', encoding='utf-8').write(s[:m.start(1)] + json.dumps(p, ensure_ascii=False) + s[m.end(1):])
print(g['montagem'])
