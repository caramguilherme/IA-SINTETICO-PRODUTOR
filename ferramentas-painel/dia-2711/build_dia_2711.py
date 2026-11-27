# Painéis do dia 27/11/2026: nora82 (17h), nora83 (20h30) e nora84 (0h00 de 28/11), Insta e Face.
# A decisão do aluno (27/11 ~12h55): "o 82, 83 e 84 vai ser o mesmo pacote que vem dando certo no insta e face" = o pacote do nora81
#   (1.352 views no Insta com ~9 h, 17 compartilhamentos e 17 salvos, contra 127 do nora80): as letras do nome + o corpo da maioria
#   + as 2 frases de reinício ("Now, this part matters." e "But it gets better.") + a carta (o verso dourado) na mão + a estátua de São Miguel.
#   Cada um com outra roupa e outro cômodo (a regra de 24/11: cada post do Insta gerado de novo). Sem teste (o de 27/11 foi o nora81);
#   sem o "free" hoje (o aluno, 14h07: "2", começa em 28/11). As aulas de copy do Kobata não mudaram a copy do pacote; da aula 6
#   ("a imagem é mais importante até mesmo do que a fala", 12:47) vem só a estátua inteira à esquerda dela no 1º quadro, como no nora81.
# Gerado a partir do build_dia_2611.py (o do nora81). Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2711/build_dia_2711.py
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
# 26/11 ~21h15 (o aluno, sobre o 4º lote de dicas: "daria para fazer isso no Nora 81… colocar uma frase curta de reinício para causar essa curiosidade"):
# a frase de reinício da Gio Garcia (q01: "uma frase de três ou quatro palavras [que] reabre a curiosidade", a cada 2 ou 3 frases). No nora81, 2 frases novas:
# depois da 2ª frase (onde a curva cai), um take novo; e antes do "amanhã às 10", no começo do mesmo take. As viradas que o corpo já tem ficam
# ("So take this seriously.", "Saint Michael the Archangel sent a warning.", "But the universe is warning me…").
REINICIO1 = "Now, this part matters."
G_REINICIO1 = 'she leans in a little closer to the lens, her eyebrows lift slightly and she holds a curious, serious look'
REINICIO2 = "But it gets better."

# ---------- as 3 cenas (o pacote do nora81: a carta na mão e a estátua de São Miguel; muda a roupa e o cômodo) ----------
def _img(lugar, roupa, objetos, resto, hora):
    return ('Use the attached images: the first is the approved photo of the woman (keep exactly her face, her warm medium-brown eyes, her complexion, her long '
            'black wavy hair worn loose, her small plain gold stud earrings and her thin gold chain necklace); the second is her character sheet (the same woman). '
            'Same woman, same face; change only the clothes, the place and the objects. RAW photo taken ' + hora + ' from about one meter in front of her at '
            'collarbone height (no phone, phone stand or tripod visible): ' + lugar + '; ' + objetos + '; ' + FLAG_PAREDE + '; she wears ' + roupa + '; framed from '
            'the waist up, her face in the upper middle of the image, looking straight into the camera with a calm, serious look and her lips closed; with one hand she '
            'holds one tarot card upright at collarbone height, a hand\'s width away from her face, showing only its plain gold patterned back with no text and no '
            'picture; her other hand rests ' + resto + '; ' + FIM)


