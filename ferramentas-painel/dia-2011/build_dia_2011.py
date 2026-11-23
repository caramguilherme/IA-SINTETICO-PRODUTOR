# Painéis do dia 20/11/2026 ("pode montar o 73 e o 74", ~17h40).
# nora73 (Insta 19h30; Face 0h00 de 21/11): o nora72 inteiro (a canela no carro + a fala dos 3 sinais) com UMA frase nova na frente,
#   as letras do nome ("If your name starts with the letter A, J, M, K, C, E, S, L, R, T or H, pay close attention."). 1 take no Muse.
#   Fontes: o viral 52.2 (16/11), o v4 da @takedanaomi_ (20/11, a mesma frase) e o ini1811 (o único post que levou gente ao perfil).
# nora74 (Insta às 19h30 de 23/11, segunda; o montado não chegou até as 23h40 de 22/11, então a 0h00 saiu; não gerado em 20 e 21/11; só no Insta): o campeão de volta (o nora48 a nora50), feito do zero no Muse. Ver build_nora74 abaixo.
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2011/build_dia_2011.py
import sys, json, copy, re, pathlib, importlib.util

R = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('b1911', R / 'ferramentas-painel' / 'dia-1911' / 'build_dia_1911.py')
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
MODELO = B.MODELO
FB = B.FB

# ------------------------------------------------------------------ nora73
C = dict(B.CARRO); C.update(nn='nora73', d='d2011')
FALA73 = 'If your name starts with the letter A, J, M, K, C, E, S, L, R, T or H, pay close attention.'
assert len(FALA73.split()) <= 22, len(FALA73.split())
NOME73 = 'd2011-carro-T00-letras'
MOV73 = (f'Throughout the whole 10 seconds {C["cam"]}; {C["segura"]}; with her other hand she raises it beside her shoulder and taps her thumb against each '
         'fingertip in turn as if counting, then points at the lens, with a curious, knowing look; her eyes stay on the lens; from the end of the final sentence '
         'of the take until the clip ends she keeps her lips closed and silent; no zoom and no cuts, the braid stays in place and each hand has exactly five fingers.')
