# 03/11/2026: face02 v2. O aluno montou o face02 em 02/11 ~21h e vai postar no Insta E no Face (como o face01),
# com 5 s em vez de 8, a 1ª linha e o pedido do story em amarelo-ouro, a imagem escurecida e fade na música.
# Atualiza o PAINEL-FACE02.html já existente (mesmo link KeXyFoszrLZx7BZr42765U): duração, redes, horário,
# legenda igual à do face01, comentário do Insta (antes não tinha), comentário do Face com o teste do link
# (o que ia no nora47), story-0111 no lugar do story-3110 vencido, e escala do texto (botões da direita).
# Uso: python3 -I build_face02_v2.py <pasta do repositório>
import re, json, copy, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

def ler(nome):
    s = open(f'{BASE}/{nome}', encoding='utf-8').read()
    return json.loads(re.search(r'const PACOTE = (\{.*?\});\n', s, re.S).group(1))

def gravar(nome, titulo, p):
    m = open(f'{BASE}/PAINEL-MODELO.html', encoding='utf-8').read()
    assert m.count('const PACOTE = null;') == 1
    m = m.replace('<title>Painel de Produção</title>', f'<title>{titulo}</title>')
    m = m.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    open(f'{BASE}/{nome}', 'w', encoding='utf-8').write(m)

LINK_FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
F1 = ler('PAINEL-FACE01.html')
N47 = ler('PAINEL-NORA47.html')
p = ler('PAINEL-FACE02.html')

r = p['roteiro']
r['titulo'] = 'face02 · Insta e Face: o mesmo texto longo do face01 sobre uma IMAGEM PARADA de 5 s (sem clipe)'
r['formato'] = 'Texto longo na tela sobre uma imagem parada de 5 s (a Nora no carro, de olhos fechados, espelhada); 0 crédito'
r['descricao_instagram'] = F1['roteiro']['descricao_instagram']  # a mesma legenda do face01, letra por letra
r['legenda_aviso'] = '📱📘 INSTA E FACE, ao vivo (nunca agendar). Horário: 00h30 (o fixo da noite) ou o próximo horário fixo (17h). Antes, o story-0111 nos dois.'

p['comentario_fixado'] = {
  'insta': "Your guardian angel left something for you. ✨ Tap my photo and pick your 3 cards in my story: your private reading shows what's coming to you before the 11:11 portal. 🔮",
  'face': "Your guardian angel left something for you. ✨ Pick your 3 cards here and get your private reading before the 11:11 portal 🔮 👉 " + LINK_FB}
p['respostas_face'] = copy.deepcopy(N47.get('respostas_face', {}))

st = copy.deepcopy(N47['story'])
st['nota'] = ('STORY-0111: poste ANTES do face02, no Insta e no Face (o story-3110 venceu em 01/11 ~18h30 e não há story no ar). '
              'Mesma imagem story-3110; só o texto e o adesivo mudam. Ao pôr o adesivo de link, cole o link certo de cada rede e confira na prévia. '
              'Insta (STORYIG): https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks · '
              'Face (FACE): ' + LINK_FB)
p['story'] = st

p['videos'][0]['duracao'] = 5
p['videos'][0]['cena'] = 'Imagem parada · texto longo na tela (sem fala) · 5 s'

c = p['central']
c['conferir'] = 'Conferir: 5 s; a imagem parada e espelhada (só a imagem); o texto com as letras normais, o mesmo do face01; nenhuma ponta de linha embaixo dos botões da direita.'
c['passos'] = [
  'Insta e Face (como o face01). 0 crédito: não gera nada no Flow.',
  'Imagem: a face01-IMG espelhada no CapCut (só a imagem, antes do texto), parada por 5 s.',
  'Story-0111 primeiro, no Insta e no Face (a seção Story deste painel).',
  'Postar ao vivo às 00h30 (ou no próximo horário fixo), com a legenda e o comentário deste painel.',
  'Face: faça o comentário COMO A PÁGINA (não como o seu perfil) e confira de outra conta se ele aparece em cima, com o link clicável. É o teste do link que ia no nora47.',
  'Me mande os números do face02 com ~3 h e ~12 h no Insta e no Face (views, views de 3 s, tempo médio, comentários; no Insta, países).']
p['edicao_linha'] = [
  {'quando': '1. Base (5 s)', 'texto': 'face01-IMG espelhada e parada', 'como': 'Importe a face01-IMG, espelhe (Editar → Espelhar) e deixe a duração em 5 s. Sem zoom, sem movimento, sem efeito.'},
  {'quando': '2. Os 5 s', 'texto': 'Escurecer a imagem', 'como': 'Com a imagem selecionada: Plano de fundo → Cor → preto; Básico → Opacidade → 65%.'},
  {'quando': '3. Os 5 s', 'texto': F1['texto_tela']['hook'], 'como': 'O MESMO texto do face01, um bloco só, centralizado, MAIÚSCULAS, Poppins Bold branco, tamanho 9, Sombra preta, Luz DESLIGADA. Escala do texto 80% (em 100% as pontas das linhas ficam embaixo dos botões da direita). Em amarelo-ouro: "READ THIS BEFORE YOU SCROLL." e "TAP MY PHOTO AND OPEN MY STORY: PICK 3 CARDS"; o resto branco.'},
  {'quando': '4. Os 5 s', 'texto': 'Música de sempre (“Ambient Mystical Drone”), 0 dB', 'como': 'Cortada no mesmo ponto do fim da imagem (5 s); fade-in 0,3 s; fade-out 0,5 s. Sem legenda automática, sem números fixos, sem seta.'}]
p['pecas']['decisao'] = [
  'Ideia do aluno (31/10): o vídeo da Mary parece ser uma imagem parada com o texto por cima, não um clipe.',
  'Mesmo texto e mesma legenda do face01; a imagem parada e espelhada, de 5 s (com imagem parada o recomeço não aparece e quem lê as 92 palavras vê o vídeo várias vezes).',
  'Comparar com o face01 nas mesmas horas de vida, no Insta e no Face. 0 crédito.']
gravar('PAINEL-FACE02.html', 'Painel face02 (Insta e Face)', p)
print('ok: PAINEL-FACE02 v2')
