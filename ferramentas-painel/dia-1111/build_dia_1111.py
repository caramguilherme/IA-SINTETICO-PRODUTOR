# Painéis do dia 11/11/2026 (nora55 a nora60): 6 posts (9h, 12h, 15h, 18h, 21h, 00h), Insta e Face, em 2 cenas novas (decisão do aluno, 11/11 ~00h30):
# manhã = escritório em casa com luz de janela, regata preta de gola quadrada + moletom cinza largo aberto (9h, 12h, 15h);
# noite = sala com abajur, regata preta de gola quadrada (18h, 21h, 00h). Falas: ROTEIRO-DIA-1111-NORA55-60.md.
# Teste a 0 crédito na edição (decisão do aluno, 11/11 ~01h35): prova do Trustpilot antes do CTA em 12h, 18h e 00h; sem prova em 9h, 15h e 21h;
# visual atual (caixa branca + números coloridos) em todos; o teste do visual limpo foi para 12/11.
# O LIVRE e as movimentações são PROVISÓRIOS até a imagem de cada cena ser aprovada (P32): fechar pela imagem e rodar de novo.
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-1111/build_dia_1111.py
import json, copy, re, pathlib

R = pathlib.Path(__file__).resolve().parents[2]
MODELO = (R / 'PAINEL-MODELO.html').read_text(encoding='utf-8')
assert MODELO.count('const PACOTE = null;') == 1


def pacote(nome):
    p = R / nome if (R / nome).exists() else R / 'arquivo' / 'paineis' / nome  # os painéis postados foram para o arquivo em 11/11
    t = p.read_text(encoding='utf-8')
    i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
    return json.loads(t[i:j])


P46 = pacote('PAINEL-NORA46.html')
P49 = pacote('PAINEL-NORA49.html')
P51 = pacote('PAINEL-NORA51.html')
CFG = copy.deepcopy(P51['central']['config'])  # a configuração do kit (mesma voz, mesma Central)
VOZ = [c for s in CFG for c in s['campos'] if c['campo'].startswith('Perfil de voz')][0]['copiar']
STORYIG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'

# ------------------------------------------------------------------ falas (as mesmas nas 2 cenas; cada cena gera as suas)
F = {
    'A': "If you see this on Wednesday, November 11th, this message is one hundred percent meant for you.",
    'B': "If you see this on Wednesday, November 11th, look at the time: if it's before 11:11 p.m., this is meant for you.",
    'C': "If you're holding your phone on Wednesday, November 11th, wondering if things will ever change, this message is meant for you.",
    'P': "Today the 11:11 portal is open, and the next chapter of your life begins with it, in the best way possible.",
    'K': "The rest of this message is in my story: tap my photo, three quick questions, and your private reading is ready.",
}
SUF = {'A': 'T01a-se-voce-ve', 'B': 'T01b-relogio', 'C': 'T01c-celular-na-mao', 'P': 'T02-hoje-o-portal', 'K': 'T04-cta-reading'}
ROT = {'A': 'T01a', 'B': 'T01b', 'C': 'T01c', 'P': 'T02', 'K': 'T04'}
CENA_TXT = {'A': 'a data de quarta, "if you see this on" (a frase dos maiores da Soma)', 'B': 'a data de quarta + o filtro do relógio (o do nora54)',
            'C': 'a data de quarta + a situação (celular na mão, esperando a vida mudar; lote 2, v12)', 'P': 'a promessa: hoje é o portal',
            'K': 'CTA: o resto da mensagem, a ação e a leitura'}
CAIXA = {'A': ('WEDNESDAY, NOVEMBER 11TH\nif you keep seeing 11:11,\nthis message is for you', 'one hundred percent meant for you.'),
         'B': ('WEDNESDAY, NOVEMBER 11TH\ntoday is 11:11,\nthis message is for you', 'this is meant for you.'),
         'C': ('WEDNESDAY, NOVEMBER 11TH\nif you keep seeing 11:11,\nthis is your sign', 'this message is meant for you.')}

GESTO = {
    'A': 'during the first half of the take she tilts her head slightly with a curious look, in the closing half a warm, certain smile appears and she gives one small nod',
    'B': 'during the first half of the take she leans slightly toward the lens with a bright, curious look, in the middle her eyes glance briefly down and to the left side of the frame as if checking a clock while her hand stays still, and in the closing half her eyes return to the lens and she gives one slow nod with a warm smile',
    'C': 'during the first half of the take she holds a soft, understanding look with her head tilted slightly, in the closing half she gives one slow nod with a warm, reassuring smile',
    'P': 'during the first half of the take her eyebrows lift with a joyful look, in the closing half she lifts her right hand to the height of her shoulder with the palm up and then returns it to {volta} with a warm smile',
}

CENAS = {
    'manha': dict(
        img='manha1111-IMG', pre='manha1111', nome='cena da manhã', primeiro=55,
        roupa_pt='regata preta de gola quadrada + moletom cinza largo, aberto, por cima',
        roupa='plain black square-neck cotton tank top worn under a loose, open heather-grey zip-up hoodie, both matte, no print, no logo',
        roupa_cont='her plain black square-neck tank top and the loose, open heather-grey zip-up hoodie over it',
        repouso='lightly holds the edge of the open hoodie at collarbone height', volta='the edge of the hoodie at collarbone height',
        quando='in the morning', onde='a real, lived-in American home office', luz='lit only by soft daylight from a window on the right side of the frame',
        fundo='the plain light wall, the office chair behind her, the shelf and the window light',
        visual_t04='soft morning daylight from a window in the background',
        cena_img=('real lived-in American home office in the morning, a plain light warm-grey wall behind her, the top of a simple office chair behind her shoulders, '
                  'a small green plant and a few books on a shelf at the edge of the frame'),
        hora_img='soft natural morning daylight from a window on the right side of the image',
        luz_img='only soft daylight from a window on the right side of the image, a little uneven, like a real phone photo in the morning; no studio light, no ring light',
        mao_img='her right hand, on the left side of the image, lightly holds the edge of the open hoodie at the height of her collarbone, with exactly five fingers',
        bagunca='a mug on the edge of the desk, a few books, ordinary home clutter, any signage or packaging unbranded and unreadable',
        cam='f/8 aperture, ISO 400, 1/100s shutter speed'),
    'noite': dict(
        img='noite1111-IMG', pre='noite1111', nome='cena da noite', primeiro=58,
        roupa_pt='regata preta de gola quadrada, alças largas',
        roupa='plain black square-neck cotton tank top with wide straps, matte, no print, no logo',
        roupa_cont='her plain black square-neck tank top with wide straps',
        repouso='rests at collarbone height with her fingertips lightly touching the small gold Venus pendant',
        volta='the small gold Venus pendant at collarbone height',
        quando='at night', onde='a real, lived-in American living room', luz='lit only by a warm table lamp on the right side of the frame',
        fundo='the plain warm-grey wall, the sofa behind her and the lamp',
        visual_t04='warm table lamp light in the background',
        cena_img=('real lived-in American living room at night, a plain warm-grey wall behind her, the corner of a beige sofa with a throw blanket behind her shoulders, '
                  'a small table lamp at the edge of the frame'),
        hora_img='warm tungsten lamp light with soft low-key shadows',
        luz_img='only a warm table lamp on the right side of the image, a little uneven, like a real phone video at night; no studio light, no ring light',
        mao_img=('her right hand, on the left side of the image, rests at the height of her collarbone with her fingertips lightly touching the small gold Venus pendant, '
                 'with exactly five fingers'),
        bagunca='a throw blanket on the sofa, a few books on a side table, ordinary home clutter, any signage or packaging unbranded and unreadable',
        cam='f/8 aperture, ISO 800, 1/60s shutter speed'),
}


