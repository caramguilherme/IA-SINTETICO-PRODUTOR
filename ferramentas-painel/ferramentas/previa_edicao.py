#!/usr/bin/env python3
"""Prévia da edição (P45): compõe as camadas de uma spec sobre quadros do vídeo, sem renderizar tudo.

Uso:  python3 -I previa_edicao.py spec.json saida.png 2.0 9.0 20 34 46 57
Gera uma folha com até 8 quadros (4 por linha), cada um com a caixa, os números, a legenda, a faixa,
a seta e as imagens que valem naquele segundo. Serve para conferir posições ANTES do render (~8 min).
"""
import json, os, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import editar_video as ev
from PIL import Image


def quadro(sp, t, W, H, k, tmp):
    p = os.path.join(tmp, f'q_{t}.png')
    subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', sp['entrada'], '-frames:v', '1', p])
    base = Image.open(p).convert('RGBA')
    for it in sp['itens']:
        tipo = it['tipo']
        if tipo == 'legenda':
            dest = {x.upper() for x in it.get('destaques', [])}
            for txt, a, b in ev.blocos_legenda(it['palavras'], it.get('max_palavras', 3)):
                if max(a, it['ini']) <= t < min(b, it['fim']):
                    base = Image.alpha_composite(base, ev.png_legenda(W, H, txt, dest, it, k))
            continue
        if not (it['ini'] <= t < it['fim']):
            continue
        if tipo == 'caixa': im = ev.png_caixa(W, H, it, k)[0]
        elif tipo == 'texto': im = ev.png_texto(W, H, it, k)
        elif tipo == 'seta': im = ev.png_seta(W, H, it, k)
        elif tipo == 'imagem': im = ev.png_imagem(W, H, it, k)
        else: continue
        base = Image.alpha_composite(base, im)
    return base.convert('RGB')


def main():
    sp = json.load(open(sys.argv[1], encoding='utf-8'))
    if sp.get('estilo'):  # 12/11: o mesmo estilo do render (editar_video.py)
        ev.TEMA = ev.EST.tema(sp['estilo']); ev.COM_ESTILO = True
    saida = sys.argv[2]
    tempos = [float(x) for x in sys.argv[3:11]]
    W, H = ev.sonda(sp['entrada']); k = W / 720.0
    tmp = tempfile.mkdtemp(prefix='previa_')
    fotos = [quadro(sp, t, W, H, k, tmp).resize((360, 640)) for t in tempos]
    lin = (len(fotos) + 3) // 4
    folha = Image.new('RGB', (360 * min(4, len(fotos)), 640 * lin), 'black')
    for i, f in enumerate(fotos):
        folha.paste(f, ((i % 4) * 360, (i // 4) * 640))
    folha.save(saida)
    # medidas úteis: onde cada caixa e cada número cai na tela (% da largura e da altura)
    for it in sp['itens']:
        if it['tipo'] in ('caixa', 'texto', 'seta'):
            im = {'caixa': lambda: ev.png_caixa(W, H, it, k)[0], 'texto': lambda: ev.png_texto(W, H, it, k), 'seta': lambda: ev.png_seta(W, H, it, k)}[it['tipo']]()
            b = im.getbbox()
            nome = it.get('texto') or (it['linhas'][0] if isinstance(it.get('linhas', [''])[0], str) else 'caixa') if it['tipo'] != 'seta' else 'seta'
            print(f"{it['tipo']:6} {str(nome)[:28]:28} x {b[0]/W*100:5.1f}-{b[2]/W*100:5.1f}%  y {b[1]/H*100:5.1f}-{b[3]/H*100:5.1f}%  ({it['ini']}-{it['fim']} s)")
    print('ok', saida)


if __name__ == '__main__':
    main()
