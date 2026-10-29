# 29/10/2026 (pedido do aluno): todo painel termina com "Respostas no Face": a resposta ao comentário e a mensagem
# no direct (Messenger) com o link do Face, para copiar e colar. Só no Face: no Insta o direct pediu verificação facial.
# Padrão no modelo (RESP_FACE); o pacote pode trocar com pk.respostas_face {aviso, comentario[], dm[], link}.
import sys
f = (sys.argv[1] if len(sys.argv) > 1 else '.') + '/PAINEL-MODELO.html'
s = open(f, encoding='utf-8').read()
SEC = '''    <section class="card" id="respostasface">
      <h2>Respostas no Face (comentário e direct)</h2>
      <div class="tip" id="rfAviso" style="margin-bottom:10px;font-size:15px"></div>
      <div id="rfBox"></div>
    </section>

    <section class="card hide" id="pecas">'''
JS = '''const RESP_FACE={
  aviso:'Só no Face (no Insta o direct pediu verificação facial). Para cada pessoa que comentar: responda o comentário com uma frase (sem link) e mande a mensagem com o link no direct. Vá alternando as versões: não mande o mesmo texto para todo mundo.',
  link:'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks',
  comentario:['✨ Just sent you a DM, beautiful! 💖🔮','💖 Check your messages, beautiful! ✨🔮','🔮 Sent you something in your DM, beautiful! ✨'],
  dm:['✨ Your reading is waiting for you, beautiful! 🔮💖 Tap here to discover the message meant for you:','✨ Your 3 cards are ready, beautiful! 🔮💖 Tap here, pick them and see what\\'s coming for you:','💖 Your message is here, beautiful! ✨🔮 Tap below, pick your 3 cards and see what\\'s coming for you:']};
function montarRespFace(){
  const r=Object.assign({},RESP_FACE,(pk&&pk.respostas_face)||{});
  $('rfAviso').textContent=r.aviso;
  const it=(tit,txt,i,pre)=>'<div class="item"><button class="cp" id="'+pre+i+'">Copiar</button><h3>'+esc(tit)+'</h3><div class="box">'+esc(txt)+'</div></div>';
  const dmTxt=d=>d+'\\n\\n'+r.link;
  $('rfBox').innerHTML='<div class="mono">Resposta no comentário (sem link)</div>'+r.comentario.map((c,i)=>it('Versão '+(i+1),c,i,'rfC')).join('')
    +'<div class="mono" style="margin-top:14px">Mensagem no direct (com o link do Face)</div>'+r.dm.map((d,i)=>it('Versão '+(i+1),dmTxt(d),i,'rfD')).join('');
  r.comentario.forEach((c,i)=>{$('rfC'+i).onclick=e=>copiar(c,e.currentTarget)});
  r.dm.forEach((d,i)=>{$('rfD'+i).onclick=e=>copiar(dmTxt(d),e.currentTarget)});
}

/* ORDEM DE PRODUÇÃO:'''
R = [
 ('    <section class="card hide" id="pecas">', SEC),
 ("'textotela','fala','descricao','comentario']\n    :['pecas'", "'textotela','fala','descricao','comentario','respostasface']\n    :['pecas'"),
 ("'story','textotela','fala','descricao','comentario'];\n  const pn", "'story','textotela','fala','descricao','comentario','respostasface'];\n  const pn"),
 ('/* ORDEM DE PRODUÇÃO:', JS),
 ("  ordenar();\n  $('painel').classList.remove('hide');", "  montarRespFace();\n  ordenar();\n  $('painel').classList.remove('hide');"),
]
for a, b in R:
    assert s.count(a) == 1, (a[:60], s.count(a))
    s = s.replace(a, b)
open(f, 'w', encoding='utf-8').write(s)
print('modelo ok')
