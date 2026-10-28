# 28/10/2026: só o nora36 saiu em 27/10. Hoje: 17h nora37 (curto), 19h nora38 (placa), 21h nora39 (curto),
# 23h nora40 (placa), 01h de 29/10 nora41 (placa nova, Câncer/Escorpião/Peixes). Story novo do Manifestation
# (3 cartas na mesa, gerado do blueprint) antes das 16h45, no painel do nora37.
import re, json, copy, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

def ler(nome):
    s = open(f'{BASE}/{nome}', encoding='utf-8').read()
    m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
    return s, m, json.loads(m.group(1))

def gravar(nome, s, m, p):
    open(f'{BASE}/{nome}', 'w', encoding='utf-8').write(s[:m.start(1)] + json.dumps(p, ensure_ascii=False) + s[m.end(1):])

AGENDA = ('Os signos do dia (28/10) ficam divididos entre os 5 vídeos: 17h nora37 curto Touro/Virgem/Capricórnio, '
          '19h nora38 placa Áries/Leão/Sagitário, 21h nora39 curto Câncer/Escorpião/Peixes, 23h nora40 placa '
          'Touro/Virgem/Capricórnio, 01h (29/10) nora41 placa Câncer/Escorpião/Peixes.')
POSTAR = {'PAINEL-NORA37.html': ('27/10 às 19h', '28/10 às 17h'), 'PAINEL-NORA38.html': ('27/10 às 21h', '28/10 às 19h'),
          'PAINEL-NORA39.html': ('27/10 às 23h', '28/10 às 21h'), 'PAINEL-NORA40.html': ('28/10 às 01h', '28/10 às 23h')}

# --- story novo (Manifestation): identidade igual (trava, mapa, âncora e bloco negativo da Nora v2), cena nova ---
_, _, p37 = ler('PAINEL-NORA37.html')
ident = p37['story']['prompt_imagem'].split('FIXED OUTFIT:')[0].rstrip()
STORY_PROMPT = ident + '\n\n' + (
 'FIXED OUTFIT: fortune-teller, subtle mystic; a soft emerald-green fine-knit crew-neck sweater with long sleeves, no print, embroidery or shine. '
 'Clothing is secondary to the contrast of the three cards on the table. Fixed accessories, always visible: the long gold star-and-moon drop earrings, '
 'the long thin gold chain with the small gold Venus-symbol pendant, thin gold bracelets on her left wrist, the gold sun ring and the gold face gems '
 'from the reference sheet; no other jewelry, turban, cape or costume\n\n'
 'UGC STYLE LOCK: vertical 9:16 image, photorealistic, shot in an American home with the spontaneous look of a smartphone. Natural light, real skin, '
 'fabric and hair textures, casual and slightly imperfect framing. The camera stays out of frame. No text, caption, logo, watermark or advertising look.\n\n'
 'SCENE: generate a NEW photo from the attached character sheet only (do not edit any other image). A vertical 9:16 photo taken at night in a cozy '
 'American living room, as if a friend took it with a phone. The camera is at her eye level, about 90 cm in front of her, straight on, with no tilt. '
 'She sits at a small round dark-wood table facing the camera, shoulders square, forearms resting on the table edge, head level, and she looks straight '
 'into the lens with a soft, warm, knowing smile, lips gently closed. FRAMING, in percent of the image height from the top: from 0 to 24 percent only the '
 'plain dark forest-green painted wall behind her shows, with nothing on it (this band stays empty for text); the top of her head is at about 25 percent, '
 'her eyes at about 36 percent, her chin at about 46 percent and the near table edge at about 60 percent; from 60 to 80 percent is the tabletop with the '
 'three cards; from 80 to 100 percent only plain, empty dark-wood tabletop shows (this band stays empty for a sticker). THE THREE CARDS: exactly three '
 'tall, narrow tarot cards, each about 7 cm wide and 12 cm tall, lie flat on the table face down, in one neat straight row side by side about 2 cm apart, '
 'centered left to right, the row about half of the image width, the long side of each card pointing toward the camera. All three backs are identical: '
 'deep navy blue with a fine ornate gold border and one small gold eight-pointed star in the center. No card face is visible; there are no letters, '
 'numbers, words or logos on the cards; there are no other cards and no deck anywhere. HANDS: her RIGHT hand (the hand on the LEFT side of the image) '
 'rests flat on the table just left of the left card, the tip of her index finger lightly touching that card\'s outer edge; her LEFT hand (the hand on the '
 'RIGHT side of the image) rests relaxed on the table to the right of the right card, with the thin gold bracelets and the gold sun ring visible; each '
 'hand has exactly five fingers, and neither hand covers a card or her face. LIGHT: one warm table lamp with a cream linen shade stands behind her at the '
 'far right edge of the image at shoulder height and softly lights her face from the right side of the image; the rest of the room falls into soft warm '
 'shadow, and the wall stays dark enough for light text to read on it. BACKGROUND: on a shelf at the right edge of the image, out of focus, a white mug '
 'holds a small American flag on a stick; nothing else hangs on the walls. DO NOT INCLUDE: candles, crystals, smoke, flowers, a crystal ball, other '
 'people, pets, mirrors, windows, picture frames, posters, text, captions, watermarks, logos or a date stamp. The three cards stay face down and flat. '
 'Do not rejuvenate or smooth the skin.')
