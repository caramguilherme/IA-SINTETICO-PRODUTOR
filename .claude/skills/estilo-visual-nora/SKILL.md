---
name: estilo-visual-nora
description: Use toda vez que for pôr texto num vídeo ou imagem da Nora (edição P45 do noraNN-final, versão -FACE, slideshow, POV, capa, story): desde 15/11/2026 os Reels e o -FACE usam um padrão único de alto contraste (o modelo do Clone do Gustavo, R50), igual em todo post; o story mantém o estilo creme aprovado em 11/11.
---

# Estilo visual da Nora: padrão único de alto contraste (desde 15/11/2026)

**Decisão do aluno, 15/11/2026 ~03h50:** "pode reeditar o nora65 sim. Vamos confiar no que o clone falou, e usar as edições e os modelos que ele falou. Inclusive, salva esse novo modelo de edição nas skills de edição, pra fazermos exatamente do jeito que o clone falou nas respostas."

**De onde veio:**
- **Clone do Gustavo, R50** (`CLONE-DO-GUSTAVO-RESPOSTAS.md`):
  - a fase 3 (de 12 a 14/11) derrubou a retenção: caixas pastel e translúcidas, fonte serifada fina em itálico, caixa do topo e legenda disputando o 0 s;
  - "no tráfego orgânico direto, contraste absoluto vence harmonia";
  - o público é de mulheres de 35 a 55+ nos EUA, com o brilho da tela baixo e rolando rápido;
  - "se ela não consegue ler instantaneamente… ela passa o vídeo".
- **A aula 43 do Gustavo** (`TRANSCRICOES/2026-08-31-aula-43-funil-prosperidade-e-hooks.md`, 1:03:22 a 1:08:59): "legendinha simples… mais orgânico possível", fonte básica "com um contorninho", "no máximo duas linhas", destaque "amarelinho".
- **Os 3 campeões** (nora48 a nora50: 68% a 71% nos 3 s, 18 a 21 s de tempo médio) usavam este estilo.

**O que mudou em 15/11:** o pedido de 12/11 ("variar cores e estilos pela cena") foi substituído pelo padrão abaixo, por decisão do aluno.

## O padrão (Reels do Insta e versão -FACE): `"estilo": "alto-contraste"` no spec
| Camada | Como fica | No spec |
|---|---|---|
| **Caixa do topo** (0 s até o fim do Take 1 ou do pré-gancho) | **amarela sólida, letras pretas Poppins Bold**, sem sombra; 2 linhas curtas em maiúsculas; o trecho entre [colchetes] também preto; tamanho 10 a 11 | `"caixa": TOPO_AMARELO` (de `estilos_video.py`) no item da caixa do topo |
| **Legenda** | 3 palavras por vez, no terço de baixo (`y` −310), Poppins Bold **branca com contorno preto grosso** (5 px), **palavras-chave em amarelo forte** (#FFD21F); no máximo 2 linhas | o estilo já faz; `destaques` com as palavras-chave |
| **Números fixos** | **desde 16/11 (escolha do aluno, 13h31): dois números, os dois brancos com contorno preto: o 11:11 no canto de cima à direita e o 222 no canto de cima à esquerda, na mesma altura, o vídeo todo, entre 8% e 92% da largura**; o 888 saiu ("os 3 coloridos não ficam sérios") | dois `texto`, `"cor": "#FFFFFF"` (11:11 em X 230, Y 282; 222 em X −230, Y 282) |
| **Faixa do story / do comentário (CTA)** | **caixa branca sólida, texto preto em negrito, o destaque em vermelho** (#E53935) ("Tap my photo: / your 2027 reading is in [my story]"; Face: "Your 2027 reading: / [link in the comments]"); tamanho 10 | o estilo já faz |
| **Seta** (Insta) | vermelha com contorno preto, apontando para a foto do perfil | o estilo já faz |

## Regras do modelo (Clone R50, ao pé da letra)
1. **Quando a legenda entra:**
   - **com pré-gancho visual (0 a ~4,8 s; Clone R51):** no pré-gancho, só a caixa do topo, para a pessoa olhar a ação. A legenda entra no quadro exato em que a Nora começa a falar o Take 1;
   - **sem pré-gancho (a Nora falando desde o 0 s):** a legenda pode começar no 0 s, com a caixa do topo curta (2 linhas) e longe da legenda (topo × terço de baixo).
2. **Tela limpa até o CTA:** nada de print do Trustpilot nem de caixa "Rated 4.8" no meio do vídeo. Até o CTA, só a Nora, a caixa do topo (no começo), os números e a legenda.
3. **Imagens do desejo da edição dopaminérgica** (aprovada em 15/11, aulas 12 e 14): são ilustração, não texto. Entram em tela cheia ou dividida nos primeiros ~15 s, uma por frase. A legenda continua por cima, com o contorno.
4. **Nada de pastel, translúcido, serifa fina, itálico nem cor tirada da cena.** Não variar o estilo de um post para o outro: o padrão é o mesmo em todo Reels e todo -FACE.
5. **O script não muda nada para o algoritmo:** "o Instagram não tem acesso a como você gerou o MP4". Exportar 1080x1920, 24 fps, ~4 Mbps (crf 21), como sempre.
6. **Conferir antes do render** com `previa_edicao.py`: a caixa e os números entre 8% e 92% da largura (P43), nada encostando em rosto, mão ou na carta.

## Story, slideshow, POV e capa
- **O story** segue o estilo aprovado pelo aluno em 11/11 (caixa creme com as cores da foto, marrom e itálico terracota; skill `story-nora`). O Clone não falou do story; mudar só se o aluno pedir.
- **Slideshow e POV no Face:** usam o mesmo padrão de alto contraste dos Reels: caixa sólida, legenda branca com contorno e destaque amarelo.

## Os estilos antigos
Os outros estilos de `estilos_video.py` ficam no script só para reproduzir os vídeos antigos: `creme-terracota` (o do story), `nevoa-taupe`, `noite-dourado`, `salvia-creme`, `lavanda-ameixa`, `areia-rose`, `limpo-branco` e `branco-classico` (igual ao alto-contraste, com contorno de 4 px). **Não usar em Reels novo.**

## Registrar
O estilo usado (`alto-contraste`) vai na linha do vídeo na `BIBLIOTECA-DE-TAKES.md` e no `obs` do `METRICAS-NORA.csv`, para comparar a retenção dos 3 s com o nora59 a nora64 (fase 3).
