# Painel do dia 15/11/2026: nora66, o ritual do sal Morton com a Nora falando NA MESMA CENA (Insta à 0h00 de 15 para 16/11 e o mesmo no Face, sem o hook de produto).
# Decisões: Clone R49 (opção B: bancada de cozinha, prato preto, moeda; as falas) com os meus ajustes (outra caixa, o Take 1 da pergunta curiosa, o T3 do corpo A em 2 takes);
# Clone R46 (falar na mesma cena do ritual); Clone R48 (a 2ª frase valida a rotina dela, dos 4 aos 8 s); Clone R50 (edição de alto contraste, tela limpa até o CTA);
# edição dopaminérgica aprovada pelo aluno em 15/11 03h00 (as imagens do desejo nos primeiros ~15 s, aulas 12 e 14). "pode montar" às ~03h55 de 15/11.
# Pré-gancho escrito em batidas de 0,5 s, modelado do viral 51.2 (de frente → close do produto agindo → de frente apontando), com o monte de sal (efeito que cresce
# no mesmo lugar, checklist 4) no lugar do círculo. Imagens como EDIÇÃO da d1311-PRE-canela-IMG-C (a cozinha da noite já aprovada) + a folha + a foto do Morton (lição de 14/11 20h20).
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-1511/build_dia_1511.py
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
P63 = pacote('PAINEL-NORA63.html')
CFG = copy.deepcopy(P51['central']['config'])
VOZ = [c for s in CFG for c in s['campos'] if c['campo'].startswith('Perfil de voz')][0]['copiar']
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'

ESTRELAS = ('the small flat gold crescent moon on her cheek on the left side of the frame with three tiny separate gold five-pointed stars next to it '
            '(three stars with visible points, never dots or circles)')
MORTON = ('the exact Morton Iodized Salt canister from the reference photo (a dark navy-blue cardboard cylinder with a white top and a metal pour spout, the girl in the '
          'yellow dress holding a lilac umbrella with salt pouring out, "MORTON" in big white letters and "IODIZED SALT" in yellow)')
PRATO = 'a plain round matte black ceramic plate'
MOEDA = 'one shiny gold coin'

# ------------------------------------------------------------------ a cena das falas = a d1511-PRE-sal-IMG-C (a mesma do fim do pré-gancho; R46)
SAL = dict(
    img='d1511-PRE-sal-IMG-C', nome='a cozinha da noite, de frente, com o Morton na mão',
    roupa_cont='her plain black fitted square-neck tank top with wide straps',
    quando='at night', onde='a real, lived-in American kitchen', luz='lit only by a warm pendant lamp above the counter',
    fundo='the dark kitchen cabinets, the pendant lamp and the wooden counter behind and around her', visual='warm pendant lamp light in a dark kitchen')
SEGURA = ('the hand that holds the Morton salt canister keeps it still at chest height, label facing the camera, in exactly the same position and angle as in the reference image, '
          'the whole time; the canister never moves, never turns and its label never changes; the black plate with the white salt mound and the gold coin on top stays still on the '
          'counter in the lower part of the frame')

# ------------------------------------------------------------------ falas (R49 + os meus ajustes; até 22 palavras; números por extenso)
F = {
    'S1': "Have you ever wondered why wise women pour salt before sleeping? It clears the heavy energy blocking your blessings.",
    'S2': "You spent months smiling for everyone while carrying heavy worry alone in bed, quietly wondering when your turn would arrive.",
    'S3': "The universe saw your quiet faith. A major turnaround is arriving, bringing unexpected money, deep peace, and someone truly wonderful.",
    'S4': "The worst is behind you. Heavy doors that stayed locked all year are finally opening to welcome your abundance.",
    'S5': "Comment two two two below to welcome this gentle blessing.",
    'S6': "Tap my photo and answer three quick questions in my story to get your reading for twenty twenty-seven.",
    'S7': "For your personal reading, look in the comments below to see what twenty twenty-seven holds for you.",
}
RESERVA = {
    'S1': "If you feel quietly exhausted by financial stress tonight, this simple salt ritual marks where your new chapter begins.",
    'S6': "Tap my photo for the quick reading in my story about twenty twenty-seven.",  # passou no nora63 e no nora65
    'S7': "If this found you today, it's not by chance. Look in the comments below to see what twenty twenty-seven holds for you.",
}
SUF = {'S1': 'T01-pergunta-sal', 'S2': 'T02-sorrindo-para-todos', 'S3': 'T03-fe-silenciosa', 'S4': 'T04-portas-abrindo', 'S5': 'T05-comente-222',
       'S6': 'T06-cta-story-2027', 'S7': 'T07-face-cta-comentarios-2027'}