ANEXAR = 'SÓ o blueprint (a folha da Nora v2). Nenhuma outra imagem.'
TEXTOS = [{'posicao': 'Uma frase só, no topo (na faixa da parede escura), uma cor (creme #F1E6D3), 1 a 2 linhas',
           'texto': "Tap below: pick 3 cards and see what's coming for you."}]
NOTA37 = ('Hoje (28/10), antes das 16h45, quando o story de ontem expira: no Flow, anexe SÓ o blueprint e gere esta imagem (imagem não gasta crédito); '
          'renomeie para story-2810 e me mande. Depois poste o story no Insta e no Face, com os mesmos links do Manifestation de ontem (STORYIG no Insta, '
          'FACE no Face): o texto no topo (parede escura) e o adesivo embaixo, na faixa da mesa.')
NOTA_OUTROS = 'O story de 28/10 (3 cartas na mesa, postado antes do nora37) vale para este vídeo: não precisa postar outro.'

def story(p, nota):
    st = p['story']; st['prompt_imagem'] = STORY_PROMPT; st['anexar'] = ANEXAR; st['textos'] = TEXTOS; st['nota'] = nota

def comum(nome, p):
    a, b = POSTAR[nome]
    ps = p['central']['passos']
    for i, x in enumerate(ps):
        if x.startswith('Postar em ' + a):
            ps[i] = x.replace('Postar em ' + a, 'Postar em ' + b, 1)
        ps[i] = ps[i].replace('(às 21h vai a placa nora38)', '(às 19h vai a placa nora38)')
    assert any(x.startswith('Postar em ' + b) for x in ps), nome
    dec = (p.get('pecas') or {}).get('decisao') or []
    for i, x in enumerate(dec):
        if x.startswith('Os signos do dia'):
            dec[i] = AGENDA

for nome in POSTAR:
    s, m, p = ler(nome)
    comum(nome, p)
    story(p, NOTA37 if nome == 'PAINEL-NORA37.html' else NOTA_OUTROS)
    gravar(nome, s, m, p)

# --- nora41: placa de Câncer, Escorpião e Peixes, 29/10 às 01h, datas 28, 29 e 30 ---
s40 = open(f'{BASE}/PAINEL-NORA40.html', encoding='utf-8').read()
m = re.search(r'const PACOTE = (\{.*?\});\n', s40, re.S)
txt = m.group(1)
for a, b in [('nora40', 'nora41'), ('TOURO-VIRGEM-CAPRICÓRNIO', 'CÂNCER-ESCORPIÃO-PEIXES'),
             ('Touro, Virgem e Capricórnio', 'Câncer, Escorpião e Peixes'),
             ('TAURUS, VIRGO, CAPRICORN', 'CANCER, SCORPIO, PISCES'), ('Taurus, Virgo, Capricorn', 'Cancer, Scorpio, Pisces'),
             ('T-A-U-R-U-S, V-I-R-G-O, C-A-P-R-I-C-O-R-N', 'C-A-N-C-E-R, S-C-O-R-P-I-O, P-I-S-C-E-S'),
             ('27, 28 AND 29 OF OCTOBER', '28, 29 AND 30 OF OCTOBER'), ('Postar em 28/10 às 23h', 'Postar em 29/10 às 01h')]:
    assert a in txt, a
    txt = txt.replace(a, b)
p41 = json.loads(txt)
assert 'Touro' not in json.dumps(p41['roteiro'], ensure_ascii=False)
dec = p41['pecas']['decisao']
for i, x in enumerate(dec):
    if x.startswith('Os signos do dia'):
        dec[i] = AGENDA
story(p41, NOTA_OUTROS)
s41 = s40[:m.start(1)] + json.dumps(p41, ensure_ascii=False) + s40[m.end(1):]
open(f'{BASE}/PAINEL-NORA41.html', 'w', encoding='utf-8').write(s41)
print('ok')
