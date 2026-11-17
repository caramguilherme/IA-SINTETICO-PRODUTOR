# Painéis do dia 17/11/2026: nora69 (o hook da canela no tapete do carro e a fala no carro em movimento; Face às 19h30, Insta quando a proxy voltar)
# e nora70 (o hook do alçapão com a estátua de São Miguel e a fala na escada; Insta e Face à 0h00).
# Decisão do aluno (17/11 ~13h10): "quero testar os dois vídeos de hoje no mesmo modelo desses 6 vídeos [da claire_mayaus]… a mesma copy igualzinha… com as
# ameaças, falando lá dos minutos… o visual vai ser limpo… a legenda automática na cor branca… os números também do jeito que tá, a seta aparecendo na hora
# que ela fala para clicar na foto… sem mudar nada, sem proibir nada". É o "pode montar".
# A fala é a do v2 (nora69) e a do v6 (nora70) da claire_mayaus (TRANSCRICOES/2026-11-17-claire-mayaus-6-videos.md), com só 3 mudanças:
#   (1) a data do dia; (2) sem a palavra "free" (a leitura é paga: é a única coisa falsa sobre o produto, e a Appyon proíbe);
#   (3) frases que passavam de 22 palavras foram encurtadas ou partidas para caber num take de 10 s (a Central junta frases inteiras até ~22 palavras).
# Imagens como EDIÇÃO da d1511-PRE-sal-IMG-C (a Nora aprovada) + a folha: lição de 14/11 20h20. Clipes do hook com PROMPT CURTO (aula 54; 16/11).
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-1711/build_dia_1711.py
import json, copy, re, pathlib

R = pathlib.Path(__file__).resolve().parents[2]
MODELO = (R / 'PAINEL-MODELO.html').read_text(encoding='utf-8')
assert MODELO.count('const PACOTE = null;') == 1


def pacote(nome):
    p = R / nome if (R / nome).exists() else R / 'arquivo' / 'paineis' / nome
    t = p.read_text(encoding='utf-8')
    i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
    return json.loads(t[i:j])


P46 = pacote('PAINEL-NORA46.html')
P51 = pacote('PAINEL-NORA51.html')
P66 = pacote('PAINEL-NORA66.html')
P49 = pacote('PAINEL-NORA49.html')
CFG = copy.deepcopy(P51['central']['config'])
VOZ = [c for s in CFG for c in s['campos'] if c['campo'].startswith('Perfil de voz')][0]['copiar']
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'

ESTRELAS = ('the small flat gold crescent moon on her cheek on the left side of the frame with three tiny separate gold five-pointed stars next to it '
            '(three stars with visible points, never dots or circles)')
JOIAS = (f'the thin braid wrapped with small gold rings, {ESTRELAS}, her star-and-moon drop earrings, her thin gold Venus necklace, the thin gold bracelets and the gold sun ring')
ESTATUA = ('an old painted resin statue of Saint Michael the Archangel, about 35 centimeters tall, with large beige-brown painted wings, silver-gray armor, a faded '
           'pinkish-red cape, one arm raising a sword high, standing on a rocky painted base, covered with a thin layer of grey dust')

# ------------------------------------------------------------------ as duas cenas
CARRO = dict(
    nn='nora69', d='d1711', tag='carro', img='d1711-PRE-carro-IMG-C', nome='no banco do motorista da picape, dirigindo devagar',
    roupa_cont='her light heather-gray fitted ribbed top under a long open black knit cardigan',
    onde_prompt="sits in the driver's seat of a dark gray pickup truck that is driving slowly along a quiet suburban street",
    visual='soft natural afternoon daylight inside a car', som='quiet car interior sound and a soft road hum',
    cam=('the phone stays mounted on the dashboard in front of her with an unchanged framing while the truck keeps rolling slowly forward and the houses and '
         'trees glide past the windows behind her'),
    segura=('the hand that holds the steering wheel stays on the wheel the whole time and only makes tiny natural steering corrections; the seatbelt stays '
            'across her chest'),
    livre_obj="the steering wheel, the seatbelt across her chest and the truck's interior",
)
ALCAPAO = dict(
    nn='nora70', d='d1711', tag='alcapao', img='d1711-PRE-alcapao-IMG-C', nome='em cima da escada, no corredor, com a estátua ao lado',
    roupa_cont='her cream silky long-sleeve wrap blouse tied at the waist and her beige knee-length wrap skirt',
    onde_prompt='stands on an aluminum stepladder in a bright upstairs hallway, under an open attic hatch',
    visual='soft warm indoor evening light in a hallway', som='quiet indoor room sound',
    cam='the camera stays static at her chest height in front of her with an unchanged framing',
    segura=('the hand that rests on the top rail of the ladder stays there the whole time; the dusty angel statue with golden wings stands still on the top cap of the '
            'ladder beside her and never moves'),
    livre_obj='the dusty angel statue with golden wings on the top of the ladder, the aluminum stepladder and the open attic hatch above',
)

