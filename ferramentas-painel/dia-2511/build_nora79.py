# Painel do nora79 (25/11/2026, Insta e Face às 19h30; "pode montar" do aluno às ~17h20):
#   o corpo da maioria (o texto do nora75: o maior falado do Insta desde 10/11, 694; e o do nora76-FACE e do nora77-FACE, 7 cliques), GERADO DE NOVO
#   (a regra do Insta de 24/11), no MULTI-ÂNGULO (o vídeo do Gustavo no Muse, mentoria de 23/11, 0:40:18; o 1º teste do quadro; o "re-hook every few
#   seconds" do Robert, v10), numa cozinha clara, de regata branca e calça jeans clara larga (o aluno: "nao quero moletom mais").
#   A abertura pelo modelo do Robert (v10: "Spark a question / Use visual, verbal, text & audio hooks / Copy viral hook formats"): o ritual dito com o
#   objeto na mão (o formato mais copiado da mineração, 12 vídeos e 7 contas), com o ritual do m26 (@darius.whitmore: o açúcar na soleira da porta),
#   o "I know it sounds ridiculous…" (a pergunta "por quê?") e a caixa do topo "It works so fast, it's almost scary..." (25 de 40 vídeos). A resposta
#   (a recompensa do Robert) já está no corpo: o T07, "The doors that wouldn't open will finally open."
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2511/build_nora79.py
import json, re, copy, pathlib, importlib.util

R = pathlib.Path(__file__).resolve().parents[2]
def _mod(nome, caminho):
    s = importlib.util.spec_from_file_location(nome, R / caminho)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
B23 = _mod('b2311', 'ferramentas-painel/dia-2311/build_dia_2311.py')
B24 = _mod('b2411', 'ferramentas-painel/dia-2411/build_dia_2411.py')
FB, COMUNS, MODELO, VOZ, VC = B23.FB, B23.COMUNS, B23.MODELO, B23.VOZ, B23.VC
assert FB.endswith('&aff=dl7zx6ks')
NN = 'nora79'
ROSTO = B23.ROSTO.replace('her face with clean natural skin', 'her face with clean natural skin, her light hazel-green eyes with a golden ring around the pupil '
                          '(exactly the same eye color in every clip, never brown or dark)')
ROUPA = 'her plain white ribbed tank top and light-wash wide-leg jeans'
IMG_REF = B23.IMG_B   # d2311-sofa-IMG-B: a Nora sem a pintura (a referência do rosto)
FLAG = 'a real American flag in a simple wooden picture frame with glass, about the size of a small poster, hanging on the light kitchen wall behind her, high on the left side, not touching her head'

# ---------- a fala: o corpo da maioria (B23.FALA), o T01 novo e a data de sexta ----------
T01 = "Pour a little sugar on your doorstep tonight. I know it sounds ridiculous, but you'll thank me forever."
FALA = [T01] + list(B23.FALA[1:])
FALA[2] = FALA[2].replace('Wednesday, November twenty-fifth', 'Friday, November twenty-seventh')
assert 'Friday, November twenty-seventh' in FALA[2]
CTA_FACE = B24.CTA_FACE77
SUF = ['acucar', 'mulher-deitada', 'datas', 'fe', 'aviso', 'arcanjo', 'correntes', 'sete-minutos', 'selos-amen', 'amanha', 'alinhada', 'leitura', 'cta-story']
N = len(FALA)
NOMES = [f'd2511-cozinha-T{i + 1:02d}-{SUF[i]}' for i in range(N)]
NOME_CTA = 'd2511-cozinha-T14-FACE-cta-comentario'
IMGS = [f'd2511-cozinha-IMG-T{i + 1:02d}' for i in range(N)]

# o ângulo e o objeto de cada take (o vídeo do Gustavo: a mesma pessoa, roupa e cozinha; muda a câmera e o objeto da frase na frente)
ANG = [None,
       None,  # T02 = a imagem base (IMG-T02)
       'the camera moves a little to her left and closer, framing her from the shoulders up; on the wall beside her hangs a plain paper wall calendar with no readable writing',
       'the camera is lower, at counter height, looking slightly up at her; on the counter in front of her stands a lit white candle in a clear glass jar',
       'a close-up of her face and shoulders from the front, with the light kitchen wall behind her',
       'the camera moves about 30 degrees to her right; on the windowsill behind her stands a small white statue of an angel holding a sword',
       'a wider shot from farther back that shows the kitchen back door behind her, slightly open with daylight coming in; on the counter lies a ring of old brass keys',
       'the camera is a little higher, looking slightly down at her; on the counter in front of her sits a small white kitchen timer',
       'framed from the waist up from the front; she holds her phone in one hand at shoulder height, the screen facing away from the camera',
       'the camera moves to her left and a little farther back; on the wall behind her hangs a round white wall clock with the hands at ten o\'clock',
       'the camera is at counter height, from her right; on the counter sits a white bowl of fresh oranges',
       'framed from the waist up from the front; she holds her phone at collarbone height, the screen facing away from the camera',
       'a close-up from the front, framed from the shoulders up, with her hands out of the frame']