fw = re.findall(r"[a-z']+", FALA73.lower()); mw = re.findall(r"[a-z']+", MOV73.lower())
assert not ((set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - B.COMUNS), 'a movimentação repete palavras da fala'
PROMPT73 = B.prompt_manual(C, FALA73, MOV73)
NORA72_DRIVE = 'https://drive.google.com/file/d/1-pAb4VN_F6kT5b-yVYJckpfMt1dVu1-s/view?usp=sharing'


def nora73():
    P = copy.deepcopy(B.pacote('PAINEL-NORA72.html'))
    P['roteiro'].update({
        'id': 'nora73-CARRO-LETRAS-2011',
        'titulo': 'nora73 · postado às 18h15 de 20/11 (Insta e Face) · o nora72 com as letras do nome na frente',
        'duracao_total': 57,
        'descricao_instagram': ('If your name starts with one of these letters, this is for you 👀 Your private reading is waiting in my story 🔮\n'
                                'Comment the first letter of your name 👇\n'
                                '#manifestation #angelnumbers #messagefromtheuniverse #2027 #lawofattraction'),
        'descricao_face': ('If your name starts with one of these letters ✨ Most people never notice these 3 signs. Your reading is waiting in my story and in the comments 🔮\n'
                           '#manifestation #1111 #messagefromtheuniverse #2027'),
    })
    P['videos'] = [{'rotulo': 'T00', 'cena': 'as letras do nome (entra antes do T01 do nora72)', 'duracao': 10,
                    'primeiro_quadro': 'IMAGEM 1 (d1711-PRE-carro-IMG-C)', 'acao': '', 'b_roll': '', 'fala': FALA73, 'movimentacao': MOV73, 'arquivo': NOME73}]
    P['texto_tela'] = {'hook': 'If your name starts with\n[one of these letters]', 'hook_comeca': 'o 1º quadro do hook', 'hook_termina': 'o fim da frase das letras',
                       'hook_alt': '', 'extras': []}
    P['comentario_fixado'] = {'insta': 'If your initial is one of them ✨ tap my profile picture above, your 2027 reading is waiting in my story',
                              'face': 'Your reading for 2027 is right here ✨ 👉 ' + FB}
    P['story'] = {'ja_postado': True,
                  'nota': 'Antes de postar, confira se o story repostado hoje (o adesivo “TAP TO CONTINUE 🎁”, com o link STORYIG) está no ar no Insta e no Face.'}
    ct = P['central']
    ct['config'] = []
    ct['colagens'] = [{'titulo': 'nora73: 1 take só (no Muse, sem a Central)', 'fala': FALA73, 'movimentacao': [MOV73], 'takes': [0]}]
    ct['conferir'] = ('Conferir o take: é a Nora da imagem C (rosto, lua com as 3 estrelinhas, trança, brincos, colar de Vênus), no carro, a mão no volante, o cinto e a '
                      'rua passando; ela diz as 11 letras uma vez só, em inglês, e fecha a boca no fim. Renomeie para ' + NOME73 + '.')
    ct['agente'] = {
        'imagem': 'd1711-PRE-carro-IMG-C',
        'intro': 'Não precisa da Central hoje: é 1 take só. No Muse, na conversa da Nora, anexe a d1711-PRE-carro-IMG-C e cole o prompt abaixo.',
        'aviso_tag': 'cole no Muse, com a d1711-PRE-carro-IMG-C anexada',
        'aviso': PROMPT73,
        'passos': [
            'No Muse, na conversa da Nora: anexe a d1711-PRE-carro-IMG-C (a mesma do nora72) e cole o prompt acima, numa mensagem só. ~1 min.',
            f'Renomeie o clipe para {NOME73}.',
            'Confira se ela diz as 11 letras (A, J, M, K, C, E, S, L, R, T, H) uma vez só e fecha a boca no fim. Se o Muse recusar: “Generate it again, exactly as '
            'written.” Se errar uma letra, gere de novo.',
        ],
    }
    P['edicao_linha'] = [
        {'quando': 'A. O montado do nora72', 'texto': 'Baixe o NORA72.mp4 do seu Drive (o montado que você me mandou)', 'como': NORA72_DRIVE},
        {'quando': 'B. Projeto novo no CapCut', 'texto': f'1º o {NOME73}, logo depois o NORA72.mp4', 'como': 'Sem FusionZ: eu corto os silêncios do take novo aqui.'},
        {'quando': 'C. O hook: NÃO põe no CapCut', 'texto': 'O hook da canela já está comigo', 'como': 'Eu emendo o hook e o flash branco antes do take novo.'},
        {'quando': 'D. Música', 'texto': 'A de sempre (“Ambient Mystical Drone”), −18 dB, só embaixo do take novo', 'como': 'O NORA72.mp4 já tem a música dele.'},
        {'quando': 'E. Exportar e me mandar (até ~19h10)', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': '1080×1920, nome nora73-montado (acima de 30 MB, link do Drive). Se for mais rápido, me mande só o take novo, que eu emendo aqui (ele fica sem música embaixo, ~8 s). Eu devolvo o nora73-final (Insta, 19h30) e o nora73-final-FACE (Face, 0h00).'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': [
            {'nome': 'd1711-PRE-carro-IMG-C', 'tipo': 'imagem', 'status': 'reutilizar', 'onde': 'A mesma do nora72. Anexe ela no Muse.', 'descricao': 'A mesma do nora72.'},
            {'nome': 'hook da canela no carro', 'tipo': 'hook', 'status': 'reutilizar', 'onde': 'Já está comigo.', 'descricao': 'Eu emendo antes do take novo.'},
            {'nome': NOME73, 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{FALA73}”'},
            {'nome': 'NORA72.mp4 (o montado do nora72)', 'tipo': 'corpo', 'status': 'reutilizar', 'onde': 'No seu Drive.', 'descricao': 'Os 6 takes do nora72, como estão.'},
        ],
        'decisao': [
            '1 take no Muse: a frase das letras do nome na frente do nora72 inteiro. Só a abertura muda.',
            'Postado às 18h15 de 20/11, no Insta e no Face (decisão do aluno).',
            'Hipótese: a abertura pelas iniciais (o único post que levou gente ao perfil foi o curto das iniciais: 21 visitas) leva gente ao perfil também no falado.',
            'O story vence às ~18h15: reposte antes, no Insta e no Face.',
        ],
    }
    P['ordem'] = ['pecas', 'agente', 'cenas', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    return P


# ------------------------------------------------------------------ nora74: o campeão de volta (o nora48 a nora50), feito do zero no Muse
# O campeão (06 a 10/11: 1.638 a 2.043 views, 10 a 19 follows) = o tsunami + um Take 1 de signos + o corpo A limpo (os 7 takes do nora40 sem os vermelhos).
# O aluno não tem mais os takes (20/11): os 8 takes são gerados de novo no Muse, com o texto do corpo A limpo como era. O tsunami é o hook do nora68
# (d1611-PRE-onda-HOOK.mp4, que está aqui) e a fala vai na mesma praia, na d1611-PRE-onda-IMG-C (sem imagem nova). Só no Insta (os selos e o
# "Comment 222" na fala são isca de engajamento no Face). É o teste "copy ou conta": se o campeão fizer ~150 views, a trava é a conta.
# 20/11 ~17h45: o aluno mandou o hook ORIGINAL do campeão (nora47-PRE-tsunami-inteiro-AB.mp4, 7,85 s: a praia, ela corre para o bunker, a porta
# treme e a água espirra lá dentro) e os 2 clipes do nora68. O nora74 usa o original; a fala continua DENTRO do bunker (R46), e a imagem das falas é o
# último quadro do hook (d2011-bunker-IMG.jpg, 1080×1920; a Nora com a lua e as 3 estrelinhas, a trança com anéis, o blazer de linho creme).
ONDA = dict(
    nn='nora74', d='d2011', tag='bunker', img='d2011-bunker-IMG', nome='dentro do bunker, de frente para a porta de aço, calma',
    roupa_cont='her cream-white linen blazer over a plain white V-neck blouse',
    quando='right after the wave has passed', onde='a small concrete bunker by the beach', luz='lit by the warm light of a caged wall lamp on the left',
    fundo='the riveted dark-gray steel door behind her, the bare concrete walls and ceiling, and the glowing caged wall lamp on the left',
    visual='warm light from a caged wall lamp inside a concrete bunker', som='quiet room tone inside a concrete bunker with the faint muffled sound of the ocean outside',
    segura=('both of her hands stay down, relaxed by her sides at the bottom edge of the frame the whole time and never move; no water, spray or drip appears '
            'during the takes'),
    livre_obj='the riveted steel door, the concrete walls and the glowing caged wall lamp',
)
FALA74 = [
    "Taurus, Virgo or Capricorn: if you've been carrying everything on your own, listen to this before the year ends.",
    "Don't tell anyone what's about to happen. I don't know your name or what you did, but the universe saw your faith.",
    "A major turnaround is coming your way over the next few days. I see something very unusual happening in your life.",
    "There's money, prosperity and someone incredibly wonderful about to show up in your life unexpectedly. The universe chose you for this.",
    "Archangel Michael has sent a warning. A phase of victory and prosperity is approaching your life. The worst is finally over.",
    "I can already see the chains keeping you trapped in scarcity being broken. Closed financial doors are starting to open.",
    "Now save this video, that will be your first seal. Tap the follow button down below, that will be your second seal.",
    "Comment 222 to claim this energy, then tap my profile picture. The second part of this sign is waiting in my stories.",
]
SUF74 = ['signos-terra', 'segredo-fe', 'virada', 'prosperidade', 'sao-miguel', 'correntes', 'selos', 'cta-222-story']
EXP74 = [
    'she holds a serious, knowing look and gives one slow nod in the closing half',
    'she leans in slightly toward the lens with a confidential, knowing look, then gives one small nod',
    'her eyebrows lift a little with a hopeful, intrigued look, then she gives one small nod',
    'a warm, bright smile grows on her face and she gives one small nod',
    'she holds a calm, serious look in the first half and in the closing half a relieved smile appears',
    'she holds a calm, confident look and gives one small slow nod in the closing half',
    'she holds a warm, encouraging look and gives two small nods',
    'she holds a warm, encouraging smile and glances down toward the lower left corner of the frame, then back at the lens',
]
N74 = len(FALA74)
assert len(SUF74) == len(EXP74) == N74


def nome74(i):
    return f'd2011-onda-T{i + 1:02d}-{SUF74[i]}'


def mov74(i):
    return (f'Throughout the whole 10 seconds the camera stays static at chest height in front of her with an unchanged framing; {ONDA["segura"]}; her eyes stay on '
            f'the lens; {EXP74[i]}; only her face moves, never her hands; from the end of the final sentence of the take until the clip ends she keeps her lips closed and '
            'silent; no zoom and no cuts, the braid stays in place, everything else stays still and each hand has exactly five fingers.')


for i in range(N74):
    assert len(FALA74[i].split()) <= 22, (i + 1, len(FALA74[i].split()))
    fw = re.findall(r"[a-z']+", FALA74[i].lower()); mw = re.findall(r"[a-z']+", mov74(i).lower())
    assert not ((set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - B.COMUNS - {('the', 'take'), ('a', 'small'), ('the', 'sea')}), (i + 1,)
    if i + 1 < N74:
        prox = re.split(r'(?<=[.!?])\s+', FALA74[i + 1])[0]
        assert len(FALA74[i].split()) + len(prox.split()) >= 25, (i + 1, 'cabe no take anterior')


def livre74():
    c = ONDA
    return (f'Casual real video {c["quando"]} inside {c["onde"]}, filmed from a static camera at her chest height about one meter in front of her, looking exactly like a '
            f'real phone video, {c["luz"]}. CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, {B.JOIAS}, {c["roupa_cont"]}, and '
            f'{c["livre_obj"]} stay exactly as in the reference image; the framing is exactly the one of the reference image, from the chest up, her face in the upper '
            f'middle of the frame; {c["segura"]}; {c["fundo"]} stay exactly where they are; natural skin texture with visible pores, slight phone grain, everything in '
            'focus, no bokeh, no filter, no glow and no sparkles; the camera is static, no zoom, no cuts and no reframing; no phone, phone stand, tripod, object, person, '
            f'animal or text appears or disappears; each hand always has exactly five fingers; no on-screen text, no captions; {c["som"]} only, no music. SPEECH RULE '
            "for every take: she says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added "
            'sentence before, between or after; the number 222 is spoken as "two two two"; she speaks in a calm, confident, confidential tone, like someone sharing an '
            'important message with one person; when she finishes the last word she closes her lips, stays silent and keeps a calm still expression until the clip ends.')


def config74():
    cf = copy.deepcopy(B.BASE['central']['config'])
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = 'colar o texto abaixo (a imagem é a d2011-bunker-IMG, o último quadro do hook do tsunami)'
                campo['copiar'] = livre74()
            elif campo['campo'] == 'COLE SUA COPY AQUI':
                campo['valor'] = 'colar a fala inteira (seção “A fala e a movimentação”): é 1 colagem só, com os 8 takes'
            elif campo['campo'] == 'Movimento de câmera':
                campo['valor'] = 'Estático / câmera parada, sem zoom (se essa opção não existir: Handheld sutil, sem zoom; o LIVRE já diz câmera parada)'
            elif campo['campo'] == 'Atmosfera / mood':
                campo['valor'] = 'Íntimo e confidencial'
            elif campo['campo'] == 'Movimentação':
                campo['valor'] = 'colar as 8 linhas, uma por take (seção “A fala e a movimentação”)'
            elif campo['campo'] == 'Conferir':
                campo['valor'] = '8 takes (8 ou 10 s cada, como na lista da seção “A fala e a movimentação”)'
    B.VC.adicionar(cf)
    return cf


def nora74():
    P = copy.deepcopy(B.pacote('PAINEL-NORA72.html'))
    P['figurino'] = ONDA['roupa_cont']
    P['imagens_titulo'] = 'Imagem das falas (a d2011-bunker-IMG, o último quadro do hook)'
    P['refs'] = ['d2011-bunker-IMG em todos os takes']
    P['imagens'] = [{'rotulo': 'IMAGEM 1 · d2011-bunker-IMG', 'cena': 'já existe (o último quadro do hook do tsunami; eu mandei no chat)', 'anexar': 'a d2011-bunker-IMG'}]
    P['roteiro'].update({
        'id': 'nora74-CAMPEAO-ONDA-2011',
        'titulo': 'nora74 · Insta às 19h30 de 23/11 (segunda) · o campeão de volta: o tsunami original + Touro, Virgem e Capricórnio + o corpo A limpo',
        'duracao_total': 70,
        'descricao_instagram': ("Taurus, Virgo, Capricorn: if you've been carrying everything on your own, listen before the year ends. 🔮\n"
                                'The worst is finally over. Your private reading is waiting in my story.\n'
                                'Comment 222 to claim this energy 👇\n'
                                '#manifestation #taurus #virgo #capricorn #2027'),
        'descricao_face': 'Não vai ao Face: os selos e o pedido de comentário na fala são isca de engajamento lá.',
    })
    P['videos'] = [{'rotulo': f'T{i + 1:02d}', 'cena': SUF74[i], 'duracao': 10, 'primeiro_quadro': 'IMAGEM 1 (d2011-bunker-IMG)', 'acao': '', 'b_roll': '',
                    'fala': FALA74[i], 'movimentacao': mov74(i), 'arquivo': nome74(i)} for i in range(N74)]
    P['texto_tela'] = {'hook': 'Taurus, Virgo or Capricorn:\n[listen to this]', 'hook_comeca': 'o 1º quadro do hook', 'hook_termina': 'o fim da 1ª frase (o T01)',
                       'hook_alt': '', 'extras': []}
    P['comentario_fixado'] = {'insta': 'The worst is finally over 🙏 tap my profile picture above, the second part is waiting in my story', 'face': '(não vai ao Face)'}
    P['story'] = {'ja_postado': True, 'nota': 'Antes de postar, confira se o story repostado hoje (o adesivo “TAP TO CONTINUE 🎁”, com o link STORYIG) está no ar no Insta.'}
    lista = ' · '.join(f'{i + 1} = {nome74(i)}' for i in range(N74))
    ct = P['central']
    ct['config'] = config74()
    ct['colagens'] = [{'titulo': 'nora74: a colagem única (T01 a T08)', 'fala': ' '.join(FALA74), 'movimentacao': [mov74(i) for i in range(N74)],
                     'takes': list(range(N74))}]
    ct['conferir'] = ('Conferir em cada take: é a Nora do último quadro do hook (rosto, lua com as 3 estrelinhas, trança com anéis, brincos, colar de Vênus, o blazer de '
                      'linho creme); dentro do bunker, a porta de aço atrás e a luminária acesa; as mãos paradas embaixo; sem água; ela fala uma vez só e diz “two two two”. Renomeie com o nome da lista.')
    ag = copy.deepcopy(ct['agente'])
    ag['imagem'] = 'd2011-bunker-IMG'
    ag['intro'] = ('No Muse, na conversa da Nora: anexe a d2011-bunker-IMG, cole o aviso do Muse e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central '
                   '(1 colagem: 1 mensagem).')
    ag['passos'] = [
        'Na Central: preencha como na seção da Central (o LIVRE e a movimentação são os do nora74) e cole a fala inteira. Confira: 8 takes.',
        'No Muse, na conversa da Nora: 1 MENSAGEM só, com a d2011-bunker-IMG + o aviso do Muse + o “COPIAR TUDO JUNTO” da Central (os 8 takes).',
        f'Renomeie cada take com o nome da lista (o número é a ordem na mensagem): {lista}.',
        'Confira cada take: dentro do bunker, a porta de aço atrás, as mãos paradas embaixo, sem água, a lua com as 3 estrelinhas; ela fala uma vez só, sem repetir palavra, e diz '
        '“two two two” no T08. Se o Muse recusar um prompt: NÃO deixe ele reescrever; mande na mesma conversa “Generate prompt X again, exactly as written.”',
        'Limite do Muse: ~15 vídeos por dia (livre hoje). Se aparecer o “video_daily_budget_exhausted”, me avise com quantos takes saíram.',
        'Se o Muse parar no meio: responda na MESMA conversa, sem anexar nada: “Please continue and generate prompts X to Y from my previous message, in the same order.”',
    ]
    ct['agente'] = ag
    P['silencio']['intro'] = ('Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” só os 8 takes do Muse (T01 a T08), de uma vez. O hook não entra: ele está '
                              'comigo. “Zoom nos cortes” = DESLIGADO; o resto como abaixo.')
    P['silencio']['nome'] = 'nora74-cortado'
    P['silencio']['ordem'] = 'pela ordem do nome (T01 a T08)'
    P['silencio']['depois'] = ['Suba os 8 takes e espere a Prévia.',
                               'Aperte play com Resultado marcado: confira a primeira palavra do T01 e a última do T08.',
                               'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.',
                               'Clique em Cortar e baixar e salve como nora74-cortado.']
    P['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': 'Projeto novo no CapCut com o nora74-cortado', 'como': 'É o vídeo que saiu da FusionZ. Começa direto no T01.'},
        {'quando': 'B. O hook: NÃO põe no CapCut', 'texto': 'O tsunami original (o nora47-PRE-tsunami-inteiro-AB que você mandou) já está comigo', 'como': 'Eu emendo o hook antes do T01, em corte seco.'},
        {'quando': '1. Do T01 ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Começa no 1º quadro do montado.'},
        {'quando': '2. Exportar e me mandar (até ~19h00 de 23/11)', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': '1080×1920, nome nora74-montado (acima de 30 MB, link do Drive). Eu devolvo o nora74-final (Insta, 19h30 de 23/11). Não vai ao Face.'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': ([{'nome': 'd2011-bunker-IMG', 'tipo': 'imagem das falas', 'status': 'reutilizar', 'onde': 'O último quadro do hook do tsunami (eu mandei no chat). Anexe ela no Muse.', 'descricao': 'O último quadro do hook.'},
                   {'nome': 'hook do tsunami original (nora47-PRE-tsunami-inteiro-AB, 7,85 s)', 'tipo': 'hook', 'status': 'reutilizar', 'onde': 'Já está comigo.', 'descricao': 'Eu emendo antes do T01, em corte seco.'}]
                  + [{'nome': nome74(i), 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{FALA74[i]}”'} for i in range(N74)]),
        'decisao': [
            '8 takes no Muse: o campeão de 06 a 10/11 (o nora48 a nora50: 1,6 mil a 2 mil views, 10 a 19 follows) feito de novo: o tsunami original + Touro, Virgem e '
            'Capricórnio + o corpo A limpo, com o texto como era (o segredo, o Arcanjo, os selos, o 222). A fala continua dentro do bunker, no último quadro do hook.',
            'Insta às 19h30 de 23/11, segunda (o montado até ~19h00; gerar os 8 takes no Muse cedo); não foi gerado em 20 nem em 21/11, e a 0h00 de 23/11 passou. Não vai ao Face. O limite do Muse (~15 por dia) está livre.',
            'Hipótese: se o campeão também fizer ~150 views, a trava é a conta (e vem a Nora sem a pintura, depois dos 40 vídeos que o nora74 fecha); se passar de 500, é a copy.',
        ],
    }
    P['ordem'] = ['pecas', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario']
    return P


def salvar(P, nn, rotulo):
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>' + rotulo + '</title>', html, count=1)
    (R / f'PAINEL-{nn.upper()}.html').write_text(html, encoding='utf-8')
    print('ok', nn, len(html), 'bytes')


if __name__ == '__main__':
    salvar(nora73(), 'nora73', 'Painel nora73 · letras do nome · 20/11')
    salvar(nora74(), 'nora74', 'Painel nora74 · o campeão de volta · 20/11')
