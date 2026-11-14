# Painéis do dia 14/11/2026: nora64 (o loop de 8 s sem fala, Insta e Face, ~21h) e nora65 (a Nora de frente com a carta dourada, Face assim que editado, Insta ~1h).
# Decisões: Clone R44 (o loop), R45 (a carta só na imagem), R46 (o loop à noite; o das 0h com a carta desde o quadro 0; sem corte de cenário) e R47 (as falas);
# CLAUDE.md 14/11 19h15 (a headline "FOR THE TIRED WOMAN: / 2027 IS FINALLY YOUR YEAR"; a prova troca de avaliação); Omni 1.2 Flash em 360p.
# O "pode montar" veio às 19h15 de 14/11. O aluno escolhe a imagem pela lista de conferência (pressa da noite) e me manda a escolhida.
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-1411/build_dia_1411.py
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
CARTA = ('a plain rectangular golden card about the size of a playing card, held upright with its front facing the camera, smooth metallic gold with only a simple embossed '
         'sun symbol in the center, no letters, no numbers, no words, no pictures and no tarot imagery')

# ------------------------------------------------------------------ prompts de imagem (mesmo esqueleto do prompt_img de 11/11)
PELE = ('natural matte skin finish with visible pores and fine skin texture, subtle natural micro-imperfections, faint under-eye texture, natural variation in tone between face, '
        'neck and hands, delicate peach fuzz, no oily or wet shine and no specular hotspots on the forehead, nose or cheeks, no smoothing, skin tone, age and features exactly as in '
        'the reference image,\n'
        'hair exactly as in the reference image, with a few fine flyaway strands at the hairline and no floating strands, believable fabric weight and natural creases, all clothing '
        'unbranded, anatomically correct hands with five natural fingers each, nothing duplicated or floating, lifelike anatomy and proportions with natural facial asymmetry, caught '
        'in a natural moment rather than posed, eyes with natural moisture and small centred catchlights,\n')
FIM = ('no film emulation, straight smartphone frame, no date stamp, no text, no watermark, natural phone colors, no color grading, natural skin tone preserved separately from the colour grade,\n'
       'photorealistic, unretouched, candid documentary, UGC style, no studio lighting, no filters, no tattoos, no extra, fused or missing fingers, no duplicated or floating objects, no '
       'warped reflections or architecture, no readable text, logos, captions or watermarks anywhere (the card has no writing), no oily, wet, waxy or plastic skin, no beauty retouching '
       'or airbrushing, no HDR look or over-sharpening, no exaggerated background blur, no fortune-teller costume, no tarot cards,\n'
       'character consistency: identical face, same skin tone, same hair, same body proportions as the reference image — only wardrobe, environment, and pose change')
JOIAS = ('small flat shiny gold crescent moon with three tiny gold stars on the outer edge of her cheekbone near the temple, on the left side of the image; long gold '
         'star-and-moon drop earrings; thin gold necklace with a small Venus pendant; thin gold bracelets; gold sun ring; hazel-green eyes; long, loose, softly wavy jet-black hair '
         'falling past her shoulders, not tied back; one thin braid wrapped with small gold rings clearly visible at the front, on the right side of the image; clean forehead with no jewelry,\n')


def img_loop():
    return ('RAW photo of the exact same character from the attached reference image, preserving every facial feature, identity, age, ethnicity, skin tone, and hairstyle exactly as shown in the reference,\n'
            'warm, confident, knowing smile with her lips gently closed,\n'
            'soft deep burgundy fine-knit long-sleeve top with a round crew neck, matte, no print, no logo, ' + JOIAS +
            'photo taken from about 1 meter in front of her, at the height of her eyes, straight on (no phone, phone stand or tripod anywhere in the image): she sits at a small round '
            'dark-wood table in a cozy real American living room at night, facing the camera, framed from the waist up, centered; her left hand, on the right side of the image, holds '
            + CARTA + ', at chest height, a little to the side of her body so the whole card is visible and nothing covers her face; her right hand, on the left side of the image, rests '
            'relaxed on the table; a small purple amethyst crystal cluster and a plain white ceramic mug stand on the table in front of her; both hands are fully visible, each with '
            'exactly five fingers; she looks straight into the lens,\n'
            'FRAMING, in percent of the image height from the top: from 0 to 22 percent only the plain dark warm wall behind her, with nothing on it (this band stays empty for text); '
            'the top of her head at about 24 percent, her eyes at about 33 percent; the table edge at about 78 percent; from 85 to 100 percent only the plain dark tabletop '
            '(this band stays empty for a sticker),\n'
            'cozy real lived-in American living room at night, a plain dark warm-grey wall behind her, the edge of a beige sofa at the side of the frame,\n'
            'warm tungsten light from a small table lamp on the right side of the image and the soft glow of the golden card, a little uneven, like a real phone photo at night; no studio '
            'light, no ring light,\n' + PELE +
            'shot on a smartphone camera, iPhone 15 main camera: looks exactly like a real casual photo taken with an iPhone, slight phone grain, everything in focus, no bokeh, no filter, '
            'f/8 aperture, ISO 800, 1/60s shutter speed, natural depth of field, background stays readable, mild sensor noise in the shadows,\n' + FIM)


