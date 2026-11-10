# 29/10/2026 ~13h: ideia do aluno aprovada. O nora41 deixa a placa na mão e vira a fita na boca
# (reel de @daflones_, seção 41 de BIBLIOTECA-VIDEOS-VIRAIS.md) com o papel dos signos e das datas
# num porta-retrato em pé na mesa. O hook do nora42 vira a mesma cena com GEMINI, LIBRA, AQUARIUS.
# nora40 e nora43: só as linhas que citam a placa do nora41 e o hook do nora42.
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

def abrir(n):
    f = f'{BASE}/PAINEL-NORA{n}.html'
    s = open(f, encoding='utf-8').read()
    m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
    return f, s, m, json.loads(m.group(1))

def salvar(f, s, m, p):
    open(f, 'w', encoding='utf-8').write(s[:m.start(1)] + json.dumps(p, ensure_ascii=False) + s[m.end(1):])

LEITURA = ('29/10/2026 (~13h, troca da placa pela fita e o porta-retrato): a leitura completa de LEIA-TUDO-ANTES.md foi feita nesta sessão, '
    'no mesmo dia, antes de montar os painéis do nora40 ao nora43 (FATOS-DO-ALUNO.md, CLAUDE.md, 00-LEIA-PRIMEIRO.md, BRIEFING-MANIFESTACAO.md, '
    'PROJETO-Dana.md, BRIEFING-LOVECHART.md, LICOES-FLOW-E-PROMPTS.md, COMUNIDADE-E-ESTRATEGIA.md, os DNA Visual, REGISTRO-DE-PERSONAS.md, '
    'hooks.md, Formatos Narrativos, Exemplos de Roteiros, ctas.md, COMUNICACAO-VISCERAL-E-FALADA.md, as BIBLIOTECA-*, PESQUISA-PUBLICO.md, '
    'Prompts.txt, CHECKLIST-DE-PRODUCAO.md, PAPEL-AGENTE-FLOW.md, GUIA-CREATIVE-HUB.md, os PLANO-CREDITOS-*, os PASSO-A-PASSO-*, os EXEMPLO-*, '
    'PAINEL-MODELO.html, as métricas, BIBLIOTECA-DE-TAKES.md, os ROTEIRO-*, os RESERVA-*, os STORY-* e os TAKE-NOVO-*). '
    'Para esta troca reli inteiros, neste turno: FATOS-DO-ALUNO.md, LICOES-FLOW-E-PROMPTS.md (checklist e todas as lições), DNA Visual - Nora v2.md, '
    'BIBLIOTECA-PRE-GANCHOS.md, COMUNIDADE-E-ESTRATEGIA.md (27 a 29/10), BIBLIOTECA-VIDEOS-VIRAIS.md (M2 e seção 41, a fita na boca), '
    'ROTEIRO-NORA41 e ROTEIRO-NORA42, PAINEL-MODELO.html (ordem das seções e etapas) e os pacotes dos painéis do nora40 ao nora43. '
    'Não reabri neste turno os arquivos de método de fala (hooks, formatos, CTAs, bodies, cold reading, copy): a fala dos longos não mudou e o nora41 não tem fala.')

DIA = ('Os signos do dia (29/10) ficam divididos entre os 4 vídeos do Insta: 17h nora40 Áries/Leão/Sagitário (longo, hook do geodo), '
    '19h30 nora41 Câncer/Escorpião/Peixes (texto na tela: a fita na boca e o porta-retrato dos signos, ideia do aluno), '
    '22h nora42 Gêmeos/Libra/Aquário (longo, hook da fita na boca), 00h30 nora43 Touro/Virgem/Capricórnio (longo, hook da pedra escura). '
    'No Face, os mesmos 4 ao vivo e, às 14h, a nora39-VAR.')

def troca_dia(p):
    d = p['pecas']['decisao']
    for i, t in enumerate(d):
        if t.startswith('Os signos do dia (29/10)'):
            d[i] = DIA
            return
    raise SystemExit('linha do dia não achada')

# ---------------- nora41 ----------------
SIGNOS41 = 'CANCER, SCORPIO, PISCES'
TOPO = 'Keep your mouth shut. November is your most blessed month. Send it to yourself.'

