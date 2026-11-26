# Painéis do dia 26/11/2026 (decisão do aluno, ~16h00): 3 falados, sem curto, às 17h30, 21h00 e 00h30, no Insta e no Face.
# 26/11 18h50 (o aluno, indo treinar): o nora81 passa para quando ficar pronto, na noite de 26/11, com o story novo; o nora82 (o teste) vai às 17h de 27/11.
#   "o teste é 1 por dia, o resto é usar o que vem dando certo (letra + corpo da maioria)"; "mudar o cenario, a roupa, pra nao ficar repetido";
#   "priorizar manter a copy toda, igual da maioria, só mudar uma palavra ou frase, se fizer sentido com as dicas".
# O que deu certo: as letras do nome + o corpo da maioria (nora76-FACE 4.516 views, nora77-FACE 3.625; a mineração de 26/11: as letras em 3 contas).
#   nora80 (17h30): no carro, blusa preta de manga comprida, a ametista nas mãos (o m03 da @beverly.earhart: as letras + o corpo A no carro, com a bandeira).
#   nora81 (21h00): à mesa, suéter creme, uma carta de tarô (o verso) na mão, a estátua de São Miguel (o m06 e o m11).
#   nora82 (00h30): o TESTE DO DIA (a 2ª frase como pico, do m11: "You're about to experience the luckiest days of your entire life. Are you ready?"),
#     no quarto, blusa verde-escura de tricô, uma caneca de chá nas mãos. Os outros 2 são o controle (a 2ª frase da receita, a mulher deitada).
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2611/build_dia_2611.py
import json, copy, re, pathlib, importlib.util

R = pathlib.Path(__file__).resolve().parents[2]


def _mod(nome, rel):
    s = importlib.util.spec_from_file_location(nome, R / rel)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


B23 = _mod('b2311', 'ferramentas-painel/dia-2311/build_dia_2311.py')
B24 = _mod('b2411', 'ferramentas-painel/dia-2411/build_dia_2411.py')
B, VC, FB, COMUNS, MODELO, VOZ = B23.B, B23.VC, B23.FB, B23.COMUNS, B23.MODELO, B23.VOZ
assert FB.endswith('&aff=dl7zx6ks')

IMG_BASE = 'd2511-cozinha-IMG-T02'   # a Nora v3 (sem a pintura, olhos castanhos), a do nora79
FOLHA = 'nora-v3-blueprint'
ROSTO = B23.ROSTO.replace('her face with clean natural skin', 'her face with clean natural skin, her warm medium-brown eyes (exactly the same eye color in every '
                          'clip, never green, hazel, gray, blue, amber or black)')
FIM = ('looks exactly like a real casual iPhone photo, slight phone grain, natural colors, everything in focus, no bokeh; no glow, no sparkle, no light effect; no phone, '
       'phone stand or tripod anywhere in the image; no text and no logo anywhere; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16')
FLAG_PAREDE = ('on the plain light wall behind her, high on the left, a real American flag in a simple wooden picture frame with glass, about the size of a small '
               'poster, never touching her head')

# ---------- a fala: as letras + o corpo da maioria (o do nora75 ao nora77) ----------
LETRAS = B23.FALA76   # "If your name starts with the letter A, J, M, K, C, E, S, L, R, T or H, be very careful."
CORPO = list(B23.FALA[1:])
CORPO[1] = CORPO[1].replace('Wednesday, November twenty-fifth', 'Saturday, November twenty-eighth')   # 26/11 na costa leste (Brasília −2 h), 2 dias à frente
assert 'Saturday, November twenty-eighth' in CORPO[1]
FALA_CONTROLE = [LETRAS] + CORPO
PICO = "You're about to experience the luckiest days of your entire life. Are you ready?"   # o m11 (e o m06, m09, m13), palavra por palavra
FALA_TESTE = [LETRAS, PICO] + CORPO[1:]
CTA_FACE = B24.CTA_FACE77   # "That's why I left you a quick reading. Check the first comment below to get your reading."
SUF = ['letras', 'mulher-deitada', 'datas', 'fe', 'aviso', 'arcanjo', 'correntes', 'sete-minutos', 'selos-amen', 'amanha', 'alinhada', 'leitura', 'cta-story']
SUF_TESTE = ['letras', 'dias-de-sorte'] + SUF[2:]
G_LETRAS = B23.GESTO76
GESTO_CONTROLE = [G_LETRAS] + list(B23.GESTO[1:])
GESTO_TESTE = [G_LETRAS, 'her eyebrows lift with a bright, excited look and a small smile grows, then she tilts her head slightly as if waiting for an answer'] + list(B23.GESTO[2:])
GESTO_CTA_FACE = B24.GESTO_CTA_FACE

