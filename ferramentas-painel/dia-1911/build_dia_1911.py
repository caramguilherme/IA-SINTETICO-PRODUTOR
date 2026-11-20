# Painéis do dia 19/11/2026: nora71 (o hook do alçapão + a fala na escada; Insta às 19h30) e nora72 (o hook da canela no carro +
# a fala no carro; Face às 19h30 e Insta à 0h00). A mesma fala nova nos dois; muda só o hook, o cenário e a roupa (decisão do aluno,
# 19/11 ~13h30: "a gente vai usar o mesmo hook da canela e do alçapão… a copy vai ser diferente… a mesma copy nos dois vídeos de hoje";
# "pode montar" às ~13h34).
# A fala: o roteiro 3 da pesquisa oficial do Manifestation ("most people never notice these three things": os 3 sinais → a receptora
# cósmica → ninguém ensinou a ler) com a estrutura da aula 65 (os slides "Viralização x Conversão": identificação → sinais → explicação
# → benefício → CTA qualificado) e o CTA padrão de 19/11 (aula 54 com o texto do funil; Clone R78 a R80). Sem data, sem ameaça, sem
# dinheiro, sem cartas; ~122 palavras (~44 s), 6 takes.
# As imagens e os hooks já existem (d1711-PRE-alcapao-IMG-C, d1711-PRE-carro-IMG-C; os hooks do nora70 e do nora69): só os 6 takes no Muse.
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-1911/build_dia_1911.py
import sys, json, copy, re, pathlib

R = pathlib.Path(__file__).resolve().parents[2]
MODELO = (R / 'PAINEL-MODELO.html').read_text(encoding='utf-8')
assert MODELO.count('const PACOTE = null;') == 1


def pacote(nome):
    p = R / nome if (R / nome).exists() else R / 'arquivo' / 'paineis' / nome
    t = p.read_text(encoding='utf-8')
    i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
    return json.loads(t[i:j])


sys.path.insert(0, str(R / 'ferramentas-painel'))
import voz_consistencia as VC  # noqa: E402
BASE = pacote('PAINEL-NORA70.html')  # o painel do Muse (versão 2 do nora70): o aviso do Muse, a config da Central, o mapa
VOZ = [c for s in BASE['central']['config'] for c in s['campos'] if c['campo'].startswith('Perfil de voz')][0]['copiar']
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
assert FB.endswith('&aff=dl7zx6ks')

ESTRELAS = ('the small flat gold crescent moon on her cheek on the left side of the frame with three tiny separate gold five-pointed stars next to it '
            '(three stars with visible points, never dots or circles)')
JOIAS = (f'the thin braid wrapped with small gold rings, {ESTRELAS}, her star-and-moon drop earrings, her thin gold Venus necklace, the thin gold bracelets and the gold sun ring')

# ------------------------------------------------------------------ as duas cenas (as mesmas do nora70 e do nora69)
ALCAPAO = dict(
    nn='nora71', d='d1911', tag='alcapao', img='d1711-PRE-alcapao-IMG-C', nome='em cima da escada, no corredor, com a estátua ao lado',
    hook='o alçapão com a estátua (o do nora70)',
    roupa_cont='her cream silky long-sleeve wrap blouse tied at the waist and her beige knee-length wrap skirt',
    onde_prompt='stands on an aluminum stepladder in a bright upstairs hallway, under an open attic hatch',
    visual='soft warm indoor evening light in a hallway', som='quiet indoor room sound',
    cam='the camera stays static at her chest height in front of her with an unchanged framing',
    segura=('the hand that rests on the top rail of the ladder stays there the whole time; the dusty angel statue with golden wings stands still on the top cap of the '
            'ladder beside her and never moves'),
    livre_obj='the dusty angel statue with golden wings on the top of the ladder, the aluminum stepladder and the open attic hatch above',
)
CARRO = dict(
    nn='nora72', d='d1911', tag='carro', img='d1711-PRE-carro-IMG-C', nome='no banco do motorista da picape, dirigindo devagar',
    hook='a canela no tapete do carro (o do nora69)',
    roupa_cont='her light heather-gray fitted ribbed top under a long open black knit cardigan',
    onde_prompt="sits in the driver's seat of a dark gray pickup truck that is driving slowly along a quiet suburban street",
    visual='soft natural afternoon daylight inside a car', som='quiet car interior sound and a soft road hum',
    cam=('the phone stays mounted on the dashboard in front of her with an unchanged framing while the truck keeps rolling slowly forward and the houses and '
         'trees glide past the windows behind her'),
    segura=('the hand that holds the steering wheel stays on the wheel the whole time and only makes tiny natural steering corrections; the seatbelt stays '
            'across her chest'),
    livre_obj="the steering wheel, the seatbelt across her chest and the truck's interior",
)