GESTO = ['she keeps the jar tilted and a thin stream of white sugar keeps falling toward the threshold below the frame while she talks',
         'she rests both hands on the counter with a calm, knowing look, as if she can see the woman she is talking about',
         'she leans in slightly toward the lens with a serious, knowing look',
         'her eyebrows lift with a hopeful, bright look and a small smile grows',
         'she holds a calm, serious look and gives one slow nod',
         'she holds a serious look in the first half and in the closing half a relieved smile appears',
         'she holds a calm, confident look and nods slowly',
         'she leans in slightly with an encouraging look',
         'she gives two small nods with a warm, encouraging look, holding the phone still',
         'she holds a warm, hopeful smile',
         'she holds a calm, serious, caring look',
         'she holds a warm, knowing look and gives one small nod, holding the phone still',
         'she raises one hand into the frame, points down toward the lower left corner with a warm, encouraging smile, then looks back at the lens']
GESTO_CTA = B24.GESTO_CTA_FACE
# 25/11 22h (revisão a pedido do aluno): os títulos das imagens em português (os prompts seguem em inglês)
ANG_PT = ['no vão da porta da cozinha, despejando açúcar na soleira', 'atrás do balcão, de frente (a imagem base dos outros takes)',
          'mais perto, um pouco à esquerda, com um calendário de papel na parede', 'de baixo, na altura do balcão, com uma vela acesa num pote de vidro',
          'close no rosto e nos ombros, de frente', 'uns 30° à direita, com uma estatueta branca de anjo com espada na janela',
          'mais aberto, com a porta dos fundos entreaberta e um molho de chaves antigas no balcão', 'de cima, com um timer de cozinha branco no balcão',
          'da cintura para cima, com o celular na mão na altura do ombro', 'à esquerda e mais longe, com um relógio de parede marcando 10h',
          'na altura do balcão, pela direita, com uma tigela de laranjas', 'da cintura para cima, com o celular na altura da clavícula',
          'close de frente, do ombro para cima, sem as mãos']
assert len(ANG_PT) == N
assert len(ANG) == len(GESTO) == len(SUF) == N

_FIM = ('looks exactly like a real casual iPhone photo, slight phone grain, natural colors, everything in focus, no bokeh; no glow, no sparkle, no light effect; '
        'no phone stand or tripod anywhere in the image; no text and no logo anywhere; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16')
PROMPT_T01 = ('Use the attached image as the reference for the woman only: keep exactly her face, her eyes, her complexion and her long black wavy hair worn loose, '
              'with no marks on her face, small plain gold stud earrings and a thin gold chain necklace. New photo: RAW photo taken in the late afternoon from about one meter '
              'in front of her, at collarbone height: she stands in the open back doorway of a bright, simple American kitchen with white cabinets and a light countertop, '
              f'soft daylight; she wears a plain white ribbed tank top and light-wash wide-leg jeans; {FLAG}; framed from mid-thigh up, looking straight into the camera '
              'with a calm, knowing look and her lips closed; she holds a clear glass sugar jar in both hands, tilted down, and a thin stream of white sugar falls from it '
              'toward the door threshold below the frame; ' + _FIM)
PROMPT_T02 = ('The attached image is the approved photo. Keep exactly the same woman, the same face, the same loose hair, the same white ribbed tank top and light-wash '
              'jeans, the same kitchen, the same framed American flag on the wall and the same light. Change only this: the sugar jar is gone; she now stands behind the '
              'kitchen counter facing the camera, framed from the waist up, both hands resting on the counter; her phone lies face down on the counter in front of her; '
              'the framed flag stays on the wall behind her, high on the left side, not touching her head; ' + _FIM)