CENA41 = (
    'Generate a NEW photo from the attached character sheet only. Vertical 9:16 photo of the woman from the attached reference sheet sitting at a small '
    'dark walnut-wood desk in a dim, cozy real American bedroom at night, as if a friend took it with a phone. '
    'CAMERA: a handheld phone at the height of her mouth, about 60 cm in front of her face, level, no tilt. '
    'FRAMING, in percent of the image height from the top: from 0 to 12 percent only the dark wall and the top of her hair; her eyes at about 29 percent; '
    'her closed lips at about 36 percent; her chin at about 40 percent; the picture frame from about 52 to 71 percent; the desk surface from about 65 percent '
    'down to the bottom of the image. Her knees, legs, the chair and the floor are NOT in the frame. '
    'POSE AND FACE: she sits upright with her shoulders square to the lens and looks straight into the lens with a calm, intense, knowing gaze; her lips are '
    'closed and relaxed, with no smile. '
    'HANDS AND TAPE: both hands are raised in front of her at collarbone height, between her chin and the top of the picture frame, at about 41 to 49 percent '
    'of the image height, never covering her mouth, her chin or the picture frame: her LEFT hand (the hand on the RIGHT side of the image) holds one roll of '
    'wide washi tape between its thumb and fingers; her RIGHT hand (the hand on the LEFT side of the image) pinches the free end of the tape between its thumb '
    'and index finger and has pulled out a flat strip about 10 cm long, stretched horizontally between her two hands and still attached to the roll. '
    'THE WASHI TAPE: a paper tape about 3 cm wide, matte deep emerald green, printed with a small repeating pattern of tiny gold five-pointed stars and tiny '
    'gold crescent moons; the roll is about 6 cm across; no letters, numbers, words or logos on the tape. The small gold sun ring is on her right index finger '
    'and the thin gold bracelets are on her left wrist; each hand has exactly five fingers with natural proportions; nothing else is in her hands. '
    'THE PICTURE FRAME: one simple thin gold metal picture frame, landscape (wider than tall), about 18 cm wide and 13 cm tall, standing upright on the desk '
    'on its small easel back, at the front edge of the desk, about 30 cm from the lens, centered left to right, its front facing the lens squarely, spanning '
    'about 56 percent of the image width, its top edge at about 52 percent and its bottom edge resting on the desk at about 71 percent of the image height; '
    'the frame is matte, with no glass glare and no reflections. Instead of a photo, the frame holds one plain matte white card that fills its opening; on the '
    'card, written by hand with thick felt-tip markers in neat, bold capital letters, there are exactly two centered lines and nothing else: the first line, '
    'large, in bright red marker, reads CANCER, SCORPIO, PISCES; the second line, smaller, in black marker, reads 29, 30 AND 31 OF OCTOBER. Spell every word '
    'exactly like that, letter by letter (C-A-N-C-E-R, S-C-O-R-P-I-O, P-I-S-C-E-S). No other words, numbers, drawings, stickers, tags or logos on the card '
    'or the frame. The frame stands in front of her lower torso and never covers her face or her hands. '
    'THE DESK: plain dark walnut wood; on it there is only the picture frame and, at the back of the desk at the far right edge of the image, beside her left '
    'elbow, a small plain white ceramic mug holding a small American flag (about 20 by 13 cm, on a short wooden stick). The front corners of the desk on both '
    'sides of the picture frame stay empty. '
    'BACKGROUND (soft and out of focus): a plain deep navy-blue bedroom wall; one strand of tiny warm-white fairy lights hangs in loose loops on the wall behind '
    'her, on both sides of her head and shoulders, glowing as small soft round bokeh dots, never in front of her face and never above the top of her head; on '
    'the RIGHT side of the image, behind her shoulder, a small bedside lamp with a cream fabric shade glowing warm. Nothing else: no other people, no pets, no '
    'posters, no other picture frames, no signs, no logos and no readable text except the two lines on the card. '
    'LIGHT: warm tungsten lamp light from the right side of the image as the key light plus the soft glow of the fairy lights, the rest of the room dim and '
    'cozy; a realistic low-light phone photo with a little natural grain. '
    'FREE ZONES: the top 12 percent of the frame shows only the dark wall and the top of her hair, and the wall at the left and right edges of the image beside '
    'her head stays plain (only the soft fairy lights). No date stamp, no watermark, no caption, no logo. Do not rejuvenate or smooth her face.')

FIM41 = (
    'VISUAL REFERENCE LOCK: use exclusively the ATTACHED image as the identity authority. There is no pet in this project: no animal appears in any scene. '
    'EDIT of the attached image (the woman at the desk with the roll of washi tape and the gold picture frame). Keep EVERYTHING exactly as it is: the same '
    'woman, the same face, eyes, eyebrows, hair, braid, face gems, earrings, necklace, bracelets and ring, the same wine-red top, the same gold picture frame '
    'in the same position, size and angle with the same white card and the same two handwritten lines (CANCER, SCORPIO, PISCES in red and 29, 30 AND 31 OF '
    'OCTOBER in black, letter by letter), the same desk, the same mug with the small American flag, the same fairy lights, lamp, wall and warm light, and the '
    'same framing and camera. Change ONLY these three things: '
    '(1) one torn strip of the same matte emerald-green washi tape with tiny gold stars and tiny gold crescent moons, about 12 cm long and 3 cm wide, is now '
    'stuck flat and smooth, horizontally, across her closed lips, covering both lips completely from corner to corner and reaching about 1.5 cm onto each '
    'cheek, with slightly uneven torn ends; it covers nothing else: her nose, her chin, the gold crescent-moon gem and the three tiny gold star gems on her '
    'cheek stay fully visible; '
    '(2) her two hands now rest relaxed on the desk on both sides of the picture frame, never covering the card: her RIGHT hand (the hand on the LEFT side of '
    'the image) lies flat on the desk just left of the frame, and her LEFT hand (the hand on the RIGHT side of the image) rests on the desk just right of the '
    'frame with the small roll of washi tape loosely under its fingers; each hand has exactly five fingers; '
    '(3) her eyebrows are raised very slightly and she looks straight into the lens with a calm, intense, knowing gaze. '
    'Only one strip of tape anywhere. No text added, no date stamp, no watermark, no caption. Do not rejuvenate or smooth her face.')

