# 31/10/2026: painel do nora46, o 1º vídeo do corpo B (portal 11/11, 3 sinais; regra P42, aula do Iorhan de 30/10).
# Base: PAINEL-NORA40.html (Central, voz, identidade) e PAINEL-NORA44.html (mapa da tela, story).
# Uso: python3 build3110.py <pasta do repositório>
import re, json, copy, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

def ler(nome):
    s = open(f'{BASE}/{nome}', encoding='utf-8').read()
    return json.loads(re.search(r'const PACOTE = (\{.*?\});\n', s, re.S).group(1))

def gravar(n, p):
    m = open(f'{BASE}/PAINEL-MODELO.html', encoding='utf-8').read()
    assert m.count('const PACOTE = null;') == 1 and 'im.prompt_completo||promptImagem(im)' in m
    m = m.replace('<title>Painel de Produção</title>', f'<title>Painel nora{n}</title>')
    m = m.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    open(f'{BASE}/PAINEL-NORA{n}.html', 'w', encoding='utf-8').write(m)

P40, P44 = ler('PAINEL-NORA40.html'), ler('PAINEL-NORA44.html')

# ---------------- falas (as do roteiro aprovado em 31/10) ----------------
TAKES = [
 ('T01-gancho-portal-sinal', 'Gancho: o portal e a predestinação',
  "The 11:11 portal is about to open, and if this video reached you today, it's not a coincidence. It's a sign."),
 ('T02-qualificacao-vida-parada', 'Qualificação (a dor em uma frase)',
  "If you've been working so hard and still feel stuck, like your real life hasn't started yet, this message is for you."),
 ('T03-autoridade-numerologia', 'Autoridade + o mecanismo (numerologia)',
  "As an astrologer, here's what this date means: in numerology, one is a new beginning, and 11/11 holds four of them."),
 ('T04-portal-tres-sinais', 'Por que é um portal + a promessa dos 3 sinais',
  "That's why it's called a portal, and before it opens, the universe sends three signs to the people it has chosen."),
 ('T05-sinal-1-numeros', 'Sinal 1: os números repetidos',
  "Sign one: you keep seeing 11:11 or 222 on the clock, on receipts, even on license plates, and it makes you stop."),
 ('T06-sinal-2-abrindo-espaco', 'Sinal 2: quem não é para você vai embora',
  "Sign two: the wrong people are fading out of your life, and you're not chasing them back. You're making room."),
 ('T07-sinal-3-algo-bom', 'Sinal 3: o que quase ninguém percebe',
  "Sign three is the one almost nobody notices: a quiet feeling that something good is coming, even if you can't explain it."),
 ('T08-imagine-meses', 'Future pacing (imagens do desejo na tela)',
  "If that's you, imagine a few months from now: money stops being a worry, someone stays, and home feels like peace."),
 ('T09-prova-avaliacoes', 'Prova real (as avaliações na tela)',
  "Over two thousand people have already rated this reading. Here's what some of them wrote after picking their cards."),
 ('T10-cta-leitura-story', 'CTA com motivo (os sinais e a data do portal)',
  "If you noticed any of these signs, tap my profile picture and start your reading in my story before November 11th."),
 ('T11-cta-tres-cartas', 'O que ela encontra no story',
  "You'll pick three cards, and they'll show you what this new chapter is bringing you, in love and in money."),
 ('T12-seguir-222-mandar', 'Engajamento, só depois do CTA',
  "And if this found you, follow me, comment 222, and send this to yourself so it's waiting for you on the 11th."),
]

# Movimentação FINAL (31/10 ~03h, pela nora46-IMG aprovada, a 3ª das 3 variações): o microfone ficou na borda esquerda, junto do braço
# do lado esquerdo da imagem; por isso quem gesticula é a mão do lado DIREITO da imagem (a esquerda dela). Uma frase por take, sem palavras da fala.
ABRE = ('Throughout the whole 10 seconds she stays seated at the desk facing the lens, her right hand on the left side of the frame, next to the microphone, '
        'rests flat on the desk and never moves, her left hand on the right side of the frame rests flat on the desk except during the one small gesture '
        'described here, which always happens at the height of her shoulder on the right side of the frame and never in front of her face or mouth, '
        'she never touches or leans toward the microphone, and ')
FECHA = (', and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; everything else in the scene '
         'stays completely still and each hand has exactly five fingers.')
