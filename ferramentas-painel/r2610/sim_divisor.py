import re
T=[
"Taurus, Virgo or Capricorn: if this reached you on October 26th, 27th or 28th, it's meant for you. Don't tell anyone.",
"I don't know your name or what you've been through, but I can see the pattern you keep repeating in love.",
"You know something's off in love, but you can't say what. And I see a cycle opening that favors new connections.",
"If you scroll past this, you'll live the same story again with a different man. So take this seriously.",
"In astrology, your sun sign isn't the problem. Your Venus, your Moon and your 7th house decide who you keep choosing.",
"When they clash, you fall for the wrong man and blame yourself. It's not bad luck. It's a pattern.",
"Imagine finally understanding why, before you give another year to someone who doesn't fit you. Send this video to yourself now.",
"Now save this video, that will be your first seal. Double tap quickly on your screen, that will be your second seal.",
"Comment 222 so I can see you did everything. Then tap my profile picture and check my stories before they disappear.",
"The second part is waiting there: a quick quiz that reads your love chart and shows what kind of partner fits you.",
]
wc=lambda s:len(s.split())
for i,t in enumerate(T,1): print(i,wc(t),t)
full=' '.join(T)
print('total',wc(full))
sents=re.findall(r'[^.!?]+[.!?]',full)
sents=[s.strip() for s in sents]
for L in (22,23,24,25):
  takes=[];cur=[]
  for s in sents:
    if cur and wc(' '.join(cur+[s]))>L:
      takes.append(' '.join(cur));cur=[s]
    else: cur.append(s)
  takes.append(' '.join(cur))
  ok = takes==T
  print('L',L,len(takes),'OK' if ok else 'DIFERENTE')
  if not ok:
    for k in takes: print('   ',wc(k),k)
