#!/usr/bin/env python3
"""nora77 e nora78 (24/11): o aluno sobe todos os takes de uma vez na FusionZ e manda 1 montado só (os do Face no fim, T14/T15 no
nora77 e T10/T11 no nora78). Aqui eu acho o começo de cada take pelas palavras e gravo:
  - insta: o cortes-extra que tira os takes do Face do fim (o editar_simples_2311.py corta o resto pelos silêncios);
  - face: um montado novo, na ordem da versão do Face, e as palavras dele com o tempo deslocado, mais o cortes-extra das
    palavras que saem dentro de um take (o "money," do T04 no nora77).
Uso: python3 -I separar_takes_2411.py <montado.mp4> <palavras.json> <pasta> nora77|nora78
"""
import json, os, re, subprocess, sys

MONT, PAL, OUT, NN = sys.argv[1:5]
ws = json.load(open(PAL, encoding='utf-8'))
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', MONT],
                           capture_output=True, text=True).stdout)

INICIOS = {
    'nora77': ['put cinnamon in', "there's a woman", "i don't know", 'the universe saw', 'but if you', 'st michael the',
               'i can already', 'in seven minutes', 'now save this', 'if you did', 'but the universe', "that's why i left a",
               'so tap my', 'if your name', "that's why i left you"],
    'nora78': ['put cinnamon in', "if you're tired", 'and still feeling', "i don't know", 'the hardest stretch', 'a message you',
               'sometimes a big', 'and because this new season opens differently for every woman, i left',
               'now pay attention', 'if your name', 'and because this new season opens differently for every woman, check'],
}[NN]
ORDEM_FACE = {'nora77': [14, 2, 3, 4, 6, 7, 11, 15], 'nora78': [10, 2, 3, 4, 5, 6, 7, 11]}[NN]
# palavras que saem dentro de um take do Face: (take, palavra)
TIRAR_FACE = {'nora77': [(4, 'money,')], 'nora78': []}[NN]
N_INSTA = {'nora77': 13, 'nora78': 9}[NN]


def norm(t):
    return re.sub(r"[^a-z' ]", '', t.lower().replace('’', "'"))


texto = [norm(w[0]) for w in ws]
achados, k = [], 0
for frase in INICIOS:
    alvo = norm(frase).split()
    while k < len(ws):
        if texto[k:k + len(alvo)] == alvo:
            achados.append(k); k += len(alvo); break
        k += 1
    else:
        sys.exit(f'não achei o começo: {frase!r} (achados até aqui: {len(achados)})')
ini = [ws[i][1] for i in achados]
print('começo de cada take (s):', ', '.join(f'T{n + 1:02d} {t:.2f}' for n, t in enumerate(ini)))


def faixa(n):
    """take n (1 a N) no montado: de ~0,15 s antes da 1ª palavra até ~0,15 s antes da 1ª palavra do take seguinte."""
    a = max(0.0, ini[n - 1] - 0.15)
    b = (ini[n] - 0.15) if n < len(ini) else dur
    return a, b


# insta: corta do começo do 1º take do Face até o fim
ins_extra = [[round(faixa(N_INSTA + 1)[0], 3), round(dur, 3)]]
json.dump(ins_extra, open(os.path.join(OUT, f'cortes-extra-{NN}-insta.json'), 'w'))

# face: o montado na ordem do Face
tmp = os.path.join(OUT, 'face-trechos'); os.makedirs(tmp, exist_ok=True)
ENC = ['-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', '24',
       '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2']
partes, novas, extra_face, acc = [], [], [], 0.0
for j, n in enumerate(ORDEM_FACE):
    a, b = faixa(n)
    p = os.path.join(tmp, f't{j:02d}-T{n:02d}.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{a:.3f}', '-i', MONT, '-t', f'{b - a:.3f}',
                    '-vf', 'scale=1080:1920,setsar=1,fps=24', '-af', f'afade=t=in:d=0.012,afade=t=out:st={max(0, b - a - 0.012):.3f}:d=0.012',
                    *ENC, p], check=True)
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                             capture_output=True, text=True).stdout)
    for w in ws:
        if a <= w[1] < b:
            nw = [w[0], round(w[1] - a + acc, 3), round(min(w[2], b) - a + acc, 3)]
            novas.append(nw)
            for t, palavra in TIRAR_FACE:
                if t == n and norm(w[0]) == norm(palavra):
                    extra_face.append([round(nw[1] - 0.03, 3), round(nw[2] + 0.02, 3)])
    partes.append(p); acc += d
lst = os.path.join(tmp, 'lista.txt')
open(lst, 'w').write(''.join(f"file '{p}'\n" for p in partes))
mf = os.path.join(OUT, f'{NN}-montado-FACE.mp4')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', mf], check=True)
json.dump(novas, open(os.path.join(OUT, f'palavras-{NN}-FACE.json'), 'w'), ensure_ascii=False)
json.dump(extra_face, open(os.path.join(OUT, f'cortes-extra-{NN}-face.json'), 'w'))
print('ok insta: cortar', ins_extra, '| face:', mf, f'{acc:.2f}s', 'ordem', ORDEM_FACE, 'tirar', extra_face)
