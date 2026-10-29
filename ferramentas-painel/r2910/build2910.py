# 29/10/2026: painéis do nora40 (longo do corpo A, hook do geodo), nora41 (placa em cena nova), nora42 (longo, hook da placa)
# e nora43 (longo, hook da pedra escura). Base: PAINEL-NORA37.html (Central, LIVRE, mapa) e PAINEL-NORA41.html (placa).
# Uso: python3 build2910.py <pasta do repositório>
import re, json, copy, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from falas2910 import takes, checar, SIGNOS, T11_FALA, CORPO, mov, t01
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'

def ler(nome):
    s = open(f'{BASE}/{nome}', encoding='utf-8').read()
    return json.loads(re.search(r'const PACOTE = (\{.*?\});\n', s, re.S).group(1))

def gravar(n, p):
    m = open(f'{BASE}/PAINEL-MODELO.html', encoding='utf-8').read()
    assert m.count('const PACOTE = null;') == 1
    m = m.replace('<title>Painel de Produção</title>', f'<title>Painel nora{n}</title>')
    m = m.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';')
    open(f'{BASE}/PAINEL-NORA{n}.html', 'w', encoding='utf-8').write(m)

P37, P41 = ler('PAINEL-NORA37.html'), ler('PAINEL-NORA41.html')

LEITURA = ('29/10/2026: antes de montar este painel li inteiros, com a ferramenta de leitura, nesta sessão, todos os arquivos de LEIA-TUDO-ANTES.md: '
  'FATOS-DO-ALUNO.md, CLAUDE.md, 00-LEIA-PRIMEIRO.md, BRIEFING-MANIFESTACAO.md, PROJETO-Dana.md, BRIEFING-LOVECHART.md, LICOES-FLOW-E-PROMPTS.md, '
  'COMUNIDADE-E-ESTRATEGIA.md (com o Discord de 28 e 29/10), DNA Visual - Dana.md, DNA Visual - Nora.md, DNA Visual - Nora v2.md, REGISTRO-DE-PERSONAS.md, '
  'hooks.md, Formatos Narrativos - Problema e Cenario.md, Exemplos de Roteiros - 2 Formatos.md, ctas.md, COMUNICACAO-VISCERAL-E-FALADA.md, '
  'BIBLIOTECA-BODIES.md, BIBLIOTECA-COLD-READING.md, BIBLIOTECA-COPY.md, BIBLIOTECA-COPY-100-ROTEIROS.md, PESQUISA-PUBLICO.md, BIBLIOTECA-VIDEOS-VIRAIS.md, '
  'BIBLIOTECA-PRE-GANCHOS.md, Prompts.txt, CHECKLIST-DE-PRODUCAO.md, PAPEL-AGENTE-FLOW.md, GUIA-CREATIVE-HUB.md, os PLANO-CREDITOS-*, os PASSO-A-PASSO-*, '
  'EXEMPLO-ROTEIRO-APROVADO-FIGADO.md, EXEMPLO-PACOTE-FIGADO.md, PAINEL-MODELO.html, METRICAS-NORA.csv, METRICAS-NORA-LEIA.md, BIBLIOTECA-DE-TAKES.md, '
  'os ROTEIRO-R001 a ROTEIRO-NORA41, ROTEIRO-LOVECHART-RESERVA, os 3 RESERVA-ROTEIRO-*, os STORY-* e os TAKE-NOVO-*; e os pacotes dos painéis do nora35, '
  'nora37, nora39, nora40 e nora41. Não li (não se aplicam a este pedido): FOTO-PERFIL-DANA.md, PROMPT-BLUEPRINT-COMUNIDADE.md, PLANO-MVM-LEGACY-APPYON.md e os PDFs.')

AGENDA = ('Os signos do dia (29/10) ficam divididos entre os 4 vídeos do Insta: 17h nora40 Áries/Leão/Sagitário (longo, hook do geodo), '
          '19h30 nora41 placa Câncer/Escorpião/Peixes (cena nova), 22h nora42 Gêmeos/Libra/Aquário (longo, hook da placa), '
          '00h30 nora43 Touro/Virgem/Capricórnio (longo, hook da pedra escura). No Face, os mesmos 4 ao vivo e, às 14h, a nora39-VAR.')
DOR = 'as bênçãos e o dinheiro que não chegam; a virada que nunca vem (Manifestation, ângulo positivo de predestinação, P41)'
STORY_JA = ('✅ NÃO FAÇA STORY NESTE VÍDEO. O story das 3 cartas (story-2810) repostado hoje (29/10) antes das 16h30, no Insta e no Face, '
            'vale para este vídeo. Ele expira ~16h30 de 30/10.')
COMENTAR = 'Comentário: no Insta, comente e fixe (sem link); no Face, só comente (não fixa mais).'

def comentario(sig):
    return {'insta': f"{sig}, this one is yours. 🔥 PART 2 of this sign is in my story: pick 3 cards and see what's coming for you. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222 and follow me so you don't miss your sign's next message.",
            'face': f"{sig}, this one is yours. 🔥 PART 2 of this sign is in my Story: pick 3 cards and see what's coming for you. Tap my profile picture NOW, it's gone in 24 hours. Comment 222 and follow me so you don't miss your sign's next message."}
def legenda(sig, meio="if this reached you, it's not by chance"):
    return f"{sig}: {meio}. 🔮\nComment 222, follow me and tap my photo NOW: part 2 of this sign is in my story.\n#manifestation #astrology #zodiac #usa #usareels"

# ---------------- partes comuns dos longos (nora40, nora42, nora43) ----------------
def videos_de(T, total):
    return [{'rotulo': f'V{i+1}', 'cena': f'Take {int(a[1+a.index("-T"):][1:3])}/{total} · {c}', 'duracao': '10', 'primeiro_quadro': 'IMAGEM 1',
             'acao': '(ver movimentação)', 'b_roll': '', 'fala': f, 'movimentacao': m, 'arquivo': a} for i, (a, c, f, m) in enumerate(T)]

