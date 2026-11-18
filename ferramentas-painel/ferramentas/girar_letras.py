#!/usr/bin/env python3
"""Gira 180° as letras escritas em papéis brancos sobre a mesa (quando o Flow escreve virado para a avatar).

Criado em 18/11/2026 para a ini1811-IMG: o Nano Banana Pro escreveu as 10 iniciais de cabeça para baixo
para a câmera em 3 rodadas, e a edição no Flow não virou. Acha cada papel (mancha clara), acha a tinta
(traço escuro) dentro dele, apaga a tinta com a cor do papel em volta e desenha a mesma letra girada 180°
no mesmo centro, sem pintar por cima de pele (o dedo) nem fora do papel.
Uso (da raiz): python3 -I ferramentas-painel/ferramentas/girar_letras.py entrada.jpg saida.jpg --faixa 0.64 0.85
(--faixa: de onde a onde, em fração da altura, ficam os papéis.)
"""
import argparse
import numpy as np
from PIL import Image


def componentes(mask):
    h, w = mask.shape
    lab = np.zeros((h, w), np.int32); n = 0; out = []
    for y in range(h):
        for x in range(w):
            if mask[y, x] and not lab[y, x]:
                n += 1; pilha = [(y, x)]; lab[y, x] = n; ys = []; xs = []
                while pilha:
                    cy, cx = pilha.pop(); ys.append(cy); xs.append(cx)
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = n; pilha.append((ny, nx))
                out.append((n, min(ys), max(ys), min(xs), max(xs), len(ys)))
    return lab, out


def preencher(img, buraco, voltas=60):
    img = img.copy(); b = buraco.copy()
    for _ in range(voltas):
        if not b.any():
            break
        soma = np.zeros_like(img); cont = np.zeros(b.shape)
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
            vi = np.roll(np.roll(img, dy, 0), dx, 1); vb = np.roll(np.roll(b, dy, 0), dx, 1)
            ok = ~vb
            soma += vi * ok[..., None]; cont += ok
        novo = b & (cont > 0)
        img[novo] = soma[novo] / cont[novo][:, None]
        b = b & ~novo
    return img


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('entrada'); ap.add_argument('saida')
    ap.add_argument('--faixa', nargs=2, type=float, default=[0.64, 0.85])
    a = ap.parse_args()
    im = np.asarray(Image.open(a.entrada).convert('RGB')).astype(np.float64)
    H, W, _ = im.shape
    y0, y1 = int(H * a.faixa[0]), int(H * a.faixa[1])
    reg = im[y0:y1]
    lum = reg.mean(2)
    claro = lum > 200
    lab, comps = componentes(claro)
    papeis = sorted([c for c in comps if c[5] > 1500], key=lambda c: (round(c[1] / 60), c[3]))
    print(len(papeis), 'papéis achados')
    out = im.copy()
    for (n, ya, yb, xa, xb, area) in papeis:
        comp = lab[ya:yb + 1, xa:xb + 1] == n
        h, w = comp.shape
        # o que fica fora do papel: o que se alcança da borda da caixa sem passar pelo papel
        fora = np.zeros_like(comp); pilha = []
        for yy in range(h):
            for xx in (0, w - 1):
                if not comp[yy, xx] and not fora[yy, xx]:
                    fora[yy, xx] = True; pilha.append((yy, xx))
        for xx in range(w):
            for yy in (0, h - 1):
                if not comp[yy, xx] and not fora[yy, xx]:
                    fora[yy, xx] = True; pilha.append((yy, xx))
        while pilha:
            cy, cx = pilha.pop()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < h and 0 <= nx < w and not comp[ny, nx] and not fora[ny, nx]:
                    fora[ny, nx] = True; pilha.append((ny, nx))
        dentro = ~fora
        sub = reg[ya:yb + 1, xa:xb + 1]; sl = sub.mean(2)
        pele = (sub[..., 0] > sub[..., 2] + 35) & (sl > 80) & (sl < 205)  # o dedo (o papel com luz quente não conta)
        escuro = dentro & ~comp & ~pele
        # só os pedaços grandes de tinta (a letra); os furos do caderno são pequenos
        lab2, comps2 = componentes(escuro)
        tinta = np.zeros_like(escuro)
        for (k, a0, a1, b0, b1, ar) in comps2:
            if ar > 40 and (a1 - a0) > h * 0.18:
                tinta |= lab2 == k
        papel_lum = float(np.median(sl[comp]))
        tinta &= sl < papel_lum - 60  # só o traço escuro (sem o miolo branco do B, do D e do P)
        if tinta.sum() < 30:
            continue
        borda = tinta.copy()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
            borda |= np.roll(np.roll(tinta, dy, 0), dx, 1)
        borda &= dentro & ~pele
        papel_cor = np.median(sub[comp], axis=0)
        alfa = np.clip((papel_cor.mean() - sl) / max(1.0, papel_cor.mean() - np.percentile(sl[tinta], 10)), 0, 1) * borda
        ys, xs = np.nonzero(borda)
        ty0, ty1, tx0, tx1 = ys.min(), ys.max(), xs.min(), xs.max()
        limpo = preencher(sub, borda)
        caixa = alfa[ty0:ty1 + 1, tx0:tx1 + 1][::-1, ::-1]
        pode = (dentro & ~pele)[ty0:ty1 + 1, tx0:tx1 + 1]
        ca = caixa * pode
        cor_tinta = np.median(sub[tinta & (sl < np.percentile(sl[tinta], 40))], axis=0)
        alvo = limpo[ty0:ty1 + 1, tx0:tx1 + 1]
        limpo[ty0:ty1 + 1, tx0:tx1 + 1] = alvo * (1 - ca[..., None]) + cor_tinta * ca[..., None]
        bloco = out[y0 + ya:y0 + yb + 1, xa:xb + 1]
        bloco[dentro] = limpo[dentro]
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(a.saida, quality=95)
    print('ok', a.saida)


if __name__ == '__main__':
    main()
