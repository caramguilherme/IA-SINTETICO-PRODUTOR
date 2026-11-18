# Tier 1 e Índia por horário de postagem no Insta (janelas de 30 min, das 16h às 03h de Brasília), da planilha inteira.
# Pedido do aluno em 18/11/2026 ~16h25. Tier 1 = EUA, Canadá, Reino Unido, Austrália, Nova Zelândia e Irlanda, somados entre os 5 países anotados
# (é um piso: o que está fora do top 5 não entra). Índia fora do top 5 conta como 0 (na verdade fica abaixo do 5º país, ~2% a 6%).
# Sem fala = placas, fitas, loop e texto na tela. Uso (raiz do repositório): python3 -I ferramentas-painel/horarios_pais.py
import csv, re, pathlib
R = pathlib.Path(__file__).resolve().parents[1]
T1 = {'United States', 'Canada', 'United Kingdom', 'Australia', 'New Zealand', 'Ireland'}
SEMFALA = {'22', '31', '33', '35', '36', '38', '41', '45', '64', '45.1', '46.1'}
xs = []
for r in csv.DictReader(open(R / 'METRICAS-NORA.csv', encoding='utf-8-sig')):
    if r['rede'] != 'Instagram':
        continue
    ps = [r[f'pais{i}'] for i in range(1, 6) if r.get(f'pais{i}')]
    m = re.search(r'(\d{1,2})h(\d{2})?', r['postado'])
    if not ps or not m:
        continue
    t1 = ind = 0.0
    for p in ps:
        mm = re.match(r'(.+?)\s+([\d.,]+)%', p.strip())
        if mm:
            c, v = mm.group(1).strip(), float(mm.group(2).replace(',', '.'))
            t1 += v if c in T1 else 0
            ind = v if c == 'India' else ind
    h, mi = int(m.group(1)), int(m.group(2) or 0)
    xs.append(dict(o=r['ordem'], v=r['video'][:40], post=r['postado'], m=h * 60 + mi + (1440 if h < 16 else 0), t1=t1, ind=ind, views=int(r['views'] or 0), sem=r['ordem'] in SEMFALA))
for a in range(16 * 60, 27 * 60, 30):
    g = [x for x in xs if a <= x['m'] < a + 30]
    lab = f'{(a // 60) % 24:02d}h{a % 60:02d}-{((a + 30) // 60) % 24:02d}h{(a + 30) % 60:02d}'
    if not g:
        print(f'{lab}: nenhum vídeo'); continue
    n = len(g)
    print(f"{lab}: {n} vídeo(s) · Tier 1 {sum(x['t1'] for x in g) / n:.1f}% · Índia {sum(x['ind'] for x in g) / n:.1f}%")
    for x in g:
        print(f"    {x['post']:<13} {x['views']:>5} views · Tier 1 {x['t1']:.1f}% · Índia {x['ind']:.1f}%{' · sem fala' if x['sem'] else ''} · {x['v']}")