CLIPE41 = (
    'Create a single continuous 8-second video clip that opens exactly on the first supplied frame and ends exactly on the last supplied frame, vertical 9:16. '
    'Handheld smartphone camera about 60 cm from the woman at the height of her mouth, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n'
    'THE MAIN EVENT: the woman, sitting at a desk in a dim bedroom at night, tears a strip of emerald-green washi tape with tiny gold stars and moons off the '
    'roll and seals her own closed lips with it, calmly, like someone keeping a secret. A small gold picture frame with a handwritten white card stands on the '
    'desk in front of her the whole time. She never speaks.\n\n'
    'SECOND BY SECOND (something visible moves in EVERY second):\n'
    '0.0 to 1.0 s: her right hand (on the left side of the image) pulls the free end of the tape further out of the roll, from about 10 cm to about 14 cm, '
    'with a soft crackle; her left hand (on the right side of the image) holds the roll steady.\n'
    '1.0 to 2.0 s: with one quick twist of her right hand the strip tears off the roll; the strip now hangs flat from the fingers of her right hand and the '
    'roll stays in her left hand.\n'
    '2.0 to 3.0 s: both hands bring the strip up to her mouth: her right hand holds its left end and the thumb and index finger of her left hand, still '
    'holding the roll, take its right end; the strip is held flat and horizontal just in front of her closed lips.\n'
    '3.0 to 4.5 s: she presses the strip onto her closed lips and both index fingers smooth it from the center out to the corners of her mouth; the tape lies '
    'flat across her lips from corner to corner.\n'
    '4.5 to 5.5 s: both hands come down and rest on the desk on both sides of the picture frame, the roll loosely under the fingers of her left hand, exactly '
    'as in the last supplied frame.\n'
    '5.5 to 6.5 s: her eyes drop to the card in the picture frame for one moment and come back to the lens.\n'
    '6.5 to 8.0 s: she raises her eyebrows very slightly and holds still with a calm, intense, knowing look, exactly as in the last supplied frame.\n\n'
    'WHAT MUST NOT HAPPEN: she does not speak or mouth any words, and her lips stay closed for the whole clip; once the tape is on her lips it stays flat and '
    'in place until the end (it never falls, peels, slides or disappears); there is only one strip of tape; the tape never covers her nose, eyes or chin or '
    'the gold moon and star gems on her cheek; the picture frame never moves, tips, slides or falls; the handwriting on the card never changes, moves, blurs, '
    'fades or gains or loses letters, and no new text appears anywhere; her hands never cover the card; each hand has exactly five fingers; the roll never '
    'disappears or duplicates; the mug, the flag, the fairy lights, the lamp and the wall never move; the fairy lights do not blink; the lamp light does not '
    'flicker; no object, person or animal appears or disappears.\n\n'
    'VISUAL: she is the same woman as in the supplied frames, calm and composed; realistic natural physics, no morphing, no glow, no magic effects. No added '
    'text, no logos.\n\n'
    'AUDIO: real quiet bedroom sound only, with the soft crackle of the tape being pulled and one short paper rip when it tears. No music, no voice, no added '
    'sound effects.')

NUM41 = [
    {'t': '222', 'x': 13, 'y': 12, 'onde': 'alto à esquerda', 'cor_nome': 'amarelo-ouro', 'cor': '#FFD21F', 'tamanho': 15},
    {'t': '11:11', 'x': 88, 'y': 33, 'onde': 'à direita, na parede, na altura do nariz', 'cor_nome': 'rosa-choque', 'cor': '#FF4FD8', 'tamanho': 12},
    {'t': '888', 'x': 10, 'y': 57, 'onde': 'à esquerda, ao lado do porta-retrato', 'cor_nome': 'verde-limão', 'cor': '#7CFF4F', 'tamanho': 11},
]

def xy(n):
    return f"X {round(n['x'] * 7.2 - 360)} · Y {round(640 - n['y'] * 12.8)}"

NUM_TXT = '; '.join(f"{n['t']} {n['cor_nome']} {n['cor']}, tamanho {n['tamanho']}, {n['onde']} ({xy(n)})" for n in NUM41) + '.'

