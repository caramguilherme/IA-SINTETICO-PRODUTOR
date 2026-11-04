"""Leitura do Face (Biblioteca) de 04/11/2026 01h38, print do aluno."""
import csv, io, datetime as dt
ARQ = 'METRICAS-NORA.csv'
LEIT = dt.datetime(2026, 11, 4, 1, 38)
# id: (views, viewers, engaj, seguidores, impressoes, coment, distrib, tempo_total, media_s, v3s, v1min, postado_face)
D = {
 'nora47-fb':    (0, 0, 1, 0, 0, 1, '—', '0 s', 0, 0, 0, '04/11 01h37'),
 'face02-fb':    (320, 226, 7, 0, 241, 3, '+0,8x', '12min 30s', 3, 46, 0, '02/11 21h11'),
 'nora46-fb':    (61, 48, 12, 1, 48, 7, '+0,3x', '7min 47s', 8, 28, 2, '31/10 18h27'),
 'face01-fb':    (246, 199, 3, 0, 218, 1, '+0,0x', '9min 48s', 3, 39, 0, '31/10 11h07'),
 'nora45-fb':    (265, 203, 2, 0, 210, 1, '+0,0x', '14min 43s', 4, 79, 0, '30/10 21h36'),
 'nora44-fb':    (241, 233, 5, 1, 239, 1, '−1,4x', '21min 44s', 6, 116, 3, '30/10 19h05'),
 'nora43-fb':    (265, 246, 2, 0, 263, 1, '+0,6x', '27min 56s', 7, 113, 6, '30/10 01h14'),
 'nora42-fb':    (96, 85, 1, 0, 89, 1, '−1,5x', '7min 27s', 5, 26, 2, '29/10 22h38'),
 'nora41-fb':    (291, 219, 2, 0, 228, 1, '+0,0x', '17min 48s', 5, 92, 0, '29/10 19h49'),
 'nora40-fb':    (251, 238, 1, 0, 250, 1, '+1,1x', '55min 45s', 14, 83, 6, '29/10 17h18'),
 'nora39var-fb': (252, 234, 11, 0, 241, 5, '+1,3x', '21min 58s', 6, 104, 0, '29/10 16h26'),
 'nora39-fb':    (242, 207, 8, 2, 211, 3, '+1,1x', '31min 17s', 9, 120, 0, '28/10 22h45'),
}
def vida(postado):
    d, h = postado.split()
    dia, mes = map(int, d.split('/'))
    hh, mm = map(int, h.replace('h', ':').split(':'))
    t = (LEIT - dt.datetime(2026, mes, dia, hh, mm)).total_seconds() / 3600
    if t < 1: return f'~{round(t*60)} min'
    if t < 48: return f'~{int(t)}h{int(round((t-int(t))*60)):02d}'
    return f'~{round(t)} h'
raw = open(ARQ, 'rb').read().decode('utf-8-sig')
rows = list(csv.reader(io.StringIO(raw, newline='')))
cab = rows[0]; ix = {c: i for i, c in enumerate(cab)}
feitos = set()
for r in rows[1:]:
    k = r[ix['id']]
    if k not in D: continue
    v, vw, eng, seg, imp, com, dist, tt, med, v3, v1, post = D[k]
    vd = vida(post)
    ret = round(100 * v3 / v, 1) if v else ''
    r[ix['views']] = str(v); r[ix['viewers']] = str(vw); r[ix['comentarios']] = str(com); r[ix['follows']] = str(seg)
    r[ix['ret3s']] = str(ret) if ret != '' else ''; r[ix['skip']] = str(round(100 - ret, 1)) if ret != '' else ''
    r[ix['tempo']] = str(med)
    r[ix['print']] = f'04/11 01h38 (Biblioteca do Face, {vd} de vida)'
    if k == 'nora47-fb':
        r[ix['postado']] = '04/11 01h37'
    pct = f' ({str(ret).replace(".", ",")}%)' if ret != '' else ''
    nota = (f'Leitura 04/11 01h38 ({vd}): {v} views, {vw} visualizadores, {imp} impressões, engajamento {eng}, '
            f'comentários {com}, {seg} seguidor(es) novo(s), distribuição {dist}, tempo total {tt}, tempo médio {med} s, '
            f'{v3} views de 3 s{pct}, {v1} de 1 min.')
    if k == 'nora47-fb':
        nota += ' (3 min de vida: o único comentário é o da Página.)'
    r[ix['nota_face']] = (r[ix['nota_face']] + ' | ' + nota) if r[ix['nota_face']] else nota
    feitos.add(k)
print('faltou:', set(D) - feitos)
o = io.StringIO(newline='')
csv.writer(o, lineterminator='\r\n').writerows(rows)
open(ARQ, 'wb').write(b'\xef\xbb\xbf' + o.getvalue().encode('utf-8'))
