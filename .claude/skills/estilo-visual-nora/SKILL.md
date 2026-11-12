---
name: estilo-visual-nora
description: Use toda vez que for pôr texto num vídeo ou imagem da Nora (edição P45 do noraNN-final, versão -FACE, slideshow, POV, story, capa): escolher cores e fontes que combinam com a cena, a roupa e o fundo daquele vídeo, variando de um post para o outro, em vez de repetir a caixa branca com preto e vermelho.
---

# Estilo visual da Nora (pedido do aluno, 12/11/2026)

"A caixa branca com preto e vermelho não é pra ser fixa. Temos que variar, mudar, testar, deixar a edição mais bonita, com cores e estilos que ornam com o cenário, a roupa, o fundo do vídeo. Essa skill que eu quero de você." O estilo do story de 11/11 (caixa creme, marrom e itálico terracota; "agora sim, ficou top") é o ponto de partida do bom gosto: tons tirados da própria imagem, uma fonte limpa para o texto e uma serifada em itálico para o trecho que importa.

## Passo a passo (antes de montar a spec ou desenhar o texto)
1. **Tirar um quadro** do Take 1 (ou da imagem da cena) e um do pré-gancho: `ffmpeg -ss T -i video -frames:v 1 q.jpg`.
2. **Ver a paleta e os estilos que combinam:** `python3 -I ferramentas-painel/ferramentas/estilos_video.py q.jpg --ultimo <estilo do post anterior na mesma rede>`. Ele imprime a paleta do quadro, os 3 estilos que mais combinam (com o contraste do texto) e um estilo "sob-medida" tirado da paleta.
3. **Ver lado a lado antes de decidir:** `python3 -I ferramentas-painel/ferramentas/estilos_video.py --amostra q.jpg amostra.jpg ESTILO1 ESTILO2 ESTILO3` e olhar a folha (pode passar o sob-medida como JSON).
4. **Escolher com critério, dizer o porquê em 1 linha:**
   - **Combina:** a caixa no tom claro da cena (parede, roupa clara), o texto no tom escuro dela, o destaque na cor mais viva dela (madeira, planta, abajur, céu).
   - **Lê no celular:** contraste do texto na caixa de 4,5:1 ou mais; a legenda sempre com contorno escuro; conferir no quadro reduzido.
   - **Varia:** nunca o mesmo estilo em 2 posts seguidos na mesma rede (Insta e Face contam separado); na mesma cena, alternar entre os 2 ou 3 que combinam.
   - **Uma variável por vez quando houver teste:** se o teste do dia for de copy ou de corpo, o estilo pode variar (é parte da variação natural); se o teste for do visual, mudar só o estilo e manter o resto.
5. **Usar:** no spec do `editar_video.py`, `"estilo": "<nome>"` (ou o dict sob-medida) no topo; nas linhas da caixa, o trecho de destaque entre [colchetes] (a data, "2027 reading", "my story"); sem a chave "cores" (ela força o visual antigo). Números: a cor de cada um pode seguir o destaque e o tom claro do estilo, com o contorno do estilo. Slideshow, POV e story: as mesmas cores e fontes (`fazer_slideshow.py`, `texto_story.py`).
6. **Registrar o estilo usado** na linha do vídeo na `BIBLIOTECA-DE-TAKES.md` e no campo `obs` do `METRICAS-NORA.csv` ("estilo: nevoa-taupe"), para cruzar com a retenção e os cliques depois.

## Os estilos que existem (`ferramentas-painel/ferramentas/estilos_video.py`)
| Nome | Quando | Caixa · texto · destaque |
|---|---|---|
| `creme-terracota` | cenas quentes, madeira, bege, luz dourada (o story de 11/11, o slideshow de 12/11) | creme · marrom · itálico terracota |
| `nevoa-taupe` | cinza, preto, parede clara (o escritório da `manha1111-IMG`) | gelo · grafite · itálico taupe |
| `noite-dourado` | noite com abajur, fundo escuro | marrom-escuro translúcido · creme · itálico dourado |
| `salvia-creme` | plantas, roupa verde (a cena verde do kit) | creme esverdeado · verde-escuro · itálico sálvia |
| `lavanda-ameixa` | céu ao entardecer, roxos, cristais, POV de amor | lavanda clara · ameixa · itálico violeta |
| `areia-rose` | pele quente, rosa, pôr do sol | areia · marrom · itálico rosa queimado |
| `limpo-branco` | o "visual limpo" (sem caixa; letra branca com sombra) | — · branco · itálico dourado claro |
| `branco-classico` | o visual antigo, só como uma opção entre as outras | branco · preto · vermelho |
Estilo novo que funcionar entra na tabela e no `ESTILOS` do script, com a paleta de referência no `REF`.

## Não fazer
- Não voltar à caixa branca com preto e vermelho por padrão.
- Não usar cor que some no fundo (contraste baixo) nem mais de 2 fontes no mesmo vídeo.
- Não pôr efeito animado nem mudar o estilo no meio do vídeo.