ROT = {'S1': 'T01', 'S2': 'T02', 'S3': 'T03', 'S4': 'T04', 'S5': 'T05', 'S6': 'T06', 'S7': 'T07'}
TXT = {'S1': 'o Take 1: a pergunta curiosa do sal antes de dormir (R49, opção 2)',
       'S2': 'a 2ª frase: valida o cansaço dela (sorrir para todos, carregar a preocupação sozinha; R48 e R49)',
       'S3': 'o corpo A, 1ª parte: a fé silenciosa vista + a virada (dinheiro, paz, alguém especial)',
       'S4': 'o corpo A, 2ª parte: o pior passou + as portas abrindo',
       'S5': 'o pedido do 222, antes do CTA (só no Insta; R40)',
       'S6': 'o CTA do story: foto, three quick questions, a leitura de 2027 (só no Insta; a última frase; R49)',
       'S7': 'o CTA só da versão do FACE: os comentários + 2027 (no lugar do T05 e do T06)'}


def nome(k):
    return f'd1511-{SUF[k]}'


GESTO = {
    'S1': 'during the first half of the take her eyebrows lift with a curious, knowing look, in the closing half a small warm smile appears and she gives one slow nod',
    'S2': 'during the first half of the take she holds a soft, understanding look with her head tilted slightly, in the closing half a gentle reassuring smile appears',
    'S3': 'during the first half of the take she holds a calm, tender look, in the closing half her eyes brighten with a warm smile',
    'S4': 'during the first half of the take she holds a calm, confident look, in the closing half a relieved smile appears and she gives one small nod',
    'S5': 'during the first half of the take she holds an encouraging look, in the closing half she gives one small inviting nod with a bright smile',
}


def mov(k):
    g = GESTO.get(k, 'during the first half of the take she holds a warm, confident look, and in the closing half she gives one small encouraging nod with a warm smile')
    return (f'Throughout the whole 10 seconds the camera stays static at chest height in front of her with an unchanged framing; {SEGURA}; her other hand rests on the edge of the '
            f'counter and never moves; her eyes stay on the lens; {g}; only her face moves, never her hands; from the end of the final sentence of the take until the clip ends she '
            'keeps her lips closed and silent; no zoom and no cuts, the braid stays in place, everything else in the kitchen stays still and each hand has exactly five fingers.')


COMUNS = {('of', 'the'), ('and', 'the'), ('to', 'the'), ('in', 'the'), ('on', 'the'), ('at', 'the'), ('for', 'a'), ('of', 'her'), ('and', 'her'),
          ('as', 'if'), ('the', 'lens'), ('and', 'then'), ('the', 'hand'), ('she', 'gives'), ('the', 'height'), ('a', 'warm'), ('with', 'a'),
          ('the', 'whole'), ('a', 'small'), ('for', 'the'), ('the', 'salt'), ('the', 'counter')}
for k, f in list(F.items()) + [(k + 'r', v) for k, v in RESERVA.items()]:
    assert len(f.split()) <= 22, (k, len(f.split()))
    fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(k[:2]).lower())
    sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS
    assert not sobra, (k, sobra)
    for w in ('private', 'card', 'tarot', 'link', 'free', 'portal', 'claim', 'lock in', 'receive', 'secret'):
        assert w not in f.lower(), (k, w)


def livre(c):
    return (f'Casual real video {c["quando"]} in {c["onde"]}, filmed from a static camera standing on the counter at her chest height, looking exactly like a real phone video, '
            f'{c["luz"]}. CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, the thin braid wrapped with small gold rings, {ESTRELAS}, her star-and-moon '
            f'drop earrings, her thin gold Venus necklace, the thin gold bracelets and the gold sun ring, {c["roupa_cont"]}, the Morton salt canister in her hand and the black plate '
            'with the white salt mound and the gold coin stay exactly as in the reference image; the framing is exactly the one of the reference image, from the chest up, her face in '
            f'the upper middle of the frame; {SEGURA}; her other hand rests on the edge of the counter; {c["fundo"]} stay exactly where they are; natural skin texture with visible '
            'pores, slight phone grain, everything in focus, no bokeh, no filter, no glow and no sparkles; the camera is static, no zoom, no cuts and no reframing; no phone, phone '
            'stand, tripod, object, person, animal or text appears or disappears; the canister label stays exactly as in the reference image; each hand always has exactly five '
            'fingers; no on-screen text, no captions; real quiet kitchen ambient sound only, no music. SPEECH RULE for every take: she says only the exact words of that take\'s '
            'script, each word exactly once and in order, with no repeated word, no extra word and no added sentence before, between or after; numbers are spoken as words ("two two '
            'two" as three separate words, twenty twenty-seven exactly as written); when she finishes the last word she closes her lips, stays silent and keeps a calm still '
            'expression until the clip ends.')


