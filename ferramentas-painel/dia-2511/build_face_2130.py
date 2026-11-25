# Painel do post extra do Face das 21h30 de 25/11/2026 ("pode montar" do aluno às ~17h20: "2- PODE MONTAR. OK, CONCORDO COM OS PONTOS ALI"). Derivado do build_face_1600.py.
#   nora77-VAR2511-FACE: o corpo cinza do nora77 (1 vez no Face: 3,4 mil e 4 cliques) com a ABERTURA QUE PERGUNTA (o "spark a question" do Robert, v10),
#   a frase do roteiro 1 da pesquisa oficial ("…You've been seeing it for weeks, haven't you? The same numbers on the clock."); a resposta vem no fim, na leitura.
# Original (16h) ("pode montar" do aluno às ~15h25: "faz o painel do Face só das 16 horas").
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
B23.ROUPA = B24.ROUPA77   # o moletom cinza do nora77
assert 'heather-gray' in B23.ROUPA
FB, COMUNS, MODELO = B23.FB, B23.COMUNS, B23.MODELO
assert FB.endswith('&aff=dl7zx6ks')
IMG_B = B24.IMG_B77                     # d2411-cinza-IMG-B: a Nora de moletom cinza, no sofá, com o copo e a bandeira no quadro
NN = 'nora77-VAR2511-FACE'

# A pesquisa oficial, roteiro 2 (modelado de "If you see 11:11, this is for you…", 4,3 milhões): "If you keep seeing 11:11, this is for you."
# Os números falados por extenso (a SPEECH RULE). O T03: 2 dias à frente, como no original (o nora75 foi postado em 23/11 com o dia 25),
# porque o Face distribui por 1 a 2 dias (nora76-FACE: 4,5 mil com ~36 h).
T01 = "If this found you today, don't scroll. You've been seeing the same numbers on the clock for weeks, haven't you?"
T03 = "I don't know your name or what you did, but if this video found you before Friday, November twenty-seventh, get ready."
CTA = B24.CTA_FACE77                    # "That's why I left you a quick reading. Check the first comment below to get your reading."
assert T03.replace('Friday, November twenty-seventh', 'Wednesday, November twenty-fifth') == B23.FALA[2]
G01 = 'she speaks with a calm, knowing look and small natural head movements'
G03 = B23.GESTO[2]                      # o mesmo gesto do T03 do corpo
GCTA = B24.GESTO_CTA_FACE
TAKES = [('T01', 'a pergunta (no lugar do T01 da canela)', T01, G01, 'd2511-cinza-T01-pergunta', 1),
         ('T03', 'a data nova (no lugar do T03 do nora77)', T03, G03, 'd2511-cinza-T03-sexta', 3)]

# A ordem e os nomes para a FusionZ (junta pela ordem do nome): os 2 novos + os 6 do nora77 (nomes do painel de 24/11, d2411-cinza-TNN-...).
ORDEM = [('01', 'd2511-cinza-T01-pergunta', 'novo', "If this found you today, don't scroll…"),
         ('02', 'd2411-cinza-T02-mulher-deitada', 'nora75', "There's a woman lying down…"),
         ('03', 'd2511-cinza-T03-sexta', 'novo', "I don't know your name… before Friday…"),
         ('04', 'd2411-cinza-T04-fe', 'nora75', "The universe saw your faith…"),
         ('05', 'd2411-cinza-T06-arcanjo', 'nora75', "Saint Michael the Archangel sent a warning…"),
         ('06', 'd2411-cinza-T07-correntes', 'nora75', "I can already see the chains…"),
         ('07', 'd2411-cinza-T11-alinhada', 'nora75', "But the universe is warning me…"),
         ('08', 'd2411-cinza-T15-FACE-cta-comentario', 'nora75', "That's why I left you a quick reading…")]