f, s, m, p = abrir(41)
r = p['roteiro']
r['id'] = 'nora41-TEXTO-NA-TELA-FITA-PORTA-RETRATO-CANCER-ESCORPIAO-PEIXES'
r['titulo'] = 'Texto na tela (Manifestation): a fita na boca e o porta-retrato dos signos, Câncer, Escorpião e Peixes'
r['formato'] = 'Texto na tela, sem fala (clipe de 8 s): ela rasga um pedaço de fita e cola na boca; os signos e as datas ficam num porta-retrato na mesa'
r['molde_hook'] = ('reel da fita na boca (@daflones_, seção 41 de BIBLIOTECA-VIDEOS-VIRAIS.md: ação desde o 1º quadro, texto e imagem dizendo a mesma coisa) '
    '+ placa dos signos e das datas do M2, num porta-retrato em pé na mesa (ideia do aluno, 29/10) + “keep your mouth shut” dos virais w3 a w5')
r['descricao_instagram'] = ('Cancer, Scorpio, Pisces: keep your mouth shut. November is your month. 🤫\n'
    'Send this to yourself. Open my story before it disappears. Comment 222 and follow me.\n#manifestation #astrology #zodiac #usa #usareels')
r['leitura_registro'] = LEITURA
p['figurino'] = p['figurino'].replace('Clothing is secondary to the red handwriting on the white card.',
    'Clothing is secondary to the emerald tape and the red handwriting on the white card.')
p['imagens'][0]['cena'] = CENA41
v = p['videos'][0]
v['fala'] = '(sem fala) texto na tela: ' + TOPO
v['arquivo'] = 'nora41-CLIPE-fita'
p['texto_tela']['hook'] = TOPO
for k in ('insta', 'face'):
    c = p['comentario_fixado'][k]
    old = 'this one is yours. 🔥 Send it to yourself to claim it. '
    assert old in c, k
    p['comentario_fixado'][k] = c.replace(old, "this one is yours. 🤫 Don't tell anyone: send it to yourself to claim it. ", 1)

g = p['pre_gancho']
g['nome_video'] = 'nora41-CLIPE-fita'
g['conceito'] = ('A fita na boca (reel de @daflones_): ela rasga um pedaço de fita verde-esmeralda com estrelinhas e luas douradas e cola na boca, '
    'e fica olhando a lente. Os signos e as datas estão num porta-retrato em pé na mesa, no lugar da foto (ideia do aluno). '
    'A boca tapada é o “keep your mouth shut” do texto do topo.')
g['modo'] = ('Gere depois das duas imagens aprovadas (a nora41-IMG, na seção “Imagens”, e a nora41-FIM, item 1 abaixo) e do meu ok. Um vídeo só, '
    'em FRAMES: primeiro quadro = nora41-IMG, último quadro = nora41-FIM. 8 s, 9:16, áudio ligado. 12 créditos (conta de 53: 53 → 41). '
    'Se o Flow recusar por política, não repita o texto: me mande o print.')
g['etapas'] = [
    {'tipo': 'img', 'titulo': 'Imagem final: a fita colada na boca', 'nome': 'nora41-FIM',
     'anexar': 'SÓ a nora41-IMG aprovada (é uma edição dela)', 'prompt': FIM41},
    {'tipo': 'vid', 'titulo': 'Clipe: ela rasga a fita e cola na boca', 'nome': 'nora41-CLIPE-fita', 'duracao': 8,
     'quadros': 'Modo FRAMES. Primeiro quadro: nora41-IMG. Último quadro: nora41-FIM. 8 s, 9:16, áudio ligado.', 'prompt': CLIPE41},
]
g['montagem'] = ('1) Use o clipe inteiro (8 s).\n'
    '2) Ponha os números fixos, o texto do topo e, dos 5 aos 8 s, o texto do story com a seta (seção de texto na tela).\n'
    '3) Deixe o som do clipe ligado (a fita sendo puxada e rasgada) e ponha a música de sempre (“Ambient Mystical Drone”, da biblioteca do CapCut) '
    'a −12 dB, por baixo. Sem legenda na tela (ela não fala).\n'
    '4) Se a escrita do cartão mudar, se a fita sumir ou descolar, se aparecer outra tira ou se ela mexer a boca, refaça uma vez; se falhar de novo, me chame.')

c = p['central']
c['conferir'] = ('Conferir: é a Nora da nora41-IMG; ela não fala nem mexe a boca; uma tira só, que fica colada até o fim, sem cobrir o nariz nem a lua da '
    'bochecha; a escrita do cartão não muda; o porta-retrato não se mexe; as luzinhas não piscam.')
