# Painéis do dia 12/11/2026 (quinta): nora61 (16h, o longo), nora62 (20h, o curto, 2 versões) e nora63 (00h, POV de amor).
# Grade nova (Clone R28 e R29): Insta 3 por dia (16h, 20h, 00h), o mesmo vídeo no Face nessas horas.
# Corpo novo "the hardest part is over" + 2027 (Clone R25, R26), falas novas revisadas pelo Clone (R33).
# Cena: a manha1111-IMG (a do nora55, o maior do Face; decisão de 12/11 ~12h05, R32: o que validou se mantém).
# Todas as falas do dia saem numa sessão só do agente, no painel do nora61.
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-1211/build_dia_1211.py
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
STORYIG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'

# ------------------------------------------------------------------ falas (Clone R26 + R33)
F = {
    'H': "If this video finds you on Thursday, November 12th, take a deep breath: the hardest part of your year is over.",  # R26 T1 (o longo)
    'W': "You carried heavy emotional weight for months, quietly wondering if anyone truly understood the quiet battles you fought.",  # R26 T2
    'G': "Today that heavy fog is finally clearing, making room for true inner peace, clarity, and genuine emotional ease.",  # R26 T3
    'D': "When your energy aligns with this new chapter, everything you desire begins to meet you with gentle grace.",  # R26 T4 (Trustpilot nos últimos 3 s)
    'K': "This shift doesn't happen for every woman. Tap my photo and check my story to see what twenty twenty-seven holds for you.",  # R26 T5 = o T04 da noite de 11/11, que passou de 1ª
    'S': "If you're holding your phone on Thursday, November 12th, wondering if things will get lighter, this is for you.",  # R33: Take 1 do curto
    'L1': "If this finds you tonight, the love you've been quietly hoping for hasn't forgotten you.",  # R33, sem o "take a breath" (o longo abre com ele)
    'L2': "Imagine waking up next to someone who stays, who chooses you every day, and makes home finally feel like peace.",  # R33
    'L3': "Tap my photo and check my story: three quick questions show what twenty twenty-seven brings to your love life.",  # R33
}
L2_RESERVA = "Imagine someone who stays, who chooses you every single day, and makes your home finally feel like peace."
K_RESERVA = "This shift doesn't happen for every woman. Open my story to see what twenty twenty-seven holds for you."
GERA = ['H', 'W', 'G', 'D', 'K', 'S', 'L1', 'L2', 'L3']
SUF = {'H': 'T01-hardest-part', 'W': 'T02-heavy-weight', 'G': 'T03-fog-clearing', 'D': 'T04-new-chapter', 'K': 'T05-cta-2027',
       'S': 'T01b-curto-celular', 'L1': 'L1-amor', 'L2': 'L2-amor', 'L3': 'L3-amor-cta'}
ROT = {'H': 'T01', 'W': 'T02', 'G': 'T03', 'D': 'T04', 'K': 'T05', 'S': 'T01b', 'L1': 'L1', 'L2': 'L2', 'L3': 'L3'}
TXT = {'H': 'o Take 1 do longo: a data de quinta + "the hardest part of your year is over" (R25, R26)',
       'W': 'a dor: o peso que ela carregou calada (R26)', 'G': 'a promessa: a névoa saindo, paz e clareza (R26)',
       'D': 'o desejo: tudo o que ela quer começa a vir (R26); a avaliação real entra nos últimos 3 s',
       'K': 'o CTA: não acontece com toda mulher + foto e story + 2027 (R24, R26)',
       'S': 'o Take 1 do curto: a data + a situação (celular na mão, esperando ficar mais leve; R33)',
       'L1': 'POV de amor (só a voz): o amor que ela espera não a esqueceu (R31, R33)',
       'L2': 'POV de amor (só a voz): a cena do futuro, alguém que fica (R33)',
       'L3': 'POV de amor (só a voz): o CTA com 2027 e a vida amorosa (R31, R33)'}

C = dict(  # a cena da manhã de 11/11 (aprovada em 11/11 ~01h55), igual ao build_dia_1111.py
    img='manha1111-IMG', pre='d1211', nome='cena da manhã (escritório)',
    cel='her right arm on the left side of the frame', canto='bottom-left', livre_mao='her left hand on the right side of the frame', lado_gesto='right', mao='left',
    roupa_pt='regata preta canelada e ajustada, de gola quadrada + moletom cinza bem largo, aberto e meio caído nos ombros',
    roupa_cont='her plain black fitted square-neck tank top and the very oversized, open heather-grey zip-up hoodie hanging loose over it',
    repouso='rests at collarbone height, her fingers lightly holding a lock of her hair over the edge of the open hoodie', volta='the same spot at collarbone height',
    quando='in the daytime', onde='a real, lived-in American home office', luz='lit only by soft daylight from a window on the right side of the frame',
    fundo='the plain light wall, the office chair behind her, the shelf and the window light', visual='soft daylight from a window in the background')