def mapa_longo():
    mp = copy.deepcopy(P37['mapa_tela'])
    for e in mp['estilos']:
        if e['nome'].startswith('Caixa do topo'):
            e['obs'] = 'Centralizada no topo (X 0 · Y 397), do primeiro quadro do hook até o fim do Take 1. Igual nos vídeos da série.'
        if e['nome'].startswith('Faixa do story'):
            e['obs'] = 'Do Take 2 até o fim, no mesmo lugar da caixa do topo (X 0 · Y 397), logo que ela sai.'
        if e['nome'].startswith('Seta'):
            e['obs'] = 'Do Take 10 até o fim. Embaixo à esquerda, apontando para baixo, para a foto do perfil e o botão de seguir (X e Y na tabela do CapCut).'
    return mp

def edicao_longo(n, hook_txt, hook_desc, caixa):
    return [
        {'quando': '0. Antes do Take 1', 'texto': hook_txt, 'como': 'Corte seco para o corpo cortado. Veja a montagem na seção do pré-gancho.'},
        {'quando': '1. Do primeiro quadro do hook até o fim do Take 1', 'texto': caixa,
         'como': 'Caixa branca arredondada no topo (X 0 · Y 397), texto preto, a palavra “attention” em vermelho. Igual em todos os vídeos da série.'},
        {'quando': '2. O vídeo todo (do primeiro quadro do hook ao fim)', 'texto': '222  e  11:11',
         'como': 'Números fixos nos cantos de cima, em amarelo-ouro: 222 à esquerda e 11:11 à direita, acima da caixa do topo.'},
        {'quando': '3. Do Take 1 ao fim', 'texto': 'Legenda na tela (automática), em blocos de 2 a 4 palavras',
         'como': 'Faixa verde do mapa (Y -294). Destaque em amarelo-ouro: money, prosperity, blessings, seal, follow e 222.' + (' No hook não há legenda (sem fala).' if hook_desc else '')},
        {'quando': '4. Do Take 2 até o fim', 'texto': 'The second part is in my Stories ⭐',
         'como': 'Faixa no topo, no lugar da caixa (X 0 · Y 397): caixa branca arredondada, texto preto, “my Stories” em vermelho. Começa em “Don’t tell anyone”.'},
        {'quando': '5. Do Take 10 até o fim', 'texto': 'Seta vermelha (↓)',
         'como': 'Embaixo à esquerda, apontando para baixo, para a foto do perfil e o botão de seguir. Começa em “Now save this video”.'},
        {'quando': '6. O vídeo todo', 'texto': 'Música de sempre (“Ambient Mystical Drone”, da biblioteca do CapCut), −18 dB', 'como': 'Volume baixo, por baixo da voz.'},
    ]

def reuso_corpo(n):
    # cópias dos takes 2 a 11 do nora40 para o nora42 e o nora43
    L = []
    for suf, cena, fala in CORPO:
        L.append({'nome': f'nora40-{suf}', 'de': f'nora40-{suf}', 'tipo': 'corpo (do nora40)' if 'cta' not in suf else 'CTA (do nora40)',
                  'status': 'reutilizar', 'creditos': 15, 'fala': fala,
                  'descricao': f'Para a ferramenta de corte, renomeie a cópia para nora{n}-{suf}.'})
    L.append({'nome': 'nora40-T11-cta-222-story', 'de': 'nora40-T11-cta-222-story (a cópia do nora37-T03)', 'tipo': 'CTA (do nora37)',
              'status': 'reutilizar', 'creditos': 15, 'fala': T11_FALA,
              'descricao': f'Para a ferramenta de corte, renomeie a cópia para nora{n}-T11-cta-222-story.'})
    return L

def central_1take(n, T, extra_passos):
    c = copy.deepcopy(P37['central'])
    a, cena, f, m = T[0]
    c['conferir'] = 'Conferir: é a Nora da nora37-IMG; as metades do geodo nas mesmas mãos; a fala sai completa, uma vez só, com a mesma voz dos takes do nora40. Ouça a emenda do Take 1 com o Take 2.'
    c['passos'] = extra_passos + [
        'Take 1, na conta de 404. Imagem: não gere. Use a nora37-IMG.',
        'Central do curso: a MESMA configuração do nora37 e do nora40 (seção “Central do curso”, com o texto LIVRE). Cole só a fala do Take 1 e a linha de movimentação dele. Clique em GERAR PROMPT DE ANIMAÇÃO e confira: 1 take de 10 s.',
        f'Agente do Flow: anexe a nora37-IMG (só ela), cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take). 15 créditos. Renomeie para {a}. Dá para gerar logo depois dos takes do nora40.',
        f'Os takes 2 a 11 NÃO são gerados: são os do nora40 (lista em “Nomes e reaproveitamento”). Faça uma cópia de cada um e renomeie de nora40-T02… para nora{n}-T02… (2 dígitos, para a ferramenta de corte juntar na ordem).',
        'Me mande a transcrição do Take 1 e a emenda com o Take 2 antes de postar.',
        f'Corte de silêncio (seção “Cortar os silêncios”): suba nora{n}-T01 a nora{n}-T11 de uma vez, com “Juntar tudo” ligado e Corte seco. CapCut: o hook, o corpo cortado e os textos da seção de texto na tela.',
    ]
    c['agente'] = {'imagem': 'nora37-IMG',
                   'aviso': 'Irei enviar 1 prompt para você. Quero que seja feita uma animação da imagem anexada. Utilize a imagem anexada como frame inicial e frame final do vídeo.',
                   'aviso_tag': 'obrigatório: com 1 take o prompt da Central não traz o modo agente',
                   'intro': 'Uma imagem e uma mensagem: anexe a nora37-IMG, cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take na Central; com 1 take não existe o bloco “COPIAR TUDO JUNTO”).',
                   'passos': ['Abra uma conversa nova no agente do Flow.', 'Anexe a nora37-IMG (só ela).', 'Cole o aviso (acima).',
                              'Embaixo, cole o prompt do Take 1 (botão COPIAR do take na Central).',
                              f'Envie. Renomeie para {a}. Confira o vídeo e me diga se falhou (o que saiu errado).']}
    c['colagens'] = [{'titulo': 'só o Take 1', 'fala': f, 'movimentacao': [m], 'takes': [0]}]
    return c

