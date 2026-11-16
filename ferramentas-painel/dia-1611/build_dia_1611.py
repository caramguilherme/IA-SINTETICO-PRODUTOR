# Painéis do dia 16/11/2026: nora67 (o café Folgers, Insta e Face às 19h30) e nora68 (a onda que quebra no rochedo atrás dela, Insta e Face à 0h00).
# Decisões: Clone R55 e R57 (o Folgers às 19h30 contra o evento grande à 0h00, o mesmo corpo e o mesmo CTA; os Takes 1 do Clone); Clone R60 (o hook de no máximo
# 3,5 a 4,0 s em 3 tomadas de ~1,4 + ~1,4 + ~0,8 s, o gesto curto com algo se mexendo, a fala no impact); R46 (a Nora fala na mesma cena do hook);
# o corpo com palavras americanas (aluno, 16/11 12h41; dica do Caio1094); a bandeira discreta (broche + bandeirinha ao fundo; Caio e Pedro, R59);
# a tela dividida alternando com a tela cheia (aluno, 16/11 08h53; aula 12); a faixa do story com o cadeado (R55); os números 11:11 e 222 brancos (aluno, 13h31);
# o PROMPT CURTO nos clipes do pré-gancho (aluno, 16/11 ~15h10; aula 54; exceção à P32). "pode montar" às ~15h10 de 16/11.
# Imagens como EDIÇÃO da d1511-PRE-sal-IMG-C (a Nora aprovada) + a folha (+ a foto real da lata do Folgers no nora67): lição de 14/11 20h20.
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-1611/build_dia_1611.py
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
P66 = pacote('PAINEL-NORA66.html')
CFG = copy.deepcopy(P51['central']['config'])
VOZ = [c for s in CFG for c in s['campos'] if c['campo'].startswith('Perfil de voz')][0]['copiar']
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'

ESTRELAS = ('the small flat gold crescent moon on her cheek on the left side of the frame with three tiny separate gold five-pointed stars next to it '
            '(three stars with visible points, never dots or circles)')
PIN = 'a small red, white and blue enamel American flag pin (about 1.5 centimeters wide, no text)'
FOLGERS = ('the exact Folgers Classic Roast ground coffee canister from the reference photo (a red plastic canister, the orange-red label with the white sunburst '
           'logo, "Folgers" in big white letters, "Classic Roast" below it)')
CANECA = 'a clear glass coffee mug'
PIRES = 'a small plain white ceramic saucer'
MOEDA = 'one plain matte gold coin'

# ------------------------------------------------------------------ as duas cenas (a imagem C de cada uma é a das falas; R46)
CAFE = dict(
    nn='nora67', d='d1611', tag='cafe', img='d1611-PRE-cafe-IMG-C', nome='a cozinha ao anoitecer, de frente, com a caneca e a lata do Folgers',
    roupa_cont=f'her light-blue denim button-up shirt with the sleeves rolled to the elbows and the top button open, and {PIN} pinned on her shirt collar',
    quando='in the early evening', onde='a real, lived-in American kitchen', luz='lit by a warm pendant lamp above the counter and the last soft daylight from a window',
    fundo=('the wooden counter, the warm cabinets, the open shelf with a small American flag standing in a glass jar and the pendant lamp behind and around her'),
    visual='warm early-evening kitchen light', som='quiet kitchen ambient sound',
    segura=('the hand that holds the clear glass mug keeps it resting on the white saucer on the counter, wrapped around the mug, in exactly the same position as in the '
            'reference image, the whole time; the mug never lifts, never tilts and she never drinks; the open red Folgers canister stays still on the counter beside the '
            'mug with its label facing the camera, and the gold coin stays on the saucer'),
    livre_obj='the clear glass mug of coffee on the white saucer with the gold coin, and the open red Folgers canister with its label',
)
ONDA = dict(
    nn='nora68', d='d1611', tag='onda', img='d1611-PRE-onda-IMG-C', nome='a praia ao pôr do sol, de frente, o rochedo e o mar atrás',
    roupa_cont=f'her soft cream cable-knit cardigan over a plain white top, and {PIN} pinned on the cardigan just below her collarbone',
    quando='at sunset', onde='a wide sandy beach on the American coast', luz='lit by warm golden sunset light from the side',
    fundo=('the sea, the big dark rock behind her, the wet sand and, far away on the sand, a white wooden lifeguard tower with a small American flag on top'),
    visual='warm golden sunset light on a beach', som='real ocean ambient sound, soft waves and a light wind',
    segura=('both of her hands stay down, relaxed and out of the frame below the bottom edge the whole time; the sea behind her moves only with small gentle waves, '
            'no big wave and no spray during the takes'),
    livre_obj='the sea, the big dark rock and the lifeguard tower with the small flag behind her',
)

# ------------------------------------------------------------------ falas (o Take 1 é a variável do teste; T02 a T06 iguais nos dois; até 22 palavras; números por extenso)
T1 = {'nora67': "If you spent all day carrying everything alone, this quiet moment is for you.",
      'nora68': "If you feel emotionally exhausted tonight, breathe: the heaviest storm is officially behind you."}