# ------------------------------------------------------------------ a fala (6 takes; até 22 palavras; a 1ª frase do take seguinte não cabe no resto)
FALA = [
    "Most people never notice these three signs. One: you keep seeing eleven eleven, on the clock, on receipts, everywhere you look.",
    "Two: your gut warned you about someone, and you were right. Three: you lived a moment you swear you'd lived before.",
    "If that sounds like you, you may be what we call a cosmic receiver. The universe keeps sending you messages.",
    "Nobody ever taught you how to read them. That's why the signs keep coming, but nothing seems to change.",
    "If one of these felt familiar, your twenty twenty-seven reading starts with what you want most: love, abundance, peace or purpose.",
    "Now pay attention: tap my profile picture and check my story. Three quick questions, and your private reading is ready.",
]
RESERVA = {5: "Now pay attention: tap my profile picture and check my story. Three quick questions, and your reading is ready."}
SUF = ['tres-sinais-1111', 'intuicao-deja-vu', 'receptora-cosmica', 'ninguem-ensinou', 'leitura-2027', 'cta-story']
TXT = ['o gancho + o 1º sinal (o 11:11)', 'o 2º e o 3º sinais (a intuição e o déjà vu)', 'a receptora cósmica + as mensagens',
       'a virada: ninguém ensinou a ler', 'a leitura de 2027 começa com o que ela mais quer', 'o CTA: a foto, o story, 3 perguntas (a seta entra aqui)']
N = len(FALA)
assert len(SUF) == len(TXT) == N
PALAVRAS = sum(len(f.split()) for f in FALA)
assert 110 <= PALAVRAS <= 130, PALAVRAS


def nome(c, i):
    return f'{c["d"]}-{c["tag"]}-T{i + 1:02d}-{SUF[i]}'


GESTOS = [
    'she holds up three fingers beside her shoulder for a moment, then lowers them and points at the lens, with a curious, knowing look',
    'she lightly touches her fingertips to her collarbone, then opens her hand toward the lens beside her shoulder, with a warm, understanding look',
    'she points at the lens and nods slowly, with a calm, confident smile',
    'she opens her free hand palm up beside her shoulder with a gentle, caring look, then lowers it',
    'she brings her open hand up beside her chin and then opens it toward the lens, with a hopeful, warm look',
    'she points down toward the lower left corner of the frame several times, with a warm, encouraging smile',
]
assert len(GESTOS) == N


def mov(c, i):
    return (f'Throughout the whole 10 seconds {c["cam"]}; {c["segura"]}; with her other hand {GESTOS[i]}; her eyes stay on the lens; from the end of the final '
            'sentence of the take until the clip ends she keeps her lips closed and silent; no zoom and no cuts, the braid stays in place and each hand has exactly '
            'five fingers.')


COMUNS = {('of', 'the'), ('and', 'the'), ('to', 'the'), ('in', 'the'), ('on', 'the'), ('at', 'the'), ('for', 'a'), ('of', 'her'), ('and', 'her'),
          ('as', 'if'), ('the', 'lens'), ('and', 'then'), ('the', 'hand'), ('a', 'warm'), ('with', 'a'), ('the', 'whole'), ('for', 'the'), ('the', 'end'),
          ('end', 'of'), ('in', 'front'), ('front', 'of'), ('the', 'final'), ('with', 'the'), ('the', 'clip'), ('of', 'these')}
