#!/usr/bin/env python3
"""nora66 (15/11/2026): as 2 bases (Insta e Face) a partir do montado do CapCut, com as imagens do desejo já dentro do vídeo.

A edição dopaminérgica (aulas 12 e 14; aprovada pelo aluno em 15/11 03h00): cada imagem entra em tela cheia na frase que ela ilustra,
com uma animação de entrada (sai de 1,10x para 1,00x em 0,25 s e depois avança devagar até 1,05x) e um fade de 0,12 s; a voz segue
por baixo. O texto (caixa, números, legenda, faixa, seta) e os sons (riser, impact, whoosh) entram depois, pelo editar_video.py.

Uso: python3 -I montar_bases_nora66.py <montado.mp4> <pasta das imagens desejo-1..7.jpg> <pasta de saída>
"""
import math, os, subprocess, sys
from PIL import Image

MONT, DES, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
W, H, FPS = 1080, 1920, 24
V0 = 0.083                    # o vídeo do montado do CapCut começa em 0,083 s (o áudio em 0)
CORTE_T01, CORTE_T05, CORTE_T06, CORTE_T07 = 4.9163, 36.083, 40.916, 46.958
FIM = 52.886

# (imagem, início, fim) no tempo do montado; a frase que ela ilustra
IMGS = [
    (1, 7.40, 9.55),    # "pour salt before sleeping?"
    (2, 12.70, 14.85),  # "You spent months smiling for everyone,"
    (3, 14.85, 17.35),  # "while carrying heavy worry alone in bed,"
    (4, 23.80, 25.40),  # "bringing unexpected money," (só Insta: nota de dinheiro não vai no Face)
    (5, 25.40, 26.60),  # "deep peace"
    (6, 26.60, 28.20),  # "and someone truly wonderful."
    (7, 30.45, 33.45),  # "Heavy doors that stayed locked all year are finally opening"
]
# recorte de cada imagem (x0, y0, lado) em fração; a 1 sobe o pote de sal para fora da faixa da legenda (66% a 82% da altura)
RECORTE = {1: (0.0, 0.23, 0.77)}


def clipe(n, dur, saida):
    src = Image.open(os.path.join(DES, f'desejo-{n}.jpg')).convert('RGB')
    sw, sh = src.size
    x0, y0, f = RECORTE.get(n, (0.0, 0.0, 1.0))
    bw = sw * f; bh = bw * H / W
    if bh > sh * (1 - y0): bh = sh * (1 - y0); bw = bh * W / H
    cx, cy = sw * x0 + bw / 2, sh * y0 + bh / 2
    nq = int(math.ceil(dur * FPS)) + 2  # 2 quadros a mais: o corte exato fica com o enable (com o round, faltava 1 quadro e a Nora piscava entre 2 imagens)
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', saida], stdin=subprocess.PIPE)
    for i in range(nq):
        t = i / FPS
        if t < 0.25:
            u = t / 0.25; s = 1.10 - 0.10 * (1 - (1 - u) ** 3)   # entrada: 1,10x -> 1,00x, desacelerando
        else:
            s = 1.0 + 0.05 * (t - 0.25) / max(0.01, dur - 0.25)  # depois, avança devagar até 1,05x
        w, h = bw / s, bh / s
        box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
        p.stdin.write(src.resize((W, H), Image.LANCZOS, box=box).tobytes())
    p.stdin.close(); p.wait()


def base(nome, trechos, imgs):
    """trechos: [(ini, fim)] no tempo do montado, emendados; imgs: [(n, ini, fim)] já no tempo da base."""
    ins = ['-i', MONT]
    fv, fa, lv, la = [], [], [], []
    for j, (a, b) in enumerate(trechos):
        fv.append(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS,setsar=1[v{j}]')
        fa.append(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={b - a - 0.03:.3f}:d=0.03[a{j}]')
        lv.append(f'[v{j}]'); la.append(f'[a{j}]')
    f = fv + fa + [''.join(x for par in zip(lv, la) for x in par) + f'concat=n={len(trechos)}:v=1:a=1[vb][ab]']
    ult = 'vb'; fim_ant = -1.0
    for k, (n, a, b) in enumerate(imgs):
        arq = os.path.join(OUT, f'desejo-{n}-{b - a:.2f}.mp4')
        if not os.path.exists(arq): clipe(n, b - a, arq)
        ins += ['-i', arq]
        # imagem logo depois de outra: corte seco (com o fade, a Nora aparecia transparente na troca; conferido no 1º render, 15/11)
        fade = '' if abs(a - fim_ant) < 0.02 else 'fade=t=in:st=0:d=0.12:alpha=1,'
        fim_ant = b
        f.append(f'[{k + 1}:v]format=yuva420p,{fade}setpts=PTS-STARTPTS+{a:.3f}/TB[i{k}]')
        f.append(f"[{ult}][i{k}]overlay=0:0:eof_action=pass:enable='between(t,{a:.3f},{b - 0.001:.3f})'[o{k}]"); ult = f'o{k}'
    saida = os.path.join(OUT, nome)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(f), '-map', f'[{ult}]', '-map', '[ab]',
                    '-c:v', 'libx264', '-crf', '15', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', str(FPS),
                    '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', saida], check=True)
    print('ok', saida)


os.makedirs(OUT, exist_ok=True)
# Insta: o pré-gancho (já colado pelo aluno) + T01 a T06; tempo da base = montado - 0,083
base('nora66-insta-base.mp4', [(V0, CORTE_T07)], [(n, a - V0, b - V0) for n, a, b in IMGS])
# Face: T01 a T04 + T07, sem o pré-gancho e sem a imagem do dinheiro
d1 = CORTE_T05 - CORTE_T01
face = [(n, a - CORTE_T01, b - CORTE_T01) for n, a, b in IMGS if n != 4]
base('nora66-face-base.mp4', [(CORTE_T01, CORTE_T05), (CORTE_T07, FIM)], face)
