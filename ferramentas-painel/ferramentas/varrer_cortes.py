#!/usr/bin/env python3
"""A varredura dos cortes de silêncio antes do render (LICOES-FLOW-E-PROMPTS.md, 26/11 18h50; feita em código em 27/11, no nora81,
depois de o "-ly" do "unexpectedly" e o "s" do "matters" serem comidos de novo).

O `editar_simples_2311.py` corta o silêncio entre 2 palavras quando a pausa passa de 0,45 s (0,60 s depois de vírgula),
começando no fim da palavra + 0,12 s. O Whisper às vezes marca o fim cedo demais ("-ly", "s", "-ed" baixinhos), e o corte come o final.
Aqui eu meço a energia do áudio (janelas de 20 ms) depois do fim que o Whisper deu: enquanto houver voz contínua, o fim da palavra
anda para a frente. Grava o palavras.json corrigido por cima (o original fica em <arquivo>.antes-varredura.json) e diz o que mudou.

Uso: python3 -I varrer_cortes.py <video-ou-audio> <palavras.json>
"""
import json, os, subprocess, sys
import numpy as np

MIDIA, PAL = sys.argv[1:3]
SR, JAN = 16000, 0.02
LIMIAR_DB = -27.0   # voz: acima disso (a música de fundo, a -18 dB no CapCut, fica abaixo de ~-32 dB nas pausas)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', MIDIA, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'],
                     capture_output=True, check=True).stdout
a = np.frombuffer(raw, dtype=np.float32)


def db(t):
    s = a[int(t * SR):int((t + JAN) * SR)]
    return 20 * np.log10(np.sqrt((s ** 2).mean()) + 1e-9) if len(s) else -99.0


ws = json.load(open(PAL, encoding='utf-8'))
mud = []
for i, (w1, w2) in enumerate(zip(ws, ws[1:])):
    lim = 0.60 if w1[0].endswith(',') else 0.45
    if w2[1] - w1[2] <= lim:
        continue
    # anda do fim do Whisper para a frente enquanto houver voz (no máximo 0,6 s, e nunca até a palavra seguinte)
    fim, quietas = w1[2], 0
    for k in range(int(round(min(0.6, w2[1] - 0.15 - w1[2]) / JAN))):   # passos inteiros (com soma de float, 0,08 virava 0,0800001)
        t = w1[2] + k * JAN
        if db(t) > LIMIAR_DB:
            fim, quietas = t + JAN, 0
        else:
            quietas += 1
            if quietas >= 6:   # 120 ms de silêncio depois da última voz = a palavra acabou
                break
    if fim > w1[2] + 0.04:
        mud.append((i, w1[0], w1[2], round(fim, 2)))
        w1[2] = round(fim, 2)
if mud:
    os.replace(PAL, PAL.replace('.json', '') + '.antes-varredura.json')
    json.dump(ws, open(PAL, 'w'), ensure_ascii=False)
print(f'varredura {os.path.basename(PAL)}: {len(mud)} fim(ns) de palavra corrigido(s)')
for i, p, de, para in mud:
    print(f'  #{i} {p!r}: fim {de:.2f} -> {para:.2f} s')
