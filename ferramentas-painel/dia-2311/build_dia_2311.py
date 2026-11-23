# Painéis do dia 23/11/2026 ("pode montar o Nora 75 e o Nora 76", ~15h40): a Nora igual à maioria (RECEITA-DA-MAIORIA.md).
# nora75 (Insta e Face ~19h30): a Nora SEM a pintura (teste do aluno), blusa preta lisa, cabelo solto, no carro parado, com um pau de canela na mão;
#   o ritual dito no T01 + a janela de 3 datas + o corpo A "Archangel Michael has sent a warning" + os selos + "Comment amen" + o CTA "quick reading".
#   13 takes no Muse (~1:40). Texto do topo em branco solto, sem caixa (teste do aluno): "It works so fast, it's almost scary...".
# nora76 (Insta e Face ~0h00): o MESMO corpo (T02 a T13 do nora75) com um T01 novo, "There is a woman lying down…" (a 2ª abertura mais repetida):
#   1 clipe só no Muse. Texto do topo: "Turnaround is coming your way...".
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2311/build_dia_2311.py
import sys, json, copy, re, pathlib, importlib.util

R = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('b1911', R / 'ferramentas-painel' / 'dia-1911' / 'build_dia_1911.py')
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
MODELO, FB, VOZ, VC, COMUNS = B.MODELO, B.FB, B.VOZ, B.VC, B.COMUNS
assert FB.endswith('&aff=dl7zx6ks')

IMG = 'd2311-carro-IMG'
ROSTO = ('her face with clean natural skin and no marks, no paint, no moon and no stars anywhere on her face, her long black wavy hair worn loose with no braid '
         'and no rings in it, small plain gold stud earrings and a thin gold chain necklace')
ROUPA = 'her plain black fitted long-sleeve crew-neck top'
SEGURA = ('one hand rests on the steering wheel the whole time; her other hand holds a single cinnamon stick upright in front of her chest the whole time; '
          'the seatbelt stays across her chest')
CAM = 'the phone stays mounted on the dashboard in front of her with an unchanged framing; the car is parked and does not move'
SOM = 'quiet parked-car interior sound with faint birds and a distant passing car outside'

FALA = [
    "Drop a cinnamon stick on the floor of your car tonight. I know it sounds ridiculous, but you'll thank me forever.",
    "If this video found you on November twenty-third, twenty-fourth or twenty-fifth, keep what you're about to hear to yourself.",
    "I don't know your name or what you've been through, but the universe has seen your faith.",
    "Over the next few days, money, prosperity and someone very special will walk into your life unexpectedly.",
    "If you turn your back on this message, the blessing turns its back on you too. Take this seriously.",
    "Archangel Michael has sent a warning: a season of victory is beginning in your life. The worst is finally behind you.",
    "I can see the chains of scarcity breaking right now. Doors that stayed closed for years are about to open.",
    "In seven minutes, this energy settles around you, so send this video to yourself right now and come back to feel it.",
    "Save this video. That's your first seal. Double tap the screen. That's your second seal.",
    "Comment amen so I know you completed every step. Tomorrow at eleven, watch for good news.",
    "But I'm receiving a warning: this change only happens for women whose energy is aligned with abundance.",
    "That's why I left a quick reading in my story that shows if you're one of them.",
    "Tap my profile picture and watch it right now. You could be one step away from everything you've dreamed of.",
]
SUF = ['canela-ritual', 'datas', 'fe', 'virada', 'aviso', 'arcanjo', 'correntes', 'sete-minutos', 'selos', 'amen', 'alinhada', 'leitura', 'cta-story']
FALA76 = "There is a woman lying down with her phone in her hand right now, and this message is for her."
GESTO = [
    'she raises the cinnamon stick close to the lens for a moment, then lowers it toward the floor of the car, and gives a small knowing smile',
    'she leans in slightly toward the lens with a confidential, knowing look',
    'she gives one slow nod with a calm, warm look',
    'her eyebrows lift with a hopeful, bright look and a small smile grows',
    'she holds a calm, serious look and gives one slow nod',
    'she holds a serious look in the first half and in the closing half a relieved smile appears',
    'she holds a calm, confident look and nods slowly',
    'she leans in slightly with an encouraging look',
    'she gives two small nods with a warm, encouraging look',
    'she holds a warm smile and gives one small nod',
    'she holds a calm, serious, caring look',
    'she holds a warm, knowing look and gives one small nod',
    'she glances down toward the lower left corner of the frame with a warm, encouraging smile, then back at the lens',
]
GESTO76 = 'she holds a calm, knowing look, as if she can see the woman she is talking about, and gives one slow nod'
N = len(FALA)
assert len(SUF) == len(GESTO) == N