EXPR = {
 'T01': 'her eyes stay on the lens, during the first half of the take she leans slightly toward the lens with her eyebrows a little raised and an intrigued look, during the second half she gives one slow knowing nod with a warm half-smile, both hands staying on the desk',
 'T02': 'her eyes stay on the lens, during the first half of the take she tilts her head slightly to one side with a soft, understanding look, during the second half her face warms and she gives one small reassuring nod, both hands staying on the desk',
 'T03': 'her eyes stay on the lens with a calm, confident expert look, during the first half of the take she raises her left hand to the height of her shoulder on the right side of the frame with the palm open and facing up as if explaining, during the second half she lifts only the index finger of that hand once for a moment and then lowers the hand back to the desk',
 'T04': 'her eyes stay on the lens, during the first half of the take she holds a calm, assured look, during the second half she raises her left hand to the height of her shoulder on the right side of the frame with the palm open toward the lens for a moment as if presenting something and then lowers it back to the desk with a small smile',
 'T05': 'her eyes stay on the lens, during the first half of the take her eyebrows lift with a look of recognition, during the second half she gives two small quick nods with a knowing smile, both hands staying on the desk',
 'T06': 'her eyes stay on the lens, during the first half of the take she makes one slow, gentle outward wave of her left hand at the height of her shoulder toward the right edge of the frame as if letting something go, during the second half the hand returns to the desk and she shows a calm, relieved half-smile',
 'T07': 'her eyes stay on the lens, during the first half of the take she leans slightly toward the lens with a soft, almost secretive look, during the second half she rests her left palm flat at collarbone height on the white top for a moment with a warm smile and then lowers the hand back to the desk',
 'T08': 'during the first half of the take her eyes glance up and slightly to the side as if picturing something lovely, during the second half her eyes return to the lens and a wide, warm smile grows on her face, both hands staying on the desk',
 'T09': 'her eyes stay on the lens, during the first half of the take she holds a calm, confident look, during the second half she turns her left palm up at the height of her shoulder on the right side of the frame and gestures gently down toward the lower part of the frame and then lowers the hand back to the desk',
 'T10': 'her eyes stay on the lens with an encouraging look, during the first half of the take she gives one small nod, during the second half she points her left index finger down toward the bottom of the frame for a moment and then lowers the hand back to the desk',
 'T11': 'her eyes stay on the lens, during the first half of the take her eyebrows lift with a bright, excited look, during the second half she opens her left hand at the height of her shoulder on the right side of the frame with the palm up as if offering a gift while a warm smile grows, and then the hand returns to the desk',
 'T12': 'her eyes stay on the lens, during the first half of the take she gives a warm smile and one slow nod, during the second half her eyes glance down toward the lower part of the frame for one moment and come back to the lens with a warm smile, both hands staying on the desk',
}
def mov(k): return ABRE + EXPR[k] + FECHA

wc = lambda s: len(s.split())
COMUNS = {'and it','of the','in the','on the','to the','the end','the lens','of her','her head','the take','the first','the last','she gives',
          'one small','her eyes','for one','a soft','and her','at the','her face','the clip','the second','and the','with the','the left',
          'the right','is the','for the','the one','to one','one of','of that','and then','is a','a new','it has','she keeps','her lips'}
def bigr(t):
    w = re.findall(r"[a-z0-9:%'/]+", t.lower()); return {' '.join(w[i:i+2]) for i in range(len(w)-1)}

T = [(f'nora46-{suf}', cena, fala, mov(suf[:3])) for suf, cena, fala in TAKES]
PROIBIDAS = ['keep your mouth shut', 'before it disappears', 'before they disappear', 'miracle', 'guarantee', 'jealous', 'envy', 'curse', 'block',
             'turnaround', 'opportunit', 'warning', 'seven minutes', 'skip', 'scarcity', 'free']
def checar():
    F = [t[2] for t in T]
    for a, c, f, m in T:
        n = wc(f); assert 18 <= n <= 22, (a, n)
        ov = (bigr(f) & bigr(m)) - COMUNS
        assert not ov, ('SOBREPOSICAO', a, ov)
        assert m.count('. ') == 0 and m.endswith('.'), ('movimentacao com mais de uma frase', a)
        for p in PROIBIDAS: assert p not in f.lower(), ('PROIBIDA', a, p)
    full = ' '.join(F); sents = [s.strip() for s in re.findall(r'[^.!?]+[.!?]', full)]
    for L in (22, 23, 24, 25):
        tk, cur = [], []
        for s in sents:
            if cur and wc(' '.join(cur + [s])) > L: tk.append(' '.join(cur)); cur = [s]
            else: cur.append(s)
        tk.append(' '.join(cur))
        assert tk == F, ('DIVISOR', L, [wc(x) for x in tk])
checar()

# ---------------- identidade, roupa, imagens ----------------
FIG = ('subtle mystic with a polished expert look; a tailored ivory-cream blazer with notched lapels, worn open, over a plain bright-white fine silky blouse '
       'with a simple round neckline, both smooth and matte, no print, embroidery, logo or shine. Clothing is secondary to her face and her gestures. '
       'Fixed accessories, always visible: the long gold star-and-moon drop earrings, the long thin gold chain with the small gold Venus-symbol pendant '
       'resting on the white blouse, thin gold bracelets on her left wrist, a small gold sun-symbol ring on her right index finger and the gold face gems '
       'from the reference sheet; no other jewelry, turban, cape or costume')
CENA46 = ('generate a NEW photo from the attached character sheet only (do not edit any other image). A vertical 9:16 photo taken during the day in a bright, '
  'clean, modern home studio in an American house, as if a friend took it with a phone. She sits at a light natural-oak desk, facing the camera, shoulders square, '
  'leaning very slightly forward, and she looks straight into the lens with a calm, confident, warm expression and a faint closed-lip smile, like an expert about '
  'to explain something. CAMERA: a handheld phone at the height of her collarbones, about 70 cm in front of her, straight on, level, no tilt. FRAMING, in percent '
  'of the image height from the top: from 0 to 13 percent only the plain warm-white wall behind her shows; the top of her head is at about 14 percent, her eyes at '
  'about 33 percent, her chin at about 45 percent; the front edge of the desk crosses the frame horizontally at about 90 percent; her waist is just above the desk '
  'edge; her knees and legs are NOT in the frame. HANDS: both forearms rest on the desk; her RIGHT hand (the hand on the LEFT side of the image) lies relaxed on the '
  'desk a little left of center, with the small gold sun ring on her index finger; her LEFT hand (the hand on the RIGHT side of the image) lies flat and relaxed on '
  'the desk a little right of center, with the thin gold bracelets on that wrist; both hands are between about 84 and 92 percent of the image height, not touching '
  'each other, each with exactly five fingers and natural proportions; nothing is in her hands. PROPS ON THE DESK: on the LEFT side of the image, a black podcast '
  'microphone with a round black foam windscreen on a slim black boom arm that comes in from the left edge of the frame; the microphone head is at about 58 to 66 '
  'percent of the image height and between about 6 and 20 percent of the image width, angled toward her but well to the side of her body, never in front of her '
  'face, mouth, chin or hands; on the RIGHT side of the image, a small green potted plant in a white ceramic pot at the edge of the desk, not taller than her '
  'shoulder. BACKGROUND (softly out of focus): a plain warm-white wall; on the RIGHT side of the image, behind her shoulder, a light-oak wall shelf with a few books '
  'with plain spines and no readable titles, and a small American flag (about 20 by 13 cm, on a short wooden stick) standing in a white mug on the shelf. LIGHT: '
  'soft, bright natural window daylight from the LEFT side of the image as the key light, gentle and even on her face, with soft natural shadows; a clean, airy, '
  'professional but real look, like a real phone photo, not a commercial shoot. DO NOT INCLUDE: candles, crystals, tarot cards, smoke, a crystal ball, a laptop, a '
  'phone, headphones, other people, pets, mirrors, posters, picture frames with text, readable text, captions, watermarks, logos or a date stamp. Do not '
  'rejuvenate or smooth her face.')