def base_longo():
    p = {k: copy.deepcopy(P37[k]) for k in ('perfil', 'trava_referencia', 'figurino')}
    p['excecao_estilo'] = ''
    p['imagem_reutilizada'] = {'arquivo': 'nora37-IMG (a imagem dos takes do nora37)',
                               'aviso': 'Os takes usam a nora37-IMG, a mesma do nora37 e do nora39 (as metades do geodo, rosto calmo). Não gere imagem nova.'}
    p['imagens'] = [{'rotulo': 'IMAGEM 1', 'cena': '(a nora37-IMG, não gerar)'}]
    p['mapa_tela'] = mapa_longo()
    return p

# ================= nora40: longo do corpo A, hook do geodo =================
T40 = takes('nora40'); checar(T40)
p40 = base_longo()
p40['roteiro'] = {
    'id': 'nora40-LONGO-CORPO-A-ARIES-LEAO-SAGITARIO',
    'titulo': 'Longo do corpo A (Manifestation), hook do geodo: Áries, Leão e Sagitário',
    'dor': DOR,
    'formato': 'Hook visual pesado (o geodo do nora37, 4 s) + corpo A dos virais em 11 takes (~90 s): signos e datas → segredo → virada → dinheiro → a única ameaça → São Miguel → correntes → 7 minutos → mande para si → selos (salvar e seguir) → 222 e story',
    'molde_hook': 'geodo que racha (x1, x2 e x5; o Lucas usa o mesmo hook); fala = corpo A quase palavra por palavra (x1 a x5, w3 a w5, L1), com o selo de seguir do a4/a5',
    'duracao_total': 92,
    'descricao_instagram': legenda('Aries, Leo, Sagittarius'),
    'leitura_registro': LEITURA}
p40['refs'] = ['Nenhuma imagem nova: a nora37-IMG']
p40['videos'] = videos_de(T40, 11)
p40['texto_tela'] = {'hook': 'Aries, Leo, Sagittarius, pay very close attention', 'hook_comeca': 'o primeiro quadro do pré-gancho',
                     'hook_termina': 'October 29th, 30th or 31st', 'hook_alt': '', 'extras': []}
p40['comentario_fixado'] = comentario('Aries, Leo, Sagittarius')
p40['pre_gancho'] = {'titulo_secao': 'Pré-gancho (o do nora37: não gerar)', 'duracao': 4, 'tomadas': 1, 'com_rosto': True,
    'conceito': 'O geodo que racha do nora37 (viral x1), sem espelhar (o nora39 usou espelhado). O Lucas usa o mesmo hook nos vídeos dele.',
    'modo': 'Não gere nada aqui. No CapCut, use a nora37-PRE como está (sem espelhar).',
    'montagem': '1) nora37-PRE: uns 3,5 s.\n2) Corte seco para o corpo cortado (nora40-cortado: os takes 1 a 11).\n3) A caixa do topo já entra no primeiro quadro do pré-gancho.',
    'texto_tela': '', 'edicao': ''}
c40 = copy.deepcopy(P37['central'])
c40['conferir'] = ('Conferir em cada take: é a Nora v2 (rosto, lua com as estrelinhas, trança e blusa preta iguais à imagem); as duas metades do geodo nas mesmas mãos, '
                   'abertas, com o símbolo dourado na metade da direita da imagem; a fala sai completa, uma vez só, em inglês; sem texto, legenda ou música. Renomeie com o nome da lista.')
c40['passos'] = [
    'Story, antes das 16h30 (o de ontem expira ~16h30): poste de novo o story-2810 no Insta e no Face (seção “Story”). Não gera nada.',
    'Imagem e pré-gancho: não gere. Os takes usam a nora37-IMG e o hook é a nora37-PRE (conta de 404).',
    'Central do curso: a MESMA configuração do nora37 (seção “Central do curso”, com o texto LIVRE). Cole a fala inteira e as 10 linhas de movimentação (seção “A fala e a movimentação”). Confira: 10 takes de 10 s.',
    'Agente do Flow: anexe só a nora37-IMG, cole o aviso e, embaixo, o “COPIAR TUDO JUNTO” da Central, sem editar. 150 créditos (conta de 404: ~337 → ~187). Renomeie os takes com os nomes do painel (T01 a T10, com 2 dígitos).',
    'O Take 11 NÃO é gerado: faça uma cópia do nora37-T03-cta-222-story e renomeie para nora40-T11-cta-222-story.',
    'Guarde os takes 2 a 11: o nora42 (22h) e o nora43 (00h30) usam as cópias. Se der, gere já os Takes 1 deles (painéis do nora42 e do nora43), na mesma nora37-IMG.',
    'Me mande a transcrição dos 10 takes novos antes de postar.',
    'Corte de silêncio (seção “Cortar os silêncios”): suba nora40-T01 a nora40-T11 de uma vez, com “Juntar tudo” ligado e Corte seco. CapCut: nora37-PRE (sem espelhar), corpo cortado e os textos da seção de texto na tela.',
    'Postar em 29/10 às 17h no Insta e no Face, ao vivo, sem localização (é falado). ' + COMENTAR,
]
c40['agente']['imagem'] = 'nora37-IMG'
c40['agente']['aviso'] = ('Vou te enviar 10 prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um '
                          'com o devido número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.')
