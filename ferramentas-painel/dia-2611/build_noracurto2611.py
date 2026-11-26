# Painel do curto de 26/11/2026 (noracurto2611): o desafio de pausar, ~6 s, SEM fala, só no Insta às ~23h.
# O "pode montar" do aluno (26/11 ~19h00): "sem a nora falando. só ela andando rapido, em um jardim, e a pessoa tendo que pausar no pontilhado. e inves a fala,
#   algo escrito. e quando a pessoa conseguir pausar no pontilhado, aparece a msg fazendo ela ir ao story… coloca o nome como noracurto2611".
# Fontes: o desafio de pausar do Robert McKeaveney (v07 e v21: "only 1% can pause at the right time"; o tempo médio maior que o vídeo e o Insta empurrou;
#   MATERIAIS-ROBERT-MCKEAVENEY/LEIA.md); a família do ini1811 (21 visitas ao perfil, o recorde da Nora); a decisão de 25/11 17h20 (o desafio só no Insta).
# É o teste do dia de 26/11 (a regra de 16h00: 1 teste por dia). O nora81 (o falado das letras) vai às 2h.
# A imagem e o clipe no Muse, só com o blueprint (o Flow bateu o limite de imagens em 26/11). Sem fala: a Central divide os takes pela fala, então este
#   clipe vai direto no Muse, com o prompt curto de clipe sem fala (P32, exceção de 16/11).
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2611/build_noracurto2611.py
import json, copy, re, pathlib, importlib.util

R = pathlib.Path(__file__).resolve().parents[2]
s = importlib.util.spec_from_file_location('b2311', R / 'ferramentas-painel' / 'dia-2311' / 'build_dia_2311.py')
B23 = importlib.util.module_from_spec(s); s.loader.exec_module(B23)
MODELO = B23.MODELO
IG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
FB = B23.FB
assert IG.endswith('&aff=dl7zx6ks') and FB.endswith('&aff=dl7zx6ks')

NOME = 'noracurto2611'
IMG = 'noracurto2611-IMG'
CLIPE = 'noracurto2611-CLIPE'
STORY = 'story-2611-trancado'
FOLHA = 'nora-v3-blueprint'
ROUPA = 'a plain sage-green long-sleeve crew-neck top with no logo, light-wash straight jeans and plain white sneakers'
ROSTO = ('keep exactly her face, her warm medium-brown eyes, her complexion, her long black wavy hair worn loose, her small plain gold stud earrings and her thin gold '
         'chain necklace, the same woman as in every panel of the sheet; no paint, no moon, no stars and no marks on her face; do not copy the sheet layout, the labels '
         'or the white background')
FIM = ('looks exactly like a real casual iPhone photo, slight phone grain, natural colors, everything in focus, no bokeh; no glow, no sparkle, no light effect; no phone, '
       'phone stand or tripod anywhere in the image; no text and no logo anywhere; each hand has exactly five fingers; photorealistic, unretouched, vertical 9:16')
JARDIM = ('a sunny real American backyard garden in the late afternoon: a straight light-gray stone path runs across the image from the left edge to the right edge, '
          'at about 70 percent of the image height; green lawn in front of the path; behind the path, flower beds with lavender and pink roses and a plain white wooden '
          'fence; a real American flag on a short wooden pole stands in the flower bed behind the path, on the right side of the image, clearly visible; the upper 25 '
          'percent of the image is blue sky and tree tops with nothing else in it')

PROMPT_IMG = ('Generate exactly ONE photorealistic vertical 9:16 image. The attached image is the character sheet of the woman: ' + ROSTO + '. '
              'Wide RAW photo taken from a phone on a tripod about five meters away at waist height (the phone and the tripod are not visible): ' + JARDIM + '; '
              'she stands on the stone path near the LEFT edge of the image, in mid-step, walking toward the right side of the image, her body seen from the side and her '
              'face turned to the camera with a playful smile; her whole body is visible from head to feet, about one third of the image height tall; she wears ' + ROUPA +
              '; nothing else is on the path; ' + FIM)
PROMPT_STORY = ('Generate exactly ONE photorealistic vertical 9:16 image. The attached image is the character sheet of the woman: ' + ROSTO + '. '
                'Casual RAW photo taken by a friend from about one meter in front of her, at her collarbone height (no phone, phone stand or tripod visible): she stands '
                'in the same sunny American backyard garden in the late afternoon, with lavender, pink roses and a plain white wooden fence behind her and a real American '
                'flag on a short wooden pole behind her on the right side of the image; she wears ' + ROUPA + '; framed from just above her head down to her waist, her '
                'face in the upper part of the image, looking straight into the camera with a soft, warm, knowing smile and her lips closed; both hands are lowered, out of '
                'the frame; from 40 to 85 percent of the image height there is only the plain front of her sage-green top, with nothing in front of it (this area stays '
                'empty for text and a link sticker); ' + FIM)
