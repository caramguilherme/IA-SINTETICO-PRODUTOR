#!/usr/bin/env python3
"""Texto do story da Nora (estilo aprovado pelo aluno em 11/11/2026: "agora sim, ficou top").

Caixa creme quase opaca, com cantos bem arredondados e sombra marrom suave, no tom da foto;
texto marrom-escuro em Poppins Medium; o trecho entre [colchetes] vai em Cormorant SemiBold Itálico,
num tom terracota (o nome do funil: "private reading", "2027"...). O aluno põe só o adesivo de link.

Uso (da raiz do repositório):
  python3 -I ferramentas-painel/ferramentas/texto_story.py foto.jpg saida.jpg \
      --linha "Tap below: your [private reading]" --linha "is waiting for you on 11:11."

Opções: --topo 0.07 (onde a caixa começa, em fração da altura; acima da cabeça, abaixo da barra do
Instagram, ~6% a 9%), --tamanho 0.044 (fração da largura), --cores auto|padrao (auto: a caixa puxa o
tom mais claro da roupa/parede da foto; padrao: a paleta de 11/11).
Gera também <saida>-recorte.jpg (a faixa do texto no tamanho real) e <saida>-celular.jpg (a foto
inteira reduzida), para conferir a leitura antes de mandar.
"""
import argparse, os, re, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
FP = os.path.join(AQUI, 'fontes', 'Poppins-Medium.ttf')
FC = os.path.join(AQUI, 'fontes', 'Cormorant-SemiBoldItalic.ttf')
PADRAO = dict(caixa=(246, 238, 228), texto='#5A3A2A', destaque='#A0583A', sombra=(90, 58, 42))


def partes(linha, fp, fc, cor, dest):
    out = []
    for i, p in enumerate(re.split(r'\[|\]', linha)):
        if p:
            out.append((p, fc if i % 2 else fp, dest if i % 2 else cor))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('foto'); ap.add_argument('saida')
    ap.add_argument('--linha', action='append', required=True)
    ap.add_argument('--topo', type=float, default=0.07)
    ap.add_argument('--tamanho', type=float, default=0.044)
    ap.add_argument('--cores', default='padrao')
    a = ap.parse_args()
    im = Image.open(a.foto).convert('RGBA'); W, H = im.size
    pal = dict(PADRAO)
    if a.cores == 'auto':
        # tom claro da foto (média do quarto mais claro do miolo), clareado para a caixa
        px = sorted(im.convert('RGB').resize((60, 108)).getdata(), key=sum)
        cl = px[-len(px) // 4:]
        m = [sum(p[i] for p in cl) // len(cl) for i in range(3)]
        pal['caixa'] = tuple(min(255, int(v * 0.35 + 255 * 0.65)) for v in m)
    sz = int(W * a.tamanho)
    fp = ImageFont.truetype(FP, sz); fc = ImageFont.truetype(FC, int(sz * 1.32))
    linhas = [partes(l, fp, fc, pal['texto'], pal['destaque']) for l in a.linha]
    d = ImageDraw.Draw(im)
    wl = lambda l: sum(d.textlength(t, font=f) for t, f, _ in l)
    lw = max(wl(l) for l in linhas); lh = int(sz * 1.45)
    padx, pady = int(sz * 0.75), int(sz * 0.55)
    bw = int(lw + 2 * padx); bh = int(lh * len(linhas) + 2 * pady - sz * 0.3)
    x0, y0 = (W - bw) // 2, int(H * a.topo)
    if x0 < W * 0.08:
        sys.exit(f'texto largo demais ({x0 / W * 100:.1f}% da borda; o Face corta fora de 8% a 92%): diminua --tamanho ou quebre a linha')
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 6, x0 + bw, y0 + bh + 6], radius=int(sz * 0.9), fill=pal['sombra'] + (70,))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(10)))
    bx = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(bx).rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=int(sz * 0.9), fill=pal['caixa'] + (232,))
    im = Image.alpha_composite(im, bx); d = ImageDraw.Draw(im)
    y = y0 + pady - int(sz * 0.05)
    for l in linhas:
        x = (W - wl(l)) / 2
        for t, f, c in l:
            d.text((x, y - (int(sz * 0.22) if f is fc else 0)), t, font=f, fill=c); x += d.textlength(t, font=f)
        y += lh
    im = im.convert('RGB'); im.save(a.saida, quality=92)
    raiz = os.path.splitext(a.saida)[0]
    im.crop((0, max(0, y0 - int(H * 0.02)), W, min(H, y0 + bh + int(H * 0.03)))).save(raiz + '-recorte.jpg', quality=92)
    im.resize((W * 2 // 5, H * 2 // 5)).save(raiz + '-celular.jpg', quality=88)
    print(f'ok {a.saida}  caixa x {x0 / W * 100:.1f}-{(x0 + bw) / W * 100:.1f}%  y {y0 / H * 100:.1f}-{(y0 + bh) / H * 100:.1f}%')


if __name__ == '__main__':
    main()
