# 28/10 ~14h: conferência dos painéis 37 a 41 (datas das placas e do nora39 para 28, 29 e 30; conta de 404;
# horário do teste; faixa da legenda confirmada na nora37-IMG; registro de leitura do nora41).
import json,re
def load(f):
    s=open(f,encoding='utf-8').read(); m=re.search(r'const PACOTE = (\{.*?\});\n',s,re.S)
    return s,m,json.loads(m.group(1))
def save(f,s,m,p):
    open(f,'w',encoding='utf-8').write(s[:m.start(1)]+json.dumps(p,ensure_ascii=False)+s[m.end(1):])
def walk(o,fn):
    if isinstance(o,dict): return {k:walk(v,fn) for k,v in o.items()}
    if isinstance(o,list): return [walk(v,fn) for v in o]
    if isinstance(o,str): return fn(o)
    return o
LEG_OLD='A faixa da legenda (69% a 77%, logo abaixo das metades do geodo) é provisória: eu confirmo quando você me mandar a nora37-IMG.'
LEG_NEW='Faixa da legenda confirmada na nora37-IMG: centro em Y -294 (73% da altura), abaixo do geodo e das pontas dos dedos, em cima da blusa preta. Use blocos de 1 linha; se uma legenda de 2 linhas cobrir os dedos da mão do lado esquerdo, quebre em dois blocos.'
def comum(t):
    t=t.replace('Nos Take 3','No Take 3')
    t=t.replace('conta de 385 (a antiga de 437)','conta de 404').replace('conta de 385, a antiga de 437)','conta de 404)')
    t=t.replace('suba nela a nora35-IMG','se a nora35-IMG não estiver nela, suba')
    t=t.replace(LEG_OLD,LEG_NEW)
    return t
for f in ['PAINEL-NORA37.html','PAINEL-NORA38.html','PAINEL-NORA39.html','PAINEL-NORA40.html','PAINEL-NORA41.html']:
    s,m,p=load(f)
    fn=comum
    if f in ('PAINEL-NORA38.html','PAINEL-NORA40.html'):
        fn=lambda t: comum(t).replace('27, 28 AND 29','28, 29 AND 30')
    if f=='PAINEL-NORA39.html':
        fn=lambda t: comum(t).replace('October 27th, 28th or 29th','October 28th, 29th or 30th').replace(
            'Às 23h é o teste de variação no Insta (Lucas): compara com o nora37 das 19h','Às 21h é o teste de variação no Insta (Lucas): compara com o nora37 das 17h')
    p=walk(p,fn)
    if f=='PAINEL-NORA37.html':
        x=p['pecas']['proximos'][0]; x['gancho']=x['gancho'].replace('October 27th, 28th or 29th','October 28th, 29th or 30th')
    if f=='PAINEL-NORA41.html':
        r=p['roteiro']
        k=[k for k in r if 'leitura' in k.lower()] 
        print('chaves de leitura:',k)
    save(f,s,m,p)
    print(f,'ok')