def nome(c, k):
    return f"{CENAS[c]['pre']}-{SUF[k]}"


def dur(k):
    return '8' if len(F[k].split()) <= 17 else '10'


def creditos(ks):
    return sum(12 if dur(k) == '8' else 15 for k in ks)


def base_mov(c, d, g):
    s = CENAS[c]
    return (f'Throughout the whole {d} seconds she keeps an unchanged handheld selfie framing, her left arm on the right side of the frame stays extended toward the camera '
            f'holding the phone out of frame and never moves, her right hand on the left side of the frame {s["repouso"]} except during the one small '
            'gesture described here, which always happens at the height of her shoulder on the left side of the frame and never in front of her face or mouth, and her eyes '
            f'stay on the lens, {g}, and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; the camera keeps only a tiny '
            'natural handheld sway with no zoom and no cuts, the braid stays on the right side of the frame, everything else in the room stays still and each hand has exactly five fingers.')


def mov_k(c):  # o CTA sem gesto de mão (lição do T04 de 10/11: mão descendo = filtro do Flow)
    s = CENAS[c]
    return ('Throughout the whole 10 seconds she keeps an unchanged handheld selfie framing; her left arm on the right side of the frame stays extended toward the camera '
            f'holding the phone out of frame and never moves; her right hand on the left side of the frame stays still and {s["repouso"]} for '
            'the whole clip and never moves down; her eyes stay on the lens; during the first half of the take she holds a warm, confident look, and in the closing half she gives one '
            'small encouraging nod with a warm smile; from the end of the final sentence until the clip ends she keeps her lips closed and silent; the camera keeps only a tiny natural '
            'handheld sway with no zoom and no cuts, the braid stays on the right side of the frame, everything else in the room stays still and each hand has exactly five fingers.')


def mov(c, k):
    if k == 'K':
        return mov_k(c)
    return base_mov(c, 8 if dur(k) == '8' else 10, GESTO[k].format(volta=CENAS[c]['volta']))


COMUNS = {('of', 'the'), ('and', 'the'), ('to', 'the'), ('in', 'the'), ('on', 'the'), ('at', 'the'), ('for', 'a'), ('of', 'her'), ('and', 'her'),
          ('as', 'if'), ('the', 'lens'), ('her', 'left'), ('and', 'then'), ('the', 'hand'), ('she', 'gives'), ('the', 'height')}
for c in CENAS:
    for k, f in F.items():
        assert len(f.split()) <= 22, (k, len(f.split()))
        fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(c, k).lower())
        sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS
        assert not sobra, (c, k, sobra)


def livre(c):
    s = CENAS[c]
    return (f'Casual handheld iPhone front-camera selfie video {s["quando"]} in {s["onde"]}, looking exactly like a real phone video, {s["luz"]}. '
            'CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, the thin braid wrapped with small gold rings hanging down on the right side of the frame, '
            'the small flat gold crescent moon with three tiny gold stars on her cheek on the left side of the frame, her star-and-moon drop earrings, her thin gold Venus necklace, '
            f'the thin gold bracelets on her right wrist, the gold sun ring on her right hand and {s["roupa_cont"]} stay exactly as in the reference image; the framing is exactly '
            'the one of the reference image, a close selfie with her face large and centered and her eyes at about one third of the frame height; her left arm on the right side '
            'of the frame stays extended toward the camera holding the phone out of frame, running off the bottom-right corner, and never moves; her right hand on the left side of '
            f'the frame {s["repouso"]} and only lifts for the one small gesture of a take, at the height of her shoulder on the left side of the frame, never in front of her face '
            f'or mouth; {s["fundo"]} stay exactly where they are; natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter, no glow and '
            'no sparkles; the camera has only a tiny natural handheld sway, no zoom, no cuts and no reframing; no phone, object, person, animal or text appears or disappears; '
            'each hand always has exactly five fingers; no on-screen text, no captions, no logos; real quiet room ambient sound only, no music. SPEECH RULE for every take: she '
            "says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added sentence before, between or "
            'after; numbers are spoken as words (11:11 as "eleven eleven", 11:11 p.m. as "eleven eleven p.m.", November 11th as "November eleventh"); when she finishes the last '
            'word she closes her lips, stays silent and keeps a calm still expression until the clip ends.')


