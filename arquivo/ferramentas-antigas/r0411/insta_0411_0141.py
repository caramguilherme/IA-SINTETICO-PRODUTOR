"""Leituras do Insta de 04/11/2026 (face02 01h41, nora46 01h43), prints do aluno."""
import csv, io
ARQ = 'METRICAS-NORA.csv'
D = {
 'face02-ig': dict(views=151, viewers=118, likes=1, comentarios=1, salvos=0, compart=0, reposts=0, follows=0, skip=78.0, tempo=3,
   paises=['United States 33.6%', 'India 30%', 'Canada 8.6%', 'United Kingdom 3.6%', 'Malaysia 2.9%'],
   print='04/11 01h41 (~28h30 de vida)',
   nota='Leitura 04/11 01h41 (~28h30): 151 views, 118 viewers, skip 78,0% (22,0% nos 3 s), tempo médio 3 s num vídeo de 5 s (a curva cai para ~35% aos 2,5 s e ~15% aos 5 s), 0 follows, 2 visitas ao perfil, 1 curtida (no meio, ~3 s), 1 comentário, 0 envios, 0 salvos, 0 reposts; 95,7% não seguidores; idade 18-24 7,9%, 25-34 37,9%, 35-44 35,7%, 45-54 10,7%, 55-64 2,9%, 65+ 5% (45+ = 18,6%, o público mais novo da Nora); países EUA 33,6%, Índia 30%, Canadá 8,6%, Reino Unido 3,6%, Malásia 2,9%. Views no tempo: parado em ~150 desde as primeiras horas de 03/11; o reel típico está em ~750. Contra o face01-ig (clipe, mesmo texto) com ~24h30: 532 views, 46% nos 3 s, 9 s de média, 1 follow; o clipe ganhou de longe no Insta (a imagem parada perdeu views, começo e tempo), mas o face02 saiu às 21h13 e teve o melhor % de EUA (33,6% x 13%).'),
 'nora46-ig': dict(views=131, viewers=121, likes=0, comentarios=5, salvos=0, compart=1, reposts=0, follows=0, skip=45.5, tempo=11,
   paises=['United States 20.8%', 'India 15.4%', 'United Kingdom 9.2%', 'Canada 9.2%', 'Germany 6.2%'],
   print='04/11 01h43 (~79 h de vida)',
   nota='Leitura 04/11 01h43 (~79 h): 131 views (126 com ~17h30: parado), 121 viewers, skip 45,5% (54,5% nos 3 s), tempo médio 11 s em 1:28 (a curva cai para ~20% até os ~8 s, no hook + Take 1, e vai a ~5% no fim), 0 follows, 0 visitas ao perfil, 0 curtidas, 5 comentários (taxa do Insta 4,1%; 2 pessoas + as respostas do aluno + o fixado), 1 envio, 0 salvos; 93,8% não seguidores; idade 25-34 15,4%, 35-44 23,1%, 45-54 34,6%, 55-64 17,7%, 65+ 9,2% (45+ = 61,5%); EUA 20,8%, Índia 15,4%, Reino Unido 9,2%, Canadá 9,2%, Alemanha 6,2%. Sem 2ª onda (o reel típico chega a ~1 mil). Base do nora47 no Insta: mesmo corpo, gancho novo.'),
}
raw = open(ARQ, 'rb').read().decode('utf-8-sig')
rows = list(csv.reader(io.StringIO(raw, newline='')))
ix = {c: i for i, c in enumerate(rows[0])}
feitos = set()
for r in rows[1:]:
    k = r[ix['id']]
    if k not in D: continue
    d = D[k]
    for c in ('views', 'viewers', 'likes', 'comentarios', 'salvos', 'compart', 'reposts', 'follows', 'tempo'):
        r[ix[c]] = str(d[c])
    r[ix['skip']] = str(d['skip']); r[ix['ret3s']] = str(round(100 - d['skip'], 1))
    for n, p in enumerate(d['paises'], 1):
        r[ix[f'pais{n}']] = p
    r[ix['print']] = d['print']
    r[ix['obs']] = r[ix['obs']] + ' | ' + d['nota']
    feitos.add(k)
print('faltou:', set(D) - feitos)
o = io.StringIO(newline='')
csv.writer(o, lineterminator='\r\n').writerows(rows)
open(ARQ, 'wb').write(b'\xef\xbb\xbf' + o.getvalue().encode('utf-8'))
