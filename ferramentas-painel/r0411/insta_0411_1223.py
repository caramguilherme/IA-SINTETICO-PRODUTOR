"""Leitura do Insta do nora47 em 04/11/2026 12h23 (~10h48 de vida), prints do aluno."""
import csv, io
ARQ = 'METRICAS-NORA.csv'
nota = ('Leitura 04/11 12h23 (~10h48): 287 views, 255 viewers, skip 41,2% (58,8% nos 3 s), tempo médio 12 s em 1:33; '
        'curva: ~65% aos ~3 s, ~40% aos ~8 s (fim do tsunami), ~22% aos ~12 s (corte do bunker para o estúdio, Take 1), ~15% aos ~20 s, ~2% no fim; '
        'views no tempo coladas no reel típico (~280 com ~10 h); 0 follows, 0 visitas ao perfil, 5 curtidas (picos nos primeiros ~10 s), 1 comentário, 0 envios, 2 salvos, 0 reposts; '
        '96,5% não seguidores; idade 18-24 2,2%, 25-34 16,2%, 35-44 26,4%, 45-54 32,9%, 55-64 15,2%, 65+ 7,2% (45+ = 55,3%); '
        'Índia 38,6% (postado 01h35 = 10h05 na Índia), EUA 26,4% (~76 pessoas; nora46 ~28), Canadá 6,5%, Turquia 3,2%, Austrália 3,2%. '
        'Contra o nora46 (mesmo corpo): 2,1x as views, 3 s 58,8% x 54,5%, curva aos 8 s ~40% x ~20%, tempo 12 s x 11 s; mas 0 visita ao perfil nos dois.')
raw = open(ARQ, 'rb').read().decode('utf-8-sig')
rows = list(csv.reader(io.StringIO(raw, newline='')))
ix = {c: i for i, c in enumerate(rows[0])}
n = 0
for r in rows[1:]:
    if r[ix['id']] != 'nora47-ig': continue
    for c, v in dict(views=287, viewers=255, likes=5, comentarios=1, salvos=2, compart=0, reposts=0, follows=0, skip=41.2, ret3s=58.8, tempo=12).items():
        r[ix[c]] = str(v)
    for k, p in enumerate(['India 38.6%', 'United States 26.4%', 'Canada 6.5%', 'Turkey 3.2%', 'Australia 3.2%'], 1):
        r[ix[f'pais{k}']] = p
    r[ix['print']] = '04/11 12h23 (~10h48 de vida)'
    r[ix['obs']] += ' | ' + nota
    n += 1
assert n == 1
o = io.StringIO(newline='')
csv.writer(o, lineterminator='\r\n').writerows(rows)
open(ARQ, 'wb').write(b'\xef\xbb\xbf' + o.getvalue().encode('utf-8'))
print('ok')
