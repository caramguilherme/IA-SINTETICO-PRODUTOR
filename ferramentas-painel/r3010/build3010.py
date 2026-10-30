# 30/10/2026: painéis do nora45 (fita na boca, Touro/Virgem/Capricórnio, edição da nora41-IMG) e do nora46
# (longo: geodo espelhado + Take 1 novo de Câncer/Escorpião/Peixes + takes 2 a 12 do nora40).
# Base: os pacotes do PAINEL-NORA41.html e do PAINEL-NORA43.html. Uso: python3 build3010.py <pasta do repositório>
import re, json, copy, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

def ler(n):
    s = open(f'{BASE}/PAINEL-NORA{n}.html', encoding='utf-8').read()
    return json.loads(re.search(r'const PACOTE = (\{.*?\});\n', s, re.S).group(1))

def gravar(n, p):
    m = open(f'{BASE}/PAINEL-MODELO.html', encoding='utf-8').read()
    assert m.count('const PACOTE = null;') == 1
    m = m.replace('<title>Painel de Produção</title>', f'<title>Painel nora{n}</title>')
    m = m.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    open(f'{BASE}/PAINEL-NORA{n}.html', 'w', encoding='utf-8').write(m)

def troca(o, pares):
    if isinstance(o, dict): return {k: troca(v, pares) for k, v in o.items()}
    if isinstance(o, list): return [troca(v, pares) for v in o]
    if isinstance(o, str):
        for a, b in pares: o = o.replace(a, b)
    return o

def xy(x, y): return round(x / 100 * 720 - 360), round(640 - y / 100 * 1280)
def num_txt(ns): return '; '.join(f"{u['t']} {u['cor_nome']} {u['cor']}, tamanho {u['tamanho']}, {u['onde']} (X {xy(u['x'], u['y'])[0]} · Y {xy(u['x'], u['y'])[1]})" for u in ns) + '.'

STORYIG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
FACE = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'

LEITURA = ('30/10/2026 (conta nova do Claude): li inteiros, com a ferramenta de leitura, nesta sessão: FATOS-DO-ALUNO.md, CLAUDE.md, '
  'LICOES-FLOW-E-PROMPTS.md (checklist e todas as lições), COMUNIDADE-E-ESTRATEGIA.md (inteiro, até o Discord de 29/10 e as DMs de 30/10), '
  'VALIDACAO-CONTA-E-AVATAR.md, BRIEFING-MANIFESTACAO.md, DNA Visual - Nora v2.md, BIBLIOTECA-PRE-GANCHOS.md, BIBLIOTECA-VIDEOS-VIRAIS.md (inteiro), '
  'BIBLIOTECA-DE-TAKES.md, 00-LEIA-PRIMEIRO.md, REGISTRO-DE-PERSONAS.md, PAINEL-MODELO.html, ROTEIRO-NORA40 a ROTEIRO-NORA43, as métricas de 28 a 30/10 '
  '(CSV e diário) e os pacotes dos painéis do nora40 ao nora43. AINDA NÃO LI HOJE (o story venceu às 16h30 e o aluno precisava postar): '
  'os arquivos de método de fala e copy (hooks, formatos, exemplos, CTAs, comunicação visceral, bodies, cold reading, copy, pesquisa de público), '
  'Prompts.txt, CHECKLIST-DE-PRODUCAO.md, PAPEL-AGENTE-FLOW.md, GUIA-CREATIVE-HUB.md, PROJETO-Dana.md, BRIEFING-LOVECHART.md, os DNA da Dana e da Nora v1, '
  'os EXEMPLO-*, os PLANO-CREDITOS-*, os PASSO-A-PASSO-*, os STORY-*, os TAKE-NOVO-* e os roteiros R001 a nora39. ')

