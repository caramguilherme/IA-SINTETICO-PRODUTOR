#!/usr/bin/env python3
"""Monta o pré-gancho do nora67 (o café Folgers), no formato do Clone R60: 3 tomadas, ~3,6 s.

Uso: python3 -I montar_hook_nora67.py <pasta com os 3 vídeos d1611-PRE-cafe-*> <saida.mp4>

Os cortes saíram da conferência quadro a quadro de 16/11 (ROTEIRO-DIA-1611-NORA67-68.md, Andamento):
- 1-colher, 0,60 a 2,00 s: o café cai da colher na água e se espalha, com a lata do Folgers legível ao lado;
- 2-moeda, 0,90 a 2,30 s, aproximado 1,25x na caneca: a mão solta a moeda e ela cai no café e afunda.
  O vídeo segue e a moeda "atravessa" o vidro e aparece no pires a partir de ~2,6 s (erro do Flow): o corte para antes;
- 3-aponta, 1,75 a 2,55 s: ela tira a mão da caneca e aponta para a lente, com o gesto ainda andando (R59/R60).
Áudio: só o ambiente dos clipes, com fade de 20 ms em cada emenda; o riser e o impact entram na edição final.
"""
import glob
import os
import subprocess
import sys

CORTES = [  # (parte do nome, início, fim, zoom)
    ('1-colher', 0.60, 2.00, 1.0),
    ('2-moeda', 0.90, 2.30, 1.25),
    ('3-aponta', 1.75, 2.55, 1.0),
]
W, H, FPS = 1080, 1920, 30


def main(pasta, saida):
    entradas, filtros, rotulos = [], [], []
    for i, (parte, ini, fim, zoom) in enumerate(CORTES):
        arq = glob.glob(os.path.join(pasta, f'd1611-PRE-cafe-{parte}*.mp4'))
        assert len(arq) == 1, (parte, arq)
        entradas += ['-i', arq[0]]
        dur = fim - ini
        v = f'[{i}:v]trim={ini}:{fim},setpts=PTS-STARTPTS,scale={W}:{H},fps={FPS}'
        if zoom > 1.0:
            cw, ch = int(W / zoom) // 2 * 2, int(H / zoom) // 2 * 2
            # centrado na caneca (metade de baixo do quadro), sem sair da imagem
            x, y = (W - cw) // 2 - 40, H - ch
            v += f',crop={cw}:{ch}:{x}:{y},scale={W}:{H}'
        filtros.append(v + ',setsar=1' + f'[v{i}]')
        filtros.append(f'[{i}:a]atrim={ini}:{fim},asetpts=PTS-STARTPTS,aresample=48000,'
                       f'afade=t=in:d=0.02,afade=t=out:st={dur - 0.02:.3f}:d=0.02[a{i}]')
        rotulos.append(f'[v{i}][a{i}]')
    filtros.append(''.join(rotulos) + f'concat=n={len(CORTES)}:v=1:a=1[v][a]')
    cmd = ['ffmpeg', '-v', 'error', '-y', *entradas, '-filter_complex', ';'.join(filtros),
           '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '17', '-preset', 'medium',
           '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', saida]
    subprocess.run(cmd, check=True)
    print(saida)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