c40['agente']['passos'] = ['Abra uma conversa nova no agente do Flow.',
    'Nas configurações do agente, ligue a opção de gerar sem pedir aprovação e salve antes de enviar.',
    'Anexe só a nora37-IMG (o blueprint não vai no agente).',
    'Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.',
    'Envie. O agente gera os 10 vídeos; confira cada um e me diga qual falhou (take e problema).',
    'Se ele gerar menos de 10, abra um projeto novo no Flow e mande de novo só os que faltaram.']
c40['colagens'] = [{'titulo': 'nora40 (10 takes)', 'fala': ' '.join(t[2] for t in T40), 'movimentacao': [t[3] for t in T40], 'takes': list(range(10))}]
p40['central'] = c40
st = copy.deepcopy(P37['story'])
st['nota'] = ('Hoje (29/10), antes das 16h30, quando o story de ontem expira: poste de novo o story-2810 (a mesma imagem das 3 cartas; não gere outra), '
              'com o mesmo texto no topo e o mesmo adesivo embaixo, e os mesmos links do Manifestation (STORYIG no Insta, FACE no Face). '
              'Só se você não tiver mais a imagem: gere com o prompt abaixo (anexe só o blueprint).')
p40['story'] = st
p40['edicao_linha'] = edicao_longo(40, 'Pré-gancho (nora37-PRE, sem espelhar, uns 3,5 s)', False, 'Aries, Leo, Sagittarius, pay very close attention')
L40 = [{'nome': 'nora37-PRE', 'de': 'nora37-PRE', 'tipo': 'pré-gancho (do nora37)', 'status': 'reutilizar', 'creditos': 7, 'descricao': 'Sem espelhar.'},
       {'nome': 'nora37-IMG', 'de': 'nora37-IMG', 'tipo': 'imagem 1 (do nora37)', 'status': 'reutilizar', 'descricao': 'Primeiro e último quadro dos 10 takes novos.'}]
for (a, cena, f, m) in T40:
    L40.append({'nome': a, 'tipo': 'gancho' if '-T01-' in a else ('CTA' if 'cta' in a else 'corpo'), 'status': 'gerar', 'creditos': 15,
                'descricao': f'{cena}: “{f}”', 'base': 'Corpo A (x1 a x5, w3 a w5, L1)' + (' + selo de seguir (a4/a5)' if 'T10' in a else ''),
                'serve': 'Só deste vídeo (cada grupo de signos tem o seu Take 1).' if '-T01-' in a else 'nora42 e nora43 (cópia renomeada) e os próximos longos.'})
L40.append({'nome': 'nora37-T03-cta-222-story', 'de': 'nora37-T03-cta-222-story', 'tipo': 'CTA (do nora37)', 'status': 'reutilizar', 'creditos': 15,
            'fala': T11_FALA, 'descricao': 'Take 11. Para a ferramenta de corte, renomeie a cópia para nora40-T11-cta-222-story.'})
p40['pecas'] = {'lista': L40, 'decisao': [
    'O longo do corpo A volta como o principal (Lucas, 28/10: “exatamente daquele jeito”, hook visual + copy longa; os dele passam de 2 min). Mesmo vídeo no Insta e no Face.',
    'Barato: os 10 takes novos na nora37-IMG (150) + o nora37-T03 como Take 11 + o geodo do nora37 como hook (0).',
    'Take 10 troca o toque duplo por seguir (a4/a5): a meta do dia é visita ao perfil e seguidor; o comentário e a legenda pedem o mesmo.',
    'A faixa do story entra no Take 2, não só no fim: o tempo médio dos falados é de 5 a 8 s.',
    AGENDA],
    'proximos_intro': 'Os takes 2 a 11 deste vídeo servem ao nora42 e ao nora43 (cópias renomeadas). Os Takes 1 deles estão nos painéis de cada um; dá para gerar logo depois destes, na mesma nora37-IMG.',
    'proximos': [{'nome': f'nora{n}-T01-gancho-{SIGNOS["nora"+n][2]}', 'modelo': h, 'custo': '15 (hoje, conta de 404)', 'gancho': t01('nora' + n),
                  'texto': SIGNOS['nora' + n][1] + ', pay very close attention'} for n, h in (('42', 'hook da placa (cena do nora41)'), ('43', 'hook da pedra escura (nora34-PRE)'))]}
gravar(40, p40)

# ================= nora41: placa em cena nova =================
p41 = copy.deepcopy(P41)
CARTAO = ('one flat, rigid rectangle of plain matte white card stock, held horizontally, flat and facing the lens squarely, about 35 cm from the lens, centered, '
          'spanning about 75 percent of the frame width, its top edge just below her chin at about 46 percent of the frame height and its bottom edge at about 68 percent; '
          'it never covers her mouth. On it, written by hand with thick felt-tip markers in neat, bold capital letters, there are exactly two centered lines and nothing else: '
          'the first line, large, in bright red marker, reads {L1}; the second line, smaller, in black marker, reads 29, 30 AND 31 OF OCTOBER. Spell every word exactly like that, '
          'letter by letter ({SP}). No other words, numbers, drawings, stickers, tags or logos on the card.')