def prompt_img(c):
    s = CENAS[c]
    return ('RAW photo of the exact same character from the attached reference image, preserving every facial feature, identity, age, ethnicity, skin tone, and hairstyle exactly as shown in the reference,\n'
            'peaceful soft smile,\n'
            f'{s["roupa"]}, small flat shiny gold crescent moon with three tiny gold stars on the outer edge of her cheekbone near the temple, on the left side of the image; long gold '
            'star-and-moon drop earrings; thin gold necklace with a small Venus pendant; thin gold bracelets; gold sun ring; hazel-green eyes; one thin braid with small gold rings '
            'on the right side of the image; clean forehead with no jewelry,\n'
            "selfie taken with her own phone at arm's length: her left arm, on the right side of the image, is raised toward the camera and is cut off by the bottom-right corner "
            'of the frame, and the phone itself is not visible; framed from the upper waist up, her face large and centered with her eyes at about 30 percent of the image height; '
            f'{s["mao_img"]}; she looks straight into the phone camera with her lips slightly parted, as if about to speak; no prop, no object in her hands or anywhere in the frame,\n'
            f'{s["cena_img"]},\n'
            f'{s["hora_img"]},\n'
            f'{s["luz_img"]},\n'
            'natural matte skin finish with visible pores and fine skin texture, subtle natural micro-imperfections, faint under-eye texture, natural variation in tone between face, '
            'neck and hands, delicate peach fuzz, no oily or wet shine and no specular hotspots on the forehead, nose or cheeks, at most a faint soft sheen on the nose bridge, no '
            'smoothing, skin tone, age and features exactly as in the reference image,\n'
            'hair exactly as in the reference image, with a few fine flyaway strands at the hairline and no floating strands, believable fabric weight and natural creases, all '
            'clothing unbranded, anatomically correct hands with five natural fingers each, nothing duplicated or floating, lifelike anatomy and proportions with natural facial '
            'asymmetry, caught in a natural moment rather than posed, slight asymmetry in the expression, eyes with natural moisture and small centred catchlights,\n'
            f'{s["bagunca"]},\n'
            'shot on a smartphone camera with iPhone 15 front camera selfie: looks exactly like a real casual photo taken with an iPhone, natural skin texture with visible pores, '
            f'slight phone grain, everything in focus, no bokeh, no filter, {s["cam"]}, natural depth of field, background stays readable,\n'
            'taken by herself as a handheld selfie, slightly imperfect framing with a subtle tilt, ordinary camera-roll depth of field, mild sensor noise in the shadows, restrained '
            'edge sharpening and modest JPEG softness, slightly abrupt highlight roll-off, warm or coloured light kept soft so the skin stays matte, camera at eye level, one coherent '
            'light direction with matching nose, jaw and eye-socket shadows, environment colour casts kept off the skin,\n'
            'no film emulation, straight smartphone frame, no date stamp, no text, no watermark, natural phone colors, no color grading, natural skin tone preserved separately from the colour grade,\n'
            'photorealistic, unretouched, candid documentary, UGC style, no studio lighting, no filters, no tattoos, no extra, fused or missing fingers, no duplicated or floating objects, no '
            'warped reflections or architecture, no readable text, logos, captions or watermarks, no oily, wet, waxy or plastic skin, no beauty retouching or airbrushing, no HDR look '
            'or over-sharpening, no exaggerated background blur, no fortune-teller costume,\n'
            'character consistency: identical face, same skin tone, same hair, same body proportions as the reference image — only wardrobe, environment, and pose change')


def img_central(c, n):
    s = CENAS[c]; outros = [n + 1, n + 2]
    return {
        'titulo': f'IMAGEM · {s["img"]} (a mesma para os takes do nora{n}, nora{outros[0]} e nora{outros[1]})',
        'nome': s['img'],
        'aviso': ('Não precisa do Gerador de Prompts: o prompt abaixo já está no formato dele, conferido (sem "fortune teller", sem "friend", sem objeto). '
                  f'Roupa: {s["roupa_pt"]}. O rosto e as marcas da Nora não mudam (Clone R19 e R21); sem tatuagem.'),
        'passos': [
            'No Flow (conta contatocaram): Imagem · 9:16 · Nano Banana Pro · x4. Anexe só a folha da Nora (a de 1K).',
            'Cole o prompt do botão Copiar abaixo, inteiro, e gere.',
            'Confira cada uma das 4: é a Nora (lua com 3 estrelinhas na bochecha do lado esquerdo da imagem, trança com anéis, brincos de estrela e lua, colar de Vênus, testa limpa)? '
            'A roupa é a pedida, lisa, sem marca? O celular não aparece? Parece foto de celular? Algum texto nos cantos? Mão com 5 dedos?',
            f'Me mande as 4 (print ou os arquivos). Eu escolho com você, fecho o LIVRE e as movimentações pela escolhida (P32) e republico este painel no mesmo link. '
            f'Renomeie a escolhida para {s["img"]}. Só gere os takes depois disso.',
        ],
        'grupos': [{'titulo': 'Prompt da imagem (cole no Flow)', 'nota': 'conferido em 11/11 ~00h40', 'campos': [
            {'campo': f'Prompt da {s["img"]}', 'valor': prompt_img(c), 'copiar': 1}]}],
    }


def prompt_k_manual(c):
    s = CENAS[c]
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image speaks directly '
            f'to her phone camera in a casual handheld selfie video at home {s["quando"]}.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + F['K'] + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            'VOICE PACING: medium pace (155 to 180 words per minute), about 8 seconds of speech; when she finishes the last word she closes her lips and stays silent '
            'with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + mov_k(c) + '\n\n'
            f'VISUAL: realistic casual iPhone front-camera selfie video, {s["visual_t04"]}, natural skin texture with visible pores, '
            'slight phone grain, everything in focus, no bokeh, no filter.\n\n'
            'CAMERA: handheld, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n'
            'AUDIO: only her voice and quiet room ambience; no music, no other voices, no sound effects.\n\n'
            'CONTINUITY: her face, long black wavy hair, the thin braid with small gold rings, the small gold crescent moon with three tiny gold stars on her cheek, '
            f'her star-and-moon earrings, her gold Venus necklace, her gold sun ring and bracelets, {s["roupa_cont"]} and the room behind her stay '
            'exactly as in the reference image; no phone, object, person or text appears; each hand has exactly five fingers; no on-screen text, captions or logos.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.')


def config(c):
    cf = copy.deepcopy(CFG)
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = f'colar o texto abaixo (PROVISÓRIO até a {CENAS[c]["img"]} ser aprovada; eu fecho pela imagem e republico)'
                campo['copiar'] = livre(c)
    return cf


