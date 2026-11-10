# 29/10/2026 ~17h30: nora41-IMG, nora41-FIM e o clipe aprovados. O porta-retrato saiu mais baixo que o pedido
# (62% a 84% da altura; o cartão de 68% a 78%), então o texto do story sobe para cima do porta-retrato (58%),
# o 888 vai para a borda esquerda (5%, 63%) e a seta vai para (7%, 70%), longe das mãos na mesa.
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'
f = f'{BASE}/PAINEL-NORA41.html'
s = open(f, encoding='utf-8').read()
m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
p = json.loads(m.group(1))
mt = p['mapa_tela']
for n in mt['numeros']:
    if n['t'] == '888':
        n.update({"x": 5, "y": 63, "onde": "na borda esquerda, ao lado do braço, acima do porta-retrato"})
mt['legenda'] = [56.5, 59.5]
def xy(n): return f"X {round(n['x'] * 7.2 - 360)} · Y {round(640 - n['y'] * 12.8)}"
NUM_TXT = '; '.join(f"{n['t']} {n['cor_nome']} {n['cor']}, tamanho {n['tamanho']}, {n['onde']} ({xy(n)})" for n in mt['numeros']) + '.'
for st in mt['estilos']:
    if st['nome'].startswith('Números fixos'):
        st['obs'] = NUM_TXT
    elif st['nome'].startswith('Texto do story'):
        st['obs'] = 'Centralizado em X 0 · Y -102 (58% da altura): no peito dela, logo ACIMA do porta-retrato (as mãos já estão na mesa dos 5 aos 8 s).'
    elif st['nome'].startswith('Seta'):
        st['obs'] = 'Dos 5 aos 8 s, junto com o texto do story: à esquerda, em X -310 · Y -256 (acima da mão dela na mesa), apontando para baixo, para a foto do perfil.'
mt['regras'] = [
    'Lugares conferidos na nora41-IMG, na nora41-FIM e no clipe (29/10): números longe do rosto, das mãos, da fita e do porta-retrato.',
    'Este vídeo não tem fala, então não tem legenda na tela. São 4 textos: os números fixos (222, 888 e 11:11), o texto do topo (o clipe todo) e, dos 5 aos 8 s, o texto do story e a seta.',
    'O cartão do porta-retrato fica de 68% a 78% da altura: nada em cima dele. O texto do story vai ACIMA do porta-retrato (Y -102), não embaixo.',
    'Confira o quadro dos 5 s: se as mãos ainda estiverem descendo por cima do texto do story, comece o texto e a seta aos 5,5 s.',
]
e = p['edicao_linha']
e[1]['como'] = 'Cada número de uma cor e de um tamanho, num lugar, parados do primeiro ao último quadro: ' + NUM_TXT
e[2]['como'] = ('Texto do story: branco, tamanho 9, em 1 linha, em X 0 · Y -102 (no peito dela, logo acima do porta-retrato). '
                'Junto, a seta vermelha à esquerda (X -310 · Y -256), apontando para baixo, para a foto do perfil.')
pc = p['pecas']['lista']
for it in pc:
    if it['nome'] in ('nora41-IMG', 'nora41-FIM', 'nora41-CLIPE-fita'):
        it['status'] = 'feito'
p['pecas']['decisao'].insert(0, 'Imagens e clipe conferidos (29/10 ~17h30): grafia certa, a Nora certa, uma tira só, fita colada até o fim, cartão parado, sem fala. O porta-retrato saiu mais baixo (cartão a 68%-78%): texto do story acima dele e 888 e seta reposicionados.')
open(f, 'w', encoding='utf-8').write(s[:m.start(1)] + json.dumps(p, ensure_ascii=False) + s[m.end(1):])
print(NUM_TXT)
