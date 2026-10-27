import json,re,copy
D='/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/manif2710/'
s35=open('PAINEL-NORA35.html',encoding='utf-8').read(); m=re.search(r'const PACOTE = (.*?);\n',s35,re.S); base=json.loads(m.group(1))
REG="27/10/2026 (Manifestation, P41, e a estratégia de 27/10): li nesta sessão, com a ferramenta de leitura, FATOS-DO-ALUNO.md, CLAUDE.md, 00-LEIA-PRIMEIRO.md, BRIEFING-MANIFESTACAO.md, PROJETO-Dana.md, LICOES-FLOW-E-PROMPTS.md (inteiro), BIBLIOTECA-VIDEOS-VIRAIS.md (seções 20 a 39), METRICAS-NORA.csv, PAINEL-MODELO.html e o painel do nora35 (o molde deste); COMUNIDADE-E-ESTRATEGIA.md e o Discord de 26/10 foram lidos e escritos nesta sessão. Os outros arquivos de LEIA-TUDO-ANTES.md foram lidos inteiros na montagem do nora35 (26/10), que este painel repete trocando só os signos, as datas e os textos."
TOPO="Don't you dare scroll past this, or the universe might skip your blessing."
def placa(nn,signos_en,signos_lista,signos_pt,soletra,hora,data_post):
    p=copy.deepcopy(base)
    cap=signos_lista
    r=p['roteiro']
    r['id']=f'nora{nn}-TEXTO-NA-TELA-PLACA-'+'-'.join(signos_pt.upper().split(', ')).replace(' E ','-')
    r['titulo']=f'Texto na tela (Manifestation): a placa de {signos_pt} (modelo M2)'
    r['dor']='as bênçãos e o dinheiro que não chegam; o sinal que ela espera (Manifestation, ângulo positivo de predestinação, P41)'
    r['molde_hook']='viral M2 (placa dos signos + datas, drusa de ametista desfocada na frente) + a frase do M2 e do a4/a5 “Don’t you dare scroll past this, or the universe might skip your blessing” no texto do topo; repete o nora35, que fez 2.448 views'
    r['descricao_instagram']=f"{signos_en}: if this found you, it's not by chance. 🔮\nComment 222. Tap my photo NOW: the second part of this sign is in my story.\n#manifestation #astrology #zodiac #usa #usareels"
    r['leitura_registro']=REG
    p['refs']=['A nora35-IMG (a imagem da placa do nora35), só ela']
    im=p['imagens'][0]
    im['cena']=(f"EDIT of the attached image (the woman holding the handwritten white card). Keep EVERYTHING exactly as it is: the same woman, the same face, eyes, hair, braid, face gems, earrings, necklace, bracelets and ring, the same emerald-green blazer and black top, the same pose, the same hands in the same places with five fingers each, the same white card in the same position, size and angle, the same blurred amethyst cluster at the bottom, the same door, lamp, small American flag in the mug, wall and warm lamp light, and the same framing. Change ONLY the two handwritten lines on the white card, in the same neat bold capital felt-tip handwriting, the same sizes and the same colors as before: the first line, large, in bright red marker, now reads {cap}; the second line, smaller, in black marker, now reads 27, 28 AND 29 OF OCTOBER. Spell every word exactly like that, letter by letter ({soletra}). Exactly two centered lines and nothing else on the card: no other words, numbers, drawings, stickers, tags or logos. No date stamp, no watermark, no caption. Do not rejuvenate or smooth her face.")
    im['anexar']='SÓ a nora35-IMG (a imagem da placa do nora35). Nada mais: nem o blueprint.'
    v=p['videos'][0]; v['fala']='(sem fala) texto na tela: '+TOPO; v['arquivo']=f'nora{nn}-CLIPE-placa'
    p['texto_tela']['hook']=TOPO
    pg=p['pre_gancho']; pg['nome_video']=f'nora{nn}-CLIPE-placa'
    pg['conceito']=f'Repete o nora35 (2.448 views): a Nora segura a placa escrita à mão, agora com {signos_pt} em vermelho e 27, 28 AND 29 OF OCTOBER em preto. Ela não fala: empurra a placa até a lente, acena e volta.'
    pg['modo']=f'Gere só depois da nora{nn}-IMG aprovada (seção “Imagens”) e do meu ok na grafia da placa. Um vídeo só, em FRAMES: primeiro e último quadro = nora{nn}-IMG. 8 s, 9:16, áudio ligado. 12 créditos (conta de 53). Se o Flow recusar por política, não repita o texto: me mande o print.'
    for e in pg['etapas']:
        e['nome']=f'nora{nn}-CLIPE-placa'; e['quadros']=f'Modo FRAMES. Primeiro quadro: nora{nn}-IMG. Último quadro: a mesma nora{nn}-IMG. 8 s, 9:16, áudio ligado.'
    c=p['central']
    c['conferir']=f'Conferir: é a Nora da nora{nn}-IMG; ela não fala; a escrita da placa não muda; a placa fica nas duas mãos e não cobre o rosto; a sala fica parada.'
    c['passos']=[
     'Vídeo de 8 s SEM fala. Não usa a Central do curso nem o agente. Tudo na conta de 53 (suba nela a nora35-IMG).',
     f'IMAGEM (seção “Imagens”): no Flow, anexe SÓ a nora35-IMG e cole o prompt de edição (botão “Copiar imagem com trava”). Aprove só se: é a mesma Nora e a mesma cena; a placa diz exatamente {cap} (vermelho) e 27, 28 AND 29 OF OCTOBER (preto), sem outra palavra; as duas mãos nas bordas da placa; cinco dedos; sem carimbo de data. Se a grafia sair errada, gere de novo (imagem não gasta crédito). Renomeie para nora{nn}-IMG e me mande.',
     f'Depois do meu ok: o clipe (seção “Clipe”) em FRAMES, primeiro e último quadro = nora{nn}-IMG, 8 s, 9:16, áudio ligado. Renomeie para nora{nn}-CLIPE-placa. 12 créditos.',
     'CapCut: números fixos, texto do topo, texto do story com a seta (dos 5 aos 8 s) e a música de sempre (−18 dB). Sem legenda na tela e sem corte de silêncio: a Nora não fala.',
     f'Postar em {data_post} às {hora} no Insta e no Face, ao vivo, com a localização Los Angeles, California no Insta. O story do Manifestation (3 cartas) tem de estar no ar.']
    p['comentario_fixado']={'insta':f"{signos_en}, this one is yours. 🔥 PART 2 of this sign is in my story: pick 3 cards and see what's coming for you. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222.",
     'face':f"{signos_en}, this one is yours. 🔥 PART 2 of this sign is in my Story: pick 3 cards and see what's coming for you. Tap my profile picture NOW, it's gone in 24 hours. Comment 222."}
    st=p['story']; st['textos']=[{'posicao':'Uma frase só, no centro, uma cor (creme #F1E6D3), 1 a 2 linhas','texto':"Tap below: pick 3 cards and see what's coming for you."}]; st['adesivos']=['Pick my 3 cards','See my cards']
    st['nota']='O story do Manifestation postado antes do nora36 (3 cartas) vale para este vídeo: não precisa postar outro.'
    E=p['edicao_linha']
    E[0]['texto']=TOPO; E[0]['como']='Texto no topo, em 3 linhas, do segundo 0 ao fim do clipe. “Don’t you dare scroll past this,” em amarelo-ouro; o resto branco.'
    E[2]['texto']='The second part is in my story  +  seta vermelha'
    for e in p['mapa_tela']['estilos']:
        if e['nome'].startswith('Texto do topo'): e['obs']='Centralizado, em 3 linhas, do segundo 0 ao fim do clipe. “Don’t you dare scroll past this,” em amarelo-ouro.'
        if e['nome'].startswith('Texto do story'): e['nome']='Texto do story (dos 5 aos 8 s): “The second part is in my story”'
    p['mapa_tela']['regras']=[x.replace('nora35-IMG',f'nora{nn}-IMG') for x in p['mapa_tela']['regras']]
    p['pecas']={'lista':[
      {'nome':f'nora{nn}-IMG','tipo':'imagem 1','status':'gerar','descricao':f'Edição da nora35-IMG: a mesma cena, a placa agora com {signos_pt} e 27, 28 AND 29 OF OCTOBER.','base':'nora35 (2.448 views no Insta) e o viral M2.','serve':'Outras placas: cada grupo de signos é uma edição desta mesma cena.'},
      {'nome':f'nora{nn}-CLIPE-placa','tipo':'clipe sem fala','status':'gerar','creditos':12,'descricao':'8 s: ela empurra a placa até a lente, acena e volta (o mesmo movimento do nora35).','base':'nora35 + placa do M2.','serve':'Face: versões -ESP e -VEL.'}],
      'decisao':['A placa (nora35) é o único vídeo da Nora nova que passou do teto de ~120 views no Insta: 2.448, com 8 s de tempo médio (visto inteiro) e 5 seguidores.','Mesma cena, só a placa muda: imagem por edição (sem crédito) + 1 clipe de 12 créditos.',f'{signos_pt}: os signos do dia ficam divididos entre os 4 vídeos (19h Touro/Virgem/Capricórnio, 21h Câncer/Escorpião/Peixes, 23h Gêmeos/Libra/Aquário, 01h Áries/Leão/Sagitário).']}
    html=s35[:m.start(1)]+json.dumps(p,ensure_ascii=False)+s35[m.end(1):]
    html=re.sub(r'<title>.*?</title>',f'<title>Painel nora{nn}</title>',html,count=1)
    open(f'PAINEL-NORA{nn}.html','w',encoding='utf-8').write(html)
    json.dump(p,open(D+f'p{nn}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    return p
placa('38','Gemini, Libra, Aquarius','GEMINI, LIBRA, AQUARIUS','Gêmeos, Libra e Aquário','G-E-M-I-N-I, L-I-B-R-A, A-Q-U-A-R-I-U-S','23h','27/10')
placa('39','Aries, Leo, Sagittarius','ARIES, LEO, SAGITTARIUS','Áries, Leão e Sagitário','A-R-I-E-S, L-E-O, S-A-G-I-T-T-A-R-I-U-S','01h','28/10')
for nn in ('38','39'):
    s=open(f'PAINEL-NORA{nn}.html',encoding='utf-8').read()
    for w in re.findall(r'(?i)love chart|quiz|Venus is|nora35-CLIPE|26, 27|437',s.split('const PACOTE = ')[1].split(';\n')[0]): print(nn,'resto:',w)
