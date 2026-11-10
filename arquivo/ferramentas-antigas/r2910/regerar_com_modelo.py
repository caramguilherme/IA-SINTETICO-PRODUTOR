# Regera os painéis indicados com o PAINEL-MODELO.html atual, mantendo o pacote de cada um (sem mudar nada nele).
import re, sys
BASE, NUMS = sys.argv[1], [int(x) for x in sys.argv[2:]]
M = open(f'{BASE}/PAINEL-MODELO.html', encoding='utf-8').read()
for n in NUMS:
    f = f'{BASE}/PAINEL-NORA{n}.html'
    js = re.search(r'const PACOTE = (\{.*?\});\n', open(f, encoding='utf-8').read(), re.S).group(1)
    out = M.replace('<title>Painel de Produção</title>', f'<title>Painel nora{n}</title>').replace('const PACOTE = null;', 'const PACOTE = ' + js + ';')
    open(f, 'w', encoding='utf-8').write(out)
    print('ok', n)
