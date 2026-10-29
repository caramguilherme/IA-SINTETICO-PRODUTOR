# 29/10/2026 (pedido do aluno): 222, 888 e 11:11 espalhados pelo quadro (um em cima, um no meio, um mais embaixo),
# longe do rosto, das mãos e do objeto, e em lugares diferentes em cada vídeo (como a Scarllet, a Nadia e o M1/M2).
# Lugares conferidos na nora37-IMG (imagem 267 do chat): bandeira à esquerda (x 0-33%, y 22-38%), cabelo x 17-83%,
# rosto x 32-65% / y 28-51%, geodo e mãos x 16-86% / y 49-73%, abajur x 82-100% / y 37-63%.
# Regera os painéis 40 a 43 com o PAINEL-MODELO.html atual (com mapa_tela.numeros).
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'
cc = lambda x, y: (round(x / 100 * 720 - 360), round(640 - y / 100 * 1280))
POS = {
 40: [('11:11', 13, 12, 'alto à esquerda'), ('888', 84, 30, 'no meio à direita, na parede acima do abajur'), ('222', 8, 62, 'embaixo à esquerda, ao lado da mão')],
 41: [('222', 86, 12, 'alto à direita'), ('11:11', 9, 32, 'à esquerda, na altura dos olhos'), ('888', 88, 38, 'à direita, ao lado do ombro')],
 42: [('222', 86, 12, 'alto à direita'), ('11:11', 12, 30, 'à esquerda, em cima da bandeira'), ('888', 9, 46, 'mais embaixo à esquerda, abaixo da bandeira')],
 43: [('888', 50, 11.5, 'alto, no centro'), ('222', 85, 36, 'no meio à direita, acima do abajur'), ('11:11', 7, 60, 'embaixo à esquerda, ao lado da mão')],
}
EXTRA = {
 40: 'No hook (geodo do nora37) os lugares são os mesmos: nada encosta na pedra.',
 41: 'Lugares provisórios: eu confirmo quando você me mandar a nora41-IMG. Quando ela empurra a placa (do 0 ao 5,5 s), o 888 pode encostar na borda branca da placa: tudo bem, só não pode cobrir a escrita.',
 42: 'No hook da placa, quando ela empurra a placa até a lente, o 888 pode encostar na borda branca da placa: tudo bem, só não pode cobrir a escrita (se cobrir, suba o 888 para Y 120).',
 43: 'Confira o 1º quadro do hook da pedra escura (nora34-PRE): se um número cobrir a pedra ou o rosto, suba ou desça uns 60 no Y.',
}
M = open(f'{BASE}/PAINEL-MODELO.html', encoding='utf-8').read()
assert 'mt.numeros' in M
for n, L in POS.items():
    f = f'{BASE}/PAINEL-NORA{n}.html'
    s = open(f, encoding='utf-8').read()
    p = json.loads(re.search(r'const PACOTE = (\{.*?\});\n', s, re.S).group(1))
    mt = p['mapa_tela']
    mt['numeros'] = [{'t': t, 'x': x, 'y': y, 'onde': o} for t, x, y, o in L]
    lugares = '; '.join(f'{t} {o} (X {cc(x, y)[0]} · Y {cc(x, y)[1]})' for t, x, y, o in L)
    ok = 0
    for e in p['edicao_linha']:
        if e['texto'].startswith('222  ·  888'):
            e['texto'] = '  ·  '.join(t for t, *_ in L) + '  (espalhados)'
            e['como'] = f'Números fixos em amarelo-ouro, cada um num lugar, parados do primeiro ao último quadro: {lugares}.'
            ok += 1
    for e in mt['estilos']:
        if e['nome'].startswith('Números fixos'):
            e['nome'] = 'Números fixos espalhados (' + ', '.join(t for t, *_ in L) + ')'
            e['obs'] = f'Os três do mesmo tamanho, cada um num lugar (X e Y na tabela do CapCut): {lugares}.'
            ok += 1
    assert ok == 2, (n, ok)
    regras = [r for r in mt['regras'] if not r.startswith('Números fixos 222, 888 e 11:11')]
    regras.insert(0, 'Números fixos espalhados (um em cima, um no meio, um mais embaixo), longe do rosto, das mãos e do objeto, nos lugares do desenho. ' + EXTRA[n])
    mt['regras'] = regras
    out = M.replace('<title>Painel de Produção</title>', f'<title>Painel nora{n}</title>').replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    open(f, 'w', encoding='utf-8').write(out)
    print(n, lugares)