AGENDA = ('Plano de 30/10 (refeito às 16h55, o dia atrasou): story-2810 repostado às ~17h; ~17h30 nora44 = pedra escura + corpo do nora40 '
          '(Áries/Leão/Sagitário, 0 crédito); ~20h nora45 = a fita de Touro/Virgem/Capricórnio (12) + o story novo; ~22h30 nora46 = geodo espelhado + '
          'Take 1 novo de Câncer/Escorpião/Peixes (15); ~01h nora47 = hook do esconderijo (nora27-PRE) + corpo do nora42 (Gêmeos/Libra/Aquário, 0). '
          'Face: os mesmos, ao vivo, e a nora40-VAR.')

# ======================= nora45: a fita, Touro/Virgem/Capricórnio =======================
p = troca(ler('41'), [
    ('CANCER, SCORPIO, PISCES', 'TAURUS, VIRGO, CAPRICORN'),
    ('C-A-N-C-E-R, S-C-O-R-P-I-O, P-I-S-C-E-S', 'T-A-U-R-U-S, V-I-R-G-O, C-A-P-R-I-C-O-R-N'),
    ('29, 30 AND 31 OF OCTOBER', '30 AND 31 OF OCTOBER'),
    ('Cancer, Scorpio, Pisces', 'Taurus, Virgo, Capricorn'),
    ('Câncer, Escorpião e Peixes', 'Touro, Virgem e Capricórnio'),
    ('cancer-escorpiao-peixes', 'touro-virgem-capricornio'), ('CANCER-ESCORPIAO-PEIXES', 'TOURO-VIRGEM-CAPRICORNIO'),
    ('wine-red', 'ivory-cream'), ('blusa vinho', 'blusa creme'),
    ('nora41', 'nora45'),
])
TOPO = 'Keep your mouth shut. November will be the luckiest month of your life. Send it to yourself.'
r = p['roteiro']
r['id'] = 'nora45-TEXTO-NA-TELA-FITA-PORTA-RETRATO-TOURO-VIRGEM-CAPRICORNIO'
r['titulo'] = 'Texto na tela (Manifestation): a fita na boca e o porta-retrato dos signos, Touro, Virgem e Capricórnio (a cena do nora41, blusa creme, frase nova)'
r['formato'] = 'Texto na tela, sem fala (clipe de 8 s): a mesma cena do nora41 por edição da imagem (signos, datas e cor da blusa novos); ela rasga a fita e cola na boca'
r['molde_hook'] = 'a fita do nora41 (2.909 views, 7 envios, ~337 pessoas dos EUA no Insta) lateralizada: mesma cena, outra cor de roupa e frase do topo nova (Antoine Martel: "the luckiest month of your entire life")'
r['descricao_instagram'] = ('Taurus, Virgo, Capricorn: keep your mouth shut. November is your luckiest month. 🤫\n'
                            'Send this to yourself. Open my story before it disappears. Comment 222 and follow me.\n'
                            '#manifestation #astrology #zodiac #usa #usareels')
r['leitura_registro'] = LEITURA + 'Este vídeo não tem fala: os arquivos de fala e copy não mudam nada nele.'
p['refs'] = ['A nora41-IMG (a imagem do nora41, já aprovada), só ela, na IMAGEM 1']
p['trava_referencia'] = ('There is no pet in this project: no animal appears in any scene. The ATTACHED image is one approved photo of this exact woman at her desk; '
  'it is the only identity reference. Keep her the exact same living person: the same face, face shape, hazel-green eyes, eyebrows, nose, lips, '
  'skin tone, very long wavy jet-black hair, the thin braid with tiny gold rings, exactly ONE gold crescent-moon gem with three tiny gold stars on her '
  'cheek on the left side of the image, the gold star-and-moon earrings and the gold Venus-symbol necklace. Do not redesign, beautify, de-age, age, '
  'recolor, lighten or darken her face, hair, eyes or skin.')
p['figurino'] = ('fortune-teller, subtle mystic; a soft ivory-cream fine-knit long-sleeve top with a round crew neckline, smooth and matte, no print, '
  'embroidery, logo or shine. Clothing is secondary to the emerald tape and the red handwriting on the white card. Fixed accessories, always visible: '
  'the long gold star-and-moon drop earrings, the long thin gold chain with the small gold Venus-symbol pendant, thin gold bracelets on her left wrist, '
  'a small gold sun-symbol ring on her right index finger and the gold face gems; no other jewelry, turban, cape or costume')
