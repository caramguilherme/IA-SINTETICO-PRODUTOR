# Painéis do kit do portal (nora51 a nora54), 10/11/2026. Base: PAINEL-MODELO.html; Central e voz do pacote do nora46;
# mapa, story e respostas no formato do nora49. Falas: ROTEIRO-KIT-PORTAL-NORA51-54.md.
# O LIVRE e as movimentações são PROVISÓRIOS até a kitportal-IMG ser aprovada (P32: escritos pela imagem aprovada).
# Uso (raiz do repositório): python3 -I ferramentas-painel/kit-portal/build_kit_portal.py
import json, copy, re, sys, pathlib

R = pathlib.Path(__file__).resolve().parents[2]
MODELO = (R / 'PAINEL-MODELO.html').read_text(encoding='utf-8')
assert MODELO.count('const PACOTE = null;') == 1


def pacote(nome):
    t = (R / nome).read_text(encoding='utf-8')
    i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
    return json.loads(t[i:j])


P46 = pacote('PAINEL-NORA46.html')
P49 = pacote('PAINEL-NORA49.html')
CFG = copy.deepcopy(P46['central']['config'])
VOZ = [c for s in CFG for c in s['campos'] if c['campo'].startswith('Perfil de voz')][0]['copiar']
STORYIG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'

# ------------------------------------------------------------------ falas (ROTEIRO-KIT-PORTAL-NORA51-54.md)
F = {
    'T01a': "This video will find you on Tuesday, November 10th, and if it does, this message is one hundred percent meant for you.",
    'T01b': "If you see this on Tuesday, November 10th, this message is one hundred percent meant for you.",
    'T01c': "If you're watching this on Tuesday, November 10th, it's a sign, and this message is meant for you.",
    'T01d': "If you see this on Wednesday, November 11th, this message is one hundred percent meant for you.",
    'T02': "Tomorrow, the 11:11 portal opens, and the next chapter of your life begins with it, in the best way possible.",
    'T02b': "Tomorrow is 11:11, and the doors that stayed closed for so long are getting ready to open for you.",
    'T02d': "Today the 11:11 portal is open, and the next chapter of your life begins with it, in the best way possible.",
    'T03': "Love, peace, purpose, ease, and money that finally stops being a worry: every part of your life is getting an upgrade.",
    'T04': "Your private reading shows what this new chapter is bringing you: tap my photo, open my story, and answer three quick questions.",
    'T05': "Now, here's what most people don't know about 11:11, and why you keep seeing it everywhere lately.",
    'T06': "When the same numbers keep finding you, I call it being a cosmic receiver: the universe speaks to you through signs.",
    'T07': "And 11:11 is a gateway between who you are now and who you're becoming, so the intentions you set now carry further.",
    'T08': "So tap my photo and open my story: three quick questions, and your private reading is ready for you.",
    'T09': "The better you treat this video, the bigger the blessing will be, so save it and send it to someone you love.",
}
NOMES = {
    'T01a': 'kitportal-T01a-data-terca', 'T01b': 'kitportal-T01b-data-terca-se-voce-ve', 'T01c': 'kitportal-T01c-data-terca-e-um-sinal',
    'T01d': 'kitportal-T01d-data-quarta', 'T02': 'kitportal-T02-amanha-o-portal', 'T02b': 'kitportal-T02b-amanha-as-portas',
    'T02d': 'kitportal-T02d-hoje-o-portal', 'T03': 'kitportal-T03-as-areas-da-vida', 'T04': 'kitportal-T04-cta-reading',
    'T05': 'kitportal-T05-regancho-1111', 'T06': 'kitportal-T06-cosmic-receiver', 'T07': 'kitportal-T07-gateway',
    'T08': 'kitportal-T08-cta-de-novo', 'T09': 'kitportal-T09-engajamento',
}
CENA = {
    'T01a': 'a data do dia (abertura do longo)', 'T01b': 'a data do dia (abertura do curto das 17h)', 'T01c': 'a data do dia (abertura do curto das 22h)',
    'T01d': 'a data de quarta (abertura do curto da 00h30)', 'T02': 'a promessa: amanhã é o portal', 'T02b': 'a promessa: as portas vão abrir',
    'T02d': 'a promessa: hoje é o portal (11/11)', 'T03': 'as áreas da vida (as 4 do funil)', 'T04': 'CTA: o que ela ganha, o que tem lá, a ação',
    'T05': 're-gancho: o que ninguém sabe do 11:11', 'T06': 'mecanismo: cosmic receiver', 'T07': 'mecanismo: a passagem e as intenções',
    'T08': 'CTA de novo', 'T09': 'engajamento (depois do CTA)',
}

# movimentação provisória: selfie, braço direito (lado esquerdo da imagem) segurando o celular fora do quadro, mão esquerda livre
BASE_MOV = ('Throughout the whole {d} seconds she keeps an unchanged handheld selfie framing, her right arm on the left side of the frame stays raised toward the camera '
            'holding the phone out of frame and never moves, her left hand on the right side of the frame stays relaxed at collarbone height except during the one small '
            'gesture described here, which always happens at the height of her shoulder on the right side of the frame and never in front of her face or mouth, and her eyes '
            'stay on the lens, {g}, and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; the camera keeps only a tiny '
            'natural handheld sway with no zoom and no cuts, everything else in the room stays still and each hand has exactly five fingers.')
