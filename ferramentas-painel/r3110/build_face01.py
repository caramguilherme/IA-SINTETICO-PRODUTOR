# 31/10/2026: painel do face01, o 1º teste SÓ do Facebook (fora da numeração noraNN, pedido do aluno).
# Formato do vídeo da 1ª venda da Mary (seção 42 de BIBLIOTECA-VIDEOS-VIRAIS.md): texto longo na tela sobre um clipe calmo
# (a Nora no carro, de olhos fechados), com o anjo da guarda no lugar da senhora falecida (P15) e sem "before it disappears" (P42).
# Base: PAINEL-NORA45.html (clipe único sem fala). Uso: python3 build_face01.py <pasta do repositório>
import re, json, copy, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

def ler(nome):
    s = open(f'{BASE}/{nome}', encoding='utf-8').read()
    return json.loads(re.search(r'const PACOTE = (\{.*?\});\n', s, re.S).group(1))

def gravar(nome, titulo, p):
    m = open(f'{BASE}/PAINEL-MODELO.html', encoding='utf-8').read()
    assert m.count('const PACOTE = null;') == 1 and 'pk.ordem' in m
    m = m.replace('<title>Painel de Produção</title>', f'<title>{titulo}</title>')
    m = m.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    open(f'{BASE}/{nome}', 'w', encoding='utf-8').write(m)

P45, P40 = ler('PAINEL-NORA45.html'), ler('PAINEL-NORA40.html')

TEXTO = ('READ THIS BEFORE YOU SCROLL.\n\n'
         'YOUR GUARDIAN ANGEL HAS BEEN TRYING TO GET YOUR ATTENTION ALL WEEK.\n\n'
         "THERE'S SOMETHING LEFT FOR YOU THAT YOU STILL HAVEN'T RECEIVED.\n\n"
         "A BLESSING, A PROTECTION, SOMETHING THAT WAS ALWAYS MEANT FOR YOU AND CAN STILL REACH YOU TODAY, BEFORE THE 11:11 PORTAL OPENS.\n\n"
         'IT ONLY ARRIVES WHEN YOU CLAIM THIS ENERGY AS YOUR OWN.\n\n'
         "TO DISCOVER WHAT IT IS, TAP MY PHOTO AND OPEN MY STORY: PICK 3 CARDS AND SEE WHAT'S COMING TO YOU.\n\n"
         'THEN SEND THIS TO YOURSELF AND COMMENT "222" TO STRENGTHEN IT.')
for proib in ('DISAPPEAR', 'PASSED AWAY', 'DIED', 'GUARANTEE', 'MIRACLE', 'LINK'):
    assert proib not in TEXTO, proib

FIG = ('casual and cozy; a soft oatmeal-beige chunky-knit crew-neck sweater, matte, no print, logo or shine. Fixed accessories, always visible: the long gold '
       'star-and-moon drop earrings, the long thin gold chain with the small gold Venus-symbol pendant over the sweater and the gold face gems from the reference '
       'sheet; no hat, no sunglasses, no other jewelry, turban, cape or costume')
CENA = ('generate a NEW photo from the attached character sheet only (do not edit any other image). A vertical 9:16 photo taken in late afternoon inside a parked '
  'car in a quiet American parking lot in autumn, as if a friend sitting in the passenger seat took it with a phone. She sits in the driver\'s seat, her body facing '
  'the windshield, her head resting lightly against the headrest and turned a little toward the camera in a soft three-quarter view, her EYES CLOSED, lips gently '
  'closed in a faint, peaceful smile, as if praying or listening to something only she can hear. CAMERA: a phone held at the height of her eyes, about 60 cm from her, '
  'from the passenger seat, level, no tilt. FRAMING, in percent of the image height from the top: from 0 to 18 percent the car roof lining and the top of the '
  'windshield; the top of her head is at about 20 percent, her closed eyes at about 33 percent, her chin at about 45 percent; her shoulders and the top of the sweater '
  'fill the bottom of the frame down to 100 percent; her hands, the steering wheel and the dashboard are NOT in the frame. BACKGROUND (softly out of focus, through the '
  'windshield and the driver\'s window): a parking lot with a few parked cars and trees with orange and golden autumn leaves; no readable signs, plates, logos or text. '
  'LIGHT: soft, warm, low golden-hour light coming through the windshield and falling on her face; the car interior is dim, the whole image is warm, slightly dark and '
  'low in contrast, with a little natural phone grain. DO NOT INCLUDE: other people, pets, a phone, a cap, sunglasses, a seatbelt across her face, a rear-view mirror '
  'covering her face, text, captions, watermarks, logos or a date stamp. Do not rejuvenate or smooth her face.')