# ------------------------------------------------------------------ falas (17 takes; até 22 palavras; o take seguinte não cabe no resto: a Central junta frases inteiras)
FALAS = {
    'nora69': [
        "Keep your mouth shut if this video showed up for you on Tuesday, November seventeenth or Wednesday, November eighteenth.",
        "Do not tell anyone what's about to happen. I don't know your name or what you did.",
        "But the universe saw your faith, and a major turnaround is coming your way over the next few days.",
        "A very unusual shift is happening in your life. There is money, prosperity, and someone incredibly wonderful about to show up unexpectedly.",
        "But if you turn your back on this message, the blessings will turn their backs on you too. So take this seriously.",
        "Saint Michael the Archangel has sent a warning. A phase of victory and prosperity is approaching your life.",
        "The worst is finally over, and I can already see the chains keeping you trapped in scarcity breaking apart.",
        "The doors that wouldn't open for you are finally going to start opening.",
        "In the next seven minutes, a powerful energy of abundance will wash over you and stay with you forever.",
        "Send this video to yourself right now, because in seven minutes you are going to come back and confirm this energetic shift.",
        "Now save this video, because that will be your first seal. Double tap quickly on the screen.",
        "That will be your second seal, and comment I believe so I can see you did everything.",
        "If you did everything right, tomorrow morning at ten ten, you'll receive incredibly good news confirming the start of this new phase.",
        "But the universe is warning me this shift will only happen to people whose energy is aligned with its frequency of abundance.",
        "That is why I left a quick reading in my stories that will reveal if you are one of them.",
        "Tap my profile picture down below and go check it out right now.",
        "Because you could be one step away from living everything you've ever dreamed of.",
    ],
}
F70 = list(FALAS['nora69'])
F70[0] = "Keep your mouth shut. If this video showed up for you on November eighteenth, do not tell anyone what's about to happen."
F70[1] = "I don't know your name or what you did, but the universe saw your faith."
F70[2] = "A major turnaround is coming your way over the next few days, and a very unusual shift is happening in your life."
F70[3] = "There is money, prosperity, and someone incredibly wonderful about to show up unexpectedly."
F70[11] = "That will be your second seal, and write I believe in the comments so I can see you did everything."
F70[13] = "But I'm being warned that this shift will only happen to people whose energy is aligned with the universe's frequency of abundance."
F70[15] = "So tap my profile picture down below and go check it out right now."
FALAS['nora70'] = F70

# reservas (se a fala cair no filtro do Flow 2 vezes)
RESERVA = {
    0: {'nora69': "Keep this to yourself if this video showed up for you on Tuesday, November seventeenth or Wednesday, November eighteenth.",
        'nora70': "Keep this to yourself. If this video showed up for you on November eighteenth, do not tell anyone what's about to happen."},
    3: {'nora69': "A very unusual shift is happening in your life. There is abundance, prosperity, and someone incredibly wonderful about to show up unexpectedly.",
        'nora70': "There is abundance, prosperity, and someone incredibly wonderful about to show up unexpectedly."},
    5: {'nora69': "Saint Michael has sent a message. A phase of victory and prosperity is approaching your life.",
        'nora70': "Saint Michael has sent a message. A phase of victory and prosperity is approaching your life."},
    12: {'nora69': "If you did everything right, tomorrow morning at ten ten, you'll get incredibly good news confirming the start of this new phase.",
         'nora70': "If you did everything right, tomorrow morning at ten ten, you'll get incredibly good news confirming the start of this new phase."},
}
SUF = ['abertura-data', 'nao-conte', 'universo-viu', 'dinheiro-alguem', 'ameaca', 'sao-miguel', 'correntes', 'portas', 'sete-minutos', 'mande-pra-si',
       '1o-selo', '2o-selo-comente', 'amanha-10h10', 'alinhadas', 'leitura-story', 'toque-foto', 'um-passo']
TXT = ['a abertura com a data e o segredo', 'não conte + "eu não sei seu nome"', 'o universo viu a sua fé + a virada', 'a mudança + dinheiro, prosperidade e alguém',
       'a ameaça + "leve a sério"', 'São Miguel mandou um aviso', 'o pior passou + as correntes', 'as portas abrindo', 'nos próximos 7 minutos',
       'mande o vídeo para você', 'o 1º selo (salvar) + toque duas vezes', 'o 2º selo + o comentário "I believe"', 'amanhã às 10h10 a notícia',
       'só para quem está alinhada', 'por isso a leitura no story', 'toque na foto do perfil (a seta entra aqui)', 'a um passo de tudo o que sonhou']
N = len(SUF)
assert all(len(FALAS[k]) == N for k in FALAS)


def fala(c, i):
    return FALAS[c['nn']][i]


def nome(c, i):
    return f'{c["d"]}-{c["tag"]}-T{i + 1:02d}-{SUF[i]}'


GESTOS = [
    'she points her index finger straight at the lens and keeps it there, with a serious, knowing look',
    'she raises her open palm toward the lens like a gentle stop sign, then lowers it, with a firm look',
    'she points at the lens and moves her finger slightly with the rhythm of her words, eyebrows raised',
    'she points at the lens, tilts her head slightly and gives a small knowing smile at the end',
    'she slowly wags her index finger from side to side, with a stern, serious look',
    'she points at the lens and briefly closes her eyes, then opens them with an intense look',
    'she points at the lens and nods slowly, with a calm, confident look',
    'she opens her free hand toward the lens with a hopeful look, then points at the lens again',
    'she points at the lens with a wide-eyed, excited look',
    'she points at the lens and then taps her chest once with her fingertips, with an urgent look',
    'she makes two quick taps in the air toward the lens with her fingertip, then points at the lens',
    'she points at the lens and nods twice, with an encouraging look',
    'she points at the lens with a bright, excited smile',
    'she raises her index finger beside her face as if giving a warning, with a serious look',
    'she points at the lens, then points down toward the lower corner of the frame, with a warm look',
    'she points down toward the lower left corner of the frame several times, with an urgent, encouraging look',
    'she points at the lens and gives a warm, hopeful smile at the end',
]
assert len(GESTOS) == N