def prompt_manual(c, fala, movimento):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image stands behind her kitchen '
            f'counter {c["quando"]} and speaks directly to the camera.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + fala + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            'VOICE PACING: medium pace (155 to 180 words per minute), about 8 seconds of speech; when she finishes the last word she closes her lips and stays silent '
            'with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + movimento + '\n\n'
            f'VISUAL: realistic casual phone video, {c["visual"]}, natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter.\n\n'
            'CAMERA: static at chest height, no zoom, no cuts, no reframing.\n\n'
            'AUDIO: only her voice and quiet kitchen ambience; no music, no other voices, no sound effects.\n\n'
            f'CONTINUITY: her face, long black wavy hair, the thin braid with small gold rings, {ESTRELAS}, her star-and-moon earrings, her gold Venus necklace, her gold sun ring and '
            f'bracelets, {c["roupa_cont"]}, the Morton salt canister with its label, the black plate with the salt mound and the gold coin, and the kitchen behind her stay exactly as '
            'in the reference image; no phone, object, person or text appears; each hand has exactly five fingers; no on-screen text or captions.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.')


def config(c):
    cf = copy.deepcopy(CFG)
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = f'colar o texto abaixo (fechado pela {c["img"]}, a imagem C do pré-gancho)'
                campo['copiar'] = livre(c)
            elif campo['campo'] == 'Movimento de câmera':
                campo['valor'] = 'Estático / câmera parada, sem zoom (se essa opção não existir: Handheld sutil, sem zoom; o LIVRE já diz câmera parada)'
            elif campo['campo'] == 'Estilo visual':
                campo['valor'] = 'UGC moderno (a câmera parada no balcão; o LIVRE descreve)'
    return cf


PRE_LUCAS = ('Below, you will find several prompts, each corresponding to a different video. Please generate all the videos in sequential order, from the first prompt to the last.\n'
             'Maintain the exact same voice across all videos, ensuring EXACTLY THE SAME VOLUME, with no variations in background, intonation, or vocal clarity. Use the attached image as both the first and last frame of every generated video.\n'
             'Please submit ALL generation requests at once and in the correct order, so that all videos can be generated simultaneously.\n'
             'If the generation of any video fails, please resubmit ONLY the item that failed until it is successfully generated.')


def agente(c, ks):
    nomes = [f'{i + 1} = {nome(k)}' for i, k in enumerate(ks)]
    return {
        'imagem': c['img'],
        'intro': 'Anexe a imagem, cole o aviso e, embaixo dele, o bloco “COPIAR TUDO JUNTO” da Central.',
        'aviso_tag': 'cole antes do bloco da Central',
        'aviso': (f'Vou te enviar {len(ks)} prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um com o devido '
                  'número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.'),
        'passos': [
            'Conta do Flow: a que tiver ~120 créditos (me diga o saldo das 4). Abra um PROJETO NOVO no Flow e uma conversa nova no agente.',
            'Nas configurações do agente: Omni 1.2 Flash · 360p · 10 s · 9:16 (10 créditos por take) e gerar sem pedir aprovação. Depois, BAIXE cada take em 720p (não gasta crédito).',
            f'Anexe só a {c["img"]} (a imagem C do pré-gancho, a escolhida).',
            'Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.',
            'Renomeie cada take com o nome da lista (o número é a ordem): ' + ' · '.join(nomes) + '. '
            'Se ele não renomear, mande na mesma conversa: “Now rename each video with the correct number from the prompt.”',
            f'Confira na grade, pelo nome, se os {len(ks)} saíram; se o pote do Morton continua parado na mão, com o rótulo igual; se o prato com o monte de sal e a moeda continua no balcão; '
            'e se a lua no rosto tem as 3 estrelinhas. Se um falhar por política: mande na mesma conversa “Please generate video X from my previous message again, with the same prompt.” '
            '(X = o número dele na lista). Se falhar de novo, não insista: me mande o print.',
            f'Se o T06 (o CTA do Insta) falhar 2 vezes, gere à mão: Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; Início = {c["img"]}; Fim = vazio; cole o prompt abaixo, '
            f'inteiro (10 créditos), e renomeie para {nome("S6")}. PROMPT: ' + prompt_manual(c, F['S6'], mov('S6')),
            'Se falhar também no Frames: o mesmo caminho com a fala reserva (a que passou no nora63 e no nora65) e o mesmo nome. PROMPT RESERVA: ' + prompt_manual(c, RESERVA['S6'], mov('S6')),
            f'Se o T07 (o CTA do Face) falhar 2 vezes: o mesmo caminho à mão (10 créditos), renomeado para {nome("S7")}. PROMPT: ' + prompt_manual(c, F['S7'], mov('S7'))
            + ' · RESERVA: ' + prompt_manual(c, RESERVA['S7'], mov('S7')),
            f'Se o T01 falhar 2 vezes: à mão, com a fala reserva (a outra opção do Clone), renomeado para {nome("S1")}. PROMPT: ' + prompt_manual(c, RESERVA['S1'], mov('S1')),
            'Se o agente parar no meio (por exemplo, “alta demanda”): responda na MESMA conversa, sem anexar nada: “Please continue and generate videos X to Y from my previous message, in the same order.” '
            '(troque X e Y pelos números que faltaram). Se ele gerar só o 1º e parar de novo: cole antes do bloco da Central o “pré-prompt do Lucas” (abaixo) e mande de novo só os que faltaram.',
            'Se o agente disser que não dá para usar a imagem como quadro inicial e final com fala: gere à mão: Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; '
            f'Início = {c["img"]}; Fim = vazio; no prompt, só o texto do prompt daquele take.',
            'Pré-prompt do Lucas (só se precisar): ' + PRE_LUCAS,
        ],
    }


