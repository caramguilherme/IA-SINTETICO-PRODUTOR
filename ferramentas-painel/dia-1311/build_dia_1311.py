# Painéis do dia 13/11/2026 (sexta-feira 13): nora62 (Face, à tarde, o bicarbonato) e nora63 (Insta à 0h de 13 para 14/11 e o mesmo no Face, a canela).
# Decisões: Clone R39, R40 e R41 (CLONE-DO-GUSTAVO-RESPOSTAS.md); o vídeo da volta sem data (aluno, 13/11 ~11h15); pré-gancho com a Nora em ação,
# algo novo a cada 0,5 s e um produto famoso dos EUA com o rótulo real (regra de 13/11 10h38 e ~10h50; BIBLIOTECA-PRE-GANCHOS.md, topo e nº 39);
# o comentário do 222 antes do CTA do story, que é a última frase (13/11 10h56, os virais do Scoped); Omni 1.2 Flash em 360p (padrão desde 12/11).
# Cenas: nora62 na manha1111-IMG (a do nora55, o maior do Face; dia); nora63 na noite1111-IMG (a da noite de 11/11; posta à 0h).
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-1311/build_dia_1311.py
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
P49 = pacote('PAINEL-NORA49.html')
P51 = pacote('PAINEL-NORA51.html')
CFG = copy.deepcopy(P51['central']['config'])
VOZ = [c for s in CFG for c in s['campos'] if c['campo'].startswith('Perfil de voz')][0]['copiar']
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'

# ------------------------------------------------------------------ as duas cenas (iguais às do build_dia_1111.py e do build_dia_1211.py)
MANHA = dict(
    img='manha1111-IMG', nome='cena da manhã (escritório)',
    cel='her right arm on the left side of the frame', canto='bottom-left', livre_mao='her left hand on the right side of the frame', lado_gesto='right', mao='left',
    roupa_cont='her plain black fitted square-neck tank top and the very oversized, open heather-grey zip-up hoodie hanging loose over it',
    repouso='rests at collarbone height, her fingers lightly holding a lock of her hair over the edge of the open hoodie', volta='the same spot at collarbone height',
    quando='in the daytime', onde='a real, lived-in American home office', luz='lit only by soft daylight from a window on the right side of the frame',
    fundo='the plain light wall, the office chair behind her, the shelf and the window light', visual='soft daylight from a window in the background')
NOITE = dict(
    img='noite1111-IMG', nome='cena da noite (sala com abajur)',
    cel='her right arm on the left side of the frame', canto='bottom-left', livre_mao='her left hand on the right side of the frame', lado_gesto='right', mao='left',
    roupa_cont='her plain black fitted square-neck tank top with wide straps',
    repouso='rests at collarbone height with her fingertips lightly touching the small gold Venus pendant', volta='the small gold Venus pendant at collarbone height',
    quando='at night', onde='a real, lived-in American living room', luz='lit only by a warm table lamp on the right side of the frame',
    fundo='the plain light warm wall, the beige sofa with the throw blanket, the lamp and the small bookshelf behind her', visual='warm table lamp light in the background')

ESTRELAS = ('the small flat gold crescent moon on her cheek on the left side of the frame with three tiny separate gold five-pointed stars next to it '
            '(three stars with visible points, never dots or circles)')

# ------------------------------------------------------------------ falas
F = {
    # nora62 (Face, à tarde; sexta-feira 13; R41 com o T1 sem o "before noon" e o T3 sem o "first")
    'B1': "Drop baking soda in water this Friday the 13th: your luck is about to change.",
    'B2': "Today a financial door that was locked all year is finally opening to bring unexpected ease to your family.",
    'B3': "This blessing doesn't happen for everyone. Check the link in the comments below to see what twenty twenty-seven holds for you.",
    # nora63 (Insta à 0h e Face à 0h; sem data; R41 + o T1 do viral nº 3 reescrito)
    'C1': "Put cinnamon in a glass of water before you leave home. I know it sounds silly, but you'll thank me later.",
    'C2': "The universe saw your quiet faith. A major turnaround is arriving, bringing unexpected money, deep peace, and someone truly wonderful.",
    'C3': "The worst is behind you. Heavy doors that stayed locked all year are finally opening to welcome your abundance.",
    'C4': "Comment two two two right now so I know your energy is ready to receive this shift.",
    'C5': "This shift isn't the same for every woman. Tap my photo for the quick reading in my story for twenty twenty-seven.",
}
RESERVA = {
    'B3': "This blessing doesn't happen for everyone. The link in the comments shows what twenty twenty-seven holds for you.",
    'C5': "This shift isn't the same for every woman. Open my story for the quick reading about twenty twenty-seven.",
}
SUF = {'B1': 'T01-bicarbonato', 'B2': 'T02-porta-financeira', 'B3': 'T03-cta-link-2027',
       'C1': 'T01-canela', 'C2': 'T02-fe-silenciosa', 'C3': 'T03-portas-abrindo', 'C4': 'T04-comente-222', 'C5': 'T05-cta-story-2027'}