V = {
    'nora82': dict(
        hora='17h00 de 27/11', pref='quarto', img='d2711-quarto-IMG', roupa_pt='blusa verde-escura de tricô', obj_pt='uma carta (o verso dourado) na mão',
        lugar_pt='no quarto, sentada na beira da cama, com a estátua de São Miguel no criado-mudo',
        roupa='her plain dark-green long-sleeve knit top with no logo',
        cena=('Casual real video in the early evening in a cozy American bedroom, she sits on the edge of her bed; on the nightstand beside her a colorful statue of '
              'Saint Michael the Archangel and a warm bedside lamp (the statue at her left side, fully visible in the frame); ' + FLAG_PAREDE + ', filmed from a static camera about one meter in front of her at collarbone '
              'height, looking exactly like a real phone video. '),
        cam='the camera stays static about one meter in front of her at collarbone height with an unchanged framing',
        segura='one hand holds one tarot card upright at collarbone height, below her chin, never touching or covering her face, showing only its plain gold patterned back the whole time; her other hand rests on her lap',
        objeto='the tarot card with its plain gold back in her hand, the bed, the nightstand with the statue and the lamp, and the framed flag',
        som='quiet bedroom sound', lugar_en='on the edge of her bed', luz='warm bedside lamp light',
        prompt_img=_img('she sits on the edge of her bed in a cozy real American bedroom in the early evening',
                        'a plain dark-green long-sleeve knit top with no logo',
                        'on the nightstand beside her, a colorful statue of Saint Michael the Archangel about 30 centimeters tall, standing at her left side at about the height of her waist, fully visible in the frame (never cut off and never hidden behind her) and a warm bedside lamp',
                        'on her lap', 'in the early evening'),
        copia='o pacote do nora81 (as letras, a carta na mão, a estátua de São Miguel, as 2 frases de reinício), no quarto'),
    'nora83': dict(
        hora='20h30 de 27/11', pref='sala', img='d2711-sala-IMG', roupa_pt='blusa vinho (bordô) de manga comprida', obj_pt='uma carta (o verso dourado) na mão',
        lugar_pt='na sala, sentada no sofá, com a estátua de São Miguel na mesinha ao lado',
        roupa='her plain deep burgundy long-sleeve top with no logo',
        cena=('Casual real video in the evening in a simple American living room, she sits on a beige fabric sofa; on the small side table next to her a colorful '
              'statue of Saint Michael the Archangel and a small table lamp (the statue at her left side, fully visible in the frame); ' + FLAG_PAREDE + ', filmed from a static camera about one meter in front of her at '
              'collarbone height, looking exactly like a real phone video, warm indoor light. '),
        cam='the camera stays static about one meter in front of her at collarbone height with an unchanged framing',
        segura='one hand holds one tarot card upright at collarbone height, below her chin, never touching or covering her face, showing only its plain gold patterned back the whole time; her other hand rests on the armrest of the sofa',
        objeto='the tarot card with its plain gold back in her hand, the sofa, the side table with the statue and the lamp, and the framed flag',
        som='quiet living room sound', lugar_en='on the sofa in her living room', luz='warm indoor evening light',
        prompt_img=_img('she sits on a beige fabric sofa in a simple real American living room in the evening, warm indoor light',
                        'a plain deep burgundy long-sleeve top with no logo',
                        'on the small side table next to her, a colorful statue of Saint Michael the Archangel about 30 centimeters tall, standing at her left side at about the height of her waist, fully visible in the frame (never cut off and never hidden behind her) and a small table lamp',
                        'on the armrest of the sofa', 'in the evening'),
        copia='o pacote do nora81 (as letras, a carta na mão, a estátua de São Miguel, as 2 frases de reinício), na sala'),
    'nora84': dict(
        hora='0h00 de 28/11', pref='escrivaninha', img='d2711-escrivaninha-IMG', roupa_pt='suéter azul-marinho de tricô', obj_pt='uma carta (o verso dourado) na mão',
        lugar_pt='à escrivaninha, à noite, com a estátua de São Miguel em cima dela',
        roupa='her plain navy-blue knit sweater with no logo',
        cena=('Casual real video late at night at home, she sits at a simple wooden desk; on the desk a colorful statue of Saint Michael the Archangel, a closed '
              'notebook and a warm desk lamp (the statue at her left side, fully visible in the frame); ' + FLAG_PAREDE + ', filmed from a static camera about one meter in front of her at collarbone height, looking exactly '
              'like a real phone video. '),
        cam='the camera stays static about one meter in front of her at collarbone height with an unchanged framing',
        segura='one hand holds one tarot card upright at collarbone height, below her chin, never touching or covering her face, showing only its plain gold patterned back the whole time; her other hand rests on the desk',
        objeto='the tarot card with its plain gold back in her hand, the desk with the statue, the closed notebook and the lamp, and the framed flag',
        som='quiet room sound at night', lugar_en='at the wooden desk in her home', luz='warm desk lamp light at night',
        prompt_img=_img('she sits at a simple wooden desk in her real American home late at night, warm desk lamp light',
                        'a plain navy-blue knit sweater with no logo',
                        'on the desk, a colorful statue of Saint Michael the Archangel about 30 centimeters tall, standing at her left side at about the height of her waist, fully visible in the frame (never cut off and never hidden behind her), a closed notebook and a warm desk lamp',
                        'on the desk', 'late at night'),
        copia='o pacote do nora81 (as letras, a carta na mão, a estátua de São Miguel, as 2 frases de reinício), à escrivaninha'),
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
    'nora82': dict(
        insta=("If your letter is here, something you've been waiting for may be closer than you think 🍀 Your private reading is waiting in my story 🔮\n"
               "Comment the time you're watching this ⏰\n#manifestation #abundance #2027 #lawofattraction #newchapter"),
        face=('If your letter is on this list, this was meant to find you today ✨ Your reading is waiting in the first comment 🔮\n#manifestation #2027 #newchapter'),
        fix_insta='The next chapter starts with one small step 🍀 tap my profile picture above and check my story',
        fix_face='This reading was meant to find you today ✨ 👉 '),
    'nora83': dict(
        insta=("Saint Michael asked me to share this tonight 🕊️ If your letter was called, your private reading is waiting in my story 🔮\n"
               'Type 11:11 if you feel this message is for you ✨\n#manifestation #archangelmichael #1111 #2027 #lawofattraction'),
        face=("Saint Michael's message for tonight 🕊️ If your letter was called, your reading is waiting in the first comment 🔮\n#manifestation #archangelmichael #2027"),
        fix_insta='Your letter was called for a reason 🕊️ tap my profile picture above, the rest of the message is in my story',
        fix_face='Before you go to sleep tonight, open your reading here 🌙 👉 '),
    'nora84': dict(
        insta=("If this found you at midnight, it's not by chance 🌙 Your private reading is waiting in my story 🔮\n"
               "Comment 222 if you're ready for your new chapter ✨\n#manifestation #angelnumbers #222 #2027 #lawofattraction"),
        face=('If this message found you tonight, it was meant for you 🌙 Your reading is waiting in the first comment 🔮\n#manifestation #2027 #angelnumbers'),
        fix_insta='If your letter was called tonight 🌙 tap my profile picture above, your reading is in my story',
        fix_face='A new chapter is waiting for you here 🌙 👉 '),
}
assert len({t['fix_face'] for t in TEXTOS.values()}) == 3


