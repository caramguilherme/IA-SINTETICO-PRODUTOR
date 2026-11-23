"""Mineração em lotes: baixa só os vídeos NOVOS de uma pasta pública do Drive,
tira o áudio, transcreve (faster-whisper "small") e monta uma folha de quadros por vídeo.

Uso (rodar com python3 -I; os arquivos baixados ficam fora do repositório):
  HF_HUB_DISABLE_XET=1 python3 -I ferramentas-painel/mineracao/minerar.py PASTA_ID TRABALHO REGISTRO.tsv

- PASTA_ID: o id da pasta do Drive (a parte depois de /folders/).
- TRABALHO: uma pasta no scratchpad (os vídeos leves, os .wav, os .json e as folhas).
- REGISTRO.tsv: o registro do repositório (n, id do Drive, nome do arquivo, lote). Quem já está
  nele não é baixado de novo; os novos continuam a numeração (m59, m60…).
"""
import sys, os, re, html, json, subprocess, datetime

def sh(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, **kw)

def listar(pasta):
    r = sh(['curl', '-sS', '-L', f'https://drive.google.com/embeddedfolderview?id={pasta}'])
    ents = re.findall(r'id="entry-([A-Za-z0-9_-]+)".*?flip-entry-title">([^<]*)', r.stdout, re.S)
    return [(i, html.unescape(t)) for i, t in ents]

def baixar(i, n, w):
    v = os.path.join(w, f'_m{n}.mp4')
    for _ in range(3):
        if sh(['curl', '-sS', '-L', '-o', v, f'https://drive.usercontent.google.com/download?id={i}&export=download&confirm=t']).returncode == 0:
            break
    sh(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-i', v, '-vn', '-ac', '1', '-ar', '16000', os.path.join(w, f'm{n}.wav')])
    sh(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-i', v, '-vf', 'scale=-2:960', '-c:v', 'libx264', '-crf', '28', '-preset', 'veryfast', '-an', os.path.join(w, f'm{n}-leve.mp4')])
    d = sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', v]).stdout.strip()
    os.remove(v)
    return float(d or 0)

def transcrever(ns, w):
    import wave
    import numpy as np
    from faster_whisper import WhisperModel
    m = WhisperModel('small', device='cpu', compute_type='int8', cpu_threads=4)
    for n in ns:
        wav = os.path.join(w, f'm{n}.wav')
        f = wave.open(wav)
        a = np.frombuffer(f.readframes(f.getnframes()), dtype=np.int16).astype(np.float32) / 32768
        segs, info = m.transcribe(a, vad_filter=True, beam_size=1)
        segs = [{'ini': round(s.start, 2), 'fim': round(s.end, 2), 'texto': s.text.strip()} for s in segs]
        json.dump({'lang': info.language, 'segs': segs}, open(os.path.join(w, f'm{n}.json'), 'w'), ensure_ascii=False, indent=1)
        print('transcrito', n, info.language, flush=True)

def folha(n, w, d):
    from PIL import Image, ImageDraw, ImageFont
    fw, fh = 216, 384
    try:
        fonte = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    except Exception:
        fonte = ImageFont.load_default()
    v = os.path.join(w, f'm{n}-leve.mp4')
    ts = [0.1, 1, 2, 3, 5] + [d * 0.2, d * 0.4, d * 0.6, d * 0.8, max(d - 3, 0)]
    im = Image.new('RGB', (fw * 5, fh * 2 + 40), 'white'); dr = ImageDraw.Draw(im)
    for k, t in enumerate(ts):
        q = os.path.join(w, f'_q{n}_{k}.jpg')
        sh(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-ss', f'{min(t, max(d - 0.1, 0)):.2f}', '-i', v, '-frames:v', '1', '-vf', f'scale={fw}:{fh}', q])
        x, y = (k % 5) * fw, 40 + (k // 5) * fh
        if os.path.exists(q):
            im.paste(Image.open(q), (x, y)); os.remove(q)
        dr.rectangle([x, y, x + 62, y + 22], fill='black'); dr.text((x + 3, y + 2), f'{t:.0f}s', fill='yellow', font=fonte)
    dr.text((5, 10), f'm{n}  ({d:.0f} s)', fill='black', font=fonte)
    im.save(os.path.join(w, f'folha-m{n}.jpg'), quality=80)

def main():
    pasta, w, reg = sys.argv[1:4]
    os.makedirs(w, exist_ok=True)
    feitos = {}
    if os.path.exists(reg):
        for l in open(reg):
            p = l.rstrip('\n').split('\t')
            if len(p) >= 3 and p[0] != 'n':
                feitos[p[1]] = p
    prox = max([int(p[0]) for p in feitos.values()] + [0]) + 1
    from zoneinfo import ZoneInfo
    lote = datetime.datetime.now(ZoneInfo('America/Sao_Paulo')).strftime('%d/%m %H:%M')
    novos = []
    for i, nome in listar(pasta):
        if i not in feitos:
            novos.append((f'{prox:02d}', i, nome)); prox += 1
    print(len(novos), 'novos', flush=True)
    if not novos:
        return
    durs = {}
    for n, i, nome in novos:
        durs[n] = baixar(i, n, w); print('baixado', n, nome, f'{durs[n]:.0f}s', flush=True)
    transcrever([n for n, _, _ in novos], w)
    for n, _, _ in novos:
        folha(n, w, durs[n])
    novo_reg = not os.path.exists(reg)
    with open(reg, 'a') as f:
        if novo_reg:
            f.write('n\tid_drive\tarquivo\tlote\tduracao_s\n')
        for n, i, nome in novos:
            f.write(f'{n}\t{i}\t{nome}\t{lote}\t{durs[n]:.0f}\n')
    print('FIM', flush=True)

if __name__ == '__main__':
    main()
