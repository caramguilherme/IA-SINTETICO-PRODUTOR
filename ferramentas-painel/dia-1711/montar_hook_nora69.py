"""Hook do nora69 (modelo do v2 da claire_mayaus): 6 tomadas alternando aberto e close, ~6,7 s,
a frase no alto sem caixa (branca, contorno fino), o som do ambiente de cada clipe."""
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
SRC, OUT, EMOJI = sys.argv[1], sys.argv[2], sys.argv[3]
FONTE = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
W, H = 1080, 1920
clip = lambda k: [os.path.join(SRC, f) for f in os.listdir(SRC) if f.startswith(f"d1711-PRE-carro-{k}")][0]
SEG = [("1-pote", 0.50, 1.80),   # aberto: abre o pote
       ("2-canela", 0.00, 1.00), # close: a canela caindo embaixo do tapete
       ("1-pote", 3.00, 3.92),   # aberto: mexe no tapete
       ("2-canela", 1.90, 2.90), # close: o tapete no lugar, a mão ajeita
       ("3-entra", 0.25, 1.70),  # aberto: entra na picape
       ("3-entra", 2.50, 3.50)]  # dentro: põe o cinto
# o texto do hook (2 linhas, como o dela)
linhas = ["When the money arrives Don't", "tell anyone what you've done"]
f = ImageFont.truetype(FONTE, 64)
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
emo = Image.open(EMOJI).convert("RGBA").resize((70, 70), Image.LANCZOS)
y = int(H * 0.125)
for i, t in enumerate(linhas):
    tw = d.textlength(t, font=f) + (82 if i == 1 else 0)
    x = (W - tw) / 2
    # sombra suave + contorno fino, como o texto do Instagram
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    ds.text((x + 3, y + 4), t, font=f, fill=(0, 0, 0, 150))
    img = Image.alpha_composite(img, sh.filter(ImageFilter.GaussianBlur(4)))
    d = ImageDraw.Draw(img)
    d.text((x, y), t, font=f, fill="#FFFFFF", stroke_width=3, stroke_fill=(20, 20, 20, 255))
    if i == 1:
        img.alpha_composite(emo, (int(x + d.textlength(t, font=f) + 12), y - 2))
    y += 84
txt = os.path.join(os.path.dirname(OUT), "hook69-texto.png"); img.save(txt)
# corta cada tomada (vídeo 1080x1920 30 fps, áudio 48 kHz com 15 ms de fade nas pontas)
parts = []
for n, (k, a, b) in enumerate(SEG):
    p = os.path.join(os.path.dirname(OUT), f"seg{n}.mp4"); dur = b - a
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a}", "-t", f"{dur}", "-i", clip(k),
        "-vf", f"scale={W}:{H},fps=30,setsar=1", "-af", f"aresample=48000,afade=t=in:d=0.015,afade=t=out:st={dur-0.015:.3f}:d=0.015",
        "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", p], check=True)
    parts.append(p)
lst = os.path.join(os.path.dirname(OUT), "lista.txt")
open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
cru = os.path.join(os.path.dirname(OUT), "hook69-sem-texto.mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", cru], check=True)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", cru], capture_output=True, text=True).stdout)
# o texto do hook do começo ao fim + o flash branco nos últimos 0,15 s (prévia; no final o flash cobre o corte)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", cru, "-i", txt, "-filter_complex",
    f"[0:v][1:v]overlay=0:0,fade=t=out:st={dur-0.15:.3f}:d=0.15:color=white[v]", "-map", "[v]", "-map", "0:a",
    "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "copy", OUT], check=True)
print("hook:", round(dur, 2), "s ->", OUT)