NEG_GEN = 'No text, captions, logos, watermark or date stamp anywhere in the image. Natural skin texture; every hand has exactly five fingers with natural proportions.'
D1 = ('Vertical 9:16 photorealistic close-up phone photo, spontaneous and real, of a woman\'s hands only (no face in the frame) holding a loose, generous fan of US '
      'dollar bills just above a light wooden kitchen table in warm morning sunlight; one thin gold bracelet on her wrist; a white coffee mug and a small plant softly '
      'out of focus in the background. The bills are a little out of focus at the edges, so no serial number, portrait or small print on them is readable. ' + NEG_GEN)
D2 = ('Vertical 9:16 photorealistic candid phone photo of a happy couple in their thirties laughing together while cooking in a sunlit, cozy American kitchen; the '
      'man stands behind the woman with one arm around her waist and she turns her head toward him, smiling; both faces are partly turned away from the camera, a '
      'real, unposed moment; warm afternoon light through a window; a wooden cutting board with vegetables on the counter. No famous or recognizable people. ' + NEG_GEN)
D3 = ('Vertical 9:16 photorealistic close-up phone photo of a woman\'s hand only (no face in the frame) holding a set of house keys on a simple silver ring in front '
      'of the white front door of a cozy American house at golden hour; the porch light is on and glows warm; a small potted plant and a plain doormat by the door; '
      'the door, the porch and the warm light are softly out of focus behind the keys. No house number. ' + NEG_GEN)

REF_TXT = ('VISUAL REFERENCE LOCK: use exclusively the ATTACHED references as identity authorities. Preserve the face, build, hair, proportions and appearance of '
           'the human and the pet. Do not mix identities. ')
ESTILO_IMG = ('UGC STYLE LOCK: vertical 9:16 image, photorealistic, shot in an American home with the spontaneous look of a smartphone. Natural light, real skin, '
              'fabric and hair textures, casual and slightly imperfect framing. The camera stays out of frame. No text, caption, logo, watermark or advertising look.')
FIG_STORY = FIG.replace('Clothing is secondary to her face and her gestures.', 'Clothing is secondary to the contrast of the three cards on the desk.')
CENA_STORY = ('generate a NEW photo from the attached character sheet only (do not edit any other image). A vertical 9:16 photo taken in the evening at a light-oak '
  'desk in a cozy American home studio, as if a friend took it with a phone. She sits behind the desk facing the camera, shoulders square, leaning slightly forward, '
  'and looks straight into the lens with a soft, warm, knowing smile, lips gently closed. CAMERA: a phone at the height of her eyes, about 90 cm in front of her, '
  'straight on, no tilt. FRAMING, in percent of the image height from the top: from 0 to 24 percent only the plain deep emerald-green painted wall behind her shows, '
  'with nothing on it (this band stays empty for text); the top of her head is at about 25 percent, her eyes at about 35 percent, her chin at about 45 percent; her '
  'hands and the three cards on the desk are between about 60 and 76 percent; from 78 to 100 percent only the plain, empty light-oak desk top shows (this band stays '
  'empty for a sticker). THE THREE CARDS: exactly three tall, narrow tarot cards, each about 7 cm wide and 12 cm tall, lie flat on the desk in front of her, face '
  'down, in one neat straight row side by side about 2 cm apart, centered left to right, the row about half of the image width, the long side of each card '
  'pointing toward the camera. All three backs are identical: deep navy blue with a fine ornate gold border and one small gold eight-pointed star in the center. No '
  'card face is visible; there are no letters, numbers, words or logos on the cards; there are no other cards and no deck anywhere. HANDS: her RIGHT hand (the hand '
  'on the LEFT side of the image) is held just above the middle card, the tip of her index finger about 1 cm above it, as if she is about to pick it; her LEFT hand '
  '(the hand on the RIGHT side of the image) rests flat on the desk on the right side of the image, with the thin gold bracelets visible; each hand has exactly five '
  'fingers, and neither hand covers a card or her face. LIGHT: one small brass desk lamp with a warm bulb at the far right edge of the image, at the height of her '
  'shoulder, softly lights her face from the right side of the image; the rest of the room falls into soft warm shadow, and the top band of wall stays dark enough '
  'for light text to read on it. BACKGROUND: on the desk at the right edge of the image, out of focus, a white mug holds a small American flag on a stick. DO NOT '
  'INCLUDE: candles, crystals, smoke, flowers, a crystal ball, a phone, a microphone, other people, pets, mirrors, windows, picture frames, posters, text, captions, '
  'watermarks, logos or a date stamp. The three cards stay face down and flat. Do not rejuvenate or smooth the skin.')
STORY_PROMPT = (REF_TXT + P40['trava_referencia'] + '\n\nFIXED OUTFIT: ' + FIG_STORY + '\n\n' + ESTILO_IMG + '\n\nSCENE: ' + CENA_STORY)