# ---------- as 3 cenas ----------
V = {
    'nora80': dict(
        hora='17h30', pref='carro', img='d2611-carro-IMG', roupa_pt='blusa preta de manga comprida', obj_pt='a ametista nas mãos', lugar_pt='no carro parado',
        roupa='her plain black long-sleeve crew-neck top with no logo',
        cena=('Casual real video in the late afternoon, she sits in the driver\'s seat of her parked car, daylight through the windows, a real American cloth flag '
              'hung flat across the rear window behind the seats, seen over her shoulder, filmed from a phone fixed on the dashboard about 60 centimeters in front of '
              'her at eye level, looking exactly like a real phone video. '),
        cam='the camera stays fixed on the dashboard about 60 centimeters in front of her at eye level with an unchanged framing',
        segura='both hands hold the raw purple amethyst cluster at waist height near the bottom of the frame, turning it slowly now and then',
        objeto='the raw purple amethyst cluster in her hands, the car seat and the American flag across the rear window',
        som='quiet parked-car sound', lugar_en='in the driver\'s seat of her parked car', luz='soft daylight through the car windows',
        prompt_img=('Use the attached images: the first is the approved photo of the woman (keep exactly her face, her warm medium-brown eyes, her complexion, her long '
                    'black wavy hair worn loose, her small plain gold stud earrings and her thin gold chain necklace); the second is her character sheet (the same woman). '
                    'Same woman, same face; change only the clothes, the place and the object. RAW photo taken in the late afternoon from a phone fixed on the dashboard '
                    'about 60 centimeters in front of her at eye level (no phone, phone stand or tripod visible): she sits in the driver\'s seat of her parked car, '
                    'daylight through the windows, a real American cloth flag hung flat across the rear window behind the seats, seen over her shoulder and never '
                    'covering her head; she wears a plain black long-sleeve crew-neck top with no logo; framed from the waist up, her face in the upper middle of the '
                    'image, looking straight into the camera with a calm, serious look and her lips closed; with both hands she holds a raw purple amethyst cluster about '
                    'eight centimeters wide at waist height, plain matte, no glint; ' + FIM),
        copia='o m03 da @beverly.earhart (as letras + o corpo da maioria, no carro, com a ametista nas mãos e a bandeira atrás)',
        teste=False),
    'nora81': dict(
        hora='assim que ficar pronto, à noite de 26/11 (~22h a 23h)', pref='mesa', img='d2611-mesa-IMG', roupa_pt='suéter creme de tricô', obj_pt='uma carta (o verso dourado) na mão', lugar_pt='à mesa, com a estátua de São Miguel',
        roupa='her plain cream cable-knit sweater with no logo',
        cena=('Casual real video in the evening at home, she sits at a wooden dining table with a colorful statue of Saint Michael the Archangel, a small raw amethyst '
              'cluster and an unlit white pillar candle in front of her, ' + FLAG_PAREDE + ', filmed from a static camera about one meter in front of her at collarbone '
              'height, looking exactly like a real phone video, warm indoor light. '),
        cam='the camera stays static about one meter in front of her at collarbone height with an unchanged framing',
        segura=('one hand holds one tarot card upright at collarbone height, below her chin, never touching or covering her face, showing only its plain gold patterned back the whole '
                'time; her other hand rests on the table'),
        objeto='the tarot card with its plain gold back in her hand, the statue, the amethyst, the unlit candle and the framed flag',
        som='quiet room sound', lugar_en='at the wooden dining table in her home', luz='warm indoor evening light',
        prompt_img=('Use the attached images: the first is the approved photo of the woman (keep exactly her face, her warm medium-brown eyes, her complexion, her long '
                    'black wavy hair worn loose, her small plain gold stud earrings and her thin gold chain necklace); the second is her character sheet (the same woman). '
                    'Same woman, same face; change only the clothes, the place and the objects. RAW photo taken in the evening from about one meter in front of her at '
                    'collarbone height (no phone, phone stand or tripod visible): she sits at a wooden dining table in a real American home, warm indoor light; on the '
                    'table in front of her, on the left, a colorful statue of Saint Michael the Archangel about 30 centimeters tall, and on the right a small raw amethyst '
                    'cluster and an unlit white pillar candle; ' + FLAG_PAREDE + '; she wears a plain cream cable-knit sweater with no logo; framed from the waist up, her '
                    'face in the upper middle of the image, looking straight into the camera with a calm, serious look and her lips closed; with one hand she holds one '
                    'tarot card upright at collarbone height, a hand\'s width away from her face, showing only its plain gold patterned back with no text and no picture; '
                    'her other hand rests on the table; ' + FIM),
        copia='o m06 do @itsadrian.reed e o m11 (as letras, a carta na mão o vídeo todo, a estátua de São Miguel na mesa), com o corpo da maioria',
        teste=False),
    'nora82': dict(
        hora='17h00 de 27/11', pref='quarto', img='d2611-quarto-IMG', roupa_pt='blusa verde-escura de tricô', obj_pt='uma caneca de chá nas mãos', lugar_pt='no quarto, sentada na cama',
        roupa='her plain dark-green long-sleeve knit top with no logo',
        cena=('Casual real video at night in a cozy American bedroom, she sits on the edge of her bed, a warm bedside lamp on the nightstand at the side, '
              + FLAG_PAREDE + ', filmed from a static camera about one meter in front of her at collarbone height, looking exactly like a real phone video. '),
        cam='the camera stays static about one meter in front of her at collarbone height with an unchanged framing',
        segura='both hands hold the plain white ceramic mug of tea at collarbone height the whole time',
        objeto='the plain white mug of tea in her hands, the bed, the bedside lamp and the framed flag',
        som='quiet bedroom sound at night', lugar_en='on the edge of her bed', luz='warm bedside lamp light',
        prompt_img=('Use the attached images: the first is the approved photo of the woman (keep exactly her face, her warm medium-brown eyes, her complexion, her long '
                    'black wavy hair worn loose, her small plain gold stud earrings and her thin gold chain necklace); the second is her character sheet (the same woman). '
                    'Same woman, same face; change only the clothes, the place and the object. RAW photo taken at night from about one meter in front of her at '
                    'collarbone height (no phone, phone stand or tripod visible): she sits on the edge of her bed in a cozy real American bedroom, a warm bedside lamp '
                    'on the nightstand at the side; ' + FLAG_PAREDE + '; she wears a plain dark-green long-sleeve knit top with no logo; framed from the waist up, her face '
                    'in the upper middle of the image, looking straight into the camera with a calm, serious look and her lips closed; with both hands she holds a plain '
                    'white ceramic mug of tea at collarbone height, a little below her chin; ' + FIM),
        copia='as letras + o corpo da maioria, com a 2ª frase do m11 (o vídeo mais repetido da mineração de 26/11)',
        teste=True),
}
for k, v in V.items():
    for w in ('chest', 'skin', 'body', 'breast', 'underwear', 'wine', 'powder', 'paint', 'shining', 'glowing', 'sparkling'):
        assert w not in v['prompt_img'].lower(), (k, w)


