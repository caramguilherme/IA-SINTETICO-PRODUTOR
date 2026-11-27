#!/usr/bin/env python3
"""noracurto2611 (26/11), o desafio de pausar: a Nora atravessa o jardim e a pessoa tenta pausar com ela dentro do pontilhado.

Passo 1 (este script):
- acha no montado a entrada dela pela esquerda e a saída pela direita;
  - o clipe do Muse tem um pulo no 1º quadro: a imagem com ela no meio, que some no 3º; `LICOES`, 26/11 19h17;
- corta só esse trecho, acelera (VEL) e repete N vezes, emendando a saída pela direita com a entrada pela esquerda, sem pulo;
- grava o pontilhado no meio do caminho e a música do montado, do 0 em diante, com um fade curto no fim.

Passo 2 (`editar_video.py`, com a spec que este script grava):
- a caixa do topo (branca, preto, a palavra-chave em vermelho) o vídeo todo;
- nos quadros em que ela está dentro do pontilhado, a caixa troca pela mensagem de chegada e a seta grande aponta a foto do perfil;
- os 2 números brancos.

Uso: python3 -I editar_curto_2611.py <montado.mp4> <pasta-saida> [VEL=1.45] [N=3]
(1,45x e 3 passadas cabem nos 6 s de música do montado; "dentro" = o corpo inteiro, do 3º ao 97º percentil, dentro do pontilhado)
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

MONT, OUT = sys.argv[1], sys.argv[2]
VEL = float(sys.argv[3]) if len(sys.argv) > 3 else 1.45
N = int(sys.argv[4]) if len(sys.argv) > 4 else 3
W, H = 1080, 1920
# o pontilhado: x de 28% a 72%, y de 24% a 84% (ela vai de ~28% a ~80% da altura; medido no clipe de 26/11)
PX0, PX1, PY0, PY1 = 0.28, 0.72, 0.24, 0.84
TOPO = ['Can you stop me', 'inside the [line]?']
CERTO = ['You did it!', 'Your 2027 reading is in [my story]']
os.makedirs(OUT, exist_ok=True)


def sonda(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate:format=duration',
                        '-of', 'json', p], capture_output=True, text=True).stdout
    j = json.loads(r); a, b = j['streams'][0]['r_frame_rate'].split('/')
    return float(a) / float(b), float(j['format']['duration'])


fps, dur = sonda(MONT)
# 1) onde ela está em cada quadro (diferença contra o jardim vazio, sem a bandeira da direita)
w, h = 176, 312
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', MONT, '-vf', f'scale={w}:{h}', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'],
                     capture_output=True).stdout
f = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(float)
n = len(f)
cnt = np.array([0] * n); cx = np.array([np.nan] * n); bx0 = np.ones(n); bx1 = np.zeros(n)
# o fundo: a mediana dos quadros vazios (0,1 a 0,6 s, depois do pulo e antes de ela entrar)
bg = np.median(f[int(0.1 * fps):int(0.6 * fps)], axis=0)
for i in range(n):
    d = np.abs(f[i] - bg) > 30
    d[:int(h * 0.22)] = False                       # o céu e as árvores mexem
    d[int(h * 0.40):int(h * 0.70), int(w * 0.80):] = False  # a bandeira do canteiro, à direita, mexe sozinha
    cnt[i] = d.sum()
    if cnt[i] > 150:
        xs = np.nonzero(d)[1]; cx[i] = xs.mean() / w; bx0[i], bx1[i] = np.percentile(xs, 3) / w, np.percentile(xs, 97) / w
ini = next(i for i in range(int(0.15 * fps), n) if cnt[i] > 150 and cx[i] < 0.12)
meio = next(i for i in range(ini, n) if cnt[i] > 150 and cx[i] > 0.70)
fim = next(i for i in range(meio, n) if cnt[i] < 120)        # saiu pela direita
dentro = [i for i in range(ini, fim) if cnt[i] > 150 and bx0[i] >= PX0 + 0.005 and bx1[i] <= PX1 - 0.005]
assert dentro == list(range(dentro[0], dentro[-1] + 1)), dentro
t_in, t_out = ini / fps, fim / fps
passo = (t_out - t_in) / VEL
total = passo * N
print(f'fps {fps:.2f}  entra {t_in:.2f}s  sai {t_out:.2f}s  dentro: quadros {dentro[0]}-{dentro[-1]}  passada {passo:.2f}s x{N} = {total:.2f}s')
if total > dur:
    print('AVISO: o vídeo passa da música do montado; baixar N ou subir VEL')

# 2) o pontilhado (traços brancos com sombra suave, cantos arredondados)
pont = Image.new('RGBA', (W, H), (0, 0, 0, 0))
x0, x1, y0, y1 = PX0 * W, PX1 * W, PY0 * H, PY1 * H


def tracos(dr, cor, larg, off=0):
    dash, gap = 34, 22
    for (ax, ay, bx, by) in [(x0, y0, x1, y0), (x1, y0, x1, y1), (x1, y1, x0, y1), (x0, y1, x0, y0)]:
        L = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5; t = 0
        while t < L:
            t2 = min(L, t + dash)
            dr.line([(ax + (bx - ax) * t / L + off, ay + (by - ay) * t / L + off), (ax + (bx - ax) * t2 / L + off, ay + (by - ay) * t2 / L + off)],
                    fill=cor, width=larg)
            t += dash + gap


sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); tracos(ImageDraw.Draw(sh), (0, 0, 0, 120), 10, 2)
pont.alpha_composite(sh.filter(ImageFilter.GaussianBlur(3)))
tracos(ImageDraw.Draw(pont), (255, 255, 255, 255), 8)
p_pont = os.path.join(OUT, 'pontilhado.png'); pont.save(p_pont)

# 3) a base: o trecho acelerado, N vezes, com o pontilhado e a música do montado do 0 em diante
seg = os.path.join(OUT, 'seg.mp4')
subprocess.check_call(['ffmpeg', '-y', '-v', 'error', '-ss', f'{t_in:.4f}', '-to', f'{t_out:.4f}', '-i', MONT, '-an',
                       '-vf', f'setpts=(PTS-STARTPTS)/{VEL},scale={W}:{H},fps={fps:.4f}', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', seg])
lst = os.path.join(OUT, 'lista.txt'); open(lst, 'w').write(''.join(f"file '{seg}'\n" for _ in range(N)))
base = os.path.join(OUT, 'base.mp4')
subprocess.check_call(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-i', MONT, '-loop', '1', '-i', p_pont,
                       '-filter_complex', f"[0:v][2:v]overlay=0:0:shortest=1,format=yuv420p[v];[1:a]atrim=0:{total:.3f},afade=t=out:st={max(0, total - 0.3):.3f}:d=0.3[a]",
                       '-map', '[v]', '-map', '[a]', '-t', f'{total:.3f}', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-c:a', 'aac', '-b:a', '192k', base])

# 4) as janelas "dentro" no tempo do vídeo final
jan = []
for p in range(N):
    a = p * passo + (dentro[0] - ini) / fps / VEL
    b = p * passo + (dentro[-1] + 1 - ini) / fps / VEL
    jan.append((round(a, 3), round(b, 3)))
itens = []
t = 0.0
for a, b in jan:  # a caixa do topo fora das janelas
    if a > t: itens.append({'tipo': 'caixa', 'ini': round(t, 3), 'fim': a, 'x': 0, 'y': 500, 'tamanho': 11, 'linhas': TOPO})
    itens.append({'tipo': 'caixa', 'ini': a, 'fim': b, 'x': 0, 'y': 500, 'tamanho': 10, 'linhas': CERTO})
    itens.append({'tipo': 'seta', 'ini': a, 'fim': b, 'x': -285, 'y': -400, 'tamanho': 44})
    t = b
if total - t > 0.01: itens.append({'tipo': 'caixa', 'ini': round(t, 3), 'fim': round(total, 3), 'x': 0, 'y': 500, 'tamanho': 11, 'linhas': TOPO})
itens += [{'tipo': 'texto', 'ini': 0, 'fim': round(total, 3), 'x': -245, 'y': 330, 'tamanho': 13, 'texto': '222', 'cor': '#FFFFFF'},
          {'tipo': 'texto', 'ini': 0, 'fim': round(total, 3), 'x': 245, 'y': 330, 'tamanho': 14, 'texto': '11:11', 'cor': '#FFFFFF'}]
final = os.path.join(OUT, 'noracurto2611-final.mp4')
json.dump({'entrada': base, 'saida': final, 'crf': 19, 'preset': 'medium', 'estilo': 'alto-contraste', 'itens': itens},
          open(os.path.join(OUT, 'spec.json'), 'w'), ensure_ascii=False, indent=1)
json.dump({'t_in': t_in, 't_out': t_out, 'vel': VEL, 'n': N, 'passo': passo, 'total': total, 'dentro_quadros': dentro, 'janelas': jan},
          open(os.path.join(OUT, 'mapa.json'), 'w'), indent=1)
print('janelas (s):', jan)
print('ok', base, '->', os.path.join(OUT, 'spec.json'))
