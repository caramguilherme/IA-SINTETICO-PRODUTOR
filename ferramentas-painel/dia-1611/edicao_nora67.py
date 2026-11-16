#!/usr/bin/env python3
"""Edição do nora67 (o café Folgers), 16/11/2026: as 2 bases com as imagens do desejo, o cadeado e as 2 specs.

Uso: python3 -I edicao_nora67.py <NORA67.mp4 montado> <palavras.json do montado> <pasta de trabalho>
Depois: editar_video.py <pasta>/spec-nora67.json e <pasta>/spec-nora67-FACE.json (cópias ficam em ferramentas/specs/).

O montado do aluno (43,1 s) veio com o 1º hook (o da moeda boiando, reprovado por ele às 19h18) em 0,083 a 3,75 s e os
takes T01 a T06 depois (cortes em 8,25 · 15,25 · 23,33 · 30,083 · 37,833). Aqui:
- Insta = o hook novo (d1611-PRE-cafe-HOOK.mp4, 3,667 s, a moeda cortada no ar) + o montado de 3,75 a 37,833 (T01 a T05);
- Face  = o montado de 3,75 a 30,083 (T01 a T04) + de 37,833 ao fim (T06), sem o hook do produto (regra de 14/11).
Imagens do desejo (ROTEIRO_DESEJO do build_dia_1611.py): dividida e cheia alternadas, do T02 ao fim do T04; a do dinheiro só no Insta.
"""
import copy
import json
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
FERR = os.path.join(AQUI, '..', 'ferramentas')
DES = os.path.join(AQUI, 'desejo-1080')
HOOK = os.path.join(AQUI, 'd1611-PRE-cafe-HOOK.mp4')
H_DUR = 3.667
T01, T05_FIM, T04_FIM = 3.75, 37.833, 30.083

# (arquivo, ini, fim no MONTADO, modo, foco_y, só no Insta)
IMAGENS = [
    ('d1511-DESEJO-2-sorrindo-para-todos.jpg', 9.10, 11.00, 'dividida', 0.5, False),   # "holding it together for everyone"
    ('d1611-DESEJO-8-contas-e-tarefas.jpg', 11.00, 12.85, 'dividida', 0.55, False),     # "juggling bills and errands"
    ('d1511-DESEJO-3-sozinha-na-cama.jpg', 12.85, 15.20, 'cheia', 0.5, False),          # "quietly wondering when your turn would come"
    ('d1511-DESEJO-4-dinheiro-no-envelope.jpg', 19.20, 20.65, 'cheia', 0.5, True),      # "unexpected cash" (só Insta)
    ('d1511-DESEJO-5-paz-na-varanda.jpg', 20.65, 21.95, 'dividida', 0.55, False),       # "peace of mind"
    ('d1511-DESEJO-6-casal-na-praia.jpg', 21.95, 23.30, 'cheia', 0.5, False),           # "someone truly wonderful"
    ('d1511-DESEJO-7-porta-abrindo.jpg', 24.38, 27.90, 'dividida', 0.5, False),         # "doors… finally opening"
    ('d1611-DESEJO-9-festas.jpg', 27.90, 30.05, 'cheia', 0.5, False),                   # "just in time for the holidays"
]
DESTAQUES = ['ALONE,', 'QUIET', 'EVERYONE,', 'BILLS', 'ERRANDS,', 'TURN', 'FAITH.', 'TURNAROUND', 'CASH,', 'PEACE',
             'WONDERFUL.', 'HARDEST', 'OVER.', 'DOORS', 'OPENING,', 'HOLIDAYS.', 'PHOTO', 'STORY', '2027.', 'COMMENTS', '2027']
CAIXA_TOPO = {"fundo": [255, 214, 0, 255], "texto": "#000000", "destaque": "#000000", "fonte": "bold",
              "destaque_fonte": "bold", "raio": 14, "sombra": None}


def ff(*a):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *a], check=True)