p['imagens'][0]['cena'] = ('EDIT of the attached image (the woman at the small walnut desk at night, holding a roll of emerald washi tape with a strip pulled out, '
  'a gold picture frame with a handwritten white card standing on the desk in front of her). Keep EVERYTHING exactly as it is: the same woman and face, '
  'the same pose, the same position of her head, eyes, lips and both hands, the same roll of emerald-green washi tape with tiny gold stars and crescent moons '
  'in her LEFT hand (the hand on the RIGHT side of the image) and the same flat strip, about 10 cm long, pinched by her RIGHT hand (the hand on the LEFT side '
  'of the image), the same gold picture frame in the same position, size and angle, the same desk, the same white mug with the small American flag, '
  'the same fairy lights, lamp, navy wall and warm light, and the same framing and camera. Change ONLY these two things: '
  '(1) the two handwritten lines on the white card inside the gold picture frame now read, in the same thick felt-tip handwriting, the same neat bold '
  'capital letters, the same sizes and the same centered positions: the first line, large, in bright red marker: TAURUS, VIRGO, CAPRICORN; the second line, '
  'smaller, in black marker: 30 AND 31 OF OCTOBER. Spell every word exactly like that, letter by letter (T-A-U-R-U-S, V-I-R-G-O, C-A-P-R-I-C-O-R-N). '
  'No other words, numbers, drawings, stickers, tags or logos on the card or the frame. (2) Her top is now a soft ivory-cream fine-knit long-sleeve top with '
  'the same round crew neckline and the same relaxed fit, smooth and matte, with no print, embroidery, logo or shine; nothing else about her changes. '
  'Each hand keeps exactly five fingers. No date stamp, no watermark, no caption, no logo. Do not rejuvenate or smooth her face.')
p['imagens'][0]['anexar'] = 'SÓ a nora41-IMG (a imagem do nora41, já aprovada: é uma edição dela). Não anexe o blueprint nem outra imagem.'
v = p['videos'][0]; v['fala'] = '(sem fala) texto na tela: ' + TOPO
p['texto_tela']['hook'] = TOPO
p['comentario_fixado'] = {
  'insta': "Taurus, Virgo, Capricorn, this one is yours. 🤫 Don't tell anyone: send it to yourself to claim it. PART 2 of this sign is in my story: pick 3 cards and see what November brings you. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222 and follow me so you don't miss your sign's next message.",
  'face': "Taurus, Virgo, Capricorn, this one is yours. 🤫 Don't tell anyone: send it to yourself to claim it. PART 2 of this sign is in my Story: pick 3 cards and see what November brings you. Tap my profile picture NOW, it's gone in 24 hours. Comment 222 and follow me so you don't miss your sign's next message."}
g = p['pre_gancho']
g['conceito'] = ('A fita do nora41 (o vídeo de 8 s que mais trouxe gente dos EUA e mais envios), na mesma cena, com outros signos, a blusa creme e uma frase nova no topo. '
                 'Ela rasga a fita verde-esmeralda com estrelinhas e luas douradas e cola na boca; os signos e as datas estão no porta-retrato da mesa.')
g['modo'] = ('Gere depois das duas imagens aprovadas (a nora45-IMG, na seção “Imagens”, e a nora45-FIM, item 1 abaixo) e do meu ok. Um vídeo só, em FRAMES: '
             'primeiro quadro = nora45-IMG, último quadro = nora45-FIM. 8 s, 9:16, áudio ligado. 12 créditos (conta de 53: 53 → 41). '
             'Se o Flow recusar por política, não repita o texto: me mande o print.')