GESTO = {
    'T01a': 'during the first half of the take she leans slightly toward the lens with her eyebrows a little raised and an intrigued look, during the second half she gives one slow knowing nod with a warm half-smile',
    'T01b': 'during the first half of the take she tilts her head slightly with a curious look, during the second half a warm, certain smile appears and she gives one small nod',
    'T01c': 'during the first half of the take she raises her eyebrows with a look of recognition, during the second half she gives two small quick nods with a knowing smile',
    'T01d': 'during the first half of the take she leans slightly toward the lens with a bright, excited look, during the second half she gives one slow nod with a wide warm smile',
    'T02': 'during the first half of the take she raises her left hand to the height of her shoulder with the palm open and facing up as if offering something, during the second half the hand returns to collarbone height and a wide smile grows',
    'T02b': 'during the first half of the take she holds a calm, reassuring look, during the second half she opens her left hand at the height of her shoulder with the palm turning outward slowly as if opening something, then lowers it',
    'T02d': 'during the first half of the take her eyebrows lift with a joyful look, during the second half she opens her left hand at the height of her shoulder with the palm up and then lowers it with a warm smile',
    'T03': 'during the first half of the take she lifts her left hand to the height of her shoulder and counts softly on her fingers, one finger at a time, during the second half the hand returns to collarbone height and she smiles',
    'T04': 'during the first half of the take she holds a warm, confident look, during the second half she points her left index finger down toward the lower left part of the frame for a moment and then lowers the hand',
    'T05': 'during the first half of the take she leans slightly toward the lens with a soft, almost secretive look, during the second half she lifts only the index finger of her left hand at shoulder height for a moment and then lowers it',
    'T06': 'during the first half of the take she raises her left hand to the height of her shoulder with the palm open as if explaining, during the second half she lowers it slowly and gives one calm, confident nod',
    'T07': 'during the first half of the take her eyes glance up and slightly to the side as if picturing something lovely, during the second half her eyes return to the lens and a calm smile grows',
    'T08': 'during the first half of the take she gives one small encouraging nod, during the second half she points her left index finger down toward the lower left part of the frame for a moment and then lowers the hand',
    'T09': 'during the first half of the take she rests her left palm flat at collarbone height for a moment with a warm smile, during the second half she lowers the hand and gives one slow nod',
}


def mov(k):
    d = 8 if len(F[k].split()) <= 17 else 10
    return BASE_MOV.format(d=d, g=GESTO[k])


def dur(k):
    return '8' if len(F[k].split()) <= 17 else '10'


# conferências: até 22 palavras; nenhuma sequência de 2 palavras da fala na movimentação (fora palavras comuns)
COMUNS = {('of', 'the'), ('and', 'the'), ('to', 'the'), ('in', 'the'), ('on', 'the'), ('at', 'the'), ('for', 'a'), ('of', 'her'), ('and', 'her'),
          ('as', 'if'), ('the', 'lens'), ('her', 'left'), ('and', 'then'), ('the', 'hand'), ('she', 'gives'), ('the', 'height')}
for k, f in F.items():
    assert len(f.split()) <= 22, (k, len(f.split()))
    fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(k).lower())
    bf = set(zip(fw, fw[1:])); bm = set(zip(mw, mw[1:]))
    sobra = (bf & bm) - COMUNS
    assert not sobra, (k, sobra)

LIVRE = ('[PROVISÓRIO: confiro e fecho pela kitportal-IMG aprovada antes de você gerar] Casual handheld iPhone front-camera selfie video at night in a real, slightly messy '
         'American bedroom, looking exactly like a real phone video, lit only by a warm bedside lamp on the right side of the frame and one lit white candle on the nightstand behind her. '
         'CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair with the thin gold-ringed braid, the small flat gold crescent moon with three tiny gold stars on her '
         'cheek, her star-and-moon drop earrings, her Venus necklace, her bracelets and rings and her plain emerald-green sweatshirt stay exactly as in the reference image; the framing is '
         'exactly the one of the reference image, a close selfie from the middle of her chest up with her face large and centered and her eyes at about 30 percent of the frame height; '
         'her right arm on the left side of the frame stays raised toward the camera holding the phone out of frame and never moves; her left hand on the right side of the frame stays '
         'relaxed at collarbone height and only rises for the one small gesture of each take, at the height of her shoulder, never in front of her face or mouth; the unmade bed, the lamp, '
         'the candle and the wall behind her stay exactly where they are; natural skin texture with visible pores, slight phone grain, everything in focus, no bokeh, no filter, no glow '
         'and no sparkles; the camera has only a tiny natural handheld sway, no zoom, no cuts and no reframing; no object, person, animal or text appears or disappears; each hand always '
         'has exactly five fingers; no on-screen text, no captions, no logos; real quiet room ambient sound only, no music. SPEECH RULE for every take: she says only the exact words of '
         'that take\'s script, each word exactly once and in order, with no repeated word, no extra word and no added sentence before, between or after; numbers are spoken as words '
         '(11:11 as "eleven eleven", November 10th as "November tenth", November 11th as "November eleventh"); when she finishes the last word she closes her lips, stays silent and '
         'keeps a calm still expression until the clip ends.')