def cadeado(saida, px=120):
    """O cadeado desenhado (o 🔒 não existe na Poppins): vermelho do destaque da faixa, com o furo da chave branco."""
    im = Image.new('RGBA', (px, px), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    vm = (221, 29, 29, 255)
    lw = int(px * 0.11)
    d.arc([px * 0.24, px * 0.04, px * 0.76, px * 0.60], 180, 360, fill=vm, width=lw)
    d.line([px * 0.24 + lw / 2, px * 0.32, px * 0.24 + lw / 2, px * 0.50], fill=vm, width=lw)
    d.line([px * 0.76 - lw / 2, px * 0.32, px * 0.76 - lw / 2, px * 0.50], fill=vm, width=lw)
    d.rounded_rectangle([px * 0.12, px * 0.44, px * 0.88, px * 0.96], radius=int(px * 0.10), fill=vm)
    d.ellipse([px * 0.43, px * 0.56, px * 0.57, px * 0.70], fill=(255, 255, 255, 255))
    d.rectangle([px * 0.475, px * 0.66, px * 0.525, px * 0.84], fill=(255, 255, 255, 255))
    im.save(saida)


def pos_cadeado(linha1, linha2, y, tamanho=10, W=1080):
    """Onde fica o vão de espaços no fim da linha 1 da faixa (mesma conta do png_caixa_estilo): devolve x, y no espaço 720."""
    k = W / 720.0; sz = tamanho * 2.8 * k
    f = ImageFont.truetype(os.path.join(FERR, 'fontes', 'Poppins-Bold.ttf'), int(round(sz)))
    d = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    w1, w2 = d.textlength(linha1, font=f), d.textlength(linha2.strip('[]'), font=f)
    vao = d.textlength(linha1.rstrip(), font=f)
    x0 = W / 2 - max(w1, w2) / 2 + (max(w1, w2) - w1) / 2  # início da linha 1 (centrada)
    asc, desc = f.getmetrics(); lh = int((asc + desc) * 1.15); pady = int(13 * k)
    bh = lh * 2 + 2 * pady
    cy_px = (1920 / 2 - y * k) - bh / 2 + pady + lh / 2
    cx_px = x0 + vao + (w1 - vao) / 2
    return (cx_px - W / 2) / k, (1920 / 2 - cy_px) / k


def palavras(arq, de, ate, desloc):
    ws = json.load(open(arq, encoding='utf-8'))
    out = []
    for w, a, b in ws:
        if de - 0.6 <= a < ate:
            a2 = max(a, de + 0.03) + desloc
            out.append([w.replace('1111', '11:11'), round(a2, 3), round(b + desloc, 3)])
    return out


def main(montado, pal_json, pasta):
    os.makedirs(pasta, exist_ok=True)
    fim_m = 43.10
    # 1. a pré-base do Insta: o hook novo + o montado do T01 ao fim do T05
    pre = os.path.join(pasta, 'nora67-insta-pre.mp4')
    ff('-i', HOOK, '-i', montado, '-filter_complex',
       f'[0:v]fps=24,scale=1080:1920,setsar=1[v0];[0:a]aresample=48000,afade=t=out:st={H_DUR - 0.03:.3f}:d=0.03[a0];'
       f'[1:v]trim={T01}:{T05_FIM},setpts=PTS-STARTPTS,setsar=1[v1];'
       f'[1:a]atrim={T01}:{T05_FIM},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d=0.03,afade=t=out:st={T05_FIM - T01 - 0.03:.3f}:d=0.03[a1];'
       '[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]', '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '14', '-preset', 'medium',
       '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-b:a', '192k', pre)
    d_ins = H_DUR - T01                       # montado → Insta
    d_fb1 = -T01                              # montado (T01 a T04) → Face
    d_fb2 = (T04_FIM - T01) - T05_FIM         # montado (T06) → Face
    dur_ins = H_DUR + (T05_FIM - T01)
    dur_fb = (T04_FIM - T01) + (fim_m - T05_FIM)

    def imgs(desloc, insta):
        return [{"arquivo": os.path.join(DES, a), "ini": round(i + desloc, 3), "fim": round(f + desloc, 3), "modo": m, "foco_y": fy}
                for a, i, f, m, fy, so in IMAGENS if insta or not so]
    cfg_i = {"entrada": pre, "saida": os.path.join(pasta, 'nora67-insta-base.mp4'), "imagens": imgs(d_ins, True)}
    cfg_f = {"entrada": montado, "saida": os.path.join(pasta, 'nora67-face-base.mp4'),
             "trechos": [[T01, T04_FIM], [T05_FIM, fim_m]], "imagens": imgs(d_fb1, False)}
    for nome, cfg in (('desejo-nora67.json', cfg_i), ('desejo-nora67-FACE.json', cfg_f)):
        p = os.path.join(pasta, nome); json.dump(cfg, open(p, 'w'), indent=1)
        subprocess.run([sys.executable, '-I', os.path.join(FERR, 'montar_desejo.py'), p], check=True)

    # 2. o cadeado e a faixa do Insta
    lock = os.path.join(pasta, 'cadeado.png'); cadeado(lock)
    l1, l2 = 'Your 2027 reading:      ', '[tap my photo]'
    lx, ly = pos_cadeado(l1, l2, 470)
    numeros = lambda fim: [
        {"tipo": "texto", "ini": 0, "fim": fim, "x": -230, "y": 282, "tamanho": 13, "texto": "222", "cor": "#FFFFFF"},
        {"tipo": "texto", "ini": 0, "fim": fim, "x": 230, "y": 282, "tamanho": 13, "texto": "11:11", "cor": "#FFFFFF"}]
    caixa = lambda fim: {"tipo": "caixa", "ini": 0, "fim": fim, "x": 0, "y": 458, "tamanho": 10,
                         "linhas": ["CARRYING IT ALL ALONE?", "TRY THIS COFFEE RITUAL"], "caixa": CAIXA_TOPO}
    whoosh = lambda lst: [{"som": "whoosh", "pico_em": round(d["ini"] + 0.05, 3), "db": -12} for d in lst]

    pal_i = palavras(pal_json, T01, T05_FIM, d_ins)
    ins = {"entrada": cfg_i["saida"], "saida": os.path.join(pasta, 'nora67-final.mp4'), "crf": 21, "preset": "medium",
           "estilo": "alto-contraste", "corte": H_DUR, "respiro": 0.1,
           "sons": [{"som": "riser", "pico_em": "corte-0.1"}, {"som": "impact", "pico_em": "corte"}] + whoosh(cfg_i["imagens"]),
           "itens": [caixa(round(8.25 + d_ins, 3))] + numeros(round(dur_ins, 3)) + [
               {"tipo": "legenda", "ini": H_DUR, "fim": round(dur_ins, 3), "palavras": pal_i, "destaques": DESTAQUES, "y": -310, "tamanho_px": 38},
               {"tipo": "caixa", "ini": round(T04_FIM + d_ins, 3), "fim": round(dur_ins, 3), "x": 0, "y": 470, "tamanho": 10, "linhas": [l1, l2]},
               {"tipo": "imagem", "ini": round(T04_FIM + d_ins, 3), "fim": round(dur_ins, 3), "arquivo": lock, "largura": 30,
                "x": round(lx, 1), "y": round(ly, 1)},
               {"tipo": "seta", "ini": round(T04_FIM + d_ins, 3), "fim": round(dur_ins, 3), "x": -288, "y": -333, "tamanho": 14}]}
    pal_f = palavras(pal_json, T01, T04_FIM, d_fb1) + palavras(pal_json, T05_FIM, fim_m, d_fb2)
    fb = {"entrada": cfg_f["saida"], "saida": os.path.join(pasta, 'nora67-final-FACE.mp4'), "crf": 21, "preset": "medium",
          "estilo": "alto-contraste", "sons": whoosh(cfg_f["imagens"]),
          "itens": [caixa(round(8.25 + d_fb1, 3))] + numeros(round(dur_fb, 3)) + [
              {"tipo": "legenda", "ini": 0, "fim": round(dur_fb, 3), "palavras": pal_f, "destaques": DESTAQUES, "y": -310, "tamanho_px": 38},
              {"tipo": "caixa", "ini": round(T05_FIM + d_fb2, 3), "fim": round(dur_fb, 3), "x": 0, "y": 470, "tamanho": 10,
               "linhas": ["Your 2027 reading:", "[link in the comments]"]}]}
    for nome, sp in (('spec-nora67.json', ins), ('spec-nora67-FACE.json', fb)):
        json.dump(sp, open(os.path.join(pasta, nome), 'w'), indent=1)
    print('insta', round(dur_ins, 3), 'face', round(dur_fb, 3), 'cadeado', round(lx, 1), round(ly, 1))


if __name__ == '__main__':
    main(*sys.argv[1:4])
