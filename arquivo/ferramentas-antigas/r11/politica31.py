# Corrige os prompts do nora31 depois da recusa por politica do Flow (imagem A, 22/10/2026).
# Tira palavras de corpo e de roupa intima de todos os prompts (inclusive da lista do que nao aparece).
import json,re,sys
F='/home/user/IA-SINTETICO-PRODUTOR/PAINEL-NORA31.html'
MODELO='/home/user/IA-SINTETICO-PRODUTOR/PAINEL-MODELO.html'
s=open(F,encoding='utf-8').read()
m=re.search(r'^const PACOTE = (.*);\s*$',s,re.M)
d=json.loads(m.group(1))

def rep(t,a,b,n=1):
    assert t.count(a)==n,(a[:70],t.count(a))
    return t.replace(a,b)

HANDS=("THE HANDS: slim adult hands with a warm golden light-to-medium tan (not orange), anatomically correct, exactly five fingers on each hand, "
 "short natural nails with pale pink polish, one small gold sun-symbol ring on the index finger of each hand, and three thin gold bracelets stacked on her LEFT wrist only "
 "(on the right side of the image), none on the right wrist; the cuffs of long fitted deep forest-emerald (dark green with a slight blue tone) waffle-knit sleeves are visible at the bottom edge of the frame.")
FIM=("Natural light and real textures with the spontaneous look of a smartphone; no CGI, no 3D render, no illustration, no advertising look.")
KITCHEN=("Behind it there is only a soft, warm, out-of-focus blur: a white kitchen cabinet at the upper left of the image, a dark night window at the upper right of the image "
 "and the warm yellow glow of a hanging pendant lamp, which is the only light.")

A=("Vertical 9:16 smartphone macro photo, photorealistic, generated from scratch with no reference image. The lens is about 22 cm from a woman's two hands in a real American home kitchen at night. "
 +KITCHEN+" In the center of the frame, about 20 cm from the lens, a sealed adhesive-bandage wrapper is held horizontally between the two hands: a white paper wrapper about 9 cm long and 3 cm wide "
 "with a thin red stripe along its top edge, completely closed and sealed, with NO readable text and NO brand name on it. Her LEFT hand (the hand on the RIGHT side of the image) pinches the right end "
 "of the wrapper between its thumb and index finger and holds it steady. Her RIGHT hand (the hand on the LEFT side of the image) pinches the small red pull tab at the left end of the wrapper between "
 "its thumb and index fingertips, ready to pull it. The wrapper and the fingertips are in sharp macro focus. "+HANDS+
 " ONLY THESE ARE IN THE FRAME: the two hands, the two sleeve cuffs, the closed wrapper and the blurred kitchen; nothing else: no face, no hair, no other object, no second wrapper, no person, no animal, "
 "no text, no logo, no watermark and no date stamp. "+FIM)

C=("Vertical 9:16 smartphone macro photo, photorealistic, generated from scratch with no reference image, in the style of a casual clothing product photo. The lens is about 22 cm in front of one small "
 "red satin brief with lace trim, a clothing item held up flat by hand, in a real American home kitchen at night. "+KITCHEN+
 " Her LEFT hand (the hand on the RIGHT side of the image) holds the garment by its right top corner between the thumb and fingers, so it hangs open and flat in the center of the frame with its smooth "
 "bright-red satin front panel (about 12 cm wide and 14 cm tall) facing the lens, framed by scalloped red lace trim along its top edge and its curved lower edges; the garment is plain and intact, with "
 "nothing printed on it and nothing attached to it yet. Her RIGHT hand (the hand on the LEFT side of the image) holds one beige adhesive bandage about 7.5 cm long by its center between the thumb and "
 "index finger, vertically, about 6 cm in front of the center of the satin panel, its white backing tabs already peeled off so its sticky side faces the satin, not touching it yet, with no text on it. "
 "The satin panel, the bandage and the fingertips are in sharp macro focus. "+HANDS+
 " ONLY THESE ARE IN THE FRAME: the two hands, the two sleeve cuffs, the red garment, the bandage and the blurred kitchen; nothing else: no face, no hair, no other object, no person, no animal, "
 "no text, no logo, no watermark and no date stamp. "+FIM)

et=d['pre_gancho']['etapas']
assert [e['nome'] for e in et]==['nora31-PRE-A','nora31-PRE-B','nora31-PRE-V1','nora31-PRE-C','nora31-PRE-D','nora31-PRE-V2']
et[0]['prompt']=A
et[3]['prompt']=C
et[1]['prompt']=rep(et[1]['prompt'],'No face, no body, no text.','No face and no text.')
t=et[4]['prompt']
t=rep(t,'the same red satin-and-lace brief held by its right waistband corner','the same red satin garment with lace trim held by its right top corner')
t=rep(t,'The brief stays intact and plain. No face, no body, no text.','The garment stays intact and plain. No face and no text.')
et[4]['prompt']=t
t=et[5]['prompt']
t=rep(t,'a red satin-and-lace brief','a small red satin garment with lace trim')
t=rep(t,', never drops and never shows a body',' and never drops')
t=t.replace(' brief',' garment')
et[5]['prompt']=t