ORDEM_TXT = [f'{n}-{arq} ({"NOVO" if o == "novo" else "do nora77"}: “{c}”)' for n, arq, o, c in ORDEM]
assert [a for _, a, o, _ in ORDEM if o == 'novo'] == [t[4] for t in TAKES]
for _n, _a, _o, _c in ORDEM:
    if _o == 'nora75' and not _a.endswith('cta-comentario'):
        _i = int(_a.split('-T')[1][:2]) - 1
        assert _a == f'd2411-cinza-T{_i + 1:02d}-{B23.SUF[_i]}' or _a.endswith('T15-FACE-cta-comentario'), _a
        assert _a.endswith('cta-comentario') or B23.FALA[_i].startswith(_c.split('…')[0]), _a

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
    P = B23.base('nora77')
    P['imagens_titulo'] = f'Imagem das falas (a {IMG_B}, a mesma do nora77)'
    P['refs'] = [f'{IMG_B} nos 2 takes']
    P['imagens'] = [{'rotulo': f'IMAGEM 1 · {IMG_B}', 'cena': 'a mesma do nora77 (moletom cinza, o copo de água de canela na mão, a bandeira no quadro)', 'anexar': f'a {IMG_B}'}]
    P['roteiro'] = {
        'id': 'NORA77-VAR2511-FACE',
        'titulo': 'nora77-VAR2511-FACE · só Face, ~0h00 de 26/11 (era 21h30; passou porque o nora79 foi para ~21h) · o corpo do nora77 (moletom cinza) com a abertura que pergunta e a data nova',
        'duracao_total': 70,
        'descricao_instagram': 'Não vai ao Insta: este post é só do Face.',
        'descricao_face': ("You've been seeing the same numbers for weeks, haven't you? ✨ Your reading is waiting in the first comment 🔮\n"
                           '#manifestation #angelnumbers #2027'),
    }
    P['videos'] = [{'rotulo': rot, 'cena': cena, 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({IMG_B})', 'acao': '', 'b_roll': '',
                    'fala': f, 'movimentacao': B23.mov(g), 'arquivo': arq} for rot, cena, f, g, arq, _ in TAKES]
    P['texto_tela'] = {'hook': '', 'hook_comeca': '—', 'hook_termina': '—', 'hook_alt': '', 'extras': []}
    B23.mapa(P)
    P['comentario_fixado'] = {'insta': 'Não vai ao Insta.',
                              'face': 'The numbers keep finding you for a reason ✨ your reading is waiting for you here 👉 ' + FB}
    assert P['comentario_fixado']['face'].endswith('&aff=dl7zx6ks')
    P['ocultar_cenas'] = True
    ct = P['central']
    ct['config'] = []
    ct['colagens'] = [{'titulo': f'{rot}: {cena}', 'fala': f, 'movimentacao': [B23.mov(g)], 'takes': [k]} for k, (rot, cena, f, g, _, _) in enumerate(TAKES)]
    ct['conferir'] = f'Conferir os 2 takes: a Nora da {IMG_B}, de moletom cinza, SEM a lua e SEM as estrelinhas, com o copo; ela fala uma vez só e fecha a boca no fim.'
    p1, p3 = (prompt(f, g, arq, c) for _, _, f, g, arq, c in TAKES)
    ct['agente'] = {
        'titulo': 'No Muse: os 2 prompts, um por mensagem (sem a Central)',
        'imagem': IMG_B,
        'intro': (f'2 clipes no Muse, NA MESMA CONVERSA da Nora (a do nora75 ao nora79: a voz). Em cada um: anexe a {IMG_B} e cole o prompt, um clipe por mensagem.'),
        'aviso_tag': f'o prompt do T01 (o passo 1), com a {IMG_B} anexada; os 2 prompts já são completos (voz, movimentação, continuidade): a Central não entra',
        'aviso': p1,
        'passos': [f'O T01 (a pergunta): anexe a {IMG_B}, clique em “Copiar aviso” (o prompt do T01, acima) e cole. Salve como {TAKES[0][4]}. ~1 min.',
                   f'O T03 (a data nova, “before Friday, November twenty-seventh”): anexe a {IMG_B} e cole o prompt abaixo. Salve como {TAKES[1][4]}. PROMPT: ' + p3,
                   'Confira os 2: o moletom cinza; sem a lua e sem as estrelinhas; o copo na mão; ela fala uma vez só e fecha a boca no fim; a voz igual à do nora77. '
                   'Se o Muse recusar: “Generate it again, exactly as written.”',
                   'Renomeie os 8 arquivos com o número na frente (a FusionZ junta pela ordem do nome; os 2 novos e os 6 do nora77 juntos): ' + ' · '.join(ORDEM_TXT) + '.',
                   'Monte como na seção “Cortar os silêncios” e no CapCut (abaixo) e me mande o ' + NN + '-montado.'],
    }
    P['silencio'] = {
        'intro': ('Arraste na “M2M FusionZ” os 8 arquivos de uma vez (01 a 08), já renomeados com o número na frente. A ferramenta junta pela ordem do nome. '
                  'Sai 1 arquivo só. “Zoom nos cortes” = DESLIGADO.'),
        'nome': NN + '-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': '01 a 08 (o 01 e o 03 são os novos)',
        'depois': ['Suba os 8 e espere a Prévia.', 'Confira a primeira palavra do 01 (“If this found you today…”) e a última do 08 (“…get your reading.”).',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', 'Clique em Cortar e baixar e salve como ' + NN + '-cortado.'],
    }
    P['edicao_linha'] = [
        {'quando': 'O que vai no vídeo', 'texto': 'T01 novo (a pergunta) + T02 do nora77 + T03 novo (a data) + T04 (eu tiro o “money”), T06, T07 e T11 do nora77 + o T15 do Face do nora77 (o comentário)',
         'como': 'Ficam fora, como no nora77-FACE: o T05 (a ameaça), o T08, o T09, o T10, o T12 e o T13.'},
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {NN}-cortado', 'como': 'Começa direto no 01 (a pergunta), sem hook.'},
        {'quando': '1. Do começo ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB, do 1º ao último quadro', 'como': 'Assim a música não some no meio nem no fim.'},
        {'quando': '2. Exportar e me mandar até ~23h30', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'1080×1920, nome {NN}-montado (acima de 30 MB, link do Drive). Eu devolvo em ~15 min com a legenda simples, o 11:11✨ e a faixa do comentário, e tiro o “money” do 04. A bandeira já está na cena (o quadro do nora77).'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': [{'nome': IMG_B, 'tipo': 'imagem das falas', 'status': 'reutilizar', 'onde': 'A mesma do nora77.', 'descricao': 'Moletom cinza, o copo na mão.'}]
                 + [{'nome': arq, 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{f}”'} for _, _, f, _, arq, _ in TAKES]
                 + [{'nome': 'o T02, o T04, o T06, o T07, o T11 e o T15 do Face do nora77', 'tipo': 'corpo', 'status': 'reutilizar', 'onde': 'Os arquivos do nora77 que você tem.', 'descricao': 'O mesmo corpo.'}],
        'decisao': [
            'O QUE ESTE VÍDEO TESTA: a abertura que pergunta (o “spark a question” do Robert; a frase do roteiro 1 da pesquisa oficial) contra a que qualifica (o 11:11 '
            'das 16h e as letras do nora77-FACE). A medida, com ~24 h: as views, os 3 s, o tempo médio e os cliques no link (Insights do Reel).',
            '2 clipes no Muse + 6 arquivos do nora77 que você já tem: 8 na FusionZ, numerados de 01 a 08, e a música no CapCut.',
            'Só no Face, à ~0h00 (era 21h30; o nora79 foi para ~21h a 21h30, e no Face ficam 2 h ou mais entre os posts). Legenda sem pedido de comentário; o comentário da Página (um texto novo, a regra de 25/11) com o link FACE inteiro, sem a prévia, fixado pelo app.',
        ],
    }
    P['story'] = {'ja_postado': True, 'nota': 'O story novo vai à noite, no Insta e no Face no mesmo horário (o painel do nora79).'}
    P['ordem'] = ['pecas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    txt = json.dumps(P, ensure_ascii=False)
    for velho in ('November twenty-fifth', 'Wednesday', 'camiseta preta', 'eleven eleven', 'bandeirinha'):
        assert velho not in txt, velho
    return P


if __name__ == '__main__':
    P = painel()
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>Painel nora77-VAR2511-FACE · a pergunta + o corpo do nora77 · Face 21h30 de 25/11</title>', html, count=1)
    (R / 'PAINEL-NORA77-VAR2511-FACE.html').write_text(html, encoding='utf-8')
    print('ok', len(html), 'bytes')