for _t in (PROMPT_IMG, PROMPT_STORY):
    for _w in ('chest', 'skin', 'body,', 'breast', 'underwear', 'paint ', 'shining', 'glowing'):
        assert _w not in _t.lower(), _w

VID = ('Use the attached image as the first frame. Real casual 6-second video from a static camera on a tripod, steady, no zoom, no pan, no camera movement, real speed; '
       'no phone, phone stand or tripod ever appears in the frame. ACTION, starting in the very first frame: she walks briskly along the stone path from the left side of '
       'the frame to the right side, at a fast natural walking pace, her whole body always visible from head to feet; she passes the center of the frame at about 2 to 3 '
       'seconds, glancing at the camera with a playful smile, and keeps walking until she leaves the frame at the right edge at about 5 seconds; the last second shows the '
       'empty path. She never speaks and her lips stay closed in a smile. The garden, the flowers, the fence and the American flag stay exactly as in the attached image '
       'and do not move except for a light breeze. She keeps the same face, warm medium-brown eyes, loose hair, ' + ROUPA + ' the whole time; nothing appears or '
       'disappears. AUDIO: quiet garden ambience with a few birds; no music, no voice. No on-screen text, no captions.')
MUSE = ('Generate exactly ONE video clip, only one version, vertical 9:16, about 6 seconds, using the attached image as the first frame. She does not speak in this clip. '
        'Name it ' + CLIPE + '. Follow the prompt exactly as written. Prompt: ' + VID)

TOPO = 'Can you stop me\ninside the [line]? 👀'
CERTO = 'You did it ✨\nYour 2027 reading is waiting in [my story]'
INSTA_RESP = ['You got it ✨ your 2027 reading is waiting in my story 🔮', 'Haha it takes a few tries 💛 tap my photo, your reading is in my story',
              'You stopped me ✨ check my story before you go', 'So glad this found you 💫 tap my photo for your reading', 'I see you 🙏 your next step is in my story']