ROT = {'B1': 'T01', 'B2': 'T02', 'B3': 'T03', 'C1': 'T01', 'C2': 'T02', 'C3': 'T03', 'C4': 'T04', 'C5': 'T05'}
TXT = {'B1': 'o Take 1 do Face: o bicarbonato + a sexta-feira 13 (R41)', 'B2': 'a promessa: a porta financeira abrindo (R39)',
       'B3': 'o CTA do Face: a bênção não é para todos + o link nos comentários + 2027 (R39)',
       'C1': 'o Take 1 da volta: a canela no copo d\'água (viral nº 3 do Scoped, reescrito; sem data)',
       'C2': 'a fé silenciosa vista + a virada: dinheiro, paz e alguém especial (R41)',
       'C3': 'o pior passou + as portas abrindo (R41); a avaliação da Katrina nos últimos 3 s',
       'C4': 'o pedido do 222, antes do CTA (R40 + os virais do Scoped; só no Insta)',
       'C5': 'o CTA: não é igual para toda mulher + foto, story e 2027 (R41, sem o "only")'}
PRE = {'B': 'd1311', 'C': 'd1311'}
CENA = {'B': MANHA, 'C': NOITE}


def nome(k):
    return f'{PRE[k[0]]}-{SUF[k]}' + ('-face' if k[0] == 'B' else '')


GESTO = {
    'B1': 'during the first half of the take her eyebrows lift with a bright, curious look, in the closing half a confident smile appears and she gives one small nod',
    'B2': 'during the first half of the take she holds a calm, knowing look, in the closing half she lifts her {mao} hand to the height of her shoulder with the palm up and then returns it to {volta} with a warm smile',
    'C1': 'during the first half of the take her eyebrows lift with a playful, knowing look, in the closing half a small amused smile appears and she gives one quick nod',
    'C2': 'during the first half of the take she holds a soft, tender look with her head tilted slightly, in the closing half her eyes brighten with a warm smile',
    'C3': 'during the first half of the take she holds a calm, reassuring look, in the closing half she lifts her {mao} hand to the height of her shoulder with the palm up and then returns it to {volta} with a relieved smile',
    'C4': 'during the first half of the take she holds an encouraging look, in the closing half she gives one small inviting nod with a bright smile',
}


def base_mov(c, d, g):
    return (f'Throughout the whole {d} seconds she keeps an unchanged handheld selfie framing, {c["cel"]} stays extended toward the camera '
            f'holding the phone out of frame and never moves, {c["livre_mao"]} {c["repouso"]} except during the one small '
            f'gesture described here, which always happens at the height of her shoulder on the {c["lado_gesto"]} side of the frame and never in front of her face or mouth, and her eyes '
            f'stay on the lens, {g}, and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; the camera keeps only a tiny '
            'natural handheld sway with no zoom and no cuts, the braid stays on the right side of the frame, everything else in the room stays still and each hand has exactly five fingers.')


def mov_cta(c):  # CTA sem gesto de mão (lição do T04 de 10/11: mão descendo = filtro do Flow)
    return (f'Throughout the whole 10 seconds she keeps an unchanged handheld selfie framing; {c["cel"]} stays extended toward the camera '
            f'holding the phone out of frame and never moves; {c["livre_mao"]} stays still and {c["repouso"]} for '
            'the whole clip and never moves down; her eyes stay on the lens; during the first half of the take she holds a warm, confident look, and in the closing half she gives one '
            'small encouraging nod with a warm smile; from the end of the final sentence until the clip ends she keeps her lips closed and silent; the camera keeps only a tiny natural '
            'handheld sway with no zoom and no cuts, the braid stays on the right side of the frame, everything else in the room stays still and each hand has exactly five fingers.')


def mov(k):
    c = CENA[k[0]]
    if k in ('B3', 'C5'):
        return mov_cta(c)
    return base_mov(c, 10, GESTO[k].format(volta=c['volta'], mao=c['mao']))


COMUNS = {('of', 'the'), ('and', 'the'), ('to', 'the'), ('in', 'the'), ('on', 'the'), ('at', 'the'), ('for', 'a'), ('of', 'her'), ('and', 'her'),
          ('as', 'if'), ('the', 'lens'), ('her', 'left'), ('and', 'then'), ('the', 'hand'), ('she', 'gives'), ('the', 'height'), ('a', 'warm'), ('with', 'a'),
          ('the', 'whole'), ('a', 'small'), ('for', 'the')}
for k, f in list(F.items()) + [(k + 'r', v) for k, v in RESERVA.items()]:
    assert len(f.split()) <= 22, (k, len(f.split()))
    kk = k[:2]
    fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(kk).lower())
    sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS
    assert not sobra, (k, sobra)
    assert 'private' not in f.lower() and 'card' not in f.lower() and 'portal' not in f.lower(), k


