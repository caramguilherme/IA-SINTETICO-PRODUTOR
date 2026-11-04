# nora48 e nora49 (04/11/2026 ~13h, aprovado pelo aluno): o gancho do tsunami (nora47) nos dois, para comparar o CORPO com o mesmo gancho.
# nora48 = tsunami + Take 1 de Câncer/Escorpião/Peixes gerado na nora37-IMG (quarto à noite) + corpo A limpo (takes do nora40 sem T02, T06, T09 e T10).
# nora49 = tsunami ESPELHADO + Take 1 de Áries/Leão/Sagitário (nora46-IMG) + corpo B do nora46. Edição pela P45 (o aluno manda o montado sem texto).
import re, json
rx = r'const PACOTE = (\{.*?\});\n'
def load(f):
    s = open(f, encoding='utf-8').read(); m = re.search(rx, s, re.S); return s, m, json.loads(m.group(1))
def save(f, s, m, P):
    s = s[:m.start()] + 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';\n' + s[m.end():]
    open(f, 'w', encoding='utf-8').write(s)
def bigr(t):
    w = re.findall(r"[a-z0-9:']+", t.lower()); return {(w[i], w[i+1]) for i in range(len(w)-1)}
COMUNS = {('and', 'it'), ('of', 'the'), ('to', 'the')}

_, _, P40 = load('PAINEL-NORA40.html')
_, _, P47 = load('PAINEL-NORA47.html')
FACE = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
INSTA = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
LEIT = ('04/11/2026 ~13h (aprovação do aluno às ~13h para postar hoje às 19h30 e 22h; leitura PARCIAL, registro honesto): reli o CLAUDE.md inteiro (seção 0 e P1 a P45), '
        'os pacotes dos painéis do nora40 (corpo A: falas dos 12 takes, LIVRE e movimentação da nora37-IMG, mapa da tela), do nora46/nora47 (corpo B, tsunami, edição P45) e deste painel, '
        'o roteiro do nora40, as leituras de métricas de 04/11 (METRICAS-NORA-LEIA.md) e as regras P42 e do nora50 em diante. Não reli a lista inteira de LEIA-TUDO-ANTES.md hoje '
        '(a última leitura completa foi em 31/10). Não há fala nova: os Takes 1 são os já escritos e checados em 01/11; o corpo A é o do nora40, sem os takes vermelhos.')
STORY_REPOSTE = ('REPOSTE O STORY ANTES DAS 19h30 (o story-0311 de ontem vence ~22h45; repostando agora ele cobre a noite toda): a mesma imagem (story-3110), o mesmo texto e o adesivo com o link certo de cada rede; confira na prévia. '
                 'Insta (STORYIG): ' + INSTA + ' · Face (FACE): ' + FACE)

def story(nota, ja):
    st = json.loads(json.dumps(P47['story'])); st['nota'] = nota
    if ja: st['ja_postado'] = True
    else: st.pop('ja_postado', None)
    return st

HOOK_CONCEITO = ('O gancho do nora47 (o tsunami: praia, a onda gigante, ela corre e se tranca no bunker, a onda bate na porta), JÁ PRONTO: 0 crédito. '
                 'No nora47 ele dobrou as views do nora46 no Insta (287 x 134 com ~11 h), segurou 58,8% nos 3 s e ~40% aos 8 s (o nora46 tinha ~20%). Gancho que pegou fica; agora muda o corpo.')

# ---------------------------------------------------------------- nora48
F = 'PAINEL-NORA48.html'; s, m, P = load(F)
FALA = P['videos'][0]['fala']
MOV = P40['videos'][0]['movimentacao'].replace(
    'during the first half of the take she holds a firm, serious look with her brows slightly lowered',
    'during the first half of the take she holds a calm, knowing look with soft eyes')