def img_carta():
    return ('RAW photo of the exact same character from the attached reference image, preserving every facial feature, identity, age, ethnicity, skin tone, and hairstyle exactly as shown in the reference,\n'
            'peaceful soft smile,\n'
            'soft deep navy-blue fine-knit long-sleeve top with a round crew neck, matte, no print, no logo, ' + JOIAS +
            "selfie taken with her own phone at arm's length: her right arm, on the left side of the image, is raised toward the camera and is cut off by the bottom-left corner "
            'of the frame, and the phone itself is not visible; framed from the upper waist up, her face large and centered with her eyes at about 30 percent of the image height; '
            'her left hand, on the right side of the image, holds ' + CARTA + ', close to her chest at the height of her collarbone, a little to the right of her chin, never covering '
            'her face, mouth or chin, the whole card visible, with exactly five fingers on the hand; she looks straight into the phone camera with her lips slightly parted, as if about to '
            'speak; the card is the only object in her hands,\n'
            'real lived-in American bedroom at night, a plain warm off-white wall behind her, the edge of a headboard with a cream throw blanket behind her shoulders, a small lamp at '
            'the edge of the frame,\n'
            'warm tungsten lamp light with soft low-key shadows, the golden card catching the warm light,\n'
            'only a warm bedside lamp on the right side of the image, a little uneven, like a real phone video at night; no studio light, no ring light,\n' + PELE +
            'a pillow and a book on the bed behind her, ordinary home clutter, any signage or packaging unbranded and unreadable,\n'
            'shot on a smartphone camera with iPhone 15 front camera selfie: looks exactly like a real casual photo taken with an iPhone, natural skin texture with visible pores, '
            'slight phone grain, everything in focus, no bokeh, no filter, f/8 aperture, ISO 800, 1/60s shutter speed, natural depth of field, background stays readable,\n'
            'taken by herself as a handheld selfie, slightly imperfect framing with a subtle tilt, mild sensor noise in the shadows, camera at eye level, one coherent light direction,\n' + FIM)


# 14/11 19h30: a escolhida (a 4ª opção) saiu espelhada do prompt: a carta na mão DIREITA dela (lado ESQUERDO da imagem), erguida na altura do ombro;
# a mão esquerda (lado direito da imagem) apoiada na mesa. O clipe segue a imagem escolhida.
LOOP_VID = ('Use the supplied image as the first frame. Real casual 8-second video at night from a static camera at eye height, steady, no zoom, real speed, no slow motion; no phone, '
            'phone stand or tripod ever appears in the frame. The action starts in the very first frame: from 0 to 2 seconds she brings the golden card a little closer to the lens with '
            'her right hand (the hand on the left side of the frame) while her other hand, the one on the right side of the frame, rises from the table and taps the center of the card '
            'twice with its index finger; from 2 to 5 seconds that same free hand points down toward the bottom-left corner of the frame with the index finger, with a knowing smile '
            'and her eyes on the lens; from 5 to 8 seconds the free hand goes back to rest flat on the table and she holds the card still at shoulder height, smiling into the lens. She '
            'never speaks and her lips stay closed the whole time. The golden card keeps its plain front with only the embossed sun, no letters or pictures ever appear on it, and it '
            'never leaves her right hand. She keeps the same face, crescent moon with three tiny gold stars, earrings, necklace, bracelets, rings and burgundy top the whole time; the '
            'crystal, the mug, the lamp and the room stay still; each hand has exactly five fingers; nothing appears or disappears. AUDIO: quiet room ambience only; no music, no voice. '
            'No on-screen text, no captions.')

# ------------------------------------------------------------------ nora65: a cena da carta e as falas (R47)
CARTA_CENA = dict(
    img='carta1411-IMG', nome='a carta dourada (quarto à noite)',
    cel='her right arm on the left side of the frame', canto='bottom-left',
    roupa_cont='her soft deep navy-blue fine-knit long-sleeve top',
    quando='at night', onde='a real, lived-in American bedroom', luz='lit only by a warm bedside lamp on the right side of the frame',
    fundo='the plain warm off-white wall, the headboard with the cream throw blanket and the lamp behind her', visual='warm bedside lamp light in the background')