CORPO = {
    'S2': "You spent all year holding it together for everyone, juggling bills and errands, quietly wondering when your turn would come.",
    'S3': "The universe saw your quiet faith. A major turnaround is coming, bringing unexpected cash, peace of mind and someone truly wonderful.",
    'S4': "The hardest part is over. Doors that stayed shut all year are finally opening, just in time for the holidays.",
    'S5': "Tap my photo and answer three quick questions in my story to uncover your guiding energy for twenty twenty-seven.",
    'S6': "For your personal reading, look in the comments below to see what twenty twenty-seven holds for you.",
}
RESERVA = {
    'S2': "You spent all year holding it together for everyone, juggling work and errands, quietly wondering when your turn would come.",  # se "bills" cair no filtro
    'S3': "The universe saw your quiet faith. A major turnaround is coming, bringing unexpected money, peace of mind and someone truly wonderful.",  # se "cash" cair
    'S5': "Tap my photo for the quick reading in my story about twenty twenty-seven.",  # passou no nora63 e no nora65
    'S6': "If this found you today, it's not by chance. Look in the comments below to see what twenty twenty-seven holds for you.",
}
SUF = {'S1': 'T01-take1', 'S2': 'T02-segurando-tudo', 'S3': 'T03-fe-silenciosa', 'S4': 'T04-portas-abrindo', 'S5': 'T05-cta-story-2027', 'S6': 'T06-face-cta-comentarios-2027'}
ROT = {'S1': 'T01', 'S2': 'T02', 'S3': 'T03', 'S4': 'T04', 'S5': 'T05', 'S6': 'T06'}
TXT = {'S1': 'o Take 1 (a variável do teste: o mesmo corpo nos dois vídeos)',
       'S2': 'a 2ª frase: valida a rotina dela (segurar tudo, as contas e as tarefas; R48)',
       'S3': 'o corpo A, 1ª parte: a fé silenciosa vista + a virada (o dinheiro, a paz, alguém especial)',
       'S4': 'o corpo A, 2ª parte: o pior passou + as portas abrindo, a tempo das festas',
       'S5': 'o CTA do story (Clone R55, versão A; só no Insta; um comando só, sem o 222 na fala, R54)',
       'S6': 'o CTA só da versão do FACE: os comentários + 2027 (no lugar do T05)'}


def fala(c, k):
    return T1[c['nn']] if k == 'S1' else CORPO[k]


def nome(c, k):
    return f'{c["d"]}-{c["tag"]}-{SUF[k]}'


GESTO = {
    'S1': 'during the first half of the take she holds a soft, knowing look with her head tilted slightly, in the closing half a warm reassuring smile appears',
    'S2': 'during the first half of the take she holds a gentle, understanding look, in the closing half a soft smile appears and she gives one slow nod',
    'S3': 'during the first half of the take she holds a calm, tender look, in the closing half her eyes brighten with a warm smile',
    'S4': 'during the first half of the take she holds a calm, confident look, in the closing half a relieved smile appears and she gives one small nod',
}


def mov(c, k):
    g = GESTO.get(k, 'during the first half of the take she holds a warm, confident look, and in the closing half she gives one small encouraging nod with a warm smile')
    maos = (f'{c["segura"]}; her other hand rests on the edge of the counter and never moves' if c['tag'] == 'cafe' else c['segura'])
    return (f'Throughout the whole 10 seconds the camera stays static at chest height in front of her with an unchanged framing; {maos}; her eyes stay on the lens; '
            f'{g}; only her face moves, never her hands; from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; '
            'no zoom and no cuts, the braid stays in place, everything else stays still and each hand has exactly five fingers.')


COMUNS = {('of', 'the'), ('and', 'the'), ('to', 'the'), ('in', 'the'), ('on', 'the'), ('at', 'the'), ('for', 'a'), ('of', 'her'), ('and', 'her'),
          ('as', 'if'), ('the', 'lens'), ('and', 'then'), ('the', 'hand'), ('she', 'gives'), ('the', 'height'), ('a', 'warm'), ('with', 'a'),
          ('the', 'whole'), ('a', 'small'), ('for', 'the'), ('the', 'counter'), ('the', 'mug'), ('the', 'sea'), ('a', 'soft'), ('the', 'take'),
          ('the', 'first'), ('first', 'half'), ('half', 'of')}
for c in (CAFE, ONDA):
    for k in ('S1', 'S2', 'S3', 'S4', 'S5', 'S6'):
        for f in [fala(c, k)] + ([RESERVA[k]] if k in RESERVA else []):
            assert len(f.split()) <= 22, (k, len(f.split()))
            fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(c, k).lower())
            sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS
            assert not sobra, (c['nn'], k, sobra)
            for w in ('private', 'card', 'tarot', 'link', 'free', 'portal', 'claim', 'lock in', 'receive', 'secret', 'two two two'):
                assert w not in f.lower(), (k, w)


def livre(c):
    return (f'Casual real video {c["quando"]} on {c["onde"]}' if c['tag'] == 'onda' else f'Casual real video {c["quando"]} in {c["onde"]}') + (
        f', filmed from a static camera at her chest height about one meter in front of her, looking exactly like a real phone video, {c["luz"]}. CONTINUITY LOCKS for '
        f'every take: the woman, her face, her long black wavy hair, the thin braid wrapped with small gold rings, {ESTRELAS}, her star-and-moon drop earrings, her thin '
        f'gold Venus necklace, the thin gold bracelets and the gold sun ring, {c["roupa_cont"]}, and {c["livre_obj"]} stay exactly as in the reference image; the framing '
        f'is exactly the one of the reference image, from the chest up, her face in the upper middle of the frame; {c["segura"]}; {c["fundo"]} stay exactly where they are; '
        'natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter, no glow and no sparkles; the camera is static, no zoom, no '
        'cuts and no reframing; no phone, phone stand, tripod, object, person, animal or text appears or disappears; each hand always has exactly five fingers; no on-screen '
        f'text, no captions; {c["som"]} only, no music. SPEECH RULE for every take: she says only the exact words of that take\'s script, each word exactly once and in '
        'order, with no repeated word, no extra word and no added sentence before, between or after; numbers are spoken as words (twenty twenty-seven exactly as written); '
        'when she finishes the last word she closes her lips, stays silent and keeps a calm still expression until the clip ends.')


