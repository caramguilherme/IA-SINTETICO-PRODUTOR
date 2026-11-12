#!/usr/bin/env python3
"""Edição automática dos vídeos da Nora (P45, 03/11/2026).

O aluno manda o vídeo montado no CapCut (hook + takes + música, SEM texto). Este script põe por cima
caixa do topo, números fixos, legenda, imagens (desejo, avaliações), faixa do story e seta, sem mexer no áudio.

Uso:  python3 -I editar_video.py spec.json
Coordenadas como no CapCut: X e Y a partir do centro de uma tela 720x1280, Y para cima (o hook X 0 · Y 397).
Tamanho como no CapCut (campo Tamanho); 1 unidade ~ PX_POR_TAMANHO px na tela 720 (calibrar com um quadro real).

spec.json:
{
 "entrada": "video.mp4", "saida": "final.mp4",
 "itens": [
  {"tipo":"caixa","ini":0,"fim":15.2,"x":0,"y":397,"tamanho":10,"linhas":["TAURUS, VIRGO, CAPRICORN","11:11, the most powerful portal"],"cores":["#E53935","#000000"]},
  {"tipo":"texto","ini":0,"fim":15.2,"x":245,"y":486,"tamanho":15,"texto":"11:11","cor":"#E53935"},
  {"tipo":"imagem","ini":20,"fim":24,"arquivo":"casal.jpg","x":0,"y":150,"largura":560,"fade":0.25,"borda":12},
  {"tipo":"legenda","ini":7.4,"fim":15.2,"palavras":[["TAURUS",7.4,7.9],["VIRGO",7.9,8.3]],"destaques":["TAURUS","VIRGO"],"y":-294,"tamanho_px":38}
 ],
 "respiro": 0.1,
 "sons": [{"som":"riser","pico_em":"corte-0.1"}, {"som":"impact","pico_em":"corte"}]
}

"sons" (12/11/2026, Clone R34; opcional): efeitos misturados ao áudio do montado, no tempo certo. "pico_em" é o segundo do
vídeo em que cai o pico do som (o fim do riser, a batida do impact); "corte" acha sozinho o corte do pré-gancho para a fala
(1ª troca de cena forte entre 1 e 9 s). "db" (opcional) é o volume do pico em relação à referência (a voz ou o pré-gancho, o mais alto; padrão em SONS). Sons em sons/.
Sem "sons", o áudio é copiado sem mexer.
"""
import importlib.util, json, os, re, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(AQUI, 'fontes', 'Poppins-Bold.ttf')
PX_POR_TAMANHO = 2.8  # 13,5 no CapCut ~ 38 px na tela 720 (calibrar)
OURO = '#FFD21F'
# 12/11/2026 (pedido do aluno): o estilo dos textos varia por vídeo e combina com a cena ("estilo" no spec; ver estilos_video.py
# e a skill estilo-visual-nora). Sem "estilo", sai o visual antigo (caixa branca, preto e vermelho, legenda branca e ouro).
_spec = importlib.util.spec_from_file_location('estilos_video', os.path.join(AQUI, 'estilos_video.py'))
EST = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(EST)
TEMA = EST.tema(None)
COM_ESTILO = False
# Efeitos sonoros (Clone R34, 12/11/2026): riser de ~2,5 s que termina no corte do pré-gancho + impact (whoosh grave com batida) no
# 1º quadro da fala. Mixkit, licença grátis de efeitos sonoros (sons/LEIA.md). db = pico do som em relação à referência: o mais alto
# entre a voz e o som do pré-gancho (o pré-gancho costuma vir ~10 dB acima da voz; com a voz de referência, o riser sumia no tsunami).
SONS_DIR = os.path.join(AQUI, 'sons')
# Escolhidos pelo aluno em 12/11 ~13h40 (teste de 5 risers e 3 impacts no nora55): riser = o 2 (orquestra dramática, tensão que explode no
# fim), riser-lento = o 4 (o "riser sound effect" de outubro do aluno), alternados entre posts seguidos da mesma rede; impact = o B ajustado.
SONS = {'riser': ('riser-nora.wav', 0), 'riser-lento': ('riser-lento-nora.wav', 0), 'impact': ('impact-nora.wav', 1),
        'whoosh': ('whoosh-nora.wav', -8), 'sparkle': ('sparkle-nora.wav', -12)}