for c in (ALCAPAO, CARRO):
    for i in range(N):
        for f in [FALA[i]] + ([RESERVA[i]] if i in RESERVA else []):
            assert len(f.split()) <= 22, (c['nn'], i + 1, len(f.split()), f)
            fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(c, i).lower())
            sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS
            assert not sobra, (c['nn'], i + 1, sobra)
            for w in ('card', 'tarot', 'link', 'free', 'portal', 'money', 'cash', 'november', 'december'):
                assert w not in f.lower(), (i + 1, w)
        if i + 1 < N:  # a 1ª frase do take seguinte não pode caber no resto deste (folga de 3 palavras)
            prox = re.split(r'(?<=[.!?])\s+', FALA[i + 1])[0]
            assert len(FALA[i].split()) + len(prox.split()) >= 25, (c['nn'], i + 1, 'cabe no take anterior')
        frases = re.split(r'(?<=[.!?])\s+', FALA[i])  # as frases de dentro do take somam até 22 (a Central junta)
        assert sum(len(x.split()) for x in frases) <= 22


def livre(c):
    if c['tag'] == 'carro':
        abre = ("Casual real video in the afternoon inside a dark gray pickup truck that is driving slowly along a quiet American suburban street, filmed by a phone "
                "mounted on the dashboard about 60 centimeters in front of her at face height, looking exactly like a real phone video, lit by soft natural daylight "
                "through the windows. She sits in the driver's seat. The truck keeps moving slowly forward during every take: through the side and rear windows the "
                "houses, lawns and trees glide past smoothly and the daylight shifts gently across her face; the camera moves only with the very slight vibration of "
                "the road. ")
    else:
        abre = ('Casual real video in the evening in a bright upstairs hallway of an American home with white walls and a white ceiling, filmed from a static camera '
                'at her chest height about one meter in front of her, looking exactly like a real phone video, lit by soft warm indoor light. She stands on an aluminum '
                'stepladder right under the open attic hatch. ')
    return abre + (
        f'CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, {JOIAS}, {c["roupa_cont"]}, and {c["livre_obj"]} stay exactly as in the '
        f'reference image; the framing is exactly the one of the reference image, her face in the upper middle of the frame; {c["segura"]}; natural skin texture with '
        'visible pores, slight phone grain, everything in focus, no bokeh, no filter, no glow and no sparkles; no zoom, no cuts and no reframing; no phone, phone stand, '
        'tripod, object, person, animal or text appears or disappears; each hand always has exactly five fingers; no on-screen text, no captions; '
        f'{c["som"]} only, no music. SPEECH RULE for every take: she says only the exact words of that take\'s script, each word exactly once and in order, with no '
        'repeated word, no extra word and no added sentence before, between or after; numbers are spoken as words exactly as written; she speaks in a warm, calm and '
        'confident tone, like a friend who understands signs talking to one person; when she finishes the last word she closes her lips, stays silent and keeps a '
        'calm still expression until the clip ends.')


def prompt_manual(c, txt, movimento):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image '
            f'{c["onde_prompt"]} and speaks directly to the camera.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + txt + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            'VOICE PACING: medium pace (155 to 180 words per minute), about 8 seconds of speech, warm, calm and confident; when she finishes the last word she closes '
            'her lips and stays silent with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + movimento + '\n\n'
            f'VISUAL: realistic casual phone video, {c["visual"]}, natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter.\n\n'
            + ('CAMERA: mounted on the dashboard, no zoom, no cuts, no reframing; the street keeps gliding past the windows.\n\n' if c['tag'] == 'carro'
               else 'CAMERA: static at chest height, no zoom, no cuts, no reframing.\n\n')
            + f'AUDIO: only her voice and {c["som"]}; no music, no other voices, no sound effects.\n\n'
            f'CONTINUITY: her face, long black wavy hair, {JOIAS}, {c["roupa_cont"]}, {c["livre_obj"]} and everything behind her stay exactly as in the reference image; '
            'no phone, object, person or text appears; each hand has exactly five fingers; no on-screen text or captions.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.')