c['passos'] = [
    'Vídeo de 8 s SEM fala. Não usa a Central do curso nem o agente. Tudo na conta de 53.',
    'IMAGEM (seção “Imagens”): no Flow, anexe SÓ o blueprint e cole o prompt (botão “Copiar imagem com trava”). Aprove só se: é a Nora (lua e 3 '
    'estrelinhas na bochecha do lado esquerdo da imagem, trança com anéis); blusa vinho; o cartão do porta-retrato diz exatamente CANCER, SCORPIO, PISCES '
    '(vermelho) e 29, 30 AND 31 OF OCTOBER (preto), sem outra palavra; a fita é verde-esmeralda com estrelinhas e luas douradas, sem letras; uma mão segura '
    'o rolo e a outra a ponta da fita, cinco dedos, sem cobrir a boca nem o porta-retrato; sem carimbo de data. Se a grafia sair errada, gere de novo '
    '(imagem não gasta crédito). Renomeie para nora41-IMG.',
    'IMAGEM FINAL (seção “Clipe”, item 1): anexe SÓ a nora41-IMG aprovada e cole o prompt. Aprove só se: a fita está colada na boca de canto a canto, sem '
    'cobrir o nariz nem a lua da bochecha; uma tira só; as mãos estão na mesa, dos dois lados do porta-retrato; o cartão continua com a mesma escrita. '
    'Renomeie para nora41-FIM e me mande as duas imagens.',
    'Depois do meu ok: o clipe (seção “Clipe”, item 2) em FRAMES, primeiro quadro = nora41-IMG, último quadro = nora41-FIM, 8 s, 9:16, áudio ligado. '
    'Renomeie para nora41-CLIPE-fita. 12 créditos (conta de 53: 53 → 41). Se o Flow recusar por política, não repita: me mande o print.',
    'CapCut: números fixos, texto do topo, texto do story com a seta (dos 5 aos 8 s), som do clipe ligado e a música de sempre (“Ambient Mystical Drone”, '
    'da biblioteca do CapCut) a −12 dB. Sem legenda na tela e sem corte de silêncio: a Nora não fala.',
    'Postar em 29/10 às 19h30 no Insta e no Face, ao vivo. No Insta, ponha a localização Los Angeles, California. O story repostado hoje tem de estar no ar. '
    'Comentário: no Insta, comente e fixe (sem link); no Face, só comente (não fixa mais).',
]

e = p['edicao_linha']
e[0]['texto'] = TOPO
e[0]['como'] = ('Texto no topo, em 3 linhas, do segundo 0 ao fim do clipe. “Keep your mouth shut.” em branco; “November is your most blessed month.” '
    'em amarelo-ouro; “Send it to yourself.” em branco.')
e[1]['como'] = 'Cada número de uma cor e de um tamanho, num lugar, parados do primeiro ao último quadro: ' + NUM_TXT
e[2]['como'] = ('Texto do story: branco, tamanho 9, em 1 linha, logo abaixo do porta-retrato (faixa verde do mapa da tela). Junto, a seta vermelha embaixo '
    'à esquerda, apontando para baixo, para a foto do perfil.')
e[3]['texto'] = 'Som do clipe ligado (a fita rasgando) + música de sempre (“Ambient Mystical Drone”, da biblioteca do CapCut), −12 dB'
e[3]['como'] = 'Sem legenda na tela (ela não fala) e sem corte de silêncio.'

mt = p['mapa_tela']
mt['legenda'] = [72, 77]
mt['numeros'] = NUM41
for st in mt['estilos']:
    if st['nome'].startswith('Números fixos'):
        st['obs'] = NUM_TXT
    elif st['nome'].startswith('Texto do topo'):
        st['cor'] = 'branco #FFFFFF; “November is your most blessed month.” em amarelo-ouro #FFD21F'
        st['obs'] = 'Centralizado, em 3 linhas, do segundo 0 ao fim do clipe, em X 0 · Y 374 (logo abaixo do 222, sem encostar; pode tocar o alto do cabelo, nunca os olhos).'
    elif st['nome'].startswith('Texto do story'):
        st['obs'] = 'Centralizado, logo abaixo do porta-retrato (faixa verde).'
mt['regras'] = [
    'Números fixos espalhados (um em cima, um no meio, um mais embaixo), longe do rosto, das mãos, da fita e do porta-retrato, nos lugares do desenho. '
    'Lugares provisórios: eu confirmo quando você me mandar a nora41-IMG e a nora41-FIM.',
    'Este vídeo não tem fala, então não tem legenda na tela. São 4 textos: os números fixos (222, 888 e 11:11), o texto do topo (o clipe todo) e, dos 5 aos '
    '8 s, o texto do story na faixa verde e a seta vermelha embaixo à esquerda.',
    'A faixa verde (72% a 77%) é provisória: eu confirmo quando você me mandar as imagens. Nada em cima do rosto, da fita, do cartão ou das mãos.',
    'Confira o quadro dos 5 s: se o texto do story tocar o porta-retrato ou as mãos, comece o texto e a seta aos 6 s.',
]