def mov(c, i):
    return (f'Throughout the whole 10 seconds {c["cam"]}; {c["segura"]}; with her other hand {GESTOS[i]}; her eyes stay on the lens; from the end of the final '
            'sentence of the take until the clip ends she keeps her lips closed and silent; no zoom and no cuts, the braid stays in place and each hand has exactly '
            'five fingers.')


COMUNS = {('of', 'the'), ('and', 'the'), ('to', 'the'), ('in', 'the'), ('on', 'the'), ('at', 'the'), ('for', 'a'), ('of', 'her'), ('and', 'her'),
          ('as', 'if'), ('the', 'lens'), ('and', 'then'), ('the', 'hand'), ('she', 'gives'), ('a', 'warm'), ('with', 'a'), ('the', 'whole'), ('a', 'small'),
          ('for', 'the'), ('the', 'take'), ('the', 'first'), ('of', 'her'), ('at', 'the'), ('she', 'points'), ('points', 'at'), ('the', 'ladder'), ('the', 'wheel'),
          ('on', 'the'), ('the', 'end'), ('end', 'of'), ('in', 'front'), ('front', 'of'), ('the', 'final'), ('to', 'the'), ('a', 'serious'), ('it', 'there'),
          ('the', 'truck'), ('with', 'the'), ('her', 'words'), ('you', 'are')}
for c in (CARRO, ALCAPAO):
    for i in range(N):
        textos = [fala(c, i)] + ([RESERVA[i][c['nn']]] if i in RESERVA else [])
        for f in textos:
            assert len(f.split()) <= 22, (c['nn'], i + 1, len(f.split()), f)
            fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(c, i).lower())
            sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS
            assert not sobra, (c['nn'], i + 1, sobra)
            for w in ('private', 'card', 'tarot', 'link', 'free', 'portal'):
                assert w not in f.lower(), (i + 1, w)
        if i + 1 < N:  # a 1ª frase do take seguinte não pode caber no resto deste (folga de 3 palavras: a Central já juntou 23)
            prox = re.split(r'(?<=[.!?])\s+', fala(c, i + 1))[0]
            assert len(fala(c, i).split()) + len(prox.split()) >= 25, (c['nn'], i + 1, 'cabe no take anterior')


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
        'repeated word, no extra word and no added sentence before, between or after; numbers and dates are spoken as words exactly as written; she speaks in a direct, '
        'serious, intimate tone, like telling a secret to one person; when she finishes the last word she closes her lips, stays silent and keeps a calm still '
        'expression until the clip ends.')


def prompt_manual(c, txt, movimento):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image '
            f'{c["onde_prompt"]} and speaks directly to the camera.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + txt + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            'VOICE PACING: medium pace (155 to 180 words per minute), about 8 seconds of speech, direct and serious; when she finishes the last word she closes her lips '
            'and stays silent with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + movimento + '\n\n'
            f'VISUAL: realistic casual phone video, {c["visual"]}, natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter.\n\n'
            + ('CAMERA: mounted on the dashboard, no zoom, no cuts, no reframing; the street keeps gliding past the windows.\n\n' if c['tag'] == 'carro'
               else 'CAMERA: static at chest height, no zoom, no cuts, no reframing.\n\n')
            + f'AUDIO: only her voice and {c["som"]}; no music, no other voices, no sound effects.\n\n'
            f'CONTINUITY: her face, long black wavy hair, {JOIAS}, {c["roupa_cont"]}, {c["livre_obj"]} and everything behind her stay exactly as in the reference image; '
            'no phone, object, person or text appears; each hand has exactly five fingers; no on-screen text or captions.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.')


def config(c):
    cf = copy.deepcopy(CFG)
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = f'colar o texto abaixo (fechado pela {c["img"]}, a imagem C do hook)'
                campo['copiar'] = livre(c)
            elif campo['campo'] == 'Movimento de câmera':
                campo['valor'] = ('Estático / câmera parada, sem zoom (o LIVRE já diz que a câmera está presa no painel e que a rua passa nas janelas)' if c['tag'] == 'carro'
                                  else 'Estático / câmera parada, sem zoom (se essa opção não existir: Handheld sutil, sem zoom; o LIVRE já diz câmera parada)')
            elif campo['campo'].startswith('Velocidade'):
                campo['valor'] = 'Média — CTA (155–180 WPM). É a velocidade padrão da Nora. No agente, cada take sai com 10 s (Omni 1.2 Flash em 360p, 10 créditos).'
            elif campo['campo'] == 'Estilo visual':
                campo['valor'] = 'UGC moderno (o LIVRE descreve)'
    return cf


PRE_LUCAS = ('Below, you will find several prompts, each corresponding to a different video. Please generate all the videos in sequential order, from the first prompt to the last.\n'
             'Maintain the exact same voice across all videos, ensuring EXACTLY THE SAME VOLUME, with no variations in background, intonation, or vocal clarity. Use the attached image as both the first and last frame of every generated video.\n'
             'Please submit ALL generation requests at once and in the correct order, so that all videos can be generated simultaneously.\n'
             'If the generation of any video fails, please resubmit ONLY the item that failed until it is successfully generated.')
