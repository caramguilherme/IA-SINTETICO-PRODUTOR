# 29/10/2026 ~12h (pedido do aluno): o longo ganha o Take 2 "claim this energy" (seguir, 222 e enviar logo no começo);
# o corpo A passa a ser os takes 3 a 11 e o nora37-T03 vira o Take 12. Muda os painéis do nora40, nora42 e nora43 no lugar
# (mantém números espalhados, cores, legendas e respostas do Face já aplicados).
import re, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from falas2910 import takes, checar, CORPO, T11_FALA
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

def ler(n):
    f = f'{BASE}/PAINEL-NORA{n}.html'; s = open(f, encoding='utf-8').read()
    m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S); return f, s, m, json.loads(m.group(1))
def gravar(f, s, m, p):
    open(f, 'w', encoding='utf-8').write(s[:m.start(1)] + json.dumps(p, ensure_ascii=False) + s[m.end(1):])
def troca(p, pares):
    js = json.dumps(p, ensure_ascii=False)
    for a, b in pares:
        assert a in js, a
        js = js.replace(a, b)
    return json.loads(js)
def videos_de(T):
    return [{'rotulo': f'V{i+1}', 'cena': f'Take {i+1}/12 · {c}', 'duracao': '10', 'primeiro_quadro': 'IMAGEM 1', 'acao': '(ver movimentação)',
             'b_roll': '', 'fala': fl, 'movimentacao': mv, 'arquivo': a} for i, (a, c, fl, mv) in enumerate(T)]

ED_SETA = ('Do Take 10 até o fim', 'Do Take 11 até o fim')
FAIXA = ('Começa em “Don’t tell anyone”.', 'Começa em “Before you scroll”.')
DEC = 'O pedido vem também no começo (Take 2: seguir, 222 e mandar para si, o “claim this energy” dos virais curtos), porque quase todo mundo sai antes do fim; os selos do fim continuam (Takes 10 a 12).'

# ---------- nora40 ----------
T40 = takes('nora40'); checar(T40); assert len(T40) == 11
f, s, m, p = ler(40)
p['videos'] = videos_de(T40)
c = p['central']['colagens'][0]
c.update({'titulo': 'nora40 (11 takes)', 'fala': ' '.join(t[2] for t in T40), 'movimentacao': [t[3] for t in T40], 'takes': list(range(11))})
p = troca(p, [
 ('Cole a fala inteira e as 10 linhas de movimentação', 'Cole a fala inteira e as 11 linhas de movimentação'),
 ('Confira: 10 takes de 10 s.', 'Confira: 11 takes de 10 s.'),
 ('150 créditos (conta de 404: ~337 → ~187). Renomeie os takes com os nomes do painel (T01 a T10, com 2 dígitos).', '165 créditos (conta de 404: ~337 → ~172). Renomeie os takes com os nomes do painel (T01 a T11, com 2 dígitos).'),
 ('O Take 11 NÃO é gerado: faça uma cópia do nora37-T03-cta-222-story e renomeie para nora40-T11-cta-222-story.', 'O Take 12 NÃO é gerado: faça uma cópia do nora37-T03-cta-222-story e renomeie para nora40-T12-cta-222-story.'),
 ('Guarde os takes 2 a 11:', 'Guarde os takes 2 a 12:'),
 ('Me mande a transcrição dos 10 takes novos', 'Me mande a transcrição dos 11 takes novos'),
 ('suba nora40-T01 a nora40-T11 de uma vez', 'suba nora40-T01 a nora40-T12 de uma vez'),
 ('Vou te enviar 10 prompts', 'Vou te enviar 11 prompts'),
 ('O agente gera os 10 vídeos', 'O agente gera os 11 vídeos'),
 ('Se ele gerar menos de 10,', 'Se ele gerar menos de 11,'),
 ('corpo A dos virais em 11 takes (~90 s): signos e datas → segredo', 'corpo A dos virais em 12 takes (~100 s): signos e datas → pedido no começo (seguir, 222, mandar para si) → segredo'),
 ('(nora40-cortado: os takes 1 a 11)', '(nora40-cortado: os takes 1 a 12)'),
 ('Barato: os 10 takes novos na nora37-IMG (150) + o nora37-T03 como Take 11', 'Barato: os 11 takes novos na nora37-IMG (165) + o nora37-T03 como Take 12'),
 ('Take 10 troca o toque duplo por seguir', 'Take 11 troca o toque duplo por seguir'),
 ('Os takes 2 a 11 deste vídeo servem ao nora42 e ao nora43', 'Os takes 2 a 12 deste vídeo servem ao nora42 e ao nora43'),
 ED_SETA, FAIXA,
 ('Primeiro e último quadro dos 10 takes novos.', 'Primeiro e último quadro dos 11 takes novos.'),
 ('Take 11. Para a ferramenta de corte, renomeie a cópia para nora40-T11-cta-222-story.', 'Take 12. Para a ferramenta de corte, renomeie a cópia para nora40-T12-cta-222-story.'),
])
p['roteiro']['duracao_total'] = 100
L = [x for x in p['pecas']['lista'] if not x['nome'].startswith('nora40-T')]
gerar = []
for (a, cena, fl, mv) in T40:
    gerar.append({'nome': a, 'tipo': 'gancho' if '-T01-' in a else ('CTA' if 'cta' in a else 'corpo'), 'status': 'gerar', 'creditos': 15,
                  'descricao': f'{cena}: “{fl}”', 'base': ('Pedido do começo dos virais curtos (“claim this energy”, R03/R05, R11)' if '-T02-' in a else 'Corpo A (x1 a x5, w3 a w5, L1)' + (' + selo de seguir (a4/a5)' if '-T11-' in a else '')),
                  'serve': 'Só deste vídeo (cada grupo de signos tem o seu Take 1).' if '-T01-' in a else 'nora42 e nora43 (cópia renomeada) e os próximos longos.'})
