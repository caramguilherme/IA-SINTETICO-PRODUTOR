# Slideshow do Face das 13h de 12/11 (0 crédito): as imagens do desejo (chaves de casa e o casal) com headline e a faixa do comentário.
# O aluno põe a música no CapCut. Uso: python3 -I ferramentas-painel/dia-1211/slideshow/fazer_slideshow.py saida.mp4
import sys, subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont
R = pathlib.Path(__file__).resolve().parents[3]
FX = R / 'ferramentas-painel' / 'imagens-fixas'
FONTE = str(R / 'ferramentas-painel' / 'ferramentas' / 'fontes' / 'Poppins-Bold.ttf')
W, H, FPS = 1080, 1920, 30
VERM = (229, 57, 53)
SLIDES = [  # (imagem, linhas, segundos, linhas em vermelho)
    ('nora46-DESEJO-3-casa.jpg', ['Will trying harder', 'bring you the life', 'you want?'], 3.6, []),
    ('nora46-DESEJO-2-casal.jpg', ["It's not about", "trying harder. It's about", 'being ready to receive.'], 4.0, [2]),
    ('nora46-DESEJO-2-casal.jpg', ['Your 2027 reading:', 'link in the comments'], 3.6, [1]),
]
FUSAO = 0.4


def base(img, t, dur, z0, z1):
    im = Image.open(FX / img).convert('RGB')
    esc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)
    z = z0 + (z1 - z0) * (t / dur)
    w, h = round(W / z), round(H / z)
    x = (im.width - w) // 2; y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h)).resize((W, H), Image.LANCZOS)


def caixa(fr, linhas, verm, seta, ytop=0.085):
    d = ImageDraw.Draw(fr)
    f = ImageFont.truetype(FONTE, 60)
    alt = 78
    larg = max(d.textlength(l, font=f) for l in linhas)
    pad = 40
    bw = larg + 2 * pad; bh = alt * len(linhas) + 2 * pad - 10
    assert bw <= 0.84 * W, bw
    x0 = (W - bw) / 2; y0 = ytop * H
    sombra = Image.new('RGBA', fr.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(sombra)
    ds.rounded_rectangle((x0 + 6, y0 + 10, x0 + bw + 6, y0 + bh + 10), 34, fill=(0, 0, 0, 70))
    fr.paste(Image.alpha_composite(fr.convert('RGBA'), sombra).convert('RGB'))
    d = ImageDraw.Draw(fr)
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), 34, fill=(255, 255, 255))
    for i, l in enumerate(linhas):
        tw = d.textlength(l, font=f)
        d.text(((W - tw) / 2, y0 + pad - 8 + i * alt), l, font=f, fill=VERM if i in verm else (17, 17, 17))
    if seta:
        cx = W / 2; ty = y0 + bh + 30
        d.polygon([(cx - 46, ty), (cx + 46, ty), (cx, ty + 70)], fill=VERM, outline=(0, 0, 0))
    return fr


def quadro(i, t):
    img, linhas, dur, verm = SLIDES[i]
    z0, z1 = (1.0, 1.07) if i % 2 == 0 else (1.07, 1.0)
    if i == 2:
        z0, z1 = 1.0, 1.05
    return caixa(base(img, t, dur, z0, z1), linhas, verm, i == 2, 0.60 if i == 2 else 0.085)


def main(saida):
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-shortest',
           '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-c:a', 'aac', '-movflags', '+faststart', saida]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i, (img, linhas, dur, verm) in enumerate(SLIDES):
        n = round(dur * FPS)
        for k in range(n):
            t = k / FPS
            fr = quadro(i, t)
            if i + 1 < len(SLIDES) and t > dur - FUSAO:
                a = (t - (dur - FUSAO)) / FUSAO
                fr = Image.blend(fr, quadro(i + 1, 0), a)
            p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()
    print('ok', saida)


if __name__ == '__main__':
    main(sys.argv[1])
