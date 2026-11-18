---
name: story-nora
description: Use quando o Guilherme mandar a foto do story da Nora (as 4 opções para escolher ou a escolhida em 2K) ou pedir o texto do story na imagem: escolher a foto, pôr o texto no estilo aprovado (caixa creme com as cores da foto) e devolver pronta para ele só colocar o adesivo de link.
---

# Story da Nora: foto + texto (estilo aprovado em 11/11/2026: "agora sim, ficou top")

O story leva quem vem do vídeo ao link (STORYIG no Insta, FACE no Face). A foto é a Nora no dia a dia (Clone R2), sem cartas; o texto é curto; o aluno põe só o adesivo de link, no próprio app.

## ⚠️ Desde 18/11/2026: o estilo é o texto nativo do Instagram (não mais o creme)
O aluno pediu um story "mais simples, mais básico, igual é falado nas aulas", e deixou comigo o texto, a fonte, a cor e o tamanho ("quem vai editar a foto e colocar o texto é você"). Nenhuma aula fala de fonte ou cor: a aula 39 (0:58:02, o Felps) fala de "imagens… com textuzinho", e o Clone R2 (aulas 13, 54 e 55), de texto curto e objetivo. **Ajuste das ~16h50, pelos 5 stories de contas do nicho (`MATERIAIS-STORIES-REFERENCIA/LEIA.md`): o texto vai no MEIO da tela, sobre o peito, logo acima do adesivo, em 1 a 3 caixas (uma branca com preto e outra coral com branco), com emoji no fim; o adesivo leva texto próprio em maiúsculas ("SEE YOUR 2027 ✨") e pode ter o GIF da mãozinha. Uso: `--caixa "branco|..." --caixa "coral|... 👇"`, `--topo 0.46`; o script diz onde fica o adesivo. O resto do parágrafo abaixo (o modo, o topo 0.08 e "sem emoji") ficou antigo.** O padrão agora: `ferramentas-painel/ferramentas/texto_story_nativo.py`, que imita o texto que qualquer pessoa põe no app: Inter SemiBold (parecida com a "Classic" do Instagram), centralizada, cada linha numa faixa de cantos arredondados, sem sombra, sem cor de destaque e sem itálico; `--modo branco` (texto preto em faixa branca, o padrão, para parede clara), `preto` (texto branco em faixa preta) ou `sombra` (texto branco sem faixa, para fundo escuro); `--tamanho 0.042` e `--topo 0.08` de partida. **Sem emoji na imagem** (a fonte não tem; a ação fica no adesivo). Texto de 1 a 2 linhas, ligado ao CTA do vídeo do dia; o adesivo de link "TAP HERE" (Adão Gomes, 27/10). O passo a passo abaixo continua (escolher a foto, conferir o recorte e o celular, entregar, registrar); o estilo creme (`texto_story.py`) fica só como histórico.

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