c = p['central']
c['passos'] = [
  'Vídeo de 8 s SEM fala. Não usa a Central do curso nem o agente. Tudo na conta de 53 (a mesma em que você gerou o nora41).',
  'IMAGEM (seção “Imagens”): no Flow, anexe SÓ a nora41-IMG e cole o prompt (botão “Copiar imagem com trava”). Aprove só se: é a Nora (lua e 3 estrelinhas na bochecha do lado esquerdo da imagem); a blusa ficou creme; o cartão diz exatamente TAURUS, VIRGO, CAPRICORN (vermelho) e 30 AND 31 OF OCTOBER (preto), sem outra palavra; a fita e as mãos estão iguais às do nora41, cinco dedos; sem carimbo de data. Se a grafia sair errada, gere de novo (imagem não gasta crédito). Renomeie para nora45-IMG.',
  'IMAGEM FINAL (seção “Clipe”, item 1): anexe SÓ a nora45-IMG aprovada e cole o prompt. Aprove só se: a fita está colada na boca de canto a canto, sem cobrir o nariz nem a lua da bochecha; uma tira só; as mãos estão na mesa, dos dois lados do porta-retrato; o cartão continua com a mesma escrita. Renomeie para nora45-FIM e me mande as duas imagens.',
  'Depois do meu ok: o clipe (seção “Clipe”, item 2) em FRAMES, primeiro quadro = nora45-IMG, último quadro = nora45-FIM, 8 s, 9:16, áudio ligado. Renomeie para nora45-CLIPE-fita. 12 créditos (conta de 53: 53 → 41). Se o Flow recusar por política, não repita: me mande o print.',
  'CapCut: números fixos, texto do topo, texto do story com a seta (dos 5 aos 8 s), som do clipe ligado e a música de sempre (“Ambient Mystical Drone”, da biblioteca do CapCut) a −12 dB. Sem legenda na tela e sem corte de silêncio: a Nora não fala.',
  'Postar em 30/10 por volta das 20h no Insta e no Face, ao vivo. No Insta, ponha a localização Los Angeles, California. Antes de postar, poste o STORY NOVO (seção Story). Comentário: no Insta, comente e fixe (sem link); no Face, só comente (não fixa mais).']
c['conferir'] = 'Conferir: é a Nora da nora45-IMG; ela não fala nem mexe a boca; uma tira só, que fica colada até o fim, sem cobrir o nariz nem a lua da bochecha; a escrita do cartão não muda; o porta-retrato não se mexe; as luzinhas não piscam.'
# story NOVO (30/10)
st = p['story']
pref = st['prompt_imagem'].split('FIXED OUTFIT:')[0]
st['prompt_imagem'] = pref + ('FIXED OUTFIT: fortune-teller, subtle mystic; a soft ivory-cream fine-knit long-sleeve top with a round crew neckline, no print, embroidery or shine. '
  'Clothing is secondary to the contrast of the three cards on the dark throw. Fixed accessories, always visible: the long gold star-and-moon drop earrings, '
  'the long thin gold chain with the small gold Venus-symbol pendant, thin gold bracelets on her left wrist, the gold sun ring and the gold face gems from the '
  'reference sheet; no other jewelry, turban, cape or costume\n\n'
  'UGC STYLE LOCK: vertical 9:16 image, photorealistic, shot in an American home with the spontaneous look of a smartphone. Natural light, real skin, fabric and '
  'hair textures, casual and slightly imperfect framing. The camera stays out of frame. No text, caption, logo, watermark or advertising look.\n\n'
  'SCENE: generate a NEW photo from the attached character sheet only (do not edit any other image). A vertical 9:16 photo taken at night in a cozy American '
  'bedroom, as if a friend took it with a phone. She sits cross-legged on a made bed covered with a deep emerald-green velvet throw, facing the camera, shoulders '
  'square, leaning slightly forward, and she looks straight into the lens with a soft, warm, knowing smile, lips gently closed. CAMERA: a phone at the height of '
  'her eyes, about 90 cm in front of her, straight on, with no tilt. FRAMING, in percent of the image height from the top: from 0 to 24 percent only the plain '
  'deep navy-blue bedroom wall behind her shows, with nothing on it (this band stays empty for text); the top of her head is at about 25 percent, her eyes at '
  'about 35 percent, her chin at about 45 percent; her hands and the three cards on the velvet throw in front of her are between about 60 and 76 percent; from '
  '78 to 100 percent only plain, empty emerald velvet throw shows (this band stays empty for a sticker). THE THREE CARDS: exactly three tall, narrow tarot cards, '
  'each about 7 cm wide and 12 cm tall, lie flat on the velvet throw in front of her crossed legs, face down, in one neat straight row side by side about 2 cm '
  'apart, centered left to right, the row about half of the image width, the long side of each card pointing toward the camera. All three backs are identical: '
  'deep navy blue with a fine ornate gold border and one small gold eight-pointed star in the center. No card face is visible; there are no letters, numbers, '
  'words or logos on the cards; there are no other cards and no deck anywhere. HANDS: her RIGHT hand (the hand on the LEFT side of the image) is held just above '
  'the middle card, the tip of her index finger about 1 cm above it, as if she is about to pick it; her LEFT hand (the hand on the RIGHT side of the image) rests '
  'relaxed on her knee on the right side of the image, with the thin gold bracelets visible; each hand has exactly five fingers, and neither hand covers a card or '
  'her face. LIGHT: one small bedside lamp with a cream fabric shade at the far right edge of the image, at the height of her shoulder, softly lights her face from '
  'the right side of the image; one strand of tiny warm-white fairy lights hangs low on the wall behind her at the height of her shoulders, glowing as small soft '
  'round out-of-focus dots on both sides of her, never above her head and never in the top band; the rest of the room falls into soft warm shadow, and the top '
  'band of wall stays dark enough for light text to read on it. BACKGROUND: on the bedside table at the right edge of the image, out of focus, a white mug holds '
  'a small American flag on a stick. DO NOT INCLUDE: candles, crystals, smoke, flowers, a crystal ball, a phone, other people, pets, mirrors, windows, picture '
  'frames, posters, text, captions, watermarks, logos or a date stamp. The three cards stay face down and flat. Do not rejuvenate or smooth the skin.')