CENA41 = ('Vertical 9:16 close-up photo of the woman from the attached reference sheet in a dim, cozy real American bedroom at night. FRAMING: from the top of her head '
  'down to just below her collarbones; her knees, legs, the bed and the floor are NOT in the frame. The camera is a handheld phone at the height of her collarbones, '
  'about 55 cm in front of her, level, no tilt. Her face is large and centered in the upper half of the frame, with her eyes at about 30 percent of the frame height; '
  'a calm, intense, knowing gaze straight into the lens; lips closed in a faint knowing half-smile; shoulders square to the lens, leaning slightly toward the camera. '
  'HANDS: she holds one handwritten card with BOTH hands in front of her, just below her chin: her RIGHT hand (the hand on the LEFT side of the image) holds the card\'s '
  'left edge and her LEFT hand (the hand on the RIGHT side of the image) holds its right edge, thumbs in front on the white margins and the other fingers behind the card; '
  'the small gold sun ring is on her right index finger and the thin gold bracelets are on her left wrist; each hand has exactly five fingers with natural proportions; '
  'nothing else is in her hands. THE CARD: ' + CARTAO.format(L1='CANCER, SCORPIO, PISCES', SP='C-A-N-C-E-R, S-C-O-R-P-I-O, P-I-S-C-E-S') + ' '
  'FOREGROUND: at the bottom center of the frame, very close to the lens and softly out of focus, the top of a raw golden-yellow citrine cluster with honey-colored crystal '
  'points, filling only the bottom 10 percent of the frame. BACKGROUND (soft and out of focus): a plain deep navy-blue bedroom wall; one strand of tiny warm-white fairy '
  'lights hangs in loose loops on the wall behind her, on both sides of her at the height of her shoulders and neck, glowing as small soft round bokeh dots, never in front '
  'of her face and never above the top of her head; on the RIGHT side of the image, behind her shoulder, a small bedside lamp with a cream fabric shade glowing warm and, '
  'next to it, a small American flag (about 30 by 20 cm, on a short wooden stick) standing in a plain white ceramic mug. Nothing else: no other people, no pets, no posters, '
  'no signs, no logos and no readable text except the two lines on the card. LIGHT: warm tungsten lamp light from the right side of the image as the key light plus the '
  'soft glow of the fairy lights, the rest of the room dim and cozy; a realistic low-light phone photo with a little natural grain. FREE ZONES: the top 14 percent of the '
  'frame shows only the dark wall and the top of her hair. No date stamp, no watermark, no caption, no logo. Do not rejuvenate or smooth her face.')
TOPO41 = 'If this found you, November will be the most blessed month of your life.'
p41['roteiro'].update({
    'id': 'nora41-TEXTO-NA-TELA-PLACA-NOVA-CANCER-ESCORPIAO-PEIXES',
    'titulo': 'Texto na tela (Manifestation), placa em cena nova: Câncer, Escorpião e Peixes',
    'molde_hook': 'viral M2 (placa dos signos + datas, cristal desfocado na frente) em cena nova (quarto à noite, luzinhas, blusa vinho, citrino na frente) + frase nova do topo: aula do funil (“[mês] will be the most blessed month of your life”) e Antoine Martel (“the luckiest month of your entire life”)',
    'descricao_instagram': legenda('Cancer, Scorpio, Pisces', 'if this found you, November is your month'),
    'leitura_registro': LEITURA})
p41['refs'] = ['Blueprint da Nora v2 (a folha de consistência), só ele, na IMAGEM 1']
p41['trava_referencia'] = P37['trava_referencia']
p41['figurino'] = P41['figurino'].replace('a structured emerald-green blazer with notched lapels, worn open over a plain black fine-knit crew-neck top, both smooth and matte',
                                          'a soft deep wine-red fine-knit long-sleeve top with a round crew neckline, smooth and matte')
assert 'wine-red' in p41['figurino']
p41['imagens'] = [{'rotulo': 'IMAGEM 1', 'cena': CENA41, 'anexar': 'SÓ o blueprint da Nora v2 (a folha de consistência). Nenhuma outra imagem.'}]
p41['videos'][0]['fala'] = '(sem fala) texto na tela: ' + TOPO41
p41['texto_tela']['hook'] = TOPO41
p41['comentario_fixado'] = comentario('Cancer, Scorpio, Pisces')
pg = p41['pre_gancho']
pg['conceito'] = ('A placa do nora35 e do nora36 (as duas passaram de 2 mil) em cena nova: quarto à noite com luzinhas, blusa vinho e citrino (a pedra do dinheiro) '
                  'na frente; frase nova no topo. Ela não fala: empurra a placa até a lente, acena e volta.')
pg['modo'] = ('Gere só depois da nora41-IMG aprovada (seção “Imagens”) e do meu ok na grafia da placa. Um vídeo só, em FRAMES: primeiro e último quadro = nora41-IMG. '
              '8 s, 9:16, áudio ligado. 12 créditos (conta de 53: 41 → 29). Se o Flow recusar por política, não repita o texto: me mande o print.')
vp = pg['etapas'][0]['prompt']
vp = vp.replace('in a dim living room at night beside a warm table lamp', 'in a dim bedroom at night with soft fairy lights and a warm table lamp')
vp = vp.replace('the amethyst cluster at the bottom of the frame, the door, the lamp, the flag, the mug and the wall never move',
                'the citrine cluster at the bottom of the frame, the fairy lights, the lamp, the flag, the mug and the wall never move; the fairy lights do not blink')
