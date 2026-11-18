#!/usr/bin/env python3
"""Texto do story da Nora no jeito do texto nativo do Instagram (decisão de 18/11/2026, ajustada às ~16h50
pelos 5 stories de referência que o aluno mandou: `MATERIAIS-STORIES-REFERENCIA/LEIA.md`).

Como as contas do nicho fazem: o texto do próprio app com fundo ligado (o "A"), 2 ou 3 caixas empilhadas no
MEIO da tela (sobre o peito, logo acima do adesivo de link), cada caixa com 1 ou 2 linhas, uma caixa branca
com texto preto e outra colorida (coral, laranja, amarelo) com texto branco ou preto, emoji no fim de uma linha.
Letra sem serifa (Inter SemiBold, parecida com a "Classic" do Instagram), cantos pouco arredondados, sem sombra.

Cada --caixa é um bloco "cor|texto" (cor: branco, preto, coral, laranja, amarelo, rosa, creme); a quebra de linha
dentro da caixa é automática (até ~84% da largura), ou à mão com " // ". Uso (da raiz do repositório):
  python3 -I ferramentas-painel/ferramentas/texto_story_nativo.py foto.jpg saida.jpg \
      --caixa "branco|You found this for a reason." --caixa "coral|Your 2027 reading is waiting below 👇"
Opções: --topo 0.46 (onde a 1ª caixa começa, em fração da altura), --tamanho 0.043 (corpo da letra em fração
da largura). Diz onde o adesivo de link deve ficar e gera <saida>-recorte.jpg e <saida>-celular.jpg.
"""
import argparse, os, sys
from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(AQUI, 'fontes', 'Inter-SemiBold.otf')
EMOJI = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
CORES = {  # caixa, texto
    'branco': ((255, 255, 255), (0, 0, 0)), 'preto': ((20, 20, 20), (255, 255, 255)),
    'coral': ((226, 104, 84), (255, 255, 255)), 'laranja': ((214, 98, 52), (255, 255, 255)),
    'amarelo': ((255, 214, 0), (0, 0, 0)), 'rosa': ((246, 170, 160), (255, 255, 255)), 'creme': ((240, 232, 226), (40, 32, 28)),
}


def eh_emoji(ch):
    o = ord(ch)
    return o >= 0x1F000 or 0x2600 <= o <= 0x27BF or o in (0x2B50, 0x2728)


def medir(txt, f, fe_px):
    w = 0
    for ch in txt:
        if eh_emoji(ch):
            w += int(fe_px * 1.1)
        elif ch != '️':
            w += f.getlength(ch)
    return w


def quebrar(txt, f, fe_px, maxw):
    if ' // ' in txt:  # quebra escolhida à mão
        return [l for parte in txt.split(' // ') for l in quebrar(parte, f, fe_px, maxw)]
    linhas, atual = [], ''
    for p in txt.split(' '):
        t = (atual + ' ' + p).strip()
        if medir(t, f, fe_px) <= maxw or not atual:
            atual = t
        else:
            linhas.append(atual); atual = p
    linhas.append(atual)
    return linhas


def escrever(img, xy, txt, f, cor, fe_px, asc):
    d = ImageDraw.Draw(img); x, y = xy
    fe = None
    for ch in txt:
        if ch == '️':
            continue
        if eh_emoji(ch):
            if fe is None:
                fe = ImageFont.truetype(EMOJI, 109)
            e = Image.new('RGBA', (136, 128), (0, 0, 0, 0))
            ImageDraw.Draw(e).text((0, 0), ch, font=fe, embedded_color=True)
            e = e.crop(e.getbbox() or (0, 0, 1, 1)).resize((fe_px, fe_px), Image.LANCZOS)
            img.alpha_composite(e, (int(x + fe_px * 0.05), int(y + asc - fe_px * 0.92)))
            x += int(fe_px * 1.1)
        else:
            d.text((x, y), ch, font=f, fill=cor); x += f.getlength(ch)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('foto'); ap.add_argument('saida')
    ap.add_argument('--caixa', action='append', required=True)
    ap.add_argument('--topo', type=float, default=0.46)
    ap.add_argument('--tamanho', type=float, default=0.043)
    a = ap.parse_args()
    im = Image.open(a.foto).convert('RGBA'); W, H = im.size
    px = max(12, int(W * a.tamanho)); f = ImageFont.truetype(FONTE, px); fe_px = int(px * 1.0)
    asc, desc = f.getmetrics(); lh = int((asc + desc) * 1.08)
    padx, pady = int(px * 0.42), int(px * 0.30)
    maxw = int(W * 0.84) - 2 * padx
    y = int(H * a.topo); blocos = []
    for c in a.caixa:
        cor, txt = c.split('|', 1) if '|' in c else ('branco', c)
        if cor not in CORES:
            sys.exit(f'ERRO: cor "{cor}" (use: {", ".join(CORES)})')
        ls = quebrar(txt, f, fe_px, maxw)
        larg = int(max(medir(l, f, fe_px) for l in ls)) + 2 * padx
        alt = lh * len(ls) + 2 * pady
        x0 = (W - larg) // 2
        blocos.append((cor, ls, x0, y, x0 + larg, y + alt)); y += alt + int(H * 0.008)
    esq = min(b[2] for b in blocos) / W; dir_ = max(b[4] for b in blocos) / W
    if esq < 0.08 or dir_ > 0.92:
        sys.exit(f'ERRO: o texto vai de {esq:.0%} a {dir_:.0%} da largura (tem de ficar entre 8% e 92%)')
    d = ImageDraw.Draw(im)
    for cor, ls, x0, y0, x1, y1 in blocos:
        d.rounded_rectangle((x0, y0, x1, y1), radius=int(px * 0.18), fill=CORES[cor][0] + (255,))
        for i, l in enumerate(ls):
            lx = x0 + (x1 - x0 - medir(l, f, fe_px)) / 2
            escrever(im, (lx, y0 + pady + i * lh), l, f, CORES[cor][1] + (255,), fe_px, asc)
    out = im.convert('RGB'); out.save(a.saida, quality=95)
    base, _ = os.path.splitext(a.saida)
    fim = blocos[-1][5] / H
    out.crop((0, max(0, blocos[0][3] - int(H * 0.04)), W, min(H, blocos[-1][5] + int(H * 0.10)))).save(base + '-recorte.jpg', quality=90)
    out.resize((390, int(390 * H / W))).save(base + '-celular.jpg', quality=90)
    print(f'ok {a.saida}: texto de {esq:.0%} a {dir_:.0%} da largura e de {blocos[0][3] / H:.1%} a {fim:.1%} da altura; '
          f'adesivo de link logo abaixo, a ~{fim + 0.02:.0%} da altura, no centro')


if __name__ == '__main__':
    main()
