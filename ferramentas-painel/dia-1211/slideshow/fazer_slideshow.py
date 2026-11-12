# Slideshow do Face das 13h de 12/11 (0 crédito): as imagens do desejo (chaves de casa e o casal) com headline e a chamada para o comentário.
# Estilo do story aprovado em 11/11 (texto_story.py, "agora sim, ficou top"): caixa creme quase opaca com sombra marrom suave,
# texto marrom-escuro em Poppins Medium e o trecho entre [colchetes] em Cormorant SemiBold Itálico terracota (pedido do aluno, 12/11 ~13h10:
# "o preto e vermelho com fundo branco tá muito básico").
# O aluno põe a música no CapCut. Uso: python3 -I ferramentas-painel/dia-1211/slideshow/fazer_slideshow.py saida.mp4
import re, sys, subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = pathlib.Path(__file__).resolve().parents[3]
FX = R / 'ferramentas-painel' / 'imagens-fixas'
FONTES = R / 'ferramentas-painel' / 'ferramentas' / 'fontes'
FP = ImageFont.truetype(str(FONTES / 'Poppins-Medium.ttf'), 56)
FC = ImageFont.truetype(str(FONTES / 'Cormorant-SemiBoldItalic.ttf'), 74)
CAIXA, TEXTO, DESTAQUE, SOMBRA = (246, 238, 228), (90, 58, 42), (160, 88, 58), (90, 58, 42)
W, H, FPS = 1080, 1920, 30
SLIDES = [  # (imagem, linhas com [destaque], segundos, topo da caixa em fração da altura, seta)
    ('nora46-DESEJO-3-casa.jpg', ['Will trying harder', 'bring you [the life]', '[you want?]'], 3.6, 0.085, False),
    ('nora46-DESEJO-2-casal.jpg', ["It's not about", "trying harder. It's about", 'being [ready to receive.]'], 4.0, 0.085, False),
    ('nora46-DESEJO-2-casal.jpg', ['Your [2027 reading]', 'is waiting for you:', 'link in the comments'], 3.6, 0.60, True),
]
FUSAO = 0.4


def partes(linha):
    return [(p, FC if i % 2 else FP, DESTAQUE if i % 2 else TEXTO) for i, p in enumerate(re.split(r'\[|\]', linha)) if p]


def camada(linhas, topo, seta):  # a caixa pronta, transparente em volta (desenhada uma vez por slide)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    ls = [partes(l) for l in linhas]
    wl = lambda l: sum(d.textlength(t, font=f) for t, f, _ in l)
    sz = 56; lh = int(sz * 1.5); padx, pady = int(sz * 0.8), int(sz * 0.6)
    bw = int(max(wl(l) for l in ls) + 2 * padx); bh = int(lh * len(ls) + 2 * pady - sz * 0.3)
    x0, y0 = (W - bw) // 2, int(H * topo)
    assert x0 >= W * 0.08, f'texto largo demais: {x0 / W:.3f}'
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 8, x0 + bw, y0 + bh + 8], radius=int(sz * 0.9), fill=SOMBRA + (80,))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(12)))
    bx = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(bx).rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=int(sz * 0.9), fill=CAIXA + (236,))
    im = Image.alpha_composite(im, bx); d = ImageDraw.Draw(im)
    y = y0 + pady - int(sz * 0.05)
    for l in ls:
        x = (W - wl(l)) / 2
        for t, f, c in l:
            d.text((x, y - (int(sz * 0.24) if f is FC else 0)), t, font=f, fill=c); x += d.textlength(t, font=f)
        y += lh
    if seta:  # uma seta fina terracota apontando para baixo (os comentários), no lugar do triângulo vermelho
        cx, ty = W // 2, y0 + bh + 26
        d.ellipse([cx - 34, ty, cx + 34, ty + 68], fill=CAIXA + (236,))
        d.line([(cx, ty + 16), (cx, ty + 50)], fill=DESTAQUE, width=6)
        d.line([(cx - 13, ty + 37), (cx, ty + 51), (cx + 13, ty + 37)], fill=DESTAQUE, width=6, joint='curve')
    return im


def fundo(img, t, dur, z0, z1):
    im = Image.open(FX / img).convert('RGB')
    esc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)
    z = z0 + (z1 - z0) * (t / dur)
    w, h = round(W / z), round(H / z)
    x = (im.width - w) // 2; y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h)).resize((W, H), Image.LANCZOS).convert('RGBA')


CAMADAS = [camada(l, topo, seta) for (_, l, _, topo, seta) in SLIDES]


def quadro(i, t):
    img, _, dur, _, _ = SLIDES[i]
    z0, z1 = [(1.0, 1.07), (1.07, 1.0), (1.0, 1.05)][i]
    return Image.alpha_composite(fundo(img, t, dur, z0, z1), CAMADAS[i]).convert('RGB')


def main(saida):
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-shortest',
           '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-c:a', 'aac', '-movflags', '+faststart', saida]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i, (img, linhas, dur, topo, seta) in enumerate(SLIDES):
        for k in range(round(dur * FPS)):
            t = k / FPS
            fr = quadro(i, t)
            if i + 1 < len(SLIDES) and t > dur - FUSAO:
                fr = Image.blend(fr, quadro(i + 1, 0), (t - (dur - FUSAO)) / FUSAO)
            p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()
    print('ok', saida)


if __name__ == '__main__':
    main(sys.argv[1])