def config(c):
    cf = copy.deepcopy(BASE['central']['config'])
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = f'colar o texto abaixo (a imagem é a {c["img"]}, a mesma das falas do {"nora70" if c["tag"] == "alcapao" else "nora69"})'
                campo['copiar'] = livre(c)
            elif campo['campo'] == 'COLE SUA COPY AQUI':
                campo['valor'] = 'colar a fala inteira (seção “A fala e a movimentação”): é 1 colagem só, com os 6 takes'
            elif campo['campo'] == 'Movimento de câmera':
                campo['valor'] = ('Estático / câmera parada, sem zoom (o LIVRE já diz que a câmera está presa no painel e que a rua passa nas janelas)' if c['tag'] == 'carro'
                                  else 'Estático / câmera parada, sem zoom (se essa opção não existir: Handheld sutil, sem zoom; o LIVRE já diz câmera parada)')
            elif campo['campo'] == 'Atmosfera / mood':
                campo['valor'] = 'Caloroso e acolhedor'
            elif campo['campo'] == 'Movimentação':
                campo['valor'] = 'colar as 6 linhas, uma por take (seção “A fala e a movimentação”)'
            elif campo['campo'] == 'Conferir':
                campo['valor'] = '6 takes (8 ou 10 s cada, como na lista da seção “A fala e a movimentação”)'
    VC.adicionar(cf)
    return cf


AVISO_MUSE = BASE['central']['agente']['aviso']
assert 'NORA_VOICE_LOCK' in AVISO_MUSE and 'do not rewrite it' in AVISO_MUSE


def agente(c):
    lista = ' · '.join(f'{i + 1} = {nome(c, i)}' for i in range(N))
    confere = ('se ela continua no banco do motorista, com o cinto, a mão no volante e a rua passando nas janelas' if c['tag'] == 'carro'
               else 'se a estátua continua parada no alto da escada e a mão no corrimão')
    passos = [
        'No Muse, na conversa da Nora (as regras e a voz já estão salvas lá). Não tem modelo nem resolução para escolher: o Muse gera em 704×1232 a 24 qps, e eu '
        'ajusto na edição. ~1 min e ~2,6% do grátis da semana por take (os 6: ~16%). Gere cedo: o Muse tem um limite de ~15 vídeos por dia, e hoje são 12 (nora71 + nora72).',
        f'É 1 MENSAGEM só: a imagem {c["img"]} + o aviso do Muse + o “COPIAR TUDO JUNTO” da Central (os 6 takes).',
        f'Renomeie cada take com o nome da lista (o número é a ordem na mensagem): {lista}. O Muse numera 01, 02…; você renomeia pelo número.',
        f'Confira cada take: {confere}; se a lua no rosto tem as 3 estrelinhas; se ela fala uma vez só, sem repetir palavra, e diz “eleven eleven” e “twenty '
        'twenty-seven” por extenso (o 1º quadro pode sair um pouco diferente da imagem: normal no Muse). Se o Muse recusar um prompt: NÃO deixe ele reescrever; mande na '
        'mesma conversa “Generate prompt X again, exactly as written.” (X = o número dele na mensagem). Se recusar de novo, use a reserva do take (abaixo).',
    ]
    for i in sorted(RESERVA):
        passos.append(f'Se o Muse recusar o T{i + 1:02d} 2 vezes (o “private”): na mesma conversa, anexe a {c["img"]} e mande o prompt abaixo (a mesma fala sem o '
                      f'“private”). Renomeie para {nome(c, i)}. PROMPT: ' + prompt_manual(c, RESERVA[i], mov(c, i)))
    passos += [
        'Se outro take for recusado 2 vezes: me manda o número e a mensagem do Muse aqui, que eu troco a palavra que travou.',
        'Se o Muse parar no meio: responda na MESMA conversa, sem anexar nada: “Please continue and generate prompts X to Y from my previous message, in the same order.” '
        '(troque X e Y pelos números que faltaram).',
        'Se aparecer o limite do dia (“video_daily_budget_exhausted”): me avise na hora com quantos takes já saíram.',
    ]
    return {
        'imagem': c['img'],
        'intro': f'No Muse, na conversa da Nora: anexe a {c["img"]}, cole o aviso do Muse e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central (1 colagem: 1 mensagem). '
                 'Não precisa me mandar o prompt da Central.',
        'aviso_tag': 'cole antes do bloco da Central, no Muse',
        'aviso': AVISO_MUSE,
        'passos': passos,
    }


