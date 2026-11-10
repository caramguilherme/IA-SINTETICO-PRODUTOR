# 22/10/2026 23h30: nora33 (texto na tela) passa a usar a nora30-IMG, para postar hoje sem gerar imagem nova.
# Também: imagens A a D do nora31 na versão curta (mãos só pelo lado da imagem, sem "woman/her/adult/slim").
import json,re
R='/home/user/IA-SINTETICO-PRODUTOR/'
def load(f):
    s=open(R+f,encoding='utf-8').read(); m=re.search(r'^const PACOTE = (.*);\s*$',s,re.M)
    return s,m,json.loads(m.group(1))
def save(f,s,m,d):
    open(R+f,'w',encoding='utf-8').write(s[:m.start(1)]+json.dumps(d,ensure_ascii=False)+s[m.end(1):])
def rep(t,a,b):
    assert t.count(a)==1,(a[:60],t.count(a)); return t.replace(a,b)
risco=re.compile(r'\b(underwear|lingerie|panties|panty|chest|body|breast|bust|nude|naked|sexy|sexual|adult|slim)\b',re.I)

# ---------- nora33 ----------
s,m,d=load('PAINEL-NORA33.html')
d['roteiro']['titulo']="Texto na tela: it works so fast it’s scary (imagem do nora30)"
d['roteiro']['leitura_registro']=("22/10/2026 (noite): antes de reescrever o clipe para a imagem do nora30, li inteiros nesta sessão, com a ferramenta de leitura, todos os arquivos de `LEIA-TUDO-ANTES.md` "
 "(`FATOS-DO-ALUNO.md`, `CLAUDE.md`, `00-LEIA-PRIMEIRO.md`, `PROJETO-Dana.md`, `BRIEFING-LOVECHART.md`, `LICOES-FLOW-E-PROMPTS.md`, os três `DNA Visual`, `REGISTRO-DE-PERSONAS.md`, `hooks.md`, "
 "`Formatos Narrativos…`, `Exemplos de Roteiros…`, `ctas.md`, `COMUNICACAO-VISCERAL-E-FALADA.md`, as `BIBLIOTECA-*`, `PESQUISA-PUBLICO.md`, `Prompts.txt`, `CHECKLIST-DE-PRODUCAO.md`, `PAPEL-AGENTE-FLOW.md`, "
 "`GUIA-CREATIVE-HUB.md`, os `PLANO-CREDITOS-*` e `PASSO-A-PASSO-*`, os `EXEMPLO-*`, `PAINEL-MODELO.html`, `METRICAS-NORA.csv`, `BIBLIOTECA-DE-TAKES.md`, os `ROTEIRO-*`, os `STORY-*` e os `TAKE-NOVO-*`); "
 "sem mudança desde a leitura, fora as minhas notas no `CLAUDE.md`, no `FATOS-DO-ALUNO.md` e no `LICOES-FLOW-E-PROMPTS.md`.")
d['imagens'][0]['cena']='A mesma do nora30 (não gerar).'
d['imagem_reutilizada']={"arquivo":"nora30-IMG (a IMAGEM 1 do nora30)","aviso":"Use a IMAGEM 1 do nora30 (a Nora na cozinha à noite, com o geodo de ametista na mão esquerda, no lado direito da imagem). Não gere imagem nova."}
d['pecas']={"lista":[
  {"nome":"nora30-IMG","de":"nora30-IMG","tipo":"imagem 1","status":"reutilizar","descricao":"A IMAGEM 1 do nora30 (cozinha à noite, geodo de ametista)."},
  {"nome":"nora33-CLIPE-texto-na-tela","tipo":"clipe sem fala","status":"gerar","creditos":12,"descricao":"Clipe de 8 s: ela olha para a lente, põe o dedo nos lábios e volta.","base":"Formato texto na tela (Eduardo, Mattias) + texto do topo dos virais w6, w7 e U7.","serve":"Só deste vídeo."}],
  "decisao":["Postar hoje (22/10) sem gerar imagem nova: o clipe anima a imagem do nora30, já aprovada."]}
