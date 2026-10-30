# 30/10/2026 ~17h30 (pedido do aluno: "atualiza os painéis do nora44 ao nora46, 3 vídeos hoje; o story novo no painel do nora44").
# Cria o PAINEL-NORA44.html (pedra escura + o vídeo do nora40, 0 crédito, com o story novo) e ajusta o 45 e o 46.
# Uso: python3 build3010b.py <pasta do repositório>  (rodar depois do build3010.py)
import re, json, copy, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build3010 import ler, gravar, num_txt, LEITURA, STORYIG, FACE
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

AGENDA = ('Plano de 30/10 (3 vídeos, refeito às 17h25): story novo story-3010 (painel do nora44) antes do 1º vídeo; '
          '~18h30 nora44 = pedra escura + o vídeo do nora40 (Áries/Leão/Sagitário, 0 crédito); ~21h nora45 = a fita de Touro/Virgem/Capricórnio (12); '
          '~23h30 nora46 = geodo espelhado + Take 1 novo de Câncer/Escorpião/Peixes (15). Face: os mesmos 3, ao vivo, e a nora40-VAR.')
STORY_JA = ('✅ NÃO FAÇA STORY NESTE VÍDEO. Vale o story novo (story-3010) do painel do nora44, postado hoje antes do nora44, no Insta e no Face.')

p45, p46, p40 = ler('45'), ler('46'), ler('40')
STORY = copy.deepcopy(p45['story'])
T01 = 'Aries, Leo or Sagittarius: keep your mouth shut if this video showed up for you on October 29th, 30th or 31st.'

# ======================= nora44 =======================
p = copy.deepcopy(p40)
r = p['roteiro']
r.update({'id': 'nora44-LONGO-HOOK-PEDRA-ARIES-LEAO-SAGITARIO',
  'titulo': 'Longo do corpo A (Manifestation), hook da pedra escura: Áries, Leão e Sagitário (o vídeo do nora40 com o hook trocado, 0 crédito)',
  'formato': 'Hook da pedra escura (nora34-PRE, ~3,5 s) + o vídeo do nora40 inteiro (Take 1 de Áries/Leão/Sagitário + takes 2 a 12), ~100 s. Nada é gerado.',
  'molde_hook': 'pedra escura que racha (viral x5; o hook do nora43, que segurou 69,5% nos 3 s) + corpo A (x1 a x5)',
  'duracao_total': 100,
  'descricao_instagram': "Aries, Leo, Sagittarius: don't scroll past this. 🔮\nThen tap my photo and open my story before it disappears. Comment 222 and follow me.\n#manifestation #astrology #zodiac #usa #usareels",
  'leitura_registro': LEITURA + 'Este vídeo não gera nada (é o projeto do nora40 com o hook trocado); o único prompt é o da imagem do story novo.'})
r.pop('legenda_aviso', None)
p['clipe_unico'] = True  # esconde a Central, o agente e o corte de silêncio: nada a gerar nem a cortar
p['imagem_reutilizada'] = {'arquivo': 'nenhuma (o projeto do nora40 no CapCut)',
  'aviso': 'Nada a gerar neste vídeo (0 crédito): abra o projeto do nora40 no CapCut. Não gere imagem nem take.'}
p['imagens'] = [{'rotulo': 'IMAGEM 1', 'cena': '(não gerar)'}]
p['videos'] = [{'rotulo': 'V1', 'cena': 'Montagem no CapCut (nada a gerar)', 'duracao': '10', 'primeiro_quadro': 'IMAGEM 1', 'acao': '', 'b_roll': '',
  'fala': T01, 'movimentacao': '(não gerar: é o Take 1 do nora40)', 'arquivo': 'nora44 (projeto do nora40)'}]
