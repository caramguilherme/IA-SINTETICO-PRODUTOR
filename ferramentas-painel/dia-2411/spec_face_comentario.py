#!/usr/bin/env python3
"""Passo 2 da versão do Face do nora77 e do nora78 (24/11): a fala termina mandando para o 1º comentário ("Check the first comment
below to get your reading."), então a seta para a foto do perfil sai (não é para lá que ela manda) e entra a faixa do comentário,
igual à do nora71-FACE ao nora73-FACE e do ini1811-FACE ("Your 2027 reading:" / "[link in the comments]", branca com preto e o
destaque em vermelho), do "Check the first comment" até o fim.
Uso: python3 -I spec_face_comentario.py <mapa.json> <saida.mp4> <spec.json> [y]"""
import json, sys
MAPA, SAIDA, SPEC = sys.argv[1:4]
Y = int(sys.argv[4]) if len(sys.argv) > 4 else 470
m = json.load(open(MAPA))
cx = {"fundo": [255, 255, 255, 255], "texto": "#000000", "destaque": "#E53935", "fonte": "bold", "destaque_fonte": "bold", "raio": 14, "sombra": None}
itens = [{'tipo': 'caixa', 'ini': round(m['t_tap'], 3), 'fim': m['dur_final'], 'x': 0, 'y': Y, 'tamanho': 10,
          'linhas': ['Your 2027 reading:', '[link in the comments]'], 'caixa': cx}]
json.dump({'entrada': m['video'], 'saida': SAIDA, 'crf': 21, 'preset': 'veryfast', 'estilo': 'alto-contraste', 'itens': itens},
          open(SPEC, 'w'), ensure_ascii=False, indent=1)
print('ok', SPEC, 'faixa do comentário de', itens[0]['ini'], 'a', m['dur_final'])