# pergunta para o Clone do Gustavo (regra da 11ª leitura: avaliar a fala antes de gerar); reforçada com a resposta do Lucas Dusi de 10/11
CLONE = {
    'nota': ('Vale para o kit inteiro (nora51 a nora54). Faça depois da imagem e ANTES de gerar os takes: cole a pergunta no Clone do Gustavo (NotebookLM) e mande a resposta '
             'aqui no chat do Code junto com as 4 imagens. Se o Clone pedir mudança na fala, eu ajusto neste painel e republico antes de você gerar.'),
    'pergunta': ('Avalie esta copy para o funil de Manifestation (quiz de 3 perguntas e "private reading"). É um kit de vídeos curtos e um longo para o portal 11/11, '
                 'modelado nos virais da Soma Chhaya. Diga o que melhorar no gancho, no corpo e no CTA para levar mais gente ao story e ao clique, citando as aulas.\n\n'
                 f'GANCHO: "{F["T01a"]}"\n'
                 f'PROMESSA: "{F["T02"]}"\n'
                 f'ÁREAS: "{F["T03"]}"\n'
                 f'CTA 1: "{F["T04"]}"\n'
                 f'RE-GANCHO: "{F["T05"]}"\n'
                 f'MECANISMO: "{F["T06"]} {F["T07"]}"\n'
                 f'CTA 2: "{F["T08"]}"\n'
                 f'ENGAJAMENTO: "{F["T09"]}"\n\n'
                 'As versões curtas (~25 s) usam só GANCHO + PROMESSA + CTA 1. A versão longa usa tudo, com o CTA 1 perto dos 28 s.\n\n'
                 'Em especial: (1) depois do gancho, o corpo filtra o público certo? (2) o CTA tem um motivo forte (reason why) para tocar agora, sem medo e sem ameaça? '
                 'Sugira 2 versões do CTA 1 com até 22 palavras, mantendo "your private reading" e "three quick questions".'),
}


def config_kit():
    c = copy.deepcopy(CFG)
    for s in c:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = 'colar o texto abaixo (PROVISÓRIO até a kitportal-IMG aprovada: eu fecho antes de você gerar)'
                campo['copiar'] = LIVRE
            if campo['campo'] == 'COLE SUA COPY AQUI':
                campo['valor'] = 'colar a fala da colagem (seção “A fala e a movimentação”); cada colagem é uma geração separada'
            if campo['campo'] == 'Atmosfera / mood':
                campo['valor'] = 'Íntimo e confidencial'
            if campo['campo'] == 'Velocidade da fala':
                campo['valor'] = ('Média — CTA (155–180 WPM). É a velocidade padrão da Nora (voz calorosa e firme); '
                                  'take de 8 s (até 17 palavras) custa 12 créditos, de 10 s (18 a 22 palavras) custa 15.')
            if campo['campo'] == 'Conferir':
                campo['valor'] = 'os takes da conferência (8 ou 10 s cada, como na lista da seção “A fala e a movimentação”)'
    return c


def video(k):
    return {'rotulo': k, 'cena': CENA[k], 'duracao': dur(k), 'primeiro_quadro': 'IMAGEM 1 (kitportal-IMG)', 'acao': '', 'b_roll': '',
            'fala': F[k], 'movimentacao': mov(k), 'arquivo': NOMES[k]}


# ------------------------------------------------------------------ imagem (Gerador de Prompts do Creative Hub, com o blueprint)
IPHONE = ("iPhone 15 front camera selfie: looks exactly like a real casual photo taken with an iPhone, natural skin texture with visible pores, slight phone grain, "
          "everything in focus, no bokeh, no filter")
TRAVA_PIN = ("IMAGE 1 is the character sheet: the woman must be exactly this woman (face, gold moon with three small stars on her cheek, braid with gold rings, "
             "star-and-moon earrings, Venus necklace). IMAGE 2 is ONLY a reference for the lighting, the framing, the background mood and the phone-camera look: do not copy "
             "the person, her face, hair, body, clothes or any text from image 2.")