def sonda(arq):
    o = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                                            'stream=width,height', '-of', 'json', arq]))
    s = o['streams'][0]
    return s['width'], s['height']


def fonte(px):
    return ImageFont.truetype(FONTE, max(8, int(round(px))))


def centro(x, y, W, H):
    k = W / 720.0
    return W / 2 + x * k, H / 2 - y * k


def png_texto(W, H, it, k):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = fonte(it['tamanho'] * PX_POR_TAMANHO * k)
    cx, cy = centro(it['x'], it['y'], W, H)
    sw = max(2, int(3 * k))
    sombra = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sombra)
    sc = EST.hexrgb(TEMA['numeros']['sombra'])
    ds.text((cx + 3 * k, cy + 3 * k), it['texto'], font=f, fill=sc + (170,), anchor='mm', stroke_width=sw, stroke_fill=sc + (170,))
    sombra = sombra.filter(ImageFilter.GaussianBlur(2 * k))
    im = Image.alpha_composite(sombra, im); d = ImageDraw.Draw(im)
    d.text((cx, cy), it['texto'], font=f, fill=it.get('cor', '#FFFFFF'), anchor='mm', stroke_width=sw, stroke_fill=TEMA['numeros']['contorno'])
    return im


def png_caixa_estilo(W, H, it, k):
    """Com "estilo" no spec: linhas são strings com o trecho de destaque entre [colchetes]; cores e fontes vêm do estilo."""
    c = EST.mescla(TEMA['caixa'], it.get('caixa', {}))
    sz = it['tamanho'] * PX_POR_TAMANHO * k
    fp = EST.fonte(c['fonte'], sz); fd = EST.fonte(c['destaque_fonte'], sz * (1.25 if c['destaque_fonte'] == 'serif_it' else 1))
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    segs = [[(p, fd if i % 2 else fp, c['destaque'] if i % 2 else c['texto']) for i, p in enumerate(re.split(r'\[|\]', l)) if p] for l in it['linhas']]
    wl = [sum(d.textlength(s, font=f) for s, f, _ in l) for l in segs]
    asc, desc = fp.getmetrics(); lh = int((asc + desc) * 1.15)
    padx, pady = int(20 * k), int(13 * k)
    bw, bh = max(wl) + 2 * padx, lh * len(segs) + 2 * pady
    cx, cy = centro(it['x'], it['y'], W, H)
    x0, y0 = cx - bw / 2, cy - bh / 2
    if c['fundo'][3] > 0:
        if c.get('sombra'):
            sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 6 * k, x0 + bw, y0 + bh + 6 * k], radius=int(c['raio'] * k), fill=EST.hexrgb(c['sombra']) + (80,))
            im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(8 * k)))
        bx = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(bx).rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=int(c['raio'] * k), fill=tuple(c['fundo']))
        im = Image.alpha_composite(im, bx)
    else:  # sem caixa: sombra suave atrás das letras
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
        for i, l in enumerate(segs):
            x = cx - wl[i] / 2; y = y0 + pady + lh * i + lh / 2
            for s, f, _ in l:
                ds.text((x + 2 * k, y + 3 * k), s, font=f, fill=(0, 0, 0, 150), anchor='lm'); x += ds.textlength(s, font=f)
        im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(3 * k)))
    d = ImageDraw.Draw(im)
    for i, l in enumerate(segs):
        x = cx - wl[i] / 2; y = y0 + pady + lh * i + lh / 2
        for s, f, cor in l:
            kw = {} if c['fundo'][3] > 0 else dict(stroke_width=max(2, int(2 * k)), stroke_fill=c.get('contorno', '#000000'))
            d.text((x, y - (sz * 0.12 if f is fd and c['destaque_fonte'] == 'serif_it' else 0)), s, font=f, fill=cor, anchor='lm', **kw)
            x += d.textlength(s, font=f)
    return im, (x0 / W, (x0 + bw) / W)