assert 'calm, knowing look' in MOV
ov = (bigr(FALA) & bigr(MOV)) - COMUNS
assert not ov, ov
CORPO = [('nora40-T03-corpo-segredo-fe', 'nora48-T02'), ('nora40-T04-corpo-virada-incomum', 'nora48-T03'),
         ('nora40-T05-corpo-dinheiro-prosperidade', 'nora48-T04'), ('nora40-T07-corpo-sao-miguel', 'nora48-T05'),
         ('nora40-T08-corpo-correntes', 'nora48-T06'), ('nora40-T11-cta-selos-seguir', 'nora48-T07'),
         ('nora40-T12-cta-222-story (a cópia do nora37-T03)', 'nora48-T08')]
falas40 = {v['arquivo']: v['fala'] for v in P40['videos']}
R = P['roteiro']
R['titulo'] = 'Gancho do tsunami + Take 1 de Câncer, Escorpião e Peixes no quarto à noite + corpo A limpo (os takes do nora40 sem os vermelhos)'
R['formato'] = ('Hook do tsunami (o do nora47, pronto) + Take 1 NOVO na nora37-IMG (Câncer, Escorpião e Peixes) + 7 takes do nora40 (T03, T04, T05, T07, T08, T11 e T12; '
                'saem o T02 “claim this energy” antes da hora, o T06 da ameaça e o T09 e o T10 dos “sete minutos”) (~80 s)')
R['molde_hook'] = ('Gancho do tsunami (Vinicius Almeida; testado no nora47) + corpo A, a copy validada do nicho (a da Scarllet, “I don\'t know your name”), sem o vermelho (P42). '
                   'Teste de UMA variável contra o nora49 desta noite (mesmo gancho, corpo B): o corpo (Allan Mayer; Kaike: “copy validada + pré-hook novo”; Gustavo: “gancho que pegou fica, muda o corpo”).')
R['duracao_total'] = 80
R['leitura_registro'] = LEIT
R['descricao_instagram'] = ('Cancer, Scorpio, Pisces: if love and money keep repeating the same story, listen before 11/11, the most powerful portal of the year. 🔮\n'
                            'The worst is finally over. Your private reading is waiting in my story.\n#manifestation #1111portal #cancer #scorpio #pisces')
P['comentario_fixado'] = {
 'insta': 'Cancer, Scorpio, Pisces: love, money or peace, what are you ready to receive first? ✨ Tell me below, then tap my photo and open my story before the 11:11 portal: your private reading starts there. 🔮',
 'face': 'Cancer, Scorpio, Pisces: love, money or peace, what are you ready to receive first? ✨ Your private reading is right here, open it before the 11:11 portal 🔮 👉 ' + FACE}
P['refs'] = ['Folha de consistência da Nora (blueprint)', 'nora37-IMG (o Take 1 e o corpo A; já aprovada)', 'nora47-PRE-A e nora47-PRE-B (o hook, prontos)']
P['imagem_reutilizada'] = {'arquivo': 'nora37-IMG', 'aviso': 'O Take 1 usa a nora37-IMG, a mesma dos takes do nora40 (quarto à noite, abajur rosa, blusa preta canelada, as duas metades do geodo nas mãos). Não gere imagem nova.'}
P['imagens'] = [{'rotulo': 'IMAGEM 1 · nora37-IMG (já aprovada)', 'cena': '(não gerar)'}]
v = P['videos'][0]
v['movimentacao'] = MOV
v['cena'] = 'Take 1/8 do nora48 · Gancho no quarto à noite: Câncer, Escorpião e Peixes + o portal 11:11'
c = P['central']
c['config'] = json.loads(json.dumps(P40['central']['config']))
c['colagens'] = [{'titulo': 'só o Take 1 do nora48', 'fala': FALA, 'movimentacao': [MOV], 'takes': [0]}]
c['conferir'] = ('Conferir no Take 1: é a Nora (rosto, lua com as estrelinhas, trança, blusa preta), no quarto à noite com o abajur rosa, segurando as duas metades do geodo; '
                 'fala uma vez só, em inglês, com os signos certos, e termina em "eleven eleven, the year\'s most powerful portal"; as metades não fecham nem trocam de mão; sem texto, legenda ou música.')
