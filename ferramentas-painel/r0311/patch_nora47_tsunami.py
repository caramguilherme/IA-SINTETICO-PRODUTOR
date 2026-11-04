# nora47 com o gancho do tsunami (03/11/2026 ~23h): praia + onda + bunker, Take 1 dentro do bunker, corpo B do nora46 do Take 2 em diante.
import re, json, sys
F = sys.argv[1] if len(sys.argv) > 1 else 'PAINEL-NORA47.html'
s = open(F, encoding='utf-8').read()
m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
P = json.loads(m.group(1))
P8 = json.loads(re.search(r'const PACOTE = (\{.*?\});\n', open('PAINEL-NORA48.html', encoding='utf-8').read(), re.S).group(1))

TRAVA = P['trava_referencia']
FIG = P['figurino']
FALA = "Taurus, Virgo or Capricorn: if love hasn't caught up with who you've become, this wave came to clear the way before 11:11."
OUTFIT_BEACH = ("OUTFIT (the same as in all her recent videos): " + FIG + "; plus loose light-beige linen wide-leg trousers and simple flat tan leather sandals. "
                "The open blazer and her long hair blow in the strong wind.")
NEG = ("No other people, no animals, no boats, no buildings other than the one bunker, no houses, no signs, no flags, no logos, no text, no date stamp, no watermark, no caption. "
       "Each visible hand has exactly five fingers. Do not rejuvenate or smooth her face.")

IMG1 = ("Attach ONLY the character consistency sheet. " + TRAVA + "\n\nSCENE (a real photo taken with a smartphone, vertical 9:16, natural daylight, realistic, not cinematic): "
 "an empty, wide sandy beach in the daytime under a heavy dark-grey overcast sky. The camera is held at the height of her hips about 4 meters from her, with a wide lens and a slight low angle. "
 "She stands on wet sand slightly left of center, her whole body visible from the top of her head to her feet, her head at about 40 percent of the frame height, facing the camera; she has just noticed something: her eyes are wide and alarmed, her eyebrows raised, her lips closed, her arms slightly away from her body as if about to run. "
 "Behind her, filling the whole upper half of the image: the open sea and a gigantic dark blue-green wave already rising out of it, about four times her height, with a white foam crest just beginning to curl at the top and spray blowing off it; the wave is still far behind her and has not reached the beach. "
 "On the right side of the image, about 4 meters from her, on the sand: one small, old, weathered grey concrete bunker, about 2.5 meters tall and 3 meters wide, with one heavy dark-grey riveted steel door on the wall that faces her (the door is closed). "
 + OUTFIT_BEACH + " The top quarter of the image shows only sky and the top of the wave (free space for text). " + NEG)

IMG2 = ("Attach ONLY the approved nora47-PRE-IMG1 (this is an EDIT of it). VISUAL REFERENCE LOCK: use exclusively the ATTACHED image as the identity authority. There is no pet in this project: no animal appears in any scene. "
 "EDIT of the attached image (the woman on the beach with the giant wave rising behind her and the small concrete bunker on the right side of the image). Keep EVERYTHING else exactly as it is: the same woman, the same face, eyes, hair, braid, face gems, earrings and necklace, the same open ivory-cream blazer, white blouse, beige trousers and sandals, the same beach, sky and sea, the same bunker in the same place with the same size, and the same camera position and framing. "
 "Change ONLY these two things: (1) the giant dark blue-green wave is now much taller and closer, about six times her height, towering over the beach and curling forward, its white foam crest about to break, casting a dark shadow over the sand; it still has not touched the beach or the bunker; "
 "(2) the woman is now at the bunker on the right side of the image: its heavy riveted steel door is pulled wide open, and she is stepping into the dark doorway with one foot already inside, one hand gripping the edge of the open door, her body turned toward the doorway and her head turned back over her shoulder toward the camera, so her face is still clearly visible in a three-quarter view, with wide alarmed eyes and closed lips; her hair and blazer blow in the wind. "
 "She is not hurt and not wet. " + NEG)