vp = vp.replace('real quiet living-room sound only', 'real quiet bedroom sound only')
assert 'fairy lights do not blink' in vp and 'bedroom at night' in vp and 'bedroom sound' in vp
pg['etapas'][0]['prompt'] = vp
c = p41['central']
c['passos'] = [
    'Vídeo de 8 s SEM fala. Não usa a Central do curso nem o agente. Tudo na conta de 53.',
    'IMAGEM (seção “Imagens”): no Flow, anexe SÓ o blueprint e cole o prompt (botão “Copiar imagem com trava”). Aprove só se: é a Nora (lua e 3 estrelinhas na bochecha do lado esquerdo da imagem, trança com anéis); blusa vinho; a placa diz exatamente CANCER, SCORPIO, PISCES (vermelho) e 29, 30 AND 31 OF OCTOBER (preto), sem outra palavra; as duas mãos nas bordas da placa, cinco dedos; citrino embaixo e luzinhas atrás; sem carimbo de data. Se a grafia sair errada, gere de novo (imagem não gasta crédito). Renomeie para nora41-IMG e me mande.',
    'Depois do meu ok: o clipe (seção “Clipe”) em FRAMES, primeiro e último quadro = nora41-IMG, 8 s, 9:16, áudio ligado. Renomeie para nora41-CLIPE-placa. 12 créditos (conta de 53: 41 → 29).',
    'CapCut: números fixos, texto do topo, texto do story com a seta (dos 5 aos 8 s) e a música de sempre (“Ambient Mystical Drone”, da biblioteca do CapCut) (0 dB, a placa não tem fala). Sem legenda na tela e sem corte de silêncio: a Nora não fala.',
    'Postar em 29/10 às 19h30 no Insta e no Face, ao vivo. No Insta, ponha a localização Los Angeles, California (o teste continua nas placas). O story repostado hoje tem de estar no ar. ' + COMENTAR,
]
c['conferir'] = 'Conferir: é a Nora da nora41-IMG; ela não fala; a escrita da placa não muda; a placa fica nas duas mãos e não cobre o rosto; as luzinhas não piscam; o quarto fica parado.'
p41['story']['nota'] = STORY_JA
p41['edicao_linha'][0]['texto'] = TOPO41
p41['edicao_linha'][0]['como'] = 'Texto no topo, em 3 linhas, do segundo 0 ao fim do clipe. “If this found you,” em branco; “November will be the most blessed month of your life.” em amarelo-ouro.'
for e in p41['mapa_tela']['estilos']:
    if e['nome'].startswith('Texto do topo'):
        e['cor'] = 'branco #FFFFFF; “November will be the most blessed month of your life.” em amarelo-ouro #FFD21F'
        e['obs'] = 'Centralizado, em 3 linhas, do segundo 0 ao fim do clipe, em X 0 · Y 374 (logo abaixo do 222 e do 11:11, sem encostar).'
p41['pecas'] = {'lista': [
    {'nome': 'nora41-IMG', 'tipo': 'imagem 1', 'status': 'gerar',
     'descricao': 'Do blueprint: cena nova (quarto à noite, luzinhas, blusa vinho, citrino na frente), placa CANCER, SCORPIO, PISCES / 29, 30 AND 31 OF OCTOBER.',
     'base': 'Placa do M2 (nora35 e nora36 passaram de 2 mil); cena e frase novas porque a 3ª placa igual (nora38) cansou.',
     'serve': 'nora42: o hook é uma edição desta imagem (só a placa muda). Próximas placas: edição desta cena.'},
    {'nome': 'nora41-CLIPE-placa', 'tipo': 'clipe sem fala', 'status': 'gerar', 'creditos': 12,
     'descricao': '8 s: ela empurra a placa até a lente, acena e volta (o movimento do nora35).', 'base': 'nora35 + placa do M2.',
     'serve': 'Face: versão -VEL e com filtro (placa não espelha: a escrita inverte).'}],
    'decisao': [
     'A placa repetida pela 3ª vez (nora38) segurou menos (49% nos 3 s contra 57 a 60%): hoje a placa tem cena nova e frase nova, e só 1 placa no dia.',
     'Frase do topo: “[mês] will be the most blessed month of your life” (aula do funil: datas e meses) + Antoine Martel (“the luckiest month of your entire life”).',
     'Citrino na frente (a pedra do dinheiro, Manifestation) no lugar da ametista.',
     AGENDA]}
gravar(41, p41)

# ================= nora42: longo com o hook da placa (Gêmeos, Libra, Aquário) =================
T42 = takes('nora42'); checar(T42)
p42 = base_longo()
p42['roteiro'] = {
    'id': 'nora42-LONGO-HOOK-PLACA-GEMEOS-LIBRA-AQUARIO',
    'titulo': 'Longo do corpo A (Manifestation), hook da placa: Gêmeos, Libra e Aquário (só o Take 1 novo)',
    'dor': DOR,
    'formato': 'Hook da placa (4 s, cena do nora41) + Take 1 novo + takes 2 a 11 do nora40 (~90 s)',
    'molde_hook': 'placa dos signos (M2, cena do nora41) como hook visual + corpo A (x1 a x5); a conta dos x troca o hook e os signos com o mesmo corpo',
    'duracao_total': 92,
    'descricao_instagram': legenda('Gemini, Libra, Aquarius'),
    'leitura_registro': LEITURA}
p42['refs'] = ['A nora41-IMG aprovada, só ela, na nora42-PRE-IMG', 'Take 1: a nora37-IMG']
p42['videos'] = videos_de(T42, 11)
p42['texto_tela'] = {'hook': 'Gemini, Libra, Aquarius, pay very close attention', 'hook_comeca': 'o primeiro quadro do hook (a placa)',
                     'hook_termina': 'October 29th, 30th or 31st', 'hook_alt': '', 'extras': []}
p42['comentario_fixado'] = comentario('Gemini, Libra, Aquarius')
EDIT42 = ('VISUAL REFERENCE LOCK: use exclusively the ATTACHED image as the identity authority. There is no pet in this project: no animal appears in any scene. '
  'EDIT of the attached image (the woman holding the handwritten white card). Keep EVERYTHING exactly as it is: the same woman, the same face, eyes, hair, braid, face gems, '
  'earrings, necklace, bracelets and ring, the same wine-red top, the same pose, the same hands in the same places with five fingers each, the same white card in the same '
  'position, size and angle, the same blurred citrine cluster at the bottom, the same fairy lights, lamp, small American flag in the mug, wall and warm light, and the same '
  'framing. Change ONLY the first handwritten line on the white card, in the same neat bold capital felt-tip handwriting, the same size and the same bright red color: it now '
  'reads GEMINI, LIBRA, AQUARIUS. The second line stays exactly 29, 30 AND 31 OF OCTOBER in black. Spell every word exactly like that, letter by letter '
  '(G-E-M-I-N-I, L-I-B-R-A, A-Q-U-A-R-I-U-S). Exactly two centered lines and nothing else on the card: no other words, numbers, drawings, stickers, tags or logos. '
  'No date stamp, no watermark, no caption. Do not rejuvenate or smooth her face.')