def nome(i):
    return f'd2311-carro-T{i + 1:02d}-{SUF[i]}'


NOME76 = 'd2311-carro-T01B-mulher-deitada'


def mov(g):
    return (f'Throughout the whole 10 seconds {CAM}; {SEGURA}; {g}; her eyes stay on the lens; only her face and the hand with the cinnamon stick move; '
            'from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; no zoom and no cuts, each hand has exactly five fingers.')


EXTRA = {('the', 'lens'), ('a', 'small'), ('the', 'floor'), ('floor', 'of'), ('of', 'the'), ('the', 'car'), ('a', 'cinnamon'), ('cinnamon', 'stick')}
for i, f in list(enumerate(FALA)) + [(-1, FALA76)]:
    assert len(f.split()) <= 22, (i + 1, len(f.split()), f)
    g = GESTO[i] if i >= 0 else GESTO76
    fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(g).lower())
    sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS - EXTRA
    assert not sobra, (i + 1, sobra)
    for w in ('link', 'free', 'card', 'tarot', 'private'):
        assert w not in f.lower().split(), (i + 1, w)
    if 0 <= i < N - 1:
        prox = re.split(r'(?<=[.!?])\s+', FALA[i + 1])[0]
        assert len(f.split()) + len(prox.split()) > 22, (i + 1, 'a 1ª frase do take seguinte cabe neste')
PALAVRAS = sum(len(f.split()) for f in FALA)


def livre():
    return ("Casual real video in the afternoon inside a parked dark gray car on a quiet American suburban street, filmed by a phone mounted on the dashboard about "
            "60 centimeters in front of her at face height, looking exactly like a real phone video, lit by soft natural daylight through the windows. She sits in the "
            "driver's seat; the car does not move; through the side and rear windows, houses, lawns and trees stay still. CONTINUITY LOCKS for every take: the woman, "
            f"{ROSTO}, {ROUPA}, the cinnamon stick in her hand, the steering wheel, the seatbelt across her chest and the car's interior stay exactly as in the reference "
            f"image; the framing is exactly the one of the reference image, her face in the upper middle of the frame; {SEGURA}; natural skin texture with visible pores, "
            'slight phone grain, everything in focus, no bokeh, no filter, no glow and no sparkles; no zoom, no cuts and no reframing; no phone, phone stand, tripod, object, '
            'person, animal or text appears or disappears; no paint, moon, stars or marks ever appear on her face; each hand always has exactly five fingers; no on-screen '
            f"text, no captions; {SOM} only, no music. SPEECH RULE for every take: she says only the exact words of that take's script, each word exactly once and in order, "
            'with no repeated word, no extra word and no added sentence before, between or after; numbers and dates are spoken as words exactly as written; she speaks in a '
            'direct, serious, intimate tone, like telling a secret to one person; when she finishes the last word she closes her lips, stays silent and keeps a calm still '
            'expression until the clip ends.')