CLIPE = ('Create a single continuous 8-second video clip that opens exactly on the supplied first frame and ends exactly on the supplied last frame (the same image), '
  'vertical 9:16, so the clip loops seamlessly. Handheld smartphone camera about 60 cm from the woman, from the passenger seat, at the height of her eyes, only a tiny '
  'natural sway, no zoom, no cuts, no reframing.\n\n'
  'THE MAIN EVENT: the woman sits in the driver\'s seat of a parked car in golden afternoon light, eyes closed, completely calm, as if praying or listening. Nothing '
  'dramatic happens: it is a quiet, peaceful moment. She never speaks.\n\n'
  'SECOND BY SECOND (something small moves in EVERY second):\n'
  '0.0 to 2.0 s: she takes one slow, deep breath in; her shoulders rise very slightly; outside the windshield a few golden leaves start drifting down.\n'
  '2.0 to 4.0 s: she breathes out slowly; her faint smile grows a little; one thin strand of her hair moves gently in the air from the car vent.\n'
  '4.0 to 6.0 s: she tilts her head a few degrees toward the warm light and back; the leaves keep drifting down outside.\n'
  '6.0 to 8.0 s: she settles back into exactly the starting pose, eyes closed, faint peaceful smile, as in the supplied frame.\n\n'
  'WHAT MUST NOT HAPPEN: she does not open her eyes and does not speak or mouth any words (her lips stay closed for the whole clip); her hands never come into the '
  'frame; no other person, animal or object appears or disappears; the parked cars outside do not drive away; the light does not flicker; no text appears anywhere.\n\n'
  'VISUAL: she is the same woman as in the supplied frame; realistic natural physics, no morphing, no glow, no magic effects. No added text, no logos.\n\n'
  'AUDIO: quiet car interior ambience only, with a soft hum and a faint breeze outside. No music, no voice, no added sound effects.')

LEITURA = ('31/10/2026: a leitura completa de LEIA-TUDO-ANTES.md foi feita hoje, das ~00h40 às ~01h15, nesta sessão (registro no roteiro do nora46). Para este '
           'painel li de novo: a seção 42 de BIBLIOTECA-VIDEOS-VIRAIS.md (o vídeo da Mary, escrita hoje), as regras P15 e P42 do CLAUDE.md, as lições de clipe '
           'único e de texto na tela (LICOES-FLOW-E-PROMPTS.md) e o pacote do painel do nora45 (clipe único sem fala).')

p = {k: copy.deepcopy(P45[k]) for k in ('perfil', 'trava_referencia', 'excecao_estilo')}
p['figurino'] = FIG
p['ocultar_bloco_agente_imagem'] = True
p['clipe_unico'] = True
p['roteiro'] = {
  'id': 'face01-TEXTO-LONGO-CARRO-ANJO-DA-GUARDA',
  'titulo': 'face01 · teste só do Facebook: texto longo na tela, a Nora no carro (o formato da 1ª venda da Mary)',
  'dor': 'a bênção que ainda não chegou (Manifestation, predestinação positiva)',
  'formato': 'Texto longo na tela, sem fala, sobre um clipe calmo de 8 s que se repete (a Nora no carro, de olhos fechados)',
  'molde_hook': 'o vídeo da 1ª venda da Mary (seção 42 de BIBLIOTECA-VIDEOS-VIRAIS.md), com o anjo da guarda no lugar da senhora falecida (P15) e sem "before it disappears" (P42)',
  'duracao_total': 8,
  'descricao_instagram': "Read this before you scroll. Your guardian angel left something for you. 🙏✨\nTap my photo, open my story and pick your 3 cards. Comment 222.\n#manifestation #1111portal #guardianangel",
  'legenda_aviso': '📘 SÓ NO FACEBOOK. Não poste no Insta. Ao vivo (nunca agendar), antes das 17h. Me diga a que horas postou (o face02 vai na metade do intervalo até as 17h).',
  'leitura_registro': LEITURA}