PRE_LUCAS = ('Below, you will find several prompts, each corresponding to a different video. Please generate all the videos in sequential order, from the first prompt to the last.\n'
             'Maintain the exact same voice across all videos, ensuring EXACTLY THE SAME VOLUME, with no variations in background, intonation, or vocal clarity. Use the attached image as both the first and last frame of every generated video.\n'
             'Please submit ALL generation requests at once and in the correct order, so that all videos can be generated simultaneously.\n'
             'If the generation of any video fails, please resubmit ONLY the item that failed until it is successfully generated.')


def agente(c, ks):
    s = CENAS[c]; nomes = [nome(c, k) for k in ks]
    return {
        'imagem': s['img'],
        'aviso': (f'Vou te enviar {len(ks)} prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um com o devido '
                  'número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.'),
        'passos': [
            'Conta do Flow: contatocaram. Abra um PROJETO NOVO no Flow (se o agente parar, projeto novo, não pasta nova) e uma conversa nova no agente.',
            'Nas configurações do agente: Omni 1.1 Flash (o Flow abre no 1.2, que cobra o dobro), 9:16, 720p, gerar sem pedir aprovação.',
            f'Anexe só a {s["img"]}.',
            'Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.',
            'Renomeie cada take com o nome da lista: ' + ', '.join(nomes) + '. O agente costuma dar o número da ordem (1, 2, 3…): o 1 é o 1º nome da lista, o 2 é o 2º, e assim por diante. '
            'Se ele não renomear, mande na mesma conversa: “Now rename each video with the correct number from the prompt.”',
            'Confira na grade, pelo nome, se os 5 saíram. Se um falhar por política: mande na mesma conversa “Please generate video X from my previous message again, with the same prompt.” '
            '(X = o número dele na lista). Se falhar de novo, não insista: me mande o print.',
            f'Se o T04 (o 5º, o CTA) falhar 2 vezes: gere à mão: Vídeo → Frames → 9:16 → Omni 1.1 Flash → 720p → 10 s → x1; Início = {s["img"]}; Fim = vazio; cole o prompt abaixo, '
            f'inteiro, e gere (15 créditos). Renomeie para {nome(c, "K")}. PROMPT: ' + prompt_k_manual(c),
            'Se o agente parar no meio (por exemplo, “alta demanda”): responda na MESMA conversa, sem anexar nada: “Please continue and generate videos X to Y from my previous message, in the same order.” '
            '(troque X e Y pelos números que faltaram). Se ele gerar só o 1º e parar de novo: cole antes do bloco da Central o “pré-prompt do Lucas” (abaixo) e mande de novo só os que faltaram.',
            'Se o agente disser que não dá para usar a imagem como quadro inicial e final com fala: gere à mão: Vídeo → Frames → 9:16 → Omni 1.1 Flash → 720p → 10 s (ou 8 s, conforme a lista) → x1; '
            f'Início = {s["img"]}; Fim = vazio; no prompt, só o texto do prompt daquele take.',
            'Pré-prompt do Lucas (só se precisar): ' + PRE_LUCAS,
        ],
    }


COMUM_HASH = '#manifestation #1111portal #lawofattraction'
# prova: a avaliação real do Trustpilot (provas-trustpilot/, sem a hora relativa) que entra antes do CTA, ou None (o controle)
PROVA = {'05-karen': ('Karen W.', 'I just feel that for me there are good things about to happen'), '06-younger': ('Younger A. (EUA)', 'Everything she said is happening in my life'),
         '07-karina': ('Karina G. (EUA)', 'Wonderful, I feel so connected, this feels so real'),
         '04-katrina': ('Katrina H. (EUA)', 'So much peace here'), '03-darcey': ('Darcey (EUA)', 'very uplifting… she hit bullseye')}  # as 2 últimas são reserva
