import sys
reps=[
("$('agente').querySelector('p').textContent='Uma imagem e uma mensagem: anexe a imagem e cole o bloco “COPIAR TUDO JUNTO” da Central, que já traz as orientações ao agente (o seu aviso é opcional).';",
 "$('agente').querySelector('p').textContent=ag.intro||'Uma imagem e uma mensagem: anexe a imagem e cole o bloco “COPIAR TUDO JUNTO” da Central, que já traz as orientações ao agente (o seu aviso é opcional).';"),
("<span class=\"tag\">opcional: o prompt da Central já traz as orientações ao agente</span>",
 "<span class=\"tag\">'+esc(ag.aviso_tag||'opcional: o prompt da Central já traz as orientações ao agente')+'</span>"),
("$('todos').classList.toggle('hide',!!pk.imagem_reutilizada||!!pk.imagem_central);",
 "$('todos').classList.toggle('hide',!!pk.imagem_reutilizada||!!pk.imagem_central||!!pk.ocultar_bloco_agente_imagem);"),
("$('storyBox').innerHTML='<div class=\"item\"><button class=\"cp\" id=\"cpStImg\">",
 "$('storyBox').innerHTML=(st.nota?'<div class=\"tip\" style=\"margin-bottom:10px\">'+esc(st.nota)+'</div>':'')+'<div class=\"item\"><button class=\"cp\" id=\"cpStImg\">"),
]
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    for a,b in reps:
        assert s.count(a)==1,(f,a[:60],s.count(a))
        s=s.replace(a,b)
    open(f,'w',encoding='utf-8').write(s)
    print('ok',f)
