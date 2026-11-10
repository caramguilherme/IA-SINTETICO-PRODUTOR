# 09/11/2026: painéis do nora51, nora52 e nora53 = a fórmula do nora49 (gancho do tsunami + Take 1 novo na nora37-IMG
# + corpo A limpo do nora48-montado), para volume (4 vídeos por dia, decisão do aluno de 09/11). Não são teste:
# o único teste do dia é o nora50 (a pedra, 19h30). Base: o pacote do nora49.
# Uso: python3 -I ferramentas-painel/r0911/patch_nora51_53.py  (na raiz do repositório)
import json, copy, sys
R = sys.argv[1] if len(sys.argv) > 1 else '.'
t = open(f'{R}/PAINEL-NORA49.html', encoding='utf-8').read()
i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
BASE = json.loads(t[i:j])
t50 = open(f'{R}/PAINEL-NORA50.html', encoding='utf-8').read()
i5 = t50.index('const PACOTE = ') + len('const PACOTE = '); j5 = t50.index(';\n', i5)
STORY = json.loads(t50[i5:j5])['story']
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
FALA49 = "Aries, Leo or Sagittarius: if you know something has to change, but not how, listen before 11:11, the year's most powerful portal."

def xy(x, y):
    return f'X {round(x / 100 * 720 - 360):+d} · Y {round(640 - y / 100 * 1280):d}'.replace('+', '')

VIDEOS = [
    dict(n=51, hora='17h', espelhar=False,
         en='Taurus, Virgo or Capricorn', en3='Taurus, Virgo, Capricorn', caps='TAURUS, VIRGO, CAPRICORN',
         pt='Touro, Virgem e Capricórnio', slug='touro-virgem-capricornio', tags='#taurus #virgo #capricorn',
         fala="Taurus, Virgo or Capricorn: if you've done everything right and still feel stuck, listen before 11:11, the year's most powerful portal.",
         legenda1="Taurus, Virgo, Capricorn: if you've done everything right and still feel stuck, listen before 11/11, the most powerful portal of the year. 🔮",
         pergunta='what have you been working so hard for lately?',
         nums=[('888', 82, 10.5, 'alto à direita', 'laranja', '#FF9F1C', 15),
               ('222', 18, 30, 'no meio à esquerda, na parede', 'branco', '#FFFFFF', 12),
               ('11:11', 82, 46.9, 'à direita, na altura do ombro', 'ciano', '#3DE0FF', 11)],
         coment=['🌙 I sent it to your messages, take a look ✨', '✨ It\'s waiting in your inbox 💖', '💫 Check your DMs, it\'s there 🔮'],
         dm=['✨ [name], your private reading is here 🔮 Open it before 11:11:', '🌙 Hi [name]! Here\'s your private reading 💖 before the 11:11 portal:',
             '💫 [name], this one is for you ✨ Open your private reading here:'],
         piloto=True),
    dict(n=52, hora='22h', espelhar=True,
         en='Cancer, Scorpio or Pisces', en3='Cancer, Scorpio, Pisces', caps='CANCER, SCORPIO, PISCES',
         pt='Câncer, Escorpião e Peixes', slug='cancer-escorpiao-peixes', tags='#cancer #scorpio #pisces',
         fala="Cancer, Scorpio or Pisces: if you feel everything deeply but nothing's moving yet, listen before 11:11, the year's most powerful portal.",
         legenda1="Cancer, Scorpio, Pisces: if you feel everything deeply but nothing's moving yet, listen before 11/11, the most powerful portal of the year. 🔮",
         pergunta='what feeling do you want to wake up with every morning?',
         nums=[('222', 82, 10.5, 'alto à direita', 'rosa-choque', '#FF4FD8', 14),
               ('11:11', 18, 30, 'no meio à esquerda, na parede', 'verde-limão', '#7CFF4F', 12),
               ('888', 82, 46.9, 'à direita, na altura do ombro', 'amarelo-ouro', '#FFD21F', 11)],
         coment=['💖 It\'s in your messages now ✨', '🔮 Just sent it to you, check your inbox 💫', '✨ Sent! Look in your DMs 💖'],
         dm=['🔮 [name], here\'s your private reading ✨ before the 11:11 portal:', '💖 [name], I sent this one just for you 🔮 Open it here:',
             '✨ Hey [name]! Tap here to open your private reading 💫'],
         piloto=False),
    dict(n=53, hora='00h30', espelhar=False,
         en='Aries, Leo or Sagittarius', en3='Aries, Leo, Sagittarius', caps='ARIES, LEO, SAGITTARIUS',
         pt='Áries, Leão e Sagitário', slug='aries-leao-sagitario', tags='#aries #leo #sagittarius',
         fala="Aries, Leo or Sagittarius: if you've been waiting for a sign to move, listen before 11:11, the year's most powerful portal.",
         legenda1="Aries, Leo, Sagittarius: if you've been waiting for a sign to move, listen before 11/11, the most powerful portal of the year. 🔮",
         pergunta='what are you finally ready to start?',
         nums=[('11:11', 18, 10.5, 'alto à esquerda', 'laranja', '#FF9F1C', 16),
               ('888', 82, 30, 'no meio à direita, na parede acima do abajur', 'verde-limão', '#7CFF4F', 13),
               ('222', 18, 46.9, 'à esquerda, na altura do ombro, sobre o cabelo', 'ciano', '#3DE0FF', 11)],
         coment=['🔥 Check your inbox, I sent it ✨', '✨ It\'s in your DMs, take a look 🔮', '💫 Sent to your messages 💖'],
         dm=['🔥 [name], your private reading is here ✨ Before the 11:11 portal:', '✨ [name], open this when you have a quiet minute 🔮 Your private reading:',
             '💖 Hi [name]! Your private reading is ready 💫 Here:'],
         piloto=False),
]

