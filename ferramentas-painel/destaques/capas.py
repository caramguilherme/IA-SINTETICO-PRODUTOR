import math, sys
from PIL import Image, ImageDraw
out = sys.argv[1]
W, H, K = 1080, 1920, 4
BG = (246, 238, 228); TC = (160, 88, 58)
def tela():
    im = Image.new('RGB', (W * K, H * K), BG); return im, ImageDraw.Draw(im)
cx, cy = W * K // 2, H * K // 2
def salvar(im, nome):
    im.resize((W, H), Image.LANCZOS).save(f'{out}/{nome}.jpg', quality=95)
# lua crescente
im, d = tela(); r = 230 * K
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TC)
o = int(r * 0.42)
d.ellipse([cx - r + o + 40 * K, cy - r - 30 * K, cx + r + o + 40 * K, cy + r - 30 * K], fill=BG)
salvar(im, 'capa-about-me')
# estrela de 5 pontas
im, d = tela(); R, r2 = 250 * K, 105 * K
pts = []
for i in range(10):
    a = -math.pi / 2 + i * math.pi / 5; rr = R if i % 2 == 0 else r2
    pts.append((cx + rr * math.cos(a), cy + 20 * K + rr * math.sin(a)))
d.polygon(pts, fill=TC)
salvar(im, 'capa-reviews')
# brilho de 4 pontas + 1 pequeno
def brilho(d, x, y, R, f):
    pts = []
    for i in range(8):
        a = -math.pi / 2 + i * math.pi / 4; rr = R if i % 2 == 0 else R * f
        pts.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    d.polygon(pts, fill=TC)
im, d = tela()
brilho(d, cx - 30 * K, cy + 30 * K, 230 * K, 0.22)
brilho(d, cx + 170 * K, cy - 170 * K, 80 * K, 0.25)
salvar(im, 'capa-how-it-works')
print('ok')