def prompt_img(i):
    return ('The attached image is the approved photo. Keep exactly the same woman, the same face, the same loose hair, the same white ribbed tank top and light-wash '
            'jeans, the same kitchen and the same light; the framed American flag stays on its wall (visible only if this angle shows that wall). Change only the camera '
            f'position and one object: {ANG[i]}; she looks straight into the camera with a calm look and her lips closed; ' + _FIM)


PROMPTS_IMG = [PROMPT_T01, PROMPT_T02] + [prompt_img(i) for i in range(2, N)]
PROMPT_STORY = ('The attached image is the approved photo. Keep exactly the same woman, the same face, the same loose hair, the same white ribbed tank top and '
                'light-wash jeans, the same kitchen and the same light. Change only this: she sits on a stool at the kitchen counter holding a white mug in both hands, '
                'smiling softly into the camera, framed from the waist up; the framed American flag is visible on the wall behind her; the upper third of the image is '
                'plain light wall with nothing in it; ' + _FIM)
for _t in PROMPTS_IMG + [PROMPT_STORY]:
    for _w in ('chest', 'skin', 'body', 'breast', 'underwear', 'wine', 'paint', 'cleavage'):
        assert _w not in _t.lower(), _w


def mov(g):
    return ('Throughout the whole 10 seconds the camera stays static with exactly the framing of the reference image; she stands in the kitchen exactly as in the '
            f'reference image; {g}; her eyes stay on the lens; from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; '
            'no zoom and no cuts, each hand has exactly five fingers.')


def prompt_take(txt, g, arq, clip, total):
    voz = VOZ.replace('[Voice and Audio Instructions]', '').strip()
    seg = max(3, round(len(txt.split()) / 2.7))
    return ('Create a single continuous 10-second video clip using the supplied reference image as the first frame. The same woman from the image stands in her '
            'bright kitchen and speaks directly to the camera.\n\n'
            'SPOKEN DIALOGUE (she says exactly this, once, in this order, with nothing added): "' + txt + '"\n\n'
            'VOICE CHARACTERISTICS (LOCKED):\n' + voz + '\n\n'
            + VC.NORA.replace('{clip}', str(clip)).replace('{total}', str(total)) + '\n\n'
            'SAME VOICE AS THE OTHER CLIPS: use exactly the same voice as the other clips of this video already generated in this conversation (same timbre, pitch, '
            'accent, pace, volume, energy and microphone sound).\n\n'
            f'VOICE PACING: medium pace (155 to 180 words per minute), about {seg} seconds of speech; when she finishes the last word she closes her lips and stays '
            'silent with a calm expression until the clip ends.\n\n'
            'MOVEMENT: ' + mov(g) + '\n\n'
            'VISUAL: realistic casual phone video, soft natural daylight in a kitchen, natural texture with visible pores, slight phone grain, everything in focus, '
            'no bokeh, no filter.\n\nCAMERA: static, exactly the framing of the reference image, no zoom, no cuts, no reframing.\n\n'
            'AUDIO: only her voice and quiet kitchen sound; no music, no other voices, no sound effects.\n\n'
            f'CONTINUITY: {ROSTO}, {ROUPA}, the objects in the image, the kitchen and the framed American flag stay exactly as in the reference image; no paint, '
            'moon, stars or marks appear on her face; no person or text appears; each hand has exactly five fingers; no on-screen text or captions.\n\n'
            'Do not add, remove, repeat, rewrite or paraphrase any spoken words.'
            f'\n\nName this clip exactly {arq}, so the downloaded file already has this name.')


# ---------- conferências ----------
EXTRA = B24.EXTRA | {('the', 'counter'), ('on', 'the'), ('the', 'frame'), ('her', 'phone'), ('the', 'phone'), ('toward', 'the')}
for i, (f, g) in enumerate(list(zip(FALA, GESTO)) + [(CTA_FACE, GESTO_CTA)]):
    assert len(f.split()) <= 22, (i + 1, len(f.split()), f)
    fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", mov(g).lower())
    sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS - EXTRA
    assert not sobra, (i + 1, sobra)
    for w in ('link', 'free', 'card', 'tarot', 'private'):
        assert w not in fw, (i + 1, w)
PALAVRAS = sum(len(f.split()) for f in FALA)
PROMPTS = [prompt_take(FALA[i], GESTO[i], NOMES[i], i + 1, N) for i in range(N)]
PROMPT_CTA = prompt_take(CTA_FACE, GESTO_CTA, NOME_CTA, N, N)
for p in PROMPTS + [PROMPT_CTA]:
    assert 'sofa' not in p.lower() and 'cinnamon' not in p.lower()

