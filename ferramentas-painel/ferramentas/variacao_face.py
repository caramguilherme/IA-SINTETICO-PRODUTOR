#!/usr/bin/env python3
"""Variação do Face (regra de 10/11/2026: o Face trava post que repete o corpo de um post anterior).

Gera o noraNN-final-FACE a partir da MESMA spec da edição (P45):
  1. espelha o vídeo montado e clareia um pouco (no lugar do filtro "Dias claros" 30% do CapCut);
  2. põe por cima os mesmos textos da spec, com os números fixos espelhados (X -> -X), para continuarem
     longe do rosto e da mão livre, que trocaram de lado; caixa, legenda, imagens e seta ficam onde estão
     (a seta continua embaixo à esquerda, apontando para a foto do perfil);
  3. acelera tudo para 1,1x (vídeo e áudio, sem mudar o tom da voz).

Uso (da raiz do repositório):  python3 -I ferramentas-painel/ferramentas/variacao_face.py spec.json
Saída: o nome da "saida" da spec com -FACE antes do .mp4 (ex.: nora56-final-FACE.mp4).
"""
import json, os, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editar_video  # noqa: E402

BRILHO = 'hflip,eq=brightness=0.035:contrast=1.04:saturation=1.08:gamma=1.04'
VEL = 1.1


def main(spec_path):
    sp = json.load(open(spec_path, encoding='utf-8'))
    tmp = tempfile.mkdtemp(prefix='face_')
    base = os.path.join(tmp, 'base-espelhada.mp4')
    subprocess.check_call(['ffmpeg', '-y', '-v', 'error', '-i', sp['entrada'], '-vf', BRILHO, '-c:v', 'libx264', '-crf', '14',
                           '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'copy', base])
    sp2 = json.loads(json.dumps(sp))
    sp2['entrada'] = base
    sp2['saida'] = os.path.join(tmp, 'com-textos.mp4')
    sp2['crf'] = 16
    for it in sp2['itens']:
        if it['tipo'] == 'texto':
            it['x'] = -it['x']
    p2 = os.path.join(tmp, 'spec-face.json')
    json.dump(sp2, open(p2, 'w', encoding='utf-8'), ensure_ascii=False)
    editar_video.main(p2)
    raiz, ext = os.path.splitext(sp['saida'])
    saida = raiz + '-FACE' + (ext or '.mp4')
    subprocess.check_call(['ffmpeg', '-y', '-v', 'error', '-i', sp2['saida'], '-filter_complex',
                           f'[0:v]setpts=PTS/{VEL}[v];[0:a]atempo={VEL}[a]', '-map', '[v]', '-map', '[a]',
                           '-c:v', 'libx264', '-crf', str(sp.get('crf', 21)), '-preset', sp.get('preset', 'medium'),
                           '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', saida])
    print('ok', saida)


if __name__ == '__main__':
    main(sys.argv[1])
