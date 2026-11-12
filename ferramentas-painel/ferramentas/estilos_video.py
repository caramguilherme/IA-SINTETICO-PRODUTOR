#!/usr/bin/env python3
"""Estilos visuais dos textos da Nora (pedido do aluno, 12/11/2026: "a caixa branca com preto e vermelho não é pra ser fixa;
temos que variar, testar, deixar a edição mais bonita, com cores e estilos que ornam com o cenário, a roupa e o fundo").

Cada estilo define a caixa do topo, a faixa do CTA, a legenda, os números, a seta e a borda das imagens.
O editar_video.py lê o estilo pelo nome ("estilo": "creme-terracota" no spec) ou um dict com os campos a trocar.

Uso para escolher (da raiz do repositório):
  python3 -I ferramentas-painel/ferramentas/estilos_video.py quadro.jpg [--ultimo NOME]
  -> tira a paleta do quadro (fundo, roupa, pele), mede o contraste de cada estilo sobre ele e sugere os 3 que mais combinam,
     sem repetir o --ultimo (o estilo do post anterior na mesma rede). Também imprime um estilo "sob-medida" tirado da paleta.
  python3 -I ferramentas-painel/ferramentas/estilos_video.py --amostra quadro.jpg saida.jpg ESTILO [ESTILO...]
  -> desenha a caixa do topo, uma legenda e a faixa do CTA de cada estilo sobre o quadro, lado a lado, para conferir antes.
"""
import argparse, colorsys, copy, json, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTES = {'bold': 'Poppins-Bold.ttf', 'medium': 'Poppins-Medium.ttf', 'serif_it': 'Cormorant-SemiBoldItalic.ttf'}

