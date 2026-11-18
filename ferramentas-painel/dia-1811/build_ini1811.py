# Painel do curto de 18/11/2026 (ini1811): "Pause on your initial", 6 s, sem fala, só no Insta às 19h30.
# Decisões: o aluno (18/11 16h14 a 16h20): os cristais na mesa, sem a carta dourada; 10 papéis de caderno rasgados com as iniciais
# mais comuns das americanas de 45+ (MATERIAIS-INICIAIS-NOMES/LEIA.md); o dedo passa por cima de todas sem escolher; no fim os braços
# abertos ("qual?") e o sorriso. Fontes: o padrão 03 da pesquisa oficial (4,8 mi e 3,7 mi), a aula 18 (1:10:33, dez letras na tela),
# o Clone R72 conferido (aula 37, 1:22:27: símbolos dos EUA para a Índia não ficar no vídeo). O "pode montar" veio às 16h20.
# Nome fora da numeração (como o tsu1611): vai ao ar antes do nora70 e não muda o nome dele.
# Gerado no Flow (a imagem, 0 crédito) e no Muse (o clipe). Uso (raiz do repositório): python3 -I ferramentas-painel/dia-1811/build_ini1811.py
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
P63 = pacote('PAINEL-NORA63.html')
NOME = 'ini1811'
IMG = 'ini1811-IMG'
CLIPE = 'ini1811-CLIPE'
CIMA = ['M', 'J', 'S', 'L', 'C']   # da esquerda para a direita da imagem
BAIXO = ['A', 'B', 'K', 'D', 'P']  # da esquerda para a direita da imagem (o dedo volta pela linha de baixo, da direita para a esquerda: P, D, K, B, A)

JOIAS = ('small flat shiny gold crescent moon with three tiny gold stars on the outer edge of her cheekbone near the temple, on the left side of the image; long gold '
         'star-and-moon drop earrings; thin gold necklace with a small Venus pendant; thin gold bracelets; gold sun ring; hazel-green eyes; long, loose, softly wavy jet-black hair '
         'falling past her shoulders, not tied back; one thin braid wrapped with small gold rings clearly visible at the front, on the right side of the image; clean forehead with no jewelry,\n')
PELE = ('natural matte skin finish with visible pores and fine skin texture, subtle natural micro-imperfections, faint under-eye texture, natural variation in tone between face, '
        'neck and hands, delicate peach fuzz, no oily or wet shine and no specular hotspots on the forehead, nose or cheeks, no smoothing, skin tone, age and features exactly as in '
        'the reference image,\n'
        'hair exactly as in the reference image, with a few fine flyaway strands at the hairline and no floating strands, believable fabric weight and natural creases, all clothing '
        'unbranded, anatomically correct hands with five natural fingers each, nothing duplicated or floating, lifelike anatomy and proportions with natural facial asymmetry, caught '
        'in a natural moment rather than posed, eyes with natural moisture and small centred catchlights,\n')
FIM = ('no film emulation, straight smartphone frame, no date stamp, no watermark, natural phone colors, no color grading, natural skin tone preserved separately from the colour grade,\n'
       'photorealistic, unretouched, candid documentary, UGC style, no studio lighting, no filters, no tattoos, no extra, fused or missing fingers, no duplicated or floating objects, no '
       'warped reflections or architecture, the only writing anywhere in the image is the ten handwritten capital letters on the paper scraps (no other text, logos, captions or watermarks), '
       'no oily, wet, waxy or plastic skin, no beauty retouching or airbrushing, no HDR look or over-sharpening, no exaggerated background blur, no fortune-teller costume, no tarot cards, '
       'no golden card, no glow, sparkles, stars or light effects around the crystals,\n'
       'character consistency: identical face, same skin tone, same hair, same body proportions as the reference image — only wardrobe, environment, and pose change')
