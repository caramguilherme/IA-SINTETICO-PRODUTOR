#!/usr/bin/env python3
"""noracurto2611 (26/11), o desafio de pausar, refeito às ~21h20 na cópia do v07 e do v21 do Robert McKeaveney.

O aluno, sobre a 1ª versão (o retângulo pontilhado): "não é para fazer um quadrado pontilhado, é para fazer o pontilhado em volta do corpo dela… a
silhueta dela inteira… igual o vídeo que eu te mandei"; e a mensagem de quando acerta "não pode estar também no topo… tem que aparecer em outro
lugar, com mais destaque… uma fonte diferente, um amarelo".

O que o v07 e o v21 fazem (folhas em MATERIAIS-ROBERT-MCKEAVENEY/), item por item, e como vai na Nora:
- a silhueta: o contorno vermelho do corpo da pessoa num quadro só, parado na tela o vídeo todo, um pouco folgado → o contorno do corpo dela no
  quadro em que ela está no terço esquerdo (o espaço da direita fica para a mensagem, como no v07);
- o topo: "Only 1% can pause / At the right time!", branco com contorno preto, o "1%" em amarelo, sem caixa → igual;
- perto do quadro certo: "SOOOO CLOSE 😱 / 1 frame off...", inclinado, sobre o corpo (v21: "makes people try over and over again") → igual;
- no quadro certo: "YOU DID IT!" inclinado e a oferta ao lado do corpo, noutra fonte → "YOU DID IT! 🎉" em amarelo e "Your 2027 reading / is in my
  story 🔮" em serifa branca, inclinados, à direita dela, e a seta vermelha grande para a foto do perfil (a oferta da Nora é o story).

Passo único: lê os quadros do clipe do Muse (o vídeo), tira a silhueta pela diferença contra o jardim vazio, monta cada quadro e põe o áudio do
montado (a música que o aluno pôs no CapCut). O clipe tem um pulo no 1º quadro (LICOES, 26/11 19h17): a edição usa só a passada dela.

Uso: python3 -I editar_curto_2611.py <clipe-do-muse.mp4> <audio: o montado do CapCut, ou o próprio clipe> <pasta-saida> [VEL=2.0] [N=3]

26/11 ~21h40 (o aluno): mais rápida (2x) e a mensagem só no quadro em que ela encaixa de verdade ("1 milésimo antes, 1 milésimo depois, já não é para
aparecer"): o "YOU DID IT!" fica só no quadro-alvo, 1 quadro por passada (~0,04 s); a 2x, os quadros vizinhos mostrados são o alvo ±2, ±4 (com o "SOOOO CLOSE").
"""
import json, os, subprocess, sys
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

CLIPE, AUDIO, OUT = sys.argv[1:4]
VEL = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0   # 26/11 ~21h40 (o aluno): "achei muito devagar… tem que andar mais rápido para ficar mais difícil"
N = int(sys.argv[5]) if len(sys.argv) > 5 else 3
W, H = 1080, 1920
ALVO_X = 0.30          # o quadro-alvo: o centro do corpo dela perto de 30% da largura (o terço esquerdo)
VERMELHO = (229, 23, 43)
AMARELO = (255, 212, 0)
FONTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'ferramentas', 'fontes')
F_BOLD = os.path.join(FONTES, 'Poppins-Bold.ttf')
F_MED = os.path.join(FONTES, 'Poppins-Medium.ttf')
F_SERIF = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
F_EMOJI = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
os.makedirs(OUT, exist_ok=True)


def sonda(p):
    j = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate',
                                   '-of', 'json', p], capture_output=True, text=True).stdout)['streams'][0]
    a, b = j['r_frame_rate'].split('/')
    return j['width'], j['height'], float(a) / float(b)


cw, ch, fps = sonda(CLIPE)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', CLIPE, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, ch, cw, 3)
n = len(fr)

# 1) a máscara do corpo em cada quadro: a diferença contra o jardim vazio (entre o pulo do 1º quadro e a entrada dela)
bg = np.median(fr[int(0.12 * fps):int(0.6 * fps)], axis=0).astype(np.int16)


def mascara(i):
    d = np.abs(fr[i].astype(np.int16) - bg).max(axis=2)
    m = (d > 28).astype(np.uint8)
    m[:int(ch * 0.2)] = 0                                            # o céu e as copas mexem
    m[int(ch * 0.40):int(ch * 0.70), int(cw * 0.80):] = 0            # a bandeira do canteiro, à direita
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    k, lab, st, _ = cv2.connectedComponentsWithStats(m)
    if k < 2:
        return None
    j = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    if st[j, cv2.CC_STAT_AREA] < cw * ch * 0.004:
        return None
    m = (lab == j).astype(np.uint8)
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cheia = np.zeros_like(m); cv2.drawContours(cheia, cs, -1, 1, -1)   # sem buracos
    return cheia


