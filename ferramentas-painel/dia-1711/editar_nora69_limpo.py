#!/usr/bin/env python3
"""nora69 no visual limpo da claire_mayaus (decisão do aluno, 17/11 16h45): sem caixa, legenda no estilo da automática
do Instagram (minúscula, branca, letra normal, a frase em pedaços, sem destaque), o 222 branco à direita dos ~15 s ao fim,
a seta vermelha fina embaixo à esquerda do "Tap my profile picture" ao fim, o flash branco entre o hook e a fala.

Também corta: os silêncios longos entre as frases (o montado veio com pausas de até 4 s) e a repetição do Flow no T13
("the start of this start of this"). O Face sai sem o T10, o T11 e o T12 (Clone R67), com a variação do Face
(espelho, cor, recorte, 1,1x, sem metadados; `variacao_face.py`) e o hook sem o texto queimado (o texto vai por cima, sem espelhar).

Uso: python3 -I editar_nora69_limpo.py <montado.mp4> <palavras.json> <cortes_silencio.json> <hook-sem-texto.mp4> <pasta-saida> insta|face
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'ferramentas'))
import variacao_face as VF  # noqa: E402

MONT, PAL, CORTES, HOOK_LIMPO, OUT, VER = sys.argv[1:7]
W, H = 1080, 1920
V0 = 0.083            # o vídeo do montado do CapCut começa em 0,083 s
FIM_HOOK = 6.916      # o T01 começa aqui no montado (corte de cena)
FONTE = '/usr/share/fonts/opentype/inter/Inter-Medium.otf'
dur_m = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', MONT],
                             capture_output=True, text=True).stdout)
ws = json.load(open(PAL, encoding='utf-8'))
cortes = [(a, b) for a, b, w1, w2 in json.load(open(CORTES)) if not w1.endswith(',')]  # pausa de vírgula fica
cortes.append((119.68, 120.37))  # T13: o 1º "start of this" (o Flow repetiu); fica "the start of this new phase"
if VER == 'face':
    cortes.append((86.64, 112.36))  # sem o T10, o T11 e o T12 (os selos e o "comment I believe")
cortes.sort()
# junta cortes sobrepostos
cj = []
for a, b in cortes:
    if cj and a <= cj[-1][1]: cj[-1] = (cj[-1][0], max(cj[-1][1], b))
    else: cj.append((a, b))
# trechos que ficam (tempo do montado)
keep, t = [], FIM_HOOK
for a, b in cj:
    if a > t: keep.append((t, a))
    t = max(t, b)
keep.append((t, dur_m))


def novo(tm):
    """tempo do montado -> tempo do vídeo final (o hook dura FIM_HOOK - V0 no Insta e o do arquivo limpo no Face)."""
    acc = HOOK_DUR
    for a, b in keep:
        if tm < a: return acc
        if tm <= b: return acc + (tm - a)
        acc += b - a
    return acc


# ---------- base (sem texto): um arquivo por trecho e o concat sem recodificar ----------
# (17/11: cortar os 21 trechos num filtro só, com trim, estourou a memória: cada trim guarda os quadros)
tmp = os.path.join(OUT, f'tmp-{VER}'); os.makedirs(tmp, exist_ok=True)
ENC = ['-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', '24',
       '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2']


def trecho(n, src, a, d, vf_extra='', fade_audio=True):
    p = os.path.join(tmp, f's{n:02d}.mp4')
    af = f'afade=t=in:d=0.012,afade=t=out:st={max(0, d - 0.012):.3f}:d=0.012' if fade_audio else 'anull'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{a:.3f}', '-i', src, '-t', f'{d:.3f}',
                    '-vf', f'scale={W}:{H},setsar=1,fps=24{vf_extra}', '-af', af, *ENC, p], check=True)
    return p


partes = []
if VER == 'insta':
    HOOK_DUR = FIM_HOOK - V0
    partes.append(trecho(0, MONT, V0, HOOK_DUR))
else:
    HOOK_DUR = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', HOOK_LIMPO],
                                    capture_output=True, text=True).stdout)
    partes.append(trecho(0, HOOK_LIMPO, 0, HOOK_DUR, f',fade=t=out:st={HOOK_DUR - 0.15:.3f}:d=0.15:color=white'))
for i, (a, b) in enumerate(keep):
    fl = ',fade=t=in:st=0:d=0.12:color=white' if i == 0 else ''  # o flash branco cobre o corte do hook para a fala
    partes.append(trecho(i + 1, MONT, a, b - a, fl))
lst = os.path.join(tmp, 'lista.txt')
open(lst, 'w').write(''.join(f"file '{p}'\n" for p in partes))
base = os.path.join(tmp, 'base.mp4')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', base], check=True)
dur_b = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base],
                             capture_output=True, text=True).stdout)

# ---------- legenda (pedaços da fala, como a automática do Instagram) ----------
def limpa(p):
    p = p.replace('St.', 'saint')
    return p.lower().strip('.,!?:;"')

words = []
for i, w in enumerate(ws):
    txt, a, b = w[0], w[1], w[2]
    if a < FIM_HOOK: continue
    if any(ca <= a and b <= cb + 0.05 for ca, cb in cj): continue  # palavra cortada
    if txt == '.10' and words: words[-1][0] += ':10'; words[-1][2] = novo(b); continue
    words.append([txt, novo(a), novo(b)])
chunks, cur = [], []
for w in words:
    cur.append(w)
    fim_frase = w[0].rstrip()[-1:] in '.!?'
    virg = w[0].rstrip()[-1:] in ',:' and len(cur) >= 3
    if fim_frase or virg or len(cur) >= 6:
        chunks.append(cur); cur = []
if cur: chunks.append(cur)
leg = []
for i, c in enumerate(chunks):
    a = c[0][1]; fim = c[-1][2] + 0.35
    if i + 1 < len(chunks): fim = min(fim, chunks[i + 1][0][1]) if chunks[i + 1][0][1] - c[-1][2] < 0.6 else fim
    leg.append((' '.join(limpa(x[0]) for x in c), a, min(fim, dur_b)))

f_leg = ImageFont.truetype(FONTE, 50)
f_num = ImageFont.truetype(FONTE, 46)


def camada(desenha):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    desenha(im)
    return im


def texto_sombra(im, xy, txt, f, anchor='mm', stroke=2):
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    ds.text((xy[0] + 2, xy[1] + 3), txt, font=f, fill=(0, 0, 0, 170), anchor=anchor)
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(3)))
    ImageDraw.Draw(im).text(xy, txt, font=f, fill='#FFFFFF', anchor=anchor, stroke_width=stroke, stroke_fill=(0, 0, 0, 110))


def png_leg(txt):
    def d(im):
        dr = ImageDraw.Draw(im)
        pal = txt.split(); linhas = [txt]
        if dr.textlength(txt, font=f_leg) > W * 0.78:
            for k in range(len(pal) // 2, len(pal)):
                l1, l2 = ' '.join(pal[:k]), ' '.join(pal[k:])
                if dr.textlength(l1, font=f_leg) <= W * 0.78: linhas = [l1, l2]
        y = H * 0.775 - (len(linhas) - 1) * 31
        for ln in linhas:
            texto_sombra(im, (W / 2, y), ln, f_leg); y += 62
    return camada(d)


def png_222():
    x = W * (0.20 if VER == 'face' else 0.80)
    return camada(lambda im: texto_sombra(im, (x, H * 0.17), '222', f_num))


def png_seta():
    def d(im):
        dr = ImageDraw.Draw(im)
        cx, y0, y1 = W * 0.105, H * 0.755, H * 0.875
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
        for g in (ds, dr):
            cor = (0, 0, 0, 90) if g is ds else (229, 23, 43, 255)
            o = 3 if g is ds else 0
            g.line([(cx + o, y0 + o), (cx + o, y1 - 30 + o)], fill=cor, width=13)
            g.polygon([(cx - 34 + o, y1 - 48 + o), (cx + 34 + o, y1 - 48 + o), (cx + o, y1 + o)], fill=cor)
            if g is ds: im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(3)))
    return camada(d)


hook_txt = None
if VER == 'face':  # o texto do hook vai por cima, sem espelhar
    hook_txt = os.path.join(AQUI, 'hook69-texto.png')

t_tap = next(w[1] for w in words if w[0].lower().startswith('tap'))
cam = [(png_222(), 15.0, dur_b), (png_seta(), t_tap, dur_b)] + [(png_leg(t), a, b) for t, a, b in leg]
args = ['ffmpeg', '-v', 'error', '-y', '-i', base]
filt, ult = [], '0:v'
if VER == 'face':
    filt.append(f'[0:v]{VF.filtro_variacao()}[vx]'); ult = 'vx'
lista = []
if hook_txt: lista.append((hook_txt, 0.0, HOOK_DUR - 0.05))
for i, (im, a, b) in enumerate(cam):
    p = os.path.join(tmp, f'c{i:03d}.png'); im.save(p); lista.append((p, a, b))
for i, (p, a, b) in enumerate(lista):
    args += ['-loop', '1', '-framerate', '24', '-t', f'{min(b + 0.1, dur_b):.3f}', '-i', p]
    filt.append(f"[{ult}][{i + 1}:v]overlay=0:0:enable='between(t,{a:.3f},{b:.3f})'[o{i}]"); ult = f'o{i}'
final = os.path.join(OUT, 'nora69-final' + ('-FACE' if VER == 'face' else '') + '.mp4')
if VER == 'face':
    filt.append(f'[{ult}]setpts=PTS/{VF.VEL}[vf];[0:a]atempo={VF.VEL}[af]'); vm, am, extra = '[vf]', '[af]', VF.LIMPA
else:
    vm, am, extra = f'[{ult}]', '0:a', []
args += ['-filter_complex', ';'.join(filt), '-map', vm, '-map', am, '-c:v', 'libx264', '-crf', '21', '-preset', 'medium',
         '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', *extra, '-movflags', '+faststart', '-shortest', final]
subprocess.run(args, check=True)
json.dump({'keep': keep, 'cortes': cj, 'legenda': leg, 't_tap': t_tap, 'hook_dur': HOOK_DUR, 'dur_base': dur_b},
          open(os.path.join(OUT, f'mapa-{VER}.json'), 'w'), ensure_ascii=False, indent=1)
print('ok', final, f'base {dur_b:.2f}s', f'{len(leg)} pedaços de legenda', f'seta em {t_tap:.2f}s')
