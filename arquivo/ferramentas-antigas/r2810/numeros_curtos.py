# 28/10: volta os números fixos 222 e 11:11 aos curtos do geodo (nora37 e nora39), como em todo vídeo da Nora.
import json,re,sys
EST={"nome":"Números fixos (222 à esquerda, 11:11 à direita)","fonte":"Poppins Bold (poppins-bd)","cor":"amarelo-ouro #FFD21F","tamanho":"12","contorno":"Traço preto + Sombra preta, sem Plano de fundo. Luz DESLIGADA","obs":"Os dois do mesmo tamanho e na mesma altura, acima da caixa do topo (faixa azul do mapa)."}
LIN={"quando":"O vídeo todo (do primeiro quadro do pré-gancho ao fim)","texto":"222  e  11:11","como":"Números fixos nos cantos de cima, em amarelo-ouro: 222 à esquerda e 11:11 à direita, acima da caixa do topo."}
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    m=re.search(r'const PACOTE = (\{.*?\});\n',s,re.S)
    p=json.loads(m.group(1))
    mt=p['mapa_tela']
    if not any('Números fixos' in e['nome'] for e in mt['estilos']):
        mt['estilos'].insert(0,EST)
    mt['regras']=[r for r in mt['regras'] if not r.startswith('Sem números fixos')]
    mt['regras'].insert(0,'Números fixos 222 e 11:11 na faixa azul, o vídeo todo; a caixa do topo fica logo abaixo deles, sem encostar.')
    L=p['edicao_linha']
    L[:]=[e for e in L if '222  e  11:11' not in e['texto']]
    for e in L:
        if 'Sem números fixos' in e.get('como',''): e['como']='Volume baixo, por baixo da voz.'
    L.insert(2,dict(LIN))
    n=0
    for e in L:
        q=re.sub(r'^\d+\.\s*','',e['quando'])
        e['quando']=f'{n}. {q}'; n+=1
    s=s[:m.start(1)]+json.dumps(p,ensure_ascii=False)+s[m.end(1):]
    open(f,'w',encoding='utf-8').write(s)
    print(f,[x['quando'] for x in L])