LINK_IG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
LINK_FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
assert LINK_IG in json.dumps(P44['story'], ensure_ascii=False) and LINK_FB in json.dumps(P44['story'], ensure_ascii=False)

LEITURA = ('31/10/2026, das ~00h40 às ~01h15: li inteiros, com a ferramenta de leitura, nesta sessão, todos os arquivos de LEIA-TUDO-ANTES.md: FATOS-DO-ALUNO.md, '
  'CLAUDE.md, 00-LEIA-PRIMEIRO.md, PROJETO-Dana.md, BRIEFING-MANIFESTACAO.md, AULA-IORHAN-30-10-COPY-QUE-CONVERTE.md, BRIEFING-LOVECHART.md, LICOES-FLOW-E-PROMPTS.md, '
  'COMUNIDADE-E-ESTRATEGIA.md, VALIDACAO-CONTA-E-AVATAR.md, DNA Visual - Dana.md, DNA Visual - Nora.md, DNA Visual - Nora v2.md, REGISTRO-DE-PERSONAS.md, hooks.md, '
  'Formatos Narrativos - Problema e Cenario.md, Exemplos de Roteiros - 2 Formatos.md, ctas.md, COMUNICACAO-VISCERAL-E-FALADA.md, BIBLIOTECA-BODIES.md, '
  'BIBLIOTECA-COLD-READING.md, BIBLIOTECA-COPY.md, BIBLIOTECA-COPY-100-ROTEIROS.md, PESQUISA-PUBLICO.md, BIBLIOTECA-VIDEOS-VIRAIS.md, BIBLIOTECA-PRE-GANCHOS.md, '
  'Prompts.txt, CHECKLIST-DE-PRODUCAO.md, PAPEL-AGENTE-FLOW.md, GUIA-CREATIVE-HUB.md, os PLANO-CREDITOS-*, os PASSO-A-PASSO-*, EXEMPLO-ROTEIRO-APROVADO-FIGADO.md, '
  'EXEMPLO-PACOTE-FIGADO.md, PAINEL-MODELO.html, METRICAS-NORA.csv, METRICAS-NORA-LEIA.md, BIBLIOTECA-DE-TAKES.md, os ROTEIRO-R001 a ROTEIRO-NORA47, '
  'ROTEIRO-LOVECHART-RESERVA, os 4 RESERVA-ROTEIRO-*, os STORY-* e os TAKE-NOVO-*; e PROVAS-REAIS-TRUSTPILOT.md e os pacotes dos painéis do nora40 e do nora44. '
  'Não li (não se aplicam): FOTO-PERFIL-DANA.md, PROMPT-BLUEPRINT-COMUNIDADE.md, PLANO-MVM-LEGACY-APPYON.md e os PDFs.')

# ---------------- pacote ----------------
p = {'perfil': copy.deepcopy(P40['perfil']), 'trava_referencia': P40['trava_referencia'], 'figurino': FIG, 'excecao_estilo': '',
     'ocultar_bloco_agente_imagem': True}
p['roteiro'] = {
  'id': 'nora46-CORPO-B-PORTAL-1111-TRES-SINAIS',
  'titulo': 'Corpo B (Manifestation, aula do Iorhan): o portal 11/11 e os 3 sinais',
  'dor': 'trabalhar muito e sentir que a vida de verdade ainda não começou; o desejo de dinheiro, amor e paz (ângulo positivo, P42)',
  'formato': 'Hook da pedra escura (nora34-PRE, ~3,5 s) + 12 takes (~90 s): portal e predestinação → qualificação → a Nora explica o portal → 3 sinais → imagine → avaliações reais → story com motivo → seguir, 222 e mandar para si',
  'molde_hook': 'anúncios escalados do portal ("The November 11th portal has opened… If you\'re seeing this, it\'s not a coincidence") + predestinação saudável do Iorhan + Estrutura A (checklist de sinais)',
  'duracao_total': 90,
  'descricao_instagram': "The 11:11 portal is opening. 3 signs it chose you. 🔮\nPick 3 cards in my story and see what your new chapter brings. Follow me + comment 222.\n#manifestation #1111portal #astrology #usa #usareels",
  'leitura_registro': LEITURA}
p['refs'] = ['Blueprint da Nora v2 (só ele) na nora46-IMG e no story', 'Imagens do desejo: sem anexo', 'Avaliações: provas-trustpilot/01 a 03 (prontas)']
p['imagens'] = [
  {'rotulo': 'IMAGEM 1 · nora46-IMG (os 12 takes) · APROVADA: a 3ª das 3', 'cena': CENA46, 'anexar': 'SÓ o blueprint da Nora v2 (a folha de consistência). Nenhuma outra imagem.'},
  {'rotulo': 'IMAGEM 2 · nora46-DESEJO-1-dinheiro (Take 8) · APROVADA', 'cena': '(sem a Nora)', 'prompt_completo': D1, 'anexar': 'NADA (imagem sem a Nora).'},
  {'rotulo': 'IMAGEM 3 · nora46-DESEJO-2-casal (Take 8) · APROVADA', 'cena': '(sem a Nora)', 'prompt_completo': D2, 'anexar': 'NADA (imagem sem a Nora).'},
  {'rotulo': 'IMAGEM 4 · nora46-DESEJO-3-casa (Take 8) · APROVADA', 'cena': '(sem a Nora)', 'prompt_completo': D3, 'anexar': 'NADA (imagem sem a Nora).'}]
p['videos'] = [{'rotulo': f'T{i+1:02d}', 'cena': f'Take {i+1}/12 · {c}', 'duracao': '10', 'primeiro_quadro': 'IMAGEM 1', 'acao': '', 'b_roll': '',
                'fala': f, 'movimentacao': m, 'arquivo': a} for i, (a, c, f, m) in enumerate(T)]