# ------------------------------------------------------------------ pré-gancho: 3 imagens (edição da cozinha aprovada) + 4 vídeos de 5 s, uma ação em cada
_NORA = ('the first image is the approved photo of the woman in her kitchen at night (keep exactly her face, her long black wavy hair, the thin braid with small gold rings, '
         'the small flat gold crescent moon with three tiny gold stars on her cheek, her star-and-moon earrings, her gold Venus necklace, the thin gold bracelets, the gold sun ring '
         'and her plain black fitted square-neck tank top with wide straps; keep the same kitchen: the wooden counter, the dark cabinets and the warm pendant lamp above); the second '
         'image is her character sheet (same woman, same face); the third image is the real Morton Iodized Salt canister. Same woman, same face, same kitchen and same light: change '
         'only the objects and the pose. ')
_FIM_IMG = ('looks exactly like a real casual iPhone photo at night, warm light, slight phone grain, natural colors, everything in focus, no bokeh, no dark or gloomy mood; the only '
            'text in the image is the real label of the canister from the reference photo, sharp and legible, never changed; no other text, no logo, no watermark; no phone, phone '
            'stand or tripod anywhere in the image; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16')
TOPO = 'the upper 18 percent of the image is plain dark cabinets with nothing in it; '

IMGS = [
    ('A', 'o pote inclinado sobre o prato preto vazio (plano médio)',
     _NORA + 'RAW photo taken from about 70 centimeters in front of her, at chest height: she stands behind the wooden counter, framed from the waist up, centered; in one hand she '
     f'holds {MORTON} tilted right above {PRATO} that lies empty on the counter in the lower middle of the image, the metal spout open and pointing down at the plate, label facing '
     f'the camera; {MOEDA} lies on the counter next to the plate; her other hand rests flat on the counter; she looks down at the plate with a focused, calm expression; ' + TOPO + _FIM_IMG),
    ('B', 'o prato de perto: o monte de sal branco e a moeda na ponta dos dedos',
     _NORA + f'close-up from above at a slight angle of {PRATO} on the wooden counter filling the lower two thirds of the image: a small heap of fine white salt sits in the center '
     f'of the black plate; at the top edge of the image the metal spout of {MORTON} is tilted above the heap, label partly visible; her other hand, with the thin gold bracelets '
     f'and the gold sun ring, holds {MOEDA} between two fingers about ten centimeters above the heap; the edge of her black tank top and the warm kitchen are behind; ' + _FIM_IMG),
    ('C', 'de frente, com o Morton na mão e o prato com o monte e a moeda (é a imagem das falas)',
     _NORA + 'RAW photo taken from about 70 centimeters in front of her, at chest height: closer framing from the chest up, her face in the upper middle of the image, looking '
     f'straight into the camera with a warm, knowing smile and her lips closed; one hand holds {MORTON} still at chest height, a little to the side of her body, label facing the '
     f'camera, never covering her face, mouth or chin; her other hand rests on the edge of the counter; in the lower part of the image, on the counter in front of her, {PRATO} '
     f'with a tall white mound of salt in the center and {MOEDA} on top of the mound; ' + TOPO + _FIM_IMG),
]


def _vid(acao, som, trava):
    return ('Use the supplied image as the first frame. Real casual video at night from a static camera at chest height, steady, no zoom, real speed, no slow motion; no phone, '
            f'phone stand or tripod ever appears in the frame. The action starts in the very first frame: {acao} Then everything holds still until the clip ends. {trava} The label '
            'of the canister stays exactly as in the first frame, sharp and unchanged; each hand has exactly five fingers; nothing else appears or disappears. AUDIO: close ASMR '
            f'kitchen sounds only: {som}; no music, no voice, she does not speak and her lips stay closed. No on-screen text, no captions.')