def png_caixa(W, H, it, k):
    """linhas: lista de strings (cor da linha em 'cores') ou de listas de segmentos [[texto, cor], ...]."""
    if COM_ESTILO and 'cores' not in it and all(isinstance(l, str) for l in it['linhas']):
        return png_caixa_estilo(W, H, it, k)
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = fonte(it['tamanho'] * PX_POR_TAMANHO * k)
    cores = it.get('cores', ['#000000']) + ['#000000'] * len(it['linhas'])
    linhas = [l if isinstance(l, list) else [[l, cores[i]]] for i, l in enumerate(it['linhas'])]
    asc, desc = f.getmetrics(); lh = int((asc + desc) * 1.12)
    larg_l = [sum(d.textlength(t, font=f) for t, _ in segs) for segs in linhas]
    larg = max(larg_l)
    pad_x, pad_y = int(18 * k), int(12 * k)
    bw, bh = larg + 2 * pad_x, lh * len(linhas) + 2 * pad_y
    cx, cy = centro(it['x'], it['y'], W, H)
    x0, y0 = cx - bw / 2, cy - bh / 2
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=int(16 * k), fill=it.get('fundo', '#FFFFFF'))
    for i, segs in enumerate(linhas):
        x = cx - larg_l[i] / 2; y = y0 + pad_y + lh * i + lh / 2
        for t, cor in segs:
            d.text((x, y), t, font=f, fill=cor, anchor='lm')
            x += d.textlength(t, font=f)
    return im, (x0 / W, (x0 + bw) / W)


def png_seta(W, H, it, k):
    """Seta para baixo (vermelha com traço preto), centro em x, y; 'tamanho' como no CapCut."""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    s = it.get('tamanho', 14) * PX_POR_TAMANHO * k
    cx, cy = centro(it['x'], it['y'], W, H)
    hw, sh, hh = s * 0.16, s * 0.55, s * 0.45  # meia largura da haste, altura da haste, altura da ponta
    top = cy - (sh + hh) / 2
    pts = [(cx - hw, top), (cx + hw, top), (cx + hw, top + sh), (cx + s * 0.42, top + sh),
           (cx, top + sh + hh), (cx - s * 0.42, top + sh), (cx - hw, top + sh)]
    d.polygon(pts, fill=it.get('cor', TEMA['seta']['cor']), outline=TEMA['seta']['contorno'], width=max(2, int(3 * k)))
    return im


def png_imagem(W, H, it, k):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    src = Image.open(it['arquivo']).convert('RGBA')
    lw = int(it['largura'] * k); lh = int(src.height * lw / src.width)
    src = src.resize((lw, lh), Image.LANCZOS)
    b = int(it.get('borda', 0) * k)
    if b:
        quadro = Image.new('RGBA', (lw + 2 * b, lh + 2 * b), it.get('cor_borda', TEMA['imagem']['borda'])); quadro.paste(src, (b, b)); src = quadro
    cx, cy = centro(it.get('x', 0), it.get('y', 0), W, H)
    im.paste(src, (int(cx - src.width / 2), int(cy - src.height / 2)), src)
    return im


def png_legenda(W, H, texto, destaques, it, k):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    lg = TEMA['legenda']
    f = EST.fonte(lg['fonte'], it.get('tamanho_px', 38) * k)
    sw = max(3, int(4 * k))
    pal = texto.split()
    esp = d.textlength(' ', font=f)
    largs = [d.textlength(p, font=f) for p in pal]
    total = sum(largs) + esp * (len(pal) - 1)
    linhas = [pal]
    if total > W * 0.80 and len(pal) > 1:
        meio = len(pal) // 2; linhas = [pal[:meio], pal[meio:]]
    asc, desc = f.getmetrics(); lh = int((asc + desc) * 1.05)
    cx, cy = centro(0, it.get('y', -294), W, H)
    y = cy - lh * len(linhas) / 2 + lh / 2
    for ln in linhas:
        lw = sum(d.textlength(p, font=f) for p in ln) + esp * (len(ln) - 1)
        x = cx - lw / 2
        for p in ln:
            cor = lg['destaque'] if p.strip('.,!?:').upper() in destaques else lg['cor']
            d.text((x, y), p, font=f, fill=cor, anchor='lm', stroke_width=sw, stroke_fill=lg['contorno'])
            x += d.textlength(p, font=f) + esp
        y += lh
    return im