IMG_CENTRAL = {
    'titulo': 'IMAGEM · kitportal-IMG (a mesma para todos os takes do kit)',
    'nome': 'kitportal-IMG',
    'aviso': ('Gerador de Prompts do Creative Hub (central.mvmcreators.com.br/materiais/creative-hub), com a caixa “Já tenho o Blueprint” marcada; 0 crédito. '
              'Os campos travados pelo blueprint (idade, gênero, fenótipo, tom de pele, cabelo) você pula. Antes de colar no Flow, apague do prompt “porcelain”, '
              '“straight”, a idade e o objeto, se aparecerem. Regra do Felps (10/11): a foto tem de parecer tirada por um iPhone.'),
    'passos': [
        'Preencha os campos abaixo e gere o prompt no Gerador.',
        'No Flow: Imagem · 9:16 · Nano Banana Pro · x4. Anexe PRIMEIRO a folha da Nora (a de 1K).',
        'OPCIONAL (o jeito do Felps): procure no Pinterest uma selfie de perto, em casa, à noite, com luz de abajur e cara de celular (ex.: “iphone selfie bedroom night lamp”) e anexe DEPOIS da folha. Aí cole no começo do prompt a trava do grupo 6 (botão Copiar).',
        'Confira cada uma das 4: o rosto é o da Nora (lua com 3 estrelinhas na bochecha do lado esquerdo da imagem, trança com anéis, brincos de estrela e lua, colar de Vênus, testa limpa)? Parece foto de celular? O celular não aparece? Algum texto ou carimbo nos cantos? Se vier outra mulher, gere de novo sem a foto do Pinterest.',
        'Mande as 4 aqui no chat do Code. Eu escolho, fecho neste painel o LIVRE e as linhas de movimentação pela imagem aprovada e aviso para você seguir. Renomeie a escolhida para kitportal-IMG.',
    ],
    'grupos': [
        {'titulo': '1. Personagem', 'nota': 'travados: idade, gênero, fenótipo, tom de pele (pule)', 'campos': [
            {'campo': 'Tipo de personagem', 'valor': 'Cartomante'},
            {'campo': 'Expressão facial', 'valor': 'Sorriso suave de paz'}]},
        {'titulo': '2. Roupa e acessórios', 'nota': 'o cabelo é travado (pule)', 'campos': [
            {'campo': 'Roupa (LIVRE)', 'valor': 'plain emerald-green soft cotton crewneck sweatshirt, slightly oversized, matte, no print, no logo', 'copiar': 1},
            {'campo': 'Acessórios (LIVRE)', 'valor': ('small flat shiny gold crescent moon with three tiny gold stars on the outer edge of her cheekbone near the temple, on the left side '
                                                       'of the image; long gold star-and-moon drop earrings; thin gold necklace with a small Venus pendant; thin gold bracelets; gold sun '
                                                       'ring; hazel-green eyes; one thin braid with small gold rings; clean forehead with no jewelry'), 'copiar': 1}]},
        {'titulo': '3. Pose e objeto', 'campos': [
            {'campo': 'Pose (LIVRE)', 'valor': ('selfie taken with her own phone at arm\'s length: her right arm, on the left side of the image, is raised toward the camera and is cut '
                                                 'off by the bottom-left corner of the frame, and the phone itself is not visible; framed from the middle of her chest up, her face '
                                                 'large and centered with her eyes at about 30 percent of the image height; her left hand, on the right side of the image, rests '
                                                 'relaxed and empty at the height of her collarbone, with exactly five fingers; she looks straight into the phone camera with her '
                                                 'lips slightly parted, as if about to speak; nothing in her hands'), 'copiar': 1},
            {'campo': 'Objeto principal', 'valor': 'nenhum (se o campo obrigar, escolha qualquer um e apague do prompt antes de colar no Flow)'}]},
        {'titulo': '4. Cenário e luz', 'campos': [
            {'campo': 'Cenário', 'valor': 'Quarto com cama desfeita'},
            {'campo': 'Horário', 'valor': 'Abajur tungstênio'},
            {'campo': 'Luz (LIVRE)', 'valor': ('only a warm bedside lamp on the right side of the image and one lit white candle on the nightstand behind her, a little uneven, like a '
                                                'real phone video at night; no studio light, no ring light'), 'copiar': 1},
            {'campo': 'Color grade (LIVRE)', 'valor': 'natural phone colors, no color grading', 'copiar': 1}]},
        {'titulo': '5. Câmera', 'campos': [
            {'campo': 'Câmera', 'valor': 'Câmera de celular (amador)'},
            {'campo': 'Lente (LIVRE)', 'valor': IPHONE, 'copiar': 1},
            {'campo': 'Abertura · ISO · Obturador', 'valor': 'f/8 · 800 · 1/60'},
            {'campo': 'Emulação de filme (LIVRE)', 'valor': 'no film emulation, straight smartphone frame, no date stamp, no text, no watermark', 'copiar': 1},
            {'campo': 'Estilo final', 'valor': 'Documentário candid / UGC'},
            {'campo': 'Realismo', 'valor': 'Extremo'}]},
        {'titulo': '6. Só se anexar a foto do Pinterest', 'nota': 'cole no começo do prompt, antes do texto do Gerador', 'campos': [
            {'campo': 'Trava de identidade', 'valor': TRAVA_PIN, 'copiar': 1}]},
    ],
}

PRE_LUCAS = ('Below, you will find several prompts, each corresponding to a different video. Please generate all the videos in sequential order, from the first prompt to the last.\n'
             'Maintain the exact same voice across all videos, ensuring EXACTLY THE SAME VOLUME, with no variations in background, intonation, or vocal clarity. Use the attached image as both the first and last frame of every generated video.\n'
             'Please submit ALL generation requests at once and in the correct order, so that all videos can be generated simultaneously.\n'
             'If the generation of any video fails, please resubmit ONLY the item that failed until it is successfully generated.')


def agente(n, nomes, um=False):
    if um:
        aviso = 'Irei enviar 1 prompt para você. Quero que seja feita uma animação da imagem anexada. Utilize a imagem anexada como frame inicial e frame final do vídeo.'
    else:
        aviso = (f'Vou te enviar {n} prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um com o devido '
                 'número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.')
    return {
        'imagem': 'kitportal-IMG',
        'aviso': aviso,
        'passos': [
            'Conta do Flow: contatocaram. Abra um PROJETO NOVO no Flow (se o agente parar, projeto novo, não pasta nova) e uma conversa nova no agente.',
            'Nas configurações do agente: Omni 1.1 Flash (o Flow abre no 1.2, que cobra o dobro), 9:16, 720p, gerar sem pedir aprovação.',
            'Anexe só a kitportal-IMG.',
            'Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.' if not um else 'Cole o aviso (acima) e, embaixo, o prompt de cada take (botão COPIAR do take na Central), um por vez.',
            'Renomeie cada take com o nome da lista: ' + ', '.join(nomes) + '. O agente costuma dar o número da ordem (1, 2, 3…): o 1 é o 1º nome da lista, o 2 é o 2º, e assim por diante. '
            'Se ele não renomear, mande na mesma conversa: “Now rename each video with the correct number from the prompt.”',
            'Se o agente parar no meio (por exemplo, “alta demanda”): responda na MESMA conversa, sem anexar nada: “Please continue and generate videos X to Y from my previous message, in the same order.” '
            '(troque X e Y pelos números que faltaram; dica da Ari & Lu, 10/11). Se ele gerar só o 1º e parar de novo: cole antes do bloco da Central o texto “pré-prompt do Lucas” (abaixo) e mande de novo só os que faltaram.',
            'Se o agente disser que não dá para usar a imagem como quadro inicial e final com fala: não escolha nenhuma das opções dele. Gere à mão: Vídeo → Frames → 9:16 → Omni 1.1 Flash → 720p → 10 s (ou 8 s, conforme a lista) → x1; Início = kitportal-IMG; Fim = vazio; no prompt, só o texto do prompt daquele take, sem a frase do aviso.',
            'Pré-prompt do Lucas (só se precisar): ' + PRE_LUCAS,
        ],
    }