def prompt_manual(txt, movimento):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image sits in the '
            "driver's seat of a parked car and speaks directly to the camera.\n\n"
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + txt + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            'VOICE PACING: medium pace (155 to 180 words per minute), about 8 seconds of speech; when she finishes the last word she closes her lips and stays silent '
            'with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + movimento + '\n\n'
            'VISUAL: realistic casual phone video, soft natural afternoon daylight inside a parked car, natural skin texture with visible pores, slight phone grain, '
            'everything in focus, no bokeh, no filter.\n\nCAMERA: mounted on the dashboard, no zoom, no cuts, no reframing.\n\n'
            f'AUDIO: only her voice and {SOM}; no music, no other voices, no sound effects.\n\n'
            f'CONTINUITY: {ROSTO}, {ROUPA}, the cinnamon stick in her hand and everything behind her stay exactly as in the reference image; no paint, moon, stars or '
            'marks appear on her face; no phone, object, person or text appears; each hand has exactly five fingers; no on-screen text or captions.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.')


PROMPT_IMG = ('The first image is an approved photo of the woman sitting in a car; the second image is her character sheet (same woman, same face). Keep exactly her '
              'face, her eyes, her skin tone and her long black wavy hair. Change: her cheek is now clean natural skin, with no crescent moon, no stars, no paint and no '
              'marks anywhere on her face; her hair is worn loose, with no braid and no gold rings in it; she wears a plain black fitted long-sleeve crew-neck top, small '
              'plain gold stud earrings and a thin gold chain necklace, and nothing else on her neck or ears. Place and light: she sits in the driver\'s seat of a parked '
              'dark gray car on a quiet American suburban street on a sunny afternoon, soft natural daylight through the windows; through the side and rear windows, '
              'houses, lawns and trees. RAW photo taken by a phone mounted on the dashboard about 60 centimeters in front of her, at face height, like a real car selfie: '
              'framed from the chest up, her face in the upper middle of the image, looking straight into the camera with a calm, knowing look and her lips closed; the '
              'seatbelt across her chest; one hand rests on the steering wheel, partly visible at the bottom of the image; her other hand holds a single cinnamon stick '
              'upright in front of her chest; the upper 15 percent of the image is the plain light-gray car ceiling with nothing in it; ' + B.__dict__.get('_FIM', '') +
              'looks exactly like a real casual iPhone photo, slight phone grain, natural colors, everything in focus, no bokeh; no glow, no sparkle, no light effect; no '
              'phone, phone stand or tripod anywhere in the image; no text and no logo anywhere; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16')


def config():
    cf = copy.deepcopy(B.BASE['central']['config'])
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = f'colar o texto abaixo (a imagem é a {IMG}, a Nora sem a pintura no carro)'
                campo['copiar'] = livre()
            elif campo['campo'] == 'COLE SUA COPY AQUI':
                campo['valor'] = f'colar a fala inteira (seção “A fala e a movimentação”): é 1 colagem só, com os {N} takes'
            elif campo['campo'] == 'Movimento de câmera':
                campo['valor'] = 'Estático / câmera parada, sem zoom (o LIVRE já diz que a câmera está presa no painel e que o carro está parado)'
            elif campo['campo'] == 'Atmosfera / mood':
                campo['valor'] = 'Íntimo e confidencial'
            elif campo['campo'] == 'Movimentação':
                campo['valor'] = f'colar as {N} linhas, uma por take (seção “A fala e a movimentação”)'
            elif campo['campo'] == 'Conferir':
                campo['valor'] = f'{N} takes (8 ou 10 s cada, como na lista da seção “A fala e a movimentação”)'
    VC.adicionar(cf)
    return cf