p['texto_tela'] = {'hook': 'The 11:11 portal is opening.\n3 signs it chose you', 'hook_comeca': 'o primeiro quadro do pré-gancho',
                   'hook_termina': "It's a sign.", 'hook_alt': '', 'extras': []}
p['comentario_fixado'] = {
  'insta': "If you noticed even one of these signs, your new chapter is already on its way. ✨ Tap my photo, open my story and pick your 3 cards: see what it's bringing you in love and money before 11/11. 🔮 Comment 222 to claim it.",
  'face': "If you noticed even one of these signs, your new chapter is already on its way. ✨ Tap my profile picture, open my Story and pick your 3 cards: see what it's bringing you in love and money before 11/11. 🔮 Comment 222 to claim it."}
p['pre_gancho'] = {'titulo_secao': 'CapCut: o hook (a pedra escura, já pronta) + o corpo cortado', 'duracao': 4, 'tomadas': 1, 'com_rosto': True, 'etapas': [],
  'conceito': 'A pedra escura que racha (nora34-PRE), já gerada: 0 crédito. Foi o hook que mais segurou num longo (nora43: 69,5% nos 3 s, 19 s de média). Corte seco para o Take 1, que já abre falando do portal.',
  'modo': 'Não gere nada aqui. No CapCut, use a nora34-PRE como está (sem espelhar).',
  'montagem': '1) nora34-PRE: uns 3,5 s (corte logo depois que as metades abrem).\n2) Corte seco para o corpo cortado (nora46-cortado: T01 a T12).\n3) A caixa do topo já entra no primeiro quadro do hook.',
  'texto_tela': '', 'edicao': ''}

c = copy.deepcopy(P40['central'])
LIVRE = ('Casual handheld smartphone video in a bright, clean real American home studio during the day, lit by soft daylight from a window at the left edge of the frame. '
  'CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair with the thin gold-ringed braid on the right side of the frame, her gold moon and star '
  'face gems, her drop earrings, her Venus necklace, her bracelets and rings, her open ivory-cream blazer and her plain white round-neck top stay exactly as in the '
  'reference image; she stays seated at the light-oak desk facing the lens; the framing is exactly the one of the reference image, from a little above the top of her '
  'head down to the desk, with her face centered in the upper half of the frame and her eyes at about 31 percent of the frame height; her right hand, on the left side '
  'of the frame next to the microphone, rests flat on the desk for the whole clip; her left hand, on the right side of the frame, rests flat on the desk and only rises '
  'for the one small gesture of each take, always at the height of her shoulder on the right side of the frame, never in front of her face or mouth, and then returns '
  'to the desk; the black podcast microphone on its boom arm at the left edge of the frame, the window, the shelf with the books, the small American flag and the mug '
  'at the upper right, the potted plant at the lower right corner and the white wall stay exactly where they are and never move; she never touches or leans toward '
  'the microphone; the camera is a handheld phone at the height of her collarbones about 80 centimeters from her with only a tiny natural sway, no zoom, no cuts and '
  'no reframing; no glow and no sparkles; no object, person, animal or text appears or disappears; each hand always has exactly five fingers; no on-screen text, no '
  'captions, no logos; real quiet room ambient sound only, no music. SPEECH RULE for every take: she says only the exact words of that take\'s script, each word '
  'exactly once and in order, with no repeated word, no extra word and no added sentence before, between or after; numbers are spoken as words (11:11 and 11/11 as '
  '"eleven eleven", 222 as "two two two", November 11th as "November eleventh"); when she finishes the last word she closes her lips, stays silent and keeps a calm '
  'still expression until the clip ends.')
achou = False
for sec in c['config']:
    for k in sec['campos']:
        if k['campo'].startswith('LIVRE'):
            k['copiar'] = LIVRE; k['valor'] = 'colar o texto abaixo (fechado pela nora46-IMG aprovada)'; achou = True
        if k['campo'] == 'Atmosfera / mood':
            k['valor'] = 'Íntimo e confidencial (o mesmo dos outros longos)'
assert achou
c['conferir'] = ('Conferir em cada take: é a Nora v2 da nora46-IMG (rosto, lua com as estrelinhas, trança, blazer creme e blusa branca); ela fala uma vez só, em inglês, '
                 'com "eleven eleven"; a mão do lado do microfone (esquerdo da imagem) fica na mesa; a do lado direito só faz o gesto do take, na altura do ombro; o microfone não se mexe; '
                 'sem texto, legenda ou música. Renomeie com o nome da lista (T01 a T12).')
c['passos'] = [
  'nora46-IMG APROVADA (31/10 ~03h, a 3ª das 3 variações: janela à esquerda, microfone na borda esquerda, prateleira com a bandeirinha à direita, planta embaixo à direita). Movimentação e texto LIVRE já fechados por ela.',
  'Feito (31/10 ~03h30): as 3 imagens do desejo aprovadas (nora46-DESEJO-1-dinheiro, nora46-DESEJO-2-casal, nora46-DESEJO-3-casa) e o story-3110 escolhido (a 4ª das 4 variações).',
  'Story novo (story-3110) antes das 18h44 de hoje, quando o story-3010 vence: no Insta com o link STORYIG e no Face com o link FACE (seção “Story”). Confira o link na prévia antes de publicar.',
  'Central do curso com a configuração da seção “Central do curso” (o LIVRE é novo) e a fala e a movimentação da seção “A fala e a movimentação”. Confira: 12 takes de 10 s.',
  'Agente do Flow: anexe só a nora46-IMG, cole o aviso e, embaixo, o “COPIAR TUDO JUNTO” da Central, sem editar. 180 créditos (conta grande: 279 → 99). Renomeie os takes com os nomes do painel (T01 a T12, 2 dígitos).',
  'Se o agente gerar menos de 12, abra um projeto novo no Flow e mande só os que faltaram.',
  'Me mande a transcrição dos 12 takes antes de cortar (P33).',
  'Corte de silêncio (seção “Cortar os silêncios”): nora46-T01 a T12 de uma vez, “Juntar tudo” ligado, Corte seco.',
  'CapCut: nora34-PRE (sem espelhar, ~3,5 s) + o corpo cortado + os textos, as imagens do desejo e as avaliações (seção de texto na tela). Música de sempre a −18 dB.',
  'Postar hoje (31/10) por volta das 22h no Insta e no Face, ao vivo, sem localização (é falado). Comentário: no Insta, comente e fixe (sem link); no Face, só comente.']