st['textos'] = [{'posicao': 'Uma frase só, no topo (na faixa da parede escura), uma cor (creme #F1E6D3), 1 a 2 linhas',
                 'texto': 'Tap below: pick 3 cards and see what November brings you.'}]
st['adesivos'] = ['Pick my 3 cards', 'See my November']
st['nota'] = ('STORY NOVO (30/10, nome story-3010): poste ANTES do nora45, no Insta e no Face, além do story-2810 que você repostou às ~17h. '
              'A imagem é nova (não gasta crédito) e o texto também: quem já segue viu o story das 3 cartas duas vezes e não clicou de novo (8 → 3 → 2 cliques). '
              'Ao pôr o adesivo de link, cole o link certo de cada rede e confira na prévia antes de publicar. '
              f'Insta (STORYIG): {STORYIG} · Face (FACE): {FACE}')
st.pop('ja_postado', None)
# edição e mapa
NUM45 = [
  {'t': '11:11', 'x': 87, 'y': 12, 'onde': 'alto à direita, na parede', 'cor_nome': 'ciano', 'cor': '#3DE0FF', 'tamanho': 15},
  {'t': '888', 'x': 10, 'y': 30, 'onde': 'à esquerda, na parede, na altura dos olhos', 'cor_nome': 'amarelo-ouro', 'cor': '#FFD21F', 'tamanho': 12},
  {'t': '222', 'x': 6, 'y': 47, 'onde': 'na borda esquerda, na altura das mãos, longe delas', 'cor_nome': 'branco', 'cor': '#FFFFFF', 'tamanho': 11}]
p['mapa_tela']['numeros'] = NUM45
el = p['edicao_linha']
el[0]['texto'] = TOPO
el[0]['como'] = 'Texto no topo, em 3 linhas, do segundo 0 ao fim do clipe. “Keep your mouth shut.” em branco; “November will be the luckiest month of your life.” em amarelo-ouro; “Send it to yourself.” em branco.'
el[1]['texto'] = '11:11  ·  888  ·  222  (espalhados)'
el[1]['como'] = 'Cada número de uma cor e de um tamanho, num lugar, parados do primeiro ao último quadro: ' + num_txt(NUM45)
for e in p['mapa_tela']['estilos']:
    if e['nome'].startswith('Números'):
        e['nome'] = 'Números fixos espalhados (11:11, 888, 222)'; e['obs'] = num_txt(NUM45)
    if e['nome'].startswith('Texto do topo'):
        e['cor'] = 'branco #FFFFFF; “November will be the luckiest month of your life.” em amarelo-ouro #FFD21F'