def livre(c):
    return (f'Casual handheld iPhone front-camera selfie video {c["quando"]} in {c["onde"]}, looking exactly like a real phone video, {c["luz"]}. '
            'CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, the thin braid wrapped with small gold rings hanging down on the right side of the frame, '
            f'{ESTRELAS}, her star-and-moon drop earrings, her thin gold Venus necklace, '
            f'the thin gold bracelets on her {c["mao"]} wrist, the gold sun ring on her {c["mao"]} hand and {c["roupa_cont"]} stay exactly as in the reference image; the framing is exactly '
            f'the one of the reference image, a close selfie with her face large and centered and her eyes at about one third of the frame height; {c["cel"]} '
            f'stays extended toward the camera holding the phone out of frame, running off the {c["canto"]} corner, and never moves; {c["livre_mao"]} '
            f'{c["repouso"]} and only lifts for the one small gesture of a take, at the height of her shoulder on the {c["lado_gesto"]} side of the frame, never in front of her face '
            f'or mouth; {c["fundo"]} stay exactly where they are; natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter, no glow and '
            'no sparkles; the camera has only a tiny natural handheld sway, no zoom, no cuts and no reframing; no phone, object, person, animal or text appears or disappears; '
            'each hand always has exactly five fingers; no on-screen text, no captions, no logos; real quiet room ambient sound only, no music. SPEECH RULE for every take: she '
            "says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added sentence before, between or "
            'after; numbers are spoken as words ("Friday the 13th" as "Friday the thirteenth", "two two two" as three separate words, twenty twenty-seven exactly as written); '
            'when she finishes the last word she closes her lips, stays silent and keeps a calm still expression until the clip ends.')


def prompt_manual(c, fala, movimento):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image speaks directly '
            f'to her phone camera in a casual handheld selfie video at home {c["quando"]}.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + fala + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            'VOICE PACING: medium pace (155 to 180 words per minute), about 8 seconds of speech; when she finishes the last word she closes her lips and stays silent '
            'with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + movimento + '\n\n'
            f'VISUAL: realistic casual iPhone front-camera selfie video, {c["visual"]}, natural skin texture with visible pores, '
            'slight phone grain, everything in focus, no bokeh, no filter.\n\n'
            'CAMERA: handheld, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n'
            'AUDIO: only her voice and quiet room ambience; no music, no other voices, no sound effects.\n\n'
            f'CONTINUITY: her face, long black wavy hair, the thin braid with small gold rings, {ESTRELAS}, '
            f'her star-and-moon earrings, her gold Venus necklace, her gold sun ring and bracelets, {c["roupa_cont"]} and the room behind her stay '
            'exactly as in the reference image; no phone, object, person or text appears; each hand has exactly five fingers; no on-screen text, captions or logos.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.')


def config(c):
    cf = copy.deepcopy(CFG)
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = f'colar o texto abaixo (fechado pela {c["img"]}, aprovada em 11/11)'
                campo['copiar'] = livre(c)
    return cf


PRE_LUCAS = ('Below, you will find several prompts, each corresponding to a different video. Please generate all the videos in sequential order, from the first prompt to the last.\n'
             'Maintain the exact same voice across all videos, ensuring EXACTLY THE SAME VOLUME, with no variations in background, intonation, or vocal clarity. Use the attached image as both the first and last frame of every generated video.\n'
             'Please submit ALL generation requests at once and in the correct order, so that all videos can be generated simultaneously.\n'
             'If the generation of any video fails, please resubmit ONLY the item that failed until it is successfully generated.')


def agente(c, ks, cta):
    nomes = [f'{i + 1} = {nome(k)}' for i, k in enumerate(ks)]
    return {
        'imagem': c['img'],
        'intro': 'Anexe a imagem, cole o aviso e, embaixo dele, o bloco “COPIAR TUDO JUNTO” da Central.',
        'aviso_tag': 'cole antes do bloco da Central',
        'aviso': (f'Vou te enviar {len(ks)} prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um com o devido '
                  'número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.'),
        'passos': [
            'Conta do Flow: contatocaram. Abra um PROJETO NOVO no Flow (se o agente parar, projeto novo, não pasta nova) e uma conversa nova no agente.',
            'Nas configurações do agente: Omni 1.2 Flash · 360p · 10 s · 9:16 (o padrão desde 12/11: 10 créditos por take) e gerar sem pedir aprovação. Depois, BAIXE cada take em 720p (não gasta crédito).',
            f'Anexe só a {c["img"]}.',
            'Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.',
            'Renomeie cada take com o nome da lista (o número é a ordem): ' + ' · '.join(nomes) + '. '
            'Se ele não renomear, mande na mesma conversa: “Now rename each video with the correct number from the prompt.”',
            f'Confira na grade, pelo nome, se os {len(ks)} saíram, e se a lua no rosto tem as 3 estrelinhas com pontas (no 1.2 elas já viraram bolinhas). Se um falhar por política: mande na mesma conversa “Please generate video X from my previous message again, with the same prompt.” '
            '(X = o número dele na lista). Se falhar de novo, não insista: me mande o print.',
            f'Se o CTA ({ROT[cta]}, o último) falhar 2 vezes, gere à mão: Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; Início = {c["img"]}; Fim = vazio; cole o prompt abaixo, '
            f'inteiro (10 créditos), e renomeie para {nome(cta)}. PROMPT: ' + prompt_manual(c, F[cta], mov_cta(c)),
            f'Se falhar também no Frames: o mesmo caminho com a fala reserva e o mesmo nome. PROMPT RESERVA: ' + prompt_manual(c, RESERVA[cta], mov_cta(c)),
            'Se o agente parar no meio (por exemplo, “alta demanda”): responda na MESMA conversa, sem anexar nada: “Please continue and generate videos X to Y from my previous message, in the same order.” '
            '(troque X e Y pelos números que faltaram). Se ele gerar só o 1º e parar de novo: cole antes do bloco da Central o “pré-prompt do Lucas” (abaixo) e mande de novo só os que faltaram.',
            'Se o agente disser que não dá para usar a imagem como quadro inicial e final com fala: gere à mão: Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; '
            f'Início = {c["img"]}; Fim = vazio; no prompt, só o texto do prompt daquele take.',
            'Pré-prompt do Lucas (só se precisar): ' + PRE_LUCAS,
        ],
    }


