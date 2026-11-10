"""Leitura do Insta de 04/11/2026 01h51: nora45 (a fita Touro/Virgem/Capricórnio)."""
import csv, io
ARQ = 'METRICAS-NORA.csv'
nota = ('Leitura 04/11 01h51 (~100 h): 3.690 views (3.576 com ~38h30: parado em ~3,6 mil desde 02/11), 2.083 viewers, skip 40,7% (59,3% nos 3 s), tempo médio 9 s num clipe de 8 s (a curva fica em ~45% até os 7 s), '
        '12 follows, 11 visitas ao perfil, 73 curtidas (pico no fim, aos 8 s), 30 comentários, 23 envios, 8 salvos, 2 reposts; 99,1% não seguidores; '
        'idade 13-17 0,1%, 18-24 0,3%, 25-34 3,8%, 35-44 12,6%, 45-54 26,5%, 55-64 29,3%, 65+ 27,4% (45+ = 83,2%); Índia 20,5%, EUA 16,7%, Reino Unido 6,7%, Canadá 3,8%, Grécia 3,5%.')
raw = open(ARQ, 'rb').read().decode('utf-8-sig')
rows = list(csv.reader(io.StringIO(raw, newline='')))
ix = {c: i for i, c in enumerate(rows[0])}
n = 0
for r in rows[1:]:
    if r[ix['id']] != 'nora45-ig': continue
    for c, v in dict(views=3690, viewers=2083, likes=73, comentarios=30, salvos=8, compart=23, reposts=2, follows=12, skip=40.7, ret3s=59.3, tempo=9).items():
        r[ix[c]] = str(v)
    for k, p in enumerate(['India 20.5%', 'United States 16.7%', 'United Kingdom 6.7%', 'Canada 3.8%', 'Greece 3.5%'], 1):
        r[ix[f'pais{k}']] = p
    r[ix['print']] = '04/11 01h51 (~100 h de vida)'
    r[ix['obs']] += ' | ' + nota
    n += 1
assert n == 1
o = io.StringIO(newline='')
csv.writer(o, lineterminator='\r\n').writerows(rows)
open(ARQ, 'wb').write(b'\xef\xbb\xbf' + o.getvalue().encode('utf-8'))
print('ok')