p['central'] = {'imagem_unica': True, 'config': [], 'agente': {}, 'conferir': '',
  'colagens': [{'titulo': 'nada a gerar', 'fala': '(nada a gerar)', 'movimentacao': ['(nada a gerar)'], 'takes': [0]}],
  'passos': [
    '1) STORY NOVO primeiro (seção “Story”): gere a imagem no Flow anexando SÓ o blueprint (não gasta crédito). Aprove só se: é a Nora (lua e 3 estrelinhas na bochecha do lado esquerdo da imagem); exatamente 3 cartas viradas para baixo, iguais, sem letras; faixa de cima vazia (parede escura) e faixa de baixo vazia (manta). Renomeie para story-3010.',
    '2) Poste o story no Insta (link STORYIG) e no Face (link FACE), com o texto no topo e o adesivo embaixo. Na prévia, confira que o link do Insta termina em utm_content=STORYIG e o do Face em utm_content=FACE.',
    '3) nora44 (0 crédito): abra o projeto do nora40 no CapCut e salve uma cópia como nora44. Troque o hook do geodo pela nora34-PRE (veja “Pré-gancho”). Mude só os números fixos (veja “Edição: texto na tela”). Todo o resto fica igual ao nora40.',
    '4) Confira um quadro do hook (a pedra) e um do corpo (o geodo): nenhum número em cima do rosto, das mãos ou da pedra.',
    '5) Postar em 30/10 por volta das 18h30 no Insta e no Face, ao vivo, sem localização. Comentário: no Insta, comente e fixe (sem link); no Face, só comente.',
    '6) Face: se a nora40-VAR ainda não saiu, ela vai entre o nora44 e o nora45 (~19h45).']}
p['pre_gancho'] = {'titulo_secao': 'Pré-gancho (o do nora34: não gerar)', 'duracao': 4, 'tomadas': 1, 'com_rosto': True, 'etapas': [],
  'conceito': 'A pedra escura que racha do nora34 (viral x5), já gerada: 0 crédito. Foi o hook do nora43, o longo que mais segurou os 3 primeiros segundos (69,5%).',
  'modo': 'Não gere nada aqui. No CapCut, use a nora34-PRE como está (sem espelhar).',
  'montagem': '1) Abra o projeto do nora40 e salve uma cópia como nora44.\n2) Apague o hook do geodo (nora37-PRE) e ponha a nora34-PRE no lugar, uns 3,5 s (corte logo depois que as metades abrem).\n3) Corte seco para o corpo (o mesmo do nora40).\n4) A caixa do topo continua do primeiro quadro do hook até o fim do Take 1.',
  'texto_tela': '', 'edicao': ''}
NUM44 = [
  {'t': '222', 'x': 50, 'y': 11.5, 'onde': 'alto, no centro', 'cor_nome': 'rosa-choque', 'cor': '#FF4FD8', 'tamanho': 15},
  {'t': '888', 'x': 12, 'y': 30, 'onde': 'à esquerda, no meio', 'cor_nome': 'verde-limão', 'cor': '#7CFF4F', 'tamanho': 12},
  {'t': '11:11', 'x': 9, 'y': 55, 'onde': 'embaixo à esquerda', 'cor_nome': 'amarelo-ouro', 'cor': '#FFD21F', 'tamanho': 11}]
p['mapa_tela']['numeros'] = NUM44
for e in p['mapa_tela']['estilos']:
    if e['nome'].startswith('Números'):
        e['nome'] = 'Números fixos espalhados (222, 888, 11:11)'; e['obs'] = num_txt(NUM44)
p['mapa_tela']['regras'][0] = ('Números fixos espalhados (um em cima, um no meio, um mais embaixo), novos (não repetem os do nora40). '
  'Confira o 1º quadro do hook da pedra escura (nora34-PRE): se um número cobrir a pedra ou o rosto, suba ou desça uns 60 no Y.')
for x in p['edicao_linha']:
    if x['quando'].startswith('0.'):
        x['texto'] = 'Pré-gancho (nora34-PRE, uns 3,5 s)'
    if x['quando'].startswith('2.'):
        x['texto'] = '222  ·  888  ·  11:11  (espalhados, lugares novos)'
        x['como'] = 'Troque os números do nora40 por estes, parados do primeiro ao último quadro: ' + num_txt(NUM44)
