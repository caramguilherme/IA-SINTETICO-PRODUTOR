"""Grade do perfil do Insta (print do aluno, 04/11/2026 ~12h30): só as views. Perfil: 49 posts, 107 seguidores, 32 mil views em 30 dias."""
import csv, io
ARQ = 'METRICAS-NORA.csv'
G = {'nora47-ig': 286, 'face02-ig': 151, 'nora46-ig': 134, 'face01-ig': 546, 'nora45-ig': 3692, 'nora44-ig': 478,
     'nora43-ig': 979, 'nora42-ig': 418, 'nora41-ig': 3574, 'nora40-ig': 1415, 'nora39-ig': 137, 'nora38-ig': 2885,
     'nora37-ig': 693, 'nora36-ig': 3308, 'nora35-ig': 2805, 'nora34-ig': 135, 'nora33-ig': 206, 'nora32-ig': 120}
raw = open(ARQ, 'rb').read().decode('utf-8-sig')
rows = list(csv.reader(io.StringIO(raw, newline='')))
ix = {c: i for i, c in enumerate(rows[0])}
mud = []
for r in rows[1:]:
    k = r[ix['id']]
    if k not in G: continue
    antes = r[ix['views']]
    if antes and int(antes) == G[k]:
        continue
    velho = r[ix['print']].split(' (')[0] if r[ix['print']] else ''
    r[ix['views']] = str(G[k])
    if k == 'nora47-ig':
        r[ix['print']] = '04/11 ~12h30 (só as views, da grade do perfil; ~11 h de vida)'
        r[ix['obs']] += ' | Grade do perfil 04/11 ~12h30 (~11 h): 286 views (o nora46 parou em 131 a 134): passou da régua de ~130 com 12 h. Faltam o Insights (3 s, curva, Audience).'
    else:
        base = velho if velho and 'grade' not in r[ix['print']] else r[ix['print']].split('o resto é da leitura de ')[-1].rstrip(')')
        r[ix['print']] = f'04/11 ~12h30 (só as views, da grade do perfil; o resto é da leitura de {base})'
        r[ix['obs']] += f' | Grade do perfil 04/11 ~12h30: {G[k]:,} views (eram {int(antes):,}).'.replace(',', '.')
    mud.append((k, antes, G[k]))
for m in mud: print(m)
o = io.StringIO(newline='')
csv.writer(o, lineterminator='\r\n').writerows(rows)
open(ARQ, 'wb').write(b'\xef\xbb\xbf' + o.getvalue().encode('utf-8'))