_TS = 'She keeps the same face, braid, crescent moon with three tiny gold stars, earrings, necklace and black tank top the whole time.'
_TH = 'Her hand keeps the thin gold bracelets and the gold sun ring the whole time.'
VIDS = [
    ('1-derrama', 'A', 'o sal já caindo do bico no prato preto',
     _vid('a thick steady stream of white salt is already pouring from the metal spout onto the black plate and piles up into a growing white mound in the center of the plate, '
          'bright white against the black, while she keeps the canister tilted.', 'the salt pouring and hissing onto the plate', _TS)),
    ('2-monte', 'B', 'o monte de sal crescendo no prato (de perto)',
     _vid('the stream of salt keeps falling from the spout onto the heap and the white mound swells fast and tall in the center of the black plate, grains bouncing on the black '
          'surface, in three dimensions, never as a ribbon or a wave.', 'a close hiss of salt falling on the heap', _TH)),
    ('3-moeda', 'B', 'a moeda dourada caindo no topo do monte',
     _vid('she lets go of the gold coin and it drops onto the top of the salt mound with a bright clink, a little puff of salt jumps up around it and the coin settles shining on '
          'top of the mound.', 'one bright clink of the coin and a soft puff of salt', _TH)),
    ('4-aponta', 'C', 'ela aponta para a lente com um sorriso de quem sabe',
     _vid('with her free hand she points her index finger straight at the lens with a warm, knowing smile, and holds the point, while the other hand keeps the canister still at '
          'chest height.', 'a quiet kitchen hum and one soft tap of her fingertip in the air', _TS)),
]

# ------------------------------------------------------------------ imagens do desejo (edição dopaminérgica aprovada em 15/11 03h00; 0 crédito; sem rosto reconhecível, sem texto)
_DES_FIM = ('RAW photo, looks exactly like a real casual iPhone photo, natural colors, slight phone grain, everything in focus, no bokeh, no filter; no recognizable face (faces out '
            'of frame, from behind or turned away); no text, no logo, no watermark, no readable signs; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16')
DESEJO = [
    ('1-sal-ao-lado-da-cama', 'T01: o sal antes de dormir',
     'a small white ceramic bowl filled with coarse white salt on a wooden nightstand next to a softly glowing bedside lamp, a neatly made bed with cream linen behind it, a calm '
     'cozy real American bedroom at night, warm golden lamp light, peaceful mood; ' + _DES_FIM),
    ('2-sorrindo-para-todos', 'T02: sorrir para todos',
     'overhead view of a warm family dinner table at night: several hands passing bowls of food and filling glasses, a woman\'s hand with a thin gold bracelet serving everyone, '
     'plates, a candle and a bread basket, faces out of frame, real American home, warm cozy light; ' + _DES_FIM),
    ('3-sozinha-na-cama', 'T02: a preocupação sozinha na cama',
     'a woman in her forties with long dark wavy hair seen from behind, sitting alone on the edge of her bed at night, shoulders slightly tired, her hands resting in her lap, a '
     'warm bedside lamp beside her, quiet and tender mood, not sad or scary, her face not visible; ' + _DES_FIM),
    ('4-dinheiro-no-envelope', 'T03: o dinheiro inesperado (SÓ no Insta: nota de dinheiro não vai no Face)',
     'a woman\'s hands with a thin gold bracelet opening a white envelope on a sunny kitchen table, revealing a few crisp hundred-dollar bills, a coffee mug and soft morning light, '
     'warm and hopeful mood, real American home; ' + _DES_FIM),
    ('5-paz-na-varanda', 'T03: a paz',
     'a woman in her forties with long dark wavy hair seen from behind, wrapped in a soft cream cardigan, sitting on a wooden porch at sunrise holding a mug, golden light over a '
     'quiet green lawn, deep calm and relief, her face not visible; ' + _DES_FIM),
    ('6-casal-na-praia', 'T03: alguém maravilhoso',
     'a happy middle-aged couple seen from behind walking hand in hand on a quiet beach at golden sunset, gentle waves, warm light, romantic and peaceful, faces not visible; ' + _DES_FIM),
    ('7-porta-abrindo', 'T04: as portas abrindo',
     'a bright wooden front door of a cozy home swinging wide open from the inside onto a sunlit garden path with flowers, warm golden morning light pouring into the entryway, '
     'hopeful mood, nobody in the image; ' + _DES_FIM),
]


