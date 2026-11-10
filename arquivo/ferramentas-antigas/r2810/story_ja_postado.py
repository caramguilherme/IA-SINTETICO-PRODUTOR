# 28/10: story.ja_postado = true mostra só o aviso (sem prompt, texto e adesivo), para os vídeos que usam o story já no ar.
import json,re,sys
OLD="  if(pk.story){\n    const st=pk.story;\n    $('storyBox').innerHTML="
NEW="  if(pk.story&&pk.story.ja_postado){\n    $('storyBox').innerHTML='<div class=\"tip\" style=\"font-size:15px\">'+esc(pk.story.nota||'')+'</div>';\n  }else if(pk.story){\n    const st=pk.story;\n    $('storyBox').innerHTML="
NOTA="✅ NÃO FAÇA STORY NESTE VÍDEO. O story das 3 cartas postado em 28/10 às 16h32 (Insta e Face) já está no ar e vale para este vídeo. Ele expira ~16h30 de 29/10."
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    if 'pk.story.ja_postado' not in s:
        assert s.count(OLD)==1,f; s=s.replace(OLD,NEW)
    if f!='PAINEL-MODELO.html':
        m=re.search(r'const PACOTE = (\{.*?\});\n',s,re.S); p=json.loads(m.group(1))
        p['story']['ja_postado']=True; p['story']['nota']=NOTA
        s=s[:m.start(1)]+json.dumps(p,ensure_ascii=False)+s[m.end(1):]
    open(f,'w',encoding='utf-8').write(s); print(f,'ok')
