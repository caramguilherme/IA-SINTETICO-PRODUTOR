import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
D = sys.argv[1]
src = Image.open(f'{D}/capa-gpt.webp').convert('RGB')
W, H = 1640, 624
y0 = 300
crop = src.crop((0, y0, 1536, y0 + round(1536 * H / W)))
im = crop.resize((W, H), Image.LANCZOS).convert('RGBA')
serif = ImageFont.truetype(f'{D}/Cormorant-SemiBoldItalic.ttf', 58)
sans = ImageFont.truetype(f'{D}/Poppins-Medium.ttf', 22)
l1 = 'If this found you, it was meant to.'
l2a, l2b = 'MANIFESTATION', 'LOVE, ABUNDANCE & NEW BEGINNINGS'
cx, cy = 690, 245
lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
# sombra suave atrás do texto
sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
ds.text((cx + 2, cy + 3), l1, font=serif, anchor='mm', fill=(0, 0, 0, 200))
w2 = d.textlength(l2a, font=sans) + 40 + d.textlength(l2b, font=sans)
ds.text((cx - w2 / 2 + 2, cy + 56 + 2), l2a, font=sans, anchor='lm', fill=(0, 0, 0, 200))
ds.text((cx - w2 / 2 + d.textlength(l2a, font=sans) + 40 + 2, cy + 56 + 2), l2b, font=sans, anchor='lm', fill=(0, 0, 0, 200))
sh = sh.filter(ImageFilter.GaussianBlur(6))
d.text((cx, cy), l1, font=serif, anchor='mm', fill='#F3EAD7')
x = cx - w2 / 2; y = cy + 56
gold = '#D9B45E'
d.text((x, y), l2a, font=sans, anchor='lm', fill=gold)
sx = x + d.textlength(l2a, font=sans) + 20; r = 9; ri = 2.6
d.polygon([(sx, y - r), (sx + ri, y - ri), (sx + r, y), (sx + ri, y + ri), (sx, y + r), (sx - ri, y + ri), (sx - r, y), (sx - ri, y - ri)], fill=gold)
d.text((sx + 20, y), l2b, font=sans, anchor='lm', fill=gold)
out = Image.alpha_composite(Image.alpha_composite(im, sh), lay).convert('RGB')
out.save(f'{D}/nora-capa-face-1640x624.jpg', quality=95)
# conferência: área do celular (640x360 = 16% a 84% da largura) e canto da foto de perfil
chk = out.copy(); c = ImageDraw.Draw(chk)
mx0 = (W - H * 640 / 360) / 2
c.rectangle([mx0, 0, W - mx0, H - 1], outline='red', width=3)
c.ellipse([30, H - 150, 230, H + 50], outline='cyan', width=3)
chk.save(f'{D}/conferencia.jpg', quality=85)
mob = out.crop((int(mx0), 0, int(W - mx0), H)).resize((640, 360), Image.LANCZOS)
mob.save(f'{D}/previa-celular-640x360.jpg', quality=90)
print('ok', w2, mx0)