GESTO = {
    'H': 'during the first half of the take her shoulders rise and fall once with a slow, visible exhale and a soft look, in the closing half a warm, relieved smile appears and she gives one small nod',
    'W': 'during the first half of the take she holds a soft, understanding look with her head tilted slightly, in the closing half she gives one slow nod with a gentle smile',
    'G': 'during the first half of the take her eyebrows lift with a joyful look, in the closing half she lifts her {mao} hand to the height of her shoulder with the palm up and then returns it to {volta} with a warm smile',
    'D': 'during the first half of the take she holds a calm, knowing look, in the closing half she tilts her head slightly with a gentle, reassuring smile',
    'S': 'during the first half of the take she holds a soft, understanding look with her head tilted slightly, in the closing half she gives one slow nod with a warm, reassuring smile',
    'L1': 'during the first half of the take she holds a tender, soft look, in the closing half a small warm smile appears and she gives one slow nod',
    'L2': 'during the first half of the take her eyes glance briefly up and to the left side of the frame with a dreamy look while her hand stays still, in the closing half her eyes return to the lens with a warm smile',
}


def nome(k):
    return f"{C['pre']}-{SUF[k]}"


def dur(k):
    return '8' if len(F[k].split()) <= 17 else '10'


def creditos(ks):
    return sum(12 if dur(k) == '8' else 15 for k in ks)


def base_mov(d, g):
    return (f'Throughout the whole {d} seconds she keeps an unchanged handheld selfie framing, {C["cel"]} stays extended toward the camera '
            f'holding the phone out of frame and never moves, {C["livre_mao"]} {C["repouso"]} except during the one small '
            f'gesture described here, which always happens at the height of her shoulder on the {C["lado_gesto"]} side of the frame and never in front of her face or mouth, and her eyes '
            f'stay on the lens, {g}, and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; the camera keeps only a tiny '
            'natural handheld sway with no zoom and no cuts, the braid stays on the right side of the frame, everything else in the room stays still and each hand has exactly five fingers.')


def mov_cta():  # CTA sem gesto de mão (lição do T04 de 10/11: mão descendo = filtro do Flow)
    return (f'Throughout the whole 10 seconds she keeps an unchanged handheld selfie framing; {C["cel"]} stays extended toward the camera '
            f'holding the phone out of frame and never moves; {C["livre_mao"]} stays still and {C["repouso"]} for '
            'the whole clip and never moves down; her eyes stay on the lens; during the first half of the take she holds a warm, confident look, and in the closing half she gives one '
            'small encouraging nod with a warm smile; from the end of the final sentence until the clip ends she keeps her lips closed and silent; the camera keeps only a tiny natural '
            'handheld sway with no zoom and no cuts, the braid stays on the right side of the frame, everything else in the room stays still and each hand has exactly five fingers.')


def mov(k):
    if k in ('K', 'L3'):
        return mov_cta()
    return base_mov(8 if dur(k) == '8' else 10, GESTO[k].format(volta=C['volta'], mao=C['mao']))


COMUNS = {('of', 'the'), ('and', 'the'), ('to', 'the'), ('in', 'the'), ('on', 'the'), ('at', 'the'), ('for', 'a'), ('of', 'her'), ('and', 'her'),
          ('as', 'if'), ('the', 'lens'), ('her', 'left'), ('and', 'then'), ('the', 'hand'), ('she', 'gives'), ('the', 'height'), ('a', 'warm'), ('with', 'a')}
for k, f in F.items():
    assert len(f.split()) <= 22, (k, len(f.split()))
    fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(k).lower())
    sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS
    assert not sobra, (k, sobra)
    assert 'private' not in f.lower() and 'card' not in f.lower() and 'portal' not in f.lower(), k


def livre():
    return (f'Casual handheld iPhone front-camera selfie video {C["quando"]} in {C["onde"]}, looking exactly like a real phone video, {C["luz"]}. '
            'CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, the thin braid wrapped with small gold rings hanging down on the right side of the frame, '
            'the small flat gold crescent moon with three tiny gold stars on her cheek on the left side of the frame, her star-and-moon drop earrings, her thin gold Venus necklace, '
            f'the thin gold bracelets on her {C["mao"]} wrist, the gold sun ring on her {C["mao"]} hand and {C["roupa_cont"]} stay exactly as in the reference image; the framing is exactly '
            f'the one of the reference image, a close selfie with her face large and centered and her eyes at about one third of the frame height; {C["cel"]} '
            f'stays extended toward the camera holding the phone out of frame, running off the {C["canto"]} corner, and never moves; {C["livre_mao"]} '
            f'{C["repouso"]} and only lifts for the one small gesture of a take, at the height of her shoulder on the {C["lado_gesto"]} side of the frame, never in front of her face '
            f'or mouth; {C["fundo"]} stay exactly where they are; natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter, no glow and '
            'no sparkles; the camera has only a tiny natural handheld sway, no zoom, no cuts and no reframing; no phone, object, person, animal or text appears or disappears; '
            'each hand always has exactly five fingers; no on-screen text, no captions, no logos; real quiet room ambient sound only, no music. SPEECH RULE for every take: she '
            "says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added sentence before, between or "
            'after; numbers are spoken as words (November 12th as "November twelfth", twenty twenty-seven exactly as written); when she finishes the last '
            'word she closes her lips, stays silent and keeps a calm still expression until the clip ends.')