for v in VIDEOS:
    n = v['n']; nn = f'nora{n}'
    assert len(v['fala'].split()) <= 22, (n, len(v['fala'].split()))
    ARQ = f'{nn}-T01-gancho-portal-{v["slug"]}'
    s = json.dumps(BASE, ensure_ascii=False)
    for a, b in [(FALA49, v['fala']), ('ARIES, LEO, SAGITTARIUS', v['caps']), ('Aries, Leo, Sagittarius', v['en3']),
                 ('Aries, Leo or Sagittarius', v['en']), ('Áries, Leão e Sagitário', v['pt']), ('aries-leao-sagitario', v['slug']),
                 ('#aries #leo #sagittarius', v['tags']), ('nora49', nn)]:
        s = s.replace(a, b)
    p = json.loads(s)
    gancho = 'ESPELHADO' if v['espelhar'] else 'sem espelhar (como no nora48)'
    r = p['roteiro']
    r['id'] = f'{nn}-FORMULA-TSUNAMI-TAKE1-{v["slug"].upper()}'
    r['titulo'] = f'Gancho do tsunami ({"espelhado" if v["espelhar"] else "normal"}) + Take 1 de {v["pt"]} no quarto à noite + corpo A limpo (a fórmula do nora49)'
    r['formato'] = (f'Hook do tsunami do nora47, {gancho} (pronto) + Take 1 NOVO na nora37-IMG ({v["pt"]}) '
                    '+ os 7 takes do corpo A limpo, tirados do nora48-montado (~80 s)')
    r['molde_hook'] = ('Volume, não é teste (4 vídeos por dia, decisão do aluno de 09/11): a fórmula do nora49, que fez 1.727 views, 16 follows e 9 visitas '
                       'ao perfil no Insta com ~13h30 (EUA 33%). O único teste do dia é o nora50 (a pedra, 19h30). Aqui só mudam os signos (Take 1 novo).')
    r['descricao_instagram'] = (v['legenda1'] + '\nThe worst is finally over. Your private reading is waiting in my story.\n'
                                + '#manifestation #1111portal ' + v['tags'])
    r['leitura_registro'] = ('09/11/2026 ~13h, leitura focada (decisão do aluno de 07/11 para painel que só troca peças numa fórmula testada; registro honesto): '
        'o pacote inteiro do painel do nora49 (a base: LIVRE, perfil de voz, movimentação, edição) e o story do painel do nora50; o CLAUDE.md (seções 0 a 6, em toda mensagem); '
        'as regras P46 e P47 do REGRAS-DO-AGENTE.md e as entradas de 07 a 09/11 do LICOES-FLOW-E-PROMPTS.md (escritas por mim nesta sessão), o item 28 do checklist (números); '
        'o CLONE-DO-GUSTAVO-RESPOSTAS.md (escrito nesta sessão); as entradas de 09/11 do FATOS-DO-ALUNO.md (créditos, custo do 1.2, modelos do Flow); '
        'a BIBLIOTECA-DE-TAKES.md (linhas do nora47 ao nora50); as leituras do nora48 e do nora49 no METRICAS-NORA-LEIA.md. '
        'Os arquivos REGRAS, LICOES e FATOS não foram relidos inteiros hoje (foram lidos inteiros nesta sessão em 06 e 07/11).')
    p['videos'][0]['arquivo'] = ARQ
    p['comentario_fixado'] = {
        'insta': f'{v["en3"]}: {v["pergunta"]} ✨ Tell me below, then tap my photo and open my story before the 11:11 portal: your private reading starts there. 🔮',
        'face': f'{v["en3"]}: {v["pergunta"]} ✨ Your private reading is right here, open it before the 11:11 portal 🔮 👉 {FB}'}
    pg = p['pre_gancho']
    if v['espelhar']:
        pg['titulo_secao'] = 'Hook: o tsunami do nora47, ESPELHADO (já pronto, 0 crédito)'
        pg['conceito'] = 'O mesmo gancho do nora48 e do nora49 (o tsunami), ESPELHADO como no nora49, já pronto: 0 crédito.'
        pg['modo'] = 'Não gere nada aqui. No CapCut, espelhe só o trecho do hook (Editar → Espelhar).'
    else:
        pg['titulo_secao'] = 'Hook: o tsunami do nora47, SEM espelhar (já pronto, 0 crédito)'
        pg['conceito'] = 'O mesmo gancho do nora48 (o tsunami), sem espelhar, já pronto no começo do nora48-montado: 0 crédito.'
        pg['modo'] = 'Não gere nada aqui e não mexa no hook: ele já está no começo do nora48-montado.'
        pg['montagem'] = ('1) Projeto novo no CapCut com o nora48-montado (o vídeo SEM texto do nora48).\n'
                          '2) Divida no começo do Take 1 (~7,9 s, quando entra o quarto) e no começo do Take 2 ("Don\'t tell anyone", ~16,6 s).\n'
                          f'3) Apague o Take 1 do nora48 e encoste o {nn}-T01-cortado no lugar.\n4) No hook fica só o som da onda (sem espelhar).')
    c = p['central']
    c['passos'][0] = 'Story: o de hoje sai pelo painel do nora50 (texto do story-0311, "Tap below…"). Se já postou, não poste outro aqui.'
    c['passos'][2] = (f'Agente do Flow: conversa nova, anexe só a nora37-IMG, cole o aviso de 1 prompt e, embaixo, o prompt do take. 15 créditos. '
                      f'Renomeie para {ARQ}. **Troque para o Omni 1.1 Flash, 720p, antes de gerar** (o Flow abre no 1.2, que cobra o dobro).')
    if v['piloto']:
        c['passos'][2] += (' **PILOTO (só neste painel):** gere o mesmo Take 1 uma 2ª vez no **Omni 1.2 Flash em 360p** (10 s) e baixe em **720p** '
                           '(veja se o download cobra créditos); renomeie para nora51-T01-PILOTO-12-360p e me mande junto. Não vai ao ar: é para eu comparar a imagem.')
    if v['espelhar']:
        c['passos'][4] = (f'CapCut: projeto novo com o nora48-montado. Espelhe só o hook (0 a ~7,9 s). Divida no começo do Take 1 e no começo do Take 2 ("Don\'t tell anyone", ~16,6 s), '
                          f'apague o Take 1 do nora48 e ponha o {nn}-T01-cortado no lugar. Música −18 dB só no Take 1 novo (o resto já tem). Exporte SEM texto como {nn}-montado e me mande (Drive, se passar de 30 MB).')
    else:
        c['passos'][4] = (f'CapCut: projeto novo com o nora48-montado. NÃO espelhe o hook. Divida no começo do Take 1 (~7,9 s) e no começo do Take 2 ("Don\'t tell anyone", ~16,6 s), '
                          f'apague o Take 1 do nora48 e ponha o {nn}-T01-cortado no lugar. Música −18 dB só no Take 1 novo (o resto já tem). Exporte SEM texto como {nn}-montado e me mande (Drive, se passar de 30 MB).')
    c['passos'][5] = (f'Eu devolvo o {nn}-final (caixa do topo com os signos, números, legenda, faixa do story e seta). Confira no celular e poste hoje (09/11) às {v["hora"]} '
                      'no Insta e no Face, ao vivo. Comentário: no Insta, comente e fixe (sem link); no Face, comente COMO A PÁGINA (já tem o link).')
    p['story'] = copy.deepcopy(STORY)
    p['story']['nota'] = ('STORY: o de hoje é o do painel do nora50 (texto "Tap below: your private reading is waiting for you before the 11:11 portal.", '
                          'adesivo "Open my reading", imagem story-3110), postado uma vez no Insta e no Face. Aqui não tem story novo.')
    mt = p['mapa_tela']
    mt['numeros'] = [dict(t=a, x=x, y=y, onde=o, cor_nome=cn, cor=co, tamanho=tm) for (a, x, y, o, cn, co, tm) in v['nums']]
    mt['estilos'][0]['obs'] = ('Lugar, cor e tamanho novos (item 28): ' + '; '.join(f'{a} {cn}, {tm}, {xy(x, y)}' for (a, x, y, o, cn, co, tm) in v['nums'])
                               + '. Do 1º quadro do hook ao fim. Eu ponho (P45) e confiro na prévia (mexo se encostar em rosto, mão, geodo ou caixa).')
    mt['regras'][1] = 'Os números mudam de lugar, cor e tamanho em relação ao nora49 e ao nora50 (item 28); confiro na prévia da edição.'
    el = p['edicao_linha']
    if not v['espelhar']:
        el[1]['texto'] = 'Hook do tsunami, SEM espelhar'
        el[1]['como'] = 'Não mexa no hook (~7,9 s): ele já está no começo do nora48-montado. Só o som da onda.'
    pc = p['pecas']
    pc['lista'][0]['descricao'] = 'O tsunami, ESPELHADO no CapCut.' if v['espelhar'] else 'O tsunami, sem espelhar (já no começo do nora48-montado).'
    pc['lista'][4] = dict(nome='story do dia (painel do nora50)', de='story-3110', tipo='story', status='reutilizar',
                          descricao='O story de hoje sai pelo painel do nora50 (texto do story-0311). Não poste outro.')
    pc['decisao'] = [
        'Volume (4 vídeos por dia, decisão do aluno de 09/11): a fórmula do nora49 com outros signos. Não é teste; o teste do dia é o nora50 (a pedra, 19h30).',
        f'Horário: {v["hora"]} de 09/11, no Insta e no Face, ao vivo.',
        'Total: 15 créditos (só o Take 1)' + (' + o piloto do 1.2 em 360p (~10 créditos, não vai ao ar).' if v['piloto'] else '.')]
    p['silencio']['intro'] = (f'Só o Take 1 novo ({nn}-T01) passa por aqui: o resto vem do nora48-montado. '
                              f'Arraste só o {nn}-T01 na ferramenta “M2M FusionZ – Cortar e juntar vídeos” e deixe assim:')
    p['silencio']['depois'][1] = p['silencio']['depois'][1].replace('“Aries”', '“' + v['en'].split(',')[0] + '”')
    p['respostas_face']['comentario'] = v['coment']
    p['respostas_face']['dm'] = v['dm']
    novo = t[:i] + json.dumps(p, ensure_ascii=False) + t[j:]
    novo = novo.replace('<title>Painel nora49', f'<title>Painel {nn}')
    open(f'{R}/PAINEL-NORA{n}.html', 'w', encoding='utf-8').write(novo)
    print('ok', nn, len(v['fala'].split()), 'palavras', len(novo))