ms = [mascara(i) for i in range(n)]
cx = [None if m is None else float(np.nonzero(m)[1].mean() / cw) for m in ms]
ini = next(i for i in range(int(0.15 * fps), n) if cx[i] is not None and cx[i] < 0.12)
depois = [i for i in range(ini + int(fps), n) if ms[i] is None]
fim = depois[0] if depois else n - 1
# o alvo: o corpo inteiro na tela, o centro perto do ALVO_X
cand = [i for i in range(ini, fim) if cx[i] is not None and np.nonzero(ms[i])[1].min() > cw * 0.02]
T = min(cand, key=lambda i: abs(cx[i] - ALVO_X))
mt = ms[T]


def iou(i):
    if ms[i] is None:
        return 0.0
    a, b = ms[i] > 0, mt > 0
    return float((a & b).sum() / (a | b).sum())


io = [iou(i) for i in range(n)]

# 2) a silhueta: o contorno da máscara do alvo, suavizado e um pouco folgado, em vermelho (como no v07 e no v21)
esc = max(W / cw, H / ch); rw, rh = int(round(cw * esc)), int(round(ch * esc)); ox, oy = (rw - W) // 2, (rh - H) // 2


def para_tela(img, interp=cv2.INTER_CUBIC):
    return cv2.resize(img, (rw, rh), interpolation=interp)[oy:oy + H, ox:ox + W]


