"""Leitura do Insta de 04/11/2026 01h47: o aluno mandou como "nora45", mas o print é do face01 (texto READ THIS BEFORE YOU SCROLL, clipe de 8 s do carro)."""
import csv, io
ARQ = 'METRICAS-NORA.csv'
nota = ('Leitura 04/11 01h47 (~86 h; o aluno mandou o print com o nome "nora45 insta", mas é o face01: o texto "READ THIS BEFORE YOU SCROLL", o clipe de 8 s do carro e os números batem): '
        '545 views (532 com ~24h30: parado), 328 viewers, skip 53,7% (46,3% nos 3 s), tempo médio 10 s num clipe de 8 s (a curva fica em ~35% até os 7 s), 1 follow, 1 visita ao perfil, '
        '10 curtidas (pico no fim, aos 8 s), 8 comentários, 1 envio, 2 salvos, 0 reposts; 98,1% não seguidores; idade 18-24 1,5%, 25-34 21,9%, 35-44 28,4%, 45-54 18,1%, 55-64 13,3%, 65+ 16,8% (45+ = 48,2%); '
        'Índia 52,9%, EUA 13,8%, Reino Unido 5,8%, Austrália 2,8%, Canadá 1,9%. Contra o face02-ig (imagem parada, mesmo texto, 04/11 01h41): 151 views, 22% nos 3 s, 3 s de média.')
raw = open(ARQ, 'rb').read().decode('utf-8-sig')
rows = list(csv.reader(io.StringIO(raw, newline='')))
ix = {c: i for i, c in enumerate(rows[0])}
n = 0
for r in rows[1:]:
    if r[ix['id']] != 'face01-ig': continue
    for c, v in dict(views=545, viewers=328, likes=10, comentarios=8, salvos=2, compart=1, reposts=0, follows=1, skip=53.7, ret3s=46.3, tempo=10).items():
        r[ix[c]] = str(v)
    for k, p in enumerate(['India 52.9%', 'United States 13.8%', 'United Kingdom 5.8%', 'Australia 2.8%', 'Canada 1.9%'], 1):
        r[ix[f'pais{k}']] = p
    r[ix['print']] = '04/11 01h47 (~86 h de vida)'
    r[ix['obs']] += ' | ' + nota
    n += 1
assert n == 1
o = io.StringIO(newline='')
csv.writer(o, lineterminator='\r\n').writerows(rows)
open(ARQ, 'wb').write(b'\xef\xbb\xbf' + o.getvalue().encode('utf-8'))
print('ok')