p['refs'] = ['Blueprint da Nora v2 (só ele) na face01-IMG']
p['imagens'] = [{'rotulo': 'IMAGEM 1 · face01-IMG · APROVADA: a 4ª das 4', 'cena': CENA, 'anexar': 'SÓ o blueprint da Nora v2 (a folha de consistência). Nenhuma outra imagem.'}]
p['videos'] = [{'rotulo': 'V1', 'cena': 'Clipe único · texto longo na tela (sem fala)', 'duracao': 8, 'primeiro_quadro': 'IMAGEM 1', 'acao': '(ver seção Clipe)', 'b_roll': '',
                'fala': '(sem fala) texto na tela: ' + TEXTO.replace('\n\n', ' '), 'movimentacao': '(sem Central: o prompt do clipe está na seção Clipe)', 'arquivo': 'face01-CLIPE'}]
p['texto_tela'] = {'hook': TEXTO, 'hook_comeca': 'do segundo 0', 'hook_termina': 'o fim do clipe', 'hook_alt': '', 'extras': []}
p['comentario_fixado'] = {'insta': '— (este vídeo é só do Facebook: não vai no Insta)',
  'face': "Your guardian angel left something for you. ✨ Tap my profile picture, open my Story and pick your 3 cards to see what's coming to you. Comment 222 to claim it 🙏"}
p['pre_gancho'] = {'titulo_secao': 'Clipe (8 s, sem fala, Frames)', 'duracao': 8, 'tomadas': 1, 'com_rosto': True, 'nome_video': 'face01-CLIPE',
  'conceito': 'O formato do vídeo que deu a 1ª venda da Mary: um clipe calmo que se repete (a Nora no carro, de olhos fechados, respirando) com um texto longo por cima, para ler.',
  'modo': 'A face01-IMG já está aprovada (a 4ª das 4). Um vídeo só, em FRAMES: primeiro E último quadro = face01-IMG (assim ele repete sem pulo). 8 s, 9:16, áudio ligado. 12 créditos (conta de 41: 41 → 29).',
  'etapas': [{'tipo': 'vid', 'titulo': 'Clipe: ela respira de olhos fechados no carro', 'nome': 'face01-CLIPE', 'duracao': 8,
              'quadros': 'Modo FRAMES. Primeiro quadro: face01-IMG. Último quadro: face01-IMG (a mesma). 8 s, 9:16, áudio ligado.', 'prompt': CLIPE}],
  'montagem': '1) Use o clipe inteiro (8 s).\n2) Por cima do clipe, uma camada preta a 35% (ou Ajustar → Brilho −25), para o texto branco ler bem.\n3) O texto longo (seção de texto na tela), o clipe todo.\n4) Som do clipe ligado e a música de sempre (“Ambient Mystical Drone”) a 0 dB. Sem legenda automática (ela não fala) e sem números fixos.\n5) Se ela abrir os olhos ou mexer a boca, refaça uma vez; se falhar de novo, me chame.',
  'texto_tela': '', 'edicao': ''}
c = copy.deepcopy(P45['central'])
c['conferir'] = 'Conferir: é a Nora da face01-IMG; ela fica de olhos fechados e de boca fechada o clipe todo; as mãos não aparecem; nada surge nem some; o último quadro volta igual ao primeiro.'
c['passos'] = [
  'Teste SÓ do Facebook (não posta no Insta). Vídeo de 8 s sem fala: não usa a Central do curso nem o agente. Conta de 41.',
  'face01-IMG APROVADA (31/10 ~11h, a 4ª das 4: cabeça reta, olhos fechados, meio sorriso, cabelo solto, as estrelinhas na bochecha, árvores de outono pelo para-brisa).',
  'Agora: o clipe (seção “Clipe”) em FRAMES, primeiro e último quadro = face01-IMG, 8 s, 9:16, áudio ligado. Renomeie para face01-CLIPE. 12 créditos (conta de 41 → 29).',
  'CapCut: a camada escura, o texto longo e a música (seção de texto na tela). Sem legenda automática e sem números fixos.',
  'Postar SÓ no Facebook, ao vivo, ANTES das 17h (o nora46 abre os horários do dia às 17h). Me diga a que horas postou: o face02 vai na metade do intervalo entre o face01 e as 17h. Vale o story que estiver no ar (o story-3010 até 18h44; o story-3110 entra antes das 17h). Comentário: só comente (no Face não fixa).']