mg = para_tela(mt.astype(np.float32), cv2.INTER_LINEAR)
mg = cv2.GaussianBlur(mg, (0, 0), 7) > 0.5
mg = cv2.dilate(mg.astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))   # justa: só o quadro certo encaixa (o aluno, 26/11 ~21h40)
cs, _ = cv2.findContours(mg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
c = max(cs, key=cv2.contourArea)
c = cv2.approxPolyDP(c, 1.5, True)
sil = np.zeros((H, W, 4), np.uint8)
cv2.polylines(sil, [c], True, (*VERMELHO, 255), 8, cv2.LINE_AA)
silh = Image.fromarray(sil, 'RGBA')
x0s, y0s, ws_, hs_ = cv2.boundingRect(c)


# 3) os textos
def eh_emoji(ch_):
    o = ord(ch_)
    return o >= 0x1F000 or 0x2600 <= o <= 0x27BF or o in (0x2B50, 0x2728)


_emo = {}


def emoji(ch_, px):
    if (ch_, px) not in _emo:
        fe = ImageFont.truetype(F_EMOJI, 109)
        e = Image.new('RGBA', (160, 160), (0, 0, 0, 0)); ImageDraw.Draw(e).text((0, 0), ch_, font=fe, embedded_color=True)
        _emo[(ch_, px)] = e.crop(e.getbbox()).resize((px, px), Image.LANCZOS)
    return _emo[(ch_, px)]


def linha(partes, contorno):
    """partes: [(texto, fonte, cor)]; devolve a imagem da linha (texto com contorno preto; emoji colorido)."""
    larg, alt = 0, 0
    for t, f, _ in partes:
        a, d = f.getmetrics(); alt = max(alt, a + d)
        for ch_ in t:
            larg += int(f.size * 1.05) if eh_emoji(ch_) else f.getlength(ch_)  # o emoji: 0,12 + 0,85 + 0,08 do tamanho
    pad = contorno + 6
    im = Image.new('RGBA', (int(larg) + 2 * pad, alt + 2 * pad), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    x = pad
    for t, f, cor in partes:
        a, _ = f.getmetrics()
        for ch_ in t:
            if eh_emoji(ch_):
                px = int(f.size * 0.85); x += int(f.size * 0.12)
                im.alpha_composite(emoji(ch_, px), (int(x), int(pad + a - px * 0.80))); x += px + int(f.size * 0.08)
            else:
                dr.text((x, pad), ch_, font=f, fill=cor, stroke_width=contorno, stroke_fill=(0, 0, 0)); x += f.getlength(ch_)
    return im


def bloco(linhas, gap=0, angulo=0):
    ims = [linha(p, cont) for p, cont in linhas]
    bw = max(i.width for i in ims); bh = sum(i.height for i in ims) + gap * (len(ims) - 1)
    b = Image.new('RGBA', (bw, bh), (0, 0, 0, 0)); y = 0
    for i in ims:
        b.alpha_composite(i, ((bw - i.width) // 2, y)); y += i.height + gap
    return b.rotate(angulo, resample=Image.BICUBIC, expand=True) if angulo else b


def camada(b, cx_, cy_):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); im.alpha_composite(b, (int(cx_ - b.width / 2), int(cy_ - b.height / 2)))
    return im


def fb(px):
    return ImageFont.truetype(F_BOLD, px)


def fs(px):
    return ImageFont.truetype(F_SERIF, px)


topo = camada(bloco([([('Only ', fb(70), 'white'), ('1%', fb(70), AMARELO), (' can pause', fb(70), 'white')], 5),
                     ([('at the right time!', fb(70), 'white')], 5)], gap=-18), W / 2, H * 0.135)
perto = camada(bloco([([('SOOOO CLOSE ', fb(74), 'white'), ('😱', fb(74), 'white')], 6),
                      ([('1 frame off...', ImageFont.truetype(F_MED, 46), 'white')], 4)], gap=-14, angulo=6),
               W * min(0.60, (x0s + ws_ * 0.5) / W + 0.14), y0s + hs_ * 0.40)
dir_x = (x0s + ws_ + W * 0.96) / 2                                     # o meio do espaço à direita da silhueta
certo = camada(bloco([([('YOU DID IT! ', fb(82), AMARELO), ('🎉', fb(82), 'white')], 7),
                      ([('Your 2027 reading', fs(50), 'white')], 5),
                      ([('is in ', fs(50), 'white'), ('my story', fs(50), AMARELO), (' 🔮', fs(50), 'white')], 5)], gap=-6, angulo=7),
               dir_x, H * 0.47)


def seta():  # a seta grande para a foto do perfil (a mesma do editar_simples_2311.py: x 10,5%, de 75,5% a 87,5% da altura)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    cx_, y0, y1 = W * 0.105, H * 0.755, H * 0.875
    dr.line([(cx_, y0), (cx_, y1 - 30)], fill=(*VERMELHO, 255), width=13)
    dr.polygon([(cx_ - 34, y1 - 48), (cx_ + 34, y1 - 48), (cx_, y1)], fill=(*VERMELHO, 255))
    return im


certo.alpha_composite(seta())
fixo = Image.new('RGBA', (W, H), (0, 0, 0, 0)); fixo.alpha_composite(silh); fixo.alpha_composite(topo)
CERTO_IOU = 0.88
certos = [i for i in range(n) if io[i] >= CERTO_IOU]
pertos = [i for i in range(n) if i not in certos and (io[i] >= 0.55 or abs(i - T) <= 5) and ms[i] is not None]

# 4) a sequência: N passadas a VEL, cada uma passando exatamente pelo quadro-alvo
seq = []
for _ in range(N):
    j0 = int(np.ceil((T - ini) / VEL)); j1 = int(np.floor((fim - T) / VEL))
    seq += [T + int(round(k * VEL)) for k in range(-j0, j1 + 1)]
seq = [min(max(i, ini), fim) for i in seq]
total = len(seq) / fps
print(f'fps {fps:.2f}  entra {ini / fps:.2f}s (q{ini})  sai {fim / fps:.2f}s (q{fim})  alvo q{T} (centro {cx[T]:.2f})  '
      f'certos {certos}  pertos {pertos[0]}-{pertos[-1]}  {N} passadas a {VEL}x = {total:.2f}s')
print('IoU em volta do alvo:', {i: round(io[i], 2) for i in range(T - 3, T + 4)})

# 5) o vídeo: cada quadro montado aqui, o áudio do montado do 0 em diante
saida = os.path.join(OUT, 'noracurto2611-final.mp4')
dur_a = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', AUDIO], capture_output=True, text=True).stdout)
if dur_a < total:
    print(f'AVISO: o áudio tem {dur_a:.2f}s e o vídeo {total:.2f}s')
enc = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', f'{fps}', '-i', '-', '-i', AUDIO,
                        '-filter_complex', f'[1:a]atrim=0:{total:.3f},afade=t=out:st={max(0, total - 0.25):.3f}:d=0.25[a]', '-map', '0:v', '-map', '[a]',
                        '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart',
                        '-shortest', saida], stdin=subprocess.PIPE)
marcas = []
for k, i in enumerate(seq):
    base = Image.fromarray(np.ascontiguousarray(para_tela(fr[i])), 'RGB').convert('RGBA')
    base.alpha_composite(fixo)
    if i in certos:
        base.alpha_composite(certo); marcas.append((k, 'certo'))
    elif i in pertos:
        base.alpha_composite(perto); marcas.append((k, 'perto'))
    enc.stdin.write(np.asarray(base.convert('RGB')).tobytes())
enc.stdin.close(); enc.wait()
certo_t = [round(k / fps, 3) for k, m in marcas if m == 'certo']
json.dump({'clipe': CLIPE, 'audio': AUDIO, 'fps': fps, 'ini': ini, 'fim': fim, 'alvo': T, 'certos': certos, 'pertos': pertos, 'vel': VEL, 'n': N,
           'total': total, 'seq': seq, 'certo_t': certo_t}, open(os.path.join(OUT, 'mapa.json'), 'w'), indent=1)
print('quadros certos no vídeo (s):', certo_t)
print('ok', saida)
