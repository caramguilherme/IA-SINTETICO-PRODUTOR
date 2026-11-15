import json,glob,os,re,sys
M=sys.argv[1]
L=json.load(open(M+'/lista.json',encoding='utf-8'))
nota={x['id']:x['nota'] for x in L['ig']}; nome={x['id']:x['nome'] for x in L['drive']}
rows=[]
for t in sorted(glob.glob(M+'/txt/*.txt')):
    b=os.path.basename(t)[:-4]; sub,i=b.split('-',1)
    txt=open(t,encoding='utf-8').read().splitlines()
    head=txt[0]; lang=re.search(r'lang=(\w+)',head).group(1); dur=int(re.search(r'dur=(\d+)',head).group(1))
    fala=' '.join(re.sub(r'^\[[^\]]*\]\s*','',l) for l in txt[1:])
    info={}
    if sub=='ig':
        f=M+'/ig/'+i+'.info.json'
        if os.path.exists(f):
            j=json.load(open(f,encoding='utf-8')); info={'likes':j.get('like_count'),'views':j.get('view_count'),'user':j.get('uploader') or j.get('channel'),'data':j.get('upload_date'),'leg':(j.get('description') or '')[:160].replace('\n',' ')}
    rows.append({'sub':sub,'id':i,'lang':lang,'dur':dur,'palavras':len(fala.split()),'fala':fala,'nota':nota.get(i,''),'nome':nome.get(i,''),**info})
json.dump(rows,open(M+'/indice.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
en=[r for r in rows if r['lang']=='en']
en.sort(key=lambda r:-(r.get('likes') or 0))
for r in en:
    print(f"{r['sub']}|{r['id']}|{r.get('user','')}|likes {r.get('likes')}|{r.get('data','')}|{r['dur']}s|{r['palavras']}p|{(r['nome'] or r['nota'])[:60]}\n   HOOK: {' '.join(r['fala'].split()[:40])}")