VIDEOS = {
    55: dict(cena='manha', hora='9h', prova=None, k1='A',
             insta=f'If you see this on Wednesday, November 11th, it\'s meant for you. 🔮\nToday the 11:11 portal is open. Your private reading is waiting in my story.\nComment "ready" ✨\n{COMUM_HASH} #newbeginnings',
             pergunta='today is 11:11: which part of your life is ready for a new beginning?',
             nums=[('11:11', 82, 10.5, 'alto à direita', 'verde-limão', '#7CFF4F', 16), ('222', 18, 10.5, 'alto à esquerda', 'branco', '#FFFFFF', 13), ('888', 82, 46.9, 'à direita, na altura do ombro', 'laranja', '#FF9F1C', 11)],
             coment=['☀️ Sent it to your messages, take a look ✨', '🔮 It\'s waiting in your inbox, beautiful 💖', '✨ Check your DMs, I just sent it 🌙'],
             dm=['☀️ [name], today is 11:11 ✨ Your private reading is right here:', '🔮 Hi [name]! As promised, here is your private reading 💖', '✨ [name], open this when you have a calm minute today 🌙 Your private reading:']),
    56: dict(cena='manha', hora='12h', prova='05-karen', k1='B',
             insta=f'If you see this on Wednesday, November 11th, look at the time. 🔮\nToday the 11:11 portal is open. Your private reading is waiting in my story.\nComment "open" ✨\n{COMUM_HASH} #1111',
             pergunta='what is the first thing you want to see change after today?',
             nums=[('11:11', 82, 10.5, 'alto à direita', 'amarelo-ouro', '#FFD21F', 15), ('888', 18, 10.5, 'alto à esquerda', 'rosa-choque', '#FF4FD8', 12), ('222', 82, 46.9, 'à direita, na altura do ombro', 'ciano', '#3DE0FF', 11)],
             coment=['💌 Just sent it, check your inbox ✨', '🌟 It\'s in your messages now 🔮', '💖 Sent! Take a look at your DMs ☀️'],
             dm=['💌 [name], here\'s your private reading for today ✨', '🌟 Hi [name]! Your private reading is ready 🔮 Tap here:', '💖 [name], I saved this one for you on 11:11 ☀️ Your private reading:']),
    57: dict(cena='manha', hora='15h', prova=None, k1='C',
             insta=f'Holding your phone on November 11th, wondering if things will ever change? This is for you. 🔮\nToday the 11:11 portal is open. Your private reading is waiting in my story.\nComment "I believe" ✨\n{COMUM_HASH} #universe',
             pergunta='what are you ready to let into your life on this 11:11?',
             nums=[('888', 18, 10.5, 'alto à esquerda', 'ciano', '#3DE0FF', 14), ('11:11', 82, 10.5, 'alto à direita', 'rosa-choque', '#FF4FD8', 15), ('222', 82, 46.9, 'à direita, na altura do ombro', 'amarelo-ouro', '#FFD21F', 11)],
             coment=['🌙 Look in your messages, it\'s there 💫', '✨ I sent it to your inbox 💖', '🔮 Check your DMs, beautiful ✨'],
             dm=['🌙 [name], this 11:11 is yours 💫 Your private reading:', '✨ Hey [name]! Here\'s the private reading I told you about 💖', '🔮 [name], three quick questions and it\'s ready ✨ Your private reading:']),
    58: dict(cena='noite', hora='18h', prova='06-younger', k1='A',
             insta=f'If you see this on Wednesday, November 11th, this message found you for a reason. 🔮\nThe 11:11 portal is open today. Your private reading is waiting in my story.\nComment "new chapter" ✨\n{COMUM_HASH} #spirituality',
             pergunta='love, peace, purpose or money: where do you want this new chapter to start?',
             nums=[('222', 18, 10.5, 'alto à esquerda', 'laranja', '#FF9F1C', 14), ('888', 82, 28, 'no meio à direita', 'verde-limão', '#7CFF4F', 12), ('11:11', 82, 46.9, 'à direita, na altura do ombro', 'branco', '#FFFFFF', 11)],
             coment=['🕯️ Sent it to your inbox ✨', '💫 It\'s waiting in your messages 🔮', '🌙 Check your DMs, I sent it 💖'],
             dm=['🕯️ [name], your private reading is here, on this 11:11 ✨', '💫 Hi [name]! Open your private reading here 🔮', '🌙 [name], this one is for your new chapter 💖 Your private reading:']),
    59: dict(cena='noite', hora='21h', prova=None, k1='B',
             insta=f'November 11th: look at the time. If it\'s before 11:11 p.m., this is meant for you. 🔮\nYour private reading is waiting in my story.\nComment "thank you" ✨\n{COMUM_HASH} #abundance',
             pergunta='what are you asking the universe for tonight?',
             nums=[('222', 18, 10.5, 'alto à esquerda', 'verde-limão', '#7CFF4F', 14), ('11:11', 82, 10.5, 'alto à direita', 'laranja', '#FF9F1C', 15), ('888', 82, 46.9, 'à direita, na altura do ombro', 'branco', '#FFFFFF', 11)],
             coment=['⭐ Take a look at your messages ✨', '💖 It\'s in your DMs now 🌙', '🔮 Just sent it to you 💫'],
             dm=['⭐ [name], here is your private reading for tonight ✨', '💖 Hi [name]! Your private reading is ready for you 🌙', '🔮 [name], open this tonight, when it\'s quiet 💫 Your private reading:']),
    60: dict(cena='noite', hora='00h (da noite de 11 para 12/11; 19h na Califórnia, 22h em Nova York: ainda é 11/11 nos EUA)', prova='07-karina', k1='C',
             insta=f'If you\'re holding your phone tonight, wondering if things will ever change, this is for you. 🔮\nThe 11:11 portal is still open. Your private reading is waiting in my story.\nComment "yes" ✨\n{COMUM_HASH} #manifestingmyreality',
             pergunta='what do you want this new chapter to bring you?',
             nums=[('888', 18, 10.5, 'alto à esquerda', 'rosa-choque', '#FF4FD8', 15), ('11:11', 82, 28, 'no meio à direita', 'ciano', '#3DE0FF', 12), ('222', 82, 46.9, 'à direita, na altura do ombro', 'amarelo-ouro', '#FFD21F', 11)],
             coment=['🌙 Sent, check your inbox 💖', '✨ It\'s in your messages, take a look 🔮', '💫 I sent it to your DMs ✨'],
             dm=['🌙 [name], the 11:11 portal is still open ✨ Your private reading:', '💖 Hi [name]! Here\'s your private reading 🔮', '✨ [name], this is for your next chapter 💫 Your private reading:']),
}

LEITURA = ('11/11/2026 ~00h40, painéis do dia 11 (continuação do kit do portal): a leitura focada ampliada de 10/11 (lista no ROTEIRO-KIT-PORTAL-NORA51-54.md) + '
           'COMUNIDADE de 10/11 22h40 a 23h35 (9 vídeos da Soma e do @mundoespiritualbrasil, Lucas Dusi, 14ª leitura, volume de 6 por dia, lote 2, visual limpo, adiado para 12/11) + PROVAS-REAIS-TRUSTPILOT.md (só as avaliações sem cartas: Katrina e Darcey), '
           'BIBLIOTECA-VIDEOS-VIRAIS 49.6 a 49.8 (a Soma grava vários no mesmo dia com a mesma roupa e troca no outro dia), LICOES de 10/11 (o T04 e o filtro do Flow, '
           'nomes do Gerador, prompt do Gerador conferido, repetições do Flow), FATOS (story-0311, créditos), DNA Visual - Nora v2 (figurino varia, liso, sem estampa; '
           'rosto e marcas fixos), PLANO-MVM (cenário e roupa mudam de um vídeo para o outro, não dentro do mesmo; "sem decote" era só do perfil antigo da Nora v1).')


def xy(x, y):
    return f'X {round(x / 100 * 720 - 360)} · Y {round(640 - y / 100 * 1280)}'


