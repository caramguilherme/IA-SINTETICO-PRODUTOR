#!/usr/bin/env python3
"""Monta o pré-gancho do nora68 (o tsunami no rochedo), no formato do Clone R60: 3 tomadas, ~3,6 s.

Uso: python3 -I montar_hook_nora68.py <pasta com os 3 vídeos> <saida.mp4>

Os cortes saíram da conferência quadro a quadro de 17/11 00h07:
- Woman_standing_before_tsunami_wave (imagem A), 0,55 a 1,95 s: o tsunami gigante subindo e a crista curvando atrás dela, calma;
- Tsunami_wave_crashing_on_rocks (imagem B), 1,60 a 3,00 s: o tsunami explode no rochedo, a parede de espuma subindo;
- d1611-PRE-onda-3-aponta (imagem C), 1,55 a 2,35 s: depois da tempestade, ela levanta a mão e aponta para a lente.
Áudio: só o ambiente dos clipes, com fade de 20 ms em cada emenda; o riser e o impact entram na edição final.
"""
import glob
import os
import subprocess
import sys

CORTES = [  # (início do nome do arquivo, início, fim, zoom)
    ('Woman_standing_before_tsunami', 0.55, 1.95, 1.0),
    ('Tsunami_wave_crashing_on_rocks', 1.60, 3.00, 1.0),
    ('d1611-PRE-onda-3-aponta', 1.55, 2.35, 1.0),
]
W, H, FPS = 1080, 1920, 30


def main(pasta, saida):
    entradas, filtros, rotulos = [], [], []
    for i, (parte, ini, fim, zoom) in enumerate(CORTES):
        arq = glob.glob(os.path.join(pasta, f'{parte}*.mp4'))
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