def mapa(P, caixa):
    m = P['mapa_tela']
    m['estilos'] = [
        {'nome': 'Texto do topo (eu ponho)', 'fonte': 'negrito', 'cor': 'branco solto, SEM caixa, com sombra suave (como a maioria)', 'tamanho': '2 linhas',
         'contorno': '—', 'obs': f'“{caixa}” só nos 3 primeiros segundos. Teste do aluno (23/11): no lugar da caixa branca com vermelho.'},
        {'nome': 'Legenda (eu ponho)', 'fonte': 'Inter, peso normal', 'cor': 'branca, sem destaque', 'tamanho': 'até ~6 palavras, 2 linhas', 'contorno': 'fino escuro + sombra suave',
         'obs': 'Entra na 1ª palavra.'},
        {'nome': 'Seta (eu ponho)', 'fonte': '—', 'cor': 'vermelha', 'tamanho': 'pequena', 'contorno': '—',
         'obs': 'Embaixo à esquerda, logo acima da foto do perfil, do “Tap my profile picture” até o fim. Sem a faixa do CTA (a maioria usa só a seta).'},
    ]
    m['regras'] = ['A receita da maioria (23/11): o texto do topo em branco solto só no gancho, a legenda simples, o 222 e o 11:11 pequenos nos cantos, a seta no CTA.',
                   'Eu ponho tudo (P45); você monta só o vídeo e a música.']
    m['numeros'] = [{'t': '222', 'x': 18, 'y': 16, 'onde': 'alto à esquerda, o vídeo todo', 'cor_nome': 'branco', 'cor': '#FFFFFF', 'tamanho': 11},
                    {'t': '11:11', 'x': 82, 'y': 16, 'onde': 'alto à direita, o vídeo todo', 'cor_nome': 'branco', 'cor': '#FFFFFF', 'tamanho': 11}]


RESP_INSTA = ['Amen 🙏 your reading is waiting in my story', "That's not a coincidence ✨ tap my photo, your next step is in my story",
              'So glad this found you today 💛 check my story', 'Received ✨ your reading is in my story 🔮', 'I see you 🙏 tap my profile picture']


def base(nn):
    P = copy.deepcopy(B.BASE)
    P['ocultar_bloco_agente_imagem'] = True
    P['figurino'] = ROUPA
    rf = P['respostas_face']; rf['link'] = FB; rf['insta'] = RESP_INSTA
    P['story'] = {'ja_postado': True, 'nota': ('O story repostado em 22/11 às 22h30 vence às ~22h30 de hoje: reposte antes, ao vivo, no Insta e no Face (o mesmo arquivo, '
                                              'com o adesivo do link). Sem story no ar, o vídeo não leva a lugar nenhum.' if nn == 'nora75' else
                                              'Antes de postar, confira se o story repostado hoje está no ar no Insta e no Face.')}
    return P