# ------------------------------------------------------------------ pré-ganchos (a Nora em ação, algo novo a cada 0,5 s, produto com o rótulo real)
CANELA_IMG = ('Use the attached images as references: the first image is the woman (keep her face, her long black wavy hair, the thin braid with small gold rings, '
              f'{ESTRELAS.replace("on her cheek on the left side of the frame", "on her cheek")}, her star-and-moon earrings, her gold Venus necklace and her plain black fitted square-neck tank top with wide straps '
              'exactly the same); the second image is the real McCormick Ground Cinnamon bottle. RAW photo taken at night with a phone propped on a kitchen counter about 70 '
              'centimeters in front of her: the same woman stands behind a real lived-in American kitchen counter at night, warm light from a pendant lamp above, dark cabinets '
              'behind her; she is framed from the waist up, centered, looking down at her hands with a focused expression; in her right hand, on the left side of the image, she '
              'holds the exact McCormick Ground Cinnamon bottle from the reference photo at chest height, label facing the camera, sharp and legible (red cap with black top, '
              'the blue "Mc" square, the red "McCormick" banner, "CINNAMON GROUND"), and her left hand, on the right side of the image, is already twisting the cap open; a clear '
              'glass of water stands on the counter in front of her, in the lower middle of the image; the upper 20 percent of the image is plain dark cabinets with nothing in it; '
              'looks exactly like a real casual iPhone photo at night, slight phone grain, natural colors, everything in focus, no bokeh; the only text in the image is the real '
              'label of the cinnamon bottle; no other text, no logo, no watermark; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16')
CANELA_VID = ('Use the supplied image as the first frame. Real phone video at night, the phone propped on the counter, steady, no slow motion: every half second something new '
              'happens. 0.0 s: she pops the cap of the McCormick Ground Cinnamon bottle open with a click, the label still facing the camera. 0.5 s: she tilts the bottle and '
              'shakes a thick stream of cinnamon into the clear glass of water. 1.0 s: the cinnamon hits the water and blooms into a swirling brown cloud. 1.5 s: she stirs fast '
              'with a spoon and a golden whirlpool spins in the glass. 2.0 s: she lifts the glass up to the warm light and the water glows amber. 2.5 s: she sets the glass down and '
              'pours a little cinnamon into her open palm. 3.0 s: she brings her palm up close to the lens and blows. 3.5 s: a thick cloud of cinnamon dust flies straight toward the '
              'lens and covers the whole frame, glowing in the warm light, until the clip ends. She keeps the same face, braid, crescent moon with three tiny gold stars, earrings, '
              'necklace and black tank top the whole time; the bottle label stays the real McCormick label; each hand has exactly five fingers; nothing else appears or disappears. '
              'AUDIO: close ASMR kitchen sounds only: the cap click, the powder falling into the water, the spoon clinking fast on the glass and the blow; no music, no voice, she '
              'does not speak. No on-screen text, no captions.')
