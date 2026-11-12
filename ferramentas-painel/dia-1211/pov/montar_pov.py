# Fundo do POV narrado (nora61, 12/11/2026): as paisagens em tela cheia, com zoom lento alternado e fusão curta na troca,
# e a voz da Nora (só o áudio do vídeo cortado) por cima. Os textos, a legenda, a faixa e os sons entram depois pelo
# editar_video.py (spec com "estilo" e "sons"). O aluno põe só a música no CapCut no fim.
# Uso: python3 -I montar_pov.py --voz cortado.mp4 --imgs a.jpg b.jpg c.jpg d.jpg --trocas 7.1 14.3 21.0 --lead 1.5 --saida pov-base.mp4
#   --trocas: os segundos DA VOZ em que entra a próxima paisagem (o começo da frase seguinte); --lead: segundos só de paisagem antes da voz.
import argparse, subprocess
from PIL import Image
W, H, FPS, FUSAO = 1080, 1920, 24, 0.5
ap = argparse.ArgumentParser()
ap.add_argument('--voz', required=True); ap.add_argument('--imgs', nargs='+', required=True)
ap.add_argument('--trocas', nargs='*', type=float, default=[]); ap.add_argument('--lead', type=float, default=0.0)
ap.add_argument('--saida', required=True); ap.add_argument('--dur', type=float, default=None)
a = ap.parse_args()
dur_voz = a.dur or float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', a.voz], capture_output=True, text=True).stdout)
total = a.lead + dur_voz
cortes = [0.0] + [a.lead + t for t in a.trocas] + [total]
assert len(cortes) - 1 == len(a.imgs), 'uma paisagem por trecho: trocas = paisagens - 1'
fontes = []
for p in a.imgs:  # cobre a tela 9:16 com uma folga para o zoom
    im = Image.open(p).convert('RGB'); esc = max(W / im.width, H / im.height) * 1.0
    fontes.append(im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS))
def quadro(i, t):  # t: segundos desde o começo do trecho i; zoom de 1,00 a 1,08 (pares) ou 1,08 a 1,00 (ímpares)
    d = cortes[i + 1] - cortes[i] + FUSAO; f = min(1.0, t / d)
    z = 1.0 + 0.08 * (f if i % 2 == 0 else 1 - f)
    im = fontes[i]; w, h = round(W / z), round(H / z)
    x = (im.width - w) // 2; y = round((im.height - h) * 0.55)
    return im.crop((x, y, x + w, y + h)).resize((W, H), Image.BILINEAR)
cmd = ['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
       '-i', a.voz, '-filter_complex', f'[1:a]adelay={int(a.lead * 1000)}:all=1,apad[a]', '-map', '0:v', '-map', '[a]', '-t', f'{total:.3f}',
       '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', a.saida]
pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
n = round(total * FPS)
for k in range(n):
    t = k / FPS
    i = max(j for j in range(len(a.imgs)) if cortes[j] <= t)
    fr = quadro(i, t - cortes[i])
    if i + 1 < len(a.imgs) and t > cortes[i + 1] - FUSAO:  # fusão para a próxima
        fr = Image.blend(fr, quadro(i + 1, 0), (t - (cortes[i + 1] - FUSAO)) / FUSAO)
    pr.stdin.write(fr.tobytes())
pr.stdin.close(); pr.wait(); print('ok', a.saida, f'{total:.2f}s')