a = c['agente'] = json.loads(json.dumps(P47['central']['agente']))
a['imagem'] = 'nora37-IMG'
a['intro'] = 'Uma imagem e uma mensagem: anexe a nora37-IMG, cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take na Central; com 1 take não existe o bloco “COPIAR TUDO JUNTO”).'
a['passos'] = ['Abra uma conversa nova no agente do Flow.', 'Anexe a nora37-IMG (só ela).', 'Cole o aviso (acima).', 'Embaixo, cole o prompt do Take 1 (botão COPIAR do take na Central).',
               'Envie. Renomeie para nora48-T01-gancho-portal-cancer-escorpiao-peixes. Confira o vídeo e me diga se falhou (o que saiu errado).']
c['passos'] = [
 'Story ANTES DAS 19h30: reposte o story-0311 (seção Story deste painel).',
 'Take 1 na Central com a MESMA configuração do nora40 (o texto LIVRE do quarto à noite, nesta seção). Cole só a fala e a linha de movimentação do Take 1. Gere: 1 take de 10 s.',
 'Agente do Flow: conversa nova, anexe só a nora37-IMG, cole o aviso de 1 prompt e, embaixo, o prompt do take. 15 créditos. Renomeie para nora48-T01-gancho-portal-cancer-escorpiao-peixes.',
 'Copie e renomeie os 7 takes do nora40 (os arquivos do Flow, sem texto): T03 → nora48-T02, T04 → nora48-T03, T05 → nora48-T04, T07 → nora48-T05, T08 → nora48-T06, T11 → nora48-T07 e T12 (a cópia do nora37-T03) → nora48-T08. O T02, o T06, o T09 e o T10 NÃO entram.',
 'Corte de silêncio (M2M FusionZ): os 8 arquivos (nora48-T01 a nora48-T08), “Juntar tudo” LIGADO, Corte seco → nora48-corpo-cortado.',
 'CapCut: projeto novo. No começo, o hook do tsunami (nora47-PRE-A ~3,5 s + nora47-PRE-B 4 s, ou os ~8 s do começo do nora47-montado); corte seco para o nora48-corpo-cortado. Música de sempre −18 dB do Take 1 até o fim (no hook só o som da onda). Exporte SEM texto como nora48-montado e me mande aqui (se passar de 30 MB, link do Drive).',
 'Eu devolvo o nora48-final (caixa do topo, números, legenda, faixa do story e seta). Confira no celular e poste às 19h30 no Insta e no Face, ao vivo. Comentário: no Insta, comente e fixe (sem link); no Face, comente COMO A PÁGINA (já tem o link).']
P['pre_gancho'] = {'titulo_secao': 'Hook: o tsunami do nora47 (já pronto, 0 crédito)', 'duracao': 8, 'tomadas': 2, 'com_rosto': True, 'etapas': [],
 'conceito': HOOK_CONCEITO + ' Depois do hook, corte seco para o quarto à noite: ela começa a falar já com o geodo nas mãos.',
 'modo': 'Não gere nada aqui. No CapCut, use a nora47-PRE-A (~3,5 s) e a nora47-PRE-B (4 s), SEM espelhar.',
 'montagem': '1) nora47-PRE-A: uns 3,5 s (até ela entrar no bunker).\n2) Corte seco para a nora47-PRE-B inteira (4 s: a onda bate, a porta treme, ela olha para a lente).\n3) Corte seco para o nora48-corpo-cortado (o Take 1 no quarto à noite e os 7 takes do corpo A).\n4) No hook fica só o som da onda (sem música).',
 'texto_tela': '', 'edicao': ''}
P['texto_tela'] = {'hook': 'CANCER, SCORPIO, PISCES\n11:11, the most powerful portal\nthe worst is finally over', 'hook_comeca': 'o primeiro quadro do hook',
                   'hook_termina': "the year's most powerful portal.", 'hook_alt': '', 'extras': []}