c['agente'] = copy.deepcopy(P40['central']['agente'])
c['agente']['imagem'] = 'nora46-IMG'
c['agente']['aviso'] = ('Vou te enviar 12 prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um '
                        'com o devido número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.')
c['agente']['passos'] = ['Abra uma conversa nova no agente do Flow.',
  'Nas configurações do agente, ligue a opção de gerar sem pedir aprovação e salve antes de enviar.',
  'Anexe só a nora46-IMG (o blueprint não vai no agente).',
  'Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.',
  'Envie. O agente gera os 12 vídeos; confira cada um e me diga qual falhou (take e problema).',
  'Se ele gerar menos de 12, abra um projeto novo no Flow e mande de novo só os que faltaram.']
c['colagens'] = [{'titulo': 'nora46 (12 takes)', 'fala': ' '.join(t[2] for t in T), 'movimentacao': [t[3] for t in T], 'takes': list(range(12))}]
p['central'] = c

p['story'] = {'prompt_imagem': STORY_PROMPT, 'anexar': 'SÓ o blueprint (a folha da Nora v2). Nenhuma outra imagem.',
  'textos': [{'posicao': 'Uma frase só, uma cor (creme #F1E6D3), em 2 linhas, na parede verde acima da cabeça, logo abaixo da barra do Instagram (entre ~11% e ~19% da altura); pode encostar no alto do cabelo, nunca no rosto. Adesivo na mesa, embaixo das cartas',
              'texto': 'Tap below: pick 3 cards and see what the 11:11 portal brings you.'}],
  'adesivos': ['Pick my 3 cards', 'See my new chapter'],
  'nota': ('IMAGEM ESCOLHIDA: a 4ª das 4 variações (sorriso aberto, mãos junto da carta do meio), renomeada para story-3110; não gere outra. STORY NOVO (31/10): poste antes das 18h44 (quando o story-3010 vence) e antes do nora46, no Insta e no Face. Ao pôr o adesivo de link, '
           'cole o link certo de cada rede e confira na prévia. Insta (STORYIG): ' + LINK_IG + ' · Face (FACE): ' + LINK_FB)}

# ---------------- mapa da tela e edição ----------------
mp = copy.deepcopy(P44['mapa_tela'])
NUM = [{'t': '11:11', 'x': 84, 'y': 12, 'onde': 'alto, à direita, na parede acima da prateleira', 'cor_nome': 'vermelho', 'cor': '#E53935', 'tamanho': 15},
       {'t': '222', 'x': 12, 'y': 27, 'onde': 'à esquerda, na janela, acima do braço do microfone', 'cor_nome': 'roxo', 'cor': '#8E24AA', 'tamanho': 12},
       {'t': '888', 'x': 84, 'y': 44, 'onde': 'à direita, ao lado do ombro, acima dos botões', 'cor_nome': 'verde-esmeralda', 'cor': '#00A86B', 'tamanho': 11}]
mp['numeros'] = NUM
def xy(x, y): return f'X {round(x/100*720-360)} · Y {round(640-y/100*1280)}'
mp['estilos'] = [
  {'nome': 'Números fixos espalhados (11:11, 222, 888)', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'uma cor para cada número (abaixo)',
   'tamanho': 'um tamanho para cada número (abaixo)', 'contorno': 'Traço preto + Sombra preta, sem Plano de fundo. Luz DESLIGADA',
   'obs': '; '.join(f"{u['t']} {u['cor_nome']} {u['cor']}, tamanho {u['tamanho']}, {u['onde']} ({xy(u['x'], u['y'])})" for u in NUM) + '. Cores fortes porque o fundo é claro (o branco e o amarelo não leem na parede e na janela).'},
  {'nome': 'Caixa do topo: “The 11:11 portal is opening.” / “3 signs it chose you”', 'fonte': 'Poppins Bold (poppins-bd)',
   'cor': 'texto preto #000000; “chose you” em vermelho #E53935', 'tamanho': '10, em 2 linhas',
   'contorno': 'Plano de fundo branco arredondado, sem traço. Luz DESLIGADA', 'obs': 'Centralizada no topo (X 0 · Y 397), do primeiro quadro do hook até o fim do Take 1.'},
  {'nome': 'Os 3 sinais (no mesmo lugar da caixa do topo)', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto #000000; os números 1, 2 e 3 em vermelho #E53935',
   'tamanho': '9, uma linha por sinal', 'contorno': 'Plano de fundo branco arredondado, sem traço. Luz DESLIGADA',
   'obs': 'X 0 · Y 397. Entram um por take e ficam: “1. 11:11 everywhere” no Take 5, “2. The wrong people fade out” no Take 6, “3. Something good is coming” no Take 7. Saem no fim do Take 7.'},
  {'nome': 'Legenda automática (Claude das legendas)', 'fonte': 'Poppins Bold', 'cor': 'branco, em MAIÚSCULAS; palavra-chave em amarelo-ouro #FFD21F',
   'tamanho': 'uns 38 px de fonte (vídeo 720×1280)', 'contorno': 'preto grosso, sem caixa e sem brilho',
   'obs': 'Blocos de 2 a 4 palavras, no máximo 2 linhas. Destaques: portal, 11:11, sign, money, peace, cards, love e 222. Sem legenda no hook e no Take 9 (lá entram as avaliações).'},
  {'nome': 'Avaliações reais (Take 9)', 'fonte': 'as imagens provas-trustpilot/01-leukia.png, 02-patricia.png e 03-darcey.png (prontas)', 'cor': '—',
   'tamanho': 'escala ~85% (largura de ~630 px)', 'contorno': 'sem borda; sombra leve se quiser',
   'obs': 'Uma depois da outra, ~2 s cada, centradas em X 0 · Y -200, do começo ao fim do Take 9. No lugar da caixa do topo, no mesmo Take 9: “Rated 4.7 ⭐ by 2,000+ people” (caixa branca, X 0 · Y 397). Confira o número no Trustpilot no dia.'},
  {'nome': 'Faixa do story no topo: “Pick your 3 cards in my story ⭐”', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto #000000, “my story” em vermelho #E53935',
   'tamanho': '9, em 1 linha', 'contorno': 'Plano de fundo branco arredondado, sem traço. Luz DESLIGADA',
   'obs': 'Do Take 10 até o fim, X 0 · Y 397. Diz o que tem lá (sai o “The second part is in my Stories”).'},
  {'nome': 'Seta vermelha', 'fonte': 'no CapCut: Texto → Adicionar texto → digite ↓', 'cor': 'vermelho #E53935', 'tamanho': '14', 'contorno': 'Traço preto. Luz DESLIGADA',
   'obs': 'Do Take 10 até o fim. Embaixo à esquerda, apontando para baixo, para a foto do perfil (X -317 · Y -333).'}]
