#!/usr/bin/env python3
"""Passo 2 do estilo "simples" (nora71 e nora72, 19/11): grava a spec do `editar_video.py` com a caixa do topo só no gancho
(branca, preto, a palavra-chave em vermelho), o 222 e o 11:11 brancos o vídeo todo, a faixa do CTA (branca, preto e vermelho)
e, no Insta, a seta embaixo à esquerda (X −300, Y −400), a partir do "tap my profile picture".
Uso: python3 -I spec_simples_1911.py <mapa-insta|face.json> <saida.mp4> <spec.json> insta|face"""
import json, sys
MAPA, SAIDA, SPEC, VER = sys.argv[1:5]
m = json.load(open(MAPA))
fim = m['dur_final']
BRANCA = {'fundo': [255, 255, 255, 255], 'texto': '#000000', 'destaque': '#E53935', 'fonte': 'bold', 'destaque_fonte': 'bold', 'raio': 14, 'sombra': None}
itens = [
    {'tipo': 'caixa', 'ini': 0, 'fim': round(m['t_gancho'] + 0.25, 3), 'x': 0, 'y': 500, 'tamanho': 11,
     'linhas': ['Most people never notice', 'these [3 signs]'], 'caixa': BRANCA},
    {'tipo': 'texto', 'ini': 0, 'fim': fim, 'x': -230, 'y': 282, 'tamanho': 13, 'texto': '222', 'cor': '#FFFFFF'},
    {'tipo': 'texto', 'ini': 0, 'fim': fim, 'x': 230, 'y': 282, 'tamanho': 13, 'texto': '11:11', 'cor': '#FFFFFF'},
    {'tipo': 'caixa', 'ini': round(m['t_tap'], 3), 'fim': fim, 'x': 0, 'y': 470, 'tamanho': 10,
     'linhas': (['Tap my photo:', 'your 2027 reading is in [my story]'] if VER == 'insta' else ['Your 2027 reading:', '[link in the comments]']),
     'caixa': BRANCA},
]
if VER == 'insta':
    itens.append({'tipo': 'seta', 'ini': round(m['t_tap'], 3), 'fim': fim, 'x': -300, 'y': -400, 'tamanho': 14})
json.dump({'entrada': m['video'], 'saida': SAIDA, 'crf': 21, 'preset': 'medium', 'estilo': 'alto-contraste', 'itens': itens},
          open(SPEC, 'w'), ensure_ascii=False, indent=1)
print('ok', SPEC)