mt = P['mapa_tela'] = json.loads(json.dumps(P40['mapa_tela']))
mt['numeros'] = [
 {'t': '11:11', 'x': 18, 'y': 12, 'onde': 'alto à esquerda', 'cor_nome': 'branco', 'cor': '#FFFFFF', 'tamanho': 16},
 {'t': '888', 'x': 82, 'y': 30, 'onde': 'no meio à direita, na parede acima do abajur', 'cor_nome': 'ciano', 'cor': '#3DE0FF', 'tamanho': 12},
 {'t': '222', 'x': 18, 'y': 62, 'onde': 'embaixo à esquerda, ao lado da mão', 'cor_nome': 'amarelo-ouro', 'cor': '#FFD21F', 'tamanho': 11}]
mt['estilos'] = [
 {'nome': 'Números fixos espalhados (11:11, 888, 222)', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'uma cor para cada número (abaixo)', 'tamanho': 'um tamanho para cada número (abaixo)',
  'contorno': 'Traço preto + Sombra preta, sem Plano de fundo', 'obs': 'Os do nora40, puxados para dentro da margem do Face (P43): 11:11 branco, 16, X -230 · Y 486; 888 ciano, 12, X 230 · Y 256; 222 amarelo-ouro, 11, X -230 · Y -154. Do 1º quadro do hook ao fim. Eu ponho (P45).'},
 {'nome': 'Caixa do topo: “CANCER, SCORPIO, PISCES” / “11:11, the most powerful portal” / “the worst is finally over”', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto; a 1ª linha (os signos) em vermelho #E53935',
  'tamanho': '10, em 3 linhas (até ~84% da largura)', 'contorno': 'Plano de fundo branco arredondado', 'obs': 'X 0 · Y 397, do 1º quadro do hook até o fim do Take 1. Eu ponho (P45).'},
 {'nome': 'Legenda (eu ponho, P45)', 'fonte': 'Poppins Bold', 'cor': 'branco, em MAIÚSCULAS; palavra-chave em amarelo-ouro #FFD21F', 'tamanho': 'uns 38 px (vídeo 720×1280)', 'contorno': 'preto grosso',
  'obs': 'Do Take 1 ao fim, Y -294, blocos de 2 a 4 palavras. Destaques: Cancer, Scorpio, Pisces, 11:11, portal, money, prosperity, Michael, seal, follow, 222 e stories. Sem legenda no hook.'},
 {'nome': 'Faixa do story: “Your private reading is in my story”', 'fonte': 'Poppins Bold (poppins-bd)', 'cor': 'texto preto, “my story” em vermelho #E53935', 'tamanho': '9, em 1 linha', 'contorno': 'Plano de fundo branco arredondado',
  'obs': 'Do Take 2 (“Don\'t tell anyone”) até o fim, no lugar da caixa do topo (X 0 · Y 397). Eu ponho (P45).'},
 {'nome': 'Seta vermelha (↓)', 'fonte': '—', 'cor': 'vermelho #E53935 com traço preto', 'tamanho': '14', 'contorno': '—',
  'obs': 'Do Take 7 (“Now save this video”) até o fim, embaixo à esquerda (X -288 · Y -333, P43), apontando para a foto do perfil. Eu ponho (P45).'}]
mt['regras'] = ['Faixa da legenda conferida na nora37-IMG: Y -294 (73%), abaixo do geodo e das pontas dos dedos, em cima da blusa preta.',
                'Os números do nora40 foram puxados para dentro da margem do Face (P43). Eu confiro no quadro do vídeo e mexo uns 40 se algum encostar no cabelo, na mão ou no geodo.',
                'No hook (praia e bunker) não há legenda; a caixa do topo e os números entram desde o 1º quadro do hook.']