def prompt_manual(c, txt, movimento):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    onde = 'stands behind her kitchen counter' if c['tag'] == 'cafe' else 'stands on the beach'
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image '
            f'{onde} {c["quando"]} and speaks directly to the camera.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + txt + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            'VOICE PACING: medium pace (155 to 180 words per minute), about 8 seconds of speech; when she finishes the last word she closes her lips and stays silent '
            'with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + movimento + '\n\n'
            f'VISUAL: realistic casual phone video, {c["visual"]}, natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter.\n\n'
            'CAMERA: static at chest height, no zoom, no cuts, no reframing.\n\n'
            f'AUDIO: only her voice and {c["som"]}; no music, no other voices, no sound effects.\n\n'
            f'CONTINUITY: her face, long black wavy hair, the thin braid with small gold rings, {ESTRELAS}, her star-and-moon earrings, her gold Venus necklace, her gold sun ring and '
            f'bracelets, {c["roupa_cont"]}, {c["livre_obj"]} and everything behind her stay exactly as in the reference image; no phone, object, person or text appears; each hand '
            'has exactly five fingers; no on-screen text or captions.\n\n'
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
            elif campo['campo'].startswith('Velocidade'):
                campo['valor'] = 'Média — CTA (155–180 WPM). É a velocidade padrão da Nora (voz calorosa e firme). No agente, cada take sai com 10 s (Omni 1.2 Flash em 360p, 10 créditos).'
            elif campo['campo'] == 'Estilo visual':
                campo['valor'] = 'UGC moderno (a câmera parada; o LIVRE descreve)'
    return cf


PRE_LUCAS = ('Below, you will find several prompts, each corresponding to a different video. Please generate all the videos in sequential order, from the first prompt to the last.\n'
             'Maintain the exact same voice across all videos, ensuring EXACTLY THE SAME VOLUME, with no variations in background, intonation, or vocal clarity. Use the attached image as both the first and last frame of every generated video.\n'
             'Please submit ALL generation requests at once and in the correct order, so that all videos can be generated simultaneously.\n'
             'If the generation of any video fails, please resubmit ONLY the item that failed until it is successfully generated.')


def agente(c, ks):
    nomes = [f'{i + 1} = {nome(c, k)}' for i, k in enumerate(ks)]
    confere = ('se a caneca continua no pires com a mão em volta e a lata vermelha do Folgers no balcão, com o rótulo igual' if c['tag'] == 'cafe'
               else 'se o mar atrás continua calmo (sem onda grande) e as mãos fora do quadro')
    return {
        'imagem': c['img'],
        'intro': 'Anexe a imagem, cole o aviso e, embaixo dele, o bloco “COPIAR TUDO JUNTO” da Central.',
        'aviso_tag': 'cole antes do bloco da Central',
        'aviso': (f'Vou te enviar {len(ks)} prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um com o devido '
                  'número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.'),
        'passos': [
            'Conta do Flow: a que você escolher (~60 créditos os takes). Abra um PROJETO NOVO no Flow e uma conversa nova no agente.',
            'Nas configurações do agente: Omni 1.2 Flash · 360p · 10 s · 9:16 (10 créditos por take) e gerar sem pedir aprovação. Depois, BAIXE cada take em 720p (não gasta crédito).',
            f'Anexe só a {c["img"]} (a imagem C do pré-gancho, a escolhida).',
            'Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.',
            'Renomeie cada take com o nome da lista (o número é a ordem): ' + ' · '.join(nomes) + '. '
            'Se ele não renomear, mande na mesma conversa: “Now rename each video with the correct number from the prompt.”',
            f'Confira na grade, pelo nome, se os {len(ks)} saíram; {confere}; se o broche da bandeira continua na roupa; e se a lua no rosto tem as 3 estrelinhas. '
            'Se um falhar por política: mande na mesma conversa “Please generate video X from my previous message again, with the same prompt.” (X = o número dele na lista). '
            'Se falhar de novo, use o prompt à mão do take (abaixo).',
            f'Se o T02 falhar 2 vezes (a palavra "bills"): à mão, Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; Início = {c["img"]}; Fim = vazio; cole o prompt abaixo '
            f'(10 créditos) e renomeie para {nome(c, "S2")}. PROMPT: ' + prompt_manual(c, RESERVA['S2'], mov(c, 'S2')),
            f'Se o T03 falhar 2 vezes (a palavra "cash"): o mesmo caminho à mão, renomeado para {nome(c, "S3")}. PROMPT: ' + prompt_manual(c, RESERVA['S3'], mov(c, 'S3')),
            f'Se o T05 (o CTA do Insta) falhar 2 vezes: à mão, renomeado para {nome(c, "S5")}. PROMPT: ' + prompt_manual(c, CORPO['S5'], mov(c, 'S5'))
            + ' · RESERVA (passou no nora63 e no nora65): ' + prompt_manual(c, RESERVA['S5'], mov(c, 'S5')),
            f'Se o T06 (o CTA do Face) falhar 2 vezes: à mão, renomeado para {nome(c, "S6")}. PROMPT: ' + prompt_manual(c, CORPO['S6'], mov(c, 'S6'))
            + ' · RESERVA: ' + prompt_manual(c, RESERVA['S6'], mov(c, 'S6')),
            'Se o agente parar no meio (por exemplo, “alta demanda”): responda na MESMA conversa, sem anexar nada: “Please continue and generate videos X to Y from my previous message, in the same order.” '
            '(troque X e Y pelos números que faltaram). Se ele gerar só o 1º e parar de novo: cole antes do bloco da Central o “pré-prompt do Lucas” (abaixo) e mande de novo só os que faltaram.',
            'Se o agente disser que não dá para usar a imagem como quadro inicial e final com fala: gere à mão: Vídeo → Frames → 9:16 → Omni 1.2 Flash → 360p → 10 s → x1; '
            f'Início = {c["img"]}; Fim = vazio; no prompt, só o texto do prompt daquele take.',
            'Pré-prompt do Lucas (só se precisar): ' + PRE_LUCAS,
        ],
    }