# ------------------------------------------------------------------ o que vai na tela e nos textos
HOOK_CAIXA = 'Most people never notice\nthese [3 signs]'
LEG_INSTA = {
    'nora71': ('Most people never notice these 3 signs 👀 Your private reading is waiting in my story 🔮\n'
               'Comment 1, 2 or 3: which sign have you seen? 👇\n'
               '#manifestation #1111 #messagefromtheuniverse #2027 #lawofattraction'),
    'nora72': ('Most people never notice these 3 signs 👀 Your private reading is waiting in my story 🔮\n'
               'Comment the number you keep seeing 👇\n'
               '#manifestation #angelnumbers #messagefromtheuniverse #2027 #lawofattraction'),
}
LEG_FACE = {
    'nora71': ('Most people never notice these 3 signs ✨ Your reading is waiting in my story and in the comments 🔮\n'
               '#manifestation #1111 #messagefromtheuniverse #2027'),
    'nora72': ('You were never imagining it ✨ Most people never notice these 3 signs. Your reading is waiting in my story and in the comments 🔮\n'
               '#manifestation #angelnumbers #messagefromtheuniverse #2027'),
}
FIX_FACE = {
    'nora71': 'Your reading is waiting for you here 🙏 👉 ',
    'nora72': 'Your 2027 reading is waiting for you here ✨ 👉 ',
}
FIX_INSTA = {
    'nora71': 'If even one of these signs is yours ✨ tap my profile picture above, your 2027 reading is waiting in my story',
    'nora72': 'You were never imagining it 🙏 tap my profile picture above, your 2027 reading is waiting in my story',
}
QUANDO = {
    'nora71': ('Insta às 19h30 de hoje (19/11), o nora71-final; Face às 19h30, o nora71-final-FACE (com a variação do Face).'),
    'nora72': ('Insta e Face, postados às 01h20 de 20/11 (decisão do aluno às 01h04): o nora72-final no Insta e o nora72-final-FACE no Face. No Face é teste: o mesmo corpo do nora71-FACE, ~5 h depois.'),
}
HIPOTESE = {
    'nora71': 'Hipótese: a fala que qualifica (os 3 sinais) leva gente ao perfil e ao story (o nora69 e o nora70 tiveram 0 visitas), com o hook que segurou 26 s no Insta.',
    'nora72': 'Hipótese: com a mesma fala do nora71, o hook e o cenário do carro (o par do nora69, que saiu com o mesmo hook e a copy da claire_mayaus).',
}
HOOK_LINHA = {
    'nora71': ('O hook do alçapão já está comigo (o do nora70, sem texto). Não põe no CapCut: eu emendo ele antes do T01, com o flash branco.'),
    'nora72': ('O hook da canela está comigo, remontado sem texto a partir dos 3 clipes que você mandou (20/11 00h55). Não põe no CapCut.'),
}