def prompt_manual(fala, movimento, seg='10', fala_s='about 8 seconds'):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    return (f'Create a single continuous {seg}-second video clip using the supplied reference image as the first frame. The same woman from the image speaks directly '
            f'to her phone camera in a casual handheld selfie video at home {C["quando"]}.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + fala + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            f'VOICE PACING: medium pace (155 to 180 words per minute), {fala_s} of speech; when she finishes the last word she closes her lips and stays silent '
            'with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + movimento + '\n\n'
            f'VISUAL: realistic casual iPhone front-camera selfie video, {C["visual"]}, natural skin texture with visible pores, '
            'slight phone grain, everything in focus, no bokeh, no filter.\n\n'
            'CAMERA: handheld, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n'
            'AUDIO: only her voice and quiet room ambience; no music, no other voices, no sound effects.\n\n'
            'CONTINUITY: her face, long black wavy hair, the thin braid with small gold rings, the small gold crescent moon with three tiny gold stars on her cheek, '
            f'her star-and-moon earrings, her gold Venus necklace, her gold sun ring and bracelets, {C["roupa_cont"]} and the room behind her stay '
            'exactly as in the reference image; no phone, object, person or text appears; each hand has exactly five fingers; no on-screen text, captions or logos.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.')


def config():
    cf = copy.deepcopy(CFG)
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = 'colar o texto abaixo (fechado pela manha1111-IMG, aprovada em 11/11)'
                campo['copiar'] = livre()
    return cf


PRE_LUCAS = ('Below, you will find several prompts, each corresponding to a different video. Please generate all the videos in sequential order, from the first prompt to the last.\n'
             'Maintain the exact same voice across all videos, ensuring EXACTLY THE SAME VOLUME, with no variations in background, intonation, or vocal clarity. Use the attached image as both the first and last frame of every generated video.\n'
             'Please submit ALL generation requests at once and in the correct order, so that all videos can be generated simultaneously.\n'
             'If the generation of any video fails, please resubmit ONLY the item that failed until it is successfully generated.')


def agente(ks):
    nomes = [f'{i + 1} = {nome(k)}' for i, k in enumerate(ks)]
    return {
        'imagem': C['img'],
        'intro': 'Anexe a imagem, cole o aviso e, embaixo dele, o bloco “COPIAR TUDO JUNTO” da Central.',
        'aviso_tag': 'cole antes do bloco da Central',
        'aviso': (f'Vou te enviar {len(ks)} prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um com o devido '
                  'número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.'),
        'passos': [
            'Conta do Flow: contatocaram. Abra um PROJETO NOVO no Flow (se o agente parar, projeto novo, não pasta nova) e uma conversa nova no agente.',
            'Nas configurações do agente: Omni 1.1 Flash (o Flow abre no 1.2, que cobra o dobro), 9:16, 720p, gerar sem pedir aprovação.',
            f'Anexe só a {C["img"]} (a de ontem de manhã, a do nora55).',
            'Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.',
            'Renomeie cada take com o nome da lista (o número é a ordem): ' + ' · '.join(nomes) + '. '
            'Se ele não renomear, mande na mesma conversa: “Now rename each video with the correct number from the prompt.”',
            f'Confira na grade, pelo nome, se os {len(ks)} saíram. Se um falhar por política: mande na mesma conversa “Please generate video X from my previous message again, with the same prompt.” '
            '(X = o número dele na lista). Se falhar de novo, não insista: me mande o print.',
            f'Se o T05 (o 5º, o CTA) falhar 1 vez, gere à mão: Vídeo → Frames → 9:16 → Omni 1.1 Flash → 720p → 10 s → x1; Início = {C["img"]}; Fim = vazio; cole o prompt abaixo, '
            f'inteiro (15 créditos), e renomeie para {nome("K")}. PROMPT: ' + prompt_manual(F['K'], mov_cta()),
            f'Se o T05 falhar também no Frames: o mesmo caminho com este prompt reserva (troca o “Tap my photo and check my story” por “Open my story”, que passou ontem de manhã) e o mesmo nome. PROMPT RESERVA: ' + prompt_manual(K_RESERVA, mov_cta()),
            f'Se o L2 (o 8º) falhar 2 vezes (o filtro pode barrar o “waking up next to someone”), gere à mão no Frames, do mesmo jeito, com esta fala reserva, e renomeie para {nome("L2")}. PROMPT RESERVA: '
            + prompt_manual(L2_RESERVA, base_mov(10, GESTO['L2'].format(volta=C['volta'], mao=C['mao']))),
            'Se o agente parar no meio (por exemplo, “alta demanda”): responda na MESMA conversa, sem anexar nada: “Please continue and generate videos X to Y from my previous message, in the same order.” '
            '(troque X e Y pelos números que faltaram). Se ele gerar só o 1º e parar de novo: cole antes do bloco da Central o “pré-prompt do Lucas” (abaixo) e mande de novo só os que faltaram.',
            'Se o agente disser que não dá para usar a imagem como quadro inicial e final com fala: gere à mão: Vídeo → Frames → 9:16 → Omni 1.1 Flash → 720p → 10 s (ou 8 s, conforme a lista) → x1; '
            f'Início = {C["img"]}; Fim = vazio; no prompt, só o texto do prompt daquele take.',
            'Pré-prompt do Lucas (só se precisar): ' + PRE_LUCAS,
        ],
    }