P['edicao_linha'] = [
 {'quando': '0. No começo', 'texto': 'Hook: nora47-PRE-A + nora47-PRE-B (sem espelhar)', 'como': 'nora47-PRE-A (~3,5 s, até ela entrar no bunker), corte seco, nora47-PRE-B inteira (4 s). Só o som da onda, sem música. Sem texto.'},
 {'quando': '1. Logo depois do hook', 'texto': 'nora48-corpo-cortado (o Take 1 e os 7 takes do corpo A, já juntos)', 'como': 'Corte seco. Ouça a emenda do Take 1 (“…the year\'s most powerful portal”) com o “Don\'t tell anyone what\'s about to happen”.'},
 {'quando': '2. Do Take 1 até o fim', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Volume baixo, por baixo da voz. No hook, não.'},
 {'quando': '3. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e anexe aqui no chat do Code', 'como': '720×1280 (ou 1080×1920), qualidade alta, nome nora48-montado (se passar de 30 MB, link do Drive). Eu ponho a caixa do topo, os números, a legenda, a faixa do story e a seta e devolvo o nora48-final.'}]
P['silencio'] = {'intro': 'Os 8 arquivos do corpo (o nora48-T01 novo e as 7 cópias renomeadas do nora40) entram juntos na ferramenta “M2M FusionZ – Cortar e juntar vídeos”. Deixe assim:',
 'nome': 'nora48-corpo-cortado', 'juntar': 'LIGADO', 'transicao': 'Corte seco', 'ordem': 'pelo nome: nora48-T01 a nora48-T08 (por isso as cópias são renomeadas)',
 'depois': ['Suba os 8 arquivos e espere a Prévia.', 'Confira a ordem: Take 1 (os signos), “Don\'t tell anyone”, a virada, o dinheiro, o Arcanjo Miguel, as correntes, os selos e o 222 com o story.',
            'Aperte play com Resultado marcado e confira que nenhuma 1ª ou última palavra foi cortada.', 'Clique em Cortar e baixar e salve como nora48-corpo-cortado.']}
P['pecas']['lista'] = (
 [{'nome': 'nora47-PRE-A e nora47-PRE-B', 'de': 'nora47', 'tipo': 'hook (pronto)', 'status': 'reutilizar', 'descricao': 'O tsunami do nora47 (praia → bunker; a onda bate na porta). Sem espelhar.'},
  {'nome': 'nora37-IMG', 'de': 'nora37-IMG', 'tipo': 'imagem 1', 'status': 'reutilizar', 'descricao': 'Quarto à noite, abajur rosa, blusa preta canelada, as duas metades do geodo nas mãos (a imagem dos takes do nora40).'},
  {'nome': 'nora48-T01-gancho-portal-cancer-escorpiao-peixes', 'tipo': 'take', 'status': 'gerar', 'creditos': 15, 'descricao': '“' + FALA + '”'}]
 + [{'nome': novo, 'de': velho, 'tipo': 'corpo A', 'status': 'reutilizar', 'descricao': '“' + falas40.get(velho.split(' ')[0], 'Comment 222 to claim this energy, then tap my profile picture. The second part of this sign is waiting in my stories.') + '”',
     'onde': 'Cópia do ' + velho + ', renomeada para ' + novo + '.'} for velho, novo in CORPO]
 + [{'nome': 'nora40-T02, T06, T09 e T10', 'de': 'nora40', 'tipo': 'fora', 'status': 'não usar', 'descricao': 'O “claim this energy” antes da hora (T02), a ameaça das bênçãos (T06) e os “sete minutos” (T09 e T10): o vermelho da copy (P42).'},
    {'nome': 'story-0311 (repost)', 'de': 'story-3110', 'tipo': 'story', 'status': 'reutilizar', 'descricao': 'Repostar antes das 19h30: mesma imagem, texto e adesivo.'}])
P['pecas']['decisao'] = [
 'O gancho do tsunami fica (nora47: 2,1x as views do nora46 no Insta, 58,8% nos 3 s, ~40% aos 8 s). O que não funcionou foi o corpo B: 0 visita ao perfil em 421 views (nora46 + nora47).',
 'Uma variável por vez: hoje o nora48 (corpo A limpo) e o nora49 (corpo B) saem com o MESMO gancho e com o Take 1 da mesma série. Vence o que levar mais gente ao perfil, mais comentários e mais cliques no Tracker.',
 'Corpo A = a copy validada do nicho (Allan e Kaike: copy viral validada até as 1as vendas), que já trouxe 11 a 16 seguidores e 3,2% de comentários; sem os 4 takes vermelhos (P42).',
 'Total: 15 créditos (só o Take 1).']
P['story'] = story(STORY_REPOSTE, False)
P['respostas_face'] = json.loads(json.dumps(P47['respostas_face']))
P['central']['imagem_unica'] = True
save(F, s, m, P)
print('nora48 ok', len(FALA.split()), 'palavras')

# ---------------------------------------------------------------- nora49
F = 'PAINEL-NORA49.html'; s, m, P = load(F)
FALA9 = P['videos'][0]['fala']
R = P['roteiro']
R['titulo'] = 'Gancho do tsunami (espelhado) + Take 1 de Áries, Leão e Sagitário no estúdio + corpo B do nora46'
R['formato'] = 'Hook do tsunami do nora47, ESPELHADO (pronto) + Take 1 NOVO (nora46-IMG; Áries, Leão e Sagitário) + takes 2 a 12 do nora46 (~95 s)'
R['molde_hook'] = ('Gancho do tsunami espelhado (Vinicius Almeida; testado no nora47) + o corpo B. É o par do nora48 desta noite (mesmo gancho, corpo A limpo): '
                   'compara o corpo com o gancho igual (uma variável por vez, Allan Mayer).')
R['duracao_total'] = 95
R['leitura_registro'] = LEIT
P['comentario_fixado']['face'] = ('Aries, Leo, Sagittarius: which of the 3 signs did you feel the most? ✨ Your private reading is right here, open it before the 11:11 portal 🔮 👉 ' + FACE)
P['refs'] = ['Folha de consistência da Nora (blueprint)', 'nora46-IMG (o Take 1; já aprovada)', 'nora47-montado (o vídeo sem texto do nora47: o hook e o corpo do nora46)']
P['pre_gancho'] = {'titulo_secao': 'Hook: o tsunami do nora47, ESPELHADO (já pronto, 0 crédito)', 'duracao': 8, 'tomadas': 2, 'com_rosto': True, 'etapas': [],
 'conceito': HOOK_CONCEITO + ' Espelhado, o quadro não fica igual ao do nora47.',
 'modo': 'Não gere nada aqui. No CapCut, espelhe só o trecho do hook (Editar → Espelhar).',
 'montagem': '1) O hook do tsunami (os ~8 s do começo do nora47-montado), ESPELHADO.\n2) Corte seco para o nora49-T01-cortado (no estúdio).\n3) Corte seco para o corpo do nora46 a partir do Take 2 (“If you\'ve been working so hard”), o mesmo que está no nora47-montado, sem texto.\n4) No hook fica só o som da onda.',
 'texto_tela': '', 'edicao': ''}
c = P['central']
c['passos'] = [
 'Story: não precisa (vale o repost de hoje, antes do nora48).',
 'Take 1 na Central com a MESMA configuração do nora46 (o texto LIVRE do estúdio, nesta seção). Cole só a fala e a linha de movimentação do Take 1. Gere: 1 take de 10 s.',
 'Agente do Flow: conversa nova, anexe só a nora46-IMG, cole o aviso de 1 prompt e, embaixo, o prompt do take. 15 créditos. Renomeie para nora49-T01-gancho-portal-aries-leao-sagitario.',
 'Corte de silêncio só do nora49-T01 (nora49-T01-cortado).',
 'CapCut: projeto novo com o nora47-montado (o vídeo SEM texto que você me mandou). Espelhe só o trecho do hook (0 a ~8 s). Divida no começo do Take 1 do nora47 e no começo do Take 2 (“If you\'ve been working so hard”), apague o Take 1 do nora47 e ponha o nora49-T01-cortado no lugar. Música −18 dB só no Take 1 novo. Exporte SEM texto como nora49-montado e me mande aqui (se passar de 30 MB, link do Drive).',
 'Eu devolvo o nora49-final. Confira no celular e poste às 22h no Insta e no Face, ao vivo. Comentário: no Insta, comente e fixe (sem link); no Face, comente COMO A PÁGINA (já tem o link).']
P['edicao_linha'] = [
 {'quando': 'A. Antes de tudo', 'texto': 'Projeto novo no CapCut com o nora47-montado (sem texto)', 'como': 'É o vídeo que você exportou ontem sem texto (o hook do tsunami, o Take 1 do nora47 e o corpo do nora46).'},
 {'quando': '0. No começo', 'texto': 'Hook do tsunami ESPELHADO', 'como': 'Divida no fim do hook (~8 s, quando ela começa a falar no estúdio) e espelhe só esse trecho (Editar → Espelhar). Só o som da onda.'},
 {'quando': '1. Trocar o Take 1', 'texto': 'nora49-T01-cortado no lugar do Take 1 do nora47', 'como': 'Divida também no começo do Take 2 (“If you\'ve been working so hard”), apague o Take 1 do nora47 e encoste o nora49-T01-cortado. Ouça a emenda: termina em “before eleven eleven, the year\'s most powerful portal”.'},
 {'quando': '2. Só no Take 1 novo', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB', 'como': 'Como no nora47.'},
 {'quando': '3. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e anexe aqui no chat do Code', 'como': '720×1280, qualidade alta, nome nora49-montado (se passar de 30 MB, link do Drive). Eu ponho tudo (caixa do topo, números, legenda, desejo, avaliações, faixa do story e seta) e devolvo o nora49-final.'}]
P['silencio'] = json.loads(json.dumps(P47['silencio']))
P['silencio']['intro'] = 'Só o Take 1 novo (nora49-T01) passa por aqui: o resto vem do nora47-montado. Arraste só o nora49-T01 na ferramenta “M2M FusionZ – Cortar e juntar vídeos” e deixe assim:'
P['silencio']['nome'] = 'nora49-T01-cortado'
P['silencio']['depois'] = ['Suba o nora49-T01 e espere a Prévia.', 'Aperte play com Resultado marcado: confira que a primeira palavra (“Aries”) e a última (“portal”) não foram cortadas.',
                           'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.', 'Clique em Cortar e baixar e salve como nora49-T01-cortado. (A legenda eu ponho aqui, no fim.)']
L = [p for p in P['pecas']['lista'] if p['nome'] not in ('nora37-PRE',) and not p['nome'].startswith('story')]
for p in L:
    if p['nome'].startswith('nora46-T02'):
        p['descricao'] = 'O corpo do nora46 a partir do Take 2, SEM texto, como está no nora47-montado. Não gere, não corte e não junte de novo.'
        p['onde'] = 'No nora47-montado (o vídeo sem texto do nora47), a partir do Take 2.'
P['pecas']['lista'] = [{'nome': 'nora47-PRE-A e nora47-PRE-B (no nora47-montado)', 'de': 'nora47', 'tipo': 'hook (pronto)', 'status': 'reutilizar', 'descricao': 'O tsunami do nora47, ESPELHADO no CapCut.'}] + L
P['pecas']['decisao'] = [
 'É o par do nora48 desta noite: o mesmo gancho (tsunami, aqui espelhado) com o corpo B. Se o nora48 (corpo A limpo) levar mais gente ao perfil e ao story, o corpo A volta; se este levar, o corpo B fica.',
 'Total: 15 créditos (só o Take 1).']
P['story'] = story('✅ NÃO FAÇA STORY PARA ESTE VÍDEO: vale o story-0311 repostado hoje antes do nora48.', True)
save(F, s, m, P)
print('nora49 ok', len(FALA9.split()), 'palavras')
