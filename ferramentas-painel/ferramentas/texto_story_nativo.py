#!/usr/bin/env python3
"""Texto do story da Nora no jeito do texto nativo do Instagram (decisão de 18/11/2026).

O aluno pediu um story "mais simples, mais básico, igual é falado nas aulas" (aula 39, 0:58:02, o Felps:
"imagens… com textuzinho"; Clone R2: texto curto e objetivo). Fica como o texto que qualquer pessoa põe
no próprio app: letra sem serifa (Inter SemiBold, parecida com a "Classic" do Instagram), centralizada,
cada linha numa faixa de cantos arredondados, sem sombra, sem destaque de cor, sem itálico.

Modos (--modo): branco = texto preto em faixa branca (parede clara, o padrão); preto = texto branco em
faixa preta (fundo claro demais ou estourado); sombra = texto branco sem faixa, só uma sombra leve
(fundo escuro). Uso (da raiz do repositório):
  python3 -I ferramentas-painel/ferramentas/texto_story_nativo.py foto.jpg saida.jpg \
      --linha "You found this for a reason." --linha "Your 2027 reading is waiting below."
Opções: --topo 0.08 (onde começa, em fração da altura), --tamanho 0.042 (corpo da letra em fração da largura).
Gera também <saida>-recorte.jpg (o texto no tamanho real) e <saida>-celular.jpg (a foto reduzida).
"""
import argparse, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(AQUI, 'fontes', 'Inter-SemiBold.otf')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('foto'); ap.add_argument('saida')
    ap.add_argument('--linha', action='append', required=True)
    ap.add_argument('--topo', type=float, default=0.08)
    ap.add_argument('--tamanho', type=float, default=0.042)
    ap.add_argument('--modo', choices=['branco', 'preto', 'sombra'], default='branco')
    a = ap.parse_args()
    im = Image.open(a.foto).convert('RGB')
    W, H = im.size
    f = ImageFont.truetype(FONTE, max(12, int(W * a.tamanho)))
    asc, desc = f.getmetrics()
    padx, pady = int(W * a.tamanho * 0.42), int(W * a.tamanho * 0.22)
    alt = asc + desc + 2 * pady
    y = int(H * a.topo)
    caixas = []
    for ln in a.linha:
        l, t, r, b = f.getbbox(ln)
        larg = (r - l) + 2 * padx
        x0 = (W - larg) // 2
        caixas.append((ln, x0, y, x0 + larg, y + alt, l))
        y += alt - int(pady * 0.6)  # as faixas encostam, como no app
    esq = min(c[1] for c in caixas) / W; dir_ = max(c[3] for c in caixas) / W
    if esq < 0.08 or dir_ > 0.92:
        sys.exit(f'ERRO: o texto vai de {esq:.0%} a {dir_:.0%} da largura (tem de ficar entre 8% e 92%): encurte a linha ou baixe o --tamanho')
    camada = Image.new('RGBA', im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    raio = int(alt * 0.28)
    if a.modo in ('branco', 'preto'):
        cor_caixa = (255, 255, 255, 255) if a.modo == 'branco' else (0, 0, 0, 255)
        for _, x0, y0, x1, y1, _ in caixas:
            d.rounded_rectangle((x0, y0, x1, y1), radius=raio, fill=cor_caixa)
    else:
        sombra = Image.new('RGBA', im.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(sombra)
        for ln, x0, y0, x1, y1, l in caixas:
            ds.text((x0 + padx - l, y0 + pady + 2), ln, font=f, fill=(0, 0, 0, 150))
        camada = Image.alpha_composite(camada, sombra.filter(ImageFilter.GaussianBlur(W * 0.004)))
        d = ImageDraw.Draw(camada)
    cor_txt = (0, 0, 0, 255) if a.modo == 'branco' else (255, 255, 255, 255)
    for ln, x0, y0, x1, y1, l in caixas:
        d.text((x0 + padx - l, y0 + pady), ln, font=f, fill=cor_txt)
    out = Image.alpha_composite(im.convert('RGBA'), camada).convert('RGB')
    out.save(a.saida, quality=95)
    base, ext = os.path.splitext(a.saida)
    y0 = max(0, caixas[0][2] - int(H * 0.03)); y1 = min(H, caixas[-1][4] + int(H * 0.08))
    out.crop((0, y0, W, y1)).save(base + '-recorte.jpg', quality=90)
    out.resize((390, int(390 * H / W))).save(base + '-celular.jpg', quality=90)
    print(f'ok {a.saida}: texto de {esq:.0%} a {dir_:.0%} da largura, de {caixas[0][2] / H:.1%} a {caixas[-1][4] / H:.1%} da altura')


if __name__ == '__main__':
    main()