def blocos_legenda(palavras, max_pal=3):
    """[[palavra, ini, fim], ...] -> [(texto, ini, fim)] em blocos de 2 a 4 palavras, quebrando na pontuação."""
    out, cur = [], []
    for w in palavras:
        cur.append(w)
        if len(cur) >= max_pal or w[0].rstrip()[-1:] in '.,!?:':
            out.append(cur); cur = []
    if cur: out.append(cur)
    res = []
    for i, b in enumerate(out):
        ini = b[0][1]; fim = out[i + 1][0][1] if i + 1 < len(out) else b[-1][2]
        res.append((' '.join(x[0].upper() for x in b), ini, fim))
    return res


def janelas_db(arq, ini=0.0, fim=None, sr=16000, w=0.05, hp=250):
    """Nível (dBFS) do áudio em janelas de 50 ms, de ini a fim. hp: passa-alta (250 Hz ~ o que o alto-falante do celular toca;
    o grave do impact some no celular, então o volume é medido sem ele; hp=0 mede tudo)."""
    import numpy as np
    dur = ['-t', f'{fim - ini:.3f}'] if fim else []
    af = ['-af', f'highpass=f={hp}'] if hp else []
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{ini:.3f}'] + dur + ['-i', arq, '-vn'] + af + ['-ac', '1', '-ar', str(sr), '-f', 's16le', '-'],
                         capture_output=True, check=True).stdout
    a = np.frombuffer(raw, dtype=np.int16).astype(float) / 32768; n = int(sr * w)
    return np.array([20 * np.log10(np.sqrt(np.mean(a[i:i + n] ** 2)) + 1e-9) for i in range(0, len(a) - n, n)]), w