pc = p['pecas']
pc['lista'] = [
    {'nome': 'nora41-IMG', 'tipo': 'imagem 1 (primeiro quadro)', 'status': 'gerar',
     'descricao': 'Do blueprint: quarto à noite, ela à mesa com o rolo de fita esmeralda nas mãos; porta-retrato dourado na mesa com o cartão CANCER, SCORPIO, PISCES / 29, 30 AND 31 OF OCTOBER.',
     'base': 'Reel da fita na boca + placa do M2 num porta-retrato (ideia do aluno).',
     'serve': 'nora42: o hook é uma edição desta imagem (só a 1ª linha do cartão muda). Próximos vídeos da fita: edição desta cena.'},
    {'nome': 'nora41-FIM', 'tipo': 'imagem final (último quadro)', 'status': 'gerar',
     'descricao': 'Edição da nora41-IMG: a fita colada na boca, as mãos na mesa dos dois lados do porta-retrato.',
     'base': 'O último quadro manda no Flow (lição do item 16): garante a fita no lugar no fim.',
     'serve': 'Só deste vídeo.'},
    {'nome': 'nora41-CLIPE-fita', 'tipo': 'clipe sem fala', 'status': 'gerar', 'creditos': 12,
     'descricao': '8 s: ela puxa a fita, rasga, cola na boca, apoia as mãos na mesa, olha o cartão e volta para a lente.',
     'base': 'Reel da fita na boca (o gesto em ~4,5 s, depois parado olhando a lente).',
     'serve': 'Face: versão -VEL e com filtro (não espelhar: a escrita do cartão inverte). Os primeiros 4,5 s servem de hook para um longo de Câncer, Escorpião e Peixes.'},
]
pc['decisao'] = [
    'Ideia do aluno (29/10): no lugar da placa na mão, a fita na boca do reel de @daflones_ e os signos e as datas num porta-retrato na mesa. '
    'O porta-retrato fica parado, então o Flow deforma menos a escrita; a fita com estrelas e luas é do nicho; a boca tapada é o “keep your mouth shut”.',
    'Sem tesoura: ela rasga a fita com a mão (o Flow erra o gesto de cortar). Sem letras nem números na fita (o Flow erra número pequeno).',
    'Texto do topo: “Keep your mouth shut.” + “November is your most blessed month.” + “Send it to yourself.” (as placas quase não são compartilhadas; '
    'o envio é o selo dos virais).',
    'Mesmos 12 créditos da placa (conta de 53) e o mesmo horário (19h30).',
    DIA,
]
salvar(f, s, m, p)
print('ok 41')

# ---------------- nora42 ----------------
PRE42_IMG = (
    'VISUAL REFERENCE LOCK: use exclusively the ATTACHED image as the identity authority. There is no pet in this project: no animal appears in any scene. '
    'EDIT of the attached image (the woman at the desk with the roll of washi tape and the gold picture frame). Keep EVERYTHING exactly as it is: the same '
    'woman, the same face, eyes, hair, braid, face gems, earrings, necklace, bracelets and ring, the same wine-red top, the same pose, the same hands in the '
    'same places with five fingers each, the same emerald-green washi tape roll and the same strip between her hands, the same gold picture frame in the same '
    'position, size and angle, the same desk, mug with the small American flag, fairy lights, lamp, wall and warm light, and the same framing. Change ONLY the '
    'first handwritten line on the white card inside the picture frame, in the same neat bold capital felt-tip handwriting, the same size and the same bright '
    'red color: it now reads GEMINI, LIBRA, AQUARIUS. The second line stays exactly 29, 30 AND 31 OF OCTOBER in black. Spell every word exactly like that, '
    'letter by letter (G-E-M-I-N-I, L-I-B-R-A, A-Q-U-A-R-I-U-S). Exactly two centered lines and nothing else on the card: no other words, numbers, drawings, '
    'stickers, tags or logos. No date stamp, no watermark, no caption. Do not rejuvenate or smooth her face.')

PRE42_FIM = (
    'VISUAL REFERENCE LOCK: use exclusively the ATTACHED image as the identity authority. There is no pet in this project: no animal appears in any scene. '
    'EDIT of the attached image (the woman at the desk with the roll of washi tape and the gold picture frame that reads GEMINI, LIBRA, AQUARIUS). Keep '
    'EVERYTHING exactly as it is: the same woman, the same face, eyes, eyebrows, hair, braid, face gems, earrings, necklace, bracelets and ring, the same '
    'wine-red top, the same gold picture frame in the same position, size and angle with the same white card and the same two handwritten lines (GEMINI, '
    'LIBRA, AQUARIUS in red and 29, 30 AND 31 OF OCTOBER in black, letter by letter), the same desk, mug with the small American flag, fairy lights, lamp, wall '
    'and warm light, and the same framing and camera. Change ONLY these two things: '
    '(1) one torn strip of the same matte emerald-green washi tape with tiny gold stars and tiny gold crescent moons, about 12 cm long and 3 cm wide, is now '
    'stuck flat and smooth, horizontally, across her closed lips, covering both lips completely from corner to corner and reaching about 1.5 cm onto each '
    'cheek, with slightly uneven torn ends; it covers nothing else: her nose, her chin, the gold crescent-moon gem and the three tiny gold star gems on her '
    'cheek stay fully visible; '
    '(2) both hands are now up at her mouth, just finishing pressing the tape: the tip of the index finger of her RIGHT hand (the hand on the LEFT side of the '
    'image) presses the left end of the tape at the corner of her mouth, and the tip of the index finger of her LEFT hand (the hand on the RIGHT side of the '
    'image), which still holds the small roll of washi tape in its palm, presses the right end; her fingers never cover her eyes, her nose or the gold gems on '
    'her cheek; each hand has exactly five fingers. She looks straight into the lens with a calm, intense, knowing gaze. Only one strip of tape anywhere. No '
    'text added, no date stamp, no watermark, no caption. Do not rejuvenate or smooth her face.')