def prompt_muse(v):
    # 26/11 ~16h50 (o aluno): o Flow bateu o limite de imagens; a imagem sai no Muse, só com o blueprint anexado (o teste dele: "vou anexar só o blueprint").
    p = v['prompt_img']
    i = p.index('Same woman, same face;')
    j = p.index('. ', i) + 2
    return ('Generate exactly ONE photorealistic vertical 9:16 image. The attached image is the character sheet of the woman: keep exactly her face, her warm '
            'medium-brown eyes, her complexion, her long black wavy hair worn loose, her small plain gold stud earrings and her thin gold chain necklace, the same '
            'woman as in every panel of the sheet; no paint, no moon, no stars and no marks on her face; do not copy the sheet layout, the labels or the white '
            'background. ' + p[j:])


def mov(v, g):
    return (f'Throughout the whole 10 seconds {v["cam"]}; {v["segura"]}; {g}; her eyes stay on the lens; '
            'from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; no zoom and no cuts, each hand has exactly five fingers.')


EXTRA = B24.EXTRA | {('at', 'waist'), ('the', 'bottom'), ('of', 'the'), ('in', 'her'), ('her', 'hands'), ('the', 'table'), ('her', 'face'), ('the', 'time')}


def conferir(v, fala, gestos):
    todos = [(i, f, g) for i, (f, g) in enumerate(zip(fala, gestos))] + [(-1, LETRAS, G_LETRAS), (-1, CTA_FACE, GESTO_CTA_FACE)]
    for i, f, g in todos:
        assert len(f.split()) <= 22, (i + 1, len(f.split()), f)
        fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(v, g).lower())
        sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS - EXTRA
        assert not sobra, (i + 1, sobra)
        for w in ('link', 'free', 'card', 'tarot', 'private', 'cards'):
            assert w not in re.findall(r"[a-z']+", f.lower()), (i + 1, w)
        if 0 <= i < len(fala) - 1:
            prox = re.split(r'(?<=[.!?])\s+', fala[i + 1])[0]
            assert len(f.split()) + len(prox.split()) > 22, (i + 1, 'a 1ª frase do take seguinte cabe neste')