c['colagens'] = [{'titulo': 'clipe sem fala', 'fala': '(sem fala)', 'movimentacao': ['(sem fala)'], 'takes': [0]}]
p['central'] = c
p['story'] = {'ja_postado': True, 'nota': '✅ NÃO FAÇA STORY PARA ESTE VÍDEO. Vale o story que estiver no ar no Face (o story-3010 até 18h44; o story-3110, do painel do nora46, entra antes das 17h).'}
p['edicao_linha'] = [
  {'quando': '1. O clipe todo (8 s)', 'texto': 'Camada escura', 'como': 'Por cima do clipe, um retângulo preto a 35% de opacidade cobrindo a tela inteira (ou Ajustar → Brilho −25), para o texto branco ler bem.'},
  {'quando': '2. O clipe todo', 'texto': TEXTO,
   'como': 'Um bloco só, centralizado (X 0 · Y 0), em MAIÚSCULAS, Poppins Bold (poppins-bd), branco, tamanho 8 (se passar das bordas, 7), Sombra preta, sem Traço grosso, Luz DESLIGADA, uma linha em branco entre as frases, largura de ~90% da tela. Ocupa do ~22% ao ~85% da altura, como no vídeo da Mary.'},
  {'quando': '3. O clipe todo', 'texto': 'Som do clipe ligado + música de sempre (“Ambient Mystical Drone”), 0 dB', 'como': 'Sem legenda automática (ela não fala), sem números fixos e sem seta (o texto já diz o que fazer).'}]
p['pecas'] = {'lista': [
  {'nome': 'face01-IMG', 'tipo': 'imagem 1', 'status': 'gerar', 'descricao': 'Do blueprint: a Nora no carro parado ao fim da tarde, olhos fechados, suéter bege, árvores de outono lá fora.',
   'base': 'O vídeo da 1ª venda da Mary (mulher de olhos fechados no carro).', 'serve': 'Outros testes de texto longo no Face (troca só o texto).'},
  {'nome': 'face01-CLIPE', 'tipo': 'clipe sem fala', 'status': 'gerar', 'creditos': 12, 'descricao': '8 s em Frames, primeiro e último quadro iguais: ela respira de olhos fechados; o clipe repete sem pulo.',
   'base': 'Vídeo da Mary.', 'serve': 'Outros textos longos no Face, sem gastar crédito (só troca o texto por cima).'}],
  'decisao': [
   'Teste só do Facebook, fora da numeração nora (pedido do aluno, 31/10): os painéis nora são os vídeos do Insta e do Face a partir das 17h.',
   'Copiado do vídeo da 1ª venda da Mary: texto longo sobre um clipe calmo, "read this before you scroll", alguém tentando falar com você, uma bênção que ainda chega hoje, o que a pessoa descobre ao clicar.',
   'Trocado: a senhora falecida vira o anjo da guarda (P15; o anjo é o mecanismo dos anúncios escalados do portal); sai o "before it disappears forever" (P42); o link vai para o story das 3 cartas (no Face não dá para fixar comentário com link).',
   'O mesmo clipe serve a outros textos longos: o próximo teste do Face só troca o texto (0 crédito).']}
p['ordem'] = ['pecas', 'referencia', 'imagens', 'prehook', 'textotela', 'story', 'descricao', 'comentario', 'respostasface', 'fala']
gravar('PAINEL-FACE01.html', 'Painel face01 (só Face)', p)
print('ok: PAINEL-FACE01')