# ------------------------------------------------------------------ peças fora do agente (pré-gancho da vela, paisagens do POV, piloto do 1.2)
VELA_IMG = ('RAW photo, extreme close-up taken with a phone held about 25 centimeters away at the height of a light wooden home-office desk: a single plain white pillar candle '
            'with an unlit black wick stands on the desk, a very thin wisp of smoke barely rising from the wick; beside it, two small clear quartz crystals lie still on the wood; '
            'the room is dim, the daylight behind is softened by a sheer curtain on the right side of the image, cool grey light with deep soft shadows; the candle stands in the '
            'lower middle of the image with the tip of the wick at about 45 percent of the image height; looks exactly like a real casual iPhone photo, slight phone grain, '
            'everything in focus, no bokeh, no filter, natural colors; no person, no hand, no match, no lighter, no cards, no text, no logo, no watermark; '
            'photorealistic, unretouched, candid, UGC style, vertical 9:16')
VELA_VID = ('Use the supplied image as the first frame. Locked extreme close-up of the white pillar candle on the wooden desk, the phone held still with only a tiny natural handheld '
            'sway, no zoom, no cuts. In the very first second a tiny golden spark crackles on the black wick by itself; at about one second the wick catches and a bright flame '
            'blooms upward to about four centimeters tall with a soft whoosh, then keeps dancing and flickering, its warm amber glow spreading over the desk and making the two clear '
            'quartz crystals beside it sparkle; the flame keeps moving in every second until the clip ends. No person, no hand, no match and no lighter appear; nothing else appears '
            'or disappears; the candle and the crystals stay in place. AUDIO: close ASMR sound of the tiny spark crackle, a soft whoosh as the flame blooms, then a quiet wick '
            'crackle; no music, no voice. Realistic phone video, natural colors, slight phone grain, no text, no captions, no logos.')
LAGO_IMG = ('RAW photo taken with a phone at golden hour: a quiet lake in the American countryside at sunset, calm water reflecting a soft peach and lavender sky, a small old wooden '
            'dock in the lower part of the image, tall grass at the edges, the warm low sun near the horizon on the left side of the image, a gentle haze; peaceful, romantic and '
            'hopeful mood; the upper 25 percent of the image is plain open sky with nothing in it; vertical 9:16; looks exactly like a real casual iPhone photo, slight phone grain, '
            'natural colors, everything in focus, no bokeh, no filter; no person, no couple, no animal, no text, no logo, no watermark; photorealistic, unretouched')
PILOTO = prompt_manual(F['S'], base_mov(10, GESTO['S'].format(volta=C['volta'], mao=C['mao'])))

EXTRAS = {
    'titulo_secao': 'Peças fora do agente (Flow, à mão)',
    'conceito': ('Quatro peças rápidas, no mesmo projeto do Flow: a vela do pré-gancho do curto no Insta, as paisagens do POV de amor das 00h e o piloto do Omni 1.2 em 360p. '
                 'As imagens custam 0 crédito.'),
    'modo': 'Imagem: Flow → Imagem · 9:16 · Nano Banana Pro · x4, sem anexar nada. Vídeo: Flow → Vídeo → Frames → 9:16; Início = a imagem indicada; Fim = vazio.',
    'etapas': [
        {'titulo': 'Imagem da vela (pré-gancho do curto no Insta)', 'nome': 'd1211-PRE-vela-IMG', 'tipo': 'img', 'anexar': 'nada',
         'quadros': 'x4, 0 crédito. Escolha você mesmo a que tiver a vela mais nítida, o pavio bem visível e nenhuma mão ou texto; renomeie para d1211-PRE-vela-IMG.',
         'prompt': VELA_IMG},
        {'titulo': 'Vídeo da vela acendendo sozinha (8 s)', 'nome': 'd1211-PRE-vela', 'tipo': 'vid', 'duracao': 8,
         'quadros': 'Omni 1.1 Flash · 720p · 8 s · x1 (12 créditos). Início = d1211-PRE-vela-IMG; Fim = vazio. Eu uso só 2 a 3 s dele.', 'prompt': VELA_VID},
        {'titulo': 'Paisagens do POV de amor (00h)', 'nome': 'd1211-POV-lago-1 a 4', 'tipo': 'img', 'anexar': 'nada',
         'quadros': 'x4, 0 crédito. Baixe as 4 (se alguma tiver pessoa, texto ou defeito, gere de novo). Eu monto o POV com elas.', 'prompt': LAGO_IMG},
        {'titulo': 'Piloto do Omni 1.2 em 360p (o Take 1 do curto, duplicado)', 'nome': 'd1211-T01b-PILOTO-12-360p', 'tipo': 'vid', 'duracao': 10,
         'quadros': ('Omni 1.2 · 360p · 10 s · x1 (~10 créditos; o 1.1 Flash sai do Flow em 05/12). Início = manha1111-IMG; Fim = vazio. '
                     'Baixe em 720p e me mande junto: eu comparo com o d1211-T01b-curto-celular (rosto, boca, voz, nitidez).'),
         'prompt': PILOTO},
    ],
}