INSTA = list(range(1, 14))                 # T01 a T13
FACE = [1, 2, 3, 4, 6, 7, 11, 14]          # sem o T05 (ameaça), T08 (7 minutos), T09 (selos), T10 (amanhã às 10), T12 e T13 (CTA do story)


def painel():
    P = B23.base('nora79')
    P['figurino'] = ROUPA
    P['imagens_titulo'] = 'As imagens de cada take (uma por take: o mesmo cômodo e a mesma roupa, outro ângulo e o objeto da frase)'
    P['refs'] = [f'{IMGS[i]} no T{i + 1:02d}' for i in range(N)] + [f'{IMGS[1]} no T14 (só Face)']
    P['imagens'] = [{'rotulo': f'IMAGEM {i + 1} · {IMGS[i]}', 'cena': 'gerada no Flow (seção das imagens)', 'anexar': f'a {IMGS[i]}'} for i in range(N)]
    etapas = [{'titulo': 'T01: no vão da porta da cozinha, despejando açúcar na soleira', 'nome': IMGS[0], 'tipo': 'img',
               'anexar': f'só a {IMG_REF} (a Nora sem a pintura, de camiseta preta: é a referência do rosto)',
               'quadros': (f'x4, 0 crédito. Escolha a que tiver: a Nora sem a lua e sem as estrelinhas; regata branca e calça jeans clara larga; o pote de açúcar inclinado; '
                           f'a bandeira no quadro na parede, sem encostar na cabeça; 5 dedos em cada mão. Se o Flow recusar a regata, troque no prompt "white ribbed tank top" '
                           f'por "white short-sleeve fitted t-shirt". Renomeie para {IMGS[0]}.'),
               'prompt': PROMPT_T01},
              {'titulo': 'T02: atrás do balcão, de frente (a imagem base dos outros takes)', 'nome': IMGS[1], 'tipo': 'img', 'anexar': f'só a {IMGS[0]} que você escolheu',
               'quadros': f'x4, 0 crédito. Escolha a que tiver o mesmo rosto, a mesma roupa, o celular virado no balcão e a bandeira no quadro. Renomeie para {IMGS[1]}.',
               'prompt': PROMPT_T02}]
    for i in range(2, N):
        etapas.append({'titulo': f'T{i + 1:02d}: ' + ANG_PT[i], 'nome': IMGS[i], 'tipo': 'img', 'anexar': f'só a {IMGS[1]}',
                       'quadros': f'x4, 0 crédito. Escolha a que tiver o mesmo rosto e a mesma roupa, no ângulo novo. Renomeie para {IMGS[i]}.', 'prompt': PROMPTS_IMG[i]})
    etapas.append({'titulo': 'A foto nova do story (para variar, o seu pedido)', 'nome': 'd2511-story-cozinha', 'tipo': 'img', 'anexar': f'só a {IMGS[1]}',
                   'quadros': 'x4, 0 crédito. Me mande as 4 aqui; eu escolho e ponho o texto do story, e você só põe o adesivo do link.', 'prompt': PROMPT_STORY})
    B24.imagens_secao(P, f'As {N + 1} imagens (Flow, antes dos takes; o T14 do Face usa a do T02)',
                      ('O multi-ângulo do vídeo do Gustavo no Muse: a mesma Nora, a mesma roupa e a mesma cozinha; a cada take a câmera muda e aparece o objeto da frase. '
                       'A 1ª imagem parte da referência do rosto; a do T02 parte da 1ª; todas as outras partem da do T02.'), etapas)
    P['roteiro'] = {
        'id': 'nora79-MULTIANGULO-COZINHA-2511',
        'titulo': 'nora79 · Insta e Face assim que ficar pronto, até ~0h30 de 26/11 (a janela da noite; era 19h30) · o corpo da maioria, gerado de novo, no multi-ângulo, de regata branca e jeans, com o açúcar na soleira',
        'duracao_total': 95,
        'descricao_instagram': ("Pour a little sugar on your doorstep tonight 🍯 Your private reading is waiting in my story 🔮\n"
                                "Type OPEN if you're doing this tonight 👇\n"
                                '#manifestation #lawofattraction #2027 #abundance'),
        'descricao_face': ("Pour a little sugar on your doorstep tonight 🍯 Your reading is waiting in the first comment 🔮\n"
                           '#manifestation #lawofattraction #2027'),
    }
    P['videos'] = ([{'rotulo': f'T{i + 1:02d}', 'cena': SUF[i], 'duracao': 10, 'primeiro_quadro': f'IMAGEM {i + 1} ({IMGS[i]})', 'acao': '', 'b_roll': '',
                     'fala': FALA[i], 'movimentacao': mov(GESTO[i]), 'arquivo': NOMES[i]} for i in range(N)]
                   + [{'rotulo': 'T14 (só Face)', 'cena': 'o CTA para o comentário (no lugar do T12 e do T13 no Face)', 'duracao': 10,
                       'primeiro_quadro': f'IMAGEM 2 ({IMGS[1]})', 'acao': '', 'b_roll': '', 'fala': CTA_FACE, 'movimentacao': mov(GESTO_CTA), 'arquivo': NOME_CTA}])
    P['texto_tela'] = {'hook': "It works so fast, [it's almost scary]...", 'hook_comeca': '0,0 s', 'hook_termina': 'fim da 1ª frase (~3 s)', 'hook_alt': '', 'extras': []}
    B23.mapa(P)
    P['mapa_tela']['numeros'] = [{'t': '11:11✨', 'x': 82, 'y': 16, 'onde': 'alto à direita (à esquerda fica o quadro da bandeira)', 'cor_nome': 'branco', 'cor': '#FFFFFF', 'tamanho': 11}]
    P['comentario_fixado'] = {'insta': 'Did you do it tonight? 🍯 tap my profile picture above, your reading is waiting in my story',
                              'face': 'Every door is about to open for you ✨ your reading is waiting for you here 👉 ' + FB}
    assert P['comentario_fixado']['face'].endswith('&aff=dl7zx6ks')
    P['ocultar_cenas'] = True
    ct = P['central']
    ct['config'] = []
    ct['colagens'] = [{'titulo': f'T{i + 1:02d}', 'fala': FALA[i], 'movimentacao': [mov(GESTO[i])], 'takes': [i]} for i in range(N)]
    ct['conferir'] = 'Conferir cada take: a Nora sem a pintura, de regata branca e jeans claro, na cozinha; ela fala uma vez só, diz as datas por extenso e fecha a boca no fim.'
    passos = ['No Muse, NA MESMA CONVERSA da Nora (a do nora75 ao nora78: a voz). Um clipe por mensagem, cada um com a SUA imagem anexada (é isso que dá o ângulo novo). '
              'Os prompts já são completos (a voz travada, a consistência de voz, a movimentação e a continuidade): a Central não entra. Comece pelo corpo (T02 a T13), '
              'depois o T01 e por último o T14 do Face.']
    for i in list(range(1, N)) + [0]:
        passos.append(f'T{i + 1:02d}: anexe a {IMGS[i]} e cole o prompt. Salve como {NOMES[i]}. PROMPT: ' + PROMPTS[i])
    passos.append(f'T14 (só do Face, o CTA para o comentário): anexe a {IMGS[1]} e cole o prompt. Salve como {NOME_CTA}. PROMPT: ' + PROMPT_CTA)
    passos.append('Se algum clipe baixar com nome aleatório, ouça o começo e renomeie pela frase: '
                  + ' · '.join(f'“{" ".join(FALA[i].split()[:5])}…” → {NOMES[i]}' for i in range(N))
                  + f' · “That\'s why I left you…” → {NOME_CTA} (o do Face; o do Insta, o T12, começa em “That\'s why I left a quick…”).')
    passos.append('Confira cada take: sem a lua e sem as estrelinhas; a regata branca e o jeans; ela fala uma vez só e fecha a boca no fim; a voz igual à dos outros. '
                  'Se o Muse recusar: “Generate it again, exactly as written.” Se a voz sair diferente, gere de novo pedindo “exactly the same voice as the other clips of this video”.')
    ct['agente'] = {'titulo': f'No Muse: os {N + 1} prompts, um por mensagem, cada um com a sua imagem (sem a Central)', 'imagem': 'a imagem de cada take',
                    'intro': f'{N + 1} clipes no Muse ({N} do Insta + 1 só do Face).', 'aviso_tag': 'não precisa de aviso: os prompts estão no passo a passo, um por take',
                    'aviso': 'Sem aviso: cada prompt abaixo já é completo.', 'passos': passos}
    P['silencio'] = {
        'intro': (f'Arraste na “M2M FusionZ” os {N + 1} takes de uma vez (T01 a T14), sem separar nada. A ferramenta junta pela ordem do nome: o T14 (só do Face) fica no fim. '
                  '“Zoom nos cortes” = DESLIGADO.'),
        'nome': 'nora79-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'T01 a T14 (o T14 é o do Face)',
        'depois': ['Suba os 14 e espere a Prévia.', 'Confira a primeira palavra do T01 (“Pour a little sugar…”) e a última do T14 (“…get your reading.”).',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', 'Clique em Cortar e baixar e salve como nora79-cortado.'],
    }
    P['edicao_linha'] = [
        {'quando': 'O que vai em cada vídeo', 'texto': 'Você monta 1 arquivo só, com os 14 takes. Os 2 vídeos (Insta e Face) eu separo aqui.',
         'como': ('INSTA (nora79-final): T01 ao T13. FACE (nora79-final-FACE): T01, T02, T03, T04 (eu tiro o “money”), T06, T07, T11 + T14 (o comentário). '
                  'Ficam fora do Face: o T05 (a ameaça), o T08 (os 7 minutos e o “send to yourself”), o T09 (os selos e o amen), o T10 (“amanhã às 10”), o T12 e o T13 (o CTA do story).')},
        {'quando': 'A. Antes de tudo', 'texto': 'Projeto novo no CapCut com o nora79-cortado', 'como': 'Começa direto no T01, sem hook.'},
        {'quando': '1. Do começo ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB, do 1º ao último quadro', 'como': 'Começa no 1º quadro.'},
        {'quando': '2. Exportar e me mandar até ~23h45', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': '1080×1920, nome nora79-montado (acima de 30 MB, link do Drive). Eu devolvo em ~20 min o nora79-final (Insta) e o nora79-final-FACE.'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': ([{'nome': IMGS[i], 'tipo': 'imagem', 'status': 'gerar', 'onde': 'No Flow (x4, 0 crédito).', 'descricao': ANG_PT[i]} for i in range(N)]
                  + [{'nome': NOMES[i], 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{FALA[i]}”'} for i in range(N)]
                  + [{'nome': NOME_CTA, 'tipo': 'take do Face', 'status': 'gerar', 'descricao': f'“{CTA_FACE}”'}]),
        'decisao': [
            'O QUE ESTE VÍDEO TESTA: o multi-ângulo (o 1º do quadro de testes) contra o mesmo corpo num ângulo só (o nora75, 694, e o nora77, 122). Medida com ~24 h: a '
            'retenção aos 3 e aos 10 s, o tempo médio, a curva (pelo Robert: queda no gancho, no meio ou no fim) e as visitas ao perfil. A abertura também muda (a canela cansou).',
            f'A abertura pelo modelo do Robert: o ritual dito com o objeto na mão (o formato mais copiado), o açúcar na soleira (o m26), a pergunta “por quê?” e a caixa '
            f'“It works so fast, it\'s almost scary...”; a resposta vem no T07 (“The doors that wouldn\'t open will finally open.”). {N} takes ({PALAVRAS} palavras) + 1 do Face = {N + 1} clipes; {N + 1} imagens no Flow (com a do story).',
            'Só 1 no Insta hoje (a sua decisão: o teste do volume). Insta e Face assim que ficar pronto, até ~0h30 (a janela da noite, sem Índia; era 19h30, depois ~21h). O story novo vai junto, no mesmo horário nas duas redes.',
        ],
    }
    P['story'] = {'ja_postado': False, 'nota': ('Story novo hoje à noite, no Insta e no Face no MESMO horário (para vencerem juntos): a foto nova (a última imagem da seção das imagens); '
                                                'me mande as 4, eu ponho o texto e devolvo; você põe o adesivo “TAP TO CONTINUE 🎁” com o link STORYIG no Insta e o FACE no Face.')}
    P['ordem'] = ['pecas', 'prehook', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    txt = json.dumps(P, ensure_ascii=False)
    for velho in ('November twenty-fifth', 'moletom', 'sweatshirt', 'sofa-IMG-A', '01h15'):
        assert velho not in txt, velho
    return P


if __name__ == '__main__':
    P = painel()
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>Painel nora79 · o multi-ângulo na cozinha · 25/11</title>', html, count=1)
    (R / 'PAINEL-NORA79.html').write_text(html, encoding='utf-8')
    print('ok', N, 'takes,', PALAVRAS, 'palavras,', len(html), 'bytes')