SEGURA = ('her left hand on the right side of the frame holds the golden card with the embossed sun still, in exactly the same position and angle as in the reference image, close to her chest, '
          'the whole time, never covering her face, mouth or chin; the card never moves, never turns and never shows letters or pictures')

F = {
    'D1': "If you have carried heavy silent burdens all year, take a deep breath: your hardest days are officially behind you.",
    'D2': "A major turnaround is quietly arriving, bringing unexpected financial relief, genuine peace of mind, and someone truly special into your life.",
    'D3': "When your energy aligns with this new chapter, doors that stayed locked all year finally open with gentle ease.",
    # 14/11 20h29: o T04 e o T05 originais caíram no filtro de política com a carta (que saiu com cara de cartão de crédito) na mão:
    # "Comment two two two below to lock in this blessing." e "Tap my photo and answer three quick questions in my story to receive your reading for twenty twenty-seven."
    # As novas são as do nora63 (passaram), sem "receive" nem "lock in".
    'D4': "Comment two two two right now so I know your energy is ready for this shift.",
    'D5': "Tap my photo for the quick reading in my story about twenty twenty-seven.",
    'D6': "For your personalized reading, look in the comments below to see what twenty twenty-seven holds for you.",
}
RESERVA = {
    'D5': "Open my story for the quick reading about twenty twenty-seven.",
    'D6': "If this found you today, it's not by chance. Look in the comments below to see what twenty twenty-seven holds for you.",
}
SUF = {'D1': 'T01-fardos-silenciosos', 'D2': 'T02-virada', 'D3': 'T03-portas', 'D4': 'T04-comente-222', 'D5': 'T05-cta-story-2027', 'D6': 'T06-face-cta-comentarios-2027'}
ROT = {'D1': 'T01', 'D2': 'T02', 'D3': 'T03', 'D4': 'T04', 'D5': 'T05', 'D6': 'T06'}
TXT = {'D1': 'o Take 1: para quem carregou fardos em silêncio o ano todo (R47)', 'D2': 'a virada: dinheiro, paz e alguém especial (R47)',
       'D3': 'as portas abrindo; a avaliação real nos últimos 3 s (R47)', 'D4': 'o pedido do 222, antes do CTA (só no Insta)',
       'D5': 'o CTA do story: foto, three quick questions, a leitura de 2027 (só no Insta; a última frase)',
       'D6': 'o CTA só da versão do FACE: os comentários + 2027 (no lugar do T04 e do T05)'}


def nome(k):
    return f'd1411-{SUF[k]}'


GESTO = {
    'D1': 'during the first half of the take she holds a soft, understanding look, in the closing half a warm reassuring smile appears and she gives one small nod',
    'D2': 'during the first half of the take she holds a calm, tender look with her head tilted slightly, in the closing half her eyes brighten with a warm smile',
    'D3': 'during the first half of the take she holds a calm, confident look, in the closing half a relieved smile appears and she gives one slow nod',
    'D4': 'during the first half of the take she holds an encouraging look, in the closing half she gives one small inviting nod with a bright smile',
}


def mov(k):
    c = CARTA_CENA
    g = GESTO.get(k, 'during the first half of the take she holds a warm, confident look, and in the closing half she gives one small encouraging nod with a warm smile')
    return (f'Throughout the whole 10 seconds she keeps an unchanged handheld selfie framing; {c["cel"]} stays extended toward the camera holding the phone out of frame and never '
            f'moves; {SEGURA}; her eyes stay on the lens; {g}; only her face moves, never her hands; from the end of the final sentence of the take until the clip ends she keeps '
            'her lips closed and silent; the camera keeps only a tiny natural handheld sway with no zoom and no cuts, the braid stays on the right side of the frame, everything else in '
            'the room stays still and each hand has exactly five fingers.')


COMUNS = {('of', 'the'), ('and', 'the'), ('to', 'the'), ('in', 'the'), ('on', 'the'), ('at', 'the'), ('for', 'a'), ('of', 'her'), ('and', 'her'),
          ('as', 'if'), ('the', 'lens'), ('her', 'left'), ('and', 'then'), ('the', 'hand'), ('she', 'gives'), ('the', 'height'), ('a', 'warm'), ('with', 'a'),
          ('the', 'whole'), ('a', 'small'), ('for', 'the'), ('in', 'the'), ('the', 'card')}
for k, f in list(F.items()) + [(k + 'r', v) for k, v in RESERVA.items()]:
    assert len(f.split()) <= 22, (k, len(f.split()))
    fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(k[:2]).lower())
    sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS
    assert not sobra, (k, sobra)
    for w in ('private', 'card', 'tarot', 'link', 'free', 'portal'):
        assert w not in f.lower(), (k, w)