PRE42_VID = (
    'Create a single continuous 4-second video clip that opens exactly on the first supplied frame and ends exactly on the last supplied frame, vertical 9:16. '
    'Handheld smartphone camera about 60 cm from the woman at the height of her mouth, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n'
    'THE MAIN EVENT: the woman, sitting at a desk in a dim bedroom at night, tears a strip of emerald-green washi tape with tiny gold stars and moons off the '
    'roll and seals her own closed lips with it, calmly, like someone keeping a secret. A small gold picture frame with a handwritten white card stands on the '
    'desk in front of her the whole time. She never speaks.\n\n'
    'SECOND BY SECOND (something visible moves in EVERY second):\n'
    '0.0 to 1.0 s: her right hand (on the left side of the image) pulls the free end of the tape further out of the roll, from about 10 cm to about 14 cm, '
    'with a soft crackle; her left hand (on the right side of the image) holds the roll steady.\n'
    '1.0 to 1.8 s: with one quick twist of her right hand the strip tears off the roll; the roll stays in her left hand.\n'
    '1.8 to 2.6 s: both hands bring the strip up to her mouth: her right hand holds its left end and the thumb and index finger of her left hand, still '
    'holding the roll, take its right end.\n'
    '2.6 to 3.4 s: she presses the strip flat across her closed lips, from corner to corner.\n'
    '3.4 to 4.0 s: both index fingertips stay pressed on the two ends of the tape at the corners of her mouth and she looks into the lens with a calm, intense '
    'look, exactly as in the last supplied frame.\n\n'
    'WHAT MUST NOT HAPPEN: she does not speak or mouth any words, and her lips stay closed for the whole clip; once the tape is on her lips it stays flat and '
    'in place (it never falls, peels, slides or disappears); there is only one strip of tape; the tape and her fingers never cover her nose, eyes or chin or '
    'the gold moon and star gems on her cheek; the picture frame never moves, tips, slides or falls; the handwriting on the card never changes, moves, blurs, '
    'fades or gains or loses letters, and no new text appears anywhere; each hand has exactly five fingers; the roll never disappears or duplicates; the mug, '
    'the flag, the fairy lights, the lamp and the wall never move; the fairy lights do not blink; no object, person or animal appears or disappears.\n\n'
    'VISUAL: she is the same woman as in the supplied frames, calm and composed; realistic natural physics, no morphing, no glow, no magic effects. No added '
    'text, no logos.\n\n'
    'AUDIO: real quiet bedroom sound only, with the soft crackle of the tape being pulled and one short paper rip when it tears. No music, no voice, no added '
    'sound effects.')

f, s, m, p = abrir(42)
r = p['roteiro']
r['id'] = 'nora42-LONGO-HOOK-FITA-GEMEOS-LIBRA-AQUARIO'
r['titulo'] = 'Longo do corpo A (Manifestation), hook da fita na boca: Gêmeos, Libra e Aquário (só o Take 1 novo)'
r['formato'] = 'Hook da fita na boca (4 s, cena do nora41, porta-retrato com Gêmeos, Libra e Aquário) + Take 1 novo + takes 2 a 12 do nora40 (~100 s)'
r['molde_hook'] = ('fita na boca (reel de @daflones_, seção 41) com os signos no porta-retrato da cena do nora41 + corpo A (x1 a x5); '
    'a boca tapada antecipa o “keep your mouth shut” do Take 1')
r['leitura_registro'] = LEITURA
g = p['pre_gancho']
g['titulo_secao'] = 'Hook (4 s, a fita na boca com Gêmeos, Libra e Aquário no porta-retrato, sem fala)'
g['conceito'] = ('A cena do nora41 com o porta-retrato dizendo GEMINI, LIBRA, AQUARIUS: em 4 s ela puxa a fita, rasga e cola na boca. '
    'Corte seco para o Take 1, que diz “keep your mouth shut”. O porta-retrato tem os mesmos signos da fala (por isso não dá para usar o clipe do nora41).')
g['modo'] = ('Conta de 53, depois da nora41-IMG aprovada. Gere a nora42-PRE-IMG (anexe SÓ a nora41-IMG) e, em seguida, a nora42-PRE-FIM (anexe SÓ a '
    'nora42-PRE-IMG) e me mande as duas. Depois do meu ok, o vídeo em FRAMES: primeiro quadro = nora42-PRE-IMG, último quadro = nora42-PRE-FIM, 4 s, 9:16, '
    'áudio ligado. 7 créditos (conta de 53: 41 → 34).')