LOTES = [list(range(0, 9)), list(range(9, N))]


def agente(c):
    lista = []
    for li, lote in enumerate(LOTES):
        lista.append(f'{li + 1}ª mensagem: ' + ' · '.join(f'{j + 1} = {nome(c, i)}' for j, i in enumerate(lote)))
    confere = ('se ela continua no banco do motorista, com o cinto, a mão no volante e a rua passando nas janelas' if c['tag'] == 'carro'
               else 'se a estátua continua parada no alto da escada e a mão no corrimão da escada')
    passos = [
        'Conta do Flow: a que você escolher (~170 créditos os 17 takes). Abra um PROJETO NOVO no Flow e uma conversa nova no agente.',
        'Nas configurações do agente: Omni 1.2 Flash · 360p · 10 s · 9:16 (10 créditos por take) e gerar sem pedir aprovação. Depois, BAIXE cada take em 720p (não gasta crédito).',
        f'São 17 takes em 2 MENSAGENS na mesma conversa (são 2 colagens na Central): 1ª mensagem = a imagem {c["img"]} + o aviso + o “COPIAR TUDO JUNTO” da 1ª colagem (T01 a T09); '
        'quando os 9 terminarem, 2ª mensagem = o aviso + o “COPIAR TUDO JUNTO” da 2ª colagem (T10 a T17), anexando a mesma imagem de novo.',
        'Renomeie cada take com o nome da lista (o número é a ordem dentro de cada mensagem): ' + ' || '.join(lista) + '. '
        'Se ele não renomear, mande na mesma conversa: “Now rename each video with the correct number from the prompt.”',
        f'Confira na grade, pelo nome, se os 17 saíram; {confere}; se a lua no rosto tem as 3 estrelinhas; e se ela fala uma vez só, sem repetir palavra. '
        'Se um falhar por política: mande na mesma conversa “Please generate video X from my previous message again, with the same prompt.” (X = o número dele na mensagem). '
        'Se falhar de novo, use o prompt à mão do take (abaixo).',
    ]
    for i in sorted(RESERVA):
        passos.append(f'Se o T{i + 1:02d} falhar 2 vezes: à mão, Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; Início = {c["img"]}; Fim = vazio; cole o '
                      f'prompt abaixo (10 créditos) e renomeie para {nome(c, i)}. PROMPT: ' + prompt_manual(c, RESERVA[i][c['nn']], mov(c, i)))
    passos += [
        'Se outro take falhar 2 vezes: à mão, o mesmo caminho, com o prompt do take que a Central gerou (o COPIAR do take).',
        'Se o agente parar no meio (por exemplo, “alta demanda”): responda na MESMA conversa, sem anexar nada: “Please continue and generate videos X to Y from my previous message, in the same order.” '
        '(troque X e Y pelos números que faltaram). Se ele gerar só o 1º e parar de novo: cole antes do bloco da Central o “pré-prompt do Lucas” (abaixo) e mande de novo só os que faltaram.',
        'Se o agente disser que não dá para usar a imagem como quadro inicial e final com fala: gere à mão: Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; '
        f'Início = {c["img"]}; Fim = vazio; no prompt, só o texto do prompt daquele take.',
        'Pré-prompt do Lucas (só se precisar): ' + PRE_LUCAS,
    ]
    return {
        'imagem': c['img'],
        'intro': 'Anexe a imagem, cole o aviso e, embaixo dele, o bloco “COPIAR TUDO JUNTO” da Central (são 2 colagens: 2 mensagens).',
        'aviso_tag': 'cole antes do bloco da Central (nas 2 mensagens)',
        'aviso': ('Vou te enviar vários prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um com o '
                  'devido número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.'),
        'passos': passos,
    }


# ------------------------------------------------------------------ o hook: imagens (edição da Nora aprovada + a folha) e clipes de 5 s com PROMPT CURTO
_BASE = ('the first image is the approved photo of the woman (keep exactly her face, her long black wavy hair, the thin braid with small gold rings, the small flat '
         'gold crescent moon with three tiny gold five-pointed stars on her cheek, her star-and-moon earrings, her gold Venus necklace, the thin gold bracelets and the '
         'gold sun ring); the second image is her character sheet (same woman, same face). Same woman and same face: change her clothes to ')
_FIM = ('looks exactly like a real casual iPhone photo, slight phone grain, natural colors, everything in focus, no bokeh; no glow, no sparkle, no light effect; '
        'no phone, phone stand or tripod anywhere in the image; no text and no logo anywhere; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16')
POTE = 'a large clear glass swing-top jar with a metal clasp, full of ground cinnamon'