BIC_IMG = ('Use the attached images as references: the first image is the woman (keep her face, her long black wavy hair, the thin braid with small gold rings, '
           f'{ESTRELAS.replace("on her cheek on the left side of the frame", "on her cheek")}, her star-and-moon earrings, her gold Venus necklace, her plain black fitted square-neck tank top and the very oversized open heather-grey zip-up '
           'hoodie exactly the same); the second image is the real Arm & Hammer Pure Baking Soda box; the third is the real Heinz All Natural Distilled White Vinegar bottle. '
           'RAW photo taken in the daytime with a phone propped on a kitchen counter about 70 centimeters in front of her: the same woman stands behind a real lived-in American '
           'kitchen counter in bright daylight from a window, white cabinets behind her; framed from the waist up, centered; in her right hand, on the left side of the image, she '
           'holds the exact Arm & Hammer Pure Baking Soda box from the reference photo at chest height, front facing the camera, sharp and legible (orange and yellow box, the '
           'arm-and-hammer logo in the red circle, "pure Baking Soda"); the exact Heinz Distilled White Vinegar bottle from the reference photo stands on the counter on the right '
           'side of the image with its label facing the camera; a clear empty drinking glass and a shiny gold one-dollar coin lie on the counter in front of her; the upper 20 '
           'percent of the image is plain white cabinets with nothing in it; looks exactly like a real casual iPhone photo, slight phone grain, natural colors, everything in focus, '
           'no bokeh; the only text in the image is the real labels of the two products; no other text, no logo, no watermark; each hand has exactly five fingers; '
           'photorealistic, unretouched, vertical 9:16')
BIC_VID = ('Use the supplied image as the first frame. Real phone video in daylight, the phone propped on the counter, steady, no slow motion: every half second something new '
           'happens. 0.0 s: she rips the top flap of the Arm & Hammer box open toward the camera with a quick tearing sound, the front of the box still facing the camera. 0.5 s: '
           'she scoops a heaping spoon of white baking soda and drops it into the clear glass. 1.0 s: she grabs the Heinz vinegar bottle, label facing the camera, and pours it '
           'into the glass. 1.5 s: white foam erupts and climbs fast up the glass with a loud fizz. 2.0 s: the foam overflows the rim and spills onto the counter. 2.5 s: she '
           'drops the shiny gold coin into the foam with a bright clink. 3.0 s: she looks straight into the camera with wide, excited eyes. 3.5 s: she taps the glass twice '
           'with her fingertip while the foam keeps bubbling, until the clip ends. She keeps the same face, braid, crescent moon with three tiny gold stars, earrings, necklace, '
           'black tank top and grey hoodie the whole time; the labels stay the real Arm & Hammer and Heinz labels; each hand has exactly five fingers; nothing else appears or '
           'disappears. AUDIO: close ASMR kitchen sounds only: the box tearing, the powder falling, the vinegar pouring, the loud fizz, the coin clink and the two taps on the '
           'glass; no music, no voice, she does not speak. No on-screen text, no captions.')


def extras(tipo):
    if tipo == 'B':
        nimg, nvid, prod = 'd1311-PRE-bicarbonato-IMG', 'd1311-PRE-bicarbonato', 'arm-hammer-baking-soda-frente.jpg e heinz-distilled-white-vinegar-frente.jpg'
        img, vid, cena = BIC_IMG, BIC_VID, 'manha1111-IMG'
        tit = 'O bicarbonato Arm & Hammer com o vinagre Heinz (a espuma que transborda e a moeda)'
    else:
        nimg, nvid, prod = 'd1311-PRE-canela-IMG', 'd1311-PRE-canela', 'mccormick-ground-cinnamon-frente.jpg'
        img, vid, cena = CANELA_IMG, CANELA_VID, 'noite1111-IMG'
        tit = 'A canela McCormick no copo d’água e soprada na lente'
    return {
        'titulo_secao': 'Pré-gancho (Flow, à mão, antes dos takes)',
        'conceito': (f'{tit}: a Nora fazendo o ritual, algo novo a cada 0,5 s, com o produto de verdade (regra de 13/11). As fotos dos produtos são as que eu te mandei hoje ({prod}).'),
        'modo': ('Imagem: Flow → Imagem · 9:16 · Nano Banana Pro · x4, anexando as referências na ordem. Vídeo: Flow → Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 8 s; '
                 'Início = a imagem escolhida; Fim = vazio. Baixe em 720p.'),
        'etapas': [
            {'titulo': 'Imagem inicial do pré-gancho', 'nome': nimg, 'tipo': 'img', 'anexar': f'1º a {cena}; 2º (e 3º) a foto do produto ({prod})',
             'quadros': ('x4, 0 crédito. Escolha a que tiver o rótulo do produto IGUAL ao da foto (legível, sem letra trocada), a Nora com a lua e as 3 estrelinhas e 5 dedos em cada mão. '
                         f'Se nenhuma tiver o rótulo certo, gere de novo antes de fazer o vídeo. Se o Flow recusar por causa do nome da marca, apague o nome do texto e deixe só a foto anexada. Renomeie para {nimg}.'),
             'prompt': img},
            {'titulo': 'Vídeo do pré-gancho (8 s, algo novo a cada 0,5 s)', 'nome': nvid, 'tipo': 'vid', 'duracao': 8,
             'quadros': f'Omni 1.2 Flash · 360p · 8 s · x2 (2 chances; ~16 a 20 créditos). Início = {nimg}; Fim = vazio. Mande os 2: eu escolho e corto os ~3,5 s com mais ação.',
             'prompt': vid},
        ],
    }