def montar():
    B23.ROUPA = ROUPA
    base = B23.base(NOME)
    p = {
        'enxuto': True, 'clipe_unico': True, 'ocultar_bloco_agente_imagem': True,
        'perfil': base['perfil'], 'trava_referencia': base['trava_referencia'], 'figurino': ROUPA, 'excecao_estilo': '',
        'roteiro': {'id': 'noracurto2611-DESAFIO-PAUSAR', 'titulo': 'noracurto2611 · 26/11 · o desafio de pausar (~6 s, sem fala): só no Insta, às ~23h',
                    'duracao_total': 6,
                    'descricao_instagram': ("Can you stop me inside the line? 👀 If you did, your private reading is waiting in my story 🔮\n"
                                            'Tell me how many tries it took you 👇\n#manifestation #2027 #lawofattraction #angelnumbers'),
                    'descricao_face': '(não vai ao Face: o desafio é só do Insta, decisão de 25/11; vídeo sem fala fica fora do Face)'},
        'refs': [FOLHA + ' (só ela, nas 2 imagens)'],
        'imagens': [{'rotulo': 'IMAGEM 1 · ' + IMG, 'cena': '(o prompt está na seção do Clipe, item 1)', 'anexar': 'só a ' + FOLHA}],
        'videos': [{'rotulo': 'V1', 'cena': 'Clipe único, sem fala', 'duracao': 6, 'primeiro_quadro': 'IMAGEM 1 (' + IMG + ')', 'acao': '(ver seção Clipe)', 'b_roll': '',
                    'fala': '(sem fala) no topo, o vídeo todo: ' + TOPO.replace('\n', ' ').replace('[', '').replace(']', '') +
                            ' / só nos quadros em que ela está dentro do pontilhado: ' + CERTO.replace('\n', ' ').replace('[', '').replace(']', ''),
                    'movimentacao': '(sem Central: clipe sem fala; o prompt está na seção Clipe)', 'arquivo': CLIPE}],
        'texto_tela': {'hook': TOPO, 'hook_comeca': 'o segundo 0', 'hook_termina': 'o fim (o vídeo todo)', 'hook_alt': '', 'extras': []},
        'comentario_fixado': {'insta': 'Did you get it? ✨ tap my profile picture above, your reading is waiting in my story', 'face': '(sem Face)'},
        'respostas_face': {'insta': INSTA_RESP, 'face': []},
        'story': {'ja_postado': False,
                  'nota': ('STORY NOVO (' + STORY + ', o dos campos trancados: o teste aprovado em 26/11 09h; aula 36, 1:27:06: "o que vende na oferta é você ter respostas '
                           'bloqueadas… por que não trazer isso para o criativo"). Gere a foto no Muse (só o blueprint; prompt abaixo) e ME MANDE: eu ponho as caixas no meio '
                           'da tela e devolvo em ~10 min. Poste junto com o curto, às ~23h, no Insta e no Face, ANTES de ~01h (o da cozinha vence 01h04 no Face e 01h10 no '
                           'Insta), com o adesivo de link logo abaixo das caixas. Insta (STORYIG): ' + IG + ' · Face (FACE): ' + FB),
                  'anexar': 'só a ' + FOLHA,
                  'prompt_imagem': PROMPT_STORY,
                  'textos': [{'posicao': 'Caixa 1, branca com letra preta (eu ponho)', 'texto': 'Your 2027 reading ✨'},
                             {'posicao': 'Caixa 2, branca com letra preta (eu ponho)', 'texto': 'What 2027 is holding for you: 🔒🔒🔒'},
                             {'posicao': 'Caixa 3, branca com letra preta (eu ponho)', 'texto': "What's been holding you back: 🔒🔒🔒"},
                             {'posicao': 'Caixa 4, coral com letra branca (eu ponho)', 'texto': 'Your next step: 🔒🔒🔒'}],
                  'adesivos': ['TAP TO UNLOCK 🔓', 'UNLOCK MY 2027 ✨']},
        'central': {'imagem_unica': True,
                    'conferir': ('Conferir: é a Nora v3 (sem a pintura, olhos castanhos, cabelo solto); ela anda rápido pelo caminho, da esquerda para a direita, o corpo inteiro '
                                 'sempre na tela, e sai pela direita; a bandeira dos EUA no canteiro; boca fechada; nada escrito.'),
                    'passos': ['Clipe SEM fala. A Central divide os takes pela fala, então este não passa por ela: a imagem e o clipe saem no Muse (seção Clipe).']},
        'pre_gancho': {
            'titulo_secao': 'Clipe (~6 s, sem fala)', 'duracao': 6, 'tomadas': 1, 'com_rosto': True, 'nome_video': CLIPE,
            'conceito': ('O desafio de pausar (Robert, v07 e v21: quem tenta pausar no quadro certo assiste várias vezes, o tempo médio passa a duração do vídeo e o Insta '
                         'empurra). A Nora anda rápido pelo caminho de um jardim; um pontilhado fixo no meio da tela; no topo, "Can you stop me inside the line? 👀". Só nos '
                         'quadros em que ela está dentro do pontilhado aparece "You did it ✨ Your 2027 reading is waiting in my story", com a seta para a foto do perfil. '
                         'Eu acelero, faço ela ir e voltar (vira um loop) e ponho o pontilhado, os textos e a seta. Sem fala; só no Insta.'),
            'modo': ('1) A imagem: no Muse, na conversa da Nora, anexe SÓ a ' + FOLHA + ' e cole o prompt do item 1 (1 imagem por vez; se algo vier errado, “Generate it again, '
                     'exactly the same prompt, one new version”). 2) O clipe: no Muse, anexe a imagem escolhida e cole o bloco do item 2 (1 versão só). Baixe e me mande.'),
            'etapas': [
                {'tipo': 'img', 'titulo': 'Imagem: a Nora no caminho do jardim, no canto esquerdo, corpo inteiro', 'nome': IMG, 'anexar': 'só a ' + FOLHA,
                 'quadros': ('No Muse, 1 por vez. Confira: a Nora v3 (rosto do blueprint, sem pintura, olhos castanhos, cabelo solto); de corpo inteiro, da cabeça aos pés, no '
                             'caminho de pedra, perto da BORDA ESQUERDA, andando para a direita; blusa verde-sálvia, jeans claro, tênis branco; a bandeira dos EUA no mastro do '
                             'canteiro, à direita; o alto da imagem é céu; nada escrito. Salve como ' + IMG + '.'),
                 'prompt': PROMPT_IMG},
                {'tipo': 'vid', 'titulo': 'Clipe no Muse: ela atravessa o jardim, da esquerda para a direita', 'nome': CLIPE, 'duracao': 6,
                 'quadros': ('No Muse, na conversa da Nora: anexe a ' + IMG + ' e cole o bloco abaixo, inteiro (1 versão só). Confira: ela anda rápido e atravessa a tela inteira, '
                             'da esquerda para a direita, sempre de corpo inteiro, e sai pela direita; a câmera parada; a boca fechada. Se ela não atravessar (parar no meio ou '
                             'andar para trás), peça de novo: “Generate it again, exactly as written”. Baixe e me mande.'),
                 'prompt': MUSE}],
        },
        'edicao_linha': [
            {'quando': '1. CapCut', 'texto': 'Projeto novo com o ' + CLIPE, 'como': 'Sem cortar nada (eu acelero, faço ela ir e voltar e emendo o fim no começo).'},
            {'quando': '2. Música', 'texto': 'A música de sempre (“Ambient Mystical Drone”), do segundo 0 ao fim, −12 dB', 'como': 'Não tem fala: a música pode ficar mais alta que nos falados.'},
            {'quando': '3. Exportar e me mandar até ~22h30', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
             'como': '1080×1920, nome ' + NOME + '-montado. Eu ponho o pontilhado, o texto do topo, a mensagem dos quadros certos e a seta, e devolvo o ' + NOME + '-final em ~20 min.'}],
        'pecas': {'titulo_decisao': 'Resumo', 'lista': [
            {'nome': IMG, 'tipo': 'imagem (primeiro quadro)', 'status': 'gerar', 'descricao': 'A Nora no caminho do jardim, de corpo inteiro, no canto esquerdo, a bandeira dos EUA no canteiro.'},
            {'nome': CLIPE, 'tipo': 'clipe sem fala (Muse)', 'status': 'gerar', 'descricao': '~6 s: ela atravessa o jardim andando rápido, da esquerda para a direita.'},
            {'nome': STORY, 'tipo': 'foto do story', 'status': 'gerar', 'descricao': 'A Nora no mesmo jardim, da cintura para cima, olhando para a câmera; eu ponho as caixas dos campos trancados.'}],
            'decisao': ['O QUE ESTE VÍDEO TESTA (o teste do dia de 26/11): o desafio de pausar. A medida, com ~24 h: o tempo médio contra a duração (se passar, as pessoas estão tentando '
                        'de novo), as visitas ao perfil (a régua é o ini1811, com 21), os toques no story e a fatia da Índia.',
                        'AGORA: a imagem e o clipe no Muse (só o blueprint), e a foto do story (me mande). Monte só a música no CapCut e me mande o ' + NOME + '-montado até ~22h30.',
                        'Postar só no Insta, às ~23h, ao vivo, junto com o story novo (no Insta e no Face). Antes de abrir o Insta, conferir o IP e os EUA no mylocation.org.',
                        'O nora81 (o falado das letras) vai às 2h, no Insta e no Face.']},
    }
    mt = copy.deepcopy(base['mapa_tela'])
    mt['estilos'] = [{'nome': 'Caixa do topo, o vídeo todo: ' + TOPO.replace(chr(10), ' '), 'fonte': 'Inter', 'cor': 'branca com letra preta, a palavra-chave em vermelho',
                      'tamanho': '2 linhas', 'contorno': 'fundo sólido', 'obs': 'No céu, acima dela. Eu ponho.'},
                     {'nome': 'O pontilhado e a mensagem dos quadros certos', 'fonte': 'Inter', 'cor': 'pontilhado branco; mensagem branca com preto e vermelho', 'tamanho': '—',
                      'contorno': '—', 'obs': 'O pontilhado fixo no meio do caminho; a mensagem e a seta só nos quadros em que ela está dentro. Eu ponho.'}]
    mt['regras'] = ['Eu ponho o pontilhado, os textos e a seta (P45); você monta só o clipe e a música.']
    mt['numeros'] = [dict(t='11:11✨', x=82, y=16, onde='alto à direita', cor_nome='branco', cor='#FFFFFF', tamanho=11)]
    p['mapa_tela'] = mt
    p['ordem'] = ['pecas', 'prehook', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>Painel noracurto2611 · o desafio de pausar</title>', html, count=1)
    (R / 'PAINEL-NORACURTO2611.html').write_text(html, encoding='utf-8')
    print('ok PAINEL-NORACURTO2611.html', len(html))


montar()
