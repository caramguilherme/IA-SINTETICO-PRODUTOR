"""Recordes da Nora tirados do METRICAS-NORA.csv inteiro (regra de 18/11 01h14:
comparar com o histórico, nunca só com o print). Rodar antes de escrever
"o maior", "o melhor", "o 1º" ou "nunca":  python3 -I ferramentas-painel/recordes.py"""
import csv, os, re
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'METRICAS-NORA.csv')
rows = list(csv.DictReader(open(base, encoding='utf-8-sig')))
def num(x):
    try: return float(str(x).replace(',', '.'))
    except ValueError: return None
def top(rede, campo, n=10, filtro=None):
    rs = [r for r in rows if r['rede'] == rede and num(r[campo]) is not None and (filtro is None or filtro(r))]
    rs.sort(key=lambda r: -num(r[campo]))
    return rs[:n]
def linha(r, extra=''):
    return f"  {r['id']:<18} {r['views']:>6} views | follows {r['follows'] or '-':>3} | tempo {r['tempo'] or '-':>3} s | 3 s {r['ret3s'] or '-':>5}% | {r['pais1'][:22]} | {r['postado']}{extra} | {r['video'][:60]}"
def dist(r):
    d = re.findall(r'distribui[çc][ãa]o ([+−-]?\d+(?:,\d+)?)x', r['nota_face'])
    return num(d[-1].replace('−', '-')) if d else None
for rede in ('Instagram', 'Facebook'):
    print(f'== {rede}: as 10 maiores em views')
    for r in top(rede, 'views'): print(linha(r))
    print(f'== {rede}: as 5 maiores em follows')
    for r in top(rede, 'follows', 5): print(linha(r))
    print(f'== {rede}: os 5 maiores tempos médios (com 100+ views)')
    for r in top(rede, 'tempo', 5, lambda r: (num(r['views']) or 0) >= 100): print(linha(r))
print('== Facebook: as 8 maiores distribuições (a última leitura de cada vídeo)')
fb = [(dist(r), r) for r in rows if r['rede'] == 'Facebook' and dist(r) is not None]
for d, r in sorted(fb, key=lambda x: -x[0])[:8]: print(linha(r, f' | dist {d:+.1f}x'))