IMGT = ("Attach TWO images, in this order: FIRST the character consistency sheet, SECOND the approved nora47-PRE-IMG1. The FIRST image is the only identity authority. The SECOND image is used ONLY for her outfit (the open ivory-cream blazer and the white blouse) and for her slightly windswept hair; never copy the face, the beach or the camera from the second image. "
 + TRAVA.replace("MAP OF THE ATTACHED REFERENCE", "MAP OF THE FIRST ATTACHED IMAGE") + "\n\nFIXED OUTFIT: " + FIG + "\n\n"
 "SCENE (a real photo taken with a smartphone, vertical 9:16, realistic, not cinematic): inside a small, dim, empty concrete coastal bunker in the daytime. "
 "She stands with her back pressed flat against a heavy, closed, weathered dark-grey riveted steel door that fills the background behind her; the door is shut tight, with thin bright cracks of grey daylight along its edges. "
 "The light comes from one small caged bulb lamp mounted on the rough grey concrete wall at the upper left of the image, giving a warm dim light on her face, plus the cold daylight from the door cracks. "
 "Framing: from a little above the top of her head down to just below her elbows; the camera is a handheld phone at the height of her collarbones about 80 centimeters from her; her face is centered in the upper half of the image with her eyes at about 30 percent of the frame height. "
 "Both arms hang relaxed along her sides and both hands are below the bottom edge of the image (no hands in the frame). "
 "She looks straight into the lens with a calm, knowing expression and a faint warm half-smile, lips closed, as if the danger has just passed. Her long black wavy hair is slightly windswept, with a few loose strands, and the thin gold-ringed braid stays at the front on the right side of the image. "
 "The area above her head (top 25 percent of the image) shows only the steel door and the concrete wall, with no objects (free space for text). "
 "Dry room: no water, no puddles, no damage, no dust in the air. No other people, no animals, no signs, no flags, no logos, no text, no date stamp, no watermark, no caption. Do not rejuvenate or smooth her face.")

VID_A = ("Create a single continuous 4-second video clip that opens exactly on the first supplied frame and ends exactly on the last supplied frame, vertical 9:16. "
 "Handheld smartphone camera at the height of her hips about 4 meters from the woman, slight low angle, wide lens, natural handheld shake; the camera pans a little to the right to follow her; no zoom, no cuts.\n\n"
 "THE MAIN EVENT: on an empty beach under a dark grey sky, a gigantic dark blue-green wave rises out of the sea behind the woman; she sees it, runs across the sand and gets into the small grey concrete bunker on the right side of the image. She never speaks.\n\n"
 "SECOND BY SECOND (something visible moves in EVERY second):\n"
 "0.0 to 0.8 s: she turns her head to look back at the wave over her shoulder; the wave behind her grows from about four to about five times her height, its white foam crest starting to curl, with a deep roar.\n"
 "0.8 to 2.6 s: she runs across the wet sand toward the bunker on the right side of the image, her hair and open blazer flying in the wind; spray blows off the crest; the wave keeps rising and moving toward the shore.\n"
 "2.6 to 3.4 s: she reaches the bunker, grabs the edge of the heavy steel door and pulls it wide open.\n"
 "3.4 to 4.0 s: she steps into the doorway and looks back over her shoulder toward the camera with wide alarmed eyes while the wave towers over the beach, exactly as in the last supplied frame.\n\n"
 "WHAT MUST NOT HAPPEN: the wave does not break, does not touch the beach or the bunker and does not reach her during this clip; she never falls, is never hurt and never disappears; she does not speak or mouth any words; the bunker never moves or changes size; no other people, animals, boats or vehicles appear; no text appears anywhere; each hand has exactly five fingers.\n\n"
 "VISUAL: she is the same woman as in the supplied frames; realistic water physics like a real phone video of a huge wave, no morphing, no glow, no CGI look. No added text, no logos.\n\n"
 "AUDIO: the deep roar of the wave, strong wind, her quick steps on wet sand and the creak of the heavy metal door. No music, no voice.")

