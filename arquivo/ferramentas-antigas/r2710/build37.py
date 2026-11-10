import json,re
D='/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/manif2710/'
exec(open(D+'falas.py').read())
p36=json.load(open(D+'p36_novo.json',encoding='utf-8'))
s=open('PAINEL-NORA37.html',encoding='utf-8').read()
m=re.search(r'const PACOTE = (.*?);\n',s,re.S); p=json.loads(m.group(1))
f1="Cancer, Scorpio or Pisces: if this video reached you on October 27th, 28th or 29th, this message is 100% meant for you."
mov1=p36['videos'][0]['movimentacao']
v=p['videos'][0]; v['cena']='Take 1/12 · Gancho (Câncer, Escorpião e Peixes)'; v['fala']=f1; v['movimentacao']=mov1
r=p['roteiro']
r['titulo']='Série do geodo (Manifestation): Câncer, Escorpião e Peixes (só o Take 1 novo)'
r['dor']=p36['roteiro']['dor']
r['formato']='Série: pré-gancho do nora36 espelhado + Take 1 novo + Takes 2 a 12 do nora36'
r['duracao_total']=95
r['descricao_instagram']="Cancer, Scorpio, Pisces: if this reached you, it's not by chance. 🔮\nComment 222. Tap my photo NOW: the second part of this sign is in my story.\n#manifestation #astrology #zodiac #usa #usareels"
r['leitura_registro']=p36['roteiro']['leitura_registro']
p['texto_tela']['hook_termina']='this message is 100% meant for you'
p['comentario_fixado']={'insta':"Cancer, Scorpio, Pisces, this one is yours. 🔥 PART 2 of this sign is in my story: pick 3 cards and see what's coming for you. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222.",
 'face':"Cancer, Scorpio, Pisces, this one is yours. 🔥 PART 2 of this sign is in my Story: pick 3 cards and see what's coming for you. Tap my profile picture NOW, it's gone in 24 hours. Comment 222."}
p['pre_gancho']['montagem']=p['pre_gancho']['montagem'].replace('takes 2 a 10','takes 2 a 12')
c=p['central']
c['colagens'][0]['fala']=f1; c['colagens'][0]['movimentacao']=[mov1]
c['passos']=[
 'Imagem: não gere. O Take 1 usa a nora36-IMG (conta de 385, a antiga de 437).',
 'Central do curso: a MESMA configuração do nora36 (seção “Central do curso”, com o texto LIVRE do nora36). Cole só a fala do Take 1 e a linha de movimentação dele. Clique em GERAR PROMPT DE ANIMAÇÃO e confira: 1 take de 10 s.',
 'Agente do Flow: anexe a nora36-IMG (só ela), cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take). 15 créditos. Renomeie para nora37-T01-gancho-cancer-escorpiao-peixes.',
 'Os takes 2 a 12 NÃO são gerados: são os do nora36 (lista em “Nomes e reaproveitamento”). Faça uma cópia de cada um e renomeie de nora36-T02… para nora37-T02… (a ferramenta de corte junta pela ordem do nome; por isso os números têm 2 dígitos).',
 'Me mande a transcrição do Take 1 e a emenda com o Take 2 antes de postar.',
 'Corte de silêncio (seção “Cortar os silêncios”): suba nora37-T01 a nora37-T12 de uma vez, com “Juntar tudo” ligado e Corte seco. CapCut: pré-gancho espelhado, corpo cortado e os textos da seção de texto na tela.',
 'Postar em 27/10 às 21h no Insta e no Face, ao vivo, com a localização Los Angeles, California no Insta (2 h depois do nora36). Mesmo corpo do nora36, hook espelhado e signos novos: é o teste de variação no Insta.']
p['story']['textos']=p36['story']['textos']; p['story']['adesivos']=p36['story']['adesivos']
p['story']['nota']='O story novo do nora36 (3 cartas, link do Manifestation) vale para este vídeo: não precisa postar outro.'
p['edicao_linha']=[dict(e) for e in p36['edicao_linha']]
p['edicao_linha'][0]['texto']='Pré-gancho (nora36-PRE espelhado, uns 3,5 s)'
p['edicao_linha'][1]['texto']='Cancer, Scorpio, Pisces, pay very close attention'
for e in p['mapa_tela']['estilos']:
    if e['nome'].startswith('Faixa do story'): e['nome']='Faixa do story no topo: “The second part is in my Stories ⭐”'
    if e['nome']=='Seta vermelha': e['obs']=e['obs'].replace('Takes 9 e 10','Takes 11 e 12')
P=p['pecas']
lista=[x for x in P['lista'] if x['nome'] in ('nora36-PRE','nora36-IMG')]
for x in lista:
    if x['nome']=='nora36-IMG': x['descricao']='Primeiro e último quadro do Take 1, a mesma dos takes 2 a 12.'
lista.append({'nome':'nora37-T01-gancho-cancer-escorpiao-peixes','tipo':'gancho','status':'gerar','creditos':15,'descricao':'Take 1: “%s”'%f1,'base':'Take 1 da série (corpo A: signos + datas em que ela vê o vídeo + 100% para você).','serve':'Só deste vídeo.'})
for i,(n,cn,f) in enumerate(T[1:],2):
    lista.append({'nome':'nora36-'+n,'de':'nora36-'+n,'tipo':('CTA' if i>=10 else 'corpo')+' (do nora36)','status':'reutilizar','creditos':15,'fala':f,'descricao':'Para a ferramenta de corte, renomeie a cópia para nora37-'+n+'.'})
P['lista']=lista
P['decisao']=['Série do geodo (x1 → x2): mesmo corpo e mesmo clipe de hook espelhado, outros signos. A conta dos x posta assim no mesmo dia (x2 e x3).','Às 21h é o teste de variação no Insta (Lucas): compara com o nora36 das 19h.']
open(D+'p37_novo.json','w',encoding='utf-8').write(json.dumps(p,ensure_ascii=False,indent=1))
open('PAINEL-NORA37.html','w',encoding='utf-8').write(s[:m.start(1)]+json.dumps(p,ensure_ascii=False)+s[m.end(1):])
def walk(o,path=''):
    if isinstance(o,dict):
        for k,v in o.items(): yield from walk(v,path+'.'+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): yield from walk(v,path+'[%d]'%i)
    elif isinstance(o,str): yield path,o
pat=re.compile(r'love chart|quiz|437|takes 2 a 10|T10|Take 8|Takes 9|26/10|pattern|7th house|01h',re.I)
for path,vv in walk(p):
    mm=pat.search(vv)
    if mm: print(path,'|',vv[max(0,mm.start()-70):mm.end()+50].replace('\n',' '))
print('ok',sum(x['creditos'] for x in lista if x['status']=='gerar'))
