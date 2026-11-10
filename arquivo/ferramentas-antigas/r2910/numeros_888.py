# 29/10/2026: post do @mvmcreators (Scarllet e Nadia): todo vídeo leva 888, 11:11 e 222 na tela, e a legenda pede
# para assistir até o fim e abrir o story antes que ele suma. Aplica nos painéis do nora40 ao nora43 (0 crédito).
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'
SIG = {40: 'Aries, Leo, Sagittarius', 42: 'Gemini, Libra, Aquarius', 43: 'Taurus, Virgo, Capricorn'}
TAGS = '#manifestation #astrology #zodiac #usa #usareels'
L2 = 'Then tap my photo and open my story before it disappears. Comment 222 and follow me.'
for n in (40, 41, 42, 43):
    f = f'{BASE}/PAINEL-NORA{n}.html'
    s = open(f, encoding='utf-8').read()
    m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
    p = json.loads(m.group(1))
    ok = 0
    for e in p['edicao_linha']:
        if e['texto'].replace(' ', '') in ('222e11:11',):
            e['texto'] = '222  ·  888  ·  11:11'
            e['como'] = ('Números fixos em cima, em amarelo-ouro, na mesma altura (Y 486): 222 à esquerda, 888 no meio (X 0) e 11:11 à direita'
                         + (', acima da caixa do topo.' if n != 41 else '.'))
            ok += 1
    for e in p['mapa_tela']['estilos']:
        if e['nome'].startswith('Números fixos'):
            e['nome'] = 'Números fixos (222 à esquerda, 888 no meio, 11:11 à direita)'
            e['obs'] = 'Os três do mesmo tamanho e na mesma altura (Y 486): 222 em X -274, 888 em X 0, 11:11 em X 274.' + (' Acima da caixa do topo (faixa azul do mapa).' if n != 41 else '')
            ok += 1
    p['mapa_tela']['regras'] = [r.replace('Números fixos 222 e 11:11 na faixa azul', 'Números fixos 222, 888 e 11:11 na faixa azul') for r in p['mapa_tela']['regras']]
    p['mapa_tela']['regras'] = [r.replace('os números fixos e o texto do topo', 'os números fixos (222, 888 e 11:11) e o texto do topo') for r in p['mapa_tela']['regras']]
    assert ok == 2, (n, ok)
    if n == 41:
        p['roteiro']['descricao_instagram'] = 'Cancer, Scorpio, Pisces: November is your month. 🔮\nTap my photo and open my story before it disappears. Comment 222 and follow me.\n' + TAGS
    else:
        p['roteiro']['descricao_instagram'] = f'{SIG[n]}: watch this until the end. 🔮\n{L2}\n{TAGS}'
    open(f, 'w', encoding='utf-8').write(s[:m.start(1)] + json.dumps(p, ensure_ascii=False) + s[m.end(1):])
    print('ok', n)
