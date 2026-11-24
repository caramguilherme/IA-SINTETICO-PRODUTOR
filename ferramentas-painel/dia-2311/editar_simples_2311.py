#!/usr/bin/env python3
"""nora75 e nora76 (23/11), a partir do editar_simples_1911.py. Mudanças: sem hook (o <hook> pode ser "none"), sem flash branco,
e o "11:11✨" pequeno no alto à esquerda o vídeo todo (a cópia do m30 e do m61), desenhado aqui com a Inter + o Noto Color Emoji.
Na versão do Face sem a variação: rodar com "insta" e o cortes-extra do Face (o corpo é novo no Face).

Original: nora71 e nora72 (19/11) no estilo "simples", passo 1: o hook sem texto + o flash branco + a fala com os silêncios cortados
pelas palavras (pausa > 0,45 s; ~0,6 s depois da última palavra) + a legenda simples (Inter branca, contorno fino, sombra suave,
pedaços de até ~6 palavras, a caixa da fala normal). Na versão do Face, a variação do Face (espelho, matiz, 1,1x) entra antes da legenda.
O passo 2 (`editar_video.py` com a spec que este script grava) põe a caixa do topo, os 2 números, a faixa e a seta.
Base: `ferramentas-painel/dia-1711/editar_nora70_limpo.py` (o mesmo corte e a mesma legenda, sem os cortes do Face e sem os fixos).

Uso: python3 -I editar_simples_1911.py <montado.mp4> <palavras.json> <hook-sem-texto.mp4> <pasta-saida> insta|face <nome> [cortes-extra.json]
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'ferramentas'))
import variacao_face as VF  # noqa: E402

MONT, PAL, HOOK_LIMPO, OUT, VER, NOME = sys.argv[1:7]
EXTRA = json.load(open(sys.argv[7])) if len(sys.argv) > 7 else []
W, H = 1080, 1920
FIM_HOOK = 0.0        # o montado já começa no T01
FONTE = '/usr/share/fonts/opentype/inter/Inter-Medium.otf'
dur_m = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', MONT],
                             capture_output=True, text=True).stdout)
ws = json.load(open(PAL, encoding='utf-8'))
cortes = []
for w1, w2 in zip(ws, ws[1:]):  # silêncio longo entre palavras (a pausa de vírgula fica um pouco maior)
    lim = 0.60 if w1[0].endswith(',') else 0.45
    if w2[1] - w1[2] > lim: cortes.append((w1[2] + 0.12, w2[1] - 0.06))
if ws and ws[0][1] > 0.25: cortes.append((0.0, ws[0][1] - 0.10))  # silêncio antes da 1ª palavra
cortes += [tuple(c) for c in EXTRA]
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
# o fim: o Muse segue mexendo o corpo, a boca e suspirando depois da última palavra; fica só ~0,6 s depois dela
fim_m = min(dur_m, ws[-1][2] + 0.6) if ws else dur_m
keep.append((t, fim_m))


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
REUSA = os.environ.get('REUSAR_BASE') and os.path.exists(os.path.join(tmp, 'base.mp4'))
SEM_HOOK = HOOK_LIMPO == 'none'
HOOK_DUR = 0.0 if SEM_HOOK else float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', HOOK_LIMPO],
                                capture_output=True, text=True).stdout)
if not REUSA and not SEM_HOOK:
    partes.append(trecho(0, HOOK_LIMPO, 0, HOOK_DUR, f',fade=t=out:st={HOOK_DUR - 0.15:.3f}:d=0.15:color=white'))
for i, (a, b) in enumerate([] if REUSA else keep):
    fl = ',fade=t=in:st=0:d=0.12:color=white' if i == 0 and not SEM_HOOK else ''  # o flash branco cobre o corte do hook para a fala
    partes.append(trecho(i + 1, MONT, a, b - a, fl))
lst = os.path.join(tmp, 'lista.txt')
open(lst, 'w').write(''.join(f"file '{p}'\n" for p in partes))
base = os.path.join(tmp, 'base.mp4')
if not REUSA: subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', base], check=True)
dur_b = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base],
                             capture_output=True, text=True).stdout)

# ---------- legenda (pedaços da fala, como a automática do Instagram) ----------
def limpa(p):
    q = p.strip('.,!?:;"')
    if len(q) == 1 and q.isupper() and p.rstrip().endswith(','):  # as letras do nome (nora73): "A, J, M," ficam com a vírgula
        return q + ','
    return {'1111': '11:11', '11.11': '11:11', '11-11': '11:11'}.get(q, q)

words = []
for i, w in enumerate(ws):
    txt, a, b = w[0], w[1], w[2]
    if a < FIM_HOOK: continue
    if any(ca <= a and b <= cb + 0.05 for ca, cb in cj): continue  # palavra cortada
    if words and txt[:1] in '.:-' and txt[1:2].isdigit() and words[-1][0].isdigit():  # "10" ".10," -> "10:10," ("11" "-11" também)
        words[-1] = [words[-1][0] + ':' + txt[1:], words[-1][1], novo(b)]; continue
    words.append([txt, novo(a), novo(b)])
chunks, cur = [], []
for k, w in enumerate(words):
    cur.append(w)
    fim_frase = w[0].rstrip()[-1:] in '.!?'
    virg = w[0].rstrip()[-1:] in ',:' and len(cur) >= 3
    prox_fecha = k + 1 < len(words) and words[k + 1][0].rstrip()[-1:] in '.!?,' and len(cur) < 7  # não deixa 1 palavra sozinha
    if fim_frase or virg or (len(cur) >= 6 and not prox_fecha):
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
            # 23/11: as 2 linhas equilibradas (no nora75 sobrou 1 palavra sozinha embaixo: "dreamed / of", "faith and / money")
            ops = []
            for k in range(1, len(pal)):
                l1, l2 = ' '.join(pal[:k]), ' '.join(pal[k:])
                a1, a2 = dr.textlength(l1, font=f_leg), dr.textlength(l2, font=f_leg)
                if max(a1, a2) <= W * 0.78: ops.append((abs(a1 - a2), [l1, l2]))
            if ops: linhas = min(ops)[1]
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


t_tap = next((w[1] for i, w in enumerate(words) if w[0].lower().startswith('tap') and i + 1 < len(words)
              and words[i + 1][0].lower().startswith('my')), None)  # o "tap my profile picture"
if t_tap is None:  # 24/11: a versão do Face do nora77 em diante manda para o comentário ("Check the first comment below")
    t_tap = next(w[1] for i, w in enumerate(words) if w[0].lower().startswith('check') and i + 1 < len(words)
                 and words[i + 1][0].lower().startswith('the'))
t_g = next(w[2] for w in words if w[0].rstrip()[-1:] in '.!?')  # o fim da 1ª frase (o gancho)
f_1111 = ImageFont.truetype(FONTE, 44)
f_emo = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf', 109)


def png_1111(x_pct=0.18, y_pct=0.16):
    def d(im):
        dr = ImageDraw.Draw(im)
        tw = dr.textlength('11:11', font=f_1111); ew = 44
        x0 = W * x_pct - (tw + 8 + ew) / 2; y = H * y_pct
        texto_sombra(im, (x0, y), '11:11', f_1111, anchor='lm')
        e = Image.new('RGBA', (140, 140), (0, 0, 0, 0)); ImageDraw.Draw(e).text((0, 0), '\u2728', font=f_emo, embedded_color=True)
        e = e.crop(e.getbbox()).resize((ew, ew), Image.LANCZOS)
        im.alpha_composite(e, (int(x0 + tw + 8), int(y - ew / 2)))
    return camada(d)


# 24/11 (nora77): com a bandeira no quadro do alto à esquerda, o 11:11 vai para o alto à direita (X1111=0.82)
fixos = [(png_1111(float(os.environ.get('X1111', '0.18')), float(os.environ.get('Y1111', '0.16'))), 0.0, dur_b)]
args = ['ffmpeg', '-v', 'error', '-y', '-i', base]
filt, ult = [], '0:v'
if VER == 'face':
    filt.append(f'[0:v]{VF.filtro_variacao()}[vx]'); ult = 'vx'
# a legenda inteira numa camada só (concat de PNGs com a duração de cada pedaço; vazio transparente entre eles):
# com ~85 camadas separadas o render passava de 10 min
vazio = os.path.join(tmp, 'vazio.png'); Image.new('RGBA', (W, H), (0, 0, 0, 0)).save(vazio)
seq, t0 = [], 0.0
for i, (txt, a, b) in enumerate(sorted(leg, key=lambda x: x[1])):
    a = max(a, t0)
    if b <= a: continue
    if a > t0: seq.append((vazio, a - t0))
    pth = os.path.join(tmp, f'c{i:03d}.png'); png_leg(txt).save(pth); seq.append((pth, b - a)); t0 = b
if dur_b > t0: seq.append((vazio, dur_b - t0))
lst_leg = os.path.join(tmp, 'legenda.txt')
with open(lst_leg, 'w') as f:
    for pth, d in seq: f.write(f"file '{pth}'\nduration {d:.4f}\n")
    f.write(f"file '{seq[-1][0]}'\n")
args += ['-f', 'concat', '-safe', '0', '-i', lst_leg]
filt.append('[1:v]fps=24,format=rgba,setpts=PTS-STARTPTS[lg]')
filt.append(f'[{ult}][lg]overlay=0:0:eof_action=pass[ol]'); ult = 'ol'
lista = []
for i, (im, a, b) in enumerate(fixos):
    pth = os.path.join(tmp, f'f{i:02d}.png'); im.save(pth); lista.append((pth, a, b))
for i, (pth, a, b) in enumerate(lista):
    args += ['-loop', '1', '-framerate', '24', '-t', f'{min(b + 0.1, dur_b):.3f}', '-i', pth]
    filt.append(f"[{ult}][{i + 2}:v]overlay=0:0:enable='between(t,{a:.3f},{b:.3f})'[o{i}]"); ult = f'o{i}'
final = os.path.join(OUT, NOME + '-legenda' + ('-FACE' if VER == 'face' else '') + '.mp4')
if VER == 'face':
    filt.append(f'[{ult}]setpts=PTS/{VF.VEL}[vf];[0:a]atempo={VF.VEL}[af]'); vm, am, extra = '[vf]', '[af]', VF.LIMPA
else:
    vm, am, extra = f'[{ult}]', '0:a', []
args += ['-filter_complex', ';'.join(filt), '-map', vm, '-map', am, '-c:v', 'libx264', '-crf', '15', '-preset', 'veryfast',
         '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', *extra, '-movflags', '+faststart', '-shortest', final]
subprocess.run(args, check=True)
vel = VF.VEL if VER == 'face' else 1.0
json.dump({'keep': keep, 'cortes': cj, 'legenda': leg, 't_tap': t_tap / vel, 't_gancho': t_g / vel, 'hook_dur': HOOK_DUR / vel, 'dur_final': dur_b / vel, 'video': final},
          open(os.path.join(OUT, f'mapa-{VER}.json'), 'w'), ensure_ascii=False, indent=1)
print('ok', final, f'base {dur_b:.2f}s', f'{len(leg)} pedaços de legenda', f'gancho até {t_g:.2f}s', f'tap em {t_tap:.2f}s')