st = copy.deepcopy(STORY)
st['nota'] = ('STORY NOVO (30/10, story-3010): poste ANTES do nora44, no Insta e no Face. Se você já repostou o story-2810 hoje, este entra por cima (os dois ficam no ar). '
              'Ao pôr o adesivo de link, cole o link certo de cada rede e confira na prévia. '
              f'Insta (STORYIG): {STORYIG} · Face (FACE): {FACE}')
p['story'] = st
p['pecas'] = {'lista': [
  {'nome': 'story-3010', 'tipo': 'imagem do story', 'status': 'gerar', 'creditos': 0,
   'descricao': 'Do blueprint: a Nora sentada na cama à noite, blusa creme, 3 cartas viradas para baixo na manta esmeralda, o dedo sobre a do meio. Não gasta crédito.',
   'base': 'O story-2810 caiu de 23,5% para 8,7% de clique e mais da metade de quem vê já segue: imagem e texto novos.', 'serve': 'Story de 30/10 e 31/10.'},
  {'nome': 'nora34-PRE', 'de': 'nora34-PRE', 'tipo': 'pré-gancho (do nora34)', 'status': 'reutilizar', 'creditos': 7, 'descricao': 'A pedra escura que racha, sem espelhar.'},
  {'nome': 'projeto do nora40', 'de': 'projeto do nora40 no CapCut', 'tipo': 'o vídeo inteiro (Take 1 + takes 2 a 12)', 'status': 'reutilizar', 'creditos': 165,
   'fala': T01, 'descricao': 'Salve uma cópia como nora44 e troque só o hook e os números.'}],
  'decisao': [
    'O dia atrasou: o primeiro vídeo sai sem gerar nada. O nora40 (geodo) e o nora43 (pedra escura) foram os vídeos com mais seguidores (11 e 10), envios (16 e 19) e salvos (20 e 18) da Nora; a pedra segurou mais os 3 s (69,5%).',
    'Combinação nova no Insta (pedra + corpo de Áries/Leão/Sagitário); o Take 1 com 29, 30 e 31 ainda vale hoje.',
    'Story novo neste painel, por ser o 1º vídeo do dia.', AGENDA]}
gravar('44', p)

# ======================= nora45: sem story (vale o do nora44), horário novo =======================
p45['story'] = {'ja_postado': True, 'nota': STORY_JA}
p45['central']['passos'] = [x.replace('Postar em 30/10 por volta das 20h no Insta e no Face, ao vivo. No Insta, ponha a localização Los Angeles, California. Antes de postar, poste o STORY NOVO (seção Story).',
                                      'Postar em 30/10 por volta das 21h no Insta e no Face, ao vivo. No Insta, ponha a localização Los Angeles, California. O story novo (story-3010, do painel do nora44) já tem de estar no ar.')
                            for x in p45['central']['passos']]
assert any('por volta das 21h' in x for x in p45['central']['passos'])
p45['pecas']['lista'] = [x for x in p45['pecas']['lista'] if x['nome'] != 'story-3010']
p45['pecas']['decisao'] = [x for x in p45['pecas']['decisao'] if not x.startswith('Story novo') and not x.startswith('Plano de 30/10')] + [AGENDA]
gravar('45', p45)

# ======================= nora46: hook reaproveitado sem prompts vazios, horário novo =======================
p46['pre_gancho']['etapas'] = []
p46['story']['nota'] = STORY_JA
p46['central']['passos'] = [x.replace('por volta das 22h30', 'por volta das 23h30') for x in p46['central']['passos']]
assert any('23h30' in x for x in p46['central']['passos'])
p46['pecas']['decisao'] = [x for x in p46['pecas']['decisao'] if not x.startswith('Plano de 30/10')] + [AGENDA]
gravar('46', p46)
print('ok')