# ------------------------------------------------------------------ pré-gancho: 3 imagens (edição da Nora aprovada) + 3 vídeos de 5 s com PROMPT CURTO (aula 54)
_FIM_IMG = ('looks exactly like a real casual iPhone photo, slight phone grain, natural colors, everything in focus, no bokeh, no dark or gloomy mood; no glow, no sparkle, '
            'no light effect; no phone, phone stand or tripod anywhere in the image; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16')


def _nora(c):
    base = ('the first image is the approved photo of the woman in her kitchen at night (keep exactly her face, her long black wavy hair, the thin braid with small gold '
            'rings, the small flat gold crescent moon with three tiny gold five-pointed stars on her cheek, her star-and-moon earrings, her gold Venus necklace, the thin gold '
            'bracelets and the gold sun ring); the second image is her character sheet (same woman, same face)')
    if c['tag'] == 'cafe':
        return (base + '; the third image is the real Folgers Classic Roast canister. Same woman and same face: change her clothes to ' + c['roupa_cont'] +
                '; keep a real lived-in American kitchen with a wooden counter and warm cabinets, now in the early evening, lit by a warm pendant lamp above the counter and '
                'the last soft daylight from a window; on an open shelf behind her, small in the background, a small American flag on a stick stands in a glass jar. ')
    return (base + '. Same woman and same face: change her clothes to ' + c['roupa_cont'] + ', and change the place and the light: she now stands on a wide sandy beach '
            'on the American coast at sunset, warm golden light from the side, a light wind in her hair; behind her the sea and one big dark rock standing in the shallow '
            'water about twenty meters away; far away on the sand, small in the background, a white wooden lifeguard tower with a small American flag on top. ')


def _livre_topo(c):
    return ('the upper 18 percent of the image is plain warm cabinets with nothing in it; ' if c['tag'] == 'cafe'
            else 'the upper 18 percent of the image is open evening sky with nothing in it; ')


def imgs(c):
    n = _nora(c); topo = _livre_topo(c)
    if c['tag'] == 'cafe':
        return [
            ('A', 'a colher de café sobre a caneca de água quente, ao lado da lata do Folgers (plano médio)',
             n + 'RAW photo taken from about 70 centimeters in front of her, at chest height: she stands behind the wooden counter, framed from the waist up, centered; '
             f'on the counter in the lower part of the image, {FOLGERS} stands open on the right side of the image with its label facing the camera, sharp and legible, and '
             f'{CANECA} full of clear hot water sits on {PIRES} in the lower middle; in one hand she holds a metal teaspoon heaped with dark ground coffee right above the '
             f'mug; her other hand rests flat on the counter next to {MOEDA}; she looks down at the mug with a calm, focused expression; ' + topo + _FIM_IMG),
            ('B', 'o pires de perto: a caneca de café com vapor e a moeda entre os dedos',
             n + f'close-up from slightly above of {PIRES} on the wooden counter filling the lower two thirds of the image: {CANECA} of dark coffee sits on the saucer with a '
             f'soft wisp of real steam rising from it; her hand, with the thin gold bracelets and the gold sun ring, holds {MOEDA} between two fingers about ten '
             f'centimeters above the empty side of the saucer; at the right edge of the image, part of the open red Folgers canister and its label is visible; the edge of her '
             'denim shirt and the warm kitchen are behind; ' + _FIM_IMG),
            ('C', 'de frente, a mão em volta da caneca, a lata do Folgers no balcão (é a imagem das falas)',
             n + 'RAW photo taken from about 70 centimeters in front of her, at chest height: closer framing from the chest up, her face in the upper middle of the image, '
             f'looking straight into the camera with a warm, knowing smile and her lips closed; the flag pin is visible on her collar; in the lower part of the image, on the '
             f'counter in front of her, {CANECA} of dark coffee with a soft wisp of real steam sits on {PIRES} with {MOEDA} lying on the saucer next to the mug; one hand is '
             f'wrapped around the mug, resting on the counter; her other hand rests on the edge of the counter; {FOLGERS} stands open on the counter beside the mug, label '
             'facing the camera, never covering her face; ' + topo + _FIM_IMG),
        ]
    return [
        ('A', 'a Nora de pé na areia, a onda grande se erguendo atrás dela (plano aberto)',
         n + 'RAW photo taken from about three meters in front of her, at chest height: she stands on the dry sand framed from the knees up, slightly to the left of the '
         'center, calm, looking out to the side at the sea; behind her, about twenty meters away, a huge dark-blue wave is rising and rolling toward the big dark rock, '
         'its top just starting to curl, real water and real foam; her hands hang relaxed at her sides; ' + topo + _FIM_IMG),
        ('B', 'mais perto: a onda a ponto de bater no rochedo atrás do ombro dela',
         n + 'RAW photo taken from about one and a half meters in front of her, slightly low, at chest height: she stands calm in the left half of the image, framed from the '
         'waist up, her hair blowing in the wind, looking toward the sea; over her right shoulder, in the right half of the image, the huge wave is about to hit the big '
         'dark rock, the curling wall of water at its highest point, real water, real white foam, nothing exploding yet; ' + topo + _FIM_IMG),
        ('C', 'de frente, calma, o mar e o rochedo atrás (é a imagem das falas)',
         n + 'RAW photo taken from about one meter in front of her, at chest height: closer framing from the chest up, her face in the upper middle of the image, looking '
         'straight into the camera with a calm, warm, knowing smile and her lips closed; the flag pin is visible on the cardigan; her hands are down and out of the frame; '
         'behind her, a little to the right, the big dark rock in the sea with small calm waves and the last white foam of a wave sliding back; far away on the sand, small, '
         'the white lifeguard tower with a small American flag on top; ' + topo + _FIM_IMG),
    ]


SOM_CAFE = 'Ambient kitchen ASMR sound only, no speech and no music.'
SOM_ONDA = 'Ambient ocean ASMR sound only, wind and crashing water, no speech and no music.'


