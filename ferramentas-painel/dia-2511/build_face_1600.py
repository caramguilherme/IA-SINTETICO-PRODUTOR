# Painel do post extra do Face das 16h de 25/11/2026 ("pode montar" do aluno às ~15h25: "faz o painel do Face só das 16 horas").
#   nora75-VAR2511-FACE: o corpo da maioria de camiseta preta (o do nora75, que já existe; o corpo que vende no Face: nora76-FACE 4,5 mil e 3 cliques)
#   com 3 clipes novos no Muse: o T01 do 11:11 (a abertura do roteiro 2 da pesquisa oficial, "If you keep seeing 11:11, this is for you."),
#   o T03 com a data nova (o original dizia "before Wednesday, November twenty-fifth", que já passou) e o CTA para o 1º comentário (o do nora77-FACE).
#   A regra do Face de 25/11 01h20 (4 por dia; R92): às 16h, um corpo que já rodou no Face + um Take 1 novo, gerado.
#   Fora do Face, como no nora77-FACE: o T05 (a ameaça), o T08 (os 7 minutos), o T09 (os selos), o T10 ("amanhã às 10"), o "money" do T04 e o T12/T13 (o CTA do story).
#   Montagem (25/11 15h43, o aluno): do jeito de sempre, os 3 novos + 5 do nora75 na FusionZ, numerados de 01 a 08, e a música no CapCut o vídeo todo.
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2511/build_face_1600.py
import json, re, pathlib, importlib.util

R = pathlib.Path(__file__).resolve().parents[2]
def _mod(nome, caminho):
    s = importlib.util.spec_from_file_location(nome, R / caminho)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
B23 = _mod('b2311', 'ferramentas-painel/dia-2311/build_dia_2311.py')
B24 = _mod('b2411', 'ferramentas-painel/dia-2411/build_dia_2411.py')
B23.ROUPA = 'her plain black crew-neck short-sleeve t-shirt with no logo'   # o build_dia_2411 trocou para o cinza ao carregar; o nora75 é de camiseta preta
assert 'black' in B23.ROUPA and 'black' in B23.livre()
FB, COMUNS, MODELO = B23.FB, B23.COMUNS, B23.MODELO
assert FB.endswith('&aff=dl7zx6ks')
IMG_B = B23.IMG_B                       # d2311-sofa-IMG-B: a Nora de camiseta preta com o copo de água de canela (a do nora75 e do nora76)
NN = 'nora75-VAR2511-FACE'

# A pesquisa oficial, roteiro 2 (modelado de "If you see 11:11, this is for you…", 4,3 milhões): "If you keep seeing 11:11, this is for you."
# Os números falados por extenso (a SPEECH RULE). O T03: 2 dias à frente, como no original (o nora75 foi postado em 23/11 com o dia 25),
# porque o Face distribui por 1 a 2 dias (nora76-FACE: 4,5 mil com ~36 h).
T01 = "If you keep seeing eleven eleven, this is for you."
T03 = "I don't know your name or what you did, but if this video found you before Friday, November twenty-seventh, get ready."
CTA = B24.CTA_FACE77                    # "That's why I left you a quick reading. Check the first comment below to get your reading."
assert T03.replace('Friday, November twenty-seventh', 'Wednesday, November twenty-fifth') == B23.FALA[2]
G01 = B23.GESTO76                       # ela fala, séria, com pequenos movimentos de cabeça (o T01B do nora76)
G03 = B23.GESTO[2]                      # o mesmo gesto do T03 do nora75
GCTA = B24.GESTO_CTA_FACE
TAKES = [('T01', 'o 11:11 (no lugar do T01 da canela)', T01, G01, 'd2511-preto-T01-1111', 1),
         ('T03', 'a data nova (no lugar do T03 do nora75)', T03, G03, 'd2511-preto-T03-sexta', 3),
         ('T15', 'o CTA para o 1º comentário (no lugar do T12 e do T13)', CTA, GCTA, 'd2511-preto-T15-FACE-cta-comentario', 13)]

