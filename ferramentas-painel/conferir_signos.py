# Confere se algum texto do pacote cita signos de outro vídeo (fora da lista "Depois deste vídeo", das decisões e do registro de leitura).
# Uso: python3 conferir_signos.py <pasta> 40:Aries,Leo,Sagittarius 41:Cancer,Scorpio,Pisces ...
import re, json, sys
BASE = sys.argv[1]
TODOS = ['Aries', 'Leo', 'Sagittarius', 'Cancer', 'Scorpio', 'Pisces', 'Gemini', 'Libra', 'Aquarius', 'Taurus', 'Virgo', 'Capricorn']
def walk(o, path=''):
    if isinstance(o, dict):
        for k, v in o.items(): yield from walk(v, path + '.' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from walk(v, f'{path}[{i}]')
    elif isinstance(o, str): yield path, o
erros = 0
for arg in sys.argv[2:]:
    n, sig = arg.split(':'); sig = [x.lower() for x in sig.split(',')]
    s = open(f'{BASE}/PAINEL-NORA{n}.html', encoding='utf-8').read()
    p = json.loads(re.search(r'const PACOTE = (\{.*?\});\n', s, re.S).group(1))
    for path, txt in walk(p):
        if 'leitura_registro' in path or 'decisao' in path or 'proximos' in path: continue
        outros = [w for w in TODOS if w.lower() not in sig and re.search(r'\b' + w + r'\b', txt, re.I)]
        if outros:
            erros += 1; print(n, path, outros, '|', txt[:140].replace('\n', ' '))
print('erros:', erros)