# fundo da caixa: [r, g, b, alfa]; cores em hex. "destaque_fonte": a fonte do trecho entre [colchetes] na caixa.
BASE = {
    'caixa': {'fundo': [255, 255, 255, 255], 'texto': '#000000', 'destaque': '#E53935', 'fonte': 'bold', 'destaque_fonte': 'bold',
              'raio': 16, 'sombra': None},
    'legenda': {'fonte': 'bold', 'cor': '#FFFFFF', 'contorno': '#000000', 'destaque': '#FFD21F'},
    'numeros': {'contorno': '#000000', 'sombra': '#000000'},
    'seta': {'cor': '#E53935', 'contorno': '#000000'},
    'imagem': {'borda': '#FFFFFF'},
    'tom': 'claro',  # para o seletor: claro (caixa clara) ou escuro
}
ESTILOS = {
    # o de sempre até 12/11: fica como UMA opção, não como regra
    'branco-classico': {},
    # o do story aprovado em 11/11: creme, marrom e terracota (cenas quentes, madeira, bege, luz dourada)
    'creme-terracota': {'caixa': {'fundo': [246, 238, 228, 236], 'texto': '#5A3A2A', 'destaque': '#A0583A', 'fonte': 'medium', 'destaque_fonte': 'serif_it',
                                  'raio': 26, 'sombra': '#5A3A2A'},
                        'legenda': {'cor': '#FFF8F0', 'contorno': '#3B2418', 'destaque': '#F2C98A'},
                        'numeros': {'contorno': '#3B2418', 'sombra': '#3B2418'}, 'seta': {'cor': '#A0583A', 'contorno': '#3B2418'},
                        'imagem': {'borda': '#F6EEE4'}},
    # neutro frio para cinza, preto e parede clara (o escritório da manha1111: regata preta, moletom cinza)
    'nevoa-taupe': {'caixa': {'fundo': [242, 240, 236, 236], 'texto': '#2E2C2B', 'destaque': '#8A6A55', 'fonte': 'medium', 'destaque_fonte': 'serif_it',
                              'raio': 24, 'sombra': '#2E2C2B'},
                    'legenda': {'cor': '#FFFFFF', 'contorno': '#2A2725', 'destaque': '#E9D3B8'},
                    'numeros': {'contorno': '#2A2725', 'sombra': '#2A2725'}, 'seta': {'cor': '#8A6A55', 'contorno': '#2A2725'},
                    'imagem': {'borda': '#F2F0EC'}},
    # noite com abajur: caixa escura translúcida, texto creme, destaque dourado
    'noite-dourado': {'caixa': {'fundo': [36, 26, 24, 205], 'texto': '#F6EEE4', 'destaque': '#E8B96A', 'fonte': 'medium', 'destaque_fonte': 'serif_it',
                                'raio': 26, 'sombra': '#000000'},
                      'legenda': {'cor': '#FFF6E8', 'contorno': '#1E1512', 'destaque': '#E8B96A'},
                      'numeros': {'contorno': '#1E1512', 'sombra': '#000000'}, 'seta': {'cor': '#E8B96A', 'contorno': '#1E1512'},
                      'imagem': {'borda': '#2A1E1B'}, 'tom': 'escuro'},
    # verdes, plantas, roupa verde (a cena verde do kit)
    'salvia-creme': {'caixa': {'fundo': [238, 241, 230, 236], 'texto': '#2F3B2C', 'destaque': '#5E7D50', 'fonte': 'medium', 'destaque_fonte': 'serif_it',
                               'raio': 24, 'sombra': '#2F3B2C'},
                     'legenda': {'cor': '#FFFFFF', 'contorno': '#1F2A1D', 'destaque': '#D6E5B8'},
                     'numeros': {'contorno': '#1F2A1D', 'sombra': '#1F2A1D'}, 'seta': {'cor': '#5E7D50', 'contorno': '#1F2A1D'},
                     'imagem': {'borda': '#EEF1E6'}},
    # roxos, céu ao entardecer, cristais, lavanda (POV de amor, cenas místicas)
    'lavanda-ameixa': {'caixa': {'fundo': [243, 237, 246, 236], 'texto': '#3A2A44', 'destaque': '#7D5A9B', 'fonte': 'medium', 'destaque_fonte': 'serif_it',
                                 'raio': 26, 'sombra': '#3A2A44'},
                       'legenda': {'cor': '#FFFFFF', 'contorno': '#2A1E33', 'destaque': '#E3CCF2'},
                       'numeros': {'contorno': '#2A1E33', 'sombra': '#2A1E33'}, 'seta': {'cor': '#7D5A9B', 'contorno': '#2A1E33'},
                       'imagem': {'borda': '#F3EDF6'}},
    # areia e rosa queimado (pele quente, rosa, pôr do sol)
    'areia-rose': {'caixa': {'fundo': [248, 236, 230, 236], 'texto': '#4A2E2B', 'destaque': '#B4646A', 'fonte': 'medium', 'destaque_fonte': 'serif_it',
                             'raio': 26, 'sombra': '#4A2E2B'},
                   'legenda': {'cor': '#FFFFFF', 'contorno': '#3A2220', 'destaque': '#F7C9C2'},
                   'numeros': {'contorno': '#3A2220', 'sombra': '#3A2220'}, 'seta': {'cor': '#B4646A', 'contorno': '#3A2220'},
                   'imagem': {'borda': '#F8ECE6'}},
    # sem caixa: letra branca com sombra suave (o "visual limpo" da Soma, 10/11), destaque em itálico dourado claro
    'limpo-branco': {'caixa': {'fundo': [0, 0, 0, 0], 'texto': '#FFFFFF', 'destaque': '#F6DDB0', 'fonte': 'bold', 'destaque_fonte': 'serif_it',
                               'raio': 0, 'sombra': '#000000', 'contorno': '#1A1A1A'},
                     'legenda': {'cor': '#FFFFFF', 'contorno': '#111111', 'destaque': '#F6DDB0'},
                     'numeros': {'contorno': '#111111', 'sombra': '#000000'}, 'seta': {'cor': '#FFFFFF', 'contorno': '#111111'},
                     'imagem': {'borda': '#FFFFFF'}, 'tom': 'escuro'},
}
# a paleta "de referência" de cada estilo, para medir quanto ele combina com a cena
REF = {'branco-classico': ['#FFFFFF', '#000000', '#E53935'], 'creme-terracota': ['#F6EEE4', '#C9A27E', '#A0583A', '#5A3A2A'],
       'nevoa-taupe': ['#F2F0EC', '#9A9A9A', '#2E2C2B', '#8A6A55'], 'noite-dourado': ['#241A18', '#6B4A2E', '#E8B96A', '#F6EEE4'],
       'salvia-creme': ['#EEF1E6', '#8FA67E', '#5E7D50', '#2F3B2C'], 'lavanda-ameixa': ['#F3EDF6', '#B49BC8', '#7D5A9B', '#3A2A44'],
       'areia-rose': ['#F8ECE6', '#D9A79C', '#B4646A', '#4A2E2B'], 'limpo-branco': ['#FFFFFF', '#808080', '#202020']}