def achar_corte(arq):
    """O corte do pré-gancho para a fala: a 1ª troca de cena forte (score > 0,4) entre 1 e 9 s."""
    log = subprocess.run(['ffmpeg', '-hide_banner', '-t', '9', '-i', arq, '-vf', "select='gt(scene,0.4)',metadata=print", '-an', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    for t in re.findall(r'pts_time:([0-9.]+)', log):
        if float(t) >= 1.0: return float(t)
    sys.exit('sons: não achei o corte do pré-gancho; ponha "pico_em" em segundos no spec')


def filtros_sons(sp, idx0):
    """Entradas e filtros do ffmpeg para misturar os efeitos ao áudio do montado (entrada 0)."""
    corte = sp.get('corte'); ins, fs, labs, rel = [], [], [], []  # "corte" na spec: o segundo exato (quando o pré-gancho tem um corte interno, como o tsunami A+B)
    ref = None
    for j, s in enumerate(sp['sons']):
        arq, db_pad = SONS[s['som']] if s.get('som') in SONS else (s['arquivo'], -10)
        arq = arq if os.path.isabs(arq) else os.path.join(SONS_DIR, arq)
        pe = s['pico_em']
        if isinstance(pe, str) and pe.startswith('corte'):  # "corte" ou "corte-0.08" (antes do corte)
            corte = corte if corte is not None else achar_corte(sp['entrada']); pe = corte + float(pe[5:] or 0)
        if ref is None:  # o mais alto entre a voz (depois do corte) e o som do pré-gancho (antes), percentil 90 das janelas
            import numpy as np
            e, _ = janelas_db(sp['entrada'], ini=corte if corte is not None else 0.0)
            ref = float(np.percentile(e[e > -60], 90))
            if corte is not None and corte > 1:
                e, _ = janelas_db(sp['entrada'], ini=0.0, fim=corte)
                if (e > -60).any():  # no POV o começo é só paisagem, sem som
                    ref = max(ref, float(np.percentile(e[e > -60], 90)))
        e, w = janelas_db(arq, hp=0); pico_arq = int(e.argmax()) * w; mx_cheio = float(e.max())  # o pico de verdade (com o grave)
        mx = float(janelas_db(arq)[0].max())  # o nível que o celular toca
        ganho = min(ref + s.get('db', db_pad) - mx, -3 - mx_cheio)  # sem passar de -3 dBFS com o grave
        atraso = pe - pico_arq
        cad = 'aformat=sample_rates=48000:channel_layouts=stereo'
        if atraso < 0: cad += f',atrim=start={-atraso:.3f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.15'
        else: cad += f',adelay={int(round(atraso * 1000))}:all=1'
        ins += ['-i', arq]
        fs.append(f'[{idx0 + j}:a]{cad},volume={ganho:.1f}dB[s{j}]'); labs.append(f'[s{j}]')
        rel.append(f"{s.get('som', os.path.basename(arq))} pico em {pe:.2f}s ({s.get('db', db_pad)} dB da referência, {ref:.0f} dBFS)")
    resp = ''  # "respiro": o som do montado baixa nos últimos segundos antes do corte, para o impact bater depois de um vazio
    if sp.get('respiro') and corte is not None:
        r = float(sp['respiro']); resp = f",volume=0.2:enable='between(t,{corte - r:.3f},{corte:.3f})'"
        rel.append(f'respiro de {r:.2f}s antes do corte ({corte:.2f}s)')
    fs.append(f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo{resp}[a0];[a0]{''.join(labs)}amix=inputs={len(labs) + 1}:normalize=0:duration=first,alimiter=limit=0.95[aout]")
    return ins, fs, rel


def main(spec_path):
    global TEMA, COM_ESTILO
    sp = json.load(open(spec_path, encoding='utf-8'))
    if sp.get('estilo'):
        TEMA = EST.tema(sp['estilo']); COM_ESTILO = True
    W, H = sonda(sp['entrada']); k = W / 720.0
    tmp = tempfile.mkdtemp(prefix='edicao_')
    camadas = []  # (png, ini, fim, fade)
    avisos = []
    for n, it in enumerate(sp['itens']):
        t = it['tipo']
        if t == 'texto':
            camadas.append((png_texto(W, H, it, k), it['ini'], it['fim'], it.get('fade', 0)))
        elif t == 'caixa':
            im, (a, b) = png_caixa(W, H, it, k)
            if a < 0.08 or b > 0.92: avisos.append(f'caixa {n} passa da margem do Face: {a:.0%} a {b:.0%}')
            camadas.append((im, it['ini'], it['fim'], it.get('fade', 0)))
        elif t == 'imagem':
            camadas.append((png_imagem(W, H, it, k), it['ini'], it['fim'], it.get('fade', 0.25)))
        elif t == 'seta':
            camadas.append((png_seta(W, H, it, k), it['ini'], it['fim'], it.get('fade', 0)))
        elif t == 'legenda':
            dest = {x.upper() for x in it.get('destaques', [])}
            for txt, a, b in blocos_legenda(it['palavras'], it.get('max_palavras', 3)):
                if a >= it['fim'] or b <= it['ini']: continue
                camadas.append((png_legenda(W, H, txt, dest, it, k), max(a, it['ini']), min(b, it['fim']), 0))
    args = ['ffmpeg', '-y', '-v', 'error', '-i', sp['entrada']]
    filtros, ult = [], '0:v'
    for i, (im, a, b, fade) in enumerate(camadas):
        p = os.path.join(tmp, f'c{i:03d}.png'); im.save(p)
        args += ['-loop', '1', '-t', f'{b:.3f}', '-i', p]
        src = f'{i + 1}:v'
        if fade:
            filtros.append(f'[{src}]format=rgba,fade=t=in:st={a:.3f}:d={fade}:alpha=1,fade=t=out:st={max(a, b - fade):.3f}:d={fade}:alpha=1[f{i}]'); src = f'f{i}'
        filtros.append(f"[{ult}][{src}]overlay=0:0:enable='between(t,{a:.3f},{b:.3f})':eof_action=pass[v{i}]"); ult = f'v{i}'
    audio = ['-c:a', 'copy']; rel = []
    if sp.get('sons'):
        ins, fs_a, rel = filtros_sons(sp, len(camadas) + 1)
        args += ins; filtros += fs_a; audio = ['-c:a', 'aac', '-b:a', '192k']
    if filtros:
        args += ['-filter_complex', ';'.join(filtros), '-map', f'[{ult}]' if camadas else '0:v', '-map', '[aout]' if sp.get('sons') else '0:a?']
    args += ['-c:v', 'libx264', '-preset', sp.get('preset', 'medium'), '-crf', str(sp.get('crf', 18)), '-pix_fmt', 'yuv420p'] + audio + ['-movflags', '+faststart', sp['saida']]
    subprocess.check_call(args)
    for r in rel: print('som:', r)
    for a in avisos: print('AVISO:', a)
    print('ok', sp['saida'], f'{len(camadas)} camadas', 'estilo:', sp.get('estilo', 'branco-classico (padrão antigo)') if isinstance(sp.get('estilo'), (str, type(None))) else 'sob-medida')


if __name__ == '__main__':
    main(sys.argv[1])