# ------------------------------------------------------------------ textos
HASH = '#manifestation #lawofattraction #innerpeace #newchapter'
VIDEOS = {
    61: dict(hora='16h', tipo='longo', usa=['H', 'W', 'G', 'D', 'K'], prova='07-karina',
             caixa=('THURSDAY, NOVEMBER 12TH\nif this year felt heavy,\nthis message is for you', 'the hardest part of your year is over.'),
             insta=('If this video finds you on Thursday, November 12th, take a deep breath ✨\nThe hardest part of your year is over. Your private reading is waiting in my story 🔮\n'
                    f'Comment "peace" to claim it ✨\n{HASH}'),
             face=('The hardest part of your year is over, love ✨\nSee what 2027 holds for you: the link is in the comments 🔮\n' + HASH),
             fix_insta='Tap my profile picture above to see what 2027 holds for you in my stories ✨',
             fix_face=f'See what 2027 holds for you here ✨ 👉 {FB}'),
    62: dict(hora='20h', tipo='curto', usa=['S', 'G', 'K'], prova=None,
             caixa=('THURSDAY, NOVEMBER 12TH\nif you\'re waiting for\nthings to get lighter', 'this is for you.'),
             insta=('Holding your phone on Thursday, wondering if things will get lighter? This is for you ✨\nYour private reading is waiting in my story 🔮\n'
                    'Comment "lighter" to claim it ✨\n#manifestation #lawofattraction #newbeginnings #2027'),
             face=('Wondering if things will get lighter? This is for you, love ✨\nSee what 2027 holds for you: the link is in the comments 🔮\n'
                   '#manifestation #lawofattraction #newbeginnings #innerpeace'),
             fix_insta='Tap my profile picture above to see what 2027 holds for you in my stories ✨',
             fix_face=f'Your 2027 reading is right here 🔮 👉 {FB}'),
    63: dict(hora='00h (da noite de 12 para 13/11; 22h em Nova York, ainda quinta)', tipo='pov', usa=['L1', 'L2', 'L3'], prova=None,
             caixa=('if you\'re still hoping\nfor real love,\nthis is for you', 'hasn\'t forgotten you.'),
             insta=('The love you\'ve been hoping for hasn\'t forgotten you 💜\nYour private reading is waiting in my story 🔮\n'
                    'Comment "love" to claim it ✨\n#manifestation #lovemanifestation #soulmate #2027'),
             face=('The love you\'ve been hoping for hasn\'t forgotten you 💜\nSee what 2027 brings to your love life: the link is in the comments 🔮\n'
                   '#manifestation #lovemanifestation #soulmate #innerpeace'),
             fix_insta='Tap my profile picture above to see what 2027 brings to your love life in my stories 💜',
             fix_face=f'See what 2027 brings to your love life here 💜 👉 {FB}'),
}
PROVA = {'07-karina': ('Karina G. (EUA)', 'Wonderful, I feel so connected, this feels so real')}

RESP = {
    'aviso': ('Só no Face. Mulher que comentou: responda o comentário (sem link) e mande o direct em 2 passos (Clone R30): o passo 1 sem link; o link só quando ela responder. '
              'Homem e perfil sem foto ou com nome de empresa: só a resposta pública, apontando para o story (“tap my photo, your 2027 reading is in my story”), sem direct. '
              'No máximo ~10 directs por hora e 30 a 40 por dia, com espaço entre eles; troque [name] pelo primeiro nome; nunca o mesmo texto seguido. “Scam” e ataque: ocultar, sem responder.'),
    'link': FB,
    'comentario': ['💜 I just sent you a message, take a look ✨', '✨ Check your messages, beautiful 🌙', '🔮 I left you a little message 💫'],
    'dm': ['Hi [name] 💜 thank you for your comment! Would you like me to send you your 2027 reading?',
           'Hi [name] ✨ I\'m so glad this message found you. Can I send you your 2027 reading?',
           'Hello [name] 🌙 your comment made my day. Would you like the link to your 2027 reading?'],
    'dm2': ['Here it is 💜\n{link}\nThree quick questions, and your reading is ready.',
            'Of course ✨ here\'s your 2027 reading:\n{link}',
            'Here you go 🌙\n{link}\nTake a deep breath before you start.'],
}


def xy(x, y):
    return f'X {round(x / 100 * 720 - 360)} · Y {round(640 - y / 100 * 1280)}'


NUMS = {61: [('222', 18, 10.5, 'alto à esquerda', 'branco', '#FFFFFF', 13), ('11:11', 82, 10.5, 'alto à direita', 'verde-limão', '#7CFF4F', 16), ('888', 18, 46.9, 'à esquerda, na altura do ombro', 'laranja', '#FF9F1C', 11)],
        62: [('11:11', 82, 10.5, 'alto à direita', 'amarelo-ouro', '#FFD21F', 15), ('888', 18, 10.5, 'alto à esquerda', 'rosa-choque', '#FF4FD8', 12), ('222', 18, 46.9, 'à esquerda, na altura do ombro', 'ciano', '#3DE0FF', 11)]}


