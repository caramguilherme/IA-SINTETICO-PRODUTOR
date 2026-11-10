# 29/10/2026: números fixos espalhados pelo quadro, com posição própria em cada vídeo (pedido do aluno).
# O PAINEL-MODELO.html passa a aceitar mapa_tela.numeros = [{"t":"222","x":9,"y":62,"onde":"embaixo à esquerda"}, ...]
# (x e y em % da largura e da altura): desenha cada número no mapa, lista na legenda do mapa e põe o X/Y de cada um
# na tabela do CapCut no lugar das duas linhas fixas (esquerda e direita).
import sys
f = (sys.argv[1] if len(sys.argv) > 1 else '.') + '/PAINEL-MODELO.html'
s = open(f, encoding='utf-8').read()
R = [
 ("      {n:'Rodapé do app (nome, descrição, botão)',y:mt.rodape_app,x:[0,100],c:'#ff6b5b',t:'#ffd0ca'}];\n",
  "      {n:'Rodapé do app (nome, descrição, botão)',y:mt.rodape_app,x:[0,100],c:'#ff6b5b',t:'#ffd0ca'}].filter(z=>!(mt.numeros&&z.y===mt.codigos));\n    const NU=mt.numeros||[];\n"),
 ("    sv+='<text x=\"'+(W*.46)+'\" y=\"'+(H*(mt.legenda[0]+mt.legenda[1])/200+1)+'\" font-size=\"3.8\" font-weight=\"700\" text-anchor=\"middle\" fill=\"#fff\">'+esc(mt.legenda_curto||'LEGENDA')+'</text></svg>';",
  "    sv+='<text x=\"'+(W*.46)+'\" y=\"'+(H*(mt.legenda[0]+mt.legenda[1])/200+1)+'\" font-size=\"3.8\" font-weight=\"700\" text-anchor=\"middle\" fill=\"#fff\">'+esc(mt.legenda_curto||'LEGENDA')+'</text>';\n    NU.forEach(u=>{sv+='<text x=\"'+(W*u.x/100)+'\" y=\"'+(H*u.y/100+1.4)+'\" font-size=\"4\" font-weight=\"700\" text-anchor=\"middle\" fill=\"#FFD21F\" stroke=\"#000\" stroke-width=\".35\" paint-order=\"stroke\">'+esc(u.t)+'</text>'});\n    sv+='</svg>';"),
 ("    rows+=lin('#ff6b5b','Botões do lado direito (curtir, comentar, enviar)',",
  "    NU.forEach(u=>{rows+=lin('#FFD21F','Número fixo '+u.t+(u.onde?' ('+u.onde+')':''),'centro em '+u.x+'% da largura e '+u.y+'% da altura')});\n    rows+=lin('#ff6b5b','Botões do lado direito (curtir, comentar, enviar)',"),
 ("    const ys=(a)=>(a[0]+a[1])/2,P=[\n      ['Número fixo da esquerda (222 ou 444)',12,ys(mt.codigos)],\n      ['Número fixo da direita (11:11)',88,ys(mt.codigos)],\n",
  "    const ys=(a)=>(a[0]+a[1])/2,P=[\n      ...(NU.length?NU.map(u=>['Número fixo '+u.t+(u.onde?' ('+u.onde+')':''),u.x,u.y]):[['Número fixo da esquerda (222 ou 444)',12,ys(mt.codigos)],['Número fixo da direita (11:11)',88,ys(mt.codigos)]]),\n"),
]
for a, b in R:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
open(f, 'w', encoding='utf-8').write(s)
print('modelo ok')
