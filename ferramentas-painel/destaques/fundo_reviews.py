import sys
from PIL import Image, ImageDraw, ImageFilter
base, saida = sys.argv[1], sys.argv[2]
prints = sys.argv[3:]
W, H = 1080, 1920
im = Image.open(base).convert('RGB').resize((W, H))
im = im.filter(ImageFilter.GaussianBlur(28))
creme = Image.new('RGB', (W, H), (246, 238, 228))
im = Image.blend(im, creme, 0.55).convert('RGBA')
y = int(H * 0.20)
gap = int(H * 0.025)
for p in prints:
    pr = Image.open(p).convert('RGBA')
    w = int(W * 0.90); h = int(pr.height * w / pr.width)
    pr = pr.resize((w, h), Image.LANCZOS)
    pad = 20
    card = Image.new('RGBA', (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(card).rounded_rectangle([0, 0, w + 2 * pad - 1, h + 2 * pad - 1], radius=34, fill=(255, 255, 255, 255))
    card.paste(pr, (pad, pad), pr)
    x = (W - card.width) // 2
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([x, y + 8, x + card.width, y + card.height + 8], radius=34, fill=(90, 58, 42, 60))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(12)))
    im.paste(card, (x, y), card)
    print(p, 'y %.1f-%.1f%%' % (y / H * 100, (y + card.height) / H * 100))
    y += card.height + gap
im.convert('RGB').save(saida, quality=95)