p['mapa_tela']['regras'][0] = ('A cena é a mesma do nora41 (edição da imagem), então os lugares dos números saem dos que já foram conferidos lá, trocados de lado e de cor. '
  'Confira na nora45-IMG e na nora45-FIM: se algum número cobrir o rosto, as mãos, a fita ou o porta-retrato, me mande a imagem.')
p['pecas'] = {'lista': [
  {'nome': 'nora45-IMG', 'tipo': 'imagem 1 (primeiro quadro)', 'status': 'gerar', 'creditos': 0,
   'descricao': 'Edição da nora41-IMG: cartão TAURUS, VIRGO, CAPRICORN / 30 AND 31 OF OCTOBER e blusa creme. Imagem não gasta crédito.',
   'base': 'A fita do nora41 (o melhor vídeo de 8 s em envios e em pessoas dos EUA), lateralizada: mesma cena, outra roupa, outros signos.',
   'serve': 'Hook de 4 s para um longo de Touro, Virgem e Capricórnio (os primeiros ~4,5 s do clipe).'},
  {'nome': 'nora45-FIM', 'tipo': 'imagem final (último quadro)', 'status': 'gerar', 'creditos': 0,
   'descricao': 'Edição da nora45-IMG: a fita colada na boca, as mãos na mesa.', 'base': 'O último quadro manda no Flow (lição do item 16).', 'serve': 'Só deste vídeo.'},
  {'nome': 'nora45-CLIPE-fita', 'tipo': 'clipe sem fala', 'status': 'gerar', 'creditos': 12,
   'descricao': '8 s: ela puxa a fita, rasga, cola na boca, apoia as mãos na mesa, olha o cartão e volta para a lente (o mesmo prompt do nora41).',
   'base': 'O clipe do nora41 deu certo de primeira (29/10).', 'serve': 'Face: versão com filtro e 1,1x (não espelhar: a escrita do cartão inverte).'},
  {'nome': 'story-3010', 'tipo': 'imagem do story', 'status': 'gerar', 'creditos': 0,
   'descricao': 'Do blueprint: a Nora sentada na cama à noite, blusa creme, 3 cartas viradas para baixo na manta esmeralda, o dedo sobre a do meio.',
   'base': 'Story novo: o story-2810 caiu de 23,5% para 8,7% de clique e mais da metade de quem vê já segue.', 'serve': 'Story de 30/10 e 31/10.'}],
  'decisao': [
    'Fita de novo, porque o nora41 foi o vídeo de 8 s com mais envios (7), mais salvos (6) e mais gente dos EUA (~337) da Nora.',
    'Lateralizar em vez de repetir igual (a placa repetida pela 3ª vez perdeu EUA): a mesma cena por edição da nora41-IMG, outra cor de blusa (creme), outros signos e frase nova no topo.',
    'Frase do topo modelada do Antoine Martel (70 mil curtidas): “the luckiest month of your entire life”, com o mês que vem (novembro) e o pedido de envio, que funcionou no nora41.',
    'Datas: 30 e 31 de outubro (o vídeo sai na noite de 30/10 e roda até 31/10).',
    'Story novo junto com este vídeo: texto novo (“see what November brings you”) e imagem nova, para quem já segue ter motivo de tocar de novo.',
    AGENDA]}
gravar('45', p)