def mescla(a, b):
    out = copy.deepcopy(a)
    for k, v in (b or {}).items():
        out[k] = mescla(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def tema(est):
    """est: nome, dict ou None -> estilo completo."""
    if est is None:
        return copy.deepcopy(BASE)
    if isinstance(est, str):
        return mescla(BASE, ESTILOS[est])
    base = mescla(BASE, ESTILOS.get(est.get('base', 'branco-classico'), {}))
    return mescla(base, {k: v for k, v in est.items() if k != 'base'})


def fonte(nome, px):
    return ImageFont.truetype(os.path.join(AQUI, 'fontes', FONTES[nome]), max(8, int(round(px))))


def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(c):
    def ch(v):
        v /= 255; return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = c[:3]; return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contraste(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + 0.05) / (lb + 0.05)


def paleta(arq, n=6):
    im = Image.open(arq).convert('RGB').resize((90, 160))
    q = im.quantize(colors=n, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[:n * 3]; cont = sorted(q.getcolors(), reverse=True)
    return [(c / (90 * 160), tuple(pal[i * 3:i * 3 + 3])) for c, i in cont]


def dist(a, b):
    ha, sa, va = colorsys.rgb_to_hsv(*[x / 255 for x in a]); hb, sb, vb = colorsys.rgb_to_hsv(*[x / 255 for x in b])
    dh = min(abs(ha - hb), 1 - abs(ha - hb)) * (0.3 + min(sa, sb))
    return dh * 2 + abs(sa - sb) + abs(va - vb) * 0.6


def nota(est, pal):
    ref = [hexrgb(h) for h in REF[est]]
    return sum(p * min(dist(c, r) for r in ref) for p, c in pal)


def sob_medida(pal):
    """um estilo tirado da própria cena: caixa no tom mais claro (clareado), texto no mais escuro (escurecido), destaque no mais saturado."""
    cores = [c for _, c in pal]
    claro = max(cores, key=lambda c: lum(c)); escuro = min(cores, key=lambda c: lum(c))
    sat = max(cores, key=lambda c: colorsys.rgb_to_hsv(*[x / 255 for x in c])[1])
    caixa = tuple(int(v * 0.3 + 255 * 0.7) for v in claro)
    texto = tuple(int(v * 0.35) for v in escuro)
    dest = sat
    while contraste(dest, caixa) < 3.0 and sum(dest) > 30:
        dest = tuple(int(v * 0.85) for v in dest)
    h = lambda c: '#%02X%02X%02X' % c
    return {'base': 'creme-terracota', 'caixa': {'fundo': list(caixa) + [236], 'texto': h(texto), 'destaque': h(dest), 'sombra': h(texto)},
            'legenda': {'contorno': h(texto)}, 'seta': {'cor': h(dest), 'contorno': h(texto)}, 'imagem': {'borda': h(caixa)}}


def amostra(arq, saida, nomes):
    base = Image.open(arq).convert('RGBA'); W, H = base.size; k = W / 720
    quadros = []
    for nm in nomes:
        t = tema(json.loads(nm) if nm.startswith('{') else nm)
        im = base.copy()
        im = desenhar_caixa(im, ['[THURSDAY, NOVEMBER 12TH]', 'if this year felt heavy,', 'this message is for you'], t, k, 0.13)
        im = desenhar_caixa(im, ['Tap my photo: your', '[2027 reading] is in my story'], t, k, 0.30)
        d = ImageDraw.Draw(im); f = fonte(t['legenda']['fonte'], 38 * k)
        x = W / 2; y = H * 0.72
        d.text((x, y), 'THE HARDEST PART', font=f, fill=t['legenda']['cor'], anchor='mm', stroke_width=int(4 * k), stroke_fill=t['legenda']['contorno'])
        d.text((x, y + 48 * k), 'IS OVER', font=f, fill=t['legenda']['destaque'], anchor='mm', stroke_width=int(4 * k), stroke_fill=t['legenda']['contorno'])
        d.text((W * 0.05, H * 0.03), nm[:24], font=fonte('bold', 22 * k), fill='#FFFFFF', stroke_width=2, stroke_fill='#000000')
        quadros.append(im.convert('RGB').resize((W // 2, H // 2)))
    out = Image.new('RGB', (sum(q.width for q in quadros) + 10 * (len(quadros) - 1), quadros[0].height), 'white')
    x = 0
    for q in quadros:
        out.paste(q, (x, 0)); x += q.width + 10
    out.save(saida, quality=88); print('ok', saida)


def desenhar_caixa(im, linhas, t, k, yfrac):
    """caixa do topo no estilo t (linhas com [destaque]); devolve a imagem. Usada pela amostra e pelo editar_video.py."""
    import re
    W, H = im.size; c = t['caixa']
    sz = 10 * 2.8 * k
    fp = fonte(c['fonte'], sz); fd = fonte(c['destaque_fonte'], sz * (1.25 if c['destaque_fonte'] == 'serif_it' else 1))
    d = ImageDraw.Draw(im)
    segs = [[(p, fd if i % 2 else fp, c['destaque'] if i % 2 else c['texto']) for i, p in enumerate(re.split(r'\[|\]', l)) if p] for l in linhas]
    wl = [sum(d.textlength(s, font=f) for s, f, _ in l) for l in segs]
    asc, desc = fp.getmetrics(); lh = int((asc + desc) * 1.15)
    padx, pady = int(20 * k), int(13 * k)
    bw, bh = max(wl) + 2 * padx, lh * len(segs) + 2 * pady
    x0, y0 = (W - bw) / 2, H * yfrac
    if c.get('sombra') and c['fundo'][3] > 0:
        sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 6 * k, x0 + bw, y0 + bh + 6 * k], radius=int(c['raio'] * k), fill=hexrgb(c['sombra']) + (80,))
        im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(8 * k)))
    if c['fundo'][3] > 0:
        bx = Image.new('RGBA', im.size, (0, 0, 0, 0))
        ImageDraw.Draw(bx).rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=int(c['raio'] * k), fill=tuple(c['fundo']))
        im = Image.alpha_composite(im, bx)
    d = ImageDraw.Draw(im)
    for i, l in enumerate(segs):
        x = (W - wl[i]) / 2; y = y0 + pady + lh * i + lh / 2
        for s, f, cor in l:
            kw = {}
            if c['fundo'][3] == 0:
                kw = dict(stroke_width=max(2, int(3 * k)), stroke_fill=c.get('contorno', '#000000'))
            d.text((x, y - (sz * 0.12 if f is fd and c['destaque_fonte'] == 'serif_it' else 0)), s, font=f, fill=cor, anchor='lm', **kw)
            x += d.textlength(s, font=f)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('quadro', nargs='?'); ap.add_argument('--ultimo', default='')
    ap.add_argument('--amostra', nargs='+', metavar=('QUADRO', 'SAIDA'))
    a = ap.parse_args()
    if a.amostra:
        amostra(a.amostra[0], a.amostra[1], a.amostra[2:] or ['creme-terracota', 'nevoa-taupe', 'noite-dourado']); return
    pal = paleta(a.quadro)
    print('paleta do quadro (fração · cor):', ', '.join(f'{p:.0%} ' + '#%02X%02X%02X' % c for p, c in pal))
    notas = sorted((nota(e, pal), e) for e in ESTILOS if e != a.ultimo)
    fundo_med = tuple(sum(p * c[i] for p, c in pal) for i in range(3))
    for n, e in notas[:3]:
        t = tema(e); c = t['caixa']
        cx = contraste(hexrgb(c['texto']), tuple(c['fundo'][:3])) if c['fundo'][3] else contraste(hexrgb(c['texto']), fundo_med)
        print(f'  {e:16s} combina {1 / (n + 0.05):.1f} · contraste do texto {cx:.1f}:1' + ('' if cx >= 4.5 else '  (BAIXO: só com contorno/sombra)'))
    print('sob-medida:', json.dumps(sob_medida(pal), ensure_ascii=False))


if __name__ == '__main__':
    main()