VID42 = ('Create a single continuous 4-second video clip that opens exactly on the supplied first frame, vertical 9:16. There is no last frame. Handheld smartphone camera '
  'about 55 cm from the woman at the height of her collarbones, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n'
  'THE MAIN EVENT: the woman, in a dim bedroom at night with soft fairy lights and a warm table lamp, holds a white handwritten card with both hands just below her chin. '
  'She pushes the card toward the lens and holds it there with an intense look. She never speaks.\n\n'
  'SECOND BY SECOND (something visible moves in EVERY second):\n'
  '0.0 to 1.0 s: both hands push the card straight toward the lens and slightly down, from about 35 cm to about 22 cm away, so it grows to about 90 percent of the frame '
  'width; the card stays flat, horizontal and facing the lens, its top edge stays below her chin and her eyes stay on the lens above it.\n'
  '1.0 to 2.0 s: she holds the card close and still; her eyebrows lower slightly in a serious, intense look.\n'
  '2.0 to 3.0 s: she gives one slow knowing nod with her lips closed while the card stays still.\n'
  '3.0 to 4.0 s: she holds still with the card close to the lens and a faint closed-lip half-smile.\n\n'
  'WHAT MUST NOT HAPPEN: she does not speak or mouth any words (her lips stay closed for the whole clip); the handwriting on the card never changes, moves, blurs, fades or '
  'gains or loses letters, and no new text appears anywhere; the card never bends, folds, flips, turns, tilts away or drops, and never covers her eyes or mouth; both hands '
  'stay on the card\'s side edges; each hand has exactly five fingers; the citrine cluster at the bottom of the frame, the fairy lights, the lamp, the flag, the mug and the '
  'wall never move; the fairy lights do not blink; no object, person or animal appears or disappears; the lamp light does not flicker.\n\n'
  'VISUAL: she is the same woman as in the supplied frame; realistic natural physics, no morphing, no glow, no magic effects. No added text, no logos.\n\n'
  'AUDIO: real quiet bedroom sound only, with the faint rustle of the card. No music, no voice, no added sound effects.')
p42['pre_gancho'] = {'titulo_secao': 'Hook (4 s, a placa de Gêmeos, Libra e Aquário, sem fala)', 'duracao': 4, 'tomadas': 1, 'com_rosto': True,
    'conceito': 'A placa do nora41, agora com Gêmeos, Libra e Aquário, como hook de 4 s: ela empurra a placa até a lente e fica. A placa diz os mesmos signos da fala do Take 1 (por isso não dá para usar o clipe do nora41 como está).',
    'modo': 'Conta de 53, depois da nora41-IMG aprovada. Gere a nora42-PRE-IMG (anexe SÓ a nora41-IMG) e me mande. Depois do meu ok, o vídeo em FRAMES: primeiro quadro = nora42-PRE-IMG, SEM último quadro, 4 s, 9:16, áudio ligado. 7 créditos (conta de 53: 29 → 22).',
    'etapas': [
        {'tipo': 'img', 'titulo': 'Imagem: a placa com Gêmeos, Libra e Aquário', 'nome': 'nora42-PRE-IMG', 'anexar': 'SÓ a nora41-IMG aprovada (é uma edição dela)', 'prompt': EDIT42},
        {'tipo': 'vid', 'titulo': 'Vídeo: ela empurra a placa até a lente', 'nome': 'nora42-PRE', 'duracao': 4,
         'quadros': 'Modo FRAMES. Primeiro quadro: nora42-PRE-IMG. Sem último quadro. 4 s, 9:16, áudio ligado.', 'prompt': VID42}],
    'montagem': '1) nora42-PRE: uns 3,5 s (corte com a placa perto da lente).\n2) Corte seco para o corpo cortado (nora42-cortado: o Take 1 novo + as cópias dos takes 2 a 11 do nora40).\n3) A caixa do topo já entra no primeiro quadro do hook.\nPlano B, se o Flow mexer na escrita: a nora42-PRE-IMG como foto por 2 s, com zoom leve (100% a 108%), 0 crédito.',
    'texto_tela': '', 'edicao': ''}