def livre(c):
    return (f'Casual handheld iPhone front-camera selfie video {c["quando"]} in {c["onde"]}, looking exactly like a real phone video, {c["luz"]}. '
            'CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, the thin braid wrapped with small gold rings hanging down on the right side of the frame, '
            f'{ESTRELAS}, her star-and-moon drop earrings, her thin gold Venus necklace, the thin gold bracelets and the gold sun ring on her left hand, {c["roupa_cont"]} '
            'and the golden card with the embossed sun stay exactly as in the reference image; the framing is exactly the one of the reference image, a close selfie with her face large '
            f'and centered and her eyes at about one third of the frame height; {c["cel"]} stays extended toward the camera holding the phone out of frame, running off the '
            f'{c["canto"]} corner, and never moves; {SEGURA}; {c["fundo"]} stay exactly where they are; natural skin texture with visible pores, slight phone grain, everything in '
            'focus, no bokeh, no filter, no glow and no sparkles; the camera has only a tiny natural handheld sway, no zoom, no cuts and no reframing; no phone, object, person, animal '
            'or text appears or disappears; each hand always has exactly five fingers; no on-screen text, no captions, no logos; real quiet room ambient sound only, no music. SPEECH RULE '
            "for every take: she says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added sentence "
            'before, between or after; numbers are spoken as words ("two two two" as three separate words, twenty twenty-seven exactly as written); when she finishes the last word '
            'she closes her lips, stays silent and keeps a calm still expression until the clip ends.')


def prompt_manual(c, fala, movimento):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image speaks directly '
            f'to her phone camera in a casual handheld selfie video at home {c["quando"]}.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + fala + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            'VOICE PACING: medium pace (155 to 180 words per minute), about 8 seconds of speech; when she finishes the last word she closes her lips and stays silent '
            'with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + movimento + '\n\n'
            f'VISUAL: realistic casual iPhone front-camera selfie video, {c["visual"]}, natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter.\n\n'
            'CAMERA: handheld, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n'
            'AUDIO: only her voice and quiet room ambience; no music, no other voices, no sound effects.\n\n'
            f'CONTINUITY: her face, long black wavy hair, the thin braid with small gold rings, {ESTRELAS}, her star-and-moon earrings, her gold Venus necklace, her gold sun ring and '
            f'bracelets, {c["roupa_cont"]}, the golden card with the embossed sun and the room behind her stay exactly as in the reference image; no phone, object, person or text '
            'appears; each hand has exactly five fingers; no on-screen text, captions or logos.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.')


def config(c):
    cf = copy.deepcopy(CFG)
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = f'colar o texto abaixo (fechado pela {c["img"]}, a escolhida pela lista de conferência)'
                campo['copiar'] = livre(c)
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
            'Conta do Flow: contatocaram. Abra um PROJETO NOVO no Flow e uma conversa nova no agente.',
            'Nas configurações do agente: Omni 1.2 Flash · 360p · 10 s · 9:16 (10 créditos por take) e gerar sem pedir aprovação. Depois, BAIXE cada take em 720p (não gasta crédito).',
            f'Anexe só a {c["img"]}.',
            'Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.',
            'Renomeie cada take com o nome da lista (o número é a ordem): ' + ' · '.join(nomes) + '. '
            'Se ele não renomear, mande na mesma conversa: “Now rename each video with the correct number from the prompt.”',
            f'Confira na grade, pelo nome, se os {len(ks)} saíram; se a carta continua dourada, parada, sem letra nenhuma; e se a lua no rosto tem as 3 estrelinhas. Se um falhar por política: '
            'mande na mesma conversa “Please generate video X from my previous message again, with the same prompt.” (X = o número dele na lista). Se falhar de novo, não insista: me mande o print.',
            f'Se o T05 (o CTA do Insta) falhar 2 vezes, gere à mão: Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; Início = {c["img"]}; Fim = vazio; cole o prompt abaixo, '
            f'inteiro (10 créditos), e renomeie para {nome("D5")}. PROMPT: ' + prompt_manual(c, F['D5'], mov('D5')),
            f'Se falhar também no Frames: o mesmo caminho com a fala reserva e o mesmo nome. PROMPT RESERVA: ' + prompt_manual(c, RESERVA['D5'], mov('D5')),
            f'Se o T06 (o CTA do Face) falhar 2 vezes: o mesmo caminho à mão (10 créditos), renomeado para {nome("D6")}. PROMPT: ' + prompt_manual(c, F['D6'], mov('D6'))
            + ' · RESERVA: ' + prompt_manual(c, RESERVA['D6'], mov('D6')),
            'Se o agente parar no meio (por exemplo, “alta demanda”): responda na MESMA conversa, sem anexar nada: “Please continue and generate videos X to Y from my previous message, in the same order.” '
            '(troque X e Y pelos números que faltaram). Se ele gerar só o 1º e parar de novo: cole antes do bloco da Central o “pré-prompt do Lucas” (abaixo) e mande de novo só os que faltaram.',
            'Se o agente disser que não dá para usar a imagem como quadro inicial e final com fala: gere à mão: Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; '
            f'Início = {c["img"]}; Fim = vazio; no prompt, só o texto do prompt daquele take.',
            'Pré-prompt do Lucas (só se precisar): ' + PRE_LUCAS,
        ],
    }