def montar(n):
    v = VIDEOS[n]; nn = f'nora{n}'; usa = v['usa']; gera = GERA if n == 61 else []
    hora_curta = v['hora'].split(' (')[0]
    perfil = copy.deepcopy(P46['perfil']); perfil.pop('teste', None)
    caixa, caixa_fim = v['caixa']
    p = {
        'enxuto': True, 'imagens_titulo': 'Imagem (a manha1111-IMG de ontem, não gerar)',
        'perfil': perfil, 'trava_referencia': P46['trava_referencia'], 'figurino': C['roupa_cont'], 'excecao_estilo': '',
        'ocultar_bloco_agente_imagem': True,
        'roteiro': {'id': f'{nn}-DIA-1211-{v["tipo"].upper()}',
                    'titulo': f'{nn} · 12/11 (quinta), {hora_curta} · ' + {'longo': 'o longo do corpo novo (tsunami inteiro, com a avaliação da Karina)',
                                                                           'curto': 'o curto do corpo novo (2 versões: vela no Insta, tsunami no Face)',
                                                                           'pov': 'POV de amor (só a voz da Nora sobre paisagem)'}[v['tipo']],
                    'duracao_total': {'longo': 50, 'curto': 25, 'pov': 28}[v['tipo']],
                    'descricao_instagram': v['insta'], 'descricao_face': v['face']},
        'refs': ['manha1111-IMG em todos os takes (a de ontem de manhã)'],
        'imagens': [{'rotulo': 'IMAGEM 1 · manha1111-IMG', 'cena': '(gerada em 11/11, no painel do nora55)', 'anexar': 'nada (já existe)'}],
        'videos': [{'rotulo': ROT[k], 'cena': TXT[k], 'duracao': dur(k), 'primeiro_quadro': 'IMAGEM 1 (manha1111-IMG)', 'acao': '', 'b_roll': '',
                    'fala': F[k], 'movimentacao': mov(k), 'arquivo': nome(k)} for k in (gera if gera else usa)],
        'texto_tela': {'hook': caixa, 'hook_comeca': 'o primeiro quadro do pré-gancho' if v['tipo'] != 'pov' else 'o primeiro quadro', 'hook_termina': caixa_fim, 'hook_alt': '', 'extras': []},
        'comentario_fixado': {'insta': v['fix_insta'], 'face': v['fix_face']},
        'respostas_face': RESP,
        'imagem_reutilizada': {'arquivo': 'manha1111-IMG', 'aviso': 'Use a manha1111-IMG de ontem (a do nora55): anexe-a no agente. Não gere imagem nova da Nora hoje.'},
        'story': {'ja_postado': True, 'nota': 'O story de hoje é o story-1211 (a varanda com o texto de 2027, adesivo “See your 2027”), postado ao meio-dia; vence ~12h de 13/11. Não poste outro.'},
    }

    # ---------------- mapa da tela (eu ponho tudo na edição, P45)
    mt = copy.deepcopy(P49['mapa_tela'])
    mt['numeros'] = [dict(t=a, x=x, y=y, onde=o, cor_nome=cn, cor=co, tamanho=tm) for (a, x, y, o, cn, co, tm) in NUMS.get(n, [])]
    linhas = caixa.split('\n')
    est = []
    if n in NUMS:
        est.append({'nome': 'Números fixos espalhados (11:11, 888, 222)', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'uma cor para cada número', 'tamanho': 'um tamanho para cada número',
                    'contorno': 'Traço preto + Sombra preta, sem Plano de fundo', 'obs': '; '.join(f'{a} {cn}, {tm}, {xy(x, y)}' for (a, x, y, o, cn, co, tm) in NUMS[n]) + '. Eu ponho (P45).'})
    est.append({'nome': 'Caixa do topo: ' + ' / '.join(f'“{l}”' for l in linhas), 'fonte': 'Poppins Bold (poppins-bd)',
                'cor': 'texto preto' + ('; a 1ª linha (a data) em vermelho #E53935' if v['tipo'] != 'pov' else ''), 'tamanho': '10, em 3 linhas', 'contorno': 'Plano de fundo branco arredondado',
                'obs': 'Do 1º quadro até o fim do Take 1, acima dos olhos. Eu ponho (P45).'})
    est.append({'nome': 'Legenda (eu ponho, P45)', 'fonte': 'Poppins Bold', 'cor': 'branco, em MAIÚSCULAS; palavra-chave em amarelo-ouro #FFD21F', 'tamanho': 'uns 38 px (vídeo 720×1280)',
                'contorno': 'preto grosso', 'obs': 'A partir do Take 1 (no pré-gancho não), blocos de 2 a 4 palavras, abaixo do queixo.' + (' Some enquanto a avaliação está na tela.' if v['prova'] else '')})
    est.append({'nome': 'Faixa do CTA, versão do INSTA: “Tap my photo: your 2027 reading is in my story”', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto, “my story” em vermelho #E53935',
                'tamanho': '9', 'contorno': 'Plano de fundo branco arredondado', 'obs': 'Do CTA até o fim, no topo; com a seta vermelha embaixo à esquerda (X -288 · Y -333), apontando para a foto do perfil (Clone R29).'})
    est.append({'nome': 'Faixa do CTA, versão do FACE: “Your 2027 reading: link in the comments ⬇️”', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto, “in the comments” em vermelho #E53935',
                'tamanho': '9', 'contorno': 'Plano de fundo branco arredondado', 'obs': 'Do CTA até o fim, no topo; sem seta para a foto (12/11 11h55: no Face o link clicável é o do comentário, R31).'})
    if v['prova']:
        quem, trecho = PROVA[v['prova']]
        est.append({'nome': f'Avaliação real do Trustpilot: {quem} (“{trecho}”)', 'fonte': f'provas-trustpilot/{v["prova"]}-sem-hora.png (print real do aluno, 11/11, sem a hora relativa)',
                    'cor': '—', 'tamanho': '~84% da largura', 'contorno': 'cantos arredondados e sombra leve',
                    'obs': 'Nos últimos ~3 s do T04, sobre a blusa, longe do rosto, com a caixa “Rated 4.8 ★ by 2,200+ people” no topo (número real de 11/11). Eu ponho (P45).'})
        est.append({'nome': 'Imagens do desejo (casal e casa; a do dinheiro só no Insta)', 'fonte': 'ferramentas-painel/imagens-fixas/nora46-DESEJO-2-casal.jpg, -3-casa.jpg, -1-dinheiro.jpg',
                    'cor': '—', 'tamanho': 'cartão ~60% da largura', 'contorno': 'cantos arredondados e sombra leve',
                    'obs': 'No começo do T04 (“everything you desire begins to meet you”), ~1,5 s cada, antes da avaliação. Eu ponho (P45).'})
    if v['tipo'] == 'pov':
        est.append({'nome': 'Fundo do POV', 'fonte': 'as 4 paisagens do lago (d1211-POV-lago-1 a 4), geradas no painel do nora61', 'cor': '—', 'tamanho': 'tela cheia, zoom lento',
                    'contorno': '—', 'obs': 'Uma paisagem por frase (~7 s cada), troca com fusão curta. Sem a Nora na tela: só a voz. Eu monto tudo (P45).'})
    mt['estilos'] = est
    mt['regras'] = ['Hoje só o corpo muda (uma variável): os textos e os números seguem o visual de sempre.',
                    'Duas versões do mesmo vídeo: a do Insta (faixa do story + seta) e a do Face (faixa do comentário). Eu mando as duas.' if v['tipo'] != 'longo' or True else '']
    p['mapa_tela'] = mt

    # ---------------- corte e montagem
    corte = f'{nn}-cortado'
    lista = ', '.join(nome(k) for k in usa)
    p['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” só estes {len(usa)} takes, de uma vez: {lista}. Ela junta pela ordem do nome (já estão em ordem).',
        'nome': corte, 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pela ordem do nome (' + ', '.join(ROT[k] for k in usa) + ')',
        'depois': [f'Suba os {len(usa)} takes e espere a Prévia.', 'Aperte play com Resultado marcado: confira a primeira palavra do 1º take e a última do último.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', f'Clique em Cortar e baixar e salve como {corte}.']}
    if v['tipo'] == 'longo':
        p['edicao_linha'] = [
            {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {corte}', 'como': 'É o vídeo que saiu da FusionZ.'},
            {'quando': 'B. Pré-gancho no começo', 'texto': 'O tsunami INTEIRO: nora47-PRE-A + nora47-PRE-B, sem espelhar',
             'como': f'No começo da linha do tempo, antes do {corte}, sem música por baixo. É o do nora49 e do nora50 (68% a 72% nos 3 s; Clone R29). 0 crédito.'},
            {'quando': '1. Do Take 1 ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Começa no Take 1 (no tsunami, só o som dele).'},
            {'quando': '2. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
             'como': f'1080×1920, qualidade alta, nome {nn}-montado (acima de 30 MB, link do Drive). Eu ponho tudo e devolvo o {nn}-final (Insta) e o {nn}-final-FACE (a faixa do comentário).'}]
    elif v['tipo'] == 'curto':
        p['edicao_linha'] = [
            {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {corte}', 'como': 'É o vídeo que saiu da FusionZ.'},
            {'quando': 'B. Versão do INSTA', 'texto': 'Pré-gancho: a vela (d1211-PRE-vela), só 2 a 3 s, corte seco',
             'como': 'No começo, antes do Take 1, sem música por baixo. Use o trecho em que a chama acende (o 1º ao 3º segundo). Exporte SEM texto como ' + f'{nn}-montado-INSTA.'},
            {'quando': 'C. Versão do FACE', 'texto': 'Duplique o projeto e troque só o começo: o tsunami curto, nora47-PRE-A ESPELHADO (~4 s)',
             'como': 'O que fez o nora55 virar o maior do Face (Clone R32); espelhado para não abrir igual ao longo das 16h. Exporte SEM texto como ' + f'{nn}-montado-FACE.'},
            {'quando': '1. Nas duas versões', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB, a partir do Take 1', 'como': 'No pré-gancho, só o som dele.'},
            {'quando': '2. Me mandar', 'texto': 'Os 2 arquivos aqui no chat do Code (ou link do Drive)', 'como': f'Eu ponho os textos e devolvo o {nn}-final (Insta) e o {nn}-final-FACE.'}]
    else:
        p['edicao_linha'] = [
            {'quando': '1. Só o corte', 'texto': f'Mande o {corte} (a voz) e as 4 paisagens do lago aqui no chat', 'como': 'Não precisa CapCut agora: eu monto o POV (paisagem + voz + legenda + faixa) e devolvo as 2 versões.'},
            {'quando': '2. Música (depois que eu devolver)', 'texto': 'No CapCut: abra o nora63-final, ponha a música de sempre a −18 dB e exporte; o mesmo no nora63-final-FACE',
             'como': 'É o único passo seu na montagem do POV.'}]

    # ---------------- peças e resumo
    pecas = [{'nome': 'manha1111-IMG', 'de': 'manha1111-IMG (do painel do nora55)', 'tipo': 'imagem 1', 'status': 'reutilizar', 'descricao': 'A imagem da manhã de ontem, a do nora55.'}]
    for k in usa:
        if gera:
            pecas.append({'nome': nome(k), 'tipo': 'take', 'status': 'gerar', 'creditos': 12 if dur(k) == '8' else 15, 'descricao': f'“{F[k]}”'})
        else:
            pecas.append({'nome': nome(k), 'de': f'{nome(k)} (do painel do nora61)', 'tipo': 'take', 'status': 'reutilizar', 'descricao': f'“{F[k]}”', 'fala': F[k]})
    for k in gera:
        if k not in usa:
            dono = 62 if k == 'S' else 63
            pecas.append({'nome': nome(k), 'tipo': 'take', 'status': 'gerar', 'creditos': 12 if dur(k) == '8' else 15, 'descricao': f'Para o nora{dono}: “{F[k]}”'})
    if n == 61:
        pecas += [{'nome': 'd1211-PRE-vela-IMG e d1211-PRE-vela', 'tipo': 'pré-gancho', 'status': 'gerar', 'creditos': 12, 'descricao': 'A vela acendendo sozinha (só para o curto do Insta, nora62).'},
                  {'nome': 'd1211-POV-lago-1 a 4', 'tipo': 'imagem', 'status': 'gerar', 'creditos': 0, 'descricao': 'As paisagens do POV de amor (nora63).'},
                  {'nome': 'd1211-T01b-PILOTO-12-360p', 'tipo': 'piloto', 'status': 'gerar', 'creditos': 10, 'descricao': 'O Take 1 do curto no Omni 1.2 em 360p, para comparar.'}]
    if v['prova']:
        pecas.append({'nome': 'avaliação da Karina', 'tipo': 'prova', 'status': 'reutilizar', 'onde': 'Eu ponho na edição, nos últimos 3 s do T04. Você não faz nada.'})
    tot = creditos(GERA) + 12 + 10
    decisao = {
        'longo': [f'GERAR AGORA, numa sessão só do agente (contatocaram): os {len(GERA)} takes do dia (o longo, o Take 1 do curto e as 3 falas do POV de amor), mais as 4 peças à mão. Créditos: ~{tot}.',
                  'Montar: o tsunami INTEIRO + T01 a T05. A avaliação da Karina e as imagens do desejo eu ponho no T04.',
                  'Postar às 16h, ao vivo, no Insta (o nora61-final) e no Face (o nora61-final-FACE). No Face, logo depois, o comentário da Página com o link.',
                  'É o 1º post no Insta depois de ~20 h: se passar de 300 views, a conta não está no “limbo” (aula 39). Me mande os prints com ~3 h.'],
        'curto': ['Usa 3 takes do painel do nora61: T01b + T03 + T05 (~25 s), sem avaliação (como o nora55, Clone R32).',
                  'Duas versões: Insta com a vela de 2 a 3 s; Face com o tsunami curto espelhado (o que ganhou lá).',
                  'Postar às 20h, ao vivo: Insta o nora62-final; Face o nora62-final-FACE e, logo depois, o comentário da Página com o link.'],
        'pov': ['Usa as 3 falas de amor do painel do nora61 (L1 + L2 + L3, ~28 s), só a voz, sobre as paisagens do lago.',
                'Eu monto o POV inteiro (fundo, legenda, faixa); você só põe a música no fim.',
                'Postar às 00h, ao vivo: Insta o nora63-final; Face o nora63-final-FACE e o comentário da Página com o link.'],
    }[v['tipo']]
    p['pecas'] = {'lista': pecas, 'decisao': decisao, 'titulo_decisao': 'Resumo'}

    if gera:
        p['central'] = {'imagem_unica': True,
                        'conferir': ('Conferir em cada take: é a Nora da manha1111-IMG (rosto, lua com 3 estrelinhas, trança, brincos, colar de Vênus, regata preta e moletom cinza); ela fala uma vez só, '
                                     'em inglês, com "November twelfth" e "twenty twenty-seven"; o braço do celular não se mexe; a mão livre só faz o gesto do T03, na altura do ombro; '
                                     'sem texto, legenda ou música. Renomeie com o nome da lista.'),
                        'passos': [], 'config': config(), 'agente': agente(GERA),
                        'colagens': [{'titulo': f'{nn}: os {len(GERA)} takes do dia ({", ".join(ROT[k] for k in GERA)})', 'fala': ' '.join(F[k] for k in GERA),
                                      'movimentacao': [mov(k) for k in GERA], 'takes': list(range(len(GERA)))}]}
        p['pre_gancho'] = EXTRAS
        ordem = ['pecas', 'imagens', 'central', 'cenas', 'agente', 'prehook', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    else:
        p['central'] = {'imagem_unica': True, 'conferir': '', 'passos': [], 'config': config(), 'agente': agente(['S']), 'colagens': []}
        ordem = ['pecas', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    p['ordem'] = ordem
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', f'<title>Painel {nn} · dia 12/11</title>', html, count=1)
    (R / f'PAINEL-NORA{n}.html').write_text(html, encoding='utf-8')
    print('ok', nn, v['tipo'], 'usa', [ROT[k] for k in usa], 'gera', len(gera), 'créditos dos takes', creditos(gera) if gera else 0)


for n in VIDEOS:
    montar(n)