VID_B = ("Create a single continuous 4-second video clip that opens exactly on the supplied frame and ends exactly on the same supplied frame, vertical 9:16. "
 "Handheld smartphone camera inside the bunker about 80 cm from the woman at the height of her collarbones; it shakes hard only during the impact and then settles back to the exact framing of the frame; no zoom, no cuts.\n\n"
 "THE MAIN EVENT: inside a small dim concrete bunker, the woman stands with her back pressed against the closed heavy steel door; outside, the giant wave slams into the door. She never speaks.\n\n"
 "SECOND BY SECOND (something visible moves in EVERY second):\n"
 "0.0 to 0.7 s: she presses her back against the door, breathing fast, eyes wide, lips closed; a low rumble grows louder.\n"
 "0.7 to 1.5 s: a massive boom: the steel door shudders hard behind her, she flinches, a little dust and grit falls from the ceiling, and the caged lamp on the wall swings and flickers.\n"
 "1.5 to 2.5 s: short thin jets of white seawater spray in through the narrow gaps at the edges of the door, on both sides behind her shoulders, and then stop.\n"
 "2.5 to 4.0 s: the shaking stops, the lamp settles, the roar fades to a distant rumble; she exhales, her face relaxes and she looks straight into the lens with a calm, faint, knowing half-smile, exactly as in the frame.\n\n"
 "WHAT MUST NOT HAPPEN: the door never opens, bends or breaks; the water never floods the room, never hits her and never stays on her; her hair, face, face gems, earrings, necklace, blazer and blouse stay exactly as in the frame; she is never hurt; she does not speak or mouth any words and her lips stay closed; both hands stay below the bottom edge of the image the whole time; no object, person, animal or text appears or disappears.\n\n"
 "VISUAL: the same woman as in the supplied frame; realistic physics, no morphing, no glow, no CGI look. No added text, no logos.\n\n"
 "AUDIO: a growing rumble, one huge metallic boom, rattling grit, the hiss of water spray, then quiet with a distant rumble of the sea. No music, no voice.")

LIVRE = ("Casual handheld smartphone video inside a small, dim, empty concrete coastal bunker in the daytime, lit by one small caged bulb lamp on the concrete wall at the upper left of the frame and by thin cracks of grey daylight along the edges of the closed steel door behind her. "
 "CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair (slightly windswept) with the thin gold-ringed braid on the right side of the frame, her gold moon and star face gems, her drop earrings, her Venus necklace, her open ivory-cream blazer and her plain white round-neck top stay exactly as in the reference image; she stands with her back against the closed heavy riveted steel door, facing the lens; the framing is exactly the one of the reference image, from a little above the top of her head down to just below her elbows, with her face centered in the upper half of the frame and her eyes at about 30 percent of the frame height; both arms stay relaxed along her sides and both hands stay below the bottom edge of the frame for the whole clip; the door stays closed and still, the lamp and the concrete walls never move; no water, no dust and no shaking during the take; "
 "the camera is a handheld phone at the height of her collarbones about 80 centimeters from her with only a tiny natural sway, no zoom, no cuts and no reframing; no glow and no sparkles; no object, person, animal or text appears or disappears; no on-screen text, no captions, no logos; real quiet room sound with a faint distant rumble of the sea only, no music. "
 "SPEECH RULE for every take: she says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added sentence before, between or after; numbers are spoken as words (11:11 as \"eleven eleven\"); when she finishes the last word she closes her lips, stays silent and keeps a calm still expression until the clip ends.")

MOV = ("Throughout the whole 10 seconds she stands with her back against the closed steel door facing the lens, with both arms relaxed along her sides and both hands below the bottom edge of the frame, during the first half of the take she takes one slow breath and tilts her head slightly with soft, understanding eyes, during the second half she leans her head slightly toward the lens and gives one slow knowing nod with a warm half-smile, her eyes stay on the lens the whole time, and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; "
       "the door, the lamp and the walls stay completely still and no hand ever enters the frame.")

# checagem: nenhuma sequência de 2 palavras da fala na movimentação (P32)
def bigr(t):
    w = re.findall(r"[a-z0-9:']+", t.lower()); return {(w[i], w[i+1]) for i in range(len(w)-1)}
comuns = {('and','it'),('of','the'),('to','the'),('the','way')}
ov = (bigr(FALA) & bigr(MOV)) - comuns
assert not ov, ov
assert len(FALA.split()) <= 22

R = P['roteiro']
R['titulo'] = 'Gancho do tsunami (praia, onda, bunker) + Take 1 de Touro, Virgem e Capricórnio dentro do bunker + corpo B do nora46'
R['formato'] = 'Hook NOVO do tsunami em 2 tomadas (praia → bunker; a onda bate na porta) + Take 1 NOVO dentro do bunker (Touro, Virgem e Capricórnio) + takes 2 a 12 do nora46 (~95 s)'
R['molde_hook'] = ('“gancho bizarro” do tsunami (Vinicius Almeida, 83 vendas em out., 100% Face; BIBLIOTECA-VIDEOS-VIRAIS seção 48): ela na praia, a onda gigante atrás, '
                   'ela corre e se tranca num bunker, a onda bate na porta e ela começa a falar. Take 1 pela aula do Iorhan (signos + para quem é: amor que não acompanhou) e a onda reenquadrada como positiva (“veio abrir caminho”), sem ameaça (P42).')