c=d['central']
c['conferir']="Conferir: é a Nora da imagem do nora30; ela não fala; o dedo vai só aos lábios; o geodo fica na mão esquerda dela (lado direito da imagem) do começo ao fim; a cozinha fica parada."
c['passos']=["Clipe só de 8 s, SEM fala. Não usa a Central do curso nem o agente.",
 "Imagem: a IMAGEM 1 do nora30 (nora30-IMG). Não gere imagem nova.",
 "Flow, modo FRAMES: primeiro e último quadro = a nora30-IMG; 8 s, 9:16, áudio ligado; cole o prompt da seção “Clipe”. Renomeie para nora33-CLIPE-texto-na-tela. 12 créditos.",
 "Story antes do vídeo: a mesma imagem do pingente, texto “Tap below and take the free love quiz.”, adesivo “Take the free quiz”.",
 "CapCut: texto do topo, números fixos, segundo texto com a seta e a música de sempre (−18 dB). Sem legenda automática e sem corte de silêncio."]
pg=d['pre_gancho']
pg['modo']="Um vídeo só, em FRAMES: primeiro e último quadro = a nora30-IMG. 8 s, 9:16, áudio ligado. Se o Flow recusar por política, não repita o mesmo texto: me mande o print."
pg['conceito']="Formato texto na tela, com a Nora da imagem do nora30. Texto do topo dos virais w6, w7 e U7. Ela não fala: olha para a lente, põe o dedo nos lábios e volta à posição."
e=pg['etapas'][0]
e['quadros']="Modo FRAMES. Primeiro quadro: nora30-IMG. Último quadro: a mesma nora30-IMG. 8 s, 9:16, áudio ligado."
e['prompt']=("Create a single continuous 8-second video clip that opens exactly on the first supplied frame and ends exactly on the last supplied frame (they are the same image), vertical 9:16. "
 "Handheld smartphone camera about 60 cm from the woman at the height of her collarbones, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n"
 "THE MAIN EVENT: the woman, sitting in a home kitchen at night under a warm hanging lamp, looks into the lens, raises her free hand and presses one index finger against her lips in a silent "
 "keep-it-secret gesture, holds it, then lowers it. She never speaks. In the first frame her left hand (on the RIGHT side of the image) holds the large slab of purple amethyst crystals beside her face "
 "with the crystals facing the lens, and her right hand rests out of frame below the bottom edge.\n\n"
 "SECOND BY SECOND (something visible moves in EVERY second):\n"
 "0.0 to 1.0 s: she takes a small breath, her eyebrows rise slightly and her eyes stay on the lens; the amethyst stays steady beside her face.\n"
 "1.0 to 2.5 s: her right hand rises from below the bottom edge, up the LEFT side of the frame, to chin height, with the index finger extended and the other fingers curled.\n"
 "2.5 to 4.5 s: the tip of her right index finger comes to rest vertically against her lips, centered on her mouth, and she holds it there with her eyes firm on the lens, with one slow blink at about 3.5 s.\n"
 "4.5 to 6.0 s: she lowers the finger away from her lips and the hand drops down the left side of the frame and out of frame below the bottom edge.\n"
 "6.0 to 8.0 s: both hands are back in the first-frame positions; she gives a tiny knowing smile with her lips closed and holds still; exactly as in the last supplied frame.\n\n"
 "WHAT MUST NOT HAPPEN: she does not speak or mouth any words (her lips only press against the finger and stay closed); the amethyst never changes hands, never turns away, never drops and never "
 "covers her face; the finger touches only her lips, not her nose or chin; no other hand sign appears; each hand has exactly five fingers; the white cabinet, the black coffee machine, the dark window, "
 "the hanging lamp and the granite counter never move; no object appears or disappears.\n\n"
 "VISUAL: she is the same woman as in the supplied frames; realistic natural physics, no morphing, no glow, no magic effects. No text, no logos.\n\n"
 "AUDIO: real quiet kitchen room sound only. No music, no voice, no added sound effects.")