def colagem(titulo, ks, idx):
    return {'titulo': titulo, 'fala': ' '.join(F[k] for k in ks), 'movimentacao': [mov(k) for k in ks], 'takes': idx}


def creditos(ks):
    return sum(12 if dur(k) == '8' else 15 for k in ks)


# ------------------------------------------------------------------ cada vídeo
COMUM_HASH = '#manifestation #1111portal #lawofattraction'
VIDEOS = {
    51: dict(hora='17h', dia='10/11 (terça)', tipo='curto', usa=['T01b', 'T02', 'T04'], gera=['T01a', 'T01b', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09'],
             caixa='TUESDAY, NOVEMBER 10TH\nif you keep seeing 11:11,\nthis message is for you', caixa_fim='one hundred percent meant for you.',
             insta=f'If you see this on Tuesday, November 10th, it\'s meant for you. 🔮\nTomorrow is 11:11. Your private reading is waiting in my story.\nComment "I receive" to claim this ✨\n{COMUM_HASH} #manifestingmyreality',
             pergunta='which part of your life do you want to change first: love, peace, purpose or money?',
             nums=[('11:11', 82, 10.5, 'alto à direita', 'amarelo-ouro', '#FFD21F', 15), ('222', 18, 30, 'no meio à esquerda', 'rosa-choque', '#FF4FD8', 12), ('888', 82, 46.9, 'à direita, na altura do ombro', 'ciano', '#3DE0FF', 11)],
             coment=['✨ I sent it to your messages, take a look 🔮', '💖 It\'s waiting in your inbox ✨', '🌙 Check your DMs, it\'s there 💫'],
             dm=['✨ [name], your private reading is here 🔮 Open it before 11:11:', '🌙 Hi [name]! Here\'s your private reading 💖 before the 11:11 portal:', '💫 [name], this one is for you ✨ Your private reading:']),
    52: dict(hora='19h30', dia='10/11 (terça)', tipo='longo', usa=['T01a', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08', 'T09'], gera=[],
             caixa='TUESDAY, NOVEMBER 10TH\ntomorrow is 11:11,\nthis message is for you', caixa_fim='one hundred percent meant for you.',
             insta=f'This video found you on Tuesday, November 10th for a reason. 🔮\nTomorrow the 11:11 portal opens. Your private reading is waiting in my story.\nComment "thank you universe" ✨\n{COMUM_HASH} #spirituality',
             pergunta='what do you want to bring into your next chapter?',
             nums=[('222', 18, 10.5, 'alto à esquerda', 'laranja', '#FF9F1C', 14), ('888', 82, 30, 'no meio à direita', 'verde-limão', '#7CFF4F', 12), ('11:11', 18, 46.9, 'à esquerda, na altura do ombro', 'branco', '#FFFFFF', 11)],
             coment=['🔮 Just sent it to you, check your inbox ✨', '✨ It\'s in your messages now 💖', '💫 Sent! Look in your DMs 🌙'],
             dm=['🔮 [name], here\'s your private reading ✨ before the 11:11 portal:', '💖 [name], I sent this one just for you 🔮 Open it here:', '✨ Hey [name]! Tap here to open your private reading 💫']),
    53: dict(hora='22h', dia='10/11 (terça)', tipo='curto', usa=['T01c', 'T02b', 'T04'], gera=['T01c', 'T02b'],
             caixa='TUESDAY, NOVEMBER 10TH\nif you keep seeing 11:11,\nit\'s a sign', caixa_fim='this message is meant for you.',
             insta=f'If you\'re watching this on Tuesday, November 10th, it\'s a sign. 🔮\nTomorrow is 11:11. Your private reading is waiting in my story.\nComment "I accept" ✨\n{COMUM_HASH} #abundance',
             pergunta='which door are you ready to see open: love, money or peace?',
             nums=[('888', 18, 10.5, 'alto à esquerda', 'rosa-choque', '#FF4FD8', 15), ('11:11', 82, 30, 'no meio à direita', 'ciano', '#3DE0FF', 12), ('222', 18, 46.9, 'à esquerda, na altura do ombro', 'amarelo-ouro', '#FFD21F', 11)],
             coment=['🌙 Sent it to your inbox, beautiful ✨', '✨ Check your messages, it\'s there 🔮', '💖 I just sent it to you 💫'],
             dm=['🌙 [name], your private reading is ready ✨ before 11:11:', '💫 Hi [name]! Open your private reading here 🔮', '✨ [name], open this when you have a quiet minute 💖 Your private reading:']),
    54: dict(hora='00h30 (já quarta, 11/11)', dia='11/11 (quarta), à 00h30', tipo='curto', usa=['T01d', 'T02d', 'T04', 'T09'], gera=['T01d', 'T02d'],
             caixa='WEDNESDAY, NOVEMBER 11TH\ntoday is 11:11,\nthis message is for you', caixa_fim='one hundred percent meant for you.',
             insta=f'If you see this on Wednesday, November 11th, it\'s meant for you. 🔮\nToday the 11:11 portal is open. Your private reading is waiting in my story.\nComment "I\'m ready" ✨\n{COMUM_HASH} #1111',
             pergunta='today is 11:11: what are you asking the universe for?',
             nums=[('11:11', 82, 10.5, 'alto à direita', 'verde-limão', '#7CFF4F', 16), ('222', 18, 30, 'no meio à esquerda', 'branco', '#FFFFFF', 13), ('888', 82, 46.9, 'à direita, na altura do ombro', 'laranja', '#FF9F1C', 11)],
             coment=['💫 It\'s in your DMs, take a look ✨', '🔥 Check your inbox, I sent it 🔮', '✨ Sent to your messages 💖'],
             dm=['💫 [name], today is 11:11 ✨ Your private reading is here:', '🔮 Hi [name]! Your private reading is ready, today on 11:11 💖', '✨ [name], this one is for today 💫 Your private reading:']),
}

LEITURA = ('10/11/2026, leitura focada ampliada (decisão do aluno, 10/11 ~01h55; registro completo no ROTEIRO-KIT-PORTAL-NORA51-54.md): REGRAS-DO-AGENTE.md (P1 a P47), '
           'LICOES-FLOW-E-PROMPTS.md (checklist e lições de 19/10 a 10/11, inclusive a do Felps de 10/11), FATOS-DO-ALUNO.md (resumo, contas, funil, telas do funil, créditos), '
           'CLONE-DO-GUSTAVO-RESPOSTAS.md (R6 a R16), ANALISE-FUNIL-MANIFESTATION-VSL.md (seções 1 a 5 e o cosmic receiver), hooks.md (seção 7), ctas.md, COMUNICACAO-VISCERAL '
           '(seção 9), DNA Visual - Nora v2.md, AULA-IORHAN-30-10 (o que está fora), BIBLIOTECA-VIDEOS-VIRAIS 49.6 e as transcrições da Soma Chhaya, AULA-09-11, BANCO-DE-HEADLINES '
           '(17 a 19), os pacotes dos painéis do nora46 (Central, voz, agente) e do nora49 (mapa, story, respostas).')


def xy(x, y):
    return f'X {round(x / 100 * 720 - 360)} · Y {round(640 - y / 100 * 1280)}'


def montar(n):
    v = VIDEOS[n]; nn = f'nora{n}'
    gera = v['gera']; usa = v['usa']
    ks = gera if gera else usa
    p = {
        'perfil': copy.deepcopy(P46['perfil']),
        'trava_referencia': P46['trava_referencia'], 'figurino': 'plain emerald-green soft cotton crewneck sweatshirt, slightly oversized, matte, no print', 'excecao_estilo': '',
        'ocultar_bloco_agente_imagem': True,
        'roteiro': {
            'id': f'{nn}-KIT-PORTAL-{v["tipo"].upper()}',
            'titulo': f'Kit do portal (modelo Soma Chhaya): {v["tipo"]}, {v["dia"]} às {v["hora"]}',
            'dor': 'a próxima fase da vida chegando (amor, paz, propósito, dinheiro sem aperto), com o portal 11:11 como motivo',
            'formato': ('Sem pré-gancho; selfie com cara de celular no quarto à noite (kitportal-IMG); takes do kit: ' + ' + '.join(usa)),
            'molde_hook': 'Gancho da data dos maiores reels da Soma Chhaya (1,2 mi, 548 mil, 463 mil, 453 mil): "This video will find you on [dia]..." / "If you see this on [dia]..."',
            'duracao_total': 75 if v['tipo'] == 'longo' else (35 if n == 54 else 25),
            'descricao_instagram': v['insta'],
            'legenda_aviso': 'No Face, use a mesma legenda SEM a linha do “Comment …” (o Face entrega menos post com pedido de comentário).',
            'leitura_registro': LEITURA,
        },
        'refs': ['Folha da Nora v2 (1K) na geração da kitportal-IMG', 'kitportal-IMG em todos os takes', 'Opcional: 1 foto do Pinterest só como referência de luz'],
        'imagens': [{'rotulo': 'IMAGEM 1 · kitportal-IMG', 'cena': '(Gerador de Prompts do Creative Hub: seção Imagem do painel do nora51)', 'anexar': 'a folha da Nora (1K)'}],
        'videos': [video(k) for k in ks],
        'texto_tela': {'hook': v['caixa'], 'hook_comeca': 'o primeiro quadro', 'hook_termina': v['caixa_fim'], 'hook_alt': '', 'extras': []},
        'comentario_fixado': {
            'insta': f'{v["pergunta"].capitalize()} ✨ Tell me below, then tap my photo and open my story: your private reading starts there. 🔮',
            'face': f'{v["pergunta"].capitalize()} ✨ Your private reading is right here 🔮 👉 {FB}'},
        'story': {'ja_postado': True, 'nota': (
            'STORY: não tem story novo. Reposte o story-0311 (o mesmo de ontem: imagem story-3110, texto “Tap below: your private reading is waiting for you before the 11:11 portal.”, '
            'adesivo “Open my reading”) ANTES das 22h55 de hoje (10/11), no Insta e no Face, e confira o link de cada rede na prévia. '
            f'Insta (STORYIG): {STORYIG} · Face (FACE): {FB}')},
        'respostas_face': {'aviso': P49['respostas_face']['aviso'], 'comentario': v['coment'], 'dm': v['dm']},
    }
    if n == 54:
        p['story']['nota'] = ('STORY: o repost de hoje às ~22h deixa o story-0311 no ar até ~22h de 11/11; não poste outro agora. '
                              'Em 11/11, perto das 22h, reposte com o texto “Tap below: your private reading is waiting for you on 11:11.” (painel de 11/11).')
    mt = copy.deepcopy(P49['mapa_tela'])
    mt['numeros'] = [dict(t=a, x=x, y=y, onde=o, cor_nome=cn, cor=co, tamanho=tm) for (a, x, y, o, cn, co, tm) in v['nums']]
    caixa1 = v['caixa'].split('\n')
    mt['estilos'] = [
        {'nome': 'Números fixos espalhados (11:11, 888, 222)', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'uma cor para cada número', 'tamanho': 'um tamanho para cada número',
         'contorno': 'Traço preto + Sombra preta, sem Plano de fundo',
         'obs': 'Lugar, cor e tamanho novos (item 28): ' + '; '.join(f'{a} {cn}, {tm}, {xy(x, y)}' for (a, x, y, o, cn, co, tm) in v['nums']) + '. Do 1º quadro ao fim; confiro na imagem aprovada e na prévia. Eu ponho (P45).'},
        {'nome': 'Caixa do topo: ' + ' / '.join(f'“{l}”' for l in caixa1), 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto; a 1ª linha (a data) em vermelho #E53935',
         'tamanho': '10, em 3 linhas (até ~84% da largura)', 'contorno': 'Plano de fundo branco arredondado',
         'obs': 'X 0 · Y 397, do 1º quadro até o fim do 1º take (a data). Eu ponho (P45).'},
        {'nome': 'Legenda (eu ponho, P45)', 'fonte': 'Poppins Bold', 'cor': 'branco, em MAIÚSCULAS; palavra-chave em amarelo-ouro #FFD21F', 'tamanho': 'uns 38 px (vídeo 720×1280)',
         'contorno': 'preto grosso', 'obs': 'Do 1º quadro ao fim (não há pré-gancho), blocos de 2 a 4 palavras, abaixo do queixo; confiro a faixa na imagem aprovada.'},
        {'nome': 'Faixa do story: “Your private reading is in my story”', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto, “my story” em vermelho #E53935',
         'tamanho': '9, em 1 linha', 'contorno': 'Plano de fundo branco arredondado', 'obs': 'Do take do CTA (T04) até o fim, no lugar da caixa do topo (X 0 · Y 397). Eu ponho (P45).'},
        {'nome': 'Seta vermelha (↓)', 'fonte': '—', 'cor': 'vermelho #E53935 com traço preto', 'tamanho': '14', 'contorno': '—',
         'obs': 'Do take do CTA (T04) até o fim, embaixo à esquerda (X -288 · Y -333, P43), apontando para a foto do perfil. Eu ponho (P45).'},
    ]
    mt['regras'] = ['Posições provisórias: confiro todas na kitportal-IMG aprovada e na prévia da edição (número longe do rosto, da mão e da caixa).',
                    'Sem pré-gancho: a caixa do topo, os números e a legenda entram desde o 1º quadro.']
    p['mapa_tela'] = mt

    corte_nome = f'{nn}-cortado'
    lista_usa = ', '.join(NOMES[k] for k in usa)
    p['silencio'] = {
        'intro': f'Arraste na ferramenta “M2M FusionZ – Cortar e juntar vídeos” só estes takes do kit, de uma vez: {lista_usa}. Ela junta pela ordem do nome (já estão em ordem).',
        'nome': corte_nome, 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pela ordem do nome (' + ', '.join(usa) + ')',
        'depois': [f'Suba os {len(usa)} takes e espere a Prévia.',
                   f'Aperte play com Resultado marcado: confira a primeira palavra do 1º take e a última do último take.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.',
                   f'Clique em Cortar e baixar e salve como {corte_nome}. (A legenda eu ponho aqui, no fim.)']}
    p['edicao_linha'] = [
        {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut com o {corte_nome}', 'como': 'É o vídeo que saiu da FusionZ (sem pré-gancho: começa direto na data).'},
        {'quando': '1. Do começo ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'O vídeo todo, por baixo da voz.'},
        {'quando': '2. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': f'720×1280 ou 1080×1920, qualidade alta, nome {nn}-montado (se passar de 30 MB, link do Drive). Eu ponho a caixa do topo, os números, a legenda, a faixa do story e a seta e devolvo o {nn}-final.'}]

    pecas = []
    if n == 51:
        pecas.append({'nome': 'kitportal-IMG', 'tipo': 'imagem 1', 'status': 'gerar', 'creditos': 0, 'descricao': 'Selfie com cara de celular no quarto à noite (Gerador de Prompts + Nano Banana Pro, x4). A mesma imagem para o kit inteiro.'})
    else:
        pecas.append({'nome': 'kitportal-IMG', 'de': 'kitportal-IMG (do painel do nora51)', 'tipo': 'imagem 1', 'status': 'reutilizar', 'descricao': 'A imagem do kit, gerada no painel do nora51.'})
    for k in usa:
        if k in gera:
            pecas.append({'nome': NOMES[k], 'tipo': 'take', 'status': 'gerar', 'creditos': 12 if dur(k) == '8' else 15, 'descricao': f'“{F[k]}”'})
        else:
            pecas.append({'nome': NOMES[k], 'de': f'{NOMES[k]} (do painel do nora51)', 'tipo': 'take', 'status': 'reutilizar', 'descricao': f'“{F[k]}”', 'fala': F[k]})
    for k in gera:
        if k not in usa:
            pecas.append({'nome': NOMES[k], 'tipo': 'take', 'status': 'gerar', 'creditos': 12 if dur(k) == '8' else 15, 'descricao': f'Para o nora52 (longo): “{F[k]}”'})
    pecas.append({'nome': 'story-0311', 'de': 'story-3110', 'tipo': 'story', 'status': 'reutilizar', 'descricao': ('Já repostado às ~22h de 10/11: não poste outro agora (seção Story).' if n == 54 else 'Repost antes das 22h55 de 10/11 (seção Story).')})
    total = creditos(gera)
    decisao = [f'Postar em {v["dia"]} às {v["hora"]}, no Insta e no Face, ao vivo.',
               'Kit do portal (decisão do aluno, 10/11): gancho da data e promessa com prazo, modelados dos maiores reels da Soma Chhaya; sem pré-gancho.',
               ('Comparação: o longo das 19h30 contra o nora49 (corpo A, mesmo horário); os curtos contra o longo (visitas ao perfil por 1.000 views, story, Tracker).')]
    if gera:
        decisao.append(f'Créditos deste painel: {total} (conta contatocaram).' + (' + o piloto do 1.2 em 360p (~10, não vai ao ar).' if n == 51 else ''))
    else:
        decisao.append('0 crédito: todos os takes saem do painel do nora51.')
    p['pecas'] = {'lista': pecas, 'decisao': decisao}

    passos = []
    if n == 51:
        passos += ['Imagem: kitportal-IMG no Gerador de Prompts (seção Imagem). Mande as 4 aqui e ESPERE eu fechar o LIVRE e as linhas de movimentação neste painel (estão provisórios).']
    passos += [f'Central do curso com a configuração desta seção (o LIVRE é o do kit). Cole a fala e a movimentação da colagem (seção “A fala e a movimentação”). Confira: {len(ks)} takes de 8 ou 10 s.',
               'Agente do Flow na contatocaram (seção do agente): anexe só a kitportal-IMG, cole o aviso e o “COPIAR TUDO JUNTO”. Omni 1.1 Flash, 720p.',
               'Renomeie os takes com os nomes da lista (kitportal-…) e me mande a transcrição ou os takes para eu conferir as falas (P33).']
    if n == 51:
        passos += ['PILOTO (só neste painel): gere o kitportal-T01b uma 2ª vez no Omni 1.2 Flash em 360p (8 ou 10 s) e baixe em 720p (veja se o download cobra crédito); renomeie kitportal-T01b-PILOTO-12-360p e me mande. Não vai ao ar.']
    if not gera:
        passos = ['Nada para gerar: os 9 takes saem do painel do nora51 (já gerados e renomeados).']
    passos += [f'Corte de silêncio (seção “Cortar os silêncios”): {lista_usa}; Juntar tudo LIGADO, Corte seco → {corte_nome}.',
               f'CapCut: o {corte_nome} + a música de sempre a −18 dB; exporte SEM texto como {nn}-montado e me mande aqui (Drive, se passar de 30 MB).',
               f'Eu devolvo o {nn}-final. Confira no celular e poste em {v["dia"]} às {v["hora"]}, no Insta e no Face, ao vivo. Legenda: a do Insta tem o pedido de comentário; no Face, sem ele. Comentário: no Insta, comente e fixe (sem link); no Face, comente COMO A PÁGINA (já tem o link).']
    cfg = config_kit()
    if gera:
        p['central'] = {'imagem_unica': True,
                        'conferir': 'Conferir em cada take: é a Nora da kitportal-IMG (rosto, lua com 3 estrelinhas, trança, brincos, colar de Vênus, moletom verde-esmeralda); ela fala uma vez só, em inglês, com "eleven eleven" e "November tenth"; o braço do celular não se mexe; a mão livre só faz o gesto do take, na altura do ombro; sem texto, legenda ou música. Renomeie com o nome da lista.',
                        'passos': passos, 'config': cfg, 'agente': agente(len(ks), [NOMES[k] for k in ks]),
                        'colagens': [colagem(f'{nn}: {len(ks)} takes ({", ".join(ks)})', ks, list(range(len(ks))))]}
        if n == 51:
            p['imagem_central'] = IMG_CENTRAL
    else:
        p['central'] = {'imagem_unica': True, 'conferir': '', 'passos': passos, 'config': cfg, 'agente': agente(1, []), 'colagens': []}
        p['imagem_reutilizada'] = {'arquivo': 'kitportal-IMG', 'nota': 'gerada no painel do nora51'}
    if n == 51:
        p['clone'] = CLONE
        ordem = ['pecas', 'imagens', 'clone', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface', 'fala']
    elif gera:
        ordem = ['pecas', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface', 'fala']
    else:
        ordem = ['pecas', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface', 'fala']
    p['ordem'] = ordem
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', f'<title>Painel {nn} · kit do portal</title>', html, count=1)
    (R / f'PAINEL-NORA{n}.html').write_text(html, encoding='utf-8')
    print('ok', nn, 'takes', len(ks), 'gera', gera, 'créditos', creditos(gera))


for n in VIDEOS:
    montar(n)
