#!/usr/bin/env python3
"""Edição do nora68 (o tsunami no rochedo), 17/11/2026: as 2 bases com as imagens do desejo, o cadeado e as 2 specs.

Uso: python3 -I edicao_nora68.py <nora68-montado.mp4> <palavras.json do montado> <pasta de trabalho>
Depois: editar_video.py <pasta>/spec-nora68.json e <pasta>/spec-nora68-FACE.json.

O corpo, o CTA e a edição são os do nora67 (o plano de uma variável por vez, 16/11 23h25); muda só o começo (o tsunami e o Take 1).
Os tempos saem das palavras (as falas são iguais às do nora67) e dos cortes de cena do montado, sem número fixo:
- Insta = o hook do tsunami (d1611-PRE-onda-HOOK.mp4) + o montado do T01 ao fim do T05;
- Face  = o mesmo hook + o T01 a T04 + o T06 (o painel: "a versão do Face leva a onda", porque o tsunami fez 4.236 lá).
"""
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import edicao_nora67 as E  # noqa: E402  (cadeado, pos_cadeado, ff, DES, CAIXA_TOPO)

HOOK = os.path.join(AQUI, 'd1611-PRE-onda-HOOK.mp4')
CAIXA = ["FOR TIRED WOMEN:", "THE STORM ENDS TONIGHT"]
DESTAQUES = ['EXHAUSTED', 'BREATHE,', 'STORM', 'BEHIND', 'EVERYONE,', 'BILLS', 'ERRANDS,', 'TURN', 'FAITH.', 'TURNAROUND', 'CASH,', 'PEACE',
             'WONDERFUL.', 'HARDEST', 'OVER.', 'DOORS', 'OPENING,', 'HOLIDAYS.', 'PHOTO', 'STORY', '2027.', 'COMMENTS', '2027']


def limpa(w):
    return re.sub(r'[^a-z0-9]', '', w.lower())


def achar(ws, palavra, depois=0.0):
    for w, a, b in ws:
        if a >= depois and limpa(w) == palavra:
            return a, b
    raise SystemExit(f'palavra não achada: {palavra} depois de {depois}')


def cortes_de_cena(video):
    out = subprocess.run(['ffmpeg', '-hide_banner', '-i', video, '-an', '-vf', "scale=270:480,select='gt(scene\\,0.06)',metadata=print",
                          '-f', 'null', '-'], capture_output=True, text=True).stderr
    return [float(x) for x in re.findall(r'pts_time:([0-9.]+)', out)]


def corte_entre(cortes, a, b):
    """o corte de cena entre o fim de uma fala (a) e o começo da outra (b); sem corte, o meio do silêncio."""
    c = [x for x in cortes if a - 0.05 <= x <= b + 0.6]  # o whisper costuma marcar a 1ª palavra até ~0,5 s cedo
    return round(c[-1] if c else (a + b) / 2, 3)