# 25/11 15h43 (o aluno vai montar do jeito de sempre, na FusionZ e no CapCut, com os 5 clipes do nora75 que ele tem): a ordem e os nomes para a FusionZ,
# que junta pela ordem do nome; os nomes do nora75 são os do painel de 23/11 (d2311-sofa-TNN-...).
ORDEM = [('01', 'd2511-preto-T01-1111', 'novo', "If you keep seeing eleven eleven…"),
         ('02', 'd2311-sofa-T02-mulher-deitada', 'nora75', "There's a woman lying down…"),
         ('03', 'd2511-preto-T03-sexta', 'novo', "I don't know your name… before Friday…"),
         ('04', 'd2311-sofa-T04-fe', 'nora75', "The universe saw your faith…"),
         ('05', 'd2311-sofa-T06-arcanjo', 'nora75', "Saint Michael the Archangel sent a warning…"),
         ('06', 'd2311-sofa-T07-correntes', 'nora75', "I can already see the chains…"),
         ('07', 'd2311-sofa-T11-alinhada', 'nora75', "But the universe is warning me…"),
         ('08', 'd2511-preto-T15-FACE-cta-comentario', 'novo', "That's why I left you a quick reading…")]
ORDEM_TXT = [f'{n}-{arq} ({"NOVO" if o == "novo" else "do nora75"}: “{c}”)' for n, arq, o, c in ORDEM]
assert [a for _, a, o, _ in ORDEM if o == 'novo'] == [t[4] for t in TAKES]
for _n, _a, _o, _c in ORDEM:
    if _o == 'nora75':
        _i = int(_a.split('-T')[1][:2]) - 1
        assert B23.nome(_i) == _a and B23.FALA[_i].startswith(_c.split('…')[0]), _a

for rot, _, f, g, _, _ in TAKES:
    assert len(f.split()) <= 22, (rot, len(f.split()))
    fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", B23.mov(g).lower())
    sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS - B24.EXTRA
    assert not sobra, (rot, sobra)
    for w in ('link', 'free', 'card', 'tarot', 'private', 'money', 'amen', 'comment', 'seal', 'save', 'send'):
        if w == 'comment' and 'the first comment below' in f:
            continue                          # o CTA manda para o comentário da Página (onde está o link): não é pedido de comentário
        assert w not in fw, (rot, w)


def prompt(f, g, arq, clip):
    t = B23.prompt_manual(f, B23.mov(g), 'the stemmed glass of cinnamon water in her hand', arq, clip, B23.N)
    # o prompt_manual pede "about 8 seconds of speech" (feito para falas de ~20 palavras); com 9 palavras, isso pode fazer o Muse arrastar
    # a fala ou pôr palavra a mais. A duração vai pela conta de ~2,7 palavras por segundo (155 a 180 por minuto).
    seg = max(3, round(len(f.split()) / 2.7))
    assert 'about 8 seconds of speech' in t
    return t.replace('about 8 seconds of speech', f'about {seg} seconds of speech')


