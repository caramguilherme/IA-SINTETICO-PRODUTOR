# 29/10/2026 (pedido do aluno): 222, 888 e 11:11 cada um de uma cor e de um tamanho, variando de vídeo para vídeo
# (um grande, um médio, um pequeno), para chamar a atenção. Lugares de numeros_espalhados.py; conferido em
# conferencia-cores-geodo.png (nora40, nora42, nora43 em cima da nora37-IMG). Regera os painéis com o modelo atual.
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'
cc = lambda x, y: (round(x / 100 * 720 - 360), round(640 - y / 100 * 1280))
C = {'branco': '#FFFFFF', 'ciano': '#3DE0FF', 'amarelo-ouro': '#FFD21F', 'rosa-choque': '#FF4FD8',
     'vermelho': '#FF3B30', 'verde-limão': '#7CFF4F', 'laranja': '#FF9F1C'}
COR = {  # número: (cor, tamanho no CapCut)
 40: {'11:11': ('branco', 16), '888': ('ciano', 12), '222': ('amarelo-ouro', 11)},
 41: {'222': ('rosa-choque', 15), '11:11': ('amarelo-ouro', 11), '888': ('branco', 12)},
 42: {'222': ('vermelho', 12), '11:11': ('verde-limão', 13), '888': ('laranja', 15)},
 43: {'888': ('rosa-choque', 14), '222': ('verde-limão', 12), '11:11': ('ciano', 11)},
}
M = open(f'{BASE}/PAINEL-MODELO.html', encoding='utf-8').read()
assert 'u.cor_nome' in M
for n, D in COR.items():
    f = f'{BASE}/PAINEL-NORA{n}.html'
    p = json.loads(re.search(r'const PACOTE = (\{.*?\});\n', open(f, encoding='utf-8').read(), re.S).group(1))
    mt = p['mapa_tela']
    for u in mt['numeros']:
        nome, tam = D[u['t']]
        u['cor_nome'], u['cor'], u['tamanho'] = nome, C[nome], tam
    desc = '; '.join(f"{u['t']} {u['cor_nome']} {u['cor']}, tamanho {u['tamanho']}, {u['onde']} (X {cc(u['x'], u['y'])[0]} · Y {cc(u['x'], u['y'])[1]})" for u in mt['numeros'])
    ok = 0
    for e in p['edicao_linha']:
        if e['texto'].endswith('(espalhados)'):
            e['como'] = f'Cada número de uma cor e de um tamanho, num lugar, parados do primeiro ao último quadro: {desc}.'
            ok += 1
    for e in mt['estilos']:
        if e['nome'].startswith('Números fixos espalhados'):
            e['cor'] = 'uma cor para cada número (abaixo)'
            e['tamanho'] = 'um tamanho para cada número (abaixo)'
            e['obs'] = desc + '.'
            ok += 1
    assert ok == 2, (n, ok)
    out = M.replace('<title>Painel de Produção</title>', f'<title>Painel nora{n}</title>').replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    open(f, 'w', encoding='utf-8').write(out)
    print(n, desc)