p42['central'] = central_1take('42', T42, ['Hook, na conta de 53 (seção “Pré-gancho”): gere a nora42-PRE-IMG (anexe SÓ a nora41-IMG aprovada) e me mande. Depois do meu ok, o vídeo de 4 s em Frames (7 créditos). Renomeie para nora42-PRE.'])
p42['central']['passos'].append('Postar em 29/10 às 22h no Insta e no Face, ao vivo, sem localização (é falado). ' + COMENTAR)
p42['story'] = copy.deepcopy(P41['story']); p42['story']['nota'] = STORY_JA
p42['edicao_linha'] = edicao_longo(42, 'Hook da placa (nora42-PRE, uns 3,5 s)', True, 'Gemini, Libra, Aquarius, pay very close attention')
p42['mapa_tela']['regras'] = p42['mapa_tela']['regras'] + ['No hook da placa (sem fala) não há legenda; a caixa do topo fica em cima do cabelo, acima da placa.']
p42['pecas'] = {'lista': [
    {'nome': 'nora42-PRE-IMG', 'tipo': 'imagem do hook', 'status': 'gerar', 'descricao': 'Edição da nora41-IMG: só a 1ª linha da placa muda (GEMINI, LIBRA, AQUARIUS).', 'base': 'Placa do M2 na cena do nora41.', 'serve': 'Só deste vídeo.'},
    {'nome': 'nora42-PRE', 'tipo': 'vídeo do hook', 'status': 'gerar', 'creditos': 7, 'descricao': '4 s em Frames, sem último quadro: ela empurra a placa até a lente.', 'base': 'Movimento do nora35 (a placa que passou de 2 mil), em 4 s.', 'serve': 'Face: colado em outros corpos com Gêmeos, Libra e Aquário.'},
    {'nome': 'nora37-IMG', 'de': 'nora37-IMG', 'tipo': 'imagem 1 (do nora37)', 'status': 'reutilizar', 'descricao': 'Primeiro e último quadro do Take 1, a mesma dos takes 2 a 11.'},
    {'nome': T42[0][0], 'tipo': 'gancho', 'status': 'gerar', 'creditos': 15, 'descricao': f'Take 1: “{T42[0][2]}”', 'base': 'Take 1 da série (corpo A: signos + “keep your mouth shut” + datas).', 'serve': 'Só deste vídeo.'},
    ] + reuso_corpo('42'),
    'decisao': [
     'Mesmo corpo do nora40, outro hook e outros signos (a conta dos x faz assim no mesmo dia; Lucas: o hook não precisa ser no mesmo lugar).',
     'Hook da placa: a placa segura os 3 s (57 a 60% nos 3 s); aqui ela abre o longo em vez de ser o vídeo todo.',
     'A placa precisa dizer os mesmos signos da fala: por isso uma imagem editada e um clipe de 4 s (7), e não o clipe do nora41.',
     AGENDA]}
gravar(42, p42)

# ================= nora43: longo com o hook da pedra escura (Touro, Virgem, Capricórnio) =================
T43 = takes('nora43'); checar(T43)
p43 = base_longo()
p43['roteiro'] = {
    'id': 'nora43-LONGO-HOOK-PEDRA-TOURO-VIRGEM-CAPRICORNIO',
    'titulo': 'Longo do corpo A (Manifestation), hook da pedra escura: Touro, Virgem e Capricórnio (só o Take 1 novo)',
    'dor': DOR,
    'formato': 'Hook da pedra escura que racha (nora34-PRE, 4 s) + Take 1 novo + takes 2 a 11 do nora40 (~90 s)',
    'molde_hook': 'pedra escura que racha (viral x5; já usada no nora34) + corpo A (x1 a x5)',
    'duracao_total': 92,
    'descricao_instagram': legenda('Taurus, Virgo, Capricorn'),
    'leitura_registro': LEITURA}
p43['refs'] = ['Nenhuma imagem nova: a nora37-IMG']
p43['videos'] = videos_de(T43, 11)
p43['texto_tela'] = {'hook': 'Taurus, Virgo, Capricorn, pay very close attention', 'hook_comeca': 'o primeiro quadro do pré-gancho',
                     'hook_termina': 'October 29th, 30th or 31st', 'hook_alt': '', 'extras': []}
p43['comentario_fixado'] = comentario('Taurus, Virgo, Capricorn')
p43['pre_gancho'] = {'titulo_secao': 'Pré-gancho (o do nora34: não gerar)', 'duracao': 4, 'tomadas': 1, 'com_rosto': True,
    'conceito': 'A pedra escura que racha do nora34 (viral x5), já gerada: 0 crédito. Abre e mostra o quartzo rosa, como o geodo dos takes.',
    'modo': 'Não gere nada aqui. No CapCut, use a nora34-PRE como está (sem espelhar).',
    'montagem': '1) nora34-PRE: uns 3,5 s (corte logo depois que as metades abrem).\n2) Corte seco para o corpo cortado (nora43-cortado: o Take 1 novo + as cópias dos takes 2 a 11 do nora40).\n3) A caixa do topo já entra no primeiro quadro do pré-gancho.',
    'texto_tela': '', 'edicao': ''}
p43['central'] = central_1take('43', T43, [])
p43['central']['passos'].append('Postar à 00h30 de 30/10 (a noite de 29/10) no Insta e no Face, ao vivo, sem localização (é falado). ' + COMENTAR)
p43['story'] = copy.deepcopy(P41['story']); p43['story']['nota'] = STORY_JA
p43['edicao_linha'] = edicao_longo(43, 'Pré-gancho (nora34-PRE, uns 3,5 s)', False, 'Taurus, Virgo, Capricorn, pay very close attention')
p43['pecas'] = {'lista': [
    {'nome': 'nora34-PRE', 'de': 'nora34-PRE', 'tipo': 'pré-gancho (do nora34)', 'status': 'reutilizar', 'creditos': 7, 'descricao': 'A pedra escura que racha, sem espelhar.'},
    {'nome': 'nora37-IMG', 'de': 'nora37-IMG', 'tipo': 'imagem 1 (do nora37)', 'status': 'reutilizar', 'descricao': 'Primeiro e último quadro do Take 1, a mesma dos takes 2 a 11.'},
    {'nome': T43[0][0], 'tipo': 'gancho', 'status': 'gerar', 'creditos': 15, 'descricao': f'Take 1: “{T43[0][2]}”', 'base': 'Take 1 da série (corpo A: signos + “keep your mouth shut” + datas).', 'serve': 'Só deste vídeo.'},
    ] + reuso_corpo('43'),
    'decisao': [
     'Mesmo corpo do nora40, hook da pedra escura (x5) e outros signos: 15 créditos.',
     'Às 00h30 (20h30 na costa oeste dos EUA): o nora33 (01h45) fez 31% de EUA.',
     AGENDA]}
gravar(43, p43)
print('ok: PAINEL-NORA40 a 43')