def livre(v):
    return (v['cena'] + f'CONTINUITY LOCKS for every take: the woman, {ROSTO}, {v["roupa"]}, {v["objeto"]} stay exactly as in the reference image; the framing is '
            'exactly the one of the reference image, from the waist up, her face in the upper middle of the frame; ' + v['segura'] + '; natural skin texture with '
            'visible pores, slight phone grain, everything in focus, no bokeh, no filter, no glow and no sparkles; no zoom, no cuts and no reframing; no phone, phone '
            'stand, tripod, object, person, animal or text appears or disappears; no paint, moon, stars or marks ever appear on her face; each hand always has exactly '
            f'five fingers; no on-screen text, no captions; {v["som"]} only, no music. SPEECH RULE for every take: '
            "she says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added sentence "
            'before, between or after; numbers and dates are spoken as words exactly as written; she speaks in a direct, serious, intimate tone, like telling a secret to '
            'one person; when she finishes the last word she closes her lips, stays silent and keeps a calm still expression until the clip ends.')


def prompt_take(v, txt, movimento, arquivo, clip, total):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image sits '
            f'{v["lugar_en"]} and speaks directly to the camera.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + txt + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            + VC.NORA.replace('{clip}', str(clip)).replace('{total}', str(total)) + '\n\n'
            'SAME VOICE AS THE OTHER CLIPS: use exactly the same voice as the other clips of this video already generated in this '
            'conversation (same timbre, pitch, accent, pace, volume, energy and microphone sound).\n\n'
            'VOICE PACING: medium pace (155 to 180 words per minute), about 8 seconds of speech; when she finishes the last word she closes her lips and stays silent '
            'with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + movimento + '\n\n'
            f'VISUAL: realistic casual phone video, {v["luz"]}, natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter.\n\n'
            'CAMERA: static, no zoom, no cuts, no reframing.\n\n'
            f'AUDIO: only her voice and {v["som"]}; no music, no other voices, no sound effects.\n\n'
            f'CONTINUITY: {ROSTO}, {v["roupa"]}, {v["objeto"]} and everything behind her stay exactly as in the reference image; no paint, moon, stars or marks appear '
            'on her face; no phone, person or text appears; each hand has exactly five fingers; no on-screen text or captions.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.'
            f'\n\nName this clip exactly {arquivo}, so the downloaded file already has this name.')


def config(v, n):
    cf = copy.deepcopy(B.BASE['central']['config'])
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = f'colar o texto abaixo (a imagem é a {v["img"]}: a Nora {v["lugar_pt"]}, de {v["roupa_pt"]}, com {v["obj_pt"]})'
                campo['copiar'] = livre(v)
            elif campo['campo'] == 'COLE SUA COPY AQUI':
                campo['valor'] = f'colar a fala do T01 ao T{n:02d} (seção “A fala e a movimentação”): 1 colagem só, com {n} takes'
            elif campo['campo'] == 'Movimento de câmera':
                campo['valor'] = 'Estático / câmera parada, sem zoom'
            elif campo['campo'] == 'Atmosfera / mood':
                campo['valor'] = 'Íntimo e confidencial'
            elif campo['campo'] == 'Movimentação':
                campo['valor'] = f'colar as {n} linhas, uma por take (T01 a T{n:02d})'
            elif campo['campo'] == 'Conferir':
                campo['valor'] = f'{n} takes (8 ou 10 s cada)'
    VC.adicionar(cf)
    return cf


