# 29/10/2026: cada número fixo com cor e tamanho próprios (mapa_tela.numeros[].cor, .cor_nome, .tamanho), pedido do aluno.
import sys
f = (sys.argv[1] if len(sys.argv) > 1 else '.') + '/PAINEL-MODELO.html'
s = open(f, encoding='utf-8').read()
R = [
 ("font-size=\"4\" font-weight=\"700\" text-anchor=\"middle\" fill=\"#FFD21F\" stroke=\"#000\" stroke-width=\".35\" paint-order=\"stroke\">'+esc(u.t)+'</text>'",
  "font-size=\"'+(4*(u.tamanho||12)/12)+'\" font-weight=\"700\" text-anchor=\"middle\" fill=\"'+(u.cor||'#FFD21F')+'\" stroke=\"#000\" stroke-width=\".35\" paint-order=\"stroke\">'+esc(u.t)+'</text>'"),
 ("    NU.forEach(u=>{rows+=lin('#FFD21F','Número fixo '+u.t+(u.onde?' ('+u.onde+')':''),'centro em '+u.x+'% da largura e '+u.y+'% da altura')});",
  "    NU.forEach(u=>{rows+=lin(u.cor||'#FFD21F','Número fixo '+u.t+(u.onde?' ('+u.onde+')':''),(u.cor_nome?esc(u.cor_nome)+' '+esc(u.cor||'')+', tamanho '+(u.tamanho||12)+'. ':'')+'Centro em '+u.x+'% da largura e '+u.y+'% da altura')});"),
 ("...(NU.length?NU.map(u=>['Número fixo '+u.t+(u.onde?' ('+u.onde+')':''),u.x,u.y])",
  "...(NU.length?NU.map(u=>['Número fixo '+u.t+(u.cor_nome?', '+u.cor_nome+', tamanho '+(u.tamanho||12):'')+(u.onde?' ('+u.onde+')':''),u.x,u.y])"),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(f, 'w', encoding='utf-8').write(s)
print('modelo ok')
