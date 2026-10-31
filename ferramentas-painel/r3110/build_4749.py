# 31/10/2026 (~11h30): painéis do nora47, nora48 e nora49 = o corpo B do nora46 (portal 11/11, 3 sinais) com um Take 1 NOVO com signos
# em cada um (pedido do aluno: "pode trocar o take 1 do nora47 até o nora49"). Motivo: no Insta, o mesmo corpo com o mesmo Take 1 e só o
# hook trocado não é entregue (nora44: 178 views, contra 1.382 do nora40). Cada painel gera só o seu Take 1 (15 créditos; aluno, 31/10 ~19h).
# Base: PAINEL-NORA46.html (Central, LIVRE, movimentação, mapa da tela, edição). Uso: python3 -I build_4749.py <pasta do repositório>
import re, json, copy, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

def ler(nome):
    s = open(f'{BASE}/{nome}', encoding='utf-8').read()
    return json.loads(re.search(r'const PACOTE = (\{.*?\});\n', s, re.S).group(1))

def gravar(n, p):
    m = open(f'{BASE}/PAINEL-MODELO.html', encoding='utf-8').read()
    assert m.count('const PACOTE = null;') == 1 and 'pk.ordem' in m
    m = m.replace('<title>Painel de Produção</title>', f'<title>Painel nora{n}</title>')
    m = m.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    open(f'{BASE}/PAINEL-NORA{n}.html', 'w', encoding='utf-8').write(m)

P46 = ler('PAINEL-NORA46.html')
V46 = P46['videos']
assert len(V46) == 12 and V46[1]['fala'].startswith("If you've been working so hard")
M0 = V46[0]['movimentacao']
ABRE = M0[:M0.index('her eyes stay on the lens, during the first half')]
FECHA = M0[M0.index(', and from the end of the final sentence'):]