PAPEIS = ('ten small pieces of lined notebook paper on the table in front of her, each torn by hand from a spiral notebook with rough, uneven torn edges and faint blue lines, each '
          'about the size of a playing card, lying flat and slightly crooked like a real person placed them, arranged in two loose rows of five; on each piece ONE large capital letter '
          'is handwritten in thick black marker, slightly imperfect like real handwriting, filling most of the paper; IMPORTANT: the letters were written for the viewer, not for her: '
          'every letter stands upright in the photo, with the top of each letter pointing away from the camera toward her and the bottom of each letter pointing toward the camera '
          '(toward the bottom edge of the image), so the photo shows them right side up and perfectly readable, never upside down, never mirrored (from her seat they would look upside '
          'down); the top row, from the left side of the image to the right side, reads M, J, S, L, C; the bottom row, from the left side of the image to the right side, reads A, B, '
          'K, D, P; nothing else is written anywhere on the papers,\n')


def img():
    return ('RAW photo of the exact same character from the attached reference image, preserving every facial feature, identity, age, ethnicity, skin tone, and hairstyle exactly as shown in the reference,\n'
            'warm, curious, knowing smile with her lips gently closed, looking down at the papers,\n'
            'soft cream chunky-knit open cardigan over a plain black fine-knit top with a round neck, matte, no print, no logo; a tiny enamel lapel pin of the American flag, about 2 cm wide, '
            'pinned on the cardigan at chest height on the right side of the image, clearly visible; ' + JOIAS +
            'photo taken from about 1 meter in front of her, from a little above her eye height, the camera tilted slightly down so the whole tabletop and all ten papers are clearly '
            'visible and readable (no phone, phone stand or tripod anywhere in the image): she sits at a small square dark-wood table in a cozy real American living room in the early '
            'evening, facing the camera, framed from the head down to the tabletop, centered; ' + PAPEIS +
            'her right hand, on the left side of the image, hovers just above the first paper of the top row (the one with the letter M), the index finger extended and almost touching it, '
            'the other fingers relaxed; her left hand, on the right side of the image, rests flat on the table edge on the right side, away from the papers; around the papers, never '
            'covering them, stand a small purple amethyst cluster, a raw yellow citrine point and a smooth pink rose quartz stone, real and matte; both hands are fully visible, each with '
            'exactly five fingers,\n'
            'FRAMING, in percent of the image height from the top: from 0 to 18 percent only the plain warm wall behind her, with nothing on it (this band stays empty for text); '
            'the top of her head at about 20 percent, her eyes at about 28 percent; the table edge at about 50 percent; the two rows of papers between about 56 and 82 percent; from '
            '86 to 100 percent only the plain wooden tabletop (this band stays empty for a sticker),\n'
            'cozy real lived-in American living room, a plain warm beige wall behind her, the edge of a sofa with a knitted throw at the side of the frame,\n'
            'warm light from a small table lamp on the right side of the image, a little uneven, like a real phone photo indoors; no studio light, no ring light,\n' + PELE +
            'shot on a smartphone camera, iPhone 15 main camera: looks exactly like a real casual photo taken with an iPhone, slight phone grain, everything in focus, no bokeh, no filter, '
            'f/8 aperture, ISO 640, 1/60s shutter speed, natural depth of field, background stays readable, mild sensor noise in the shadows,\n' + FIM)


STORY = 'story-1811'
IG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
FIM_STORY = ('no film emulation, straight smartphone frame, no date stamp, no text, no watermark, natural phone colors, no color grading, natural skin tone preserved separately from the colour grade,\n'
             'photorealistic, unretouched, candid documentary, UGC style, no studio lighting, no filters, no tattoos, no extra, fused or missing fingers, no duplicated or floating objects, no '
             'warped reflections or architecture, no readable text, letters, logos, captions or watermarks anywhere (the papers are blank and face down), no oily, wet, waxy or plastic skin, '
             'no beauty retouching or airbrushing, no HDR look or over-sharpening, no exaggerated background blur, no fortune-teller costume, no tarot cards, no golden card, no glow, '
             'sparkles, stars or light effects around the statue or the crystals,\n'
             'character consistency: identical face, same skin tone, same hair, same body proportions as the reference image — only wardrobe, environment, and pose change')


