import re,html,json,sys
S=sys.argv[1]
t=open(S+'/gdoc/pesquisa.txt',encoding='utf-8').read()
ig=[];seen=set()
for line in t.splitlines():
    for m in re.finditer(r'instagram\.com/(?:[A-Za-z0-9_.]+/)?reel/([A-Za-z0-9_-]+)',line):
        i=m.group(1)
        if i in seen: continue
        seen.add(i)
        nota=re.sub(r'https?://\S+','',line).strip()
        ig.append({'id':i,'nota':nota})
f=open(S+'/gdoc/folder.html',encoding='utf-8').read()
dr=[]
for m in re.finditer(r'<a href="https://drive.google.com/file/d/([^/]+)/view[^"]*"[^>]*>.*?<div class="flip-entry-title">(.*?)</div>',f,re.S):
    nome=html.unescape(m.group(2))
    if re.search(r'bezos|tom hanks',nome,re.I): continue
    dr.append({'id':m.group(1),'nome':nome})
json.dump({'ig':ig,'drive':dr},open(S+'/manif/lista.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(ig),'reels;',len(dr),'ads do Drive')