def imgs(c):
    b = _BASE + c['roupa_cont']
    if c['tag'] == 'carro':
        rua = (', black wide-leg pants and white sneakers; change the place and the light: a sunny afternoon in the paved driveway of an American suburban house, '
               'with green lawns and houses behind; a dark gray pickup truck is parked there. ')
        return [
            ('A', 'agachada na porta de trás da picape aberta, com o pote de canela (plano aberto)',
             b + rua + 'RAW photo taken from about two meters away at her chest height: she crouches down next to the open rear door of the dark gray pickup truck, '
             f'framed full body, holding {POTE} against her chest with one hand, and with her other hand lifting the corner of the black rubber floor mat on the floor '
             'behind the front seat; she looks down at the floor of the truck with a calm, focused expression; ' + _FIM),
            ('B', 'de perto: os dedos jogando canela no carpete, embaixo do tapete levantado',
             b + rua + "close-up RAW photo from slightly above of the floor behind the truck's front seat, filling the whole image: the corner of the black rubber floor mat "
             'is folded back, showing the dark gray carpet; her hand with the thin gold bracelets and the gold sun ring pinches ground cinnamon from the open glass jar '
             'held in her other hand and sprinkles it onto the carpet, a little brown cinnamon already on the carpet; part of her black cardigan sleeve is visible; '
             'if a third image is attached, use it ONLY as a reference for the framing and the action of this close-up (the hand, the carpet, the jar), never for any person; ' + _FIM),
            ('D', 'pela porta do motorista aberta, ela subindo no banco do motorista',
             b + rua + "RAW photo taken from outside the truck, about one and a half meters away through the open driver's door, at chest height: she steps up into the "
             "driver's seat, one hand on the steering wheel and the other on the door frame, the glass jar no longer in her hands, a calm expression; " + _FIM),
            ('C', 'sentada no banco do motorista, de cinto, apontando para a lente (é a imagem das falas)',
             b + '; change the place and the light: she sits in the driver\'s seat of the same dark gray pickup truck with the seatbelt across her chest, driving slowly down a quiet '
             'American suburban street on a sunny afternoon, soft natural daylight through the windows; through the side and rear windows, houses, lawns and trees. '
             'RAW photo taken by a phone mounted on the dashboard about 60 centimeters in front of her, at face height, slightly to the side like a real car selfie: '
             'framed from the chest up, her face in the upper middle of the image, looking straight into the camera with a serious, knowing look and her lips '
             'closed; one hand holds the steering wheel, partly visible at the bottom of the image; her other hand is raised in front of her chest, pointing her index '
             'finger straight at the lens; the upper 15 percent of the image is the plain light-gray car ceiling with nothing in it; ' + _FIM),
        ]
    corredor = ('; change the place and the light: an upstairs hallway of an American home with white walls, white doors and a white ceiling, soft warm indoor '
                'evening light; an aluminum stepladder stands in the hallway right under a white square attic hatch in the ceiling. ')
    return [
        ('A', 'em cima da escada, as mãos empurrando o alçapão do teto (plano aberto)',
         b + corredor + 'RAW photo taken from about two meters away at her chest height, slightly from below: she stands on the third step of the aluminum stepladder, '
         'framed from the knees up, her side to the camera, both hands raised pushing the closed white attic hatch in the ceiling just above her head, looking up; '
         + _FIM),
        ('B', 'de perto: a estátua de São Miguel empoeirada nas mãos dela, perto da lente',
         b + corredor + f'close-up RAW photo taken from about 50 centimeters in front of her at chest height: standing on the stepladder, she holds {ESTATUA} in both '
         'hands right in front of the camera, filling the lower two thirds of the image, her face just behind it, her lips pursed as if about to blow the dust off; '
         'the open dark attic hatch is above her; ' + _FIM),
        ('C', 'de frente na escada, a estátua no alto da escada ao lado, apontando para a lente (é a imagem das falas)',
         b + corredor + 'RAW photo taken from about one meter in front of her at chest height: she stands on the stepladder framed from the waist up, her face in the '
         f'upper middle of the image, looking straight into the camera with a serious, knowing look and her lips closed; {ESTATUA} stands on the flat top cap of the '
         'ladder right beside her, on the side of the image, fully visible and never covering her face; one hand rests on the top rail of the ladder; her other hand '
         'is raised in front of her chest, pointing her index finger straight at the lens; the open dark attic hatch is in the ceiling above her; the upper 15 percent '
         'of the image is the plain white ceiling; ' + _FIM),
    ]


SOM_FORA = 'Ambient outdoor ASMR sound only, no speech and no music.'
SOM_CARRO = 'Ambient car ASMR sound only, no speech and no music.'
SOM_CASA = 'Ambient indoor ASMR sound only, no speech and no music.'


def vids(c):
    if c['tag'] == 'carro':
        return [
            ('1-pote', 'A', 'ela abre o fecho do pote e levanta o tapete do carro',
             'She opens the metal clasp of the glass jar of cinnamon and lifts the corner of the floor mat inside the truck. ' + SOM_FORA),
            ('2-canela', 'B', 'ela joga a canela no carpete, baixa o tapete e dá batidinhas',
             'She sprinkles the cinnamon onto the carpet, lays the rubber floor mat back over it and pats it flat with her hand. ' + SOM_CARRO),
            ('3-entra', 'D', 'ela senta no banco do motorista e puxa o cinto',
             "She sits down in the driver's seat, closes the door and pulls the seatbelt across her chest. " + SOM_CARRO),
        ]
    return [
        ('1-alcapao', 'A', 'ela abre o alçapão, põe a mão lá dentro e tira a estátua',
         'She pushes the attic hatch open, reaches into the dark attic and pulls out a dusty statue of Saint Michael, bringing it down to her chest. ' + SOM_CASA),
        ('2-sopra', 'B', 'ela sopra a poeira da estátua na direção da lente',
         'She blows the dust off the statue toward the camera and a soft cloud of real grey dust puffs into the lens. ' + SOM_CASA),
    ]