RESP_FACE = copy.deepcopy(P63['respostas_face']); RESP_FACE['insta'] = []
INSTA_222 = ['Received ✨ your 2027 reading is waiting in my story 🔮', 'I see you 💛 tap my photo, your next step is in my story',
             'This blessing is yours ✨ check my story before you go', 'Locked in ✨ your quick reading is in my story 🔮', 'So glad this found you 💫 tap my photo for your reading']
STORY = {'ja_postado': True, 'nota': 'Não poste story: o story-1211 foi repostado hoje às 18h56 (Insta e Face) e vale até ~18h56 de 15/11. Os destaques já estão no perfil.'}
SIGNOS = 'ARIES, LEO, LIBRA & SAGITTARIUS:'  # os 4 que não foram nas fitas de outubro (nora41: Câncer, Escorpião, Peixes; nora45: Touro, Virgem, Capricórnio)


# ------------------------------------------------------------------ nora64: o loop
def nora64():
    perfil = copy.deepcopy(P46['perfil']); perfil.pop('teste', None)
    texto = f'{SIGNOS}\nYOUR 2027 SHIFT STARTS TONIGHT.\nTHE WORST IS OFFICIALLY BEHIND YOU.'
    p = {
        'enxuto': True, 'clipe_unico': True, 'ocultar_bloco_agente_imagem': True,
        'perfil': perfil, 'trava_referencia': P46['trava_referencia'], 'figurino': 'soft deep burgundy fine-knit long-sleeve top', 'excecao_estilo': '',
        'roteiro': {'id': 'nora64-LOOP-1411', 'titulo': 'nora64 · 14/11 · o loop de 8 s sem fala (R44): a Nora com a carta dourada aponta para a foto do perfil',
                    'duracao_total': 8,
                    'descricao_instagram': ('Aries, Leo, Libra & Sagittarius: your 2027 shift starts tonight ✨\nYour private reading is waiting in my story 🔮\n'
                                            'Comment "222" to lock in this blessing ✨\n#manifestation #aries #leo #libra #sagittarius'),
                    'descricao_face': ('Aries, Leo, Libra & Sagittarius: your 2027 shift starts tonight ✨\nSee what 2027 holds for you: the link is in the comments 🔮\n'
                                       '#manifestation #aries #leo #libra #sagittarius')},
        'refs': ['Folha da Nora v2 (1K), só ela, na imagem'],
        'imagens': [{'rotulo': 'IMAGEM 1 · loop1411-IMG', 'cena': '(o prompt está na seção do Clipe, item 1)', 'anexar': 'a folha da Nora (1K)'}],
        'videos': [{'rotulo': 'V1', 'cena': 'Clipe único, sem fala (o loop)', 'duracao': 8, 'primeiro_quadro': 'IMAGEM 1 (loop1411-IMG)', 'acao': '(ver seção Clipe)', 'b_roll': '',
                    'fala': '(sem fala) texto na tela: ' + texto.replace('\n', ' '), 'movimentacao': '(sem Central: o prompt do clipe está na seção Clipe)', 'arquivo': 'nora64-CLIPE-loop'}],
        'texto_tela': {'hook': texto, 'hook_comeca': 'o segundo 0', 'hook_termina': 'o fim do clipe', 'hook_alt': '', 'extras': []},
        'comentario_fixado': {'insta': 'Aries, Leo, Libra & Sagittarius ✨ tap my photo: your 2027 reading is waiting in my story 🔮',
                              'face': f'Your 2027 reading is right here 🔮 👉 {FB}'},
        'respostas_face': dict(RESP_FACE, insta=INSTA_222),
        'story': STORY,
        'central': {'imagem_unica': True,
                    'conferir': 'Conferir: é a Nora da loop1411-IMG; ela não fala nem mexe a boca; a carta continua dourada, só com o sol, sem letra; o dedo aponta para baixo à esquerda; 5 dedos em cada mão.',
                    'passos': ['Vídeo de 8 s SEM fala. Não usa a Central do curso nem o agente: a imagem e o clipe saem à mão no Flow (seção Clipe).']},
        'pre_gancho': {
            'titulo_secao': 'Clipe (8 s, sem fala, Frames)', 'duracao': 8, 'tomadas': 1, 'com_rosto': True, 'nome_video': 'nora64-CLIPE-loop',
            'conceito': ('O loop do Clone R44: a Nora sentada à mesa, à noite, com a carta dourada (só o sol em relevo, sem letra), bate 2 vezes nela, aponta para baixo à esquerda '
                         '(onde fica a foto do perfil no Reels) e sorri. Sem fala. Eu ponho o texto de 3 linhas, a faixa do story e a seta; você só monta a música.'),
            'modo': ('1) A imagem: Flow → Imagem · 9:16 · Nano Banana Pro · x4, anexando SÓ a folha da Nora (1K) (0 crédito). 2) O clipe: Flow → Vídeo → Frames → 9:16 → Omni 1.2 Flash → '
                     '360p → 8 s → x2 (~16 créditos); Início = loop1411-IMG; Fim = vazio. Baixe os 2 em 720p.'),
            'etapas': [
                {'tipo': 'img', 'titulo': 'Imagem: a Nora à mesa com a carta dourada', 'nome': 'loop1411-IMG', 'anexar': 'só a folha da Nora (1K)',
                 'quadros': ('FEITO (14/11 19h30): a escolhida é a 4ª opção (a carta na mão do lado ESQUERDO da imagem, erguida no ombro; o clipe já segue ela). x4, 0 crédito. Lista usada: é a Nora (lua com 3 estrelinhas na bochecha do lado esquerdo da imagem, trança com anéis, brincos de '
                             'estrela e lua, colar de Vênus); a carta é dourada e lisa, só com o sol, SEM letra, número ou desenho de tarô; a carta não cobre o rosto; a outra mão está na mesa; 5 dedos em cada mão; o alto da imagem é só parede (espaço do texto); nenhum celular ou tripé no quadro. '
                             'Renomeie para loop1411-IMG. Se ficar em dúvida, me mande as 4.'),
                 'prompt': img_loop()},
                {'tipo': 'vid', 'titulo': 'Clipe: ela bate na carta, aponta para a foto do perfil e sorri', 'nome': 'nora64-CLIPE-loop', 'duracao': 8,
                 'quadros': ('Omni 1.2 Flash · 360p · 8 s · x2 (~16 créditos). Início = loop1411-IMG; Fim = vazio. Escolha o que tiver: a carta sem letra do começo ao fim, o dedo apontando '
                             'para baixo à esquerda, a boca fechada (ela não fala), 5 dedos. Baixe em 720p e renomeie nora64-CLIPE-loop.'),
                 'prompt': LOOP_VID}],
        },
        'edicao_linha': [
            {'quando': '1. CapCut', 'texto': 'Projeto novo com o nora64-CLIPE-loop (8 s)', 'como': 'Sem cortar nada.'},
            {'quando': '2. Música', 'texto': 'A música de sempre (“Ambient Mystical Drone”), do segundo 0 ao fim, −12 dB', 'como': 'Não tem fala: a música pode ficar mais alta que nos falados.'},
            {'quando': '3. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
             'como': '1080×1920, nome nora64-montado. Eu ponho o texto de 3 linhas, os números, a faixa do story com a seta (Insta) e a faixa do comentário (Face), e devolvo o nora64-final e o nora64-final-FACE (espelhado).'}],
        'pecas': {'titulo_decisao': 'Resumo', 'lista': [
            {'nome': 'loop1411-IMG', 'tipo': 'imagem 1 (primeiro quadro)', 'status': 'gerar', 'descricao': 'A Nora à mesa, à noite, blusa vinho, a carta dourada só com o sol na mão do lado direito da imagem, o cristal e a xícara na mesa.'},
            {'nome': 'nora64-CLIPE-loop', 'tipo': 'clipe sem fala', 'status': 'gerar', 'creditos': 16, 'descricao': '8 s: bate 2 vezes na carta, aponta para baixo à esquerda (a foto do perfil), sorri.'}],
            'decisao': ['GERAR AGORA (contatocaram): a imagem (x4, 0 crédito; escolha você pela lista) e o clipe de 8 s (x2, ~16 créditos).',
                        'Monte só a música no CapCut e me mande o nora64-montado. Eu devolvo as 2 versões em ~15 min.',
                        'Postar no Insta e no Face assim que eu devolver (antes das 21h), ao vivo. No Face, logo depois, o comentário da Página com o link. No Insta, responder quem comentar 222.']},
    }
    mt = copy.deepcopy(P49['mapa_tela'])
    mt['numeros'] = [dict(t='222', x=18, y=10.5, onde='alto à esquerda', cor_nome='amarelo-ouro', cor='#FFD21F', tamanho=13),
                     dict(t='11:11', x=82, y=10.5, onde='alto à direita', cor_nome='branco', cor='#FFFFFF', tamanho=14)]
    mt['estilos'] = [{'nome': 'Texto do topo (o clipe todo): ' + ' / '.join(texto.split('\n')), 'fonte': 'Poppins ExtraBold', 'cor': 'caixa sólida de alto contraste',
                      'tamanho': '3 linhas', 'contorno': 'Plano de fundo sólido', 'obs': 'Do segundo 0 ao fim, na faixa da parede acima da cabeça. Eu ponho (P45).'},
                     {'nome': 'Faixa do story (Insta): “Tap my photo: your 2027 reading is in my story” + seta para baixo à esquerda', 'fonte': 'Poppins Bold', 'cor': '—', 'tamanho': '9',
                      'contorno': 'Plano de fundo sólido', 'obs': 'Dos ~3 s ao fim, embaixo. No Face: “Your 2027 reading: link in the comments ⬇️”, sem seta. Eu ponho.'}]
    mt['regras'] = ['Eu ponho os textos, os números e as faixas (P45); você monta só o clipe e a música.']
    p['mapa_tela'] = mt
    p['ordem'] = ['pecas', 'prehook', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    salvar(64, p, 'o loop')


# ------------------------------------------------------------------ nora65: a carta dourada
def nora65():
    c = CARTA_CENA; ks = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
    perfil = copy.deepcopy(P46['perfil']); perfil.pop('teste', None)
    caixa = 'FOR THE TIRED WOMAN:\n2027 IS FINALLY YOUR YEAR'
    p = {
        'enxuto': True, 'imagens_titulo': 'Imagem 1 (carta1411-IMG, nova)',
        'perfil': perfil, 'trava_referencia': P46['trava_referencia'], 'figurino': c['roupa_cont'], 'excecao_estilo': '',
        'ocultar_bloco_agente_imagem': True,
        'roteiro': {'id': 'nora65-CARTA-1411', 'titulo': 'nora65 · 14/11 · a Nora de frente com a carta dourada desde o 1º quadro (R45 a R47); Face assim que editado, Insta ~1h',
                    'duracao_total': 36,
                    'descricao_instagram': ('If you carried heavy silent burdens all year, this is for you ✨\nYour private reading is waiting in my story 🔮\n'
                                            'Comment "222" to lock in this blessing ✨\n#manifestation #lawofattraction #2027 #abundance'),
                    'descricao_face': ('If you carried heavy silent burdens all year, this is for you ✨\nSee what 2027 holds for you: the link is in the comments 🔮\n'
                                       '#manifestation #lawofattraction #2027 #abundance')},
        'refs': ['Folha da Nora v2 (1K) na geração da carta1411-IMG', 'carta1411-IMG em todos os takes'],
        'imagens': [{'rotulo': 'IMAGEM 1 · carta1411-IMG', 'cena': img_carta(), 'anexar': 'só a folha da Nora (1K)'}],
        'videos': [{'rotulo': ROT[k], 'cena': TXT[k], 'duracao': '10', 'primeiro_quadro': 'IMAGEM 1 (carta1411-IMG)', 'acao': '', 'b_roll': '',
                    'fala': F[k], 'movimentacao': mov(k), 'arquivo': nome(k)} for k in ks],
        'texto_tela': {'hook': caixa, 'hook_comeca': 'o primeiro quadro', 'hook_termina': 'officially behind you.', 'hook_alt': '', 'extras': []},
        'comentario_fixado': {'insta': 'Tap my profile picture above to see what 2027 holds for you in my stories ✨', 'face': f'Your 2027 reading is right here 🔮 👉 {FB}'},
        'respostas_face': dict(RESP_FACE, insta=INSTA_222),
        'story': STORY,
    }
    mt = copy.deepcopy(P49['mapa_tela'])
    mt['numeros'] = [dict(t='888', x=18, y=10.5, onde='alto à esquerda', cor_nome='amarelo-ouro', cor='#FFD21F', tamanho=13),
                     dict(t='11:11', x=82, y=10.5, onde='alto à direita', cor_nome='branco', cor='#FFFFFF', tamanho=14),
                     dict(t='222', x=18, y=46.9, onde='à esquerda, na altura do ombro', cor_nome='laranja', cor='#FF9F1C', tamanho=11)]
    mt['estilos'] = [{'nome': 'Caixa do topo: “FOR THE TIRED WOMAN:” / “2027 IS FINALLY YOUR YEAR”', 'fonte': 'Poppins ExtraBold', 'cor': 'texto escuro extra-negrito',
                      'tamanho': '2 linhas', 'contorno': 'Plano de fundo sólido de alto contraste (a cor sai do estilo da cena; o nora63 foi amarelo)',
                      'obs': 'Do 1º quadro até o fim do Take 1. Eu ponho (P45).'},
                     {'nome': 'Faixas do CTA', 'fonte': 'Poppins Bold', 'cor': '—', 'tamanho': '9', 'contorno': 'Plano de fundo sólido',
                      'obs': 'Insta: “Tap my photo: your 2027 reading is in my story” + seta, do T05 ao fim. Face: “Your 2027 reading: link in the comments ⬇️”, do T06 ao fim. Eu ponho.'},
                     {'nome': 'Avaliação real do Trustpilot (Younger ou Karina, não a Katrina)', 'fonte': 'provas-trustpilot/ (-sem-hora)', 'cor': '—', 'tamanho': '~84% da largura',
                      'contorno': 'cantos arredondados', 'obs': 'Nos últimos ~3 s do T03, longe do rosto e da carta, com “Rated 4.8 by 2,200+ people”. Eu ponho.'}]
    mt['regras'] = ['Sem pré-gancho de ritual e sem corte de cenário (R46): o vídeo inteiro é a Nora com a carta, desde o 1º quadro.',
                    'Eu ponho os textos, os números, a avaliação, o riser curto e o impact (P45); você monta só o vídeo e a música.']
    p['mapa_tela'] = mt
    corte = 'nora65-cortado'
    p['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” os {len(ks)} takes, de uma vez: ' + ', '.join(nome(k) for k in ks) + '. O T06 (o CTA do Face) fica no fim: eu separo as 2 versões.',
        'nome': corte, 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pela ordem do nome (T01 a T06)',
        'depois': ['Suba os 6 takes e espere a Prévia.', 'Aperte play com Resultado marcado: confira a primeira palavra do T01 e a última do T06.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', f'Clique em Cortar e baixar e salve como {corte}.']}
    p['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {corte}', 'como': 'É o vídeo que saiu da FusionZ. Sem pré-gancho: começa direto no T01.'},
        {'quando': '1. Do T01 ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Começa no 1º quadro.'},
        {'quando': '2. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': '1080×1920, nome nora65-montado (acima de 30 MB, link do Drive). Eu devolvo o nora65-final (Insta: T01 a T05) e o nora65-final-FACE (T01 a T03 + o T06).'}]
    pecas = [{'nome': 'carta1411-IMG', 'tipo': 'imagem 1', 'status': 'gerar', 'descricao': 'Selfie à noite no quarto, blusa azul-marinho, a carta dourada só com o sol, parada perto do peito, na mão do lado direito da imagem.'}]
    pecas += [{'nome': nome(k), 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{F[k]}”'} for k in ks]
    p['pecas'] = {'titulo_decisao': 'Resumo', 'lista': pecas, 'decisao': [
        'GERAR (contatocaram), depois do loop: a carta1411-IMG (x4, 0 crédito) e ME MANDE AS 4 antes dos takes: o Flow pode trocar a mão da carta de lado (fez isso no loop), e o LIVRE e as movimentações precisam bater com a escolhida; eu ajusto no mesmo link em ~5 min. Depois, os 6 takes nela pelo agente. Créditos: ~60.',
        'Sem pré-gancho: o vídeo abre direto na Nora com a carta, desde o 1º quadro (R46). A fala não fala de cartas.',
        'Face: assim que eu devolver o nora65-final-FACE (sem o 222). Insta: ~4 h depois do loop (~1h), o nora65-final, com o 222 antes do story. Respostas ao 222 no Insta; no Face, o comentário da Página com o link.']}
    p['central'] = {'imagem_unica': True,
                    'conferir': ('Conferir em cada take: é a Nora da carta1411-IMG (rosto, lua com as 3 estrelinhas, trança, brincos, colar de Vênus, blusa azul-marinho); a carta continua dourada, '
                                 'parada perto do peito, sem letra; ela fala uma vez só, em inglês, com os números por extenso; o braço do celular não se mexe. Renomeie com o nome da lista.'),
                    'passos': [], 'config': config(c), 'agente': agente(c, ks),
                    'colagens': [{'titulo': 'nora65: os 6 takes (T01 a T06)', 'fala': ' '.join(F[k] for k in ks), 'movimentacao': [mov(k) for k in ks], 'takes': list(range(len(ks)))}]}
    p['ordem'] = ['pecas', 'imagens', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    salvar(65, p, 'a carta')


def salvar(n, p, tit):
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', f'<title>Painel nora{n} · dia 14/11</title>', html, count=1)
    (R / f'PAINEL-NORA{n}.html').write_text(html, encoding='utf-8')
    print('ok', f'nora{n}', tit)


nora64()
nora65()