mp['seta'] = {'x': 6, 'y': 76, 'onde': 'embaixo à esquerda, apontando para baixo, para a foto do perfil'}
mp['regras'] = [
  'Conferido na nora46-IMG: a faixa da legenda (Y -294, 73%) fica nos antebraços, logo acima da borda da mesa, abaixo do microfone e do rosto; as avaliações (X 0 · Y -200) ficam em cima do blazer, sem cobrir o rosto.',
  'Nada nas faixas vermelhas, em cima do rosto, das mãos ou do microfone. Os números ficam na parede, na janela e ao lado do ombro: se algum cobrir a cabeça do microfone ou a bandeirinha, mova uns 40 no X.',
  'Imagens do desejo (Take 8) e avaliações (Take 9) entram como sobreposição por cima do vídeo: nada pausa, a voz dela continua e a duração do vídeo não muda. Cada imagem entra na palavra que combina com ela (dinheiro, casal, casa; Leukia, Patricia, Darcey).',
  'Avaliações (Take 9): só os prints reais das pastas do projeto, sem mudar o texto; o nome do app não aparece.']
p['mapa_tela'] = mp
p['edicao_linha'] = [
  {'quando': '0. Antes do Take 1', 'texto': 'Hook (nora34-PRE, sem espelhar, uns 3,5 s)', 'como': 'Corte seco para o corpo cortado. Sem legenda no hook (sem fala).'},
  {'quando': '1. Do primeiro quadro do hook até o fim do Take 1', 'texto': 'The 11:11 portal is opening.\n3 signs it chose you',
   'como': 'Caixa branca arredondada no topo (X 0 · Y 397), texto preto, “chose you” em vermelho.'},
  {'quando': '2. O vídeo todo', 'texto': '11:11 · 222 · 888', 'como': 'Espalhados, cada um de uma cor e de um tamanho (estilos abaixo).'},
  {'quando': '3. Do Take 1 ao fim (menos o Take 9)', 'texto': 'Legenda automática, em blocos de 2 a 4 palavras', 'como': 'Faixa verde do mapa. Destaques em amarelo-ouro: portal, 11:11, sign, money, peace, cards, love e 222.'},
  {'quando': '4. Takes 5, 6 e 7', 'texto': '1. 11:11 everywhere\n2. The wrong people fade out\n3. Something good is coming',
   'como': 'No lugar da caixa do topo (X 0 · Y 397). Cada sinal entra no seu take e fica até o fim do Take 7. Começa em “Sign one”.'},
  {'quando': '5. Take 8 (a voz dela continua por baixo; nada pausa)', 'texto': '3 imagens do desejo por cima do vídeo, tela cheia', 'como': 'Sobreposição no CapCut (X 0 · Y 0, aumentada até cobrir a tela). Ela aparece falando “If that’s you, imagine a few months from now”; depois: nora46-DESEJO-1-dinheiro em “money stops being a worry”, nora46-DESEJO-2-casal em “someone stays”, nora46-DESEJO-3-casa em “and home feels like peace” (~1,5 a 2 s cada, corte seco). No take 9 ela volta na tela. JEITO SIMPLES: arraste as 3 imagens para a faixa de cima da linha do tempo, uma atrás da outra, ~2 s cada, a partir de “money”; não precisa acertar a palavra exata. Na da casa, o “WELCOME” do capacho fica embaixo da interface do app; se incomodar, zoom de 110% subindo a imagem.'},
  {'quando': '6. Take 9 (a voz continua; o rosto dela fica visível em cima)', 'texto': 'Rated 4.7 ⭐ by 2,000+ people', 'como': 'Caixa branca no topo (X 0 · Y 397) + as avaliações por cima do vídeo, na metade de baixo (sobreposição em X 0 · Y -200, escala ~85%): 01-leukia em “Over two thousand people have already rated this reading”, 02-patricia em “Here’s what some of them wrote”, 03-darcey em “after picking their cards” (~2 s cada). Tire a legenda automática deste take. JEITO SIMPLES: as 3 em fila, ~2 s cada, do começo do take 9.'},
  {'quando': '7. Do Take 10 até o fim', 'texto': 'Pick your 3 cards in my story ⭐', 'como': 'Faixa no topo (X 0 · Y 397), texto preto, “my story” em vermelho. Começa em “If you noticed”.'},
  {'quando': '8. Do Take 10 até o fim', 'texto': 'Seta vermelha (↓)', 'como': 'Embaixo à esquerda (X -317 · Y -333), para a foto do perfil.'},
  {'quando': '9. O vídeo todo', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Volume baixo, por baixo da voz.'}]

L = [{'nome': 'nora34-PRE', 'de': 'nora34-PRE', 'tipo': 'hook (do nora34)', 'status': 'reutilizar', 'creditos': 7, 'descricao': 'A pedra escura que racha, sem espelhar.'},
     {'nome': 'nora46-IMG', 'tipo': 'imagem 1', 'status': 'gerar', 'descricao': 'Do blueprint: a Nora de blazer creme num estúdio claro, com microfone de podcast (visual de especialista, aula do Iorhan).',
      'base': 'Decisão 3 da aula (visual mais profissional); formato "podcast com mulher de autoridade" do briefing do funil.', 'serve': 'Todos os vídeos do corpo B (é a imagem dos 12 takes).'},
     {'nome': 'nora46-DESEJO-1-dinheiro', 'tipo': 'imagem do desejo', 'status': 'gerar', 'descricao': 'Mãos com notas de dólar na mesa da cozinha, sem rosto.', 'base': 'Prova visual do desejo (aula do Iorhan).', 'serve': 'Todos os vídeos do corpo B.'},
     {'nome': 'nora46-DESEJO-2-casal', 'tipo': 'imagem do desejo', 'status': 'gerar', 'descricao': 'Casal rindo na cozinha, rostos meio virados.', 'base': 'Prova visual do desejo (aula do Iorhan).', 'serve': 'Todos os vídeos do corpo B.'},
     {'nome': 'nora46-DESEJO-3-casa', 'tipo': 'imagem do desejo', 'status': 'gerar', 'descricao': 'Mão com as chaves na porta de uma casa ao entardecer.', 'base': 'Prova visual do desejo (aula do Iorhan).', 'serve': 'Todos os vídeos do corpo B.'}]
for (a, cena, f, m) in T:
    L.append({'nome': a, 'tipo': 'take', 'status': 'gerar', 'creditos': 15, 'descricao': f'{cena}: “{f}”',
              'serve': 'Todos os vídeos do corpo B até 11/11.' + (' Serve também depois do dia 11 (não fala do portal).' if a[7:10] in ('T02', 'T05', 'T06', 'T07', 'T08', 'T09', 'T11') else '')})
L += [{'nome': 'provas-trustpilot/01-leukia.png, 02-patricia.png, 03-darcey.png', 'de': 'pasta provas-trustpilot do projeto', 'tipo': 'prova real', 'status': 'reutilizar',
       'descricao': 'Avaliações reais (5 estrelas), sem o nome do app.'},
      {'nome': 'story-3110', 'tipo': 'imagem do story', 'status': 'gerar', 'descricao': 'Do blueprint: a Nora de blazer creme à mesa, 3 cartas viradas para baixo, parede verde-esmeralda.', 'serve': 'O story de 31/10.'}]
p['pecas'] = {'lista': L, 'decisao': [
  'Corpo B pela aula do Iorhan (P42): qualificação, autoridade pelo conhecimento, o portal como mecanismo, 3 sinais, imagine, prova real, CTA com motivo; seguir e 222 só no fim. Placar: 9 verdes, 2 dourados, 1 amarelo, 0 vermelhos.',
  'Hook pronto da pedra escura (0): o que mais segurou num longo. A imagem dos takes é nova, de especialista (blazer creme, estúdio claro, microfone).',
  'Prova real: 3 avaliações do Trustpilot, em tela no Take 9 (autorização do aluno, 31/10). Nada inventado.',
  'O corpo é gerado uma vez (180) e serve até 11/11 trocando só o hook (0 crédito). Os takes 2, 5 a 9 e 11 servem também depois do dia 11.'],
  'proximos_intro': 'Variações mantendo a ideia, sem refazer o vídeo todo: Take 1 com signos (15) e a versão de amor ou de dinheiro (só os takes 5 a 8, 60), se o nora46 levar gente ao story.',
  'proximos': [
    {'nome': 'noraNN-T01-gancho-portal-touro-virgem-capricornio', 'modelo': 'Take 1 com signos (qualificação por signo)', 'custo': '15',
     'gancho': "Taurus, Virgo or Capricorn: the 11:11 portal is about to open, and if this reached you today, it's not a coincidence.", 'texto': 'Taurus, Virgo, Capricorn: the 11:11 portal is opening'},
    {'nome': 'noraNN-T05-sinal-1-amor', 'modelo': 'versão de amor (takes 5 a 8 novos)', 'custo': '60 (4 takes)',
     'gancho': 'Sign one: you keep dreaming about a love that feels calm, and for the first time, you believe you deserve it.', 'texto': '3 signs love is on its way'}]}
# Ordem do painel = ordem de produção (pedido do aluno, 31/10): imagens → Central → agente → corte → CapCut (hook + corpo) → textos e sobreposições → story → postar.
p['ordem'] = ['pecas', 'referencia', 'imagens', 'todos', 'central', 'cenas', 'agente', 'silencio', 'prehook', 'textotela', 'story', 'descricao', 'comentario', 'respostasface', 'fala']
gravar(46, p)
print('ok: PAINEL-NORA46 (corpo B)'); [print(t[0], wc(t[2])) for t in T]
