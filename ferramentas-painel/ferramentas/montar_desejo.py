#!/usr/bin/env python3
"""Imagens do desejo dentro do vídeo (edição dopaminérgica), em tela cheia ou em TELA DIVIDIDA (16/11/2026).

De onde vem:
  - tela cheia: o nora66 (15/11), `ferramentas-painel/dia-1511/montar_bases_nora66.py` (aulas 12 e 14);
  - tela dividida (pedido do aluno em 16/11: "pode ser um teste pra fazermos também"): a aula 12 (0:27:18 a 0:28:27,
    Iorhan): "nos primeiros 15 a 30 segundos… vai ficar mesclando entre avatar na tela e o take, a cena ocupando 100% da tela";
    "o avatar na tela, a tela dividida chamativa e o efeito sonoro… os nossos hook rates aumentaram"; "em cima da tela ou
    embaixo da tela vocês vão ter o avatar". No nora66 as 7 imagens foram em tela cheia e a Nora sumiu da tela por ~25 s.

Modos de cada imagem:
  - "cheia": a imagem ocupa a tela toda (entra de 1,10x para 1,00x em 0,25 s e depois avança devagar até 1,05x);
  - "dividida": a Nora continua falando na METADE DE CIMA (o recorte 1080x960 do quadro dela a partir de `nora_y0`, o rosto
    inteiro e os ombros) e a imagem entra na METADE DE BAIXO, com a mesma animação. A Nora fica em cima porque a legenda fica
    no terço de baixo (66% a 82% da altura): com a Nora embaixo, a legenda cobriria o rosto dela.
Regras que já valiam no nora66: imagem logo depois de outra entra em corte seco (com fade a Nora aparecia transparente na
troca) e cada imagem fica 1 quadro a mais (o overlay largava 1 quadro antes e a Nora piscava).
O texto (caixa, números, legenda, faixa, seta) e os sons entram depois, pelo editar_video.py (e o -FACE pelo variacao_face.py).

Uso: python3 -I montar_desejo.py config.json
config = {
  "entrada": "montado.mp4",            # o vídeo da Nora (com áudio)
  "saida": "base.mp4",
  "trechos": [[ini, fim], ...],        # opcional: partes do montado emendadas (sem isso, o vídeo inteiro)
  "nora_y0": 110,                      # opcional: de onde começa o recorte da Nora na tela dividida (px no quadro 1080x1920)
  "imagens": [{"arquivo": "desejo.jpg", "ini": 7.3, "fim": 9.4, "modo": "dividida", "foco_y": 0.5}, ...]
}
Os tempos das imagens são no tempo da SAÍDA (depois de emendar os trechos). "foco_y" (0 a 1) diz que altura da imagem fica
no centro do recorte (só na dividida; padrão 0,5).
"""
import json, math, os, subprocess, sys
from PIL import Image

W, H, FPS = 1080, 1920, 24
HM = H // 2


def clipe(arq, dur, w, h, saida, foco_y=0.5):
    src = Image.open(arq).convert('RGB')
    sw, sh = src.size
    bw = sw; bh = bw * h / w
    if bh > sh: bh = sh; bw = bh * w / h
    cx = sw / 2
    cy = min(max(sh * foco_y, bh / 2), sh - bh / 2)
    nq = int(math.ceil(dur * FPS)) + 2
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{w}x{h}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', saida], stdin=subprocess.PIPE)
    for i in range(nq):
        t = i / FPS
        if t < 0.25:
            u = t / 0.25; s = 1.10 - 0.10 * (1 - (1 - u) ** 3)
        else:
            s = 1.0 + 0.05 * (t - 0.25) / max(0.01, dur - 0.25)
        bw2, bh2 = bw / s, bh / s
        box = (cx - bw2 / 2, cy - bh2 / 2, cx + bw2 / 2, cy + bh2 / 2)
        p.stdin.write(src.resize((w, h), Image.LANCZOS, box=box).tobytes())
    p.stdin.close(); p.wait()


def main(cfg_path):
    cfg = json.load(open(cfg_path, encoding='utf-8'))
    ent, out = cfg['entrada'], cfg['saida']
    pasta = os.path.join(os.path.dirname(os.path.abspath(out)), 'clipes-desejo')
    os.makedirs(pasta, exist_ok=True)
    y0 = int(cfg.get("nora_y0", 110))
    imgs = sorted(cfg['imagens'], key=lambda d: d['ini'])
    ins = ['-i', ent]
    f = []
    trechos = cfg.get('trechos')
    if trechos:
        lv = []
        for j, (a, b) in enumerate(trechos):
            f.append(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS,setsar=1[v{j}]')
            f.append(f'[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={b - a - 0.03:.3f}:d=0.03[a{j}]')
            lv += [f'[v{j}]', f'[a{j}]']
        f.append(''.join(lv) + f'concat=n={len(trechos)}:v=1:a=1[vb][ab]')
    else:
        f.append('[0:v]setpts=PTS-STARTPTS,setsar=1[vb]'); f.append('[0:a]asetpts=PTS-STARTPTS[ab]')
    ndiv = sum(1 for d in imgs if d.get('modo', 'cheia') == 'dividida')
    if ndiv:
        f.append(f'[vb]split={ndiv + 1}[vm]' + ''.join(f'[vs{i}]' for i in range(ndiv)))
        for i in range(ndiv):
            f.append(f'[vs{i}]crop={W}:{HM}:0:{y0}[nt{i}]')
        ult = 'vm'
    else:
        ult = 'vb'
    fim_ant, idiv = -1.0, 0
    for k, d in enumerate(imgs):
        a, b, modo = d['ini'], d['fim'], d.get('modo', 'cheia')
        h = H if modo == 'cheia' else HM
        nome = os.path.splitext(os.path.basename(d['arquivo']))[0]
        arq = os.path.join(pasta, f'{nome}-{modo}-{b - a:.2f}-{d.get("foco_y", 0.5)}.mp4')
        if not os.path.exists(arq): clipe(d['arquivo'], b - a, W, h, arq, d.get('foco_y', 0.5))
        ins += ['-i', arq]
        seco = abs(a - fim_ant) < 0.02
        fim_ant = b
        fade = '' if seco else 'fade=t=in:st=0:d=0.12:alpha=1,'
        en = f"enable='between(t,{a - 0.001:.3f},{b + 0.040:.3f})'"
        f.append(f'[{k + 1}:v]format=yuva420p,{fade}setpts=PTS-STARTPTS+{a:.3f}/TB[i{k}]')
        if modo == 'cheia':
            f.append(f'[{ult}][i{k}]overlay=0:0:eof_action=pass:{en}[o{k}]')
        else:
            # a Nora sobe para a metade de cima (o mesmo quadro, no mesmo tempo) e a imagem entra na de baixo
            f.append(f'[{ult}][nt{idiv}]overlay=0:0:{en}[n{k}]')
            f.append(f'[n{k}][i{k}]overlay=0:{HM}:eof_action=pass:{en}[o{k}]')
            idiv += 1
        ult = f'o{k}'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(f), '-map', f'[{ult}]', '-map', '[ab]',
                    '-c:v', 'libx264', '-crf', '15', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', str(FPS),
                    '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', out], check=True)
    print('ok', out)


if __name__ == '__main__':
    main(sys.argv[1])
