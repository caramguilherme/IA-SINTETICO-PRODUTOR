# nora47 (03/11 ~23h15): o bunker vira só o gancho; o Take 1 volta para o estúdio (nora46-IMG, LIVRE e movimentação do nora46).
import re, json, subprocess, sys
F = 'PAINEL-NORA47.html'; BASE = sys.argv[1]
rx = r'const PACOTE = (\{.*?\});\n'
s = open(F, encoding='utf-8').read(); m = re.search(rx, s, re.S); P = json.loads(m.group(1))
old = json.loads(re.search(rx, subprocess.check_output(['git', 'show', BASE + ':' + F]).decode('utf-8'), re.S).group(1))
FALA = P['videos'][0]['fala']
MOV = old['videos'][0]['movimentacao']
def bigr(t):
    w = re.findall(r"[a-z0-9:']+", t.lower()); return {(w[i], w[i+1]) for i in range(len(w)-1)}
ov = (bigr(FALA) & bigr(MOV)) - {('and','it'),('of','the'),('to','the')}
assert not ov, ov
P['videos'][0]['movimentacao'] = MOV
P['central']['colagens'][0]['movimentacao'] = [MOV]
P['central']['config'] = old['central']['config']
P['imagem_reutilizada'] = old['imagem_reutilizada']
P['imagens'] = old['imagens']
P['refs'] = ['Folha de consistência da Nora (blueprint)', 'nora47-PRE-IMG1 (edição e roupa do bunker)', 'nora46-IMG (Take 1, já aprovada)']
P['mapa_tela']['regras'] = old['mapa_tela']['regras'] + ['No hook (praia e bunker) não há legenda; a caixa do topo e os números entram desde o 1º quadro do hook.']
P['central']['agente'] = old['central']['agente']
P['central']['conferir'] = old['central']['conferir'].replace('com os signos certos', 'com os signos certos (termina em "before eleven eleven")')
pg = P['pre_gancho']
for e in pg['etapas']:
    if e['nome'] == 'nora47-IMG':
        e['nome'] = 'nora47-PRE-IMG3'; e['titulo'] = 'Imagem 3: dentro do bunker, de costas para a porta (1º e último quadro do vídeo 2)'
    if e['nome'] == 'nora47-PRE-B':
        e['quadros'] = 'Modo FRAMES. Primeiro quadro: nora47-PRE-IMG3. Último quadro: nora47-PRE-IMG3 (a mesma). 4 s, 9:16, áudio ligado. 7 créditos.'
pg['conceito'] = ('Tomada 1: ela na praia, a onda gigante subindo atrás; ela corre e entra no bunker. Tomada 2: dentro, de costas na porta fechada, a onda bate, a porta treme e espirra água pelas frestas; ela respira e olha para a lente. '
                  'Corte seco para o estúdio: ela começa a falar (Take 1 com a nora46-IMG) e o corpo do nora46 segue. 14 créditos (2 × 7) no hook, conta grande.')
pg['modo'] = 'Primeiro as 3 imagens (nora47-PRE-IMG1, nora47-PRE-IMG2 e nora47-PRE-IMG3). Depois os 2 vídeos em FRAMES, 4 s, 9:16, áudio ligado.'
pg['montagem'] = ('1) nora47-PRE-A: uns 3,5 s (do começo até ela entrar no bunker).\n2) Corte seco para a nora47-PRE-B inteira (4 s: a onda bate, a porta treme, ela olha para a lente).\n'
                  '3) Corte seco para o nora47-T01 (legendado), já no estúdio: é aqui que ela começa a falar.\n4) Deixe o som dos 2 vídeos (rugido, estrondo, água). Sem legenda no hook.')