R['duracao_total'] = 95
R['leitura_registro'] = ('03/11/2026 ~23h05 (pedido do aluno: painel em ~30 min para postar hoje; leitura PARCIAL, registro honesto): reli o pacote deste painel e o do nora48 (story-0311), '
  'os prompts do hook do nora42 (modelo de imagem, edição e vídeo em Frames), a trava de identidade e o figurino do nora46, a seção 48 de BIBLIOTECA-VIDEOS-VIRAIS.md (o tsunami, descrito pelo Vinicius e pelo aluno), '
  'as regras P14, P26, P28, P29, P32, P33, P35, P42 e a do nora50 em diante do CLAUDE.md. Não reli a lista inteira de LEIA-TUDO-ANTES.md hoje (a última leitura completa foi em 31/10 para o corpo B). '
  'A fala nova tem 21 palavras e passou na checagem de sobreposição com a movimentação.')

P['refs'] = ['Folha de consistência da Nora (blueprint)', 'nora47-PRE-IMG1 (para a edição e para a roupa da nora47-IMG)']
P.pop('imagem_reutilizada', None)
P['imagens'] = [{'rotulo': 'IMAGEM 1 · nora47-IMG (dentro do bunker)', 'cena': 'dentro do bunker, de costas para a porta de aço fechada, olhando para a lente',
                 'anexar': '1º a folha (blueprint), 2º a nora47-PRE-IMG1 (só para a roupa e o cabelo)', 'prompt_completo': IMGT}]

v = P['videos'][0]
v['rotulo'] = 'T01 · nora47'
v['cena'] = 'Take 1/12 do nora47 · Gancho dentro do bunker: Touro, Virgem e Capricórnio + a onda que abriu caminho'
v['fala'] = FALA
v['movimentacao'] = MOV
v['arquivo'] = 'nora47-T01-gancho-onda-touro-virgem-capricornio'

P['pre_gancho'] = {
 'titulo_secao': 'Hook NOVO: o tsunami (2 tomadas de 4 s, sem fala)',
 'duracao': 7, 'tomadas': 2, 'com_rosto': True,
 'conceito': 'Tomada 1: ela na praia, a onda gigante subindo atrás; ela corre e entra no bunker. Tomada 2: dentro, de costas na porta fechada, a onda bate, a porta treme e espirra água pelas frestas; ela respira e olha para a lente. Corte seco para o Take 1, falado ali mesmo. 14 créditos (2 × 7), conta grande.',
 'modo': 'Primeiro as 3 imagens (nora47-PRE-IMG1, nora47-PRE-IMG2 e nora47-IMG). Depois os 2 vídeos em FRAMES, 4 s, 9:16, áudio ligado.',
 'etapas': [
  {'tipo': 'img', 'titulo': 'Imagem 1: a praia, a onda subindo atrás dela', 'nome': 'nora47-PRE-IMG1', 'anexar': 'SÓ a folha de consistência (blueprint)', 'prompt': IMG1},
  {'tipo': 'img', 'titulo': 'Imagem 2: ela entrando no bunker, a onda enorme', 'nome': 'nora47-PRE-IMG2', 'anexar': 'SÓ a nora47-PRE-IMG1 aprovada (é uma edição dela)', 'prompt': IMG2},
  {'tipo': 'img', 'titulo': 'Imagem 3: dentro do bunker (é também a IMAGEM 1 do Take 1)', 'nome': 'nora47-IMG', 'anexar': '1º a folha (blueprint), 2º a nora47-PRE-IMG1 (só para a roupa e o cabelo)', 'prompt': IMGT},
  {'tipo': 'vid', 'titulo': 'Vídeo 1: ela corre da onda e entra no bunker', 'nome': 'nora47-PRE-A', 'duracao': '4', 'quadros': 'Modo FRAMES. Primeiro quadro: nora47-PRE-IMG1. Último quadro: nora47-PRE-IMG2. 4 s, 9:16, áudio ligado. 7 créditos.', 'prompt': VID_A},
  {'tipo': 'vid', 'titulo': 'Vídeo 2: a onda bate na porta', 'nome': 'nora47-PRE-B', 'duracao': '4', 'quadros': 'Modo FRAMES. Primeiro quadro: nora47-IMG. Último quadro: nora47-IMG (a mesma). 4 s, 9:16, áudio ligado. 7 créditos.', 'prompt': VID_B},
 ],
 'montagem': '1) nora47-PRE-A: uns 3,5 s (do começo até ela entrar no bunker).\n2) Corte seco para a nora47-PRE-B inteira (4 s: a onda bate, a porta treme, ela olha para a lente).\n3) Corte seco para o nora47-T01 (legendado), que começa no mesmo quadro.\n4) Deixe o som dos 2 vídeos (rugido, estrondo, água). Sem legenda no hook.',
 'texto_tela': '', 'edicao': ''}

