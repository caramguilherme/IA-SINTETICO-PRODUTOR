"""Grade do perfil do Insta (print do aluno, 04/11/2026 ~01h55; o celular do GeeLark marca 8:51 PM, hora da Califórnia): só as views."""
import csv, io
ARQ = 'METRICAS-NORA.csv'
G = {'nora44-ig': 478, 'nora43-ig': 976, 'nora42-ig': 417, 'nora41-ig': 3573, 'nora40-ig': 1415, 'nora39-ig': 137, 'nora38-ig': 2884}
raw = open(ARQ, 'rb').read().decode('utf-8-sig')
rows = list(csv.reader(io.StringIO(raw, newline='')))
ix = {c: i for i, c in enumerate(rows[0])}
feitos = set()
for r in rows[1:]:
    k = r[ix['id']]
    if k not in G: continue
    antes, velho = r[ix['views']], r[ix['print']]
    r[ix['views']] = str(G[k])
    r[ix['print']] = f'04/11 ~01h55 (só as views, da grade do perfil; o resto é da leitura de {velho})'
    r[ix['obs']] += f' | Grade do perfil 04/11 ~01h55: {G[k]:,} views (eram {int(antes):,} em {velho.split(" (")[0]}); os outros números continuam os daquela leitura.'.replace(',', '.')
    feitos.add(k)
print('faltou:', set(G) - feitos)
o = io.StringIO(newline='')
csv.writer(o, lineterminator='\r\n').writerows(rows)
open(ARQ, 'wb').write(b'\xef\xbb\xbf' + o.getvalue().encode('utf-8'))