TEXTOS = {
    'nora80': dict(
        insta=("If your name starts with one of these letters, be very careful 👀 Your private reading is waiting in my story 🔮\n"
               'Comment the first letter of your name 👇\n#manifestation #archangelmichael #abundance #2027 #lawofattraction'),
        face=('If your name starts with one of these letters, this message is for you ✨ Your reading is waiting in the first comment 🔮\n'
              '#manifestation #2027 #archangelmichael'),
        fix_insta='Is your letter on the list? 👀 tap my profile picture above, your reading is waiting in my story',
        fix_face='If your letter was on the list, your next step is here 🔮 👉 '),
    'nora81': dict(
        insta=("Is the first letter of your name on this list? 👀 Your private reading is waiting in my story 🔮\n"
               'Type 222 if your letter was called ✨\n#manifestation #angelnumbers #abundance #2027 #lawofattraction'),
        face=('Is the first letter of your name on this list? ✨ Your reading is waiting in the first comment 🔮\n#manifestation #2027 #angelnumbers'),
        fix_insta='If your letter was called ✨ tap my profile picture above, your next step is in my story',
        fix_face="Saint Michael's message continues here ✨ 👉 "),
    'nora82': dict(
        insta=("If your letter is here, your luckiest days may be closer than you think 🍀 Your private reading is waiting in my story 🔮\n"
               "Comment the time you're watching this ⏰\n#manifestation #abundance #2027 #lawofattraction #newchapter"),
        face=('If your letter is on this list, this was meant to find you today ✨ Your reading is waiting in the first comment 🔮\n#manifestation #2027 #newchapter'),
        fix_insta='Your luckiest days start with one small step 🍀 tap my profile picture above and check my story',
        fix_face='This reading was meant to find you today ✨ 👉 '),
}
assert len({t['fix_face'] for t in TEXTOS.values()}) == 3