def vids(c):
    if c['tag'] == 'cafe':
        return [
            ('1-colher', 'A', 'o café caindo na água quente e girando, ao lado da lata',
             'She tips the spoonful of coffee into the hot water and the dark coffee swirls and spreads through the glass mug while steam rises. ' + SOM_CAFE),
            ('2-moeda', 'B', 'a moeda caindo no pires ao lado da caneca (de perto)',
             'She lets go of the coin and it drops onto the saucer next to the mug with a clink while the steam keeps rising; plain matte gold coin, no sparkle. ' + SOM_CAFE),
            ('3-aponta', 'C', 'ela puxa a caneca e aponta para a lente, o vapor subindo',
             'She pulls the mug a little closer and points straight at the lens with her other hand in one smooth move, eyes open, while the steam keeps rising. ' + SOM_CAFE),
        ]
    return [
        ('1-onda-sobe', 'A', 'a onda enorme se erguendo atrás dela, ela parada',
         'The huge wave rises and rolls toward the big dark rock behind her while she stands still on the sand, her hair blowing in the wind. ' + SOM_ONDA),
        ('2-onda-quebra', 'B', 'a onda quebrando no rochedo atrás do ombro dela, a espuma voando',
         'The wave crashes into the rock behind her and white spray bursts high into the air while she stays calm. ' + SOM_ONDA),
        ('3-aponta', 'C', 'ela se vira calma e aponta para a lente, a espuma ainda descendo atrás',
         'With the last foam still sliding back behind her, she raises one hand and points straight at the lens in one smooth move, eyes open, calm smile. ' + SOM_ONDA),
    ]


# ------------------------------------------------------------------ imagens do desejo (0 crédito): as 6 do nora66 que servem a este corpo + 2 novas
_DES_FIM = ('RAW photo, looks exactly like a real casual iPhone photo, natural colors, slight phone grain, everything in focus, no bokeh, no filter; no recognizable face (faces out '
            'of frame, from behind or turned away); no text, no logo, no watermark, no readable words or numbers on anything; each hand has exactly five fingers; '
            'photorealistic, unretouched, vertical 9:16')
DESEJO_NOVAS = [
    ('8-contas-e-tarefas', 'T02: as contas e as tarefas (bills and errands)',
     'a woman\'s hands with a thin gold bracelet at a kitchen table in the evening sorting a small stack of paper envelopes and papers with no readable text, a set of car '
     'keys, a reusable grocery bag and a mug of coffee beside them, a busy but warm real American home, warm lamp light, caring mood, not stressful; ' + _DES_FIM),
    ('9-festas', 'T04: a tempo das festas (just in time for the holidays)',
     'a cozy real American living room at night decorated for the holidays: a Christmas tree with warm white string lights, a few wrapped gifts under it, a fireplace with '
     'stockings and a soft blanket on the sofa, warm, peaceful and hopeful mood, nobody in the image; ' + _DES_FIM),
]
# a ordem da edição (tela dividida = a Nora em cima falando, a imagem embaixo; cheia = a imagem na tela toda), eu monto (montar_desejo.py)
ROTEIRO_DESEJO = [
    ('T02, "holding it together for everyone"', 'd1511-DESEJO-2-sorrindo-para-todos', 'dividida'),
    ('T02, "juggling bills and errands"', 'd1611-DESEJO-8-contas-e-tarefas', 'dividida'),
    ('T02, "quietly wondering when your turn would come"', 'd1511-DESEJO-3-sozinha-na-cama', 'cheia'),
    ('T03, "unexpected cash" (SÓ no Insta)', 'd1511-DESEJO-4-dinheiro-no-envelope', 'cheia'),
    ('T03, "peace of mind"', 'd1511-DESEJO-5-paz-na-varanda', 'dividida'),
    ('T03, "someone truly wonderful"', 'd1511-DESEJO-6-casal-na-praia', 'cheia'),
    ('T04, "doors… finally opening"', 'd1511-DESEJO-7-porta-abrindo', 'dividida'),
    ('T04, "just in time for the holidays"', 'd1611-DESEJO-9-festas', 'cheia'),
]