def img_story():
    # 18/11 ~16h35 (pedido do aluno: "um stories novo com uma outra foto… mais focado nos vídeos que vão sair hoje"): a Nora no dia a dia (Clone R2), sem cartas,
    # na mesma sala do curto, com a estátua do anjo de asas douradas do alçapão do nora70 nas mãos e os cristais na mesa; espaço livre no alto (texto) e embaixo (adesivo).
    return ('RAW photo of the exact same character from the attached reference image, preserving every facial feature, identity, age, ethnicity, skin tone, and hairstyle exactly as shown in the reference,\n'
            'soft, warm, knowing smile with her lips gently closed, looking straight into the lens,\n'
            'soft cream chunky-knit open cardigan over a plain black fine-knit top with a round neck, matte, no print, no logo; a tiny enamel lapel pin of the American flag, about 2 cm wide, '
            'pinned on the cardigan at chest height on the right side of the image; ' + JOIAS +
            'casual photo taken by a friend from about 1.2 meters in front of her, at her chest height, straight on (no phone, phone stand or tripod anywhere in the image): she sits at a '
            'small square dark-wood table in her cozy real American living room in the early evening, facing the camera, framed from just above her head down to the tabletop, centered; '
            'her right hand, on the left side of the image, holds up a small vintage angel statue about 20 cm tall, with folded golden wings and a little dust on it, as if she has just '
            'brought it down from the attic, at shoulder height beside her face, the statue turned a little toward the camera and never covering her face; her left hand, on the right '
            'side of the image, rests on the table; the front of her cardigan, from her collarbones down to the table, stays clear, with no hands or objects in front of it; on the '
            'table in front of her stand a small purple amethyst cluster, a raw yellow citrine point and a smooth pink rose quartz stone, and two small torn pieces of lined notebook '
            'paper lie face down, blank, with nothing written on them; both hands are fully visible, each with exactly five fingers,\n'
            'FRAMING, in percent of the image height from the top: the top of her head at about 12 percent, her eyes at about 24 percent; the angel statue between about 18 and 45 '
            'percent, on the left side of the image, beside her face; from 44 to 72 percent only the plain front of her cream cardigan and black top, with nothing in front of it '
            '(this area stays empty for text and a link sticker); the table edge at about 74 percent; the crystals and the papers between about 76 and 92 percent,\n'
            'cozy real lived-in American living room, a plain warm beige wall behind her with a small American flag hanging on it on the right side of the image, partly visible behind her shoulder, the edge of a sofa with a knitted throw at the side of the frame,\n'
            'warm light from a small table lamp on the right side of the image, a little uneven, like a real phone photo indoors; no studio light, no ring light,\n' + PELE +
            'shot on a smartphone camera, iPhone 15 main camera: looks exactly like a real casual photo taken with an iPhone, slight phone grain, everything in focus, no bokeh, no filter, '
            'f/8 aperture, ISO 640, 1/60s shutter speed, natural depth of field, background stays readable, mild sensor noise in the shadows,\n' + FIM_STORY)


VID = ('Use the attached image as the first frame. Real casual 6-second video from a static camera, steady, no zoom, no camera movement, real speed, no slow motion; no phone, phone '
       'stand or tripod ever appears in the frame. The action starts in the very first frame: from 0 to 4 seconds her right hand (the hand on the left side of the frame) glides slowly '
       'and smoothly about one centimeter above the papers without touching or moving them, the index finger passing over each paper of the top row from the left side of the frame '
       'to the right side, then down to the bottom row and back from the right side of the frame to the left side, never stopping on any paper, while she looks down at the papers with '
       'a curious smile; from 4 to 6 seconds she lifts both hands from the table and opens her arms to the sides with her palms up, a playful little shrug as if asking which one, and '
       'looks straight into the lens with a warm, knowing smile. She never speaks and her lips stay closed in a smile the whole time. The ten torn notebook papers stay exactly as in '
       'the attached image the whole time: same positions, same handwritten capital letters, never moving, never changing, never blurring, never disappearing; the crystals stay still '
       'and do not glow. She keeps the same face, crescent moon with three tiny gold stars, earrings, necklace, bracelets, rings, cream cardigan and the small American flag pin the whole '
       'time; each hand has exactly five fingers; nothing appears or disappears. AUDIO: quiet room ambience only; no music, no voice. No on-screen text, no captions.')
MUSE = ('Generate exactly ONE video clip, only one version, vertical 9:16, about 6 seconds, using the attached image as the first frame. She does not speak in this clip. '
        'Name it ' + CLIPE + '. Follow the prompt exactly as written. Prompt: ' + VID)