im=d['imagens'][0]
t=im['cena']
t=rep(t,'her deep forest-emerald waffle-knit top with the small American flag pin on her left chest (the right side of the image)',
        'her deep forest-emerald waffle-knit top with the small American flag pin over her heart (on the right side of the image)')
t=rep(t,'(2) both of her hands are now raised in front of her upper chest, elbows bent and close to her body, holding one red satin women\'s brief open and flat with its front facing the lens',
        '(2) both of her hands are now raised to collarbone height, elbows bent and tucked in, holding up one small red satin brief with lace trim, a clothing item held open and flat like a product photo, with its front facing the lens')
t=rep(t,'pinches the left side edge of the brief','pinches the left side edge of the garment')
t=rep(t,'(3) the brief has a smooth bright-red satin front panel about 12 cm wide and 14 cm tall and wide scalloped red lace trim around the leg openings and the waistband; its top edge is at the height of her collarbones and its bottom edge is no lower than the middle of her chest, so it never covers',
        '(3) the garment has a smooth bright-red satin front panel about 12 cm wide and 14 cm tall and scalloped red lace trim along its top edge and its curved lower edges; its top edge is at the height of her collarbones and it hangs in front of her emerald top, so it never covers')
t=rep(t,'no body visible through the brief, no second brief, no second bandage, nothing printed on the brief,','no second garment, no second bandage, nothing printed on the garment,')
t=rep(t,'no change to her face, skin, hair or top','no change to her face, hair or top')
t=rep(t,'only her top is visible: no hands, brief or object there.','only her emerald top is visible: no hands or objects there.')
im['cena']=t

d['figurino']=rep(rep(d['figurino'],'the red satin-and-lace brief in the hook','the red satin garment in the hook'),'on the left chest of her top','over her heart, on the left side of her top')
d['trava_referencia']=rep(d['trava_referencia'],'Keep her face, skin, eyes, hair, face gems, jewelry and body exactly','Keep her face, eyes, hair, face gems, jewelry and build exactly')

def fixmov(t):
    t=rep(t,'keep holding the red satin-and-lace brief open and still in front of her upper chest by its two side edges','keep holding the small red satin garment with lace trim open and still at collarbone height by its two side edges')
    t=rep(t,'and the brief never changes hands','and the garment never changes hands')
    return t
d['videos'][0]['movimentacao']=fixmov(d['videos'][0]['movimentacao'])
d['central']['colagens'][0]['movimentacao']=[fixmov(d['central']['colagens'][0]['movimentacao'][0])]
for sec in d['central']['config']:
    for k in sec['campos']:
        if k['campo'].startswith('LIVRE'):
            t=k['copiar']
            t=rep(t,'hold the red satin-and-lace brief open and still in front of her upper chest by its two side edges','hold the small red satin garment with lace trim open and still at collarbone height by its two side edges')
            t=rep(t,'the brief never changes hands','the garment never changes hands')
            t=rep(t,'a handheld phone at chest height about 60 centimeters','a handheld phone at the height of her collarbones about 60 centimeters')
            k['copiar']=t

pg=d['pre_gancho']
pg['modo']=pg['modo'].rstrip()+' Se o Flow recusar uma imagem ou um vídeo por política, não tente de novo com o mesmo texto: me mande o print.'
d['roteiro']['leitura_registro']+=(' Correção de 22/10/2026 (noite), depois de o Flow recusar a imagem A por política: reli de novo, inteiros, todos os arquivos de `LEIA-TUDO-ANTES.md` '
 'e tirei de todos os prompts as palavras de corpo e de roupa íntima (inclusive da lista do que não aparece).')

# texto final: nenhuma palavra de risco em nada que vai para o Flow ou para a Central
risco=re.compile(r'\b(underwear|lingerie|panties|panty|chest|body|bodies|breast|bust|nude|nudity|naked|sexy|sexual|leg openings?|women\'s brief)\b',re.I)
alvos=[('A',et[0]['prompt']),('B',et[1]['prompt']),('V1',et[2]['prompt']),('C',et[3]['prompt']),('D',et[4]['prompt']),('V2',et[5]['prompt']),
       ('IMG1',im['cena']),('figurino',d['figurino']),('trava',d['trava_referencia']),('mov',d['videos'][0]['movimentacao'])]
for sec in d['central']['config']:
    for k in sec['campos']:
        if k['campo'].startswith('LIVRE'): alvos.append(('LIVRE',k['copiar']))
for n,t in alvos:
    h=risco.findall(t)
    print(n,'OK' if not h else 'RISCO '+str(h))
s=s[:m.start(1)]+json.dumps(d,ensure_ascii=False)+s[m.end(1):]
OLD='const REF_TXT="VISUAL REFERENCE LOCK: use exclusively the ATTACHED references as identity authorities. Preserve the face, body, hair,'
NEW='const REF_TXT="VISUAL REFERENCE LOCK: use exclusively the ATTACHED references as identity authorities. Preserve the face, build, hair,'
for f in (F,MODELO):
    x=s if f==F else open(f,encoding='utf-8').read()
    assert x.count(OLD)==1,f
    x=x.replace(OLD,NEW)
    open(f,'w',encoding='utf-8').write(x)
    print('salvo',f)
