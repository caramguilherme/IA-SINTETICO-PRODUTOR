# 28/10: aviso de localização na seção "Legenda Insta/Face" (campo opcional roteiro.legenda_aviso).
import json,re,sys
H_OLD='<div class="box" id="insta"></div>'
H_NEW='<div class="box" id="insta"></div>\n      <div class="tip hide" id="instaAviso" style="margin-top:10px;font-size:15px"></div>'
J_OLD="$('insta').textContent=r.descricao_instagram||'(a IA não entregou a legenda)';"
J_NEW=J_OLD+"\n  {const av=$('instaAviso');if(r.legenda_aviso){av.textContent=r.legenda_aviso;av.classList.remove('hide')}else av.classList.add('hide');}"
AVISO="📍 LOCALIZAÇÃO (só no Insta): antes de publicar, toque em “Adicionar localização” e escolha Los Angeles, California. No Face, sem localização."
def molde(s):
    if 'id="instaAviso"' in s: return s
    assert s.count(H_OLD)==1 and s.count(J_OLD)==1
    return s.replace(H_OLD,H_NEW).replace(J_OLD,J_NEW)
for f in sys.argv[1:]:
    s=molde(open(f,encoding='utf-8').read())
    if f!='PAINEL-MODELO.html':
        m=re.search(r'const PACOTE = (\{.*?\});\n',s,re.S); p=json.loads(m.group(1))
        p['roteiro']['legenda_aviso']=AVISO
        s=s[:m.start(1)]+json.dumps(p,ensure_ascii=False)+s[m.end(1):]
    open(f,'w',encoding='utf-8').write(s); print(f,'ok')