def montar(nn):
    v = V[nn]
    teste = False   # 27/11: sem teste (o de hoje foi o nora81)
    fala = list(FALA_TESTE if teste else FALA_CONTROLE)
    gestos = list(GESTO_TESTE if teste else GESTO_CONTROLE)
    sufs = SUF_TESTE if teste else SUF
    if True:   # o pacote do nora81 em todos
        # com a carta na mão, sem "receive" na fala (14/11: derrubou o T04 e o T05 do nora65; LICOES-ATIVAS 3.5). O T10 só vai no Insta.
        fala[9] = fala[9].replace("you'll receive", "you'll get")
        assert 'receive' not in ' '.join(fala).lower()
        # o teste da frase de reinício (26/11 ~21h15, pedido do aluno)
        assert fala[9].startswith('If you did everything right')
        fala[9] = REINICIO2 + ' ' + fala[9]
        fala.insert(2, REINICIO1); gestos.insert(2, G_REINICIO1); sufs = list(sufs[:2]) + ['reinicio'] + list(sufs[2:])
    conferir(v, fala, gestos)
    # 26/11 ~17h10 (o aluno): os 2 takes do Face vão no fim da mesma colagem da Central, e os 15 saem do Muse de uma vez.
    conferir(v, fala + [LETRAS, CTA_FACE], gestos + [G_LETRAS, GESTO_CTA_FACE])
    n = len(fala)
    palavras = sum(len(f.split()) for f in fala)
    nomes = [f'd2711-{v["pref"]}-T{i + 1:02d}-{sufs[i]}' for i in range(n)]
    tf1, tf2 = f'T{n + 1:02d}', f'T{n + 2:02d}'   # os 2 só do Face, no fim (T14 e T15 com 13 takes; T15 e T16 no nora81)
    n_letras, n_cta = f'd2711-{v["pref"]}-{tf1}-FACE-letras', f'd2711-{v["pref"]}-{tf2}-FACE-cta-comentario'
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
        'id': f'{nn}-PACOTE-NORA81-{v["pref"].upper()}-2711',
        'titulo': (f'{nn} · Insta e Face {v["hora"]} · as letras do nome + o corpo da maioria, {v["lugar_pt"]}, de {v["roupa_pt"]}'
                   + (' · O TESTE DO DIA: a 2ª frase como pico' if teste else '') + ' · o pacote do nora81'),
        'duracao_total': 95,
        'descricao_instagram': T['insta'],
        'descricao_face': T['face'],
    }
    P['videos'] = ([{'rotulo': f'T{i + 1:02d}', 'cena': sufs[i], 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({v["img"]})', 'acao': '', 'b_roll': '',
                     'fala': fala[i], 'movimentacao': mov(v, gestos[i]), 'arquivo': nomes[i]} for i in range(n)]
                   + [{'rotulo': f'{tf1} (só Face)', 'cena': 'as letras do nome, gerada de novo (o começo do Face)', 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({v["img"]})',
                       'acao': '', 'b_roll': '', 'fala': LETRAS, 'movimentacao': mov(v, G_LETRAS), 'arquivo': n_letras},
                      {'rotulo': f'{tf2} (só Face)', 'cena': 'o CTA para o comentário (o fim do Face)', 'duracao': 10, 'primeiro_quadro': f'IMAGEM 1 ({v["img"]})',
                       'acao': '', 'b_roll': '', 'fala': CTA_FACE, 'movimentacao': mov(v, GESTO_CTA_FACE), 'arquivo': n_cta}])
    P['texto_tela'] = {'hook': '', 'hook_comeca': '—', 'hook_termina': '—', 'hook_alt': '', 'extras': []}
    B24.mapa(P)
    P['comentario_fixado'] = {'insta': T['fix_insta'], 'face': T['fix_face'] + FB}
    ct = P['central']
    ct['config'] = config(v, n + 2)
    ct['colagens'] = [{'titulo': f'{nn}: a colagem do T01 ao T{n + 2:02d} (na {v["img"]}; o {tf1} e o {tf2} são os 2 só do Face, no fim)',
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
                   f'Central, numa colagem só: os {n} do Insta (T01 a T{n:02d}) e, no fim, os 2 só do Face (o {tf1}, as letras de novo, e o {tf2}, o fim que manda para o 1º comentário).')
    ag['passos'] = [
        f'Na Central: preencha como na seção da Central (o LIVRE, a voz, o prompt de consistência de voz e as {n + 2} linhas de movimentação do {nn}) e cole a fala '
        f'inteira, do T01 ao T{n + 2:02d}. Confira: {n + 2} takes (o {tf1} começa em “If your name starts…” e o {tf2} em “That’s why I left you…”).',
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
        'intro': (f'Arraste na “M2M FusionZ” os {n + 2} takes de uma vez (T01 a {tf2}), sem separar nada. Ela junta pela ordem do nome, então o {tf1} e o {tf2} (os 2 só do Face) '
                  'ficam no fim. Sai 1 arquivo só. “Zoom nos cortes” = DESLIGADO.'),
        'nome': f'{nn}-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': f'T01 a {tf2} (o {tf1} e o {tf2} são os do Face)',
        'depois': [f'Suba os {n + 2} takes e espere a Prévia.', f'Confira a primeira palavra do T01 e a última do {tf2}.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', f'Clique em Cortar e baixar e salve como {nn}-cortado.'],
    }
    prazo = {'nora82': 'até ~16h30 de 27/11', 'nora83': 'até ~20h00 de 27/11', 'nora84': 'até ~23h30 de 27/11'}[nn]
    P['edicao_linha'] = [
        {'quando': 'O que vai em cada vídeo', 'texto': f'Você monta 1 arquivo só, com os {n + 2} takes. Os 2 vídeos (Insta e Face) eu separo aqui.',
         'como': ((f'INSTA ({nn}-final): T01 ao T14, na ordem. FACE ({nn}-final-FACE): T15 (as letras) + T02, T03 (a frase de reinício), T04, T05 (eu tiro o “money”), T07, T08, T12 + T16 (o comentário). '
                   'Ficam fora do Face: o T01 (o Face abre com o T15), o T06 (a ameaça), o T09 (os 7 minutos e o “send to yourself”), o T10 (os selos e o amen), '
                   'o T11 (“amanhã às 10”), o T13 e o T14 (o CTA do story).') if True else
                  (f'INSTA ({nn}-final): T01 ao T13, na ordem. FACE ({nn}-final-FACE): T14 (as letras) + T02, T03, T04 (eu tiro o “money”), T06, T07, T11 + T15 (o comentário). '
                   'Ficam fora do Face: o T01 (o Face abre com o T14), o T05 (a ameaça), o T08 (os 7 minutos e o “send to yourself”), o T09 (os selos e o amen), '
                   'o T10 (“amanhã às 10”), o T12 e o T13 (o CTA do story).'))},
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {nn}-cortado', 'como': f'Começa direto no T01, sem hook. O {tf1} e o {tf2} ficam no fim, como vieram da FusionZ.'},
        {'quando': '1. Do começo ao fim', 'texto': f'Música de sempre (“Ambient Mystical Drone”), −18 dB, o vídeo todo (o {tf1} e o {tf2} também)', 'como': 'Começa no 1º quadro.'},
        {'quando': f'2. Exportar e me mandar {prazo}', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'1080×1920, nome {nn}-montado (acima de 30 MB, link do Drive). Eu devolvo em ~20 min os 2 prontos: o {nn}-final (Insta) e o {nn}-final-FACE.'},
    ]
    story = {
        'nora82': 'O story no ar é o dos campos trancados (00h10 de 27/11, Insta e Face): vence ~00h10 de 28/11. Não precisa postar story agora.',
        'nora83': 'O story no ar é o dos campos trancados (00h10 de 27/11, Insta e Face): vence ~00h10 de 28/11. Não precisa postar story agora.',
        'nora84': ('ANTES de postar o nora84: reposte o story dos campos trancados (story-2611-trancado) no Insta e no Face, com o adesivo de link de sempre '
                   '(STORYIG no Insta, FACE no Face): o de 27/11 vence ~00h10 de 28/11. Antes de abrir o Insta, confira o IP e os EUA no mylocation.org.'),
    }[nn]
    P['story'] = {'ja_postado': True, 'nota': story}
    teste_txt = ('Este vídeo NÃO testa nada: é o pacote do nora81, igual (as letras + o corpo da maioria + as 2 frases de reinício + a carta na mão e a estátua '
                 'de São Miguel; o nora81 fez 1.352 views no Insta com ~9 h). Muda só a roupa e o cômodo (cada post do Insta gerado de novo). O teste de 27/11 foi o '
                 'nora81; o “free” no CTA começa em 28/11 (decisão do aluno, 14h07). A medida, com ~24 h: as views, a retenção aos 3 s e as visitas ao perfil, contra o nora81.')
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
             'as letras na frente e as 2 frases de reinício do nora81 (o T03 e o começo do T11); a data diz “before Saturday, November twenty-eighth”. Com a carta na mão, o T11 diz “get” no lugar de “receive” (regra da carta).'),
            (f'Insta e Face às {v["hora"]}. No Face: abre com o {tf1} (as letras, outro arquivo) e termina mandando para o 1º comentário; sem a ameaça, o dinheiro, '
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
    for nn, rot in (('nora82', 'Painel nora82 · o pacote do nora81, no quarto · 27/11 17h'),
                    ('nora83', 'Painel nora83 · o pacote do nora81, na sala · 27/11 20h30'),
                    ('nora84', 'Painel nora84 · o pacote do nora81, à escrivaninha · 28/11 0h')):
        P, n, pal = montar(nn)
        print(nn, n, 'takes,', pal, 'palavras')
        salvar(P, nn, rot)
