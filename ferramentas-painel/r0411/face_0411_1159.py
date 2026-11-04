"""Leitura do Face (Biblioteca) de 04/11/2026 11h59: só o nora47 mudou (os outros iguais aos de 01h38)."""
import csv, io
ARQ = 'METRICAS-NORA.csv'
nota = ('Leitura 04/11 11h59 (~10h22): 103 views, 95 visualizadores, 99 impressões, engajamento 3, comentários 1, 0 seguidor(es) novo(s), '
        'distribuição −2,9x (a pior da Página), tempo total 7min 55s, tempo médio 5 s, 39 views de 3 s (37,9%), 1 de 1 min. '
        'Contra o nora46 (mesmo corpo): 45 views com ~6h45 (−1,5x, 51% nos 3 s, 8 s) e 61 no fim: o gancho do tsunami trouxe mais views que o nora46 inteiro, '
        'mas segurou menos o começo (38% x 46% a 51%) e o tempo médio caiu (5 s x 8 s); ainda longe dos ~240 do dia 1 dos outros. '
        'Atenção: postado às 01h37 (20h37 na Califórnia, 23h37 em Nova York), mais tarde que os outros do Face (17h a 22h40): o horário também pode ter pesado.')
raw = open(ARQ, 'rb').read().decode('utf-8-sig')
rows = list(csv.reader(io.StringIO(raw, newline='')))
ix = {c: i for i, c in enumerate(rows[0])}
n = 0
for r in rows[1:]:
    if r[ix['id']] != 'nora47-fb': continue
    for c, v in dict(views=103, viewers=95, comentarios=1, follows=0, skip=62.1, ret3s=37.9, tempo=5).items():
        r[ix[c]] = str(v)
    r[ix['print']] = '04/11 11h59 (Biblioteca do Face, ~10h22 de vida)'
    r[ix['nota_face']] = (r[ix['nota_face']] + ' | ' + nota) if r[ix['nota_face']] else nota
    n += 1
assert n == 1
o = io.StringIO(newline='')
csv.writer(o, lineterminator='\r\n').writerows(rows)
open(ARQ, 'wb').write(b'\xef\xbb\xbf' + o.getvalue().encode('utf-8'))
print('ok')