def montar(n):
    v = VIDEOS[n]; nn = f'nora{n}'; c = v['cena']; s = CENAS[c]
    primeiro = (n == s['primeiro'])
    usa = [v['k1'], 'P', 'K']
    gera = ['A', 'B', 'C', 'P', 'K'] if primeiro else []
    irmaos = [m for m in VIDEOS if VIDEOS[m]['cena'] == c]
    caixa, caixa_fim = CAIXA[v['k1']]
    face_var = not primeiro  # o 2º e o 3º da cena repetem o T02 e o T04: no Face vai a variação (regra de 10/11)
    p = {
        'perfil': copy.deepcopy(P46['perfil']),
        'trava_referencia': P46['trava_referencia'], 'figurino': s['roupa'], 'excecao_estilo': '',
        'ocultar_bloco_agente_imagem': True,
        'roteiro': {
            'id': f'{nn}-DIA-1111-{c.upper()}-' + ('PROVA' if v['prova'] else 'SEM-PROVA'),
            'titulo': f'Dia 11/11 ({s["nome"]}): curto, 11/11 (quarta), {v["hora"].split(" (")[0]}, ' + ('com a prova do Trustpilot' if v['prova'] else 'sem prova (controle)'),
            'dor': 'a próxima fase da vida chegando (amor, paz, propósito, dinheiro sem aperto), com o portal 11:11 de hoje como motivo',
            'formato': f'Sem pré-gancho; selfie com cara de celular, {s["nome"]} ({s["img"]}); takes: ' + ' + '.join(ROT[k] for k in usa),
            'molde_hook': 'Gancho da data dos maiores reels da Soma Chhaya ("If you see this on [dia]..."), com a variação do relógio e a da situação',
            'duracao_total': 25,
            'descricao_instagram': v['insta'],
            'legenda_aviso': 'No Face, use a mesma legenda SEM a linha do “Comment …” (o Face entrega menos post com pedido de comentário).',
            'leitura_registro': LEITURA,
        },
        'refs': [f'Folha da Nora v2 (1K) na geração da {s["img"]}', f'{s["img"]} em todos os takes'],
        'imagens': [{'rotulo': f'IMAGEM 1 · {s["img"]}', 'cena': f'(seção Imagem do painel do nora{s["primeiro"]})', 'anexar': 'a folha da Nora (1K)'}],
        'videos': [{'rotulo': ROT[k], 'cena': CENA_TXT[k], 'duracao': dur(k), 'primeiro_quadro': f'IMAGEM 1 ({s["img"]})', 'acao': '', 'b_roll': '',
                    'fala': F[k], 'movimentacao': mov(c, k), 'arquivo': nome(c, k)} for k in (gera if gera else usa)],
        'texto_tela': {'hook': caixa, 'hook_comeca': 'o primeiro quadro', 'hook_termina': caixa_fim, 'hook_alt': '', 'extras': []},
        'comentario_fixado': {
            'insta': f'{v["pergunta"][0].upper() + v["pergunta"][1:]} ✨ Tell me below, then tap my photo and open my story: your private reading starts there. 🔮',
            'face': f'{v["pergunta"][0].upper() + v["pergunta"][1:]} ✨ Your private reading is right here 🔮 👉 {FB}'},
        'respostas_face': {'aviso': P49['respostas_face']['aviso'], 'comentario': v['coment'], 'dm': v['dm']},
    }
    if n < 58:
        p['story'] = {'ja_postado': True, 'nota': ('STORY: o story-0311 está no ar até ~19h42 de hoje (repost de 10/11 às 19h42). Não poste outro agora: o repost de hoje está no painel '
                                                   f'do nora58 (~17h50, antes do post das 18h). Links: Insta (STORYIG): {STORYIG} · Face (FACE): {FB}')}
    elif n == 58:
        p['story'] = {
            'prompt_imagem': '(Não gere imagem: use a story-3110 de novo. Só o texto muda.)',
            'anexar': 'Nada: a imagem é a story-3110, que você já tem.',
            'textos': [{'posicao': ('Uma frase só, uma cor (creme #F1E6D3), em 2 linhas, na parede acima da cabeça, logo abaixo da barra do Instagram (entre ~11% e ~19% da altura); '
                                    'pode encostar no alto do cabelo, nunca no rosto. Adesivo de link na mesa, no lugar de sempre'),
                        'texto': 'Tap below: your private reading\nis waiting for you on 11:11.'}],
            'adesivos': ['Open my reading'],
            'nota': ('REPOSTE O STORY ~17h50, ANTES DO POST DAS 18h (o de 10/11 vence ~19h42), no Insta e no Face: imagem story-3110, o texto acima em 2 linhas e o adesivo de link '
                     '“Open my reading”. Ao vivo, sem programar. Confira na prévia o link de cada rede. Em 12/11, o 1º painel do dia troca o texto pelo sem portal. '
                     f'Insta (STORYIG): {STORYIG} · Face (FACE): {FB}')}
    else:
        p['story'] = {'ja_postado': True, 'nota': ('STORY: repostado no painel do nora58 (~17h50 de 11/11; vence ~17h50 de 12/11). Não poste outro hoje. '
                                                   f'Links: Insta (STORYIG): {STORYIG} · Face (FACE): {FB}')}

    mt = copy.deepcopy(P49['mapa_tela'])
    mt['numeros'] = [dict(t=a, x=x, y=y, onde=o, cor_nome=cn, cor=co, tamanho=tm) for (a, x, y, o, cn, co, tm) in v['nums']]
    linhas = caixa.split('\n')
    topo = {'nome': 'Caixa do topo: ' + ' / '.join(f'“{l}”' for l in linhas), 'fonte': 'Poppins Bold (poppins-bd)',
            'cor': 'texto preto; a 1ª linha (a data) em vermelho #E53935', 'tamanho': '10, em 3 linhas (até ~84% da largura)', 'contorno': 'Plano de fundo branco arredondado',
            'obs': 'X 0 · Y 397, do 1º quadro até o fim do 1º take (a data). Eu ponho (P45).'}
    numeros = {'nome': 'Números fixos espalhados (11:11, 888, 222)', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'uma cor para cada número',
               'tamanho': 'um tamanho para cada número', 'contorno': 'Traço preto + Sombra preta, sem Plano de fundo',
               'obs': 'Provisório: ' + '; '.join(f'{a} {cn}, {tm}, {xy(x, y)}' for (a, x, y, o, cn, co, tm) in v['nums']) + '. Confiro na imagem aprovada e na prévia. Eu ponho (P45).'}
    mt['estilos'] = [numeros, topo,
        {'nome': 'Legenda (eu ponho, P45)', 'fonte': 'Poppins Bold', 'cor': 'branco, em MAIÚSCULAS; palavra-chave em amarelo-ouro #FFD21F', 'tamanho': 'uns 38 px (vídeo 720×1280)',
         'contorno': 'preto grosso', 'obs': 'Do 1º quadro ao fim (não há pré-gancho), blocos de 2 a 4 palavras, abaixo do queixo.' + (' Some enquanto a avaliação está na tela.' if v['prova'] else '')},
        {'nome': 'Faixa do story: “Your private reading is in my story”', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto, “my story” em vermelho #E53935',
         'tamanho': '9, em 1 linha', 'contorno': 'Plano de fundo branco arredondado', 'obs': 'Do T04 (o CTA) até o fim, X 0 · Y 397. Eu ponho (P45).'},
        {'nome': 'Seta vermelha (↓)', 'fonte': '—', 'cor': 'vermelho #E53935 com traço preto', 'tamanho': '14', 'contorno': '—',
         'obs': 'Do T04 até o fim, embaixo à esquerda (X -288 · Y -333, P43), apontando para a foto do perfil. Eu ponho (P45).'},
    ]
    if v['prova']:
        quem, trecho = PROVA[v['prova']]
        mt['estilos'].append({'nome': f'Avaliação real do Trustpilot: {quem} (“{trecho}”)', 'fonte': f'a imagem provas-trustpilot/{v["prova"]}-sem-hora.png (print real do aluno, 11/11, sem o nome do app; tirei só a hora relativa, que muda todo dia, e a linha de botões)',
                              'cor': '—', 'tamanho': '~84% da largura (604 px num vídeo de 720)', 'contorno': 'sem borda; cantos arredondados e sombra leve',
                              'obs': 'X 0 · Y -200 (sobre a blusa, longe do rosto), da palavra “begins” até o fim do T02, logo antes do CTA (~3 s); a voz continua por baixo e o vídeo não fica mais longo. Eu ponho (P45).'})
        mt['estilos'].append({'nome': 'Caixa da prova: “Rated 4.8 ★ by 2,200+ people”', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto; “4.8 ★” em vermelho #E53935',
                              'tamanho': '9, em 1 linha', 'contorno': 'Plano de fundo branco arredondado',
                              'obs': 'X 0 · Y 397, junto com a avaliação (o topo está livre nesse trecho: a caixa da data já saiu e a faixa do story ainda não entrou). Número real: 4,8 com 2.251 avaliações na página do Trustpilot em 11/11 (aluno). Eu ponho (P45).'})
    mt['regras'] = [('Teste de 11/11 a 0 crédito (decisão do aluno, 11/11 ~01h35): ' + ('este vídeo TEM a prova do Trustpilot antes do CTA' if v['prova'] else 'este vídeo NÃO tem prova (é o controle)') + '. 12h, 18h e 00h com a prova; 9h, 15h e 21h sem. Visual de agora em todos (o visual limpo foi para 12/11). Régua: visitas ao perfil por 1.000 views, toques no link do story e cliques no Tracker de cada horário.'),
                    f'Posições provisórias até a {s["img"]} ser aprovada; confiro de novo na prévia da edição (número longe do rosto, da mão e do texto).',
                    'Sem pré-gancho: o texto do topo, os números e a legenda entram desde o 1º quadro.']
    p['mapa_tela'] = mt

    corte_nome = f'{nn}-cortado'
    lista_usa = ', '.join(nome(c, k) for k in usa)
    p['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” só estes 3 takes, de uma vez: {lista_usa}. Ela junta pela ordem do nome (já estão em ordem).',
        'nome': corte_nome, 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pela ordem do nome (' + ', '.join(ROT[k] for k in usa) + ')',
        'depois': ['Suba os 3 takes e espere a Prévia.',
                   'Aperte play com Resultado marcado: confira a primeira palavra do 1º take e a última do último take.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.',
                   f'Clique em Cortar e baixar e salve como {corte_nome}. (O texto eu ponho aqui, no fim.)']}
    p['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {corte_nome}', 'como': 'É o vídeo que saiu da FusionZ (sem pré-gancho: começa direto na data).'},
        {'quando': '1. Do começo ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'O vídeo todo, por baixo da voz.'},
        {'quando': '2. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'720×1280 ou 1080×1920, qualidade alta, nome {nn}-montado (se passar de 30 MB, link do Drive). Eu ponho tudo e devolvo o {nn}-final'
                 + (f' e o {nn}-final-FACE (a variação para o Face).' if face_var else '.')}]

    pecas = []
    if primeiro:
        pecas.append({'nome': s['img'], 'tipo': 'imagem 1', 'status': 'gerar', 'creditos': 0,
                      'descricao': f'Selfie com cara de celular, {s["nome"]}: {s["roupa_pt"]} (Flow, Nano Banana Pro, x4). A mesma imagem para os 3 vídeos da cena.'})
    else:
        pecas.append({'nome': s['img'], 'de': f'{s["img"]} (do painel do nora{s["primeiro"]})', 'tipo': 'imagem 1', 'status': 'reutilizar', 'descricao': f'A imagem da {s["nome"]}, gerada no painel do nora{s["primeiro"]}.'})
    for k in usa:
        if k in gera:
            pecas.append({'nome': nome(c, k), 'tipo': 'take', 'status': 'gerar', 'creditos': 12 if dur(k) == '8' else 15, 'descricao': f'“{F[k]}”'})
        else:
            pecas.append({'nome': nome(c, k), 'de': f'{nome(c, k)} (do painel do nora{s["primeiro"]})', 'tipo': 'take', 'status': 'reutilizar', 'descricao': f'“{F[k]}”', 'fala': F[k]})
    for k in gera:
        if k not in usa:
            dono = [m for m in irmaos if VIDEOS[m]['k1'] == k][0]
            pecas.append({'nome': nome(c, k), 'tipo': 'take', 'status': 'gerar', 'creditos': 12 if dur(k) == '8' else 15, 'descricao': f'Para o nora{dono} ({VIDEOS[dono]["hora"].split(" (")[0]}): “{F[k]}”'})
    if v['prova']:
        pecas.append({'nome': f'{v["prova"]}-sem-hora', 'de': 'provas-trustpilot/ (no projeto; eu ponho)', 'tipo': 'prova', 'status': 'reutilizar', 'descricao': f'Avaliação real do Trustpilot ({PROVA[v["prova"]][0]}), antes do CTA. 0 crédito; você não precisa fazer nada.'})
    pecas.append({'nome': 'story-0311', 'de': 'story-3110', 'tipo': 'story', 'status': 'reutilizar',
                  'descricao': 'Repostar ~17h50 com o texto do 11:11 (seção Story deste painel).' if n == 58 else 'No ar; o repost de hoje é no painel do nora58 (~17h50).'})
    hora_curta = v['hora'].split(' (')[0]
    decisao = [f'ESTE VÍDEO USA SÓ 3 TAKES, nesta ordem: ' + ' + '.join(nome(c, k) for k in usa) + '.'
               + (f' Os outros 2 Takes 1 gerados neste painel são do ' + ' e do '.join(f'nora{m} ({VIDEOS[m]["hora"].split(" (")[0]})' for m in irmaos if m != n) + '.' if primeiro else ''),
               f'Postar em 11/11 (quarta), {v["hora"]}, no Insta e no Face, ao vivo.',
               (f'Dia 11 (decisão do aluno, 10/11 ~23h55 e 11/11 ~00h30): 6 por dia, de 3 em 3 h; {s["nome"]} ({s["roupa_pt"]}) para '
                + ', '.join(VIDEOS[m]['hora'].split(' (')[0] for m in irmaos) + '. Rosto e marcas da Nora iguais; cenário e roupa mudam de um dia para o outro (como a Soma), nunca dentro do vídeo.'),
               ((f'COM A PROVA (teste de 11/11, decisão do aluno): a avaliação real de {PROVA[v["prova"]][0]} no Trustpilot aparece da palavra “begins” até o fim do T02, logo antes do CTA, com a caixa “Rated 4.8 ★ by 2,200+ people” no topo (número real de 11/11). Eu ponho na edição (0 crédito); você não precisa mandar nada.')
                if v['prova'] else
                'SEM PROVA (o controle do teste de 11/11: 12h, 18h e 00h têm a avaliação do Trustpilot antes do CTA; este não). Visual de agora (caixa branca e números coloridos) em todos; o visual limpo foi para 12/11.'),
               ('Face: este vídeo repete o T02 e o T04 do post anterior da cena, e o Face trava post repetido (regra de 10/11). Eu entrego também o '
                f'{nn}-final-FACE (espelhado, mais claro, 1,1x): no Face, poste o -FACE.' if face_var else
                'Face: o mesmo arquivo do Insta (1º vídeo da cena).')]
    decisao.append(f'Créditos deste painel: {creditos(gera)} (conta contatocaram). Os outros 2 painéis da cena: 0.' if gera else f'0 crédito: os takes saem do painel do nora{s["primeiro"]}.')
    p['pecas'] = {'lista': pecas, 'decisao': decisao}

    if primeiro:
        passos = [f'Imagem: gere a {s["img"]} (seção Imagem 1) e me mande as 4 opções. Eu fecho o LIVRE e as movimentações pela escolhida e republico este painel no mesmo link. Só depois gere os takes.',
                  f'Central do curso com a configuração desta seção (o LIVRE é o desta cena). Cole a fala e a movimentação da colagem (seção “A fala e a movimentação”). Confira: 5 takes de 8 ou 10 s.',
                  f'Agente do Flow na contatocaram (seção do agente): anexe só a {s["img"]}, cole o aviso e o “COPIAR TUDO JUNTO”. Omni 1.1 Flash, 720p.',
                  f'Renomeie os 5 takes com os nomes da lista ({s["pre"]}-…). Ao baixar, ouça o 1º: a data tem de sair “Wednesday, November eleventh”.']
    else:
        passos = [f'Nada para gerar: os 3 takes saem do painel do nora{s["primeiro"]} (já gerados e renomeados).']
    passos += [f'Corte de silêncio (seção “Cortar os silêncios”): {lista_usa}; Juntar tudo LIGADO, Corte seco → {corte_nome}.',
               f'CapCut: o {corte_nome} + a música de sempre a −18 dB; exporte SEM texto como {nn}-montado e me mande aqui (Drive, se passar de 30 MB).',
               (f'Eu devolvo o {nn}-final' + (f' e o {nn}-final-FACE' if face_var else '') + f'. Confira no celular e poste em 11/11, {hora_curta}, ao vivo: no Insta o {nn}-final, no Face o '
                + (f'{nn}-final-FACE' if face_var else f'{nn}-final') + '. Legenda: a do Insta tem o pedido de comentário; no Face, sem ele. Comentário: no Insta, comente e fixe (sem link); '
                'no Face, comente COMO A PÁGINA (já tem o link).')]
    if n == 58:
        passos.insert(0, 'STORY primeiro: ~17h50, antes do post das 18h, reposte o story (seção Story).')
    cf = config(c)
    if gera:
        p['central'] = {'imagem_unica': True,
                        'conferir': (f'Conferir em cada take: é a Nora da {s["img"]} (rosto, lua com 3 estrelinhas, trança, brincos, colar de Vênus, {s["roupa_pt"]}); ela fala uma vez só, '
                                     'em inglês, com "eleven eleven" e "November eleventh"; o braço do celular não se mexe; a mão livre só faz o gesto do T02, na altura do ombro; '
                                     'sem texto, legenda ou música. Renomeie com o nome da lista.'),
                        'passos': passos, 'config': cf, 'agente': agente(c, gera),
                        'colagens': [{'titulo': f'{nn}: 5 takes da {s["nome"]} ({", ".join(ROT[k] for k in gera)})', 'fala': ' '.join(F[k] for k in gera),
                                      'movimentacao': [mov(c, k) for k in gera], 'takes': list(range(len(gera)))}]}
        p['imagem_central'] = img_central(c, n)
        ordem = ['pecas', 'imagens', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface', 'fala']
    else:
        p['central'] = {'imagem_unica': True, 'conferir': '', 'passos': passos, 'config': cf, 'agente': agente(c, ['A']), 'colagens': []}
        p['imagem_reutilizada'] = {'arquivo': s['img'], 'nota': f'gerada no painel do nora{s["primeiro"]}'}
        ordem = ['pecas', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface', 'fala']
    p['ordem'] = ordem
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', f'<title>Painel {nn} · dia 11/11</title>', html, count=1)
    (R / f'PAINEL-NORA{n}.html').write_text(html, encoding='utf-8')
    print('ok', nn, c, 'prova' if v['prova'] else 'sem prova', 'usa', [ROT[k] for k in usa], 'gera', len(gera), 'créditos', creditos(gera))


for n in VIDEOS:
    montar(n)