def pre_gancho():
    base, prod = 'd1511-PRE-sal', 'morton-iodized-salt-frente.jpg'
    etapas = []
    for letra, desc, prompt in IMGS:
        usa = ', '.join(v[0] for v in VIDS if v[1] == letra) + (' e TODOS os takes (T01 a T07)' if letra == 'C' else '')
        etapas.append({'titulo': f'Imagem {letra}: {desc}', 'nome': f'{base}-IMG-{letra}', 'tipo': 'img',
                       'anexar': '1º a d1311-PRE-canela-IMG-C (a cozinha da noite de 13/11, já aprovada); 2º a folha da Nora (1K); 3º a foto do Morton (' + prod + ', que eu te mando)',
                       'quadros': (f'x4, 0 crédito. Serve para: {usa}. Escolha a que tiver: é a Nora (o rosto da canela, lua com as 3 estrelinhas, trança com anéis); o rótulo do '
                                   'Morton IGUAL ao da foto (a menina de amarelo com o guarda-chuva, "MORTON" branco, "IODIZED SALT" amarelo, sem letra trocada); o prato preto; '
                                   '5 dedos em cada mão; nenhum celular ou tripé no quadro. Não precisa olhar de que lado está a mão. Se o Flow recusar pelo nome da marca, apague '
                                   f'"Morton" do texto e deixe só a foto anexada. Renomeie para {base}-IMG-{letra}.' + (' ME MANDE AS 4 DA IMAGEM C antes dos takes (é a imagem das falas).' if letra == 'C' else '')),
                       'prompt': prompt})
    for suf, letra, desc, prompt in VIDS:
        n = f'{base}-{suf}'
        etapas.append({'titulo': f'Vídeo {suf.split("-")[0]}: {desc}', 'nome': n, 'tipo': 'vid', 'duracao': 5,
                       'quadros': (f'Omni 1.2 Flash · 360p · 5 s · x2 (~10 créditos). Início = {base}-IMG-{letra}; Fim = vazio (nunca a imagem final: a IA trava). '
                                   f'Baixe os 2 em 720p e renomeie {n}-a e {n}-b.'),
                       'prompt': prompt})
    for suf, desc, prompt in DESEJO:
        n = f'd1511-DESEJO-{suf}'
        etapas.append({'titulo': f'Imagem do desejo: {desc}', 'nome': n, 'tipo': 'img', 'anexar': 'NADA (imagem sem a Nora)',
                       'quadros': f'x4, 0 crédito. Escolha a mais bonita e real, sem rosto aparecendo, sem texto e com 5 dedos. Renomeie para {n} e me mande junto com o montado.',
                       'prompt': prompt})
    return {
        'titulo_secao': 'Pré-gancho e imagens do desejo (Flow, à mão, antes dos takes)',
        'conceito': ('O sal Morton (opção B do Clone R49), modelado do viral 51.2 (de frente → close do produto agindo → de frente apontando), em batidas de 0,5 s: '
                     '0–0,5 s o sal já caindo do bico no prato preto · 0,5–1,0 o monte branco crescendo · 1,0–1,5 o close do monte inchando · 1,5–2,0 a moeda dourada caindo no topo '
                     '(clink) · 2,0–2,5 a moeda brilhando no monte · 2,5–3,8 a Nora de frente, com o pote na mão, aponta para a lente; e ela fala na MESMA cena, na imagem C (R46). '
                     'O monte (efeito que cresce no mesmo lugar) no lugar do círculo, que a IA desenha mal. Eu corto ~0,8 s de cada vídeo, junto ~3,8 s e ponho o riser e o impact. '
                     'Depois, as 7 imagens do desejo (0 crédito) que eu ponho nos primeiros ~15 s, uma por frase (o teste da edição dopaminérgica).'),
        'modo': ('Imagens: Flow → Imagem · 9:16 · Nano Banana Pro · x4, anexando as referências na ordem (0 crédito). Vídeos: Flow → Vídeo → Frames → 9:16 → Omni 1.2 Flash → '
                 '360p → 5 s → x2; Início = a imagem indicada; Fim = vazio. Dá para mandar todos de uma vez. Baixe em 720p e me mande todos, sem cortar.'),
        'etapas': etapas,
    }


# ------------------------------------------------------------------ montar o painel
RESP_FACE = copy.deepcopy(P63['respostas_face']); RESP_FACE['insta'] = []
INSTA_222 = ['Welcome ✨ your 2027 reading is waiting in my story 🔮', 'I see you 💛 tap my photo, your next step is in my story',
             'This blessing is yours ✨ check my story before you go', 'So glad this found you 💫 tap my photo for your reading', 'Sending you peace tonight 🌙 your reading is in my story']
CAIXA = 'FOR WOMEN WHO GIVE TOO MUCH:\nTHE MORTON SALT SHIFT'


