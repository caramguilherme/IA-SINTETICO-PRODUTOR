import json,re
D='/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/manif2710/'
T=json.load(open(D+'curto.json',encoding='utf-8'))
REG="27/10/2026 (Manifestation, P41, e a estratégia de vídeos curtos): li nesta sessão, com a ferramenta de leitura, FATOS-DO-ALUNO.md, CLAUDE.md, 00-LEIA-PRIMEIRO.md, BRIEFING-MANIFESTACAO.md, PROJETO-Dana.md, LICOES-FLOW-E-PROMPTS.md (inteiro), ROTEIRO-NORA36 (inteiro), BIBLIOTECA-VIDEOS-VIRAIS.md (seções 20 a 39, com o corpo A inteiro e os 148 vídeos da pesquisa), METRICAS-NORA.csv e PAINEL-MODELO.html; COMUNIDADE-E-ESTRATEGIA.md e o Discord de 26/10 foram lidos e escritos nesta sessão. Os outros arquivos de LEIA-TUDO-ANTES.md foram lidos inteiros na montagem original deste painel (26/10). Mudaram as falas (3 takes curtos), os textos da edição, a legenda, o comentário, o story e a lista de peças; imagens, pré-gancho e Central não mudam."
def save(fn,s,m,p): open(fn,'w',encoding='utf-8').write(s[:m.start(1)]+json.dumps(p,ensure_ascii=False)+s[m.end(1):])
# ---------- nora36 ----------
fn='PAINEL-NORA36.html'; s=open(fn,encoding='utf-8').read(); m=re.search(r'const PACOTE = (.*?);\n',s,re.S); p=json.loads(m.group(1))
p['videos']=[{'rotulo':'V%d'%(i+1),'cena':'Take %d/3 · %s'%(i+1,c),'duracao':'10','primeiro_quadro':'IMAGEM 1','acao':'(ver movimentação)','b_roll':'','fala':f,'movimentacao':mv,'arquivo':'nora36-'+n} for i,(n,c,f,mv) in enumerate(T)]
r=p['roteiro']
r['titulo']='Geodo (Manifestation), vídeo curto: Touro, Virgem e Capricórnio'
r['formato']='Hook visual pesado (geodo que racha, 4 s) + 3 takes curtos (~25 s): signos e datas → promessa → 222 e story'
r['molde_hook']='geodo que racha dos virais x1/x2/x5; fala no molde dos reels de manifestação mais curtidos da pesquisa (Soma Chhaya 297 mil e 125 mil, Antoine Martel 221 mil, Henry Westbrooks 89 mil) com a abertura do corpo A (signos, datas, 100% para você)'
r['duracao_total']=28
r['leitura_registro']=REG
c=p['central']
c['colagens']=[{'titulo':'nora36 (3 takes)','fala':' '.join(t[2] for t in T),'movimentacao':[t[3] for t in T],'takes':[0,1,2]}]
c['passos']=[
 'Pré-gancho e imagem (seção “Pré-gancho” e seção “Imagens”), na conta de 385 (a antiga de 437): gere a nora36-PRE-A (anexe SÓ o blueprint), a nora36-PRE-B (anexe SÓ a A) e a nora36-IMG (anexe SÓ a B). Imagem não gasta crédito. Me mande as 3 juntas.',
 'Depois do meu ok: o vídeo do pré-gancho em FRAMES (A → B), 4 s. 7 créditos. Renomeie para nora36-PRE.',
 'Central do curso: a configuração (seção “Central do curso”, com o texto LIVRE) e a colagem (fala inteira + 3 linhas). Confira: 3 takes de 10 s.',
 'Agente do Flow: anexe só a nora36-IMG, cole o aviso e o “COPIAR TUDO JUNTO” da Central, sem editar. 45 créditos. Renomeie os takes com os nomes do painel. Guarde os takes 2 e 3: o nora37 usa as cópias.',
 'Me mande a transcrição dos 3 takes antes de postar.',
 'Corte de silêncio só do corpo: suba os 3 takes de uma vez, com “Juntar tudo” ligado e Corte seco. CapCut: pré-gancho, corpo cortado, caixa do topo (desde o pré-gancho), legenda na tela, faixa do story e seta no Take 3, música de sempre (−18 dB).',
 'Antes de postar: troque o link do story, da bio e das respostas no Face para o link do Manifestation e poste o story novo (seção “Story”).',
 'Postar em 27/10 às 19h no Insta e no Face, ao vivo, com a localização Los Angeles, California no Insta.']
c['agente']['aviso']=c['agente']['aviso'].replace('12 prompts','3 prompts')
c['agente']['passos']=[x.replace('12 vídeos','3 vídeos') for x in c['agente']['passos']]
for sec in c['config']:
    for k in sec['campos']:
        if isinstance(k.get('valor'),str): k['valor']=k['valor'].replace('12 takes','3 takes')
E=p['edicao_linha']
E[2]['como']='Faixa verde do mapa. Destaque em amarelo-ouro: money, blessings e 222.'
E[3]={'quando':'3. No Take 3, até o fim','texto':'The second part is in my Stories ⭐','como':'Faixa no topo, no mesmo lugar da caixa (X 0 · Y 397): caixa branca arredondada, texto preto, “my Stories” em vermelho. Começa em “Comment 222”.'}
E[4]={'quando':'4. No Take 3','texto':'Seta vermelha','como':'Embaixo à esquerda, apontando para baixo, para a foto do perfil, do “Comment 222” até o fim.'}
for e in p['mapa_tela']['estilos']:
    if e['nome']=='Seta vermelha': e['obs']=re.sub(r'Takes \d+ e \d+','Take 3',e['obs'])