def nora75():
    P = base('nora75')
    P['pre_gancho'] = {
        'titulo_secao': 'A imagem das falas (Flow, antes dos takes)',
        'conceito': ('A Nora igual à maioria (RECEITA-DA-MAIORIA.md): SEM a lua e as estrelinhas (teste do aluno), cabelo solto sem a trança, blusa preta lisa, no banco do '
                     'motorista do carro parado, de dia, com um pau de canela na mão o vídeo todo. Não tem hook mudo: ela fala desde o 1º quadro, mostrando a canela.'),
        'modo': 'Flow → Imagem · 9:16 · Nano Banana Pro · x4, anexando as referências na ordem (0 crédito).',
        'etapas': [{'titulo': 'Imagem: a Nora sem a pintura, no carro, com o pau de canela', 'nome': IMG, 'tipo': 'img',
                    'anexar': '1º a d1711-PRE-carro-IMG-C (a Nora no carro, já aprovada); 2º a folha da Nora (1K)',
                    'quadros': (f'x4, 0 crédito. Serve para TODOS os takes do nora75 e do nora76. Escolha a que tiver: o mesmo rosto da Nora, SEM a lua e SEM as '
                                'estrelinhas, sem trança; a blusa preta lisa; o cinto; uma mão no volante e a outra segurando 1 pau de canela em pé na frente do peito; '
                                f'5 dedos em cada mão; nenhum celular, tripé ou texto. Renomeie para {IMG}. Se ficar em dúvida entre 2, me mande as 4.'),
                    'prompt': PROMPT_IMG}],
    }
    P['imagens_titulo'] = f'Imagem das falas (a {IMG}, que você gera no Flow)'
    P['refs'] = [f'{IMG} em todos os takes']
    P['imagens'] = [{'rotulo': f'IMAGEM 1 · {IMG}', 'cena': 'gerada no Flow (seção da imagem)', 'anexar': f'a {IMG}'}]
    P['roteiro'] = {
        'id': 'nora75-MAIORIA-CANELA-2311',
        'titulo': 'nora75 · Insta e Face ~19h30 de 23/11 · a Nora igual à maioria: sem a pintura, no carro, a canela dita + o corpo A',
        'duracao_total': 100,
        'descricao_instagram': ("It works so fast, it's almost scary... 🌿 Your private reading is waiting in my story 🔮\n"
                                'Comment amen when you’re done 🙏\n'
                                '#manifestation #cinnamon #abundance #2027 #lawofattraction'),
        'descricao_face': ("It works so fast, it's almost scary ✨ Your reading is waiting in my story and in the comments 🔮\n"
                           '#manifestation #abundance #2027'),
    }
    P['videos'] = [{'rotulo': f'T{i + 1:02d}', 'cena': SUF[i], 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({IMG})', 'acao': '', 'b_roll': '',
                    'fala': FALA[i], 'movimentacao': mov(GESTO[i]), 'arquivo': nome(i)} for i in range(N)]
    P['texto_tela'] = {'hook': "It works so fast,\nit's almost scary...", 'hook_comeca': 'o 1º quadro', 'hook_termina': '~3 s', 'hook_alt': '', 'extras': []}
    mapa(P, "It works so fast, it's almost scary...")
    P['comentario_fixado'] = {'insta': 'It works so fast 🌿 tap my profile picture above, your reading is waiting in my story',
                              'face': 'Your 2027 reading is waiting for you here ✨ 👉 ' + FB}
    lista = ' · '.join(f'{i + 1} = {nome(i)}' for i in range(N))
    ct = P['central']
    ct['config'] = config()
    ct['colagens'] = [{'titulo': f'nora75: a colagem única (T01 a T{N:02d})', 'fala': ' '.join(FALA), 'movimentacao': [mov(GESTO[i]) for i in range(N)],
                       'takes': list(range(N))}]
    ct['conferir'] = ('Conferir em cada take: é a Nora da imagem nova, SEM a lua e SEM as estrelinhas, sem trança, de blusa preta; no carro parado, o cinto, uma mão no '
                      'volante e a outra com o pau de canela; ela fala uma vez só, em inglês, e diz as datas por extenso. Renomeie com o nome da lista.')
    ag = copy.deepcopy(ct['agente'])
    ag['imagem'] = IMG
    ag['intro'] = f'No Muse, na conversa da Nora: anexe a {IMG}, cole o aviso do Muse e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central (1 colagem: 1 mensagem).'
    ag['passos'] = [
        f'Na Central: preencha como na seção da Central (o LIVRE e a movimentação são os do nora75) e cole a fala inteira. Confira: {N} takes.',
        f'No Muse: 1 MENSAGEM com a {IMG} + o aviso do Muse + o “COPIAR TUDO JUNTO” da Central. O Muse gera 6 por vez: depois do 01 ao 06, mande na mesma conversa, '
        'com a mesma imagem anexada: “Now generate Prompts 07 to 12 from my previous message, exactly as written, in the same order, using the attached image as the '
        'first frame of every clip.” E depois o 13 do mesmo jeito.',
        f'Renomeie cada take com o nome da lista (o número é a ordem na mensagem): {lista}.',
        'Confira cada take: sem a lua e sem as estrelinhas no rosto (se voltarem, gere de novo aquele take); a canela na mão; ela fala uma vez só, sem repetir palavra. '
        'Se o Muse recusar um prompt: NÃO deixe ele reescrever; mande na mesma conversa “Generate prompt X again, exactly as written.”',
        'Hoje são 14 clipes (os 13 do nora75 e 1 do nora76): o limite do Muse é de ~15 por dia. Gere já. Se aparecer o “video_daily_budget_exhausted”, me avise com quantos saíram.',
        'Se o Muse parar no meio: responda na MESMA conversa, sem anexar nada: “Please continue and generate prompts X to Y from my previous message, in the same order.”',
    ]
    ct['agente'] = ag
    P['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” os {N} takes do Muse (T01 a T{N:02d}), de uma vez. “Zoom nos cortes” = DESLIGADO; o resto como abaixo.',
        'nome': 'nora75-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': f'pela ordem do nome (T01 a T{N:02d})',
        'depois': ['Suba os takes e espere a Prévia.', f'Aperte play com Resultado marcado: confira a primeira palavra do T01 e a última do T{N:02d}.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', 'Clique em Cortar e baixar e salve como nora75-cortado.'],
    }
    P['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': 'Projeto novo no CapCut com o nora75-cortado', 'como': 'É o vídeo que saiu da FusionZ. Começa direto no T01, sem hook.'},
        {'quando': '1. Do T01 ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Começa no 1º quadro.'},
        {'quando': '2. Exportar e me mandar (até ~19h00)', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': ('1080×1920, nome nora75-montado (acima de 30 MB, link do Drive). Eu devolvo o nora75-final (Insta, completo) e o nora75-final-FACE (sem o T08, o T09 e o '
                  'T10, que pedem para mandar para si, os selos e o comentário, e sem o “money” do T04). O nora76 eu monto aqui com esse mesmo montado.')},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': ([{'nome': IMG, 'tipo': 'imagem das falas', 'status': 'gerar', 'onde': 'No Flow (x4, 0 crédito), na seção da imagem.', 'descricao': 'A Nora sem a pintura, no carro, com a canela.'}]
                  + [{'nome': nome(i), 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{FALA[i]}”'} for i in range(N)]),
        'decisao': [
            f'{N} takes no Muse, {PALAVRAS} palavras (~1:40): a receita da maioria (40 vídeos de 18 contas da Auraly, 23/11). Ela fala desde o 1º quadro mostrando a '
            'canela (o objeto nº 1); a janela de 3 datas; o corpo A "Archangel Michael has sent a warning" com os selos e o "Comment amen"; o CTA "quick reading".',
            'Testes do aluno: a Nora SEM a lua e as estrelinhas, e o texto do topo em branco solto, sem caixa.',
            'Insta e Face ~19h30 de hoje. O montado até ~19h00. O Face vai sem o T08, o T09 e o T10 e sem o “money” (segurança da Página).',
            'O story vence às ~22h30 de hoje: reposte antes, no Insta e no Face. Antes de abrir o Insta, conferir o IP e os EUA no mylocation.org.',
        ],
    }
    P['ordem'] = ['pecas', 'prehook', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    return P


def nora76():
    P = base('nora76')
    P['imagens_titulo'] = f'Imagem das falas (a {IMG}, a mesma do nora75)'
    P['refs'] = [f'{IMG} no take novo']
    P['imagens'] = [{'rotulo': f'IMAGEM 1 · {IMG}', 'cena': 'a mesma do nora75', 'anexar': f'a {IMG}'}]
    P['roteiro'] = {
        'id': 'nora76-MAIORIA-DEITADA-2311',
        'titulo': 'nora76 · Insta e Face ~0h00 de 24/11 · o corpo do nora75 com outro Take 1: “There is a woman lying down…”',
        'duracao_total': 98,
        'descricao_instagram': ('She was meant to see this today 🙏 Your private reading is waiting in my story 🔮\n'
                                'Comment amen and the time you’re watching this 👇\n'
                                '#manifestation #archangelmichael #abundance #2027 #lawofattraction'),
        'descricao_face': ('She was meant to see this today ✨ Your reading is waiting in my story and in the comments 🔮\n'
                           '#manifestation #abundance #2027'),
    }
    P['videos'] = [{'rotulo': 'T01B', 'cena': 'a mulher deitada (entra no lugar do T01 do nora75)', 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({IMG})',
                    'acao': '', 'b_roll': '', 'fala': FALA76, 'movimentacao': mov(GESTO76), 'arquivo': NOME76}]
    P['texto_tela'] = {'hook': 'Turnaround is coming\nyour way...', 'hook_comeca': 'o 1º quadro', 'hook_termina': '~3 s', 'hook_alt': '', 'extras': []}
    mapa(P, 'Turnaround is coming your way...')
    P['comentario_fixado'] = {'insta': 'She was meant to see this 🙏 tap my profile picture above, your reading is waiting in my story',
                              'face': 'Your reading is waiting for you here 🙏 👉 ' + FB}
    ct = P['central']
    ct['config'] = []
    ct['colagens'] = [{'titulo': 'nora76: 1 take só (no Muse, sem a Central)', 'fala': FALA76, 'movimentacao': [mov(GESTO76)], 'takes': [0]}]
    ct['conferir'] = f'Conferir o take: a Nora da {IMG}, sem a pintura, com a canela; ela fala uma vez só e fecha a boca no fim. Renomeie para {NOME76}.'
    ct['agente'] = {
        'imagem': IMG,
        'intro': f'Não precisa da Central: é 1 take só. No Muse, na conversa da Nora, anexe a {IMG} e cole o prompt abaixo.',
        'aviso_tag': f'cole no Muse, com a {IMG} anexada',
        'aviso': prompt_manual(FALA76, mov(GESTO76)),
        'passos': [f'Logo depois dos 13 do nora75: no Muse, anexe a {IMG} e cole o prompt acima, numa mensagem só. ~1 min.',
                   f'Renomeie o clipe para {NOME76}.',
                   'Confira: sem a lua e sem as estrelinhas; ela fala a frase uma vez só e fecha a boca no fim. Se o Muse recusar: “Generate it again, exactly as written.”'],
    }
    P['edicao_linha'] = [
        {'quando': 'A. Só o take novo', 'texto': f'Me mande o {NOME76} aqui no chat do Code, junto com o nora75-montado', 'como': 'Não precisa de CapCut: eu tiro o T01 do nora75 e ponho este no lugar, com a mesma música.'},
        {'quando': 'B. Até ~23h00', 'texto': 'Eu devolvo o nora76-final (Insta) e o nora76-final-FACE', 'como': 'O Face é o mesmo corpo do nora75-FACE no mesmo dia: como no nora72 (teste de 20/11, que não travou). Se preferir, o nora76 vai só no Insta.'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': [{'nome': IMG, 'tipo': 'imagem das falas', 'status': 'reutilizar', 'onde': 'A mesma do nora75.', 'descricao': 'A mesma do nora75.'},
                  {'nome': NOME76, 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{FALA76}”'},
                  {'nome': 'os T02 a T13 do nora75', 'tipo': 'corpo', 'status': 'reutilizar', 'onde': 'Saem do nora75-montado.', 'descricao': 'O mesmo corpo, como a maioria faz.'}],
        'decisao': [
            '1 take no Muse: o corpo do nora75 com outro Take 1, "There is a woman lying down with her phone in her hand right now…" (a 2ª abertura mais repetida: '
            '7 vídeos, 5 contas). É o jeito da maioria: o mesmo corpo com vários ganchos.',
            'As datas do T02 (23, 24 ou 25) valem: à 0h00 de Brasília ainda é 23/11 na costa leste.',
            'Insta e Face ~0h00 (4h30 depois do nora75). Texto do topo em branco solto: “Turnaround is coming your way...”.',
        ],
    }
    P['ordem'] = ['pecas', 'agente', 'cenas', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    return P


def salvar(P, nn, rotulo):
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>' + rotulo + '</title>', html, count=1)
    (R / f'PAINEL-{nn.upper()}.html').write_text(html, encoding='utf-8')
    print('ok', nn, len(html), 'bytes')


if __name__ == '__main__':
    print(N, 'takes,', PALAVRAS, 'palavras')
    salvar(nora75(), 'nora75', 'Painel nora75 · a Nora igual à maioria · 23/11')
    salvar(nora76(), 'nora76', 'Painel nora76 · o mesmo corpo, outro gancho · 23/11')
