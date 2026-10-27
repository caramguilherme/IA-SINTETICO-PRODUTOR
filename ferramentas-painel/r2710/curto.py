import json,re
D='/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/manif2710/'
p=json.load(open(D+'p36_novo.json',encoding='utf-8'))
L=[v['movimentacao'] for v in p['videos']]
T=[("T01-gancho-touro-virgem-capricornio","Gancho (signos e datas)","Taurus, Virgo or Capricorn: if this video reached you on October 27th, 28th or 29th, this message is 100% meant for you.",L[0]),
("T02-promessa-dinheiro-bencaos","A promessa (dinheiro, bênçãos e alguém maravilhoso)","The universe saw your faith. Unexpected money, blessings and someone incredibly wonderful are about to show up in your life.",L[3]),
("T03-cta-222-story","222 + o story","Comment 222 to claim this energy, then tap my profile picture. The second part of this sign is waiting in my stories.",L[11])]
wc=lambda s:len(s.split())
F=[t[2] for t in T]
for f in F: print(wc(f),f)
full=' '.join(F); sents=[s.strip() for s in re.findall(r'[^.!?]+[.!?]',full)]
for Lm in (22,23,24,25):
  takes=[];cur=[]
  for s in sents:
    if cur and wc(' '.join(cur+[s]))>Lm: takes.append(' '.join(cur));cur=[s]
    else: cur.append(s)
  takes.append(' '.join(cur)); print('L',Lm,len(takes),'OK' if takes==F else ('DIF',takes))
comuns={'and it','of the','in the','on the','to the','the end','the lens','of her','her head','the take','the first','the last','she gives','one short','her eyes','for one','the open','a soft','and her','at the','her face','her first','the clip','she keeps'}
def bigr(t): w=re.findall(r"[a-z0-9:%']+",t.lower()); return {' '.join(w[i:i+2]) for i in range(len(w)-1)}
for t in T:
    ov=(bigr(t[2])&bigr(t[3]))-comuns
    if ov: print('SOBREPOSICAO',t[0],ov)
json.dump(T,open(D+'curto.json','w',encoding='utf-8'),ensure_ascii=False)