def hook(c):
    base = f'{c["d"]}-PRE-{c["tag"]}'
    anexos = '1º a d1511-PRE-sal-IMG-C (a Nora já aprovada); 2º a folha da Nora (1K)'
    etapas = []
    for letra, desc, prompt in imgs(c):
        usa = ', '.join(v[0] for v in vids(c) if v[1] == letra) + (' e TODOS os takes (T01 a T17)' if letra == 'C' else '')
        nora = 'é a Nora (o rosto, a lua com as 3 estrelinhas, a trança com anéis, o colar de Vênus); '
        roupa = 'a blusa cinza com o cardigã preto; ' if c['tag'] == 'carro' else 'a blusa creme com a saia bege; '
        if c['tag'] == 'carro':
            conf = {'A': nora + roupa + 'o pote de vidro com a canela; a picape cinza-escura com a porta de trás aberta',
                    'B': 'a mão com as pulseiras e o anel de sol; o pote de vidro aberto; o tapete levantado e a canela no carpete',
                    'D': nora + roupa + 'ela subindo no banco do motorista, sem o pote na mão',
                    'C': nora + roupa + 'no banco do motorista, de cinto, uma mão no volante e a outra apontando para a lente; a rua e as casas nas janelas'}[letra]
        else:
            conf = {'A': nora + roupa + 'na escada de alumínio, as mãos no alçapão fechado do teto',
                    'B': nora + 'a estátua de São Miguel inteira (as asas, a espada, a capa vermelha), sem deformar, com poeira',
                    'C': nora + roupa + 'na escada, a estátua inteira no alto da escada ao lado dela, uma mão no corrimão e a outra apontando para a lente'}[letra]
        conf += '; 5 dedos em cada mão; nenhum celular, tripé ou texto.'
        usa = usa if usa.strip(', ') and not usa.startswith(' e') else 'TODOS os takes (T01 a T17)'
        an = anexos + ('; 3º (opcional) a claire-ref-canela-carpete-sem-rosto.jpg que eu te mandei, só para o enquadramento' if (c['tag'] == 'carro' and letra == 'B') else '')
        etapas.append({'titulo': f'Imagem {letra}: {desc}', 'nome': f'{base}-IMG-{letra}', 'tipo': 'img', 'anexar': an,
                       'quadros': (f'x4, 0 crédito. Serve para: {usa}. Escolha a que tiver: {conf} Renomeie para {base}-IMG-{letra}.'
                                   + (' ME MANDE AS 4 DA IMAGEM C antes dos takes (é a imagem das falas).' if letra == 'C' else '')),
                       'prompt': prompt})
    for suf, letra, desc, prompt in vids(c):
        n = f'{base}-{suf}'
        etapas.append({'titulo': f'Vídeo {suf.split("-")[0]}: {desc}', 'nome': n, 'tipo': 'vid', 'duracao': 5,
                       'quadros': (f'PROMPT CURTO (aula 54). Omni 1.2 Flash · 360p · 5 s · x2 (~10 créditos). Início = {base}-IMG-{letra}; Fim = vazio. '
                                   f'Baixe os 2 em 720p e renomeie {n}-a e {n}-b.'),
                       'prompt': prompt})
    if c['tag'] == 'carro':
        conceito = ('O hook do v2 da claire_mayaus, igual: ~6,7 s em 6 tomadas de ~1 s, sem fala: agachada na porta da picape com o pote → close abrindo o pote → '
                    'aberto → close jogando a canela no carpete e ajeitando o tapete → entrando no carro → sentada → FLASH BRANCO → ela fala no banco do motorista, '
                    'com o carro andando. Texto só no hook: “When the money arrives Don’t tell anyone what you’ve done 😏” (branco, sem caixa).')
    else:
        conceito = ('O hook do v6 da claire_mayaus, igual: ~6,6 s em 2 tomadas, sem fala: na escada, abre o alçapão e tira a estátua de São Miguel (uma tomada de ~4,7 s) → '
                    'close soprando a poeira na lente (~1,9 s) → FLASH BRANCO → ela fala na escada, com a estátua no alto da escada ao lado. Sem texto no hook.')
    conceito += ' Eu corto e junto as tomadas, ponho o flash e emendo com a fala. As imagens são edição da Nora aprovada + a folha (0 crédito).'
    return {
        'titulo_secao': 'Hook (Flow, à mão, antes dos takes)',
        'conceito': conceito,
        'modo': ('Imagens: Flow → Imagem · 9:16 · Nano Banana Pro · x4, anexando as referências na ordem (0 crédito). Vídeos: Flow → Vídeo → Frames → 9:16 → Omni 1.2 Flash → '
                 '360p → 5 s → x2; Início = a imagem indicada; Fim = vazio. Baixe em 720p e me mande todos, sem cortar.'),
        'etapas': etapas,
    }


