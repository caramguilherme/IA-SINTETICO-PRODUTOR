# Painéis do dia 24/11/2026 ("pode montar", ~11h55): o teste do corpo (FILA, quadro de testes, item 2).
#   nora77 (Insta e Face, 19h30): o corpo A da maioria, o mesmo texto do nora75 (o m30 = m61), GERADO DE NOVO do 1º ao último take
#     (regra de 24/11 11h10: cada post do Insta com o vídeo inteiro novo), no mesmo sofá, com outra roupa (moletom cinza liso no nora77, azul-marinho no nora78 desde 24/11 17h13).
#   nora78 (Insta e Face, 0h00): o corpo leve (a Modelagem do m10, ~58 s, referencias-virais/2026-11-23-mineracao/MODELAGEM-PROXIMO-FALADO.md),
#     com o MESMO Take 1 da canela, na mesma roupa e no mesmo sofá, filmado de outro ângulo (para o Insta não ler como a mesma abertura do nora77).
# As decisões do aluno (24/11 11h51): (1) o mesmo Take 1 nos dois: a canela no Insta, as letras do nome no Face; (2) no Face, a última frase falada manda
#   para o 1º comentário; (3) o corpo leve com ~58 s; (4) o multi-ângulo fica para o próximo vídeo.
# Regras que entram: a bandeirinha dos EUA na parede (do nora77 em diante), a Nora sem a pintura, a seta grande (tamanho 44), o story com o "gift".
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2411/build_dia_2411.py
import json, copy, re, pathlib, importlib.util

R = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('b2311', R / 'ferramentas-painel' / 'dia-2311' / 'build_dia_2311.py')
B23 = importlib.util.module_from_spec(spec); spec.loader.exec_module(B23)
B, VC, FB, COMUNS, MODELO = B23.B, B23.VC, B23.FB, B23.COMUNS, B23.MODELO
assert FB.endswith('&aff=dl7zx6ks')

# ---------- a cena nova (as funções do build_dia_2311 leem estes nomes do módulo na hora em que rodam) ----------
ROUPA77 = 'her plain heather-gray crew-neck sweatshirt with no logo'
ROUPA78 = 'her plain navy-blue crew-neck sweatshirt with no logo'   # 24/11 17h13: o nora78 com outra roupa (regra do aluno de 11h10: "mudar cenário, roupa")
B23.ROUPA = ROUPA77
# 24/11 ~18h, o aluno não gostou da bandeirinha colada na parede: "tinha que estar como se fosse em um quadro, com moldura. ou ela pendurada… maior… de pé".
# FLAG escolhe a versão do painel ('quadro' ou 'vertical'); as 2 frases de correção vão no chat.
FLAG = 'quadro'
FLAG_DESC = {
    'quadro': ('a real American flag displayed inside a simple wooden picture frame with glass, hanging straight on the light wall behind her, high on the '
               'left side, about the size of a small poster, like a framed flag in a real American living room, not touching her head'),
    'vertical': ('a larger real American cloth flag hanging vertically from two small nails at its top corners on the left side of the light wall behind her, '
                 'with the blue field of stars at the top left and soft natural fabric folds, from near the ceiling down to about her shoulder height, '
                 'never covering her head or her face'),
}[FLAG]
FLAG_NOME = {'quadro': 'framed American flag', 'vertical': 'hanging American flag'}[FLAG]
FLAG_PT = {'quadro': 'a bandeira dos EUA no quadro com moldura', 'vertical': 'a bandeira dos EUA grande, pendurada na vertical'}[FLAG]
BANDEIRA = FLAG_DESC
B23.CENA = ('Casual real video in the late afternoon in a cozy American living room, she sits on a gray fabric sofa with cushions behind her and a plain light wall '
            f'with {BANDEIRA}, filmed from a static camera about one meter in front of her at chest height, looking exactly like a real phone video, lit by soft natural '
            'window light. ')
ROUPA = B23.ROUPA
ROUPA_PT = 'cinza'


def usar_roupa(r, pt):
    global ROUPA, ROUPA_PT
    B23.ROUPA = ROUPA = r
    ROUPA_PT = pt

IMG75_A = 'd2311-sofa-IMG-A'                 # a do nora75 (camiseta preta), a base da edição
IMG_A77, IMG_B77 = 'd2411-cinza-IMG-A', 'd2411-cinza-IMG-B'
IMG_A78, IMG_B78 = 'd2411-lado-IMG-A', 'd2411-lado-IMG-B'

_FIM = B23._FIM
PROMPT_A77 = ('Edit the attached photo. Keep everything exactly the same: the same woman, the same face, the same loose hair, the same gray sofa and cushions, the '
              'same clear stemmed glass of water and the same cinnamon jar in her hands, the same framing and the same light. Change only two things: (1) her black '
              't-shirt becomes a plain heather-gray crew-neck sweatshirt with no logo; (2) on the plain light wall behind her add ' + FLAG_DESC + '. ' + _FIM)
PROMPT_B77 = ('The attached image is the approved photo. Keep everything exactly the same: the same woman, the same face, the same loose hair, the same heather-gray '
              'sweatshirt, the same gray sofa, the same ' + FLAG_NOME + ' on the wall, the same framing and the same light. Change only this: the cinnamon jar is gone; '
              'with one hand she holds the clear stemmed glass at collarbone height, now filled with light-brown cinnamon water; her other hand is lowered, out of the '
              'frame; ' + _FIM)