# ---------------- os 3 vídeos ----------------
RESTO = ": the 11:11 portal is about to open, and if this reached you today, it's not a coincidence."
G = [
 {'n': 47, 'suf': 'touro-virgem-capricornio', 'fala_sig': 'Taurus, Virgo or Capricorn', 'lista': 'Taurus, Virgo, Capricorn', 'pt': 'Touro, Virgem e Capricórnio',
  'tags': '#taurus #virgo #capricorn', 'hora': '21h', 'quando': 'hoje (31/10) às 21h (o nora46 saiu às 18h30; 2h30 entre posts)',
  'expr': 'her eyes stay on the lens, during the first half of the take she leans slightly toward the lens with her eyebrows a little raised and an intrigued look, '
          'during the second half she gives one slow knowing nod with a warm half-smile, both hands staying on the desk',
  'hook': 'nora37-PRE', 'hook_nome': 'o geodo que racha (nora37-PRE, sem espelhar)', 'espelhar': False, 'corte': 'uns 3,8 s (logo depois que a pedra abre e aparece o quartzo rosa)',
  'hook_conceito': 'O geodo que racha (nora37-PRE), já gerado em 28/10: a pedra cinza fechada abre nas mãos dela e mostra o quartzo rosa com o símbolo de Vênus dourado. 0 crédito. Foi o hook do nora40 (1.382 views no Insta, 11 seguidores, 16 envios). Sem espelhar.',
  'hook_alt': ''},
 {'n': 48, 'suf': 'cancer-escorpiao-peixes', 'fala_sig': 'Cancer, Scorpio or Pisces', 'lista': 'Cancer, Scorpio, Pisces', 'pt': 'Câncer, Escorpião e Peixes',
  'tags': '#cancer #scorpio #pisces', 'hora': '23h30', 'quando': 'hoje (31/10) às 23h30',
  'expr': 'her eyes stay on the lens, during the first half of the take she tilts her head slightly to one side with a calm, knowing look and a faint smile, '
          'during the second half she raises her left hand to the height of her shoulder on the right side of the frame with the palm open toward the lens for a moment '
          'and then lowers it back to the desk',
  'hook': 'nora27-PRE', 'hook_nome': 'o esconderijo (nora27-PRE)', 'espelhar': False, 'corte': 'uns 4 a 5 s (logo depois da revelação do pacote com a carta)',
  'hook_conceito': 'A revelação do esconderijo (nora27-PRE, viral U7), já gerada em 20/10: ela arranca o tapete, abre o vão no piso e revela o pacote com a carta. 0 crédito. Teve 58,4% nos 3 s no nora27 (o maior da época) e nunca foi usada no Manifestation.',
  'hook_alt': 'Se você não tiver mais o arquivo nora27-PRE, use a nora34-PRE (a pedra escura) espelhada (Editar → Espelhar, só no clipe do hook).'},
 {'n': 49, 'suf': 'aries-leao-sagitario', 'fala_sig': 'Aries, Leo or Sagittarius', 'lista': 'Aries, Leo, Sagittarius', 'pt': 'Áries, Leão e Sagitário',
  'tags': '#aries #leo #sagittarius', 'hora': '17h de 01/11', 'quando': 'amanhã (01/11) às 17h (o 1º horário do dia)',
  'expr': 'her eyes stay on the lens, during the first half of the take her eyebrows lift slightly with a warm, surprised look as if recognizing someone, '
          'during the second half she gives one slow nod and a confident half-smile, both hands staying on the desk',
  'hook': 'nora37-PRE', 'hook_nome': 'o geodo que racha ESPELHADO (nora37-PRE)', 'espelhar': True, 'corte': 'uns 3,8 s (logo depois que a pedra abre e aparece o quartzo rosa)',
  'hook_conceito': 'O mesmo geodo do nora47 (nora37-PRE), ESPELHADO no CapCut (Editar → Espelhar, só no clipe do hook): 0 crédito. Espelhado, o quadro não fica igual ao do nora47.',
  'hook_alt': ''},
]
for g in G:
    g['fala'] = g['fala_sig'] + RESTO
    g['arq'] = f"nora{g['n']}-T01-gancho-portal-{g['suf']}"
    g['mov'] = ABRE + g['expr'] + FECHA
    g['caixa'] = g['lista'].upper() + '\nThe 11:11 portal is opening.\n3 signs it chose you'
assert G[0]['mov'] == M0  # o nora47 usa a mesma linha do Take 1 do nora46

# ---------------- conferências (as mesmas do nora46) ----------------
wc = lambda s: len(s.split())
COMUNS = {'and it','of the','in the','on the','to the','the end','the lens','of her','her head','the take','the first','the last','she gives',
          'one small','her eyes','for one','a soft','and her','at the','her face','the clip','the second','and the','with the','the left',
          'the right','is the','for the','the one','to one','one of','of that','and then','is a','a new','it has','she keeps','her lips'}
def bigr(t):
    w = re.findall(r"[a-z0-9:%'/]+", t.lower()); return {' '.join(w[i:i+2]) for i in range(len(w)-1)}
PROIBIDAS = ['keep your mouth shut', 'before it disappears', 'before they disappear', 'miracle', 'guarantee', 'jealous', 'envy', 'curse', 'block',
             'turnaround', 'opportunit', 'warning', 'seven minutes', 'skip', 'scarcity', 'free']
def divisor(F):
    full = ' '.join(F); sents = [s.strip() for s in re.findall(r'[^.!?]+[.!?]', full)]
    for L in (22, 23, 24, 25):
        tk, cur = [], []
        for s in sents:
            if cur and wc(' '.join(cur + [s])) > L: tk.append(' '.join(cur)); cur = [s]
            else: cur.append(s)
        tk.append(' '.join(cur))
        assert tk == F, ('DIVISOR', L, [wc(x) for x in tk])