TOPO = 'PAUSE ON YOUR INITIAL.\n2027 HAS A MESSAGE FOR YOU.'
FIM_TXT = 'WHICH ONE IS YOURS?'
INSTA_RESP = ['Your letter found you for a reason ✨ your 2027 reading is waiting in my story 🔮', 'I see you 💛 tap my photo, your next step is in my story',
              'That letter is your sign ✨ check my story before you go', 'Beautiful ✨ your quick 2027 reading is in my story 🔮', 'So glad this found you 💫 tap my photo for your reading']


def montar():
    perfil = copy.deepcopy(P46['perfil']); perfil.pop('teste', None)
    p = {
        'enxuto': True, 'clipe_unico': True, 'ocultar_bloco_agente_imagem': True,
        'perfil': perfil, 'trava_referencia': P46['trava_referencia'], 'figurino': 'soft cream chunky-knit open cardigan over a plain black top, with a tiny American flag pin',
        'excecao_estilo': '',
        'roteiro': {'id': 'ini1811-CURTO', 'titulo': 'ini1811 · 18/11 · o curto "Pause on your initial" (6 s, sem fala): só no Insta, entre 19h00 e 19h30',
                    'duracao_total': 6,
                    'descricao_instagram': ('Pause on your initial ✨ 2027 has a message for you\nYour private reading is waiting in my story 🔮\n'
                                            'Comment the letter you paused on 👇\n#manifestation #2027 #lawofattraction #angelnumbers'),
                    'descricao_face': '(não vai ao Face: vídeo sem fala fica fora do Face, R54)'},
        'refs': ['Folha da Nora v2 (1K), só ela, na imagem'],
        'imagens': [{'rotulo': 'IMAGEM 1 · ' + IMG, 'cena': '(o prompt está na seção do Clipe, item 1)', 'anexar': 'a folha da Nora (1K)'}],
        'videos': [{'rotulo': 'V1', 'cena': 'Clipe único, sem fala', 'duracao': 6, 'primeiro_quadro': 'IMAGEM 1 (' + IMG + ')', 'acao': '(ver seção Clipe)', 'b_roll': '',
                    'fala': '(sem fala) texto na tela: ' + TOPO.replace('\n', ' ') + ' / no fim: ' + FIM_TXT,
                    'movimentacao': '(sem Central: o prompt do clipe está na seção Clipe)', 'arquivo': CLIPE}],
        'texto_tela': {'hook': TOPO, 'hook_comeca': 'o segundo 0', 'hook_termina': 'quando ela abre os braços (~4 s); dali ao fim: ' + FIM_TXT, 'hook_alt': '', 'extras': []},
        'comentario_fixado': {'insta': 'Your letter is your sign ✨ tap my profile picture to see what 2027 holds for you in my story 🔮', 'face': '(sem Face)'},
        'respostas_face': {'insta': INSTA_RESP, 'face': []},
        'story': {'ja_postado': False, 'nota': ('STORY NOVO DE HOJE (' + STORY + ', no lugar do story-1211): gere a foto pelo item 3 da seção Clipe (x4, 0 crédito) e ME MANDE AS 4 até ~18h15; '
                  'eu escolho, ponho o texto (no jeito das contas do nicho: caixas do próprio Instagram no meio da tela) e devolvo em ~10 min. Poste ANTES do curto (e antes de ~19h39, quando o story-1211 vence), ao vivo, no Insta e no Face, '
                  'com o adesivo de link logo abaixo do texto, no centro (texto do adesivo: TAP TO CONTINUE 🎁, como 4 das 10 contas do nicho; se quiser, o GIF da mãozinha clicando e uma música de piano calma do próprio app). Insta (STORYIG): ' + IG + ' · Face (FACE): ' + FB)},
        'central': {'imagem_unica': True,
                    'conferir': ('Conferir: é a Nora (lua com 3 estrelinhas, trança com anéis, brincos de estrela e lua); os 10 papéis continuam iguais e legíveis do começo ao fim '
                                 '(M J S L C em cima, A B K D P embaixo); o dedo passa sem parar e sem mexer os papéis; no fim ela abre os braços e sorri; boca fechada; 5 dedos em cada mão.'),
                    'passos': ['Vídeo de 6 s SEM fala. Não usa a Central do curso: a imagem sai no Flow e o clipe no Muse (seção Clipe).']},
        'pre_gancho': {
            'titulo_secao': 'Clipe (6 s, sem fala)', 'duracao': 6, 'tomadas': 1, 'com_rosto': True, 'nome_video': CLIPE,
            'conceito': ('O curto "Pause on your initial" (o padrão 03 da pesquisa oficial; aula 18, 1:10:33): a Nora à mesa com os cristais e 10 papéis de caderno rasgados, '
                         'cada um com uma inicial; o dedo passa por cima de todos sem escolher (quem assiste pausa na sua) e no fim ela abre os braços, como quem pergunta "qual?", '
                         'e sorri. Sem fala. O broche da bandeira dos EUA segura o público americano (aula 37, 1:22:27). Eu ponho os textos, os números, a faixa e a seta.'),
            'modo': ('(A foto do story é o item 3.) 1) A imagem: Flow → Imagem · 9:16 · Nano Banana Pro · x4, anexando SÓ a folha da Nora (1K) (0 crédito). ME MANDE AS 4: eu confiro as letras (letra de IA é o que mais erra). '
                     '2) O clipe: no Muse, na conversa da Nora já configurada, anexe a escolhida e cole o bloco do item 2 inteiro (1 versão só, ~2% do grátis da semana). Baixe e me mande.'),
            'etapas': [
                {'tipo': 'img', 'titulo': 'Imagem: a Nora à mesa com os cristais e os 10 papéis', 'nome': IMG, 'anexar': 'só a folha da Nora (1K)',
                 'quadros': ('x4, 0 crédito. Lista: é a Nora (lua com 3 estrelinhas na bochecha do lado esquerdo da imagem, trança com anéis, brincos de estrela e lua, colar de Vênus); '
                             '10 papéis de caderno rasgados, em 2 linhas de 5, cada um com UMA letra grande à mão: em cima M J S L C, embaixo A B K D P, TODAS EM PÉ PARA QUEM VÊ A FOTO (nada de letra de cabeça para baixo: o M não pode virar W), sem letra repetida, torta '
                             'demais ou faltando; o broche da bandeira dos EUA no cardigã; o dedo da mão do lado esquerdo da imagem em cima do papel do M; os cristais sem brilho e '
                             'sem cobrir papel; 5 dedos em cada mão; o alto da imagem é só parede. Renomeie para ' + IMG + ' e me mande as 4.'),
                 'prompt': img()},
                {'tipo': 'vid', 'titulo': 'Clipe no Muse: o dedo passa pelas letras, ela abre os braços e sorri', 'nome': CLIPE, 'duracao': 6,
                 'quadros': ('No Muse, na conversa da Nora: anexe a ' + IMG + ' e cole o bloco abaixo, inteiro (pede 1 versão só). Confira se tem: as 10 letras iguais do '
                             'começo ao fim, o dedo passando sem parar e sem mexer os papéis, os braços abertos e o sorriso no fim, a boca fechada, 5 dedos. Se recusar: '
                             '"Generate it again, exactly as written". Baixe e me mande (eu corto em ~6 s). Só se sair errado, peça de novo.'),
                 'prompt': MUSE},
                {'tipo': 'img', 'titulo': 'Story de hoje: a foto nova (a Nora com a estátua do anjo e os cristais)', 'nome': STORY, 'anexar': 'só a folha da Nora (1K)',
                 'quadros': ('Flow → Imagem · 9:16 · Nano Banana Pro · x4, anexando SÓ a folha da Nora (1K) (0 crédito). Lista: é a Nora (lua com 3 estrelinhas na bochecha do lado esquerdo '
                             'da imagem, trança com anéis, brincos de estrela e lua, colar de Vênus); ela olha para a lente; a estátua do anjo de asas douradas nas mãos, sem cobrir o rosto; '
                             'a estátua na altura do ombro, ao lado do rosto, sem cobrir; o peito (o cardigã) livre, sem mão nem objeto na frente (é onde vão o texto e o adesivo, no meio da tela, como nas contas do nicho); os cristais e os papéis virados na mesa, embaixo; nenhuma carta; 5 dedos em cada mão. '
                             'Renomeie para ' + STORY + ' e ME MANDE AS 4 até ~18h15.'),
                 'prompt': img_story()}],
        },
        'edicao_linha': [
            {'quando': '1. CapCut', 'texto': 'Projeto novo com o ' + CLIPE, 'como': 'Sem cortar nada (eu corto em ~6 s e emendo o fim no começo).'},
            {'quando': '2. Música', 'texto': 'A música de sempre (“Ambient Mystical Drone”), do segundo 0 ao fim, −12 dB', 'como': 'Não tem fala: a música pode ficar mais alta que nos falados.'},
            {'quando': '3. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
             'como': '1080×1920, nome ' + NOME + '-montado. Eu ponho a caixa do topo, a frase do fim, os números 222 e 11:11, a faixa do story e a seta, e devolvo o ' + NOME + '-final.'}],
        'pecas': {'titulo_decisao': 'Resumo', 'lista': [
            {'nome': IMG, 'tipo': 'imagem 1 (primeiro quadro)', 'status': 'gerar', 'descricao': 'A Nora à mesa, cardigã creme com o broche da bandeira dos EUA, os 10 papéis com as iniciais, ametista, citrino e quartzo rosa.'},
            {'nome': STORY, 'tipo': 'foto do story', 'status': 'gerar', 'descricao': 'A Nora à mesa com a estátua do anjo de asas douradas (o alçapão do nora70) na altura do ombro e os cristais; eu ponho o texto no meio da tela.'},
            {'nome': CLIPE, 'tipo': 'clipe sem fala (Muse)', 'status': 'gerar', 'descricao': '6 s: o dedo passa por cima das 10 letras sem parar; ela abre os braços ("qual?") e sorri para a câmera.'}],
            'decisao': ['AGORA: a imagem do curto e a foto do story no Flow (x4 cada, 0 crédito) e ME MANDE AS 4 DE CADA; depois o clipe no Muse (1 versão, ~2% do grátis da semana).',
                        'Monte só a música no CapCut e me mande o ' + NOME + '-montado até ~18h40. Eu devolvo o ' + NOME + '-final em ~15 min.',
                        'Antes de postar: o story repostado (vence ~19h39). Postar só no Insta entre 19h00 e 19h30 (19h30 é a melhor janela da planilha; 19h00 a 19h10 também serve), ao vivo, com a legenda abaixo e o comentário fixado. No Face, nada nesse horário (sem fala fica fora do Face).',
                        'O nora70 vai à 0h00 no Insta e no Face (o montado até ~23h).']},
    }
    mt = copy.deepcopy(P49['mapa_tela'])
    mt['numeros'] = [dict(t='222', x=18, y=10.5, onde='alto à esquerda', cor_nome='branco', cor='#FFFFFF', tamanho=13),
                     dict(t='11:11', x=82, y=10.5, onde='alto à direita', cor_nome='branco', cor='#FFFFFF', tamanho=14)]
    mt['estilos'] = [{'nome': 'Caixa do topo: ' + ' / '.join(TOPO.split('\n')) + '; dos ~4 s ao fim: ' + FIM_TXT, 'fonte': 'Poppins ExtraBold', 'cor': 'caixa amarela sólida, texto preto',
                      'tamanho': '2 linhas', 'contorno': 'Plano de fundo sólido', 'obs': 'Na faixa da parede acima da cabeça. Eu ponho (P45).'},
                     {'nome': 'Faixa do story: “Tap my photo: your 2027 reading is in my story” + seta para baixo à esquerda', 'fonte': 'Poppins Bold', 'cor': '—', 'tamanho': '9',
                      'contorno': 'Plano de fundo sólido', 'obs': 'Dos ~2 s ao fim, embaixo, abaixo dos papéis. Eu ponho.'}]
    mt['regras'] = ['Eu ponho os textos, os números e a faixa (P45); você monta só o clipe e a música.']
    p['mapa_tela'] = mt
    p['ordem'] = ['pecas', 'prehook', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>Painel ini1811 · o curto das iniciais</title>', html, count=1)
    (R / 'PAINEL-INI1811.html').write_text(html, encoding='utf-8')
    print('ok PAINEL-INI1811.html')


montar()