g['etapas'] = [
    {'tipo': 'img', 'titulo': 'Imagem: o porta-retrato com Gêmeos, Libra e Aquário', 'nome': 'nora42-PRE-IMG',
     'anexar': 'SÓ a nora41-IMG aprovada (é uma edição dela)', 'prompt': PRE42_IMG},
    {'tipo': 'img', 'titulo': 'Imagem final: a fita colada na boca, os dedos nas pontas', 'nome': 'nora42-PRE-FIM',
     'anexar': 'SÓ a nora42-PRE-IMG aprovada (é uma edição dela)', 'prompt': PRE42_FIM},
    {'tipo': 'vid', 'titulo': 'Vídeo: ela rasga a fita e cola na boca', 'nome': 'nora42-PRE', 'duracao': 4,
     'quadros': 'Modo FRAMES. Primeiro quadro: nora42-PRE-IMG. Último quadro: nora42-PRE-FIM. 4 s, 9:16, áudio ligado.', 'prompt': PRE42_VID},
]
g['montagem'] = ('1) nora42-PRE: os 4 s inteiros (termina com a fita colada).\n'
    '2) Corte seco para o corpo cortado (nora42-cortado: o Take 1 novo + as cópias dos takes 2 a 12 do nora40).\n'
    '3) A caixa do topo já entra no primeiro quadro do hook. Deixe o som do hook (a fita rasgando).\n'
    'Se a fita sumir, descolar ou aparecer outra tira, refaça uma vez; se falhar de novo, me chame.')
p['texto_tela']['hook_comeca'] = 'o primeiro quadro do hook (a fita)'
e = p['edicao_linha']
assert e[0]['texto'].startswith('Hook da placa')
e[0]['texto'] = 'Hook da fita na boca (nora42-PRE, 4 s)'
pc = p['pecas']
for it in pc['lista']:
    if it['nome'] == 'nora42-PRE-IMG':
        it['descricao'] = 'Edição da nora41-IMG: só a 1ª linha do cartão do porta-retrato muda (GEMINI, LIBRA, AQUARIUS).'
        it['base'] = 'Fita na boca + porta-retrato, na cena do nora41.'
    elif it['nome'] == 'nora42-PRE':
        it['descricao'] = '4 s em Frames (primeiro e último quadro): ela puxa a fita, rasga e cola na boca.'
        it['base'] = 'Reel da fita na boca (o gesto em ~4,5 s).'
        it['serve'] = 'Face: colado em outros corpos com Gêmeos, Libra e Aquário.'
i = next(k for k, it in enumerate(pc['lista']) if it['nome'] == 'nora42-PRE-IMG')
pc['lista'].insert(i + 1, {'nome': 'nora42-PRE-FIM', 'tipo': 'imagem final do hook', 'status': 'gerar',
    'descricao': 'Edição da nora42-PRE-IMG: a fita colada na boca, os indicadores apertando as pontas.',
    'base': 'O último quadro manda no Flow: garante a fita no lugar no fim do hook.', 'serve': 'Só deste vídeo.'})
d = pc['decisao']
for k, t in enumerate(d):
    if 'placa' in t and not t.startswith('Os signos do dia'):
        print('nora42 decisao com placa:', t[:120])
troca_dia(p)
cp = p['central']['passos']
assert cp[0].startswith('Hook, na conta de 53')
cp[0] = ('Hook, na conta de 53 (seção “Pré-gancho”): gere a nora42-PRE-IMG (anexe SÓ a nora41-IMG aprovada) e a nora42-PRE-FIM (anexe SÓ a '
    'nora42-PRE-IMG) e me mande as duas. Depois do meu ok, o vídeo de 4 s em Frames (7 créditos). Renomeie para nora42-PRE.')
rg = p['mapa_tela']['regras']
rg[0] = ('Números fixos espalhados (um em cima, um no meio, um mais embaixo), longe do rosto, das mãos e do objeto, nos lugares do desenho. No hook da '
    'fita, as mãos sobem até a boca pelo meio do quadro: os números ficam nos lados e não encostam nelas.')
rg[3] = 'No hook da fita (sem fala) não há legenda; a caixa do topo fica em cima do cabelo, acima do rosto.'
salvar(f, s, m, p)
print('ok 42')

# ---------------- nora40 e nora43 ----------------
for n in (40, 43):
    f, s, m, p = abrir(n)
    troca_dia(p)
    for it in p['pecas'].get('proximos', []):
        if it.get('modelo') == 'hook da placa (cena do nora41)':
            it['modelo'] = 'hook da fita na boca (cena do nora41, porta-retrato com os signos)'
    salvar(f, s, m, p)
    print('ok', n)

# nora42: as 2 linhas de decisão que ainda falavam da placa
f, s, m, p = abrir(42)
d = p['pecas']['decisao']
for k, t in enumerate(d):
    if t.startswith('Hook da placa:'):
        d[k] = ('Hook da fita na boca (ideia do aluno, 29/10, do reel de @daflones_): ação em todo segundo e a boca tapada antecipa o '
            '“keep your mouth shut” do Take 1; os signos no porta-retrato seguram quem procura o próprio signo, como a placa (57 a 60% nos 3 s).')
    elif t.startswith('A placa precisa dizer'):
        d[k] = 'O porta-retrato precisa dizer os mesmos signos da fala: por isso duas imagens editadas e um clipe de 4 s (7), e não o clipe do nora41.'
salvar(f, s, m, p)
print('ok 42 decisao')