def pre_gancho(c, gera_desejo):
    base = f'{c["d"]}-PRE-{c["tag"]}'
    anexos = ('1º a d1511-PRE-sal-IMG-C (a Nora da cozinha de 15/11, já aprovada); 2º a folha da Nora (1K)'
              + ('; 3º a foto da lata do Folgers (folgers-classic-roast-frente.jpg, que eu te mando)' if c['tag'] == 'cafe' else ''))
    etapas = []
    for letra, desc, prompt in imgs(c):
        usa = ', '.join(v[0] for v in vids(c) if v[1] == letra) + (' e TODOS os takes (T01 a T06)' if letra == 'C' else '')
        if c['tag'] == 'cafe':
            conf = ('é a Nora (o rosto, a lua com as 3 estrelinhas, a trança com anéis); a camisa jeans com o broche da bandeira na gola; o rótulo do Folgers IGUAL ao da foto '
                    '(o sol de raios brancos, "Folgers" branco, "Classic Roast", sem letra trocada); a caneca de vidro; 5 dedos em cada mão; nenhum celular ou tripé.')
        else:
            conf = ('é a Nora (o rosto, a lua com as 3 estrelinhas, a trança com anéis); o cardigã creme com o broche da bandeira; a onda e o rochedo de verdade (sem brilho); '
                    'a torre de salva-vidas com a bandeirinha ao longe; nenhum celular ou tripé.')
        etapas.append({'titulo': f'Imagem {letra}: {desc}', 'nome': f'{base}-IMG-{letra}', 'tipo': 'img', 'anexar': anexos,
                       'quadros': (f'x4, 0 crédito. Serve para: {usa}. Escolha a que tiver: {conf} Não precisa olhar de que lado está a mão. '
                                   + ('Se o Flow recusar pelo nome da marca, apague "Folgers" do texto e deixe só a foto anexada. ' if c['tag'] == 'cafe' else '')
                                   + f'Renomeie para {base}-IMG-{letra}.' + (' ME MANDE AS 4 DA IMAGEM C antes dos takes (é a imagem das falas).' if letra == 'C' else '')),
                       'prompt': prompt})
    for suf, letra, desc, prompt in vids(c):
        n = f'{base}-{suf}'
        etapas.append({'titulo': f'Vídeo {suf.split("-")[0]}: {desc}', 'nome': n, 'tipo': 'vid', 'duracao': 5,
                       'quadros': (f'PROMPT CURTO (o teste de hoje, aula 54). Omni 1.2 Flash · 360p · 5 s · x2 (~10 créditos). Início = {base}-IMG-{letra}; Fim = vazio. '
                                   f'Baixe os 2 em 720p e renomeie {n}-a e {n}-b.'),
                       'prompt': prompt})
    if gera_desejo:
        for suf, desc, prompt in DESEJO_NOVAS:
            n = f'd1611-DESEJO-{suf}'
            etapas.append({'titulo': f'Imagem do desejo: {desc}', 'nome': n, 'tipo': 'img', 'anexar': 'NADA (imagem sem a Nora)',
                           'quadros': (f'x4, 0 crédito. Escolha a mais bonita e real, sem rosto, sem texto legível e com 5 dedos. Renomeie para {n} e me mande. '
                                       'Servem aos 2 vídeos de hoje (o nora68 usa as mesmas). As outras 6 imagens do desejo já estão comigo (as do nora66).'),
                           'prompt': prompt})
    if c['tag'] == 'cafe':
        conceito = ('O café Folgers (Clone R55 e R60), em 3 tomadas, ~3,6 s: 0–1,4 s o café caindo da colher na água quente e girando, com a lata vermelha e o rótulo à vista · '
                    '1,4–2,8 s a moeda caindo no pires ao lado da caneca, com o clique, o vapor subindo · 2,8–3,6 s ela puxa a caneca e aponta para a lente, o vapor ainda subindo; '
                    'a fala começa no impact, sem quadro parado (R60). Ela fala na MESMA cozinha, na imagem C (R46).')
    else:
        conceito = ('A onda que quebra no rochedo atrás dela, com ela calma (Clone R56 e R57, nº 45), em 3 tomadas, ~3,6 s: 0–1,4 s a onda enorme se erguendo atrás dela · '
                    '1,4–2,8 s a onda quebrando no rochedo, a espuma voando · 2,8–3,6 s ela se vira calma e aponta para a lente, a espuma ainda descendo; a fala começa no impact. '
                    'Ela fala na MESMA praia, na imagem C (R46). No Face, a versão abre com a onda (não é hook de produto: o tsunami fez 4.236 lá).')
    conceito += (' Os clipes têm PROMPT CURTO (aula 54; o teste de hoje). Eu corto e junto as 3 tomadas e ponho o riser e o impact. '
                 + ('As imagens do desejo (2 novas aqui + 6 do nora66) entram na edição, alternando a tela dividida (a Nora em cima, a imagem embaixo) com a tela cheia.'
                    if gera_desejo else 'As imagens do desejo são as do painel do nora67 (as mesmas nos 2 vídeos).'))
    return {
        'titulo_secao': 'Pré-gancho' + (' e imagens do desejo' if gera_desejo else '') + ' (Flow, à mão, antes dos takes)',
        'conceito': conceito,
        'modo': ('Imagens: Flow → Imagem · 9:16 · Nano Banana Pro · x4, anexando as referências na ordem (0 crédito). Vídeos: Flow → Vídeo → Frames → 9:16 → Omni 1.2 Flash → '
                 '360p → 5 s → x2; Início = a imagem indicada; Fim = vazio. Dá para mandar todos de uma vez. Baixe em 720p e me mande todos, sem cortar.'),
        'etapas': etapas,
    }


# ------------------------------------------------------------------ montar os painéis
INSTA_222 = {
    'nora67': ['So glad you paused here ☕ your 2027 reading is in my story', 'You carried enough this year 💛 tap my photo, your reading is waiting',
               'This moment is yours ✨ the next step is in my story', 'Welcome, love 🌙 tap my photo for your 2027 reading', 'I see you ☕✨ check my story before you go'],
    'nora68': ['The storm is behind you 🌊 your 2027 reading is in my story', 'Breathe, love 💛 tap my photo, your next step is waiting',
               'So glad this found you tonight 🌙 your reading is in my story', 'Calm days are coming ✨ tap my photo for your reading', 'Rest now 🌊✨ check my story before you go'],
}
COMENT_FACE = {
    'nora67': ['☕ Your 2027 reading is in the Page comment ✨', '💛 The link to your reading is in the Page comment', '✨ It\'s waiting for you in the comments above, love'],
    'nora68': ['🌊 Your 2027 reading is in the Page comment', '💫 The link to your reading is pinned in the comments', '🌙 It\'s right there in the Page comment, love ✨'],
}
CAIXA = {'nora67': 'CARRYING IT ALL ALONE?\nTRY THIS COFFEE RITUAL', 'nora68': 'FOR TIRED WOMEN:\nTHE STORM ENDS TONIGHT'}
LEG1 = {'nora67': 'If you spent all day carrying everything alone, this quiet moment is for you ☕✨',
        'nora68': 'If you feel emotionally exhausted tonight, breathe: the heaviest storm is behind you 🌊'}
HASH = {'nora67': '#manifestation #lawofattraction #abundance #coffeeritual #2027', 'nora68': '#manifestation #lawofattraction #abundance #2027'}
FIXADO = {'nora67': ('Your 2027 reading is waiting in my story ☕✨ tap my profile picture above', f'Your 2027 reading starts here ☕ 👉 {FB}'),
          'nora68': ('The storm is behind you 🌊 tap my profile picture above to see what 2027 holds for you in my story', f'Your calm after the storm starts here 🌊 👉 {FB}')}