def painel():
    P = B23.base('nora75')
    P['imagens_titulo'] = f'Imagem das falas (a {IMG_B}, a mesma do nora75 e do nora76)'
    P['refs'] = [f'{IMG_B} nos 3 takes']
    P['imagens'] = [{'rotulo': f'IMAGEM 1 · {IMG_B}', 'cena': 'a mesma do nora75 (camiseta preta, o copo de água de canela na mão)', 'anexar': f'a {IMG_B}'}]
    P['roteiro'] = {
        'id': 'NORA75-VAR2511-FACE',
        'titulo': 'nora75-VAR2511-FACE · só Face, 16h de 25/11 · o corpo do nora75 (camiseta preta) com a abertura do 11:11, a data nova e o CTA para o comentário',
        'duracao_total': 70,
        'descricao_instagram': 'Não vai ao Insta: este post é só do Face.',
        'descricao_face': ('If you keep seeing 11:11, this is for you ✨ Your reading is waiting in the first comment 🔮\n'
                           '#manifestation #1111 #archangelmichael #2027'),
    }
    P['videos'] = [{'rotulo': rot, 'cena': cena, 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({IMG_B})', 'acao': '', 'b_roll': '',
                    'fala': f, 'movimentacao': B23.mov(g), 'arquivo': arq} for rot, cena, f, g, arq, _ in TAKES]
    P['texto_tela'] = {'hook': '', 'hook_comeca': '—', 'hook_termina': '—', 'hook_alt': '', 'extras': []}
    B23.mapa(P)
    P['comentario_fixado'] = {'insta': 'Não vai ao Insta.',
                              'face': 'If 11:11 keeps finding you, your reading is waiting for you here ✨ 👉 ' + FB}
    assert P['comentario_fixado']['face'].endswith('&aff=dl7zx6ks')
    ct = P['central']
    ct['config'] = []
    ct['colagens'] = [{'titulo': f'{rot}: {cena} (no Muse, sem a Central)', 'fala': f, 'movimentacao': [B23.mov(g)], 'takes': [k]}
                      for k, (rot, cena, f, g, _, _) in enumerate(TAKES)]
    ct['conferir'] = (f'Conferir cada take: a Nora da {IMG_B}, de camiseta preta, SEM a lua e SEM as estrelinhas, com o copo de água de canela; '
                      'ela fala uma vez só, diz os números por extenso e fecha a boca no fim.')
    p1, p3, pc = (prompt(f, g, arq, c) for _, _, f, g, arq, c in TAKES)
    ct['agente'] = {
        'imagem': IMG_B,
        'intro': (f'3 clipes no Muse, NA MESMA CONVERSA em que você gerou o nora75 e o nora76 (o prompt pede a mesma voz dos clipes dessa conversa). '
                  f'Em cada um: anexe a {IMG_B} e cole o prompt, um clipe por mensagem, nesta ordem.'),
        'aviso_tag': f'o prompt do T01 (o passo 1), com a {IMG_B} anexada',
        'aviso': p1,
        'passos': [f'O T01 (o 11:11): anexe a {IMG_B}, clique em “Copiar aviso” (o prompt do T01, acima) e cole. Salve como {TAKES[0][4]}. ~1 min.',
                   f'O T03 (a data nova, “before Friday, November twenty-seventh”): anexe a {IMG_B} e cole o prompt abaixo. Salve como {TAKES[1][4]}. PROMPT: ' + p3,
                   f'O T15 (o CTA para o 1º comentário): anexe a {IMG_B} e cole o prompt abaixo. Salve como {TAKES[2][4]}. PROMPT: ' + pc,
                   'Confira os 3: a camiseta preta; sem a lua e sem as estrelinhas; o copo na mão; ela fala uma vez só e fecha a boca no fim; a voz igual à do nora75. '
                   'Se o Muse recusar: “Generate it again, exactly as written.” Se a voz sair diferente, gere de novo na mesma conversa pedindo '
                   '“exactly the same voice as the other clips of this video”.',
                   'Renomeie os 8 arquivos com o número na frente (a FusionZ junta pela ordem do nome; os 3 novos e os 5 do nora75 juntos): ' + ' · '.join(ORDEM_TXT) + '.',
                   'Monte como na seção “Cortar os silêncios” e no CapCut (abaixo) e me mande o ' + NN + '-montado.'],
    }
    P['silencio'] = {
        'intro': ('Arraste na “M2M FusionZ” os 8 arquivos de uma vez (01 a 08), já renomeados com o número na frente. A ferramenta junta pela ordem do nome. '
                  'Sai 1 arquivo só. “Zoom nos cortes” = DESLIGADO.'),
        'nome': NN + '-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': '01 a 08 (o 01, o 03 e o 08 são os novos)',
        'depois': ['Suba os 8 e espere a Prévia.', 'Confira a primeira palavra do 01 (“If you keep seeing…”) e a última do 08 (“…get your reading.”).',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', 'Clique em Cortar e baixar e salve como ' + NN + '-cortado.'],
    }
    P['edicao_linha'] = [
        {'quando': 'O que vai no vídeo', 'texto': 'T01 novo (o 11:11) + T02 do nora75 + T03 novo (a data) + T04 (eu tiro o “money”), T06, T07 e T11 do nora75 + T15 novo (o comentário)',
         'como': ('Ficam fora, como no nora77-FACE: o T05 (a ameaça), o T08 (os 7 minutos e o “send to yourself”), o T09 (os selos e o amen), o T10 (“amanhã às 10”), '
                  'o T12 e o T13 (o CTA do story, que no Face quase não é visto).')},
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {NN}-cortado', 'como': 'Começa direto no 01 (o 11:11), sem hook.'},
        {'quando': '1. Do começo ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB, o vídeo todo, do 1º quadro ao último', 'como': 'Assim a música não some no meio nem no fim (o 03 e o 08 são novos).'},
        {'quando': '2. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'1080×1920, nome {NN}-montado (acima de 30 MB, link do Drive). Eu devolvo em ~15 min com a legenda simples, o 11:11✨, a bandeirinha dos EUA pequena (a cena do nora75 não tem bandeira), a faixa do comentário e a seta grande, e tiro o “money” do 04.'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': [{'nome': IMG_B, 'tipo': 'imagem das falas', 'status': 'reutilizar', 'onde': 'A mesma do nora75 e do nora76.', 'descricao': 'Camiseta preta, o copo na mão.'}]
                 + [{'nome': arq, 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{f}”'} for _, _, f, _, arq, _ in TAKES]
                 + [{'nome': 'o T02, o T04, o T06, o T07 e o T11 do nora75', 'tipo': 'corpo', 'status': 'reutilizar', 'onde': 'Saem do nora75-montado (aqui).', 'descricao': 'O mesmo corpo.'}],
        'decisao': [
            'O QUE ESTE VÍDEO TESTA: a abertura do 11:11 (um dos tipos de Take 1 do rodízio do Face: signo, 11:11, data, letras) com o corpo que vende no Face. '
            'A medida, com ~24 h: os cliques no link (nos Insights do Reel) e as views, contra o nora76-FACE (as letras: 4,5 mil, 3 cliques) e o nora75-FACE (a canela: 636).',
            '3 clipes no Muse, na conversa do nora75, + 5 clipes do nora75 que você já tem (o T02, o T04, o T06, o T07 e o T11): 8 arquivos na FusionZ, numerados de 01 a 08, e a música no CapCut.',
            'Só no Face, às 16h (ou assim que eu devolver: atrasou, posta assim que der). Legenda sem pedido de comentário; o comentário da Página com o link FACE inteiro, sem a prévia, fixado pelo app.',
            'Antes de postar: o story do Face está no ar até ~00h20 de 26/11.',
        ],
    }
    P['story'] = {'ja_postado': True, 'nota': 'O story do Face (o do “gift”, postado às 00h20) vence às ~00h20 de 26/11: nada a fazer agora.'}
    P['ordem'] = ['pecas', 'agente', 'cenas', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    txt = json.dumps(P, ensure_ascii=False)
    for velho in ('November twenty-fifth', 'Wednesday', '01h15', 'nora78-montado', 'nora77-cortado'):
        assert velho not in txt, velho
    return P


if __name__ == '__main__':
    P = painel()
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>Painel nora75-VAR2511-FACE · o 11:11 + o corpo do nora75 · Face 16h de 25/11</title>', html, count=1)
    (R / 'PAINEL-NORA75-VAR2511-FACE.html').write_text(html, encoding='utf-8')
    print('ok', len(html), 'bytes')