# ------------------------------------------------------------------ textos e números
RESP_FACE = {
    'aviso': ('Só no Face. Os directs estão PARADOS desde 13/11 (o Tracker de 12/11 fechou com 0 clique depois da 2ª leva). Responda só em público, a mulher e o homem, '
              'apontando para o comentário da Página com o link; nunca o mesmo texto seguido. “Scam” e ataque: ocultar, sem responder.'),
    'link': FB, 'sem_direct': True,
    'comentario': ['💛 Your 2027 reading is in the Page comment ✨', '✨ The link to your reading is in the Page comment 🔮', '🌙 It\'s waiting for you in the comments, love 💫'],
    'dm': [], 'insta': [],
}
INSTA_222 = ['Received ✨ your 2027 reading is waiting in my story 🔮', 'I see you 💛 tap my photo, your next step is in my story',
             'This blessing is yours ✨ check my story before you go', 'Locked in ✨ your quick reading is in my story 🔮', 'So glad this found you 💫 tap my photo for your reading']

VIDEOS = {
    62: dict(hora='à tarde, assim que ficar pronto (era 12h)', rede='só Face', tipo='face', keys=['B1', 'B2', 'B3'], prova=None,
             caixa=('FRIDAY 13TH:\nTHE BAKING SODA TRICK', 'your luck is about to change.'),
             face=('Friday the 13th? Your luck is about to change ✨\nSee what 2027 holds for you: the link is in the comments 🔮\n'
                   '#manifestation #fridaythe13th #lawofattraction #abundance'),
             insta='(não vai no Insta: o Insta está em pausa até 23h20)',
             fix_insta='', fix_face=f'See what 2027 holds for you here ✨ 👉 {FB}'),
    63: dict(hora='0h00 de 13 para 14/11 (22h em Nova York), o 1º do Insta depois da pausa', rede='Insta e Face', tipo='volta', keys=['C1', 'C2', 'C3', 'C4', 'C5'], prova='04-katrina',
             caixa=('WHEN MONEY FEELS STUCK:\nDO THIS WITH CINNAMON', 'you\'ll thank me later.'),
             insta=('Put cinnamon in a glass of water before you leave home ✨\nYour private reading is waiting in my story 🔮\n'
                    'Comment "222" to lock in this blessing ✨\n#manifestation #cinnamonritual #lawofattraction #abundance'),
             face=('Put cinnamon in a glass of water before you leave home ✨\nSee what 2027 holds for you: the link is in the comments 🔮\n'
                   '#manifestation #cinnamonritual #lawofattraction #abundance'),
             fix_insta='Tap my profile picture above to see what 2027 holds for you in my stories ✨',
             fix_face=f'Your 2027 reading is right here 🔮 👉 {FB}'),
}
PROVA = {'04-katrina': ('Katrina H. (EUA)', 'This is going to be so grand for me. Very insightful, honest and calming. So much peace here.')}
NUMS = {62: [('11:11', 82, 10.5, 'alto à direita', 'amarelo-ouro', '#FFD21F', 15), ('222', 18, 10.5, 'alto à esquerda', 'branco', '#FFFFFF', 13), ('888', 18, 46.9, 'à esquerda, na altura do ombro', 'verde-limão', '#7CFF4F', 11)],
        63: [('222', 18, 10.5, 'alto à esquerda', 'amarelo-ouro', '#FFD21F', 14), ('11:11', 82, 10.5, 'alto à direita', 'branco', '#FFFFFF', 15), ('888', 18, 46.9, 'à esquerda, na altura do ombro', 'laranja', '#FF9F1C', 11)]}


def xy(x, y):
    return f'X {round(x / 100 * 720 - 360)} · Y {round(640 - y / 100 * 1280)}'