c = P['central']
c['passos'] = [
 'Story-0311 AGORA, antes de tudo (o link está fora desde 21h10): seção Story deste painel.',
 'Imagens no Flow, nesta ordem: nora47-PRE-IMG1 (só a folha), nora47-PRE-IMG2 (só a IMG1), nora47-PRE-IMG3 (a folha + a IMG1). Confira: é a Nora, blazer creme, a onda atrás e o bunker à direita; na IMG3, sem mãos no quadro e a porta fechada.',
 'Vídeos do hook em FRAMES: nora47-PRE-A (IMG1 → IMG2) e nora47-PRE-B (IMG3 → IMG3). 7 créditos cada, conta grande.',
 'Take 1: a MESMA configuração do nora46 na Central (o mesmo texto LIVRE, que está nesta seção). Cole só a fala e a linha de movimentação do Take 1. Gere: 1 take de 10 s.',
 'Agente do Flow: conversa nova, anexe só a nora46-IMG, cole o aviso de 1 prompt e, embaixo, o prompt do take (botão COPIAR do take na Central). 15 créditos, conta grande. Renomeie para nora47-T01-gancho-onda-touro-virgem-capricornio.',
 'Corte de silêncio só do nora47-T01 (nora47-T01-cortado) e legenda automática só dele (nora47-T01-legendado), no estilo do nora46.',
 'CapCut: projeto novo com o vídeo FINAL do nora46 cortado no começo do Take 2; antes dele, nora47-PRE-A + nora47-PRE-B + o Take 1, com a caixa do topo, os números e a música (seção de texto na tela).',
 'Postar hoje (03/11) às ~23h30 no Insta e no Face, ao vivo, sem localização (se atrasar, 00h30). Comentário: no Insta, comente e fixe (sem link); no Face, comente COMO A PÁGINA com o comentário do Face deste painel (já tem o link).']
L = P['pecas']['lista']
for p in L:
    if p['nome'] == 'nora47-IMG':
        p['nome'] = 'nora47-PRE-IMG3'; p['tipo'] = 'imagem (hook)'; p['descricao'] = 'Dentro do bunker, de costas para a porta fechada (1º e último quadro do vídeo 2).'
    if p['nome'] == 'nora47-PRE-B': p['descricao'] = 'A onda bate na porta (Frames, PRE-IMG3 → PRE-IMG3).'
L.insert(3, {'nome': 'nora46-IMG', 'de': 'nora46-IMG', 'tipo': 'imagem 1', 'status': 'reutilizar', 'descricao': 'A imagem dos 12 takes do nora46 (blazer creme, estúdio claro, microfone): o Take 1 sai dela.'})
P['pecas']['decisao'][2] = 'O bunker é só o gancho; ela começa a falar já no estúdio (Take 1 com a nora46-IMG), para haver uma troca de cenário só, no instante da fala (pergunta do aluno, 03/11 ~23h). Mesma roupa (blazer creme) nos dois.'
P['pecas']['decisao'].insert(3, 'Uma variável por vez (Allan Mayer, 03/11): o corpo do nora46 fica igual; muda só o gancho (e o Take 1).')
R = P['roteiro']
R['titulo'] = 'Gancho do tsunami (praia, onda, bunker) + Take 1 de Touro, Virgem e Capricórnio no estúdio + corpo B do nora46'
R['formato'] = 'Hook NOVO do tsunami em 2 tomadas (praia → bunker; a onda bate na porta) + Take 1 NOVO no estúdio (nora46-IMG; Touro, Virgem e Capricórnio) + takes 2 a 12 do nora46 (~95 s)'
R['leitura_registro'] += ' 03/11 ~23h15: o Take 1 voltou para o estúdio (nora46-IMG, LIVRE e movimentação do nora46; fala nova checada contra a movimentação) depois da pergunta do aluno e da resposta do Allan Mayer (uma variável por vez).'
for e in P['edicao_linha']:
    if e['quando'] == '1. Logo depois do hook':
        e['como'] = 'Encostado na nora47-PRE-B e, do outro lado, no Take 2 (o vídeo do nora46). O Take 1 já é no estúdio. Ouça a emenda: termina em “before eleven eleven” e o Take 2 entra direto.'
s = s[:m.start()] + 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';\n' + s[m.end():]
open(F, 'w', encoding='utf-8').write(s); print('ok')