for g in G:
    f, m = g['fala'], g['mov']
    assert 18 <= wc(f) <= 22, (g['n'], wc(f))
    ov = (bigr(f) & bigr(m)) - COMUNS
    assert not ov, ('SOBREPOSICAO', g['n'], ov)
    assert m.count('. ') == 0 and m.endswith('.'), ('movimentacao com mais de uma frase', g['n'])
    for pr in PROIBIDAS: assert pr not in f.lower(), ('PROIBIDA', g['n'], pr)
divisor([g['fala'] for g in G])                         # a colagem dos 3 no nora47
divisor([G[0]['fala']] + [v['fala'] for v in V46[1:]])  # e a emenda com o corpo
# Números: os MESMOS do nora46 em todos (31/10 ~13h, aluno: “não tem como duplicar”). O corpo vem do vídeo FINAL do nora46, exportado,
# que já tem os números queimados; no hook e no Take 1 novos o aluno põe os mesmos 3, para o vídeo ficar igual do começo ao fim.
for g in G: g['num'] = copy.deepcopy(P46['mapa_tela']['numeros'])

def xy(x, y): return f'X {round(x/100*720-360)} · Y {round(640-y/100*1280)}'

LEITURA = ('31/10/2026: a leitura completa de LEIA-TUDO-ANTES.md foi feita hoje, das ~00h40 às ~01h15, para o corpo B (lista no painel do nora46). '
  'Para estes 3 painéis (~11h30), que só trocam o Take 1 (a frase com os signos já estava escrita no painel do nora46, em “Depois deste vídeo”), reli: '
  'o pacote do painel do nora46 e o script build3110.py, a seção 1 de LICOES-FLOW-E-PROMPTS.md (checklist, itens 1 a 31), BIBLIOTECA-DE-TAKES.md '
  '(hooks prontos), o ROTEIRO-NORA47 antigo (esconderijo), o CLAUDE.md e as leituras do Insta do nora43, do nora44 e do nora45 (METRICAS-NORA.csv). '
  'Não reli a lista inteira de novo.')

PROXIMOS = {'proximos_intro': 'Próximos Takes 1 do corpo B (15 cada, na nora46-IMG), para 01/11 em diante:',
  'proximos': [
   {'nome': 'nora50-T01-gancho-portal-gemeos-libra-aquario', 'modelo': 'Take 1 com signos (o grupo que falta)', 'custo': '15',
    'gancho': "Gemini, Libra or Aquarius: the 11:11 portal is about to open, and if this reached you today, it's not a coincidence.",
    'texto': 'GEMINI, LIBRA, AQUARIUS / The 11:11 portal is opening. / 3 signs it chose you'},
   {'nome': 'noraNN-T05-sinal-1-amor', 'modelo': 'versão de amor (takes 5 a 8 novos), se o corpo B levar gente ao story', 'custo': '60 (4 takes)',
    'gancho': 'Sign one: you keep dreaming about a love that feels calm, and for the first time, you believe you deserve it.', 'texto': '3 signs love is on its way'}]}

