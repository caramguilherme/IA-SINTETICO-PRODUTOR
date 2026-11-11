---
name: story-nora
description: Use quando o Guilherme mandar a foto do story da Nora (as 4 opções para escolher ou a escolhida em 2K) ou pedir o texto do story na imagem: escolher a foto, pôr o texto no estilo aprovado (caixa creme com as cores da foto) e devolver pronta para ele só colocar o adesivo de link.
---

# Story da Nora: foto + texto (estilo aprovado em 11/11/2026: "agora sim, ficou top")

O story leva quem vem do vídeo ao link (STORYIG no Insta, FACE no Face). A foto é a Nora no dia a dia (Clone R2), sem cartas; o texto é curto; o aluno põe só o adesivo de link, no próprio app.

## Passo a passo
1. **Texto e adesivo do dia:** do painel do vídeo que tem a seção Story (campo `story.textos` e `story.adesivos`) ou da decisão mais recente no `CLAUDE.md` (seção 1). O nome do funil vai entre [colchetes] para sair em destaque ("your [private reading]", "see what [2027] holds for you").
2. **Escolher entre as 4 opções** (quando ele mandar a grade): é a Nora (lua com 3 estrelinhas no lado esquerdo da imagem, trança com anéis, brincos de estrela e lua, colar de Vênus); olha para a lente; nada de cartas; **sobra espaço acima da cabeça** para o texto (a cabeça abaixo de ~14% da altura) e embaixo para o adesivo. Dizer uma escolha só e o motivo em 1 linha.
3. **Pôr o texto na foto em 2K que ele mandar** (salvar a foto em `ferramentas-painel/<pasta do dia>/story-DDMM.jpg`):
   `python3 -I ferramentas-painel/ferramentas/texto_story.py foto.jpg saida.jpg --linha "Tap below: your [private reading]" --linha "is waiting for you on 11:11."`
   Estilo fixo: caixa creme quase opaca (#F6EEE4, o tom claro da foto), cantos bem arredondados, sombra marrom suave; texto marrom-escuro #5A3A2A em Poppins Medium; o trecho entre colchetes em Cormorant SemiBold Itálico terracota #A0583A. Em foto de outra paleta, `--cores auto` puxa a caixa para o tom claro da própria foto. `--topo` (padrão 0,07) sobe ou desce a caixa; `--tamanho` (padrão 0,044) muda a letra.
4. **Conferir ANTES de mandar** (cobrança do aluno de 11/11: "é pra você ser certeiro, e não ficar refazendo"): abrir o `-recorte.jpg` (tamanho real) e o `-celular.jpg` (tela de celular). A caixa fica entre 8% e 92% da largura (o script recusa se passar), não toca o rosto (pode encostar no alto do cabelo) e o texto se lê inteiro em cima de qualquer fundo (janela, planta, luz). Só mandar quando estiver certo; uma versão só.
5. **Entregar:** `SendUserFile` com a imagem (display attach) e, em 2 a 3 linhas: o texto do adesivo de link, onde ele vai (embaixo, no centro, sobre a roupa ou o chão), STORYIG no Insta e FACE no Face, e quando postar (junto com o vídeo do painel, antes de o story anterior vencer, 24 h).
6. **Registrar:** a escolha e o arquivo em `BIBLIOTECA-DE-TAKES.md`; quando ele disser que postou, a hora em `FATOS-DO-ALUNO.md` e a seção 1 do `CLAUDE.md` (vence 24 h depois); commit e push.

## Não fazer
- Não trocar o estilo por conta própria (caixa branca com vermelho é o estilo dos vídeos; preto sem caixa ficou ruim de ler sobre a janela em 11/11).
- Não pôr link, preço, nome do app, "free" ou cartas no texto.
- Se o aluno perguntar "por quê", só responder: não refazer sem ele pedir.