def montar(n):
    v = VIDEOS[n]; nn = f'nora{n}'; ks = v['keys']; c = CENA[ks[0][0]]; cta = ks[-1]
    perfil = copy.deepcopy(P46['perfil']); perfil.pop('teste', None)
    caixa, caixa_fim = v['caixa']
    resp = copy.deepcopy(RESP_FACE)
    if v['tipo'] == 'volta':
        resp['insta'] = INSTA_222
    p = {
        'enxuto': True, 'imagens_titulo': f'Imagem ({c["img"]}, não gerar)',
        'perfil': perfil, 'trava_referencia': P46['trava_referencia'], 'figurino': c['roupa_cont'], 'excecao_estilo': '',
        'ocultar_bloco_agente_imagem': True,
        'roteiro': {'id': f'{nn}-DIA-1311-{v["tipo"].upper()}',
                    'titulo': f'{nn} · 13/11 (sexta-feira 13), {v["hora"]} · ' + ('o bicarbonato com vinagre, só no Face' if v['tipo'] == 'face' else 'a volta do Insta: a canela, sem data'),
                    'duracao_total': 30 if v['tipo'] == 'face' else 48,
                    'descricao_instagram': v['insta'], 'descricao_face': v['face']},
        'refs': [f'{c["img"]} em todos os takes', 'fotos dos produtos em ferramentas-painel/referencias-produtos/ (só no pré-gancho)'],
        'imagens': [{'rotulo': f'IMAGEM 1 · {c["img"]}', 'cena': '(gerada em 11/11)', 'anexar': 'nada (já existe)'}],
        'videos': [{'rotulo': ROT[k], 'cena': TXT[k], 'duracao': '10', 'primeiro_quadro': f'IMAGEM 1 ({c["img"]})', 'acao': '', 'b_roll': '',
                    'fala': F[k], 'movimentacao': mov(k), 'arquivo': nome(k)} for k in ks],
        'texto_tela': {'hook': caixa, 'hook_comeca': 'o primeiro quadro do pré-gancho', 'hook_termina': caixa_fim, 'hook_alt': '', 'extras': []},
        'comentario_fixado': {'insta': v['fix_insta'], 'face': v['fix_face']},
        'respostas_face': resp,
        'imagem_reutilizada': {'arquivo': c['img'], 'aviso': f'Use a {c["img"]} de 11/11: anexe-a no agente. Não gere imagem nova da Nora falando hoje.'},
        'story': {'ja_postado': False, 'nota': ('O story-1211 (2027) vence ~12h de 13/11: me mande os prints dele (Insta e Face) e reposte o mesmo arquivo, com o mesmo texto e o adesivo de link '
                                                 '(STORYIG no Insta; FACE no Face, botão “Saiba mais”). Ao vivo, sem programar.')},
    }
    mt = copy.deepcopy(P49['mapa_tela'])
    mt['numeros'] = [dict(t=a, x=x, y=y, onde=o, cor_nome=cn, cor=co, tamanho=tm) for (a, x, y, o, cn, co, tm) in NUMS[n]]
    linhas = caixa.split('\n')
    est = [{'nome': 'Números fixos espalhados (11:11, 888, 222)', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'uma cor para cada número', 'tamanho': 'um tamanho para cada número',
            'contorno': 'Traço preto + Sombra preta, sem Plano de fundo', 'obs': '; '.join(f'{a} {cn}, {tm}, {xy(x, y)}' for (a, x, y, o, cn, co, tm) in NUMS[n]) + '. Eu ponho (P45). O 11:11 é hora, não data: fica (aluno, 13/11).'},
           {'nome': 'Caixa do topo: ' + ' / '.join(f'“{l}”' for l in linhas), 'fonte': 'Poppins ExtraBold', 'cor': 'texto preto extra-negrito',
            'tamanho': '10, em 2 linhas', 'contorno': 'Plano de fundo AMARELO sólido (#FFD700), cantos levemente arredondados',
            'obs': 'Do 1º quadro do pré-gancho até o fim do Take 1, acima da cabeça. Alto contraste (regra de 12/11 23h25; R36). Eu ponho (P45).'},
           {'nome': 'Legenda (eu ponho, P45)', 'fonte': 'Poppins Bold', 'cor': 'branco, em MAIÚSCULAS; palavra-chave na cor do estilo', 'tamanho': 'uns 38 px (vídeo 720×1280)',
            'contorno': 'preto grosso', 'obs': 'A partir do Take 1 (no pré-gancho não), blocos de 2 a 4 palavras, abaixo do queixo.'}]
    if v['tipo'] == 'volta':
        est.append({'nome': 'Faixa do CTA, versão do INSTA: “Tap my photo: your 2027 reading is in my story”', 'fonte': 'Poppins Bold', 'cor': 'texto preto, “my story” em destaque',
                    'tamanho': '9', 'contorno': 'Plano de fundo sólido', 'obs': 'Do T05 até o fim, com a seta para a foto do perfil. No Insta o vídeo tem os 5 takes (o T04 do 222 antes do T05).'})
    est.append({'nome': 'Faixa do CTA, versão do FACE: “Your 2027 reading: link in the comments ⬇️”', 'fonte': 'Poppins Bold', 'cor': 'texto preto, “in the comments” em destaque',
                'tamanho': '9', 'contorno': 'Plano de fundo sólido', 'obs': 'Do CTA até o fim, sem seta. No Face o vídeo termina no CTA, sem o pedido do 222 (R40).'})
    if v['prova']:
        quem, trecho = PROVA[v['prova']]
        est.append({'nome': f'Avaliação real do Trustpilot: {quem} (“{trecho}”)', 'fonte': f'provas-trustpilot/{v["prova"]}-sem-hora.png (print real, sem a hora relativa)',
                    'cor': '—', 'tamanho': '~84% da largura', 'contorno': 'cantos arredondados e sombra leve',
                    'obs': 'Nos últimos ~3 s do T03, longe do rosto, com a caixa “Rated 4.8 ★ by 2,200+ people” no topo. Eu ponho (P45).'})
    mt['estilos'] = est
    mt['regras'] = ['O pré-gancho é a Nora fazendo o ritual com o produto de verdade: nada de objeto parado (regra de 13/11).',
                    'Eu ponho os textos, os números, a avaliação, o riser e o impact (P45); você monta só o vídeo e a música.']
    p['mapa_tela'] = mt
    corte = f'{nn}-cortado'
    lista = ', '.join(nome(k) for k in ks)
    p['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” só estes {len(ks)} takes, de uma vez: {lista}. Ela junta pela ordem do nome (já estão em ordem).',
        'nome': corte, 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pela ordem do nome (' + ', '.join(ROT[k] for k in ks) + ')',
        'depois': [f'Suba os {len(ks)} takes e espere a Prévia.', 'Aperte play com Resultado marcado: confira a primeira palavra do 1º take e a última do último.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', f'Clique em Cortar e baixar e salve como {corte}.']}
    pre = 'd1311-PRE-bicarbonato' if v['tipo'] == 'face' else 'd1311-PRE-canela'
    p['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {corte}', 'como': 'É o vídeo que saiu da FusionZ.'},
        {'quando': 'B. Pré-gancho no começo', 'texto': f'Os 2 vídeos do {pre}: mande os 2 para mim ANTES de montar',
         'como': 'Eu escolho o melhor, corto os ~3,5 s com mais ação e te devolvo o trecho pronto; ele entra no começo, antes do Take 1, sem música por baixo.'},
        {'quando': '1. Do Take 1 ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Começa no Take 1 (no pré-gancho, só o som dele).'},
        {'quando': '2. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'1080×1920, qualidade alta, nome {nn}-montado (acima de 30 MB, link do Drive). Eu ponho tudo e devolvo ' + (f'o {nn}-final-FACE.' if v['tipo'] == 'face' else f'o {nn}-final (Insta, com o 222) e o {nn}-final-FACE (sem o 222, com a faixa do comentário).')}]
    pecas = [{'nome': c['img'], 'de': f'{c["img"]} (de 11/11)', 'tipo': 'imagem 1', 'status': 'reutilizar', 'descricao': f'A {c["nome"]}.'},
             {'nome': f'{pre}-IMG e {pre}', 'tipo': 'pré-gancho', 'status': 'gerar', 'descricao': 'A imagem inicial (x4, 0 crédito) e o vídeo (x2) do pré-gancho, com as fotos dos produtos.'}]
    for k in ks:
        pecas.append({'nome': nome(k), 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{F[k]}”'})
    if v['prova']:
        pecas.append({'nome': 'avaliação da Katrina', 'tipo': 'prova', 'status': 'reutilizar', 'onde': 'Eu ponho na edição, nos últimos 3 s do T03. Você não faz nada.'})
    cred = 10 * len(ks) + 20
    decisao = {
        'face': [f'GERAR AGORA (contatocaram): o pré-gancho do bicarbonato (imagem x4 + vídeo x2) e os 3 takes na manha1111-IMG. Créditos: ~{cred}.',
                 'Só no Face (o Insta está em pausa até 23h20). Sexta-feira 13 na caixa e no Take 1: sai durante a sexta nos EUA.',
                 'Postar assim que ficar pronto, ao vivo; logo depois, o comentário da Página com o link. Respostas só em público (directs parados).'],
        'volta': [f'GERAR (contatocaram): o pré-gancho da canela (imagem x4 + vídeo x2) e os 5 takes na noite1111-IMG. Créditos: ~{cred}.',
                  'Sem data (à 0h a sexta-feira 13 já acabou para quem vê depois). O 222 vem antes do CTA; o story é a última frase (só no Insta; no Face o vídeo termina no CTA).',
                  'Postar à 0h00 de 13 para 14/11, ao vivo, no Insta (o nora63-final) e no Face (o nora63-final-FACE). No Insta, responder quem comentar 222 nos primeiros 30 min; no Face, o comentário da Página com o link.'],
    }[v['tipo']]
    p['pecas'] = {'lista': pecas, 'decisao': decisao, 'titulo_decisao': 'Resumo'}
    p['central'] = {'imagem_unica': True,
                    'conferir': (f'Conferir em cada take: é a Nora da {c["img"]} (rosto, lua com as 3 estrelinhas com pontas, trança, brincos, colar de Vênus, a roupa da imagem); ela fala uma vez só, '
                                 'em inglês, com os números por extenso; o braço do celular não se mexe; sem texto, legenda ou música. Renomeie com o nome da lista.'),
                    'passos': [], 'config': config(c), 'agente': agente(c, ks, cta),
                    'colagens': [{'titulo': f'{nn}: os {len(ks)} takes ({", ".join(ROT[k] for k in ks)})', 'fala': ' '.join(F[k] for k in ks),
                                  'movimentacao': [mov(k) for k in ks], 'takes': list(range(len(ks)))}]}
    p['pre_gancho'] = extras(ks[0][0])
    p['ordem'] = ['pecas', 'prehook', 'imagens', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', f'<title>Painel {nn} · dia 13/11</title>', html, count=1)
    (R / f'PAINEL-NORA{n}.html').write_text(html, encoding='utf-8')
    print('ok', nn, v['tipo'], [ROT[k] for k in ks], 'créditos ~', cred)


for n in VIDEOS:
    montar(n)