def montar():
    c = SAL; ks = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7']; nn = 'nora66'
    perfil = copy.deepcopy(P46['perfil']); perfil.pop('teste', None)
    p = {
        'enxuto': True, 'imagens_titulo': 'Imagem das falas (a d1511-PRE-sal-IMG-C, gerada no pré-gancho)',
        'perfil': perfil, 'trava_referencia': P46['trava_referencia'], 'figurino': c['roupa_cont'], 'excecao_estilo': '',
        'ocultar_bloco_agente_imagem': True,
        'roteiro': {'id': f'{nn}-SAL-1511',
                    'titulo': f'{nn} · 15/11, Insta à 0h00 (de 15 para 16/11) e o mesmo no Face · o ritual do sal Morton, a Nora falando na mesma cena (R46, R49)',
                    'duracao_total': 46,
                    'descricao_instagram': ('Have you ever wondered why wise women pour salt before sleeping? ✨\nYour private reading is waiting in my story 🔮\n'
                                            'Comment "222" to welcome this blessing ✨\n#manifestation #saltritual #lawofattraction #abundance #2027'),
                    'descricao_face': ('Have you ever wondered why wise women pour salt before sleeping? ✨\nSee what 2027 holds for you: the link is in the comments 🔮\n'
                                       '#manifestation #saltritual #lawofattraction #abundance #2027')},
        'refs': ['d1311-PRE-canela-IMG-C + a folha da Nora + a foto do Morton nas 3 imagens do pré-gancho', 'd1511-PRE-sal-IMG-C em todos os takes'],
        'imagens': [{'rotulo': 'IMAGEM 1 · d1511-PRE-sal-IMG-C', 'cena': '(gerada no pré-gancho, a imagem C)', 'anexar': 'nada aqui (ela sai no pré-gancho)'}],
        'videos': [{'rotulo': ROT[k], 'cena': TXT[k], 'duracao': '10', 'primeiro_quadro': 'IMAGEM 1 (d1511-PRE-sal-IMG-C)', 'acao': '', 'b_roll': '',
                    'fala': F[k], 'movimentacao': mov(k), 'arquivo': nome(k)} for k in ks],
        'texto_tela': {'hook': CAIXA, 'hook_comeca': 'o primeiro quadro do pré-gancho', 'hook_termina': 'blocking your blessings.', 'hook_alt': '', 'extras': []},
        'comentario_fixado': {'insta': 'Tap my profile picture above to see what 2027 holds for you in my stories ✨',
                              'face': f'Your 2027 reading is right here 🔮 👉 {FB}'},
        'respostas_face': dict(RESP_FACE, insta=INSTA_222),
        'story': {'ja_postado': False, 'nota': ('O story-1211 vence ~18h56 de 15/11: reposte o mesmo arquivo ANTES disso (Insta com o STORYIG; Face com o FACE, botão “Saiba mais”), '
                                                 'ao vivo, e me mande os prints dele antes de repostar. Hoje à 0h não precisa de story novo.')},
    }
    mt = copy.deepcopy(P49['mapa_tela'])
    mt['numeros'] = [dict(t='888', x=18, y=10.5, onde='alto à esquerda', cor_nome='azul ciano', cor='#3DE0FF', tamanho=13),
                     dict(t='11:11', x=82, y=10.5, onde='alto à direita', cor_nome='branco', cor='#FFFFFF', tamanho=14),
                     dict(t='222', x=18, y=46.9, onde='à esquerda, na altura do ombro', cor_nome='amarelo', cor='#FFD21F', tamanho=11)]
    mt['estilos'] = [
        {'nome': 'Caixa do topo: “FOR WOMEN WHO GIVE TOO MUCH:” / “THE MORTON SALT SHIFT”', 'fonte': 'Poppins Bold', 'cor': 'texto PRETO em negrito',
         'tamanho': '11, em 2 linhas', 'contorno': 'Plano de fundo AMARELO sólido (o modelo do Clone R50)',
         'obs': 'Do 1º quadro do pré-gancho até o fim do Take 1. No pré-gancho, só ela na tela (sem legenda). Eu ponho (P45).'},
        {'nome': 'Legenda (eu ponho, P45)', 'fonte': 'Poppins Bold', 'cor': 'branca, MAIÚSCULAS; palavras-chave em amarelo forte', 'tamanho': '38 px, 3 palavras por vez',
         'contorno': 'preto grosso', 'obs': 'Entra quando a Nora começa a falar o Take 1 (no pré-gancho não; Clone R50).'},
        {'nome': 'Imagens do desejo (o teste da edição dopaminérgica)', 'fonte': 'd1511-DESEJO-1 a 7', 'cor': '—', 'tamanho': 'tela cheia ou dividida, ~1,5 a 2 s cada',
         'contorno': 'entrada com fade e um whoosh curto', 'obs': 'Uma por frase nos primeiros ~15 s (T01 a T03; a porta no T04). O dinheiro só no Insta. A legenda continua por cima. Eu ponho.'},
        {'nome': 'Faixas do CTA', 'fonte': 'Poppins Bold', 'cor': 'caixa branca, texto preto, o destaque em vermelho', 'tamanho': '10', 'contorno': 'Plano de fundo sólido',
         'obs': 'Insta: “Tap my photo: your 2027 reading is in my story” + seta vermelha, do T06 ao fim. Face: “Your 2027 reading: link in the comments”, do T07 ao fim. Eu ponho.'}]
    mt['regras'] = ['Tela limpa até o CTA: sem avaliação do Trustpilot no meio (Clone R50).',
                    'O pré-gancho e as falas na MESMA cozinha (R46): nada de corte para outra cena.',
                    'Eu ponho os textos, os números, as imagens do desejo, o riser e o impact (P45); você monta só o vídeo e a música.']
    p['mapa_tela'] = mt
    corte = f'{nn}-cortado'
    p['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” só os {len(ks)} takes, de uma vez: ' + ', '.join(nome(k) for k in ks) + '. O T07 (o CTA do Face) fica no fim: eu separo as 2 versões.',
        'nome': corte, 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pela ordem do nome (T01 a T07)',
        'depois': [f'Suba os {len(ks)} takes e espere a Prévia.', 'Aperte play com Resultado marcado: confira a primeira palavra do T01 e a última do T07.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', f'Clique em Cortar e baixar e salve como {corte}.']}
    p['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {corte}', 'como': 'É o vídeo que saiu da FusionZ. Começa direto no T01.'},
        {'quando': 'B. Pré-gancho e imagens do desejo: NÃO põe no CapCut', 'texto': 'Os 4 vídeos do pré-gancho (d1511-PRE-sal-…, -a e -b) e as 7 imagens do desejo: mande todos para mim junto com o montado',
         'como': 'Eu corto ~0,8 s de cada vídeo, junto o pré-gancho (~3,8 s) antes do T01 com o riser e o impact, e ponho as imagens do desejo nos primeiros ~15 s.'},
        {'quando': '1. Do T01 ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Começa no 1º quadro do montado.'},
        {'quando': '2. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'1080×1920, nome {nn}-montado (acima de 30 MB, link do Drive). Eu devolvo o {nn}-final (Insta: pré-gancho + T01 a T06) e o {nn}-final-FACE (abre direto no T01, sem o pré-gancho do produto, T01 a T04 + o T07).'}]
    pecas = [{'nome': 'd1511-PRE-sal-IMG-A, B e C', 'tipo': 'imagens (pré-gancho; a C é a das falas)', 'status': 'gerar',
              'descricao': 'Edição da cozinha da canela (d1311-PRE-canela-IMG-C) + a folha + a foto do Morton. x4 cada, 0 crédito.'},
             {'nome': 'd1511-PRE-sal-1 a 4', 'tipo': 'pré-gancho', 'status': 'gerar', 'creditos': 40,
              'descricao': '4 vídeos de 5 s, uma ação em cada (o sal caindo, o monte crescendo, a moeda caindo, ela apontando), x2.'},
             {'nome': 'd1511-DESEJO-1 a 7', 'tipo': 'imagens do desejo', 'status': 'gerar', 'descricao': '7 imagens sem a Nora (x4 cada, 0 crédito) para a edição dopaminérgica.'}]
    pecas += [{'nome': nome(k), 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{F[k]}”'} for k in ks]
    p['pecas'] = {'titulo_decisao': 'Resumo', 'lista': pecas, 'decisao': [
        'GERAR (na conta com ~120 créditos; me diga o saldo das 4): as 3 imagens do pré-gancho (0 crédito) e ME MANDE AS 4 OPÇÕES DA IMAGEM C; depois os 4 vídeos do pré-gancho (~40), '
        'as 7 imagens do desejo (0) e os 7 takes na imagem C pelo agente (~70). Total: ~110 créditos.',
        'O vídeo testa a edição dopaminérgica: as imagens do desejo nos primeiros ~15 s (hipótese: segura mais gente aos 5 e aos 10 s que o nora63, ~25% e ~10%). Edição no modelo de alto contraste do Clone.',
        'Postar à 0h00 de 15 para 16/11, ao vivo: Insta (o nora66-final, com o 222 antes do story) e Face (o nora66-final-FACE, que abre direto na Nora falando). No Face, logo depois, o comentário da Página com o link, '
        'tirando a prévia e fixando pelo celular. No Insta, responder quem comentar 222.']}
    p['central'] = {'imagem_unica': True,
                    'conferir': ('Conferir em cada take: é a Nora da imagem C (rosto, lua com as 3 estrelinhas, trança, brincos, colar de Vênus, regata preta); o pote do Morton continua parado na mão, '
                                 'com o rótulo igual; o prato com o monte de sal e a moeda continua no balcão; ela fala uma vez só, em inglês, com os números por extenso; a câmera não se mexe. '
                                 'Renomeie com o nome da lista.'),
                    'passos': [], 'config': config(c), 'agente': agente(c, ks),
                    'colagens': [{'titulo': f'{nn}: os {len(ks)} takes (T01 a T07)', 'fala': ' '.join(F[k] for k in ks), 'movimentacao': [mov(k) for k in ks], 'takes': list(range(len(ks)))}]}
    p['pre_gancho'] = pre_gancho()
    p['ordem'] = ['pecas', 'prehook', 'imagens', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', f'<title>Painel {nn} · dia 15/11</title>', html, count=1)
    (R / f'PAINEL-NORA66.html').write_text(html, encoding='utf-8')
    print('ok', nn, [ROT[k] for k in ks], 'créditos ~110')


montar()