assert not risco.findall(e['prompt']),risco.findall(e['prompt'])
st=d['story']
st['textos']=[{"posicao":"Uma frase só, no centro, uma cor (creme #F1E6D3), 1 a 2 linhas","texto":"Tap below and take the free love quiz."}]
st['adesivos']=["Take the free quiz","Open Part 2"]
st['nota']="Use a mesma imagem do story que você já tem (a do pingente de cobre). Poste o story antes do vídeo."
save('PAINEL-NORA33.html',s,m,d)
print('nora33 ok')

# ---------- nora31: A a D na versão curta ----------
s,m,d=load('PAINEL-NORA31.html')
et=d['pre_gancho']['etapas']
MAOS=("Both hands have five fingers, short nails with pale pink polish and one small gold ring on the index finger; the hand on the right side of the image wears three thin gold bracelets. "
      "Long dark emerald-green knit sleeves end at the wrists, at the bottom edge of the frame.")
COZ=("Background: a home kitchen at night, softly out of focus, with a white cabinet at the upper left, a dark window at the upper right and the warm yellow glow of a hanging lamp.")
et[0]['prompt']=("Vertical 9:16 close-up photo, photorealistic, taken with a smartphone. Two hands hold a small sealed white paper wrapper of an adhesive strip bandage horizontally in the center of the frame, "
 "about 20 cm from the lens. The wrapper is about 9 cm long and 3 cm wide, plain white with a thin red stripe along its top edge, closed, with no text and no logo. The hand on the right side of the image "
 "holds the right end of the wrapper between thumb and index finger. The hand on the left side of the image pinches a small red pull tab at the left end, ready to open it. "+MAOS+" "+COZ+
 " Sharp focus on the wrapper and the fingertips. Only the hands, the sleeves, the wrapper and the blurred kitchen are visible. No text, no logo, no watermark.")
et[3]['prompt']=("Vertical 9:16 close-up photo, photorealistic, taken with a smartphone, like a casual clothing product photo. The hand on the right side of the image holds up one small red satin brief with lace trim "
 "by its right top corner, so it hangs open and flat in the center of the frame, about 22 cm from the lens, with its smooth bright-red satin front panel (about 12 cm wide and 14 cm tall) facing the lens and "
 "scalloped red lace trim along its top edge and its curved lower edges; it is plain and intact, with nothing printed on it and nothing attached to it yet. The hand on the left side of the image holds one "
 "beige adhesive bandage about 7.5 cm long by its center between thumb and index finger, vertically, about 6 cm in front of the center of the satin panel, its white backing tabs already peeled off, not "
 "touching the satin yet, with no text on it. "+MAOS+" "+COZ+" Sharp focus on the satin panel, the bandage and the fingertips. Only the hands, the sleeves, the red garment, the bandage and the blurred kitchen "
 "are visible. No text, no logo, no watermark.")
t=et[1]['prompt']
t=rep(t,'her LEFT hand (on the RIGHT side of the image) holds the open, empty wrapper','the hand on the right side of the image holds the open, empty wrapper')
t=rep(t,'her RIGHT hand (on the LEFT side of the image) has pulled','the hand on the left side of the image has pulled')
t=rep(t,'and stays in her left hand.','and stays in that hand.')
et[1]['prompt']=t
t=et[4]['prompt']
t=rep(t,'held by its right top corner in her left hand (on the RIGHT side of the image)','held by its right top corner by the hand on the right side of the image')
t=rep(t,'the tip of her right index finger (on the LEFT side of the image) rests on the bandage and presses it; the right thumb is out of sight behind the satin',
        'the index fingertip of the hand on the left side of the image rests on the bandage and presses it; its thumb is out of sight behind the satin')
et[4]['prompt']=t
for i in (0,1,3,4):
    p=et[i]['prompt']; assert not risco.findall(p),(i,risco.findall(p)); assert not re.search(r'\b(woman|her)\b',p,re.I),(i,re.findall(r'\b(woman|her)\b',p,re.I))
save('PAINEL-NORA31.html',s,m,d)
print('nora31 ok')