def main(montado, pal_json, pasta):
    os.makedirs(pasta, exist_ok=True)
    ws = [tuple(x) for x in json.load(open(pal_json, encoding='utf-8'))]
    dur_m = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', montado]))
    cortes = cortes_de_cena(montado)
    h_dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', HOOK]))

    # as falas: T01 "If you feel…", T02 "You spent all year…", T03 "The universe…", T04 "The hardest…", T05 "Tap my photo…", T06 "For your personal…"
    t01 = ws[0][1]
    ini_t01 = max(0.0, max([x for x in cortes if x <= t01 + 0.6] or [0.0]))  # se o montado veio com algo antes do T01, corta no corte de cena
    if t01 - ini_t01 > 1.0:
        ini_t01 = round(t01 - 0.12, 3)
    you, _ = achar(ws, 'you', t01 + 2.0)
    while True:  # o "You spent all year": o "you" seguido de "spent"
        i = [k for k, w in enumerate(ws) if w[1] == you][0]
        if limpa(ws[i + 1][0]) == 'spent':
            break
        you, _ = achar(ws, 'you', you + 0.05)
    holding, _ = achar(ws, 'holding', you)
    juggling, _ = achar(ws, 'juggling', holding)
    quietly, _ = achar(ws, 'quietly', juggling)
    universe, _ = achar(ws, 'universe', quietly)
    t03 = [w for w in ws if w[1] < universe][-1][1]  # o "The" antes do "universe"
    bringing, _ = achar(ws, 'bringing', universe)
    peace, _ = achar(ws, 'peace', bringing)
    someone, _ = achar(ws, 'someone', peace)
    hardest, _ = achar(ws, 'hardest', someone)
    t04 = [w for w in ws if w[1] < hardest][-1][1]
    doors, _ = achar(ws, 'doors', hardest)
    just, _ = achar(ws, 'just', doors)
    tap, _ = achar(ws, 'tap', just)
    personal, _ = achar(ws, 'personal', tap)
    t06 = [w for w in ws if w[1] < personal][-2][1]  # "For your personal": o "For"
    fim_t04 = [w for w in ws if w[1] < tap][-1][2]
    fim_t05 = [w for w in ws if w[1] < t06][-1][2]
    c45 = corte_entre(cortes, fim_t04, tap)
    c56 = corte_entre(cortes, fim_t05, t06)
    fim_m = round(dur_m - 0.02, 3)
    print(f'T01 {ini_t01} · fim do T04 {c45} · fim do T05 {c56} · fim {fim_m} · hook {h_dur:.3f}')
    print('âncoras', dict(you=you, holding=holding, juggling=juggling, quietly=quietly, t03=t03, bringing=bringing, peace=peace, someone=someone, t04=t04, doors=doors, just=just, tap=tap, t06=t06))
    if os.environ.get('SECO'):
        return

    # as bases (o hook na frente das duas)
    pre_i = os.path.join(pasta, 'nora68-insta-pre.mp4')
    pre_f = os.path.join(pasta, 'nora68-face-pre.mp4')
    def junta(trechos, saida):
        f = [f'[0:v]fps=24,scale=1080:1920,setsar=1[v0]', f'[0:a]aresample=48000,afade=t=out:st={h_dur - 0.03:.3f}:d=0.03[a0]']
        rot = ['[v0][a0]']
        for j, (a, b) in enumerate(trechos, 1):
            f.append(f'[1:v]trim={a}:{b},setpts=PTS-STARTPTS,setsar=1[v{j}]')
            f.append(f'[1:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d=0.03,afade=t=out:st={b - a - 0.03:.3f}:d=0.03[a{j}]')
            rot.append(f'[v{j}][a{j}]')
        f.append(''.join(rot) + f'concat=n={len(rot)}:v=1:a=1[v][a]')
        E.ff('-i', HOOK, '-i', montado, '-filter_complex', ';'.join(f), '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '14',
             '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', '24', '-c:a', 'aac', '-b:a', '192k', saida)
    junta([(ini_t01, c56)], pre_i)
    junta([(ini_t01, c45), (c56, fim_m)], pre_f)
    d1 = h_dur - ini_t01                       # montado → base (o T01 em diante)
    d2 = h_dur + (c45 - ini_t01) - c56         # montado (T06) → base do Face
    dur_i = h_dur + (c56 - ini_t01)
    dur_f = h_dur + (c45 - ini_t01) + (fim_m - c56)

    IMGS = [('d1511-DESEJO-2-sorrindo-para-todos.jpg', holding - 0.05, juggling, 'dividida', 0.5, False),
            ('d1611-DESEJO-8-contas-e-tarefas.jpg', juggling, quietly, 'dividida', 0.55, False),
            ('d1511-DESEJO-3-sozinha-na-cama.jpg', quietly, t03 - 0.08, 'cheia', 0.5, False),
            ('d1511-DESEJO-4-dinheiro-no-envelope.jpg', bringing, peace, 'cheia', 0.5, True),
            ('d1511-DESEJO-5-paz-na-varanda.jpg', peace, someone, 'dividida', 0.55, False),
            ('d1511-DESEJO-6-casal-na-praia.jpg', someone, t04 - 0.08, 'cheia', 0.5, False),
            ('d1511-DESEJO-7-porta-abrindo.jpg', doors - 0.05, just, 'dividida', 0.5, False),
            ('d1611-DESEJO-9-festas.jpg', just, min(tap, c45) - 0.05, 'cheia', 0.5, False)]
    imgs = lambda insta: [{"arquivo": os.path.join(E.DES, a), "ini": round(i + d1, 3), "fim": round(f + d1, 3), "modo": m, "foco_y": fy}
                          for a, i, f, m, fy, so in IMGS if insta or not so]
    cfg_i = {"entrada": pre_i, "saida": os.path.join(pasta, 'nora68-insta-base.mp4'), "imagens": imgs(True)}
    cfg_f = {"entrada": pre_f, "saida": os.path.join(pasta, 'nora68-face-base.mp4'), "imagens": imgs(False)}
    for nome, cfg in (('desejo-nora68.json', cfg_i), ('desejo-nora68-FACE.json', cfg_f)):
        p = os.path.join(pasta, nome); json.dump(cfg, open(p, 'w'), indent=1)
        subprocess.run([sys.executable, '-I', os.path.join(AQUI, '..', 'ferramentas', 'montar_desejo.py'), p], check=True)

    lock = os.path.join(pasta, 'cadeado.png'); E.cadeado(lock)
    l1, l2 = 'Your 2027 reading:      ', '[tap my photo]'
    lx, ly = E.pos_cadeado(l1, l2, 470)
    numeros = lambda fim: [
        {"tipo": "texto", "ini": 0, "fim": fim, "x": -230, "y": 282, "tamanho": 13, "texto": "222", "cor": "#FFFFFF"},
        {"tipo": "texto", "ini": 0, "fim": fim, "x": 230, "y": 282, "tamanho": 13, "texto": "11:11", "cor": "#FFFFFF"}]
    caixa = {"tipo": "caixa", "ini": 0, "fim": round(you - 0.1 + d1, 3), "x": 0, "y": 458, "tamanho": 10, "linhas": CAIXA, "caixa": E.CAIXA_TOPO}
    whoosh = lambda lst: [{"som": "whoosh", "pico_em": round(d["ini"] + 0.05, 3), "db": -12} for d in lst]
    def pal(de, ate, desloc):
        out = []
        for w, a, b in ws:
            if de - 0.6 <= a < ate:
                out.append([w.replace('1111', '11:11'), round(max(a, de + 0.03) + desloc, 3), round(b + desloc, 3)])
        return out
    sons_hook = lambda riser: [{"som": riser, "pico_em": "corte-0.1"}, {"som": "impact", "pico_em": "corte"}]
    ins = {"entrada": cfg_i["saida"], "saida": os.path.join(pasta, 'nora68-final.mp4'), "crf": 21, "preset": "medium",
           "estilo": "alto-contraste", "corte": round(h_dur, 3), "respiro": 0.1,
           "sons": sons_hook('riser-lento') + whoosh(cfg_i["imagens"]),  # o nora67 do Insta teve o riser: alterna
           "itens": [caixa] + numeros(round(dur_i, 3)) + [
               {"tipo": "legenda", "ini": round(h_dur, 3), "fim": round(dur_i, 3), "palavras": pal(ini_t01, c56, d1), "destaques": DESTAQUES,
                "y": -310, "tamanho_px": 38},
               {"tipo": "caixa", "ini": round(c45 + d1, 3), "fim": round(dur_i, 3), "x": 0, "y": 470, "tamanho": 10, "linhas": [l1, l2]},
               {"tipo": "imagem", "ini": round(c45 + d1, 3), "fim": round(dur_i, 3), "arquivo": lock, "largura": 30, "x": round(lx, 1), "y": round(ly, 1)},
               {"tipo": "seta", "ini": round(c45 + d1, 3), "fim": round(dur_i, 3), "x": -288, "y": -333, "tamanho": 14}]}
    fb = {"entrada": cfg_f["saida"], "saida": os.path.join(pasta, 'nora68-final-FACE.mp4'), "crf": 21, "preset": "medium",
          "estilo": "alto-contraste", "corte": round(h_dur, 3), "respiro": 0.1,
          "sons": sons_hook('riser') + whoosh(cfg_f["imagens"]),
          "itens": [caixa] + numeros(round(dur_f, 3)) + [
              {"tipo": "legenda", "ini": round(h_dur, 3), "fim": round(dur_f, 3),
               "palavras": pal(ini_t01, c45, d1) + pal(c56, fim_m, d2), "destaques": DESTAQUES, "y": -310, "tamanho_px": 38},
              {"tipo": "caixa", "ini": round(c56 + d2, 3), "fim": round(dur_f, 3), "x": 0, "y": 470, "tamanho": 10,
               "linhas": ["Your 2027 reading:", "[link in the comments]"]}]}
    for nome, sp in (('spec-nora68.json', ins), ('spec-nora68-FACE.json', fb)):
        json.dump(sp, open(os.path.join(pasta, nome), 'w'), indent=1)
    print('insta', round(dur_i, 3), 'face', round(dur_f, 3))


if __name__ == '__main__':
    main(*sys.argv[1:4])