# ------------------------------------------------------------------ montar os painéis
LEG = {'nora69': 'Keep your mouth shut if this video found you today 🤫', 'nora70': 'Keep your mouth shut if this found you tonight 🤫'}
HASH = '#manifestation #lawofattraction #1111 #messagefromtheuniverse #2027'
QUANDO = {'nora69': '17/11, Face às 19h30 e Insta quando a proxy voltar (~19h45 a 20h)', 'nora70': '17/11, Insta e Face à 0h00 (de 17 para 18/11)'}
COMENT_FACE = {'nora69': ['🙏 Your reading is in the Page comment ✨', '💛 The link to your reading is in the Page comment', '✨ It\'s waiting for you in the comments above'],
               'nora70': ['🙏 Your reading is in the Page comment', '💫 The link to your reading is pinned in the comments', '🌙 It\'s right there in the Page comment ✨']}


def montar(c):
    nn = c['nn']; idx = list(range(N))
    perfil = copy.deepcopy(P46['perfil']); perfil.pop('teste', None)
    resp = copy.deepcopy(P66['respostas_face']); resp['comentario'] = COMENT_FACE[nn]
    resp['insta'] = ['(Hoje não: até ~01h06 de 18/11, nada de responder, curtir ou fixar no Insta; as 24 h depois da verificação.)']
    titulo = ('o modelo da claire_mayaus (v2): o hook da canela no carro, a fala no carro andando' if c['tag'] == 'carro'
              else 'o modelo da claire_mayaus (v6): o hook do alçapão com a estátua, a fala na escada')
    p = {
        'enxuto': True, 'imagens_titulo': f'Imagem das falas (a {c["img"]}, gerada no hook)',
        'perfil': perfil, 'trava_referencia': P46['trava_referencia'], 'figurino': c['roupa_cont'], 'excecao_estilo': '',
        'ocultar_bloco_agente_imagem': True,
        'roteiro': {'id': f'{nn}-{c["tag"].upper()}-1711', 'titulo': f'{nn} · {QUANDO[nn]} · {titulo}', 'duracao_total': 110,
                    'descricao_instagram': f'{LEG[nn]}\nYour reading is waiting in my story 🔮\nComment "I believe" 🙏\n{HASH}',
                    'descricao_face': f'{LEG[nn]}\nYour reading is waiting in my story and in the comments 🔮\n{HASH}'},
        'refs': ['d1511-PRE-sal-IMG-C + a folha da Nora nas imagens do hook', f'{c["img"]} em todos os takes'],
        'imagens': [{'rotulo': f'IMAGEM 1 · {c["img"]}', 'cena': '(gerada no hook, a imagem C)', 'anexar': 'nada aqui (ela sai no hook)'}],
        'videos': [{'rotulo': f'T{i + 1:02d}', 'cena': TXT[i], 'duracao': '10', 'primeiro_quadro': f'IMAGEM 1 ({c["img"]})', 'acao': '', 'b_roll': '',
                    'fala': fala(c, i), 'movimentacao': mov(c, i), 'arquivo': nome(c, i)} for i in idx],
        'texto_tela': {'hook': ('When the money arrives\nDon’t tell anyone what you’ve done 😏' if c['tag'] == 'carro' else '(sem texto no hook, igual ao v6 dela)'),
                       'hook_comeca': 'o primeiro quadro do hook', 'hook_termina': 'o flash branco', 'hook_alt': '', 'extras': []},
        'comentario_fixado': {'insta': '(Hoje não fixe nada no Insta: até ~01h06 de 18/11, as 24 h depois da verificação.)',
                              'face': f'Your reading is waiting for you here 🙏 👉 {FB}'},
        'respostas_face': resp,
        'story': {'ja_postado': True, 'nota': ('Antes de postar, confira se o story está no ar no Insta e no Face (o vídeo manda para o story). Se não estiver, reposte o '
                                                'story-1211 (o mesmo arquivo), ao vivo, nos dois.')},
    }
    mt = copy.deepcopy(P49['mapa_tela'])
    mt.update({'numeros': ([dict(t='222', x=82, y=16, onde='alto à direita, dos ~15 s até o fim (no hook e nos primeiros ~8 s da fala, nenhum)', cor_nome='branco', cor='#FFFFFF', tamanho=11)]
                      if c['tag'] == 'carro' else
                      [dict(t='222', x=18, y=16, onde='alto à esquerda, só no hook; some quando a fala começa', cor_nome='branco', cor='#FFFFFF', tamanho=11),
                       dict(t='222', x=82, y=16, onde='alto à direita, dos ~43 s até o fim', cor_nome='branco', cor='#FFFFFF', tamanho=11)]),
          'estilos': [{'nome': 'Legenda (eu ponho, P45)', 'fonte': 'sem serifa, peso normal (como a automática do Instagram)', 'cor': 'branca, minúsculas, sem pontuação',
                       'tamanho': 'a frase inteira, 2 a 3 linhas', 'contorno': 'preto fino', 'obs': 'Sem destaque de cor. Entra quando ela começa a falar.'},
                      {'nome': 'Seta', 'fonte': '—', 'cor': 'vermelha, fina', 'tamanho': 'pequena, canto de baixo à esquerda', 'contorno': '—',
                       'obs': 'Do “Tap my profile picture” até o fim. Sem faixa de CTA.'}],
          'regras': ['Visual limpo, igual ao da claire_mayaus: sem caixa do topo, sem faixa, sem imagem do desejo, sem bandeira.',
                     'Flash branco de ~0,3 s entre o hook e a fala.', 'Eu ponho a legenda, o número, a seta e o flash (P45); você monta só o vídeo e a música.']})
    p['mapa_tela'] = mt
    corte = f'{nn}-cortado'
    p['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” só os {N} takes (T01 a T17), de uma vez. O hook não entra: ele vem para mim. HOJE, MUDE 1 CAMPO: “Zoom nos cortes” = DESLIGADO (sem zoom), porque o vídeo dela não tem zoom nos cortes; o resto como abaixo.',
        'nome': corte, 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pela ordem do nome (T01 a T17)',
        'depois': [f'Suba os {N} takes e espere a Prévia.', 'Aperte play com Resultado marcado: confira a primeira palavra do T01 e a última do T17.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', f'Clique em Cortar e baixar e salve como {corte}.']}
    p['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {corte}', 'como': 'É o vídeo que saiu da FusionZ. Começa direto no T01.'},
        {'quando': 'B. O hook: NÃO põe no CapCut',
         'texto': f'Os vídeos do hook ({c["d"]}-PRE-{c["tag"]}-…, -a e -b): mande para mim junto com o montado',
         'como': 'Eu corto as tomadas, monto o hook (~6,7 s), ponho o flash branco e emendo antes do T01.'},
        {'quando': '1. Do T01 ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Começa no 1º quadro do montado.'},
        {'quando': '2. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'1080×1920, nome {nn}-montado (acima de 30 MB, link do Drive). Eu devolvo o {nn}-final (Insta, completo) e o {nn}-final-FACE (espelhado, com a variação do Face e SEM o T10, o T11 e o T12, os selos e o comment I believe: Clone R67, segurança da Página).'}]
    cr_hook = 10 * len(vids(c))
    pecas = [{'nome': f'{c["d"]}-PRE-{c["tag"]}-IMG-' + ('A, B, D e C' if c['tag'] == 'carro' else 'A, B e C'), 'tipo': 'imagens (hook; a C é a das falas)', 'status': 'gerar',
              'descricao': 'Edição da d1511-PRE-sal-IMG-C + a folha. x4 cada, 0 crédito.'},
             {'nome': f'{c["d"]}-PRE-{c["tag"]}-1 a {len(vids(c))}', 'tipo': 'hook (prompt curto)', 'status': 'gerar', 'creditos': cr_hook,
              'descricao': f'{len(vids(c))} vídeos de 5 s, uma ação em cada, x2.'}]
    pecas += [{'nome': nome(c, i), 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{fala(c, i)}”'} for i in idx]
    if c['tag'] == 'carro':
        postar = ('Face às 19h30, ao vivo (o nora69-final-FACE). Insta só depois que a proxy voltar (19h42): confira o IP 168.235.144.192 e os EUA no mylocation.org, '
                  'abra o Insta e poste o nora69-final, ao vivo (~19h45 a 20h). ')
    else:
        postar = 'À 0h00 (de 17 para 18/11), ao vivo: Insta (o nora70-final, 4 h depois do nora69) e Face (o nora70-final-FACE). '
    p['pecas'] = {'titulo_decisao': 'Resumo', 'lista': pecas, 'decisao': [
        f'GERAR (~{170 + cr_hook} créditos, na conta que você escolher): as imagens do hook (0 crédito) e ME MANDE AS 4 OPÇÕES DA IMAGEM C; depois os vídeos do hook (~{cr_hook}) '
        'e os 17 takes na imagem C pelo agente, em 2 mensagens (~170).',
        'Igual ao vídeo da claire_mayaus: a mesma fala (só a data de hoje e sem o “free”, porque a leitura é paga), o mesmo hook e o visual limpo. '
        'O par de hoje testa o hook: a canela no carro (19h30) contra o alçapão (0h00). Medida: os 3 s, a curva aos 10 s, as visitas ao perfil e os cliques no Tracker.',
        postar + 'No Face, logo depois, o comentário da Página com o link, tirando a prévia e fixando pelo celular. No Insta, até ~01h06 de 18/11, nada de responder, curtir ou fixar.']}
    p['central'] = {'imagem_unica': True,
                    'conferir': ('Conferir em cada take: é a Nora da imagem C (rosto, lua com as 3 estrelinhas, trança, brincos, colar de Vênus); '
                                 + ('no banco do motorista, com o cinto e a mão no volante, a rua passando nas janelas; ' if c['tag'] == 'carro'
                                    else 'na escada, a estátua parada no alto da escada e a mão no corrimão; ')
                                 + 'ela fala uma vez só, em inglês, com as datas e os números por extenso. Renomeie com o nome da lista.'),
                    'passos': [], 'config': config(c), 'agente': agente(c),
                    'colagens': [{'titulo': f'{nn}: colagem {li + 1} (T{lote[0] + 1:02d} a T{lote[-1] + 1:02d})', 'fala': ' '.join(fala(c, i) for i in lote),
                                  'movimentacao': [mov(c, i) for i in lote], 'takes': lote} for li, lote in enumerate(LOTES)]}
    p['pre_gancho'] = hook(c)
    p['ordem'] = ['pecas', 'prehook', 'imagens', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', f'<title>Painel {nn} · dia 17/11</title>', html, count=1)
    (R / f'PAINEL-{nn.upper()}.html').write_text(html, encoding='utf-8')
    print('ok', nn, N, 'takes', 'créditos ~', 170 + cr_hook, [len(fala(c, i).split()) for i in idx])


montar(CARRO)
montar(ALCAPAO)