def montar(c):
    P = copy.deepcopy(BASE)
    nn = c['nn']
    P.pop('pre_gancho', None)
    P['ocultar_bloco_agente_imagem'] = True
    P['figurino'] = c['roupa_cont']
    P['imagens_titulo'] = f'Imagem das falas (a {c["img"]}, que você já tem)'
    P['refs'] = [f'{c["img"]} em todos os takes']
    P['roteiro'] = {
        'id': f'{nn}-{c["tag"].upper()}-1911',
        'titulo': (f'{nn} · {QUANDO[nn].split(".")[0]} · a fala nova dos 3 sinais (pesquisa oficial + aula 65), com o hook {c["hook"]}'),
        'duracao_total': 44,
        'descricao_instagram': LEG_INSTA[nn],
        'descricao_face': LEG_FACE[nn],
    }
    P['imagens'] = [{'rotulo': f'IMAGEM 1 · {c["img"]}', 'cena': f'já existe ({c["nome"]})', 'anexar': f'a {c["img"]} (a mesma das falas do {"nora70" if c["tag"] == "alcapao" else "nora69"})'}]
    P['videos'] = [{'rotulo': f'T{i + 1:02d}', 'cena': TXT[i], 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({c["img"]})', 'acao': '', 'b_roll': '',
                    'fala': FALA[i], 'movimentacao': mov(c, i), 'arquivo': nome(c, i)} for i in range(N)]
    P['texto_tela'] = {'hook': HOOK_CAIXA, 'hook_comeca': 'o 1º quadro do hook', 'hook_termina': 'o fim de “these three signs.” (a 1ª frase)', 'hook_alt': '', 'extras': []}
    P['comentario_fixado'] = {'insta': FIX_INSTA[nn], 'face': FIX_FACE[nn] + FB}
    rf = P['respostas_face']
    rf['link'] = FB
    rf['insta'] = ['I see you 🙏 your 2027 reading is waiting in my story',
                   "That's not a coincidence ✨ tap my photo, your next step is in my story",
                   'So glad this found you today 💛 check my story',
                   "You're not imagining it 🙏 tap my photo for your reading",
                   'Received ✨ your reading is in my story 🔮']
    P['story'] = {'ja_postado': True,
                  'nota': ('O story-1811 vence às ~18h55 de hoje: reposte antes, ao vivo, no Insta e no Face (o mesmo arquivo, com o adesivo do link). Sem story no ar, o vídeo não leva a lugar nenhum.'
                           if nn == 'nora71' else 'Antes de postar, confira se o story repostado em 19/11 às 18h15 está no ar no Insta e no Face (vale até ~18h15 de 20/11: reposte antes).')}
    m = P['mapa_tela']
    m['legenda'] = [69, 77]
    m['estilos'] = [
        {'nome': 'Caixa do topo (eu ponho)', 'fonte': 'negrito', 'cor': 'branca, letra preta, “3 signs” em vermelho', 'tamanho': '2 linhas', 'contorno': '—',
         'obs': 'Do 1º quadro do hook até o fim da 1ª frase. Depois, a tela fica só com a Nora, a legenda e os números.'},
        {'nome': 'Legenda (eu ponho)', 'fonte': 'Inter, peso normal', 'cor': 'branca, sem destaque', 'tamanho': 'até ~6 palavras, 2 linhas', 'contorno': 'fino escuro + sombra suave',
         'obs': 'Entra na 1ª palavra.'},
        {'nome': 'Faixa do CTA + seta', 'fonte': '—', 'cor': 'branca com preto e vermelho; seta vermelha', 'tamanho': '—', 'contorno': '—',
         'obs': 'Embaixo à esquerda, logo acima da foto do perfil (X −300, Y −400), do “tap my profile picture” até o fim.'},
    ]
    m['regras'] = ['O estilo “simples” (18/11 23h30): a caixa branca só no gancho, a legenda simples, os 2 números brancos, a faixa e a seta no CTA.',
                   'Flash branco de ~0,3 s entre o hook e a fala.',
                   'Eu ponho tudo (P45); você monta só o vídeo e a música.']
    m['numeros'] = [{'t': '222', 'x': 18, 'y': 16, 'onde': 'alto à esquerda, o vídeo todo', 'cor_nome': 'branco', 'cor': '#FFFFFF', 'tamanho': 11},
                    {'t': '11:11', 'x': 82, 'y': 16, 'onde': 'alto à direita, o vídeo todo', 'cor_nome': 'branco', 'cor': '#FFFFFF', 'tamanho': 11}]
    P['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” só os 6 takes do Muse (T01 a T06), de uma vez. O hook não entra: ele está comigo. '
                 '“Zoom nos cortes” = DESLIGADO (igual ao nora70); o resto como abaixo.',
        'nome': f'{nn}-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pela ordem do nome (T01 a T06)',
        'depois': ['Suba os 6 takes e espere a Prévia.',
                   'Aperte play com Resultado marcado: confira a primeira palavra do T01 e a última do T06.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro. O balanço do corpo no fim de cada take, eu corto aqui.',
                   f'Clique em Cortar e baixar e salve como {nn}-cortado.'],
    }
    saida = (f'Eu devolvo o {nn}-final (Insta, 19h30) e o {nn}-final-FACE (Face, 19h30, com a variação do Face).' if nn == 'nora71'
             else f'Eu devolvo o {nn}-final (Insta, 0h00) e o {nn}-final-FACE (para decidir amanhã).')
    P['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {nn}-cortado', 'como': 'É o vídeo que saiu da FusionZ. Começa direto no T01.'},
        {'quando': 'B. O hook: NÃO põe no CapCut', 'texto': HOOK_LINHA[nn], 'como': 'Eu monto o hook, ponho o flash branco e emendo antes do T01.'},
        {'quando': '1. Do T01 ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Começa no 1º quadro do montado.'},
        {'quando': '2. Exportar e me mandar (' + ('até ~18h40' if nn == 'nora71' else 'até ~23h') + ')', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'1080×1920, nome {nn}-montado (acima de 30 MB, link do Drive). {saida}'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': ([{'nome': c['img'], 'tipo': 'imagem das falas', 'status': 'reutilizar', 'onde': 'É a mesma imagem das falas do ' + ('nora70.' if c['tag'] == 'alcapao' else 'nora69.') + ' Anexe ela no Muse.', 'descricao': 'A mesma do ' + ('nora70.' if c['tag'] == 'alcapao' else 'nora69.')},
                   {'nome': 'hook ' + c['hook'], 'tipo': 'hook', 'status': 'reutilizar', 'onde': 'O hook já está comigo; eu emendo antes do T01, com o flash branco.', 'descricao': 'Eu emendo antes do T01, com o flash branco.'}]
                  + [{'nome': nome(c, i), 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{FALA[i]}”'} for i in range(N)]),
        'decisao': [
            f'6 takes no Muse (~16% do grátis da semana), {PALAVRAS} palavras (~44 s): a fala nova dos 3 sinais (o roteiro 3 da pesquisa oficial com a estrutura da '
            'aula 65), sem data, sem ameaça, sem dinheiro, com o CTA padrão. A mesma fala no nora71 e no nora72.',
            QUANDO[nn],
            HIPOTESE[nn],
            ('O montado até ~18h40. O story-1811 vence às ~18h55: reposte antes, no Insta e no Face.' if nn == 'nora71'
             else 'O montado até ~23h (o Insta vai à 0h00). O story repostado hoje às ~18h55 vale até ~18h55 de amanhã.'),
        ],
    }
    ct = P['central']
    ct['config'] = config(c)
    ct['colagens'] = [{'titulo': f'{nn}: a colagem única (T01 a T06)', 'fala': ' '.join(FALA), 'movimentacao': [mov(c, i) for i in range(N)],
                     'takes': list(range(N))}]
    ct['agente'] = agente(c)
    ct['conferir'] = (f'Conferir em cada take: é a Nora da imagem C (rosto, lua com as 3 estrelinhas, trança, brincos, colar de Vênus); '
                      + ('no carro, a mão no volante, o cinto e a rua passando; ' if c['tag'] == 'carro' else 'na escada, a estátua parada no alto da escada e a mão no corrimão; ')
                      + 'ela fala uma vez só, em inglês, com “eleven eleven” e “twenty twenty-seven” por extenso. Renomeie com o nome da lista.')
    P['ordem'] = ['pecas', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    return P


if __name__ == '__main__':
    for c in (ALCAPAO, CARRO):
        P = montar(c)
        html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';')
        rotulo = {'nora71': 'Painel nora71 · alçapão · 19/11', 'nora72': 'Painel nora72 · canela no carro · 19/11'}[c['nn']]
        html = re.sub(r'<title>[^<]*</title>', '<title>' + rotulo + '</title>', html, count=1)
        (R / f'PAINEL-{c["nn"].upper()}.html').write_text(html, encoding='utf-8')
        print('ok', c['nn'], len(html), 'bytes;', PALAVRAS, 'palavras')