# ======================= nora46: geodo espelhado + Take 1 novo de Câncer/Escorpião/Peixes =======================
T1 = 'Cancer, Scorpio or Pisces: keep your mouth shut if this video showed up for you on October 30th, 31st or November 1st.'
q = troca(ler('43'), [
    ('Taurus, Virgo or Capricorn: keep your mouth shut if this video showed up for you on October 29th, 30th or 31st.', T1),
    ('Taurus, Virgo or Capricorn', 'Cancer, Scorpio or Pisces'), ('Taurus, Virgo, Capricorn', 'Cancer, Scorpio, Pisces'),
    ('Touro, Virgem e Capricórnio', 'Câncer, Escorpião e Peixes'), ('Touro/Virgem/Capricórnio', 'Câncer/Escorpião/Peixes'),
    ('touro-virgem-capricornio', 'cancer-escorpiao-peixes'), ('TOURO-VIRGEM-CAPRICORNIO', 'CANCER-ESCORPIAO-PEIXES'),
    ('October 29th, 30th or 31st', 'October 30th, 31st or November 1st'),
    ('nora43', 'nora46')])
r = q['roteiro']
r['id'] = 'nora46-LONGO-HOOK-GEODO-ESPELHADO-CANCER-ESCORPIAO-PEIXES'
r['titulo'] = 'Longo do corpo A (Manifestation), hook do geodo espelhado: Câncer, Escorpião e Peixes (só o Take 1 novo)'
r['formato'] = 'Hook do geodo que racha, espelhado (nora37-PRE, 4 s) + Take 1 novo + takes 2 a 12 do nora40 (~100 s)'
r['molde_hook'] = 'geodo que racha espelhado (viral x2: o mesmo clipe do x1, espelhado) + corpo A (x1 a x5)'
r['leitura_registro'] = LEITURA + 'Este painel só gera o Take 1, no molde dos Takes 1 do nora40, do nora42 e do nora43 (mesma configuração da Central, mesma linha de movimentação); o corpo é o do nora40.'
q['videos'][0]['fala'] = T1
q['central']['colagens'][0]['fala'] = T1
q['central']['passos'] = [
  'Take 1, na conta grande (249 → 234). Imagem: não gere. Use a nora37-IMG.',
  'Central do curso: a MESMA configuração do nora37 e do nora40 (seção “Central do curso”, com o texto LIVRE). Cole só a fala do Take 1 e a linha de movimentação dele. Clique em GERAR PROMPT DE ANIMAÇÃO e confira: 1 take de 10 s.',
  'Agente do Flow: anexe a nora37-IMG (só ela), cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take). 15 créditos. Renomeie para nora46-T01-gancho-cancer-escorpiao-peixes.',
  'Os takes 2 a 12 NÃO são gerados: são os do nora40 (lista em “Nomes e reaproveitamento”). Faça uma cópia de cada um e renomeie de nora40-T02… para nora46-T02… (2 dígitos, para a ferramenta de corte juntar na ordem).',
  'Me mande a transcrição do Take 1 e a emenda com o Take 2 antes de postar.',
  'Corte de silêncio (seção “Cortar os silêncios”): suba nora46-T01 a nora46-T12 de uma vez, com “Juntar tudo” ligado e Corte seco. CapCut: o hook espelhado, o corpo cortado e os textos da seção de texto na tela.',
  'Postar em 30/10 por volta das 22h30 no Insta e no Face, ao vivo, sem localização (é falado). Comentário: no Insta, comente e fixe (sem link); no Face, só comente (não fixa mais).']
q['pre_gancho'] = {'titulo_secao': 'Pré-gancho (o do nora37, ESPELHADO: não gerar)', 'duracao': 4, 'tomadas': 1, 'com_rosto': True,
  'conceito': 'O geodo que racha do nora37 (viral x1), espelhado na horizontal como o viral x2 e o nora39: a mesma pedra, outro lado. 0 crédito. O nora40 usou o mesmo clipe sem espelhar.',
  'modo': 'Não gere nada aqui. No CapCut, espelhe na horizontal SÓ o clipe nora37-PRE (o corpo não), antes de pôr os textos.',
  'montagem': '1) nora37-PRE espelhado: uns 3,5 s (corte logo depois que as metades abrem).\n2) Corte seco para o corpo cortado (nora46-cortado: o Take 1 novo + as cópias dos takes 2 a 12 do nora40).\n3) A caixa do topo já entra no primeiro quadro do pré-gancho.',
  'texto_tela': '', 'edicao': ''}