c = P['central']
for sec in c['config']:
    for cp in sec['campos']:
        if cp.get('campo', '').startswith('LIVRE'):
            cp['valor'] = 'colar o texto abaixo (feito para a nora47-IMG, dentro do bunker)'; cp['copiar'] = LIVRE
        if cp.get('campo') == 'Atmosfera / mood':
            cp['valor'] = 'Íntimo e confidencial'
c['conferir'] = ('Conferir no Take 1: é a Nora (rosto, lua com as estrelinhas, trança, blazer creme e blusa branca), de costas para a porta de aço; ela fala uma vez só, em inglês, com os signos certos e "eleven eleven"; '
                 'as mãos não aparecem; a porta, a lâmpada e as paredes não se mexem; sem água, sem texto, legenda ou música. Ouça a emenda com o Take 2 do nora46.')
c['colagens'] = [{'titulo': 'só o Take 1 do nora47', 'fala': FALA, 'movimentacao': [MOV], 'takes': [0]}]
c['passos'] = [
 'Story-0311 AGORA, antes de tudo (o link está fora desde 21h10): seção Story deste painel.',
 'Imagens no Flow, nesta ordem: nora47-PRE-IMG1 (só a folha), nora47-PRE-IMG2 (só a IMG1), nora47-IMG (a folha + a IMG1). Confira: é a Nora, blazer creme, a onda atrás e o bunker à direita; na nora47-IMG, sem mãos no quadro e a porta fechada.',
 'Vídeos do hook em FRAMES: nora47-PRE-A (IMG1 → IMG2) e nora47-PRE-B (nora47-IMG → nora47-IMG). 7 créditos cada, conta grande.',
 'Central do curso: a mesma configuração do nora46, MAS com o texto LIVRE novo desta seção (é outro cenário). Cole só a fala e a linha de movimentação do Take 1. Gere: 1 take de 10 s.',
 'Agente do Flow: conversa nova, anexe só a nora47-IMG, cole o aviso de 1 prompt e, embaixo, o prompt do take (botão COPIAR do take na Central). 15 créditos, conta grande. Renomeie para nora47-T01-gancho-onda-touro-virgem-capricornio.',
 'Corte de silêncio só do nora47-T01 (nora47-T01-cortado) e legenda automática só dele (nora47-T01-legendado), no estilo do nora46.',
 'CapCut: projeto novo com o vídeo FINAL do nora46 cortado no começo do Take 2; antes dele, nora47-PRE-A + nora47-PRE-B + o Take 1, com a caixa do topo, os números e a música (seção de texto na tela).',
 'Postar hoje (03/11) às ~23h30 no Insta e no Face, ao vivo, sem localização (se atrasar, 00h30). Comentário: no Insta, comente e fixe (sem link); no Face, comente COMO A PÁGINA com o comentário do Face deste painel (já tem o link).']
a = c['agente']
a['imagem'] = 'nora47-IMG'
a['intro'] = 'Uma imagem e uma mensagem: anexe a nora47-IMG, cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take na Central; com 1 take não existe o bloco “COPIAR TUDO JUNTO”).'
a['passos'] = ['Abra uma conversa nova no agente do Flow.', 'Anexe a nora47-IMG (só ela).', 'Cole o aviso (acima).',
               'Embaixo, cole o prompt do Take 1 (botão COPIAR do take na Central).',
               'Envie. Renomeie para nora47-T01-gancho-onda-touro-virgem-capricornio. Confira o vídeo e me diga se falhou (o que saiu errado).']

st = json.loads(json.dumps(P8['story']))
st['nota'] = ('STORY NOVO (story-0311): poste AGORA, antes do nora47, no Insta e no Face (o story-0111 venceu às 21h10 e o link está fora). Imagem: a story-3110. Sem cartas no texto. '
              'Ao pôr o adesivo de link, cole o link certo de cada rede e confira na prévia. Insta (STORYIG): https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks · '
              'Face (FACE): https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks')
st.pop('ja_postado', None)
P['story'] = st