p['pecas']['lista'] = L[:2] + gerar + L[2:]
p['pecas']['decisao'].insert(1, DEC)
gravar(f, s, m, p)

# ---------- nora42 e nora43 ----------
for n in (42, 43):
    f, s, m, p = ler(n)
    for v in p['videos']:
        v['cena'] = v['cena'].replace('Take 1/11', 'Take 1/12')
    p = troca(p, [
     ('Os takes 2 a 11 NÃO são gerados', 'Os takes 2 a 12 NÃO são gerados'),
     (f'suba nora{n}-T01 a nora{n}-T11 de uma vez', f'suba nora{n}-T01 a nora{n}-T12 de uma vez'),
     ('takes 2 a 11 do nora40 (~90 s)', 'takes 2 a 12 do nora40 (~100 s)'),
     ('cópias dos takes 2 a 11 do nora40', 'cópias dos takes 2 a 12 do nora40'),
     ('Primeiro e último quadro do Take 1, a mesma dos takes 2 a 11.', 'Primeiro e último quadro do Take 1, a mesma dos takes 2 a 12.'),
     ED_SETA, FAIXA,
    ])
    p['roteiro']['duracao_total'] = 100
    keep = [x for x in p['pecas']['lista'] if not x['nome'].startswith('nora40-T')]
    reuso = []
    for suf, cena, fl, ex in CORPO:
        reuso.append({'nome': f'nora40-{suf}', 'de': f'nora40-{suf}', 'tipo': 'CTA (do nora40)' if 'cta' in suf else 'corpo (do nora40)',
                      'status': 'reutilizar', 'creditos': 15, 'fala': fl, 'descricao': f'Para a ferramenta de corte, renomeie a cópia para nora{n}-{suf}.'})
    reuso.append({'nome': 'nora40-T12-cta-222-story', 'de': 'nora40-T12-cta-222-story (a cópia do nora37-T03)', 'tipo': 'CTA (do nora37)', 'status': 'reutilizar',
                  'creditos': 15, 'fala': T11_FALA, 'descricao': f'Para a ferramenta de corte, renomeie a cópia para nora{n}-T12-cta-222-story.'})
    p['pecas']['lista'] = keep + reuso
    p['pecas']['decisao'].insert(1, DEC)
    gravar(f, s, m, p)
print('ok')
