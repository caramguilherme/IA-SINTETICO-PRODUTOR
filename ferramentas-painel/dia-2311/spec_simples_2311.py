#!/usr/bin/env python3
"""Passo 2 do nora75 e do nora76 (23/11), a cópia do m30 e do m61: sem caixa do topo, sem faixa e sem o 222; o "11:11✨" já entra
no passo 1 (editar_simples_2311.py). Aqui só a seta vermelha embaixo à esquerda (X −300, Y −400, tamanho 14), do "tap my profile
picture" até o fim, nas duas versões (a fala do CTA manda para a foto do perfil e o story, no Insta e no Face).
Desde 24/11 11h33 (o aluno: "pode fazer a seta grande sim"; aula 26, 0:39:29; Clone R88), a seta é grande: tamanho 44
(era 14), X −285 no Insta e X −250 no Face (a borda esquerda em 8% da largura, P43), Y −400.
Uso: python3 -I spec_simples_2311.py <mapa-insta.json> <saida.mp4> <spec.json> [insta|face]"""
import json, sys
MAPA, SAIDA, SPEC = sys.argv[1:4]
REDE = sys.argv[4] if len(sys.argv) > 4 else 'insta'
m = json.load(open(MAPA))
fim = m['dur_final']
itens = [{'tipo': 'seta', 'ini': round(m['t_tap'], 3), 'fim': fim, 'x': -250 if REDE == 'face' else -285, 'y': -400, 'tamanho': 44}]
# preset veryfast: o vídeo tem ~1:40 e o post é às 19h30 (o medium leva ~12 min nesse tamanho)
json.dump({'entrada': m['video'], 'saida': SAIDA, 'crf': 21, 'preset': 'veryfast', 'estilo': 'alto-contraste', 'itens': itens},
          open(SPEC, 'w'), ensure_ascii=False, indent=1)
print('ok', SPEC, 'seta de', itens[0]['ini'], 'a', fim)