P['mapa_tela']['regras'] = ['Na nora47-IMG a faixa da legenda (Y -294, 73%) fica no tronco, abaixo do queixo; as mãos não aparecem. No hook (praia) não há legenda.',
  'Os números ficam no mesmo lugar do nora46 (para não pular na emenda): na praia ficam no céu e na onda; no bunker, na porta e na parede. Se algum cobrir o rosto ou o cabelo, mova uns 40 no X ou no Y.']

E = P['edicao_linha']
for e in E:
    if e['quando'] == '0. No começo':
        e['texto'] = 'Hook: nora47-PRE-A + nora47-PRE-B'
        e['como'] = 'nora47-PRE-A (~3,5 s, até ela entrar no bunker), corte seco, nora47-PRE-B inteira (4 s). Deixe o som dos dois. Sem legenda no hook.'
    if e['quando'] == '1. Logo depois do hook':
        e['texto'] = 'nora47-T01-legendado'
        e['como'] = 'Encostado na nora47-PRE-B e, do outro lado, no Take 2 (o vídeo do nora46). Ouça a emenda: termina em “before eleven eleven” e o Take 2 entra direto.'
    if e['quando'].startswith('2.'):
        e['how'] = None
    if e['quando'].startswith('4.'):
        e['texto'] = 'Música de sempre (“Ambient Mystical Drone”), −18 dB, só no Take 1'
        e['como'] = 'No hook fica só o som da onda (sem música). Do Take 2 em diante a música já está no vídeo do nora46.'
for e in E: e.pop('how', None)

P['pecas']['lista'] = [
 {'nome': 'nora47-PRE-IMG1', 'tipo': 'imagem (hook)', 'status': 'gerar', 'descricao': 'A praia, a onda gigante subindo atrás dela, o bunker à direita.'},
 {'nome': 'nora47-PRE-IMG2', 'tipo': 'imagem (hook)', 'status': 'gerar', 'descricao': 'Edição da IMG1: ela entrando no bunker, a onda enorme.'},
 {'nome': 'nora47-IMG', 'tipo': 'imagem 1', 'status': 'gerar', 'descricao': 'Dentro do bunker, de costas para a porta fechada (1º e último quadro do vídeo 2 e imagem do Take 1).'},
 {'nome': 'nora47-PRE-A', 'tipo': 'hook (vídeo 1)', 'status': 'gerar', 'creditos': 7, 'descricao': 'Ela corre da onda e entra no bunker (Frames, IMG1 → IMG2).'},
 {'nome': 'nora47-PRE-B', 'tipo': 'hook (vídeo 2)', 'status': 'gerar', 'creditos': 7, 'descricao': 'A onda bate na porta (Frames, nora47-IMG → nora47-IMG).'},
 {'nome': 'nora47-T01-gancho-onda-touro-virgem-capricornio', 'tipo': 'take', 'status': 'gerar', 'creditos': 15, 'descricao': '“' + FALA + '”'},
 {'nome': 'nora46-T02 a nora46-T12 (o corpo B)', 'de': 'nora46', 'tipo': 'corpo', 'status': 'reutilizar', 'descricao': 'O vídeo FINAL do nora46, exportado, a partir do Take 2. Não gere, não corte e não junte de novo.', 'onde': 'O vídeo final do nora46 que você exportou (com tudo), a partir do Take 2.'},
 {'nome': 'story-0311', 'de': 'story-3110', 'tipo': 'story', 'status': 'reutilizar', 'descricao': 'Mesma imagem do story-3110; texto e adesivo novos (sem cartas).', 'onde': 'Postar AGORA, antes do nora47.'}]
P['pecas']['decisao'] = [
 'Hook novo e “bizarro” (Vinicius Almeida: “o gancho é o mais importante”; aula de 07/09: Face entre 200 e 500 views = gancho; a Nora para em ~240 a 290).',
 'Mesmo corpo do nora46: se o resultado mudar, foi o gancho (e o Take 1). Comparar com o nora46 com ~3 h e ~24 h (3 s, 8 s e views no Face).',
 'Take 1 dentro do bunker, como no viral (a onda bate e ela começa a falar). Mesma roupa do corpo B (blazer creme) para a emenda com o estúdio não estranhar.',
 'Total: 29 créditos na conta grande (7 + 7 + 15).']

P['roteiro']['descricao_instagram'] = R['descricao_instagram']
new = 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';\n'
s = s[:m.start()] + new + s[m.end():]
s = re.sub(r'<title>.*?</title>', '<title>Painel nora47</title>', s, count=1)
open(F, 'w', encoding='utf-8').write(s)
print('ok', len(FALA.split()), 'palavras')
