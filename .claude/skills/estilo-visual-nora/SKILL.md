---
name: estilo-visual-nora
description: Use toda vez que for pôr texto num vídeo ou imagem da Nora (edição P45 do noraNN-final, versão -FACE, slideshow, POV, capa, story): desde 18/11/2026 23h30 os Reels e o -FACE usam o padrão "simples" (caixa do topo branca com preto e a palavra-chave em vermelho só no gancho, legenda simples como a do nora69, os 2 números brancos), igual em todo post; o story usa o texto nativo do Instagram.
---

# Estilo visual da Nora: padrão "simples" (desde 18/11/2026 23h30)

**Decisão do aluno, 18/11/2026 23h30** (depois da Clone R75): "concordo com a legenda mais simples tb… a caixa branca com letra preta, em destaque a letra vermelha, nos primeiros segundos (gancho, headline)". Antes, no ini1811: "nao achei que o amarelo ficou bom, parece muito poluido".

**De onde veio (conferido nas transcrições):**
- **Aula 43 do Gustavo** (`TRANSCRICOES/2026-08-31-aula-43-funil-prosperidade-e-hooks.md`): a legenda, 1:03:22 a 1:05:12 ("legendinha simples… legenda mais que impossível os velhinhos lerem pra ficar um negócio orgânico, padrãozinho… vou botar um contorninho… no máximo duas linhas"); a headline, 1:11:52 a 1:12:46 ("acima da cabeça mesmo, no topo do vídeo… isso é muito pessoal… amarela não, vou botar a branca com vermelho").
- **Aula 19** (0:59:00): "você deixa só para a legenda começar… quando a redline sai" (a headline sai da tela); 1:12:14: "Tá muita informação na tela".
- **Aula 57** (0:33:41 a 0:34:00): legenda "clássica… bem simples… fundinho sólido não… contorno mais fininho"; 0:34:29 a 0:34:50: a headline só no gancho é uma opção do editor; 0:37:34: os números nos cantos, "isso é pessoal".
- **Clone R73 e R75:** a caixa amarela e a legenda de alto contraste da R50 foram opinião dele; nenhuma aula liga a cor da caixa ou o estilo da legenda à retenção ou ao clique.

## O padrão (Reels do Insta e versão -FACE)
| Camada | Como fica |
|---|---|
| **Caixa do topo** | **só no gancho** (0 s até o fim da 1ª frase, 3 a 5 s); **branca sólida, letra preta em negrito (Poppins Bold), a palavra-chave entre [colchetes] em vermelho** (#E53935); 2 linhas curtas no máximo, acima da cabeça; depois some |
| **Legenda** | **simples, como a do nora69** (`ferramentas-painel/dia-1711/editar_nora69_limpo.py`): Inter, branca, contorno fino escuro e sombra suave; **sem destaque colorido e sem caixa alta**; pedaços da fala de até ~6 palavras, quebrando na pontuação; no máximo 2 linhas; no terço de baixo; entra na 1ª palavra |
| **Números fixos** | dois, os dois brancos com contorno preto: o 11:11 no canto de cima à direita e o 222 no de cima à esquerda, na mesma altura, o vídeo todo, entre 8% e 92% da largura (11:11 em X 230, Y 282; 222 em X −230, Y 282) |
| **Faixa do story / do comentário (CTA)** | caixa branca sólida, texto preto em negrito, o destaque em vermelho ("Tap my photo: / your 2027 reading is in [my story]"; Face: "Your 2027 reading: / [link in the comments]") |
| **Seta** (Insta) | vermelha com contorno preto, embaixo à esquerda, logo acima da foto do perfil do Reels: X −300, Y −400 (≈81% da altura; regra do aluno de 18/11 19h20) |

## Regras
1. **A caixa do topo não fica o vídeo todo:** some no fim do gancho. Nada de caixa amarela.
2. **Tela limpa até o CTA:** nada de print do Trustpilot nem de "Rated 4.8" no meio. Até o CTA, só a Nora, a caixa (no gancho), os números e a legenda.
3. **Imagens do desejo** (edição dopaminérgica, aulas 12 e 14) são ilustração, não texto: a legenda continua por cima.
4. **Nada de pastel, translúcido, serifa fina, itálico nem cor tirada da cena.** O padrão é o mesmo em todo Reels e todo -FACE.
5. **O script não muda nada para o algoritmo.** Exportar 1080x1920, 24 fps, ~4 Mbps (crf 21).
6. **Conferir antes do render** com `previa_edicao.py`: a caixa e os números entre 8% e 92% da largura (P43), nada encostando em rosto, mão ou na carta.
7. **No editor:** até o preset "simples" entrar no `editar_video.py`, a legenda simples sai do mesmo jeito do `editar_nora69_limpo.py` (Inter, pedaços de até ~6 palavras, contorno 2 com alfa baixo e sombra desfocada); a caixa usa o fundo branco do `BASE` de `estilos_video.py` (sem o `TOPO_AMARELO`), com `ini` 0 e `fim` no fim da 1ª frase.

## Story, slideshow, POV e capa
- **O story** usa o texto nativo do Instagram desde 18/11 (`texto_story_nativo.py`; skill `story-nora`).
- **Slideshow e POV no Face:** o mesmo padrão dos Reels.

## Os estilos antigos
O alto contraste de 15/11 (`alto-contraste` + `TOPO_AMARELO`) e os outros estilos de `estilos_video.py` (`creme-terracota`, `nevoa-taupe`, `noite-dourado`, `salvia-creme`, `lavanda-ameixa`, `areia-rose`, `limpo-branco`, `branco-classico`) ficam só para reproduzir os vídeos antigos. **Não usar em Reels novo.**

## Registrar
O estilo usado ("simples") vai na linha do vídeo na `BIBLIOTECA-DE-TAKES.md` e no `obs` do `METRICAS-NORA.csv`, para comparar os 3 s e a curva aos 10 s com os vídeos de alto contraste (15 a 18/11).