QUANDO = {'nora67': '16/11, Insta e Face às 19h30', 'nora68': '16/11, Insta e Face à 0h00 (de 16 para 17/11)'}


def montar(c):
    nn = c['nn']; ks = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']; gera_desejo = (nn == 'nora67')
    perfil = copy.deepcopy(P46['perfil']); perfil.pop('teste', None)
    resp = copy.deepcopy(P66['respostas_face']); resp['comentario'] = COMENT_FACE[nn]; resp['insta'] = INSTA_222[nn]
    titulo = ('o café Folgers (ritual de bancada), a Nora falando na mesma cozinha' if c['tag'] == 'cafe'
              else 'a onda que quebra no rochedo atrás dela (evento grande), a Nora falando na mesma praia')
    p = {
        'enxuto': True, 'imagens_titulo': f'Imagem das falas (a {c["img"]}, gerada no pré-gancho)',
        'perfil': perfil, 'trava_referencia': P46['trava_referencia'], 'figurino': c['roupa_cont'], 'excecao_estilo': '',
        'ocultar_bloco_agente_imagem': True,
        'roteiro': {'id': f'{nn}-{c["tag"].upper()}-1611', 'titulo': f'{nn} · {QUANDO[nn]} · {titulo} (R55, R57, R60)', 'duracao_total': 45,
                    'descricao_instagram': f'{LEG1[nn]}\nYour private reading is waiting in my story 🔮\nComment "222" to welcome this blessing ✨\n{HASH[nn]}',
                    'descricao_face': f'{LEG1[nn]}\nSee what 2027 holds for you: the link is in the comments 🔮\n{HASH[nn]}'},
        'refs': ['d1511-PRE-sal-IMG-C + a folha da Nora' + (' + a foto da lata do Folgers' if c['tag'] == 'cafe' else '') + ' nas 3 imagens do pré-gancho',
                 f'{c["img"]} em todos os takes'],
        'imagens': [{'rotulo': f'IMAGEM 1 · {c["img"]}', 'cena': '(gerada no pré-gancho, a imagem C)', 'anexar': 'nada aqui (ela sai no pré-gancho)'}],
        'videos': [{'rotulo': ROT[k], 'cena': TXT[k], 'duracao': '10', 'primeiro_quadro': f'IMAGEM 1 ({c["img"]})', 'acao': '', 'b_roll': '',
                    'fala': fala(c, k), 'movimentacao': mov(c, k), 'arquivo': nome(c, k)} for k in ks],
        'texto_tela': {'hook': CAIXA[nn], 'hook_comeca': 'o primeiro quadro do pré-gancho', 'hook_termina': fala(c, 'S1').split()[-2] + ' ' + fala(c, 'S1').split()[-1],
                       'hook_alt': '', 'extras': []},
        'comentario_fixado': {'insta': FIXADO[nn][0], 'face': FIXADO[nn][1]},
        'respostas_face': resp,
        'story': {'ja_postado': True, 'nota': ('Reposte o story-1211 (o mesmo arquivo) antes das ~17h07 de hoje, no Insta e no Face, ao vivo: ele vale até amanhã à tarde. '
                                                'Hoje à noite não precisa de story novo.')},
    }
    mt = copy.deepcopy(P49['mapa_tela'])
    mt['numeros'] = [dict(t='222', x=18, y=10.5, onde='alto à esquerda', cor_nome='branco', cor='#FFFFFF', tamanho=13),
                     dict(t='11:11', x=82, y=10.5, onde='alto à direita', cor_nome='branco', cor='#FFFFFF', tamanho=13)]
    mt['estilos'] = [
        {'nome': f'Caixa do topo: “{CAIXA[nn].splitlines()[0]}” / “{CAIXA[nn].splitlines()[1]}”', 'fonte': 'Poppins Bold', 'cor': 'texto PRETO em negrito',
         'tamanho': '11, em 2 linhas', 'contorno': 'Plano de fundo AMARELO sólido (Clone R50)',
         'obs': 'Do 1º quadro do pré-gancho até o fim do Take 1. No pré-gancho, só a imagem (sem legenda). Eu ponho (P45).'},
        {'nome': 'Legenda (eu ponho, P45)', 'fonte': 'Poppins Bold', 'cor': 'branca, MAIÚSCULAS; palavras-chave em amarelo forte', 'tamanho': '38 px, 3 palavras por vez',
         'contorno': 'preto grosso', 'obs': 'Entra quando a Nora começa a falar o Take 1 (no pré-gancho não).'},
        {'nome': 'Imagens do desejo (tela dividida alternando com tela cheia)', 'fonte': 'd1511-DESEJO-2 a 7 + d1611-DESEJO-8 e 9', 'cor': '—',
         'tamanho': 'dividida = a Nora em cima falando, a imagem embaixo; cheia = a imagem na tela toda; ~1,5 a 2 s cada',
         'contorno': 'entrada animada e um whoosh curto', 'obs': 'Do T02 ao fim do T04, uma por frase. O dinheiro só no Insta. A legenda fica por cima de tudo. Eu ponho.'},
        {'nome': 'Faixa do CTA com o cadeado', 'fonte': 'Poppins Bold', 'cor': 'caixa branca, texto preto, o destaque em vermelho', 'tamanho': '10', 'contorno': 'Plano de fundo sólido',
         'obs': 'Insta: “Your 2027 reading: 🔒 / tap my photo” (o cadeado desenhado) + seta vermelha para a foto do perfil, do T05 ao fim. Face: “Your 2027 reading: link in the comments”, do T06 ao fim. Eu ponho.'}]
    mt['regras'] = ['Na tela, só o 11:11 e o 222, os dois brancos, nos cantos de cima (escolha do aluno, 16/11).',
                    'O pré-gancho e as falas na MESMA cena (R46): nada de corte para outro lugar.',
                    'Eu ponho os textos, os números, as imagens do desejo, o riser e o impact (P45); você monta só o vídeo e a música.']
    p['mapa_tela'] = mt
    corte = f'{nn}-cortado'
    p['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” só os {len(ks)} takes, de uma vez: ' + ', '.join(nome(c, k) for k in ks) + '. O T06 (o CTA do Face) fica no fim: eu separo as 2 versões.',
        'nome': corte, 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pela ordem do nome (T01 a T06)',
        'depois': [f'Suba os {len(ks)} takes e espere a Prévia.', 'Aperte play com Resultado marcado: confira a primeira palavra do T01 e a última do T06.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', f'Clique em Cortar e baixar e salve como {corte}.']}
    p['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {corte}', 'como': 'É o vídeo que saiu da FusionZ. Começa direto no T01.'},
        {'quando': 'B. Pré-gancho e imagens do desejo: NÃO põe no CapCut',
         'texto': f'Os 3 vídeos do pré-gancho ({c["d"]}-PRE-{c["tag"]}-…, -a e -b)' + (' e as 2 imagens do desejo novas' if gera_desejo else '') + ': mande para mim junto com o montado',
         'como': 'Eu corto e junto o pré-gancho (~3,6 s) antes do T01 com o riser e o impact, e ponho as imagens do desejo (tela dividida e tela cheia).'},
        {'quando': '1. Do T01 ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Começa no 1º quadro do montado.'},
        {'quando': '2. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'1080×1920, nome {nn}-montado (acima de 30 MB, link do Drive). Eu devolvo o {nn}-final (Insta: pré-gancho + T01 a T05) e o {nn}-final-FACE '
                 + ('(abre direto no T01, sem o hook do produto: T01 a T04 + o T06).' if c['tag'] == 'cafe' else '(com a onda: pré-gancho + T01 a T04 + o T06).')}]
    pecas = [{'nome': f'{c["d"]}-PRE-{c["tag"]}-IMG-A, B e C', 'tipo': 'imagens (pré-gancho; a C é a das falas)', 'status': 'gerar',
              'descricao': 'Edição da d1511-PRE-sal-IMG-C + a folha' + (' + a foto da lata do Folgers' if c['tag'] == 'cafe' else '') + '. x4 cada, 0 crédito.'},
             {'nome': f'{c["d"]}-PRE-{c["tag"]}-1 a 3', 'tipo': 'pré-gancho (prompt curto)', 'status': 'gerar', 'creditos': 30,
              'descricao': '3 vídeos de 5 s, uma ação em cada, x2.'}]
    if gera_desejo:
        pecas.append({'nome': 'd1611-DESEJO-8 e 9', 'tipo': 'imagens do desejo', 'status': 'gerar', 'descricao': '2 imagens novas sem a Nora (x4 cada, 0 crédito); servem aos 2 vídeos.'})
    pecas += [{'nome': nome(c, k), 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{fala(c, k)}”'} for k in ks]
    teste = ('O par de hoje testa o tipo de hook: o ritual de bancada (este, 19h30) contra o evento grande (a onda, 0h00), com o mesmo corpo, o mesmo CTA e a mesma edição. '
             'Medida: % nos 3 s e a curva aos 5 s. Também em teste: a tela dividida (aos 10 e aos 20 s, contra o nora66) e o prompt curto nos clipes do gancho.')
    postar = ('Postar às 19h30, ao vivo: Insta (o nora67-final) e Face (o nora67-final-FACE, que abre direto na Nora falando). '
              if c['tag'] == 'cafe' else 'Postar à 0h00 (de 16 para 17/11), ao vivo: Insta (o nora68-final, 4 h depois do nora67) e Face (o nora68-final-FACE, com a onda). ')
    p['pecas'] = {'titulo_decisao': 'Resumo', 'lista': pecas, 'decisao': [
        'GERAR (na conta que você escolher, ~90 créditos): as 3 imagens do pré-gancho (0 crédito) e ME MANDE AS 4 OPÇÕES DA IMAGEM C; depois os 3 vídeos do pré-gancho com o '
        'prompt curto (~30)' + (', as 2 imagens do desejo novas (0)' if gera_desejo else '') + ' e os 6 takes na imagem C pelo agente (~60).',
        teste,
        postar + 'No Face, logo depois, o comentário da Página com o link, tirando a prévia e fixando pelo celular. No Insta, responder quem comentar 222.']}
    p['central'] = {'imagem_unica': True,
                    'conferir': (f'Conferir em cada take: é a Nora da imagem C (rosto, lua com as 3 estrelinhas, trança, brincos, colar de Vênus, o broche da bandeira); '
                                 + ('a caneca continua no pires com a mão em volta e a lata do Folgers no balcão, com o rótulo igual; ' if c['tag'] == 'cafe'
                                    else 'o mar atrás continua calmo e as mãos fora do quadro; ')
                                 + 'ela fala uma vez só, em inglês, com os números por extenso; a câmera não se mexe. Renomeie com o nome da lista.'),
                    'passos': [], 'config': config(c), 'agente': agente(c, ks),
                    'colagens': [{'titulo': f'{nn}: os {len(ks)} takes (T01 a T06)', 'fala': ' '.join(fala(c, k) for k in ks), 'movimentacao': [mov(c, k) for k in ks],
                                  'takes': list(range(len(ks)))}]}
    p['pre_gancho'] = pre_gancho(c, gera_desejo)
    p['ordem'] = ['pecas', 'prehook', 'imagens', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', f'<title>Painel {nn} · dia 16/11</title>', html, count=1)
    (R / f'PAINEL-{nn.upper()}.html').write_text(html, encoding='utf-8')
    print('ok', nn, [ROT[k] for k in ks], 'créditos ~90')


montar(CAFE)
montar(ONDA)