def montar(nn):
    v = V[nn]
    teste = v['teste']
    fala = list(FALA_TESTE if teste else FALA_CONTROLE)
    gestos = list(GESTO_TESTE if teste else GESTO_CONTROLE)
    sufs = SUF_TESTE if teste else SUF
    if nn == 'nora81':
        # com a carta na mão, sem "receive" na fala (14/11: derrubou o T04 e o T05 do nora65; LICOES-ATIVAS 3.5). O T10 só vai no Insta.
        fala[9] = fala[9].replace("you'll receive", "you'll get")
        assert 'receive' not in ' '.join(fala).lower()
    conferir(v, fala, gestos)
    # 26/11 ~17h10 (o aluno): os 2 takes do Face vão no fim da mesma colagem da Central, e os 15 saem do Muse de uma vez.
    conferir(v, fala + [LETRAS, CTA_FACE], gestos + [G_LETRAS, GESTO_CTA_FACE])
    n = len(fala)
    palavras = sum(len(f.split()) for f in fala)
    nomes = [f'd2611-{v["pref"]}-T{i + 1:02d}-{sufs[i]}' for i in range(n)]
    n_letras, n_cta = f'd2611-{v["pref"]}-T14-FACE-letras', f'd2611-{v["pref"]}-T15-FACE-cta-comentario'
    B23.ROUPA = v['roupa']
    P = B23.base(nn)
    P['figurino'] = v['roupa']
    escolha = (f'Confira primeiro o rosto (a mesma Nora do blueprint, SEM a lua e SEM as estrelinhas, os olhos CASTANHOS, o cabelo solto), depois: {v["roupa_pt"]}; '
               f'{v["obj_pt"]}; a bandeira dos EUA sem cobrir a cabeça; 5 dedos em cada mão; nada escrito em lugar nenhum. Salve como {v["img"]}.')
    P['pre_gancho'] = {
        'titulo_secao': 'A imagem (no Muse, antes dos takes)',
        'conceito': (f'Uma imagem só, para os {n} takes e os 2 do Face: a Nora v3 (sem a pintura, olhos castanhos) {v["lugar_pt"]}, de {v["roupa_pt"]}, com '
                     f'{v["obj_pt"]} e a bandeira dos EUA. A cópia de {v["copia"]}. O Flow bateu o limite de imagens (26/11): a imagem sai no Muse, só com o blueprint.'),
        'modo': 'Muse, na conversa da Nora: anexar só a nora-v3-blueprint e colar o prompt. Ele gera 1 imagem por vez.',
        'etapas': [{'titulo': f'A imagem de todos os takes ({v["lugar_pt"]}), no Muse, só com o blueprint', 'nome': v['img'], 'tipo': 'img',
                    'anexar': f'só a {FOLHA} (a folha da Nora v3, em 1K)',
                    'quadros': ('1 imagem por vez. ' + escolha + ' Se o rosto escapar ou algo vier errado, mande na mesma conversa: “Generate it again, exactly the '
                                'same prompt, one new version.” Se quiser, me mande a imagem antes de gerar os takes: eu confiro o rosto contra o blueprint.'),
                    'prompt': prompt_muse(v)},
                   {'titulo': 'Reserva: no Flow, quando o limite de imagens voltar (x4, 0 crédito)', 'nome': v['img'], 'tipo': 'img',
                    'anexar': f'1º a {IMG_BASE} (a Nora do nora79, na cozinha); 2º a {FOLHA} (a folha da Nora v3, em 1K)',
                    'quadros': 'x4, 0 crédito. ' + escolha + ' Guarde as 3 que sobrarem: uma delas vira o story.',
                    'prompt': v['prompt_img']}],
    }
    P['imagens_titulo'] = f'A imagem das falas ({v["img"]}, em todos os takes)'
    P['refs'] = [f'{v["img"]} do T01 ao T{n:02d} e nos 2 takes do Face']
    P['imagens'] = [{'rotulo': f'IMAGEM 1 · {v["img"]}', 'cena': 'gerada no Muse (seção da imagem)', 'anexar': f'a {v["img"]}'}]
    T = TEXTOS[nn]
    P['roteiro'] = {
        'id': f'{nn}-LETRAS-CORPO-MAIORIA-{v["pref"].upper()}-2611',
        'titulo': (f'{nn} · Insta e Face {v["hora"]} · as letras do nome + o corpo da maioria, {v["lugar_pt"]}, de {v["roupa_pt"]}'
                   + (' · O TESTE DO DIA: a 2ª frase como pico' if teste else '')),
        'duracao_total': 95,
        'descricao_instagram': T['insta'],
        'descricao_face': T['face'],
    }
    P['videos'] = ([{'rotulo': f'T{i + 1:02d}', 'cena': sufs[i], 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({v["img"]})', 'acao': '', 'b_roll': '',
                     'fala': fala[i], 'movimentacao': mov(v, gestos[i]), 'arquivo': nomes[i]} for i in range(n)]
                   + [{'rotulo': 'T14 (só Face)', 'cena': 'as letras do nome, gerada de novo (o começo do Face)', 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({v["img"]})',
                       'acao': '', 'b_roll': '', 'fala': LETRAS, 'movimentacao': mov(v, G_LETRAS), 'arquivo': n_letras},
                      {'rotulo': 'T15 (só Face)', 'cena': 'o CTA para o comentário (o fim do Face)', 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({v["img"]})',
                       'acao': '', 'b_roll': '', 'fala': CTA_FACE, 'movimentacao': mov(v, GESTO_CTA_FACE), 'arquivo': n_cta}])
    P['texto_tela'] = {'hook': '', 'hook_comeca': '—', 'hook_termina': '—', 'hook_alt': '', 'extras': []}
    B24.mapa(P)
    P['comentario_fixado'] = {'insta': T['fix_insta'], 'face': T['fix_face'] + FB}
    ct = P['central']
    ct['config'] = config(v, n + 2)
    ct['colagens'] = [{'titulo': f'{nn}: a colagem do T01 ao T{n + 2:02d} (na {v["img"]}; o T14 e o T15 são os 2 só do Face, no fim)',
                       'fala': ' '.join(fala + [LETRAS, CTA_FACE]),
                       'movimentacao': [mov(v, g) for g in gestos + [G_LETRAS, GESTO_CTA_FACE]], 'takes': list(range(n + 2))}]
    ct['conferir'] = (f'Conferir em cada take: a Nora SEM a lua e SEM as estrelinhas, os olhos castanhos, de {v["roupa_pt"]}, {v["lugar_pt"]}, com {v["obj_pt"]} e a '
                      'bandeira; ela fala uma vez só e diz as letras, as datas e os números por extenso.')
    ag = copy.deepcopy(ct['agente'])
    ag['imagem'] = v['img']
    velho = 'Name each clip with its prompt number (01, 02, 03 and so on).'
    assert velho in ag['aviso']
    ag['aviso'] = ag['aviso'].replace(velho, 'Name each clip with exactly this file name, so the downloaded file already has it: '
                                      + ', '.join(f'Prompt {i + 1} = {(nomes + [n_letras, n_cta])[i]}' for i in range(n + 2)) + '.')
    todos = nomes + [n_letras, n_cta]
    resto = ', '.join(f'Prompt {i + 1} = {todos[i]}' for i in range(6, n + 2))
    msg_resto = ('“Now generate the remaining prompts from my previous message, exactly as written, in the same order, using the attached image as the first '
                 f'frame of every clip, and name each clip with exactly this file name: {resto}.”')
    lista = ' · '.join(f'T{i + 1:02d} começa em “{" ".join(f.split()[:5])}…” → {todos[i]}' for i, f in enumerate(fala + [LETRAS, CTA_FACE]))
    ag['intro'] = (f'No Muse, na mesma conversa da Nora (a voz). Siga os passos de cima para baixo. São {n + 2} clipes, todos com a {v["img"]} e todos pela '
                   f'Central, numa colagem só: os {n} do Insta (T01 a T{n:02d}) e, no fim, os 2 só do Face (o T14, as letras de novo, e o T15, o fim que manda para o 1º comentário).')
    ag['passos'] = [
        f'Na Central: preencha como na seção da Central (o LIVRE, a voz, o prompt de consistência de voz e as {n + 2} linhas de movimentação do {nn}) e cole a fala '
        f'inteira, do T01 ao T{n + 2:02d}. Confira: {n + 2} takes (o T14 começa em “If your name starts…” e o T15 em “That’s why I left you…”).',
        f'O vídeo inteiro (T01 a T{n + 2:02d}, {n + 2} clipes): no Muse, anexe a {v["img"]} + o aviso do Muse + o “COPIAR TUDO JUNTO”. O Muse gera 5 ou 6 por vez: '
        f'depois dos primeiros, mande na mesma conversa, com a mesma imagem: {msg_resto} Repita a mesma mensagem até sair o T{n + 2:02d}.',
        f'Confira os nomes ao baixar (o site põe “media-generation-” na frente e um código no fim; pode deixar). Se algum vier com nome aleatório, ouça o começo e renomeie: {lista}.',
        f'Confira cada take: sem a lua e sem as estrelinhas; os olhos castanhos (iguais em todos); {v["roupa_pt"]}; {v["obj_pt"]}; ela fala uma vez só e fecha a boca no fim. '
        'Se o Muse recusar: “Generate prompt X again, exactly as written.”',
        'Se a voz de algum take sair diferente das outras, gere aquele de novo na mesma conversa, pedindo “exactly the same voice as the other clips of this video”. '
        'Se aparecer o erro de limite do dia, me avise com quantos saíram.',
    ]
    ct['agente'] = ag
    P['silencio'] = {
        'intro': ('Arraste na “M2M FusionZ” os 15 takes de uma vez (T01 a T15), sem separar nada. Ela junta pela ordem do nome, então o T14 e o T15 (os 2 só do Face) '
                  'ficam no fim. Sai 1 arquivo só. “Zoom nos cortes” = DESLIGADO.'),
        'nome': f'{nn}-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'T01 a T15 (o T14 e o T15 são os do Face)',
        'depois': ['Suba os 15 takes e espere a Prévia.', 'Confira a primeira palavra do T01 e a última do T15.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', f'Clique em Cortar e baixar e salve como {nn}-cortado.'],
    }
    prazo = {'nora80': 'assim que puder (se passar das 17h30, posta assim que eu devolver)', 'nora81': 'assim que ficar pronto (eu devolvo em ~20 min; posta na hora)', 'nora82': 'até ~16h30 de 27/11'}[nn]
    P['edicao_linha'] = [
        {'quando': 'O que vai em cada vídeo', 'texto': 'Você monta 1 arquivo só, com os 15 takes. Os 2 vídeos (Insta e Face) eu separo aqui.',
         'como': (f'INSTA ({nn}-final): T01 ao T13, na ordem. FACE ({nn}-final-FACE): T14 (as letras) + T02, T03, T04 (eu tiro o “money”), T06, T07, T11 + T15 (o comentário). '
                  'Ficam fora do Face: o T01 (o Face abre com o T14), o T05 (a ameaça), o T08 (os 7 minutos e o “send to yourself”), o T09 (os selos e o amen), '
                  'o T10 (“amanhã às 10”), o T12 e o T13 (o CTA do story).')},
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {nn}-cortado', 'como': 'Começa direto no T01, sem hook. O T14 e o T15 ficam no fim, como vieram da FusionZ.'},
        {'quando': '1. Do começo ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB, o vídeo todo (o T14 e o T15 também)', 'como': 'Começa no 1º quadro.'},
        {'quando': f'2. Exportar e me mandar {prazo}', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'1080×1920, nome {nn}-montado (acima de 30 MB, link do Drive). Eu devolvo em ~20 min os 2 prontos: o {nn}-final (Insta) e o {nn}-final-FACE.'},
    ]
    story = {
        'nora80': ('O story no ar é o da cozinha (01h10 no Insta, 01h04 no Face): vence ~01h de 27/11. Não poste story agora; o novo (os campos trancados) vai junto com o '
                   'nora81, na noite de 26/11. Antes de abrir o Insta, confira o IP e os EUA no mylocation.org.'),
        'nora81': ('O story da cozinha vence ~01h04 (Face) e ~01h10 (Insta): poste o NOVO junto com este vídeo, nos dois, antes das 01h. É o dos campos trancados '
                   '(o teste aprovado em 26/11). Quando gerar a imagem deste vídeo no Muse, gere mais 1 (“Generate it again, exactly the same prompt, one new version”, uma em '
                   'que ela olhe para a câmera) e me mande: eu devolvo a foto com o texto; você só põe o adesivo do link (STORYIG no Insta, FACE no Face).'),
        'nora82': 'O story novo (os campos trancados) vai com o nora81, na noite de 26/11. Antes de postar, confira se ele está no ar no Insta e no Face.',
    }[nn]
    P['story'] = {'ja_postado': True, 'nota': story}
    teste_txt = ('O QUE ESTE VÍDEO TESTA (o teste do dia, 1 só): a 2ª frase como PICO, do m11 (o vídeo mais repetido da mineração de 26/11): “You’re about to experience '
                 'the luckiest days of your entire life. Are you ready?” no lugar da mulher deitada. O resto é igual ao nora80 e ao nora81 (o controle). A medida, com ~24 h: '
                 'a retenção aos 3 s e aos 10 s, o skip e as visitas ao perfil, contra o nora81 (a noite de 26/11) e o nora80 (o fim da tarde de 26/11). Olhar a fatia da Índia antes de comparar: o nora82 vai às 17h, a faixa da tarde.' if teste else
                 'Este vídeo NÃO testa nada: é o que vem dando certo, igual (as letras + o corpo da maioria; o nora76-FACE e o nora77-FACE, os 2 maiores da Página). '
                 'Muda só a roupa e o cenário. O teste do dia vai no nora82, às 17h de 27/11 (mudou em 26/11 18h50: o aluno não conseguiu o nora81 às 21h).')
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': ([{'nome': v['img'], 'tipo': 'imagem das falas', 'status': 'gerar', 'onde': f'No Muse, só com a {FOLHA} (1 por vez); reserva: o Flow com a {IMG_BASE} + a {FOLHA}.',
                    'descricao': f'{v["lugar_pt"]}, {v["roupa_pt"]}, {v["obj_pt"]}, a bandeira.'}]
                  + [{'nome': nomes[i], 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{fala[i]}”'} for i in range(n)]
                  + [{'nome': n_letras, 'tipo': 'take do Face', 'status': 'gerar', 'descricao': f'“{LETRAS}”'},
                     {'nome': n_cta, 'tipo': 'take do Face', 'status': 'gerar', 'descricao': f'“{CTA_FACE}”'}]),
        'decisao': [
            teste_txt,
            (f'{n} takes ({palavras} palavras, ~1:35) + 2 só do Face = {n + 2} clipes no Muse, todos com 1 imagem só. A fala é a do nora75 ao nora77 (o corpo da maioria) com '
             'as letras na frente; a data diz “before Saturday, November twenty-eighth”.' + (' Com a carta na mão, o T10 diz “get” no lugar de “receive” (regra da carta).' if nn == 'nora81' else '')),
            (f'Insta e Face às {v["hora"]}. No Face: abre com o T14 (as letras, outro arquivo) e termina mandando para o 1º comentário; sem a ameaça, o dinheiro, '
             'os 7 minutos, os selos e o “amanhã às 10”. Sem texto no topo, só o 11:11✨ (como no nora75 ao nora77); legenda simples; seta grande no fim.'),
            ('A CHECAGEM DO TAKE 1: a pergunta está na legenda e no comentário fixado (“Is your letter on the list?”); gancho visual, falado e escrito juntos: '
             f'a Nora com {v["obj_pt"]} desde o 1º quadro, as letras faladas e a legenda; formato que já viralizou: as letras do nome (3 contas na mineração de 26/11 e o maior post da Página).'),
        ],
    }
    P['ordem'] = ['pecas', 'prehook', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    return P, n, palavras


def salvar(P, nn, rotulo):
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>' + rotulo + '</title>', html, count=1)
    (R / f'PAINEL-{nn.upper()}.html').write_text(html, encoding='utf-8')
    print('ok', nn, len(html), 'bytes')


if __name__ == '__main__':
    for nn, rot in (('nora80', 'Painel nora80 · as letras + o corpo da maioria, no carro · 26/11 17h30'),
                    ('nora81', 'Painel nora81 · as letras + o corpo da maioria, à mesa · noite de 26/11'),
                    ('nora82', 'Painel nora82 · o teste da 2ª frase, no quarto · 27/11 17h')):
        P, n, pal = montar(nn)
        print(nn, n, 'takes,', pal, 'palavras')
        salvar(P, nn, rot)
