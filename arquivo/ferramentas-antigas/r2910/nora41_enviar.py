# 29/10/2026 ~12h: a placa ganha o pedido de envio ("Send it to yourself"), o sinal que falta nas placas
# (0 a 1 compartilhamento em 2,5 a 3,2 mil views). Só textos: imagem e clipe não mudam.
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'
f = f'{BASE}/PAINEL-NORA41.html'
s = open(f, encoding='utf-8').read()
m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
p = json.loads(m.group(1))
NOVO = 'If this found you, November is your most blessed month. Send it to yourself.'
p['texto_tela']['hook'] = NOVO
p['videos'][0]['fala'] = '(sem fala) texto na tela: ' + NOVO
e = p['edicao_linha'][0]
assert e['texto'].startswith('If this found you')
e['texto'] = NOVO
e['como'] = 'Texto no topo, em 3 linhas, do segundo 0 ao fim do clipe. “If this found you,” em branco; “November is your most blessed month.” em amarelo-ouro; “Send it to yourself.” em branco.'
for st in p['mapa_tela']['estilos']:
    if st['nome'].startswith('Texto do topo'):
        st['cor'] = 'branco #FFFFFF; “November is your most blessed month.” em amarelo-ouro #FFD21F'
p['roteiro']['descricao_instagram'] = ('Cancer, Scorpio, Pisces: November is your month. 🔮\n'
    'Send this to yourself. Open my story before it disappears. Comment 222 and follow me.\n#manifestation #astrology #zodiac #usa #usareels')
for k in ('insta', 'face'):
    c = p['comentario_fixado'][k]
    assert 'this one is yours. 🔥 ' in c
    p['comentario_fixado'][k] = c.replace('this one is yours. 🔥 ', 'this one is yours. 🔥 Send it to yourself to claim it. ', 1)
p['pecas']['decisao'].insert(0, 'As placas passam de 2,5 mil, mas quase ninguém compartilha (0 a 1 envio em 2,5 a 3,2 mil views): o texto do topo agora pede “Send it to yourself.”, o selo dos virais.')
open(f, 'w', encoding='utf-8').write(s[:m.start(1)] + json.dumps(p, ensure_ascii=False) + s[m.end(1):])
print('ok')