PROMPT_A78 = ('The attached image is the approved photo. Change only two things: (1) show the same moment from another camera position: the camera is about '
              '30 degrees to her right and a little closer, still at collarbone height, and she turns her face to look straight into the camera; (2) her heather-gray '
              'sweatshirt becomes a plain navy-blue crew-neck sweatshirt with no logo. Keep exactly the same woman, the same face, the '
              'same loose hair, the same gray sofa, the same clear stemmed glass of water and the same cinnamon jar tilted above it, '
              'the same light, and the same ' + FLAG_NOME + ' on the wall, now seen from the new angle, never covering her head. ' + _FIM)
def prompt_troca_bandeira(desc):
    return ('Edit the attached photo. Keep everything exactly the same: the same woman, the same face, the same loose hair, the same heather-gray sweatshirt, '
            'the same gray sofa and cushions, the same clear stemmed glass of water and the same cinnamon jar in her hands, the same framing and the same light. '
            'Change only the flag on the wall: remove the small flag pinned flat to the wall and put in its place ' + desc + '. ' + _FIM)


PROMPT_B78 = (PROMPT_B77.replace('the same heather-gray sweatshirt', 'the same navy-blue sweatshirt')
              .replace('the same framing and the same light', 'the same new camera angle, the same framing and the same light'))
assert 'navy-blue' in PROMPT_B78 and 'heather-gray' not in PROMPT_B78 and 'navy-blue' in PROMPT_A78
for _t in (PROMPT_A77, PROMPT_B77, PROMPT_A78, PROMPT_B78):
    for _w in ('chest', 'skin', 'body', 'breast', 'underwear', 'mccormick', 'wine', 'powder', 'paint'):
        assert _w not in _t.lower(), _w

# ---------- as falas ----------
FALA77 = list(B23.FALA)          # o corpo A da maioria, igual ao nora75 (o controle do teste)
SUF77 = list(B23.SUF)
GESTO77 = list(B23.GESTO)
CANELA = FALA77[0]
LETRAS = B23.FALA76              # "If your name starts with the letter A, J, M, K, C, E, S, L, R, T or H, be very careful."
GESTO_LETRAS = B23.GESTO76
# 24/11 18h20, conferência das regras antes de gerar o nora78: no corpo leve, nada explica o "be very careful" (no nora76-FACE e no nora77-FACE ele
# abre o corpo A, que tem o aviso do Arcanjo); sozinho é medo e um laço que não fecha (P42, que vale no Face: a receita da maioria só passa na frente
# dela no Insta). Fica a versão do nora73 ("pay close attention", o v4 da @takedanaomi_, seção 54 do BIBLIOTECA-VIDEOS-VIRAIS.md).
LETRAS78 = "If your name starts with the letter A, J, M, K, C, E, S, L, R, T or H, pay close attention."
assert len(LETRAS78.split()) <= 22
CTA_FACE77 = "That's why I left you a quick reading. Check the first comment below to get your reading."
FALA78 = [
    CANELA,
    "If you're tired of working, paying the bills, and solving everyone's problems,",
    "and still feeling like you never really get ahead, this is for you.",
    "I don't know your name or everything you've been through, but the universe has seen your faith.",
    "The hardest stretch may finally be falling behind you. Over the next few days, watch for the small signs:",
    "a message you weren't expecting, a door that finally opens. More room to breathe. More peace inside your home.",
    "Sometimes a big change starts with one small door opening first.",
    "And because this new season opens differently for every woman, I left something in my story for you.",
    "Now pay attention: tap my profile picture and check my story. Three quick questions, and your private reading is ready.",
]
RESERVA78 = "Now pay attention: tap my profile picture and check my story. Three quick questions, and your reading is ready."
SUF78 = ['canela-copo', 'cansada', 'nunca-sobra', 'fe', 'trecho-dificil', 'sinais', 'porta', 'cada-mulher', 'cta-story']
GESTO78 = [
    GESTO77[0],
    'she holds a tired, understanding look, as if she knows this routine well',
    'she gives one slow nod with a soft, caring look',
    'her eyebrows lift slightly with a warm, hopeful look',
    'she holds a calm look and her face softens into a small relieved smile',
    'a warm, hopeful smile grows slowly on her face',
    'she holds a calm, knowing look and nods once, slowly',
    'she leans in slightly with a warm, encouraging look',
    GESTO77[-1],
]
CTA_FACE78 = "And because this new season opens differently for every woman, check the first comment below to get your reading."
GESTO_CTA_FACE = 'she glances down toward the bottom of the frame with a warm, encouraging smile, then back at the lens'
N77, N78 = len(FALA77), len(FALA78)
assert len(SUF78) == len(GESTO78) == N78

EXTRA = B23.EXTRA | {('a', 'warm'), ('a', 'calm'), ('a', 'small')}