NUM46 = [
  {'t': '888', 'x': 86, 'y': 12, 'onde': 'alto à direita', 'cor_nome': 'branco', 'cor': '#FFFFFF', 'tamanho': 15},
  {'t': '11:11', 'x': 8, 'y': 40, 'onde': 'à esquerda, na altura do ombro', 'cor_nome': 'ciano', 'cor': '#3DE0FF', 'tamanho': 13},
  {'t': '222', 'x': 7, 'y': 64, 'onde': 'embaixo à esquerda, ao lado da mão', 'cor_nome': 'verde-limão', 'cor': '#7CFF4F', 'tamanho': 11}]
q['mapa_tela']['numeros'] = NUM46
for e in q['mapa_tela']['estilos']:
    if e['nome'].startswith('Números'):
        e['nome'] = 'Números fixos espalhados (888, 11:11, 222)'; e['obs'] = num_txt(NUM46)
q['mapa_tela']['regras'][0] = ('Números fixos espalhados (um em cima, um no meio, um mais embaixo), longe do rosto, das mãos e do objeto, nos lugares do desenho. '
  'Confira o 1º quadro do hook espelhado (a bandeira fica à direita nele): se um número cobrir o geodo ou o rosto, suba ou desça uns 60 no Y.')
for x in q['edicao_linha']:
    if x['quando'].startswith('0.'):
        x['texto'] = 'Pré-gancho (nora37-PRE espelhado, uns 3,5 s)'
    if x['quando'].startswith('2.'):
        x['texto'] = '888  ·  11:11  ·  222  (espalhados)'
        x['como'] = 'Cada número de uma cor e de um tamanho, num lugar, parados do primeiro ao último quadro: ' + num_txt(NUM46)
q['comentario_fixado'] = {
  'insta': "Cancer, Scorpio, Pisces, this one is yours. 🔥 PART 2 of this sign is in my story: pick 3 cards and see what November brings you. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222 and follow me so you don't miss your sign's next message.",
  'face': "Cancer, Scorpio, Pisces, this one is yours. 🔥 PART 2 of this sign is in my Story: pick 3 cards and see what November brings you. Tap my profile picture NOW, it's gone in 24 hours. Comment 222 and follow me so you don't miss your sign's next message."}
q['story']['nota'] = '✅ NÃO FAÇA STORY NESTE VÍDEO. Valem os stories de hoje (o story-2810 repostado às ~17h e o story-3010, novo, do painel do nora45), no Insta e no Face.'
q['story']['ja_postado'] = True
pl = q['pecas']['lista']
pl[0] = {'nome': 'nora37-PRE', 'de': 'nora37-PRE', 'tipo': 'pré-gancho (do nora37)', 'status': 'reutilizar', 'creditos': 7,
         'descricao': 'O geodo que racha, ESPELHADO na horizontal só no CapCut.'}
for x in pl:
    if x['nome'] == 'nora46-T01-gancho-cancer-escorpiao-peixes':
        x['descricao'] = 'Take 1: “' + T1 + '”'
        x['base'] = 'Take 1 da série (corpo A: signos + “keep your mouth shut” + datas), com as datas de quem vê hoje e amanhã.'
q['pecas']['decisao'] = [
  'Longo do corpo A de novo: nora40 e nora43 foram os vídeos que mais trouxeram seguidores (11 e 10), envios (16 e 19) e salvos (20 e 18) da Nora.',
  'Hook do geodo espelhado (como o viral x2 e o nora39): 0 crédito e diferente do nora40, que usou o mesmo clipe sem espelhar.',
  'Câncer, Escorpião e Peixes ainda não tinham um longo; datas 30, 31 e 1º de novembro (quem vê hoje, amanhã ou depois).',
  'A fita como hook do longo (nora42) não deu certo nas duas redes; fica só no vídeo de 8 s.',
  AGENDA]
gravar('46', q)
print('ok')