P=p['pecas']
lista=[x for x in P['lista'] if not x['nome'].startswith('nora36-T')]
for x in lista:
    if x['nome']=='nora36-IMG': x['descricao']=x['descricao'].replace('dos 12 takes','dos 3 takes')
for i,(n,cn,f,mv) in enumerate(T):
    lista.append({'nome':'nora36-'+n,'tipo':['gancho','corpo','CTA'][i],'status':'gerar','creditos':15,'descricao':'Take %d: “%s”'%(i+1,f),'base':['Abertura do corpo A (signos, datas, 100% para você).','Corpo A (“the universe saw your faith”, dinheiro e alguém maravilhoso de forma inesperada) no tom dos reels positivos mais curtidos (Soma Chhaya).','“Claim this energy” e “comment 222” (Soma Chhaya, Henry) + o story do corpo A.'][i],'serve':'Só deste vídeo (cada grupo de signos tem o seu Take 1).' if i==0 else 'nora37 e os próximos curtos da série (cópia renomeada).'})
P['lista']=lista
P['decisao']=['Estratégia de 27/10: vídeos curtos. Na Nora nova, os falados de 60 a 80 s pararam em 107 a 122 views e o curto de 30 s em 125; o único que destravou foi o de 8 s visto até o fim (nora35, 2.448). Por isso 3 takes (~25 s), não 12.','Hook visual pesado: o geodo que racha (3 de 5 vídeos da conta dos x).','Corpo e CTA gerados uma vez: o nora37 e os próximos curtos só trocam o Take 1 (15 créditos cada) e o pré-gancho.']
P['proximos_intro']='Mesma nora36-IMG, Take 1 novo (15 créditos cada) e os takes 2 e 3 copiados; pré-gancho do geodo espelhado ou outro já pronto (nora34-PRE, nora25-PRE a nora28-PRE).'
json.dump(p,open(D+'p36_curto.json','w',encoding='utf-8'),ensure_ascii=False,indent=1); save(fn,s,m,p)
# ---------- nora37 ----------
fn='PAINEL-NORA37.html'; s=open(fn,encoding='utf-8').read(); m=re.search(r'const PACOTE = (.*?);\n',s,re.S); q=json.loads(m.group(1))
q['videos'][0]['cena']='Take 1/3 · Gancho (Câncer, Escorpião e Peixes)'
q['roteiro']['titulo']='Geodo (Manifestation), vídeo curto: Câncer, Escorpião e Peixes (só o Take 1 novo)'
q['roteiro']['formato']='Pré-gancho do nora36 espelhado + Take 1 novo + Takes 2 e 3 do nora36 (~25 s)'
q['roteiro']['molde_hook']=r['molde_hook']; q['roteiro']['duracao_total']=28; q['roteiro']['leitura_registro']=REG
q['pre_gancho']['montagem']=q['pre_gancho']['montagem'].replace('takes 2 a 12','takes 2 e 3')
q['imagem_reutilizada']['aviso']=q['imagem_reutilizada']['aviso'].replace('takes 2 a 12','takes 2 e 3')
q['central']['passos']=[x.replace('takes 2 a 12','takes 2 e 3').replace('nora37-T01 a nora37-T12','nora37-T01 a nora37-T03') for x in q['central']['passos']]
q['edicao_linha']=[dict(e) for e in p['edicao_linha']]
q['edicao_linha'][0]['texto']='Pré-gancho (nora36-PRE espelhado, uns 3,5 s)'
q['edicao_linha'][1]['texto']='Cancer, Scorpio, Pisces, pay very close attention'
for e in q['mapa_tela']['estilos']:
    if e['nome']=='Seta vermelha': e['obs']=re.sub(r'Takes \d+ e \d+','Take 3',e['obs'])
Q=q['pecas']
lista=[x for x in Q['lista'] if not x['nome'].startswith('nora36-T')]
for x in lista:
    if x['nome']=='nora36-IMG': x['descricao']='Primeiro e último quadro do Take 1, a mesma dos takes 2 e 3.'
for i,(n,cn,f,mv) in enumerate(T[1:],2):
    lista.append({'nome':'nora36-'+n,'de':'nora36-'+n,'tipo':('CTA' if i==3 else 'corpo')+' (do nora36)','status':'reutilizar','creditos':15,'fala':f,'descricao':'Para a ferramenta de corte, renomeie a cópia para nora37-'+n+'.'})
Q['lista']=lista
json.dump(q,open(D+'p37_curto.json','w',encoding='utf-8'),ensure_ascii=False,indent=1); save(fn,s,m,q)
def walk(o,path=''):
    if isinstance(o,dict):
        for k,v in o.items(): yield from walk(v,path+'.'+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): yield from walk(v,path+'[%d]'%i)
    elif isinstance(o,str): yield path,o
pat=re.compile(r'12 takes|Take 10|Takes 11|T12|takes 2 a 1|180 créditos|187',re.I)
for nm,o in (('36',p),('37',q)):
    for path,v in walk(o):
        mm=pat.search(v)
        if mm: print(nm,path,'|',v[max(0,mm.start()-60):mm.end()+40])
print('creditos36',sum(x.get('creditos',0) for x in p['pecas']['lista'] if x['status']=='gerar'),'creditos37',sum(x.get('creditos',0) for x in q['pecas']['lista'] if x['status']=='gerar'))