def conferir_fala(fala, gestos, extras_face, deixa_private_no_ultimo=False):
    todos = [(i, f, g, i == 0) for i, (f, g) in enumerate(zip(fala, gestos))] + [(-1, f, g, False) for f, g in extras_face]
    for i, f, g, a in todos:
        assert len(f.split()) <= 22, (i + 1, len(f.split()), f)
        fw = re.findall(r"[a-z']+", f.lower()); mw = re.findall(r"[a-z']+", B23.mov(g, a).lower())
        sobra = (set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - COMUNS - EXTRA
        assert not sobra, (i + 1, sobra)
        proibidas = ('link', 'free', 'card', 'tarot') + (() if (deixa_private_no_ultimo and i == len(fala) - 1) else ('private',))
        for w in proibidas:
            assert w not in re.findall(r"[a-z']+", f.lower()), (i + 1, w)
        if 0 <= i < len(fala) - 1:
            prox = re.split(r'(?<=[.!?])\s+', fala[i + 1])[0]
            assert len(f.split()) + len(prox.split()) > 22, (i + 1, 'a 1ª frase do take seguinte cabe neste')


conferir_fala(FALA77, GESTO77, [(LETRAS, GESTO_LETRAS), (CTA_FACE77, GESTO_CTA_FACE)])
conferir_fala(FALA78, GESTO78, [(LETRAS78, GESTO_LETRAS), (CTA_FACE78, GESTO_CTA_FACE)], deixa_private_no_ultimo=True)
P77 = sum(len(f.split()) for f in FALA77)
P78 = sum(len(f.split()) for f in FALA78)


def nome(pref, sufs, i):
    return f'd2411-{pref}-T{i + 1:02d}-{sufs[i]}'


def livre():
    t = B23.livre().replace('the gray sofa and the cushions stay exactly as in the reference image',
                            'the gray sofa, the cushions and the ' + FLAG_NOME + ' on the wall stay exactly as in the reference image')
    assert FLAG_NOME + ' on the wall stay' in t and ROUPA in t
    return t


def config(img_b, n, mood='Íntimo e confidencial'):
    cf = copy.deepcopy(B.BASE['central']['config'])
    for s in cf:
        for campo in s['campos']:
            if campo['campo'].startswith('LIVRE'):
                campo['valor'] = f'colar o texto abaixo (a imagem é a {img_b}: a Nora no sofá, de moletom {ROUPA_PT}, com o copo de água de canela)'
                campo['copiar'] = livre()
            elif campo['campo'] == 'COLE SUA COPY AQUI':
                campo['valor'] = f'colar a fala do T02 ao T{n:02d} (seção “A fala e a movimentação”): 1 colagem só, com {n - 1} takes'
            elif campo['campo'] == 'Movimento de câmera':
                campo['valor'] = 'Estático / câmera parada, sem zoom'
            elif campo['campo'] == 'Atmosfera / mood':
                campo['valor'] = mood
            elif campo['campo'] == 'Movimentação':
                campo['valor'] = f'colar as {n - 1} linhas, uma por take (T02 a T{n:02d})'
            elif campo['campo'] == 'Conferir':
                campo['valor'] = f'{n - 1} takes (8 ou 10 s cada)'
    VC.adicionar(cf)
    return cf


def mapa(P):
    m = P['mapa_tela']
    m['estilos'] = [
        {'nome': 'Texto no topo', 'fonte': '—', 'cor': '—', 'tamanho': '—', 'contorno': '—', 'obs': 'NENHUM, como no nora75 (o m30 e o m61).'},
        {'nome': 'Legenda (eu ponho)', 'fonte': 'Inter, peso normal', 'cor': 'branca, sem destaque', 'tamanho': 'até ~6 palavras, 2 linhas',
         'contorno': 'fino escuro + sombra suave', 'obs': 'Simples, no meio para baixo.'},
        {'nome': 'Seta (eu ponho)', 'fonte': '—', 'cor': 'vermelha', 'tamanho': 'GRANDE (desde 24/11)', 'contorno': 'preto',
         'obs': 'Embaixo à esquerda, do CTA até o fim (aula 26: “you have to make it giant”).'},
    ]
    m['regras'] = ['Sem texto no topo; só o “11:11✨” pequeno no alto à direita (à esquerda fica o quadro da bandeira), a legenda simples e a seta grande no fim.',
                   'Eu ponho tudo (P45); você monta só o vídeo e a música.']
    m['numeros'] = [{'t': '11:11✨', 'x': 82, 'y': 16, 'onde': 'alto à direita, o vídeo todo (à esquerda fica o quadro da bandeira)', 'cor_nome': 'branco', 'cor': '#FFFFFF', 'tamanho': 11}]


STORY_NOTA = ('O story de 24/11 01h15 vence às ~01h15 de 25/11. Reposte ANTES, no Insta e no Face, ao vivo, com o story do “gift” '
              '(ferramentas-painel/dia-2411/story-gift-2411.jpg; eu mando no chat), adesivo “TAP TO CONTINUE 🎁” com o link STORYIG no Insta e o FACE no Face. '
              'O melhor momento é junto com o nora78, por volta das 0h30 (ainda antes das 01h15). Antes de abrir o Insta, confira o IP e os EUA no mylocation.org.')


def imagens_secao(P, titulo, conceito, etapas):
    P['pre_gancho'] = {'titulo_secao': titulo, 'conceito': conceito,
                       'modo': 'Flow → Imagem · 9:16 · Nano Banana Pro · x4, anexando as referências na ordem (0 crédito).', 'etapas': etapas}


def agente(P, n, img_a, img_b, nomes, t01, extras, rotulo, intro_extra='', falas=None):
    # 24/11 18h20 (cobrança do aluno: "pq mensagem 3 e mensagem 4? … nao tem um passo a passo, nao tem uma ordem pra se seguir"): a lista já é numerada
    # pelo painel; os rótulos "MENSAGEM 1 a 4" dentro dela davam uma 2ª numeração que não batia (o passo 5 era a "mensagem 3"). Agora cada passo diz
    # o que gera (o nome do take), com que imagem e com que nome salvar, numa ordem só.
    ct = P['central']
    ag = copy.deepcopy(ct['agente'])
    ag['imagem'] = img_b
    # 24/11 18h35 (o aluno: "pq o muse nao colocou o nome? nao era regra isso?"): era, desde 23/11 18h52 (`LICOES`), mas o aviso vinha do painel do
    # nora70 (B.BASE) com o texto antigo, "Name each clip with its prompt number", e na 1ª leva do nora77 o Muse baixou 6 clipes com nome aleatório.
    # Agora o aviso lista o nome de cada prompt, e a mensagem dos prompts 07 em diante repete os nomes deles.
    velho = 'Name each clip with its prompt number (01, 02, 03 and so on).'
    assert velho in ag['aviso'], 'o aviso do Muse mudou: conferir a frase do nome dos arquivos'
    # 24/11 23h30: o bloco da Central numera "Prompt 1", "Prompt 2"… (GUIA-CREATIVE-HUB.md); o aviso usa a mesma grafia, sem o zero
    nomes_corpo = ', '.join(f'Prompt {i} = {nomes[i]}' for i in range(1, n))
    ag['aviso'] = ag['aviso'].replace(velho, f'Name each clip with exactly this file name, so the downloaded file already has it: {nomes_corpo}.')
    resto = ', '.join(f'Prompt {i} = {nomes[i]}' for i in range(7, n))
    msg_resto = ('“Now generate the remaining prompts from my previous message, exactly as written, in the same order, using the attached image as the first '
                 f'frame of every clip, and name each clip with exactly this file name: {resto}.”')
    # 24/11 18h02 (pergunta do aluno sobre a voz do T01): o T01 passa a ser gerado DEPOIS do corpo, na mesma conversa, para o Muse copiar a voz
    # dos clipes que acabou de fazer (o "SAME VOICE AS THE OTHER CLIPS" do prompt só tem referência quando o corpo já existe). Foi assim no T01B do nora76.
    ag['intro'] = (f'No Muse, na mesma conversa da Nora (a do nora75 e do nora76: a voz). Siga os passos de cima para baixo, um de cada vez. '
                   f'São {n + len(extras)} clipes: os {n - 1} do corpo (T02 a T{n:02d}), depois o T01 e, por último, os {len(extras)} que são só do Face. '
                   'Por que 2 a mais para o Face: o Face precisa de outro começo (com o mesmo 1º take, ele lê como vídeo repetido; a sua regra de 24/11) e de '
                   'outro fim (o CTA manda para o 1º comentário, onde está o link, sem pedir comentário nem selos). O meio é o mesmo, então são só 2 clipes, não um vídeo inteiro.' + intro_extra)
    lista = ' · '.join(f'clipe {i:02d} do Muse = {nomes[i]}' for i in range(1, n))  # 24/11 18h11: o clipe 01 do Muse é o T02 (estava "02 = T02")
    # 24/11 18h27 (print do aluno): o Muse baixa os 6 primeiros clipes com um nome aleatório (só números e letras), sem o número do clipe; a ordem
    # na pasta não garante a ordem do vídeo. Por isso a lista diz as primeiras palavras de cada take: ouvir 2 segundos e renomear.
    if falas:
        lista = ' · '.join(f'T{i + 1:02d} começa em “{" ".join(falas[i].split()[:5])}…” → {nomes[i]}' for i in range(1, n))
    passos = [f'Na Central: preencha como na seção da Central (o LIVRE e a movimentação do {rotulo}) e cole a fala do T02 ao T{n:02d}. Confira: {n - 1} takes.',
              f'O corpo (T02 a T{n:02d}, {n - 1} clipes): no Muse, anexe a {img_b} + o aviso do Muse + o “COPIAR TUDO JUNTO”. O Muse gera 6 por vez: depois dos 6 primeiros, '
              f'mande na mesma conversa, com a mesma imagem: {msg_resto}',
              f'Confira os nomes ao baixar: cada clipe já deve vir com o nome dele (o site põe “media-generation-” na frente e um código no fim; pode deixar). Se algum vier com um nome aleatório, ouça o começo e renomeie pela frase: {lista}.',
              f'O T01 (só depois do corpo pronto): anexe a {img_a} e cole o prompt abaixo. Salve como {nomes[0]}. '
              'Ouça o T01 ao lado do T02: se a voz sair diferente, gere de novo na mesma conversa. PROMPT: ' + t01]
    for k, (rot, titulo, lugar, arq, prompt) in enumerate(extras, start=1):
        passos.append(f'O {rot}, o {k}º take só do Face ({titulo}; na versão do Face ele entra {lugar}): anexe a {img_b} e cole o prompt abaixo. '
                      f'Salve como {arq}. PROMPT: ' + prompt)
    passos += [f'Confira cada take: sem a lua e sem as estrelinhas no rosto; o moletom {ROUPA_PT}; {FLAG_PT}; o copo na mão; ela fala uma vez só e fecha a '
               'boca no fim. Se o Muse recusar: “Generate prompt X again, exactly as written.”',
               'Se a voz de algum take sair diferente das outras, gere aquele de novo na mesma conversa, pedindo “exactly the same voice as the other clips of this video”.']
    ag['passos'] = passos
    ct['agente'] = ag


def base(nn):
    P = B23.base(nn)
    P['figurino'] = ROUPA
    P['story'] = {'ja_postado': True, 'nota': STORY_NOTA}
    return P


def nora77():
    usar_roupa(ROUPA77, 'cinza')
    P = base('nora77')
    n = N77
    nomes = [nome('cinza', SUF77, i) for i in range(n)]
    n_letras, n_cta = 'd2411-cinza-T14-FACE-letras', 'd2411-cinza-T15-FACE-cta-comentario'  # 24/11 18h30: eram T01F e T12F; a FusionZ junta pela ordem do nome (P27) e os punha no meio
    imagens_secao(P, 'As 2 imagens (Flow, antes dos takes)',
                  ('O nora75 gerado de novo, do 1º ao último take (o Insta derruba o arquivo reaproveitado), com outra roupa: o mesmo sofá, a mesma canela no copo, '
                   f'agora de moletom cinza liso, e {FLAG_PT} na parede atrás. A Nora sem a pintura.'),
                  [{'titulo': 'Imagem A: despejando a canela no copo (o T01)', 'nome': IMG_A77, 'tipo': 'img',
                    'anexar': f'só a {IMG75_A} (a imagem A do nora75, a de camiseta preta despejando a canela)',
                    'quadros': (f'x4, 0 crédito. Escolha a que tiver: a mesma Nora SEM a lua e SEM as estrelinhas, o MOLETOM CINZA liso, {FLAG_PT}, no '
                                f'alto da parede à esquerda, sem encostar na cabeça; o copo e o pote de canela como antes; 5 dedos em cada mão. Renomeie para {IMG_A77}.'),
                    'prompt': PROMPT_A77},
                   {'titulo': 'Se você JÁ GEROU a imagem A com a bandeirinha colada na parede: corrija só a bandeira', 'nome': IMG_A77, 'tipo': 'img',
                    'anexar': 'só a melhor das 4 que você já gerou (a de moletom cinza)',
                    'quadros': f'x4, 0 crédito. Escolha a que tiver: o mesmo rosto e as mesmas mãos de antes; {FLAG_PT}, sem cobrir a cabeça. Renomeie para {IMG_A77}.',
                    'prompt': prompt_troca_bandeira(FLAG_DESC)},
                   {'titulo': 'Imagem B: o copo com a água de canela na mão (T02 em diante e os 2 takes do Face)', 'nome': IMG_B77, 'tipo': 'img',
                    'anexar': f'só a {IMG_A77} que você escolheu',
                    'quadros': f'x4, 0 crédito. Escolha a que tiver: sem o pote; o copo com a água marrom-clara na mão; o moletom cinza; {FLAG_PT}. Renomeie para {IMG_B77}.',
                    'prompt': PROMPT_B77}])
    P['imagens_titulo'] = f'As imagens das falas ({IMG_A77} no T01; {IMG_B77} no resto)'
    P['refs'] = [f'{IMG_A77} no T01', f'{IMG_B77} do T02 ao T{n:02d} e nos 2 takes do Face']
    P['imagens'] = [{'rotulo': f'IMAGEM 1 · {IMG_A77}', 'cena': 'gerada no Flow (seção das imagens)', 'anexar': f'a {IMG_A77}'},
                    {'rotulo': f'IMAGEM 2 · {IMG_B77}', 'cena': 'gerada no Flow (seção das imagens)', 'anexar': f'a {IMG_B77}'}]
    P['roteiro'] = {
        'id': 'nora77-CORPO-A-CINZA-2411',
        'titulo': 'nora77 · Insta e Face 19h30 de 24/11 · o teste do corpo, lado A: o corpo da maioria (o do nora75), gerado de novo, de moletom cinza',
        'duracao_total': 95,
        'descricao_instagram': ("Put cinnamon in a glass of water before you leave the house 🌿 Your private reading is waiting in my story 🔮\n"
                                'Type 222 if this found you today 👇\n'
                                '#manifestation #cinnamon #abundance #2027 #lawofattraction'),
        'descricao_face': ('If your name starts with one of these letters ✨ Your reading is waiting in the first comment 🔮\n'
                           '#manifestation #abundance #2027'),
    }
    P['videos'] = ([{'rotulo': f'T{i + 1:02d}', 'cena': SUF77[i], 'duracao': 10,
                     'primeiro_quadro': (f'IMAGEM 1 ({IMG_A77})' if i == 0 else f'IMAGEM 2 ({IMG_B77})'), 'acao': '', 'b_roll': '', 'fala': FALA77[i],
                     'movimentacao': B23.mov(GESTO77[i], i == 0), 'arquivo': nomes[i]} for i in range(n)]
                   + [{'rotulo': 'T14 (só Face)', 'cena': 'as letras do nome (no lugar do T01 no Face)', 'duracao': 10, 'primeiro_quadro': f'IMAGEM 2 ({IMG_B77})',
                       'acao': '', 'b_roll': '', 'fala': LETRAS, 'movimentacao': B23.mov(GESTO_LETRAS), 'arquivo': n_letras},
                      {'rotulo': 'T15 (só Face)', 'cena': 'o CTA para o comentário (no lugar do T12 e do T13 no Face)', 'duracao': 10,
                       'primeiro_quadro': f'IMAGEM 2 ({IMG_B77})', 'acao': '', 'b_roll': '', 'fala': CTA_FACE77,
                       'movimentacao': B23.mov(GESTO_CTA_FACE), 'arquivo': n_cta}])
    P['texto_tela'] = {'hook': '', 'hook_comeca': '—', 'hook_termina': '—', 'hook_alt': '', 'extras': []}
    mapa(P)
    P['comentario_fixado'] = {'insta': 'Did you do it? 🌿 tap my profile picture above, your reading is waiting in my story',
                              'face': 'Your 2027 reading is waiting for you here ✨ 👉 ' + FB}
    ct = P['central']
    ct['config'] = config(IMG_B77, n)
    ct['colagens'] = [{'titulo': f'nora77: a colagem do T02 ao T{n:02d} (na {IMG_B77})', 'fala': ' '.join(FALA77[1:]),
                       'movimentacao': [B23.mov(GESTO77[i]) for i in range(1, n)], 'takes': list(range(1, n))}]
    ct['conferir'] = (f'Conferir em cada take: a Nora SEM a lua e SEM as estrelinhas, de moletom cinza, no sofá, com o copo de água de canela e {FLAG_PT}; '
                      'ela fala uma vez só e diz as datas e os números por extenso.')
    t01 = B23.prompt_manual(FALA77[0], B23.mov(GESTO77[0], True), 'the stemmed glass of water and the cinnamon jar in her hands', nomes[0], 1, n)
    agente(P, n, IMG_A77, IMG_B77, nomes, t01,
           [('T14', 'as letras do nome', 'no lugar do T01', n_letras,
             B23.prompt_manual(LETRAS, B23.mov(GESTO_LETRAS), 'the stemmed glass of cinnamon water in her hand', n_letras, 1, n)),
            ('T15', 'o CTA para o comentário', 'no lugar do T12 e do T13', n_cta,
             B23.prompt_manual(CTA_FACE77, B23.mov(GESTO_CTA_FACE), 'the stemmed glass of cinnamon water in her hand', n_cta, n, n))],
           'nora77', falas=FALA77)
    P['silencio'] = {
        'intro': ('Arraste na “M2M FusionZ” os 15 takes de uma vez (T01 a T15), sem separar nada. A ferramenta junta pela ordem do nome, então o T14 e o T15 '
                  '(os 2 só do Face) ficam no fim. Sai 1 arquivo só, com os 15. “Zoom nos cortes” = DESLIGADO.'),
        'nome': 'nora77-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'T01 a T15 (o T14 e o T15 são os do Face)',
        'depois': ['Suba os 15 takes e espere a Prévia.', 'Confira a primeira palavra do T01 e a última do T15.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', 'Clique em Cortar e baixar e salve como nora77-cortado.'],
    }
    P['edicao_linha'] = [
        {'quando': 'O que vai em cada vídeo', 'texto': 'Você monta 1 arquivo só, com os 15 takes. Os 2 vídeos (Insta e Face) eu separo aqui.',
         'como': ('INSTA (nora77-final): T01 ao T13, na ordem. FACE (nora77-final-FACE): T14 (as letras) + T02, T03, T04 (eu tiro o “money”), T06, T07, T11 + T15 (o comentário). '
                  'Ficam fora do Face: o T01, o T05 (a ameaça), o T08 (os 7 minutos e o “send to yourself”), o T09 (os selos e o amen), o T10 (“amanhã às 10”), o T12 e o T13 (o CTA do story).')},
        {'quando': 'A. Antes de tudo', 'texto': 'Projeto novo no CapCut com o nora77-cortado', 'como': 'Começa direto no T01, sem hook. O T14 e o T15 ficam no fim, como vieram da FusionZ.'},
        {'quando': '1. Do começo ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB, o vídeo todo (o T14 e o T15 também)', 'como': 'Começa no 1º quadro.'},
        {'quando': '2. Exportar e me mandar até ~18h45', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': '1080×1920, nome nora77-montado (acima de 30 MB, link do Drive). Eu devolvo em ~20 min os 2 prontos: o nora77-final (Insta) e o nora77-final-FACE.'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': ([{'nome': IMG_A77, 'tipo': 'imagem do T01', 'status': 'gerar', 'onde': 'No Flow, editando a do nora75 (x4, 0 crédito).', 'descricao': f'Moletom cinza + {FLAG_PT}.'},
                   {'nome': IMG_B77, 'tipo': 'imagem das falas', 'status': 'gerar', 'onde': 'No Flow, editando a A (x4, 0 crédito).', 'descricao': 'O copo na mão.'}]
                  + [{'nome': nomes[i], 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{FALA77[i]}”'} for i in range(n)]
                  + [{'nome': n_letras, 'tipo': 'take do Face', 'status': 'gerar', 'descricao': f'“{LETRAS}”'},
                     {'nome': n_cta, 'tipo': 'take do Face', 'status': 'gerar', 'descricao': f'“{CTA_FACE77}”'}]),
        'decisao': [
            'O QUE ESTE VÍDEO TESTA: o corpo. É o lado A (o corpo da maioria, igual ao nora75) contra o nora78 (o corpo leve), à 0h00. A medida, com ~24 h: as visitas ao '
            'perfil e os cliques no Tracker. O Take 1 é o mesmo nos dois (a canela no Insta, as letras no Face).',
            f'{n} takes ({P77} palavras, ~1:35) + 2 só do Face = {n + 2} clipes no Muse. Tudo gerado de novo (o Insta derruba o arquivo reaproveitado), de moletom cinza, com ' + FLAG_PT + '.',
            'Insta e Face às 19h30. No Face: as letras do nome na abertura e a última frase manda para o 1º comentário; sem os selos, o “amen”, os 7 minutos, o “money” e a ameaça do T05 (“if you turn your back on this message…”). Você gera o T05 normalmente: ele vai só no Insta.',
            'O story vence às ~01h15: reposte com o do “gift”, de preferência junto com o nora78. Antes de abrir o Insta, conferir o IP e os EUA no mylocation.org.',
        ],
    }
    P['ordem'] = ['pecas', 'prehook', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    return P


def nora78():
    usar_roupa(ROUPA78, 'azul-marinho')
    P = base('nora78')
    n = N78
    nomes = [nome('lado', SUF78, i) for i in range(n)]
    n_letras, n_cta = 'd2411-lado-T10-FACE-letras', 'd2411-lado-T11-FACE-cta-comentario'  # 24/11 18h30: eram T01F e T08F
    imagens_secao(P, 'As 2 imagens (Flow, antes dos takes)',
                  ('O mesmo sofá, a mesma canela no copo e ' + FLAG_PT + ', mas com OUTRA ROUPA (moletom azul-marinho liso) e de outro ângulo (a câmera ~30° para a direita): '
                   'a frase do Take 1 é a mesma do nora77, e a roupa e o ângulo novos evitam que o Insta leia como o mesmo vídeo. A Nora sem a pintura. '
                   'Todos os takes do nora78 saem destas 2 imagens: o vídeo inteiro fica de azul-marinho.'),
                  [{'titulo': 'Imagem A: despejando a canela, do outro ângulo (o T01)', 'nome': IMG_A78, 'tipo': 'img',
                    'anexar': f'só a {IMG_A77} (a imagem A do nora77)',
                    'quadros': (f'x4, 0 crédito. Escolha a que tiver: a mesma Nora, sem a pintura, de MOLETOM AZUL-MARINHO liso, olhando para a câmera, vista de um ângulo diferente '
                                f'do nora77; {FLAG_PT} ainda na parede, sem cobrir a cabeça; o copo e o pote de canela; 5 dedos em cada mão. Renomeie para {IMG_A78}.'),
                    'prompt': PROMPT_A78},
                   {'titulo': 'Imagem B: o copo na mão, do outro ângulo (T02 em diante e os 2 takes do Face)', 'nome': IMG_B78, 'tipo': 'img',
                    'anexar': f'só a {IMG_A78} que você escolheu',
                    'quadros': f'x4, 0 crédito. Escolha a que tiver: sem o pote; o copo com a água marrom-clara na mão; o moletom azul-marinho; o mesmo ângulo novo. Renomeie para {IMG_B78}.',
                    'prompt': PROMPT_B78}])
    P['imagens_titulo'] = f'As imagens das falas ({IMG_A78} no T01; {IMG_B78} no resto)'
    P['refs'] = [f'{IMG_A78} no T01', f'{IMG_B78} do T02 ao T{n:02d} e nos 2 takes do Face']
    P['imagens'] = [{'rotulo': f'IMAGEM 1 · {IMG_A78}', 'cena': 'gerada no Flow (seção das imagens)', 'anexar': f'a {IMG_A78}'},
                    {'rotulo': f'IMAGEM 2 · {IMG_B78}', 'cena': 'gerada no Flow (seção das imagens)', 'anexar': f'a {IMG_B78}'}]
    P['roteiro'] = {
        'id': 'nora78-CORPO-LEVE-LADO-2411',
        'titulo': 'nora78 · Insta e Face ~0h30 de 25/11 · o teste do corpo, lado B: o corpo leve (a dor das contas, os sinais pequenos, o CTA com motivo)',
        'duracao_total': 65,
        'descricao_instagram': ("If you're tired of carrying everything, this is for you 🌿 Your private reading is waiting in my story 🔮\n"
                                'Comment the time you’re watching this ⏰\n'
                                '#manifestation #abundance #2027 #lawofattraction #newchapter'),
        'descricao_face': ('If your name starts with one of these letters, this is for you ✨ Your reading is waiting in the first comment 🔮\n'
                           '#manifestation #2027 #newchapter'),
    }
    P['videos'] = ([{'rotulo': f'T{i + 1:02d}', 'cena': SUF78[i], 'duracao': 10,
                     'primeiro_quadro': (f'IMAGEM 1 ({IMG_A78})' if i == 0 else f'IMAGEM 2 ({IMG_B78})'), 'acao': '', 'b_roll': '', 'fala': FALA78[i],
                     'movimentacao': B23.mov(GESTO78[i], i == 0), 'arquivo': nomes[i]} for i in range(n)]
                   + [{'rotulo': 'T10 (só Face)', 'cena': 'as letras do nome (no lugar do T01 no Face)', 'duracao': 10, 'primeiro_quadro': f'IMAGEM 2 ({IMG_B78})',
                       'acao': '', 'b_roll': '', 'fala': LETRAS78, 'movimentacao': B23.mov(GESTO_LETRAS), 'arquivo': n_letras},
                      {'rotulo': 'T11 (só Face)', 'cena': 'o CTA para o comentário (no lugar do T08 e do T09 no Face)', 'duracao': 10,
                       'primeiro_quadro': f'IMAGEM 2 ({IMG_B78})', 'acao': '', 'b_roll': '', 'fala': CTA_FACE78,
                       'movimentacao': B23.mov(GESTO_CTA_FACE), 'arquivo': n_cta}])
    P['texto_tela'] = {'hook': '', 'hook_comeca': '—', 'hook_termina': '—', 'hook_alt': '', 'extras': []}
    mapa(P)
    P['comentario_fixado'] = {'insta': 'This is your sign 🌿 tap my profile picture above, your reading is waiting in my story',
                              'face': 'Your reading is waiting for you here 🙏 👉 ' + FB}
    ct = P['central']
    ct['config'] = config(IMG_B78, n, 'Caloroso e acolhedor')  # 24/11 23h25: o corpo leve é fala de amiga (LICOES, 19/11 ~14h)
    ct['colagens'] = [{'titulo': f'nora78: a colagem do T02 ao T{n:02d} (na {IMG_B78})', 'fala': ' '.join(FALA78[1:]),
                       'movimentacao': [B23.mov(GESTO78[i]) for i in range(1, n)], 'takes': list(range(1, n))}]
    ct['conferir'] = ('Conferir em cada take: a Nora sem a pintura, de moletom azul-marinho, no ângulo novo, com o copo; ela fala uma vez só. No T09, se o Muse cortar a '
                      f'palavra “private”, gere de novo com a reserva: “{RESERVA78}”')
    t01 = B23.prompt_manual(FALA78[0], B23.mov(GESTO78[0], True), 'the stemmed glass of water and the cinnamon jar in her hands', nomes[0], 1, n)
    agente(P, n, IMG_A78, IMG_B78, nomes, t01,
           [('T10', 'as letras do nome', 'no lugar do T01', n_letras,
             B23.prompt_manual(LETRAS78, B23.mov(GESTO_LETRAS), 'the stemmed glass of cinnamon water in her hand', n_letras, 1, n)),
            ('T11', 'o CTA para o comentário', 'no lugar do T08 e do T09', n_cta,
             B23.prompt_manual(CTA_FACE78, B23.mov(GESTO_CTA_FACE), 'the stemmed glass of cinnamon water in her hand', n_cta, n, n))],
           'nora78', ' Dá para gerar logo depois do nora77, na mesma conversa.', falas=FALA78)
    ct['agente']['passos'].insert(3, f'Se o T09 sair sem a palavra “private” ou o Muse recusar, gere o T09 de novo com esta fala de reserva: “{RESERVA78}”')
    P['silencio'] = {
        'intro': ('Arraste na “M2M FusionZ” os 11 takes de uma vez (T01 a T11), sem separar nada. A ferramenta junta pela ordem do nome, então o T10 e o T11 '
                  '(os 2 só do Face) ficam no fim. Sai 1 arquivo só, com os 11. “Zoom nos cortes” = DESLIGADO.'),
        'nome': 'nora78-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'T01 a T11 (o T10 e o T11 são os do Face)',
        'depois': ['Suba os 11 takes e espere a Prévia.', 'Confira a primeira palavra do T01 e a última do T11.',
                   'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', 'Clique em Cortar e baixar e salve como nora78-cortado.'],
    }
    P['edicao_linha'] = [
        {'quando': 'O que vai em cada vídeo', 'texto': 'Você monta 1 arquivo só, com os 11 takes. Os 2 vídeos (Insta e Face) eu separo aqui.',
         'como': ('INSTA (nora78-final): T01 ao T09, na ordem. FACE (nora78-final-FACE): T10 (as letras) + T02 ao T07 + T11 (o comentário). '
                  'Ficam fora do Face: o T01 (o Face abre com outro take), o T08 e o T09 (o CTA do story).')},
        {'quando': 'A. Antes de tudo', 'texto': 'Projeto novo no CapCut com o nora78-cortado', 'como': 'Começa direto no T01, sem hook. O T10 e o T11 ficam no fim, como vieram da FusionZ.'},
        {'quando': '1. Do começo ao fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB, o vídeo todo (o T10 e o T11 também)', 'como': 'Começa no 1º quadro.'},
        {'quando': '2. Exportar e me mandar até ~0h10', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': '1080×1920, nome nora78-montado (link do Drive se passar de 30 MB). Eu devolvo em ~20 min os 2 prontos: o nora78-final (Insta) e o nora78-final-FACE.'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': ([{'nome': IMG_A78, 'tipo': 'imagem do T01', 'status': 'gerar', 'onde': 'No Flow, editando a do nora77 (x4, 0 crédito).', 'descricao': 'Moletom azul-marinho + o ângulo novo.'},
                   {'nome': IMG_B78, 'tipo': 'imagem das falas', 'status': 'gerar', 'onde': 'No Flow, editando a A (x4, 0 crédito).', 'descricao': 'O copo na mão.'}]
                  + [{'nome': nomes[i], 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{FALA78[i]}”'} for i in range(n)]
                  + [{'nome': n_letras, 'tipo': 'take do Face', 'status': 'gerar', 'descricao': f'“{LETRAS78}”'},
                     {'nome': n_cta, 'tipo': 'take do Face', 'status': 'gerar', 'descricao': f'“{CTA_FACE78}”'}]),
        'decisao': [
            'O QUE ESTE VÍDEO TESTA: o corpo. É o lado B (o corpo leve: a dor das contas na 2ª frase, os sinais pequenos, o CTA que diz o que tem do outro lado, '
            'a aula 64, 0:14:59) contra o nora77 (o corpo da maioria). A medida, com ~24 h: as visitas ao perfil e os cliques no Tracker.',
            f'{n} takes ({P78} palavras, ~1:05) + 2 só do Face = {n + 2} clipes no Muse. A mesma frase do Take 1 (a canela) e o mesmo sofá do nora77, com outra roupa (moletom azul-marinho) e de outro ângulo; o vídeo inteiro de azul-marinho.',
            'Insta e Face por volta das 0h30 (o montado até ~0h10; eu devolvo em ~20 min). No Face: as letras do nome na abertura e a última frase manda para o 1º comentário.',
            'Reposte o story do “gift” junto com este post (o de 24/11 vence às ~01h15).',
        ],
    }
    P['ordem'] = ['pecas', 'prehook', 'central', 'cenas', 'agente', 'silencio', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    return P


def salvar(P, nn, rotulo):
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>' + rotulo + '</title>', html, count=1)
    (R / f'PAINEL-{nn.upper()}.html').write_text(html, encoding='utf-8')
    print('ok', nn, len(html), 'bytes')


if __name__ == '__main__':
    print('nora77:', N77, 'takes,', P77, 'palavras · nora78:', N78, 'takes,', P78, 'palavras')
    salvar(nora77(), 'nora77', 'Painel nora77 · o corpo da maioria, de moletom cinza · 24/11')
    salvar(nora78(), 'nora78', 'Painel nora78 · o corpo leve, de moletom azul-marinho · 24/11')
