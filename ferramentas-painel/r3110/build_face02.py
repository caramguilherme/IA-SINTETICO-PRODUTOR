# 31/10/2026: painel do face02, o 2º teste SÓ do Facebook: o MESMO texto longo do face01 sobre uma IMAGEM PARADA (sem clipe),
# ideia do aluno ("acho que a Mary não usou vídeo, e sim uma imagem"). Teste: imagem parada (face02) x clipe que repete (face01).
# 0 crédito: a imagem é a 3ª das 4 variações do carro (já gerada). Uso: python3 build_face02.py <pasta do repositório>
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

F1 = ler('PAINEL-FACE01.html')
TEXTO = F1['texto_tela']['hook']
p = {k: copy.deepcopy(F1[k]) for k in ('perfil', 'trava_referencia', 'excecao_estilo', 'figurino', 'texto_tela', 'comentario_fixado', 'story')}
p['ocultar_bloco_agente_imagem'] = True
p['clipe_unico'] = True
r = copy.deepcopy(F1['roteiro'])
r.update({
  'id': 'face02-TEXTO-LONGO-IMAGEM-PARADA-CARRO',
  'titulo': 'face02 · teste só do Facebook: o mesmo texto longo do face01 sobre uma IMAGEM PARADA (sem clipe)',
  'formato': 'Texto longo na tela sobre uma imagem parada de 8 s (a Nora no carro, de olhos fechados); 0 crédito',
  'molde_hook': 'o vídeo da 1ª venda da Mary, que parece ser uma imagem parada com o texto por cima (leitura do aluno, 31/10); mesmo texto do face01',
  'descricao_instagram': "Read this before you scroll. 🙏✨\nYour guardian angel left something for you. Pick your 3 cards in my story. Comment 222.\n#manifestation #1111portal #guardianangel",
  'legenda_aviso': '📘 SÓ NO FACEBOOK. Não poste no Insta. Ao vivo (nunca agendar), por volta das 20h45 (entre o vídeo das 19h30 e o das 22h).',
  'leitura_registro': F1['roteiro']['leitura_registro'].replace('Para este painel li de novo:', 'Para este painel (face02) li de novo o pacote do face01 e:')})
p['roteiro'] = r
p['refs'] = ['Nenhuma imagem nova: a face01-IMG, espelhada no CapCut']
p['imagem_reutilizada'] = {'arquivo': 'face01-IMG',
  'aviso': 'Não gere nada. Use a face01-IMG (as outras foram apagadas) e, no CapCut, espelhe SÓ a imagem (Editar → Espelhar), antes de pôr o texto: assim o Face não vê o mesmo quadro do face01.'}
p['imagens'] = [{'rotulo': 'IMAGEM 1 · face01-IMG espelhada (já gerada)', 'cena': '(não gerar)'}]
p['videos'] = [{'rotulo': 'V1', 'cena': 'Imagem parada · texto longo na tela (sem fala)', 'duracao': 8, 'primeiro_quadro': 'IMAGEM 1', 'acao': '', 'b_roll': '',
                'fala': copy.deepcopy(F1['videos'][0]['fala']), 'movimentacao': '(sem Central: não há clipe)', 'arquivo': 'face02'}]
c = copy.deepcopy(F1['central'])
c['conferir'] = 'Conferir: a imagem fica parada os 8 s (sem zoom nem movimento); o texto é o mesmo do face01, letra por letra.'
c['passos'] = [
  'Teste SÓ do Facebook (não posta no Insta). 0 crédito: não gera nada no Flow.',
  'Imagem: a face01-IMG (as outras foram apagadas), espelhada no CapCut (só a imagem, antes do texto).',
  'CapCut (seção de texto na tela): a face01-IMG espelhada, parada por 8 s, sem zoom nem movimento; a camada escura; o MESMO texto do face01; a música a 0 dB.',
  'Postar SÓ no Facebook, ao vivo, por volta das 20h45 (entre o vídeo das 19h30 e o das 22h; o face01 vai ~18h15). Comentário: só comente.',
  'É um teste: imagem parada (face02) x clipe que repete (face01), com o mesmo texto. Me mande os números dos dois no Face com ~3 h e ~12 h (views, views de 3 s, tempo médio, comentários).']
c['colagens'] = [{'titulo': 'sem fala', 'fala': '(sem fala)', 'movimentacao': ['(sem fala)'], 'takes': [0]}]
p['central'] = c
p['edicao_linha'] = [
  {'quando': '1. Base (8 s)', 'texto': 'face01-IMG espelhada e parada', 'como': 'Importe a face01-IMG, espelhe (Editar → Espelhar) e deixe a duração em 8 s. Sem zoom, sem movimento, sem efeito (é o teste da imagem parada).'},
  {'quando': '2. Os 8 s', 'texto': 'Camada escura', 'como': 'Por cima da imagem, um retângulo preto a 35% de opacidade cobrindo a tela inteira (ou Ajustar → Brilho −25).'},
  {'quando': '3. Os 8 s', 'texto': TEXTO, 'como': 'O MESMO texto e o mesmo estilo do face01: um bloco só, centralizado (X 0 · Y 0), MAIÚSCULAS, Poppins Bold branco, tamanho 8 (ou 7), Sombra preta, Luz DESLIGADA, uma linha em branco entre as frases, largura de ~90%.'},
  {'quando': '4. Os 8 s', 'texto': 'Música de sempre (“Ambient Mystical Drone”), 0 dB', 'como': 'A imagem não tem som: a música é o único áudio. Sem legenda automática, sem números fixos, sem seta.'}]
p['pecas'] = {'lista': [
  {'nome': 'face01-IMG', 'de': 'face01-IMG', 'tipo': 'imagem', 'status': 'reutilizar',
   'descricao': 'A mesma imagem do face01, espelhada no CapCut (as outras 3 do carro foram apagadas).'}],
  'decisao': [
   'Ideia do aluno (31/10): o vídeo da Mary parece ser uma imagem parada com o texto por cima, não um clipe.',
   'Teste limpo: o mesmo texto e a mesma imagem do face01, só que parada (e espelhada, para o Face não ver o mesmo quadro).',
   '0 crédito. Se a imagem parada render igual ou mais, os próximos testes de texto longo no Face saem sem clipe.']}
p['ordem'] = ['pecas', 'referencia', 'imagens', 'textotela', 'story', 'descricao', 'comentario', 'respostasface', 'fala']
gravar('PAINEL-FACE02.html', 'Painel face02 (só Face)', p)
print('ok: PAINEL-FACE02')