def pacote(g):
    n = g['n']
    p = {k: copy.deepcopy(P46[k]) for k in ('perfil', 'trava_referencia', 'figurino', 'excecao_estilo')}
    p['ocultar_bloco_agente_imagem'] = True
    p['roteiro'] = {
      'id': f"nora{n}-CORPO-B-TAKE1-{g['suf'].upper()}",
      'titulo': f"Corpo B (portal 11/11, 3 sinais) com o Take 1 de {g['pt']}",
      'dor': P46['roteiro']['dor'],
      'formato': f"Hook pronto ({g['hook_nome']}) + Take 1 NOVO com os signos ({g['pt']}) + takes 2 a 12 do nora46 (~90 s)",
      'molde_hook': 'série por signos (P17/P23; signos na fala e na tela, dica do Matheus) sobre o Take 1 do corpo B: o portal + a predestinação saudável do Iorhan',
      'duracao_total': 90,
      'descricao_instagram': f"{g['lista']}: the 11:11 portal is opening. 3 signs it chose you. 🔮\nPick 3 cards in my story and see what your new chapter brings. Follow me + comment 222.\n#manifestation #1111portal {g['tags']}",
      'leitura_registro': LEITURA}
    p['refs'] = ['Nenhuma imagem nova: a nora46-IMG (só ela) no agente']
    p['imagem_reutilizada'] = {'arquivo': 'nora46-IMG',
      'aviso': 'O Take 1 usa a nora46-IMG, a mesma dos 12 takes do nora46 (blazer creme, estúdio claro, microfone à esquerda). Não gere imagem nova.'}
    p['imagens'] = [{'rotulo': 'IMAGEM 1 · nora46-IMG (já aprovada)', 'cena': '(não gerar)'}]
    lista_v = [g]
    p['videos'] = [{'rotulo': f"T01 · nora{x['n']}", 'cena': f"Take 1/12 do nora{x['n']} · Gancho: {x['pt']} + o portal", 'duracao': '10',
                    'primeiro_quadro': 'IMAGEM 1', 'acao': '', 'b_roll': '', 'fala': x['fala'], 'movimentacao': x['mov'], 'arquivo': x['arq']} for x in lista_v]
    p['texto_tela'] = {'hook': g['caixa'], 'hook_comeca': 'o primeiro quadro do hook', 'hook_termina': "it's not a coincidence.", 'hook_alt': '', 'extras': []}
    sig = g['lista']
    p['comentario_fixado'] = {
      'insta': f"{sig}: if you noticed even one of these signs, your new chapter is already on its way. ✨ Tap my photo, open my story and pick your 3 cards: see what it's bringing you in love and money before 11/11. 🔮 Comment 222 to claim it.",
      'face': f"{sig}: if you noticed even one of these signs, your new chapter is already on its way. ✨ Tap my profile picture, open my Story and pick your 3 cards: see what it's bringing you in love and money before 11/11. 🔮 Comment 222 to claim it."}
    esp = ' ESPELHADO (Editar → Espelhar, só no clipe do hook)' if g['espelhar'] else ' (sem espelhar)'
    p['pre_gancho'] = {'titulo_secao': f"CapCut: o hook ({g['hook']}, já pronto) + o Take 1 novo + o corpo do nora46", 'duracao': 4, 'tomadas': 1, 'com_rosto': True, 'etapas': [],
      'conceito': g['hook_conceito'] + (' ' + g['hook_alt'] if g['hook_alt'] else ''),
      'modo': f"Não gere nada aqui. No CapCut, use a {g['hook']}{esp}.",
      'montagem': (f"1) {g['hook']}{esp}: {g['corte']}.\n2) Corte seco para o nora{n}-T01 (cortado e legendado).\n"
                   "3) Corte seco para o vídeo FINAL do nora46 a partir do Take 2 (“If you've been working so hard”), com tudo o que já tem.\n"
                   "4) A caixa do topo já entra no primeiro quadro do hook."),
      'texto_tela': '', 'edicao': ''}

    c = copy.deepcopy(P46['central'])
    c['conferir'] = ('Conferir no Take 1: é a Nora da nora46-IMG (rosto, lua com as estrelinhas, trança, blazer creme e blusa branca); ela fala uma vez só, em inglês, '
                     'com os signos certos e "eleven eleven"; a mão do lado do microfone (esquerdo da imagem) fica na mesa; a do lado direito só faz o gesto do take; '
                     'o microfone não se mexe; sem texto, legenda ou música. Ouça a emenda com o Take 2 do nora46.')
    # Cada painel gera só o seu Take 1 (aluno, 31/10 ~19h: "é pra ter só o take 1 do nora47; no nora48 só o do nora48").
    c['passos'] = [
      'Imagem: não gere. Use a nora46-IMG (a mesma dos 12 takes do nora46).',
      'Central do curso: a MESMA configuração do nora46 (seção “Central do curso”, com o mesmo texto LIVRE). Cole só a fala e a linha de movimentação deste Take 1 (seção “A fala e a movimentação”). Gere e confira: 1 take de 10 s.',
      f"Agente do Flow: conversa nova, anexe só a nora46-IMG, cole o aviso de 1 prompt e, embaixo, o prompt do take (botão COPIAR do take na Central). 15 créditos, conta grande. Renomeie para {g['arq']}.",
      'Me mande a transcrição do Take 1 antes de cortar (P33).',
      f"Corte de silêncio: só o nora{n}-T01, sozinho (os valores da seção “Cortar os silêncios”), salvo como nora{n}-T01-cortado. Legenda automática só desse pedaço (o mesmo estilo do nora46), salva como nora{n}-T01-legendado.",
      'CapCut: projeto novo com o vídeo FINAL do nora46 (exportado, com tudo), cortado no começo do Take 2; antes dele, o hook e o Take 1 novos, com a caixa do topo, os números e a música (passo a passo na seção de texto na tela).',
      f"Postar {g['quando']} no Insta e no Face, ao vivo, sem localização (é falado). Story: nada novo (vale o story-3110 do nora46). Comentário: no Insta, comente e fixe (sem link); no Face, só comente."]
    c['agente'] = {'imagem': 'nora46-IMG',
      'aviso': 'Irei enviar 1 prompt para você. Quero que seja feita uma animação da imagem anexada. Utilize a imagem anexada como frame inicial e frame final do vídeo.',
      'aviso_tag': 'obrigatório: com 1 take o prompt da Central não traz o modo agente',
      'intro': 'Uma imagem e uma mensagem: anexe a nora46-IMG, cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take na Central; com 1 take não existe o bloco “COPIAR TUDO JUNTO”).',
      'passos': ['Abra uma conversa nova no agente do Flow.', 'Anexe a nora46-IMG (só ela).', 'Cole o aviso (acima).',
                 'Embaixo, cole o prompt do Take 1 (botão COPIAR do take na Central).',
                 f"Envie. Renomeie para {g['arq']}. Confira o vídeo e me diga se falhou (o que saiu errado)."]}
    c['colagens'] = [{'titulo': f"só o Take 1 do nora{n}", 'fala': g['fala'], 'movimentacao': [g['mov']], 'takes': [0]}]
    p['central'] = c

    p['story'] = {'ja_postado': True,
      'nota': '✅ NÃO FAÇA STORY PARA ESTE VÍDEO. O story-3110 já está no ar desde 31/10 às 18h30, no Insta e no Face, e vale até ~18h30 de 01/11.'}

    mp = copy.deepcopy(P46['mapa_tela'])
    mp['numeros'] = g['num']
    est = mp['estilos']
    assert est[0]['nome'].startswith('Números') and est[1]['nome'].startswith('Caixa do topo')
    est[0]['obs'] = ('; '.join(f"{u['t']} {u['cor_nome']} {u['cor']}, tamanho {u['tamanho']}, {u['onde']} ({xy(u['x'], u['y'])})" for u in g['num'])
                     + '. Os MESMOS do nora46: o resto do vídeo já vem com eles; ponha só no hook e no Take 1.')
    est[1] = {'nome': f"Caixa do topo: “{sig.upper()}” / “The 11:11 portal is opening.” / “3 signs it chose you”", 'fonte': 'Poppins Bold (poppins-bd)',
              'cor': 'texto preto #000000; a 1ª linha (os signos) em vermelho #E53935', 'tamanho': '10, em 3 linhas (se encostar nas sobrancelhas, 9)',
              'contorno': 'Plano de fundo branco arredondado, sem traço. Luz DESLIGADA',
              'obs': 'Centralizada no topo (X 0 · Y 397), do primeiro quadro do hook até o fim do Take 1.'}
    mp['regras'] = copy.deepcopy(P46['mapa_tela']['regras'])
    mp['regras'][1] = ('Nada nas faixas vermelhas, em cima do rosto, das mãos ou do microfone. Os números ficam na parede, na janela e acima da cabeça: '
                       'se algum cobrir a cabeça ou o braço do microfone, a bandeirinha ou o cabelo, mova uns 40 no X ou no Y.')
    p['mapa_tela'] = mp
    nums = ' · '.join(u['t'] for u in g['num'])
    p['edicao_linha'] = [
      {'quando': 'A. Antes de tudo', 'texto': f'Projeto novo no CapCut (nora{n}) com o vídeo FINAL do nora46',
       'como': 'Importe o vídeo do nora46 já exportado, com tudo (fotos do desejo, avaliações, sinais, legenda, faixa do story, seta, números e música). Não junte os takes de novo nem refaça nada disso.'},
      {'quando': 'B. Cortar o começo antigo', 'texto': 'Dividir no começo do Take 2',
       'como': "Ache o ponto em que ela começa “If you've been working so hard” (o Take 2), use Dividir e apague o pedaço da esquerda (o hook e o Take 1 do nora46)."},
      {'quando': '0. No começo', 'texto': f"Hook: {g['hook']}{esp}",
       'como': f"Arraste a {g['hook']} para o começo da linha do tempo; corte {g['corte']}. Corte seco para o Take 1. Sem legenda no hook." + (' ' + g['hook_alt'] if g['hook_alt'] else '')},
      {'quando': '1. Logo depois do hook', 'texto': f'nora{n}-T01-legendado',
       'como': 'Encostado no hook e, do outro lado, no Take 2 (o vídeo do nora46). Ouça a emenda: termina em “it’s not a coincidence” e o Take 2 entra direto.'},
      {'quando': '2. Do primeiro quadro do hook até o fim do Take 1', 'texto': g['caixa'],
       'como': 'Caixa do topo (X 0 · Y 397, 3 linhas): a 1ª linha (os signos) em vermelho, o resto preto. Estilo em “Estilo de cada texto”.'},
      {'quando': '3. Só no hook e no Take 1', 'texto': nums,
       'como': 'Os mesmos 3 números do nora46 (mesmo lugar, cor e tamanho; lista de estilos abaixo). Do Take 2 em diante eles já estão no vídeo.'},
      {'quando': '4. Só no hook e no Take 1', 'texto': 'Música de sempre (“Ambient Mystical Drone”), −18 dB',
       'como': 'Do Take 2 em diante a música já está no vídeo do nora46.'}]

    L = [{'nome': g['hook'], 'de': g['hook'], 'tipo': 'hook (pronto)', 'status': 'reutilizar', 'descricao': g['hook_conceito']},
         {'nome': 'nora46-IMG', 'de': 'nora46-IMG', 'tipo': 'imagem 1', 'status': 'reutilizar', 'descricao': 'A imagem dos 12 takes do nora46 (blazer creme, estúdio claro, microfone).'}]
    for x in lista_v:
        L.append({'nome': x['arq'], 'tipo': 'take', 'status': 'gerar', 'creditos': 15,
                  'descricao': f"Gancho com os signos ({x['pt']}): “{x['fala']}”",
                  })
    L += [{'nome': 'nora46-T02 a nora46-T12 (o corpo B)', 'de': 'nora46', 'tipo': 'corpo', 'status': 'reutilizar',
           'descricao': 'O vídeo FINAL do nora46, exportado, a partir do Take 2: já tem a legenda, os sinais, as fotos do desejo, as avaliações, a faixa do story, a seta, os números e a música. Não gere, não corte e não junte de novo.',
           'onde': 'Use o vídeo final do nora46 que você exportou (com tudo), a partir do Take 2.'},
          {'nome': 'story-3110', 'de': 'nora46', 'tipo': 'story', 'status': 'reutilizar', 'descricao': 'O story do nora46, no ar desde 31/10 às 18h30 (Insta e Face), vale para este vídeo.', 'onde': 'Já está no ar: não poste outro.'}]
    p['pecas'] = dict({'lista': L, 'decisao': [
      'No Insta, cada post do mesmo corpo leva um Take 1 novo: o nora44, só com o hook trocado, fez 178 views; o nora43, com Take 1 novo, fez 968. Por isso: hook pronto (0) + Take 1 com os signos (15) + o corpo do nora46.',
      'Cada painel gera só o seu Take 1: uma colagem de 1 take na Central e uma mensagem no agente, 15 créditos.',
      'Signos na fala e na caixa do topo (série por signos; dica do Matheus). A frase segue a do nora46 (o portal e “não é coincidência”), sem ameaça (P42).',
      f"Hook: {g['hook_nome']}. O resto vem do vídeo final do nora46, com os mesmos números: só o começo (hook, Take 1 e caixa) é novo."]})
    # --- só o que se usa neste painel (aluno, 31/10 ~19h30) ---
    for sec in p['central']['config']:
        for k in sec['campos']:
            if k['campo'] == 'COLE SUA COPY AQUI': k['valor'] = 'colar a fala do Take 1 (seção “A fala e a movimentação”)'
            if k['campo'] == 'Movimentação': k['valor'] = 'colar a linha do Take 1 (seção “A fala e a movimentação”)'
            if k['campo'] == 'Conferir': k['valor'] = '1 take de 10 s (seção “A fala e a movimentação”)'
            if k['campo'] == 'Copiar': k['valor'] = 'o botão COPIAR do Take 1 (com 1 take não existe o bloco “COPIAR TUDO JUNTO”)'
    p['silencio'] = {
      'intro': f"Só o Take 1 novo (nora{n}-T01) passa por aqui: o resto já vem cortado no vídeo final do nora46. Arraste só o nora{n}-T01 na ferramenta “M2M FusionZ – Cortar e juntar vídeos” e deixe assim:",
      'nome': f"nora{n}-T01-cortado", 'juntar': 'tanto faz (é 1 arquivo só)', 'transicao': 'não se aplica (1 arquivo só)', 'ordem': 'não se aplica (1 arquivo só)',
      'depois': [f"Suba o nora{n}-T01 e espere a Prévia.",
                 f"Aperte play com Resultado marcado: confira que a primeira palavra (“{g['fala_sig'].split(',')[0]}”) e a última (“coincidence”) não foram cortadas.",
                 'Se um corte comeu o fim de uma palavra, arraste a borda dele ou suba a margem de respiro.',
                 f"Clique em Cortar e baixar e salve como nora{n}-T01-cortado.",
                 f"Mande o nora{n}-T01-cortado para o Claude das legendas (o mesmo estilo do nora46, abaixo) e salve como nora{n}-T01-legendado."]}
    mp = p['mapa_tela']
    leg = [e for e in mp['estilos'] if e['nome'].startswith('Legenda automática')][0]
    leg = dict(leg, obs=f"Só no Take 1 (do Take 2 em diante o vídeo do nora46 já vem legendado). Blocos de 2 a 4 palavras, no máximo 2 linhas, na faixa verde (Y -294). Destaques em amarelo-ouro: {sig}, portal e 11:11. Sem legenda no hook.")
    mp['estilos'] = [mp['estilos'][0], mp['estilos'][1], leg]
    mp['seta'] = False
    mp['regras'] = ['Conferido na nora46-IMG: a faixa da legenda (Y -294, 73%) fica nos antebraços, logo acima da borda da mesa, abaixo do microfone e do rosto.',
                    mp['regras'][1]]
    p['ordem'] = ['pecas', 'referencia', 'imagens', 'todos', 'central', 'cenas', 'agente', 'silencio', 'prehook', 'textotela', 'story', 'descricao', 'comentario', 'respostasface', 'fala']
    return p

for g in G:
    gravar(g['n'], pacote(g))
    print(f"ok: PAINEL-NORA{g['n']}", wc(g['fala']), g['arq'])
