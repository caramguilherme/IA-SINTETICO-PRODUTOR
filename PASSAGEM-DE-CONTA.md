# Passagem para outra conta do Claude (atualizado no pente fino de 06/11/2026; vale para a 6ª conta em diante)

O aluno usa uma conta do Claude até o limite semanal acabar e passa para outra. Este arquivo diz o que a sessão nova faz primeiro. **Todo o conhecimento do projeto está no repositório** (regras, lições, estratégia, fatos, contatos, métricas, roteiros, painéis, histórico do Discord, aulas, VSL, briefings e a cópia principal do doc do MVM). Fora dele ficam só os Artifacts (painéis, dashboard) e o ambiente do Claude Code, que são de cada conta: a sessão nova recria os dois.

**Branch com tudo:** `claude/lucid-planck-zz5ob8` do repositório `caramguilherme/ia-sintetico-produtor` (a `main` parou em 30/10): a sessão nova traz a branch, como abaixo.

## 1. Antes de colar a mensagem (aluno)
1. Na conta nova, abrir o Claude Code na nuvem (claude.ai/code) e começar uma sessão **com o repositório `caramguilherme/ia-sintetico-produtor`**.
2. Se o repositório não aparecer ou o envio (push) falhar: conectar o GitHub na conta nova e instalar o Claude GitHub App no repositório (já aconteceu em 26/10; `FATOS-DO-ALUNO.md`, GitHub).
3. Colar a mensagem da seção 2 como primeira mensagem.

## 2. Mensagem para colar na sessão nova
> Sou o Guilherme. Estou trazendo o projeto da Nora de outra conta do Claude. Todo o trabalho está na branch `claude/lucid-planck-zz5ob8` do repositório `caramguilherme/ia-sintetico-produtor`. Primeiro traga essa branch para a sua: `git fetch origin claude/lucid-planck-zz5ob8` e `git merge origin/claude/lucid-planck-zz5ob8`. Depois leia o `PASSAGEM-DE-CONTA.md`, o `CLAUDE.md` inteiro (seções 0 a 5 no topo, com o estado atual na seção 1, e as regras P1 a P45 no fim), o `FATOS-DO-ALUNO.md`, o `CONTATOS-ALUNOS.md` e as últimas entradas do `COMUNIDADE-E-ESTRATEGIA.md`, e siga o passo a passo da passagem: o ambiente do Claude Code (passo 1b), o dashboard "Métricas da Nora" igual ao de hoje, os painéis dos vídeos ainda não postados e o `faster-whisper` para a edição automática (P45). No fim, me diga os links novos e me pergunte o que eu postei desde a última mensagem da outra conta.

## 3. Passo a passo da sessão nova
1. **Trazer a branch** (comandos acima) e conferir que chegaram `CLAUDE.md`, `FATOS-DO-ALUNO.md`, `CONTATOS-ALUNOS.md`, `LICOES-FLOW-E-PROMPTS.md`, `COMUNIDADE-E-ESTRATEGIA.md`, `METRICAS-NORA.csv` e os `PAINEL-NORANN.html` dos vídeos ainda não postados (`CLAUDE.md`, seção 1). Anotar na seção 1 do `CLAUDE.md` a conta nova (e a branch, se for outra).
1b. **Ambiente do Claude Code (06/11/2026):** cada conta do Claude tem os seus ambientes. Na conta nova, o padrão costuma liberar pouca coisa (na 5ª conta, só scoped.com.br): o Google Drive (vídeos acima de 30 MB) e o modelo da transcrição davam 403. Criar um ambiente pessoal chamado `ia-sintetico-produtor` (create_environment, com o aluno aprovando no cartão), com os hosts scoped.com.br, www.scoped.com.br, drive.google.com, drive.usercontent.google.com, huggingface.co, cdn-lfs.hf.co, cdn-lfs.huggingface.co, cas-bridge.xethub.hf.co e us.aws.cdn.hf.co, e o setup `pip install -q faster-whisper gdown`; ou o aluno adiciona esses hosts em Allowed domains do ambiente padrão. Baixar vídeo do Drive com `curl -sS -L -o <pasta>/noraNN-montado.mp4 "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"` (o `gdown` cai num servidor do Google que a rede não libera).
2. **Ler antes de responder:** o `CLAUDE.md` inteiro (seções 0 a 5 no topo; P1 a P45 no fim), o `FATOS-DO-ALUNO.md` (nunca perguntar o que está lá), o `CONTATOS-ALUNOS.md` (toda resposta sugerida conta como enviada; não lembrar de novo) e as últimas entradas do `COMUNIDADE-E-ESTRATEGIA.md`. **Antes de qualquer roteiro, fala nova ou painel: a leitura completa do `LEIA-TUDO-ANTES.md`**, com o registro no roteiro e no painel.
3. **Recriar o dashboard "Métricas da Nora"** pela receita de `ferramentas-painel/dashboard/COMO-RECRIAR.md` (tipo Dashboard da conta; CSV sem o BOM como asset; os documentos do banco a partir de `ferramentas-painel/dashboard/store/` e o `index.html`). Trocar o link no `CLAUDE.md` (seção 1), no `METRICAS-NORA-LEIA.md` e no `COMO-RECRIAR.md`.
4. **Doc do MVM (atualizado em 06/11):** a cópia principal é `PLANO-MVM-LEGACY-APPYON.md`, no repositório; a sessão nova só lê e atualiza esse arquivo (doc do claude.ai não abre entre contas). Recriar um doc para ler só se o aluno pedir. Histórico: o vivo era https://claude.ai/artifact/2KP736NhHJUXjF4s4JkANs, mantido também pela conversa do aluno no claude.ai (que faz as leituras do Discord e guarda a skill `doc-mvm-legacy`). A sessão nova tenta ler esse doc. **Se abrir, segue editando ele. Se não abrir** (é de outra conta), avisar o aluno: ou ele compartilha o doc com a conta nova, ou a sessão recria o doc a partir de `PLANO-MVM-LEGACY-APPYON.md` (cópia exportada do doc vivo em 05/11 ~14h, revisão 138, idêntica a ele) e troca o link na skill do claude.ai. **Não instalar o zip da skill do repositório** sem conferir com o aluno: ele é só cópia da skill do claude.ai.
5. **Painéis:** republicar como Artifacts, sem mudar nada, os `PAINEL-NORANN.html` dos vídeos que ainda não foram postados (a seção 1 do `CLAUDE.md` diz quais), depois de ler cada arquivo inteiro e rodar `node ferramentas-painel/conferir-painel.js` ("ERR: nenhum"). Painéis novos saem do `PAINEL-MODELO.html` e dos scripts de `ferramentas-painel/` (os mais novos em `rDDMM/`).
6. **Edição automática (P45):** o ambiente do passo 1b instala o `faster-whisper` e o `gdown` (o modelo "small" baixa no 1º uso, com `HF_HUB_DISABLE_XET=1`). A fonte, as imagens do desejo e as avaliações estão no repositório (`ferramentas-painel/ferramentas/fontes/`, `ferramentas-painel/imagens-fixas/`, `provas-trustpilot/`). Specs prontas: corpo B em `ferramentas-painel/r0411/spec-nora47.json` e corpo A limpo em `ferramentas-painel/r0611/spec-nora48.json`, com as transcrições; o tempo de cada palavra sai de `ferramentas-painel/r0611/transcrever_palavras.py`. Os tempos mudam a cada vídeo: transcrever o novo e conferir um quadro de cada trecho. O aluno só manda o `noraNN-montado` (Drive acima de 30 MB).
7. **Commit e push** na branch da sessão nova a cada mudança, com a assinatura que o sistema der.

## 4. Onde está cada coisa
| O quê | Onde |
|---|---|
| Regras do agente (P1 a P45), onde paramos, links | `CLAUDE.md` (seção 0 = diário de decisões; P43 a P45 no fim) |
| Regras em vigor, resumidas | topo do `COMUNIDADE-E-ESTRATEGIA.md` (03/11) e os itens de 04 e 05/11 da seção 0 do `CLAUDE.md` |
| Fatos da conta, funil, telas do quiz, links do story, contatos (linha de cada pessoa) | `FATOS-DO-ALUNO.md` |
| Conversas com outros alunos (P44): método e quadro de cada contato, rascunhos enviados | `CONTATOS-ALUNOS.md` |
| Lições do Flow, dos prompts, do painel e do CapCut (checklist; a de 05/11 sobre o agente que recusou frame inicial e final com fala está no fim) | `LICOES-FLOW-E-PROMPTS.md` |
| Discord, DMs, aulas, estratégia | `COMUNIDADE-E-ESTRATEGIA.md` (conversas inteiras em `HISTORICO-DISCORD/`, lidas até 05/11 11h29 no chat-appyon e 09h10 no vitórias-dólar) |
| Funil de Manifestation e a VSL | `BRIEFING-MANIFESTACAO.md` e `ANALISE-FUNIL-MANIFESTATION-VSL.md` |
| Funil do 2º perfil (Love Reading) | `BRIEFING-LOVE-READING.md` (PDF em `BRIEFING-LOVE-READING-AURALY.pdf`) |
| Aulas e materiais | `AULA-IORHAN-30-10-COPY-QUE-CONVERTE.md` (P42), `AULA-02-11-DO-MEDO-AO-DESEJO.md`, `AULA-03-11-TURBINANDO-CRIATIVOS-IORHAN.md` (materiais em `MATERIAIS-CALL-03-11/`), `AULA-07-09-ANALISE-DE-FUNIL.md` |
| Base do nora50 em diante | `REFERENCIA-VIDEO-*.md`, `BANCO-DE-HEADLINES.md`, guia de manifestação em `MATERIAIS-CALL-03-11/` |
| Quando insistir, trocar gancho, copy ou avatar; perfis novos | `VALIDACAO-CONTA-E-AVATAR.md` |
| Números de cada vídeo, Tracker e o diário das leituras | `METRICAS-NORA.csv` e `METRICAS-NORA-LEIA.md` |
| Peças geradas e postadas | `BIBLIOTECA-DE-TAKES.md` |
| Vídeos de referência, pré-ganchos, provas reais | `BIBLIOTECA-VIDEOS-VIRAIS.md`, `BIBLIOTECA-PRE-GANCHOS.md`, `PROVAS-REAIS-TRUSTPILOT.md` |
| Roteiros e painéis | `ROTEIRO-NORA*.md`, `PAINEL-NORA*.html`, `PAINEL-FACE01.html`, `PAINEL-FACE02.html`; reserva do próximo corpo em `RESERVA-ROTEIRO-CORPO-C-TEMPO-PASSANDO-PORTAL-1111.md` |
| Doc do MVM (curso, Appyon, contas, custos, dicas) | `PLANO-MVM-LEGACY-APPYON.md` (cópia do doc vivo de 05/11 ~14h) |
| Dashboard, skill, ferramentas | `ferramentas-painel/dashboard/`, `ferramentas-painel/skills/`, `ferramentas-painel/ferramentas/LEIA.md` (`editar_video.py`, fonte Poppins, transcrição) |
| Imagens para a edição | `ferramentas-painel/imagens-fixas/` (as 3 do desejo) e `provas-trustpilot/` (4 avaliações reais) |

Os vídeos e prints que o aluno mandou ficaram só nas sessões antigas; a análise de cada um está nos arquivos acima. Se a sessão nova precisar rever algum (por exemplo o `nora47-montado`, base do nora49), o aluno manda de novo.

## 5b. Feito na 5ª conta (06/11/2026 ~00h)
- Dashboard Métricas da Nora: https://claude.ai/artifact/GnvCkx6wnMNqcJE6BVGaUP (asset do CSV `/_blob/06441b1da354ba946b84efdd4042f713`, dataset na versão 1, o mesmo CSV de 04/11 12h23)
- Painéis: **nora48** https://claude.ai/artifact/QQpxR4dxqovuceqfrsHNU5 · **nora49** https://claude.ai/artifact/GFB4scmCX4tDB54bmhYXv3 (os arquivos como estavam)
- Doc do MVM: o vivo (2KP736NhHJUXjF4s4JkANs) não abre nesta conta; esperando o aluno compartilhar ou pedir a recriação
- `faster-whisper` 1.2.1 instalado

## 5. Links da 4ª conta (03 a 05/11; só a 4ª conta edita; não são mais atualizados depois da passagem)
- Dashboard Métricas da Nora: https://claude.ai/artifact/BzjxbGkWRRKcJdBSnUpzyd (asset do CSV `/_blob/28ad542021e3a0cc7dd9a4743eb5acf5`, dataset na versão 10, leituras até 04/11 12h23)
- Doc do MVM: o vivo é https://claude.ai/artifact/2KP736NhHJUXjF4s4JkANs (projeto 0aaa260d-18c9-48de-a9f4-eafa2d73e8e0 · tab 5b5b5c61-f3e5 · corpo 0d0724eb-ab64). Parado: https://claude.ai/artifact/Km3GMYScCPw44sR57wyiLm
- Painéis: nora47 https://claude.ai/artifact/SoqFZUhSwEr8SDUQMbCk7a (já postado) · **nora48** https://claude.ai/artifact/JyeRSyXZzdbCq2h6afNzz7 · **nora49** https://claude.ai/artifact/CsKv1MzDjzcZ4akJGRZ3wM (versão 6 de cada, 05/11 ~13h45)
- Links das contas de 30/10 e contatocaram: no histórico do `CLAUDE.md` (seção 0); não são mais atualizados.

## 6. Estado (desde 06/11/2026 o estado atual fica no `CLAUDE.md`, seção 1, atualizado a cada mudança; a sessão nova lê de lá e pergunta ao aluno o que mudou desde a hora escrita nele). Abaixo, o estado de 05/11 ~14h, só como histórico
- **Último vídeo postado:** nora47 em 04/11 às 01h35 (tsunami + Take 1 novo + corpo B). Nada saiu em 04/11 depois dele. **Tracker:** 04/11 = 0 clique o dia todo; 05/11 = 0 até 12h36 (o story-0311 venceu ~22h45 de 04/11; repost pedido para 05/11). Manifestation de 27/10 a 05/11: 17 cliques reais (todos do Insta), 9 no fim do quiz, 0 checkout. **Face: 0 clique real desde o início.**
- **Plano de 05/11 (em produção na hora da passagem):** story-0311 repostado; **nora48 às 17h** (tsunami + Take 1 de Câncer/Escorpião/Peixes na `nora37-IMG` + corpo A limpo, os 7 takes do nora40) e **nora49 às 19h30** (tsunami espelhado + Take 1 de Áries/Leão/Sagitário na `nora46-IMG` + corpo B a partir do `nora47-montado`). O aluno estava gerando o Take 1 do nora48 quando o **agente do Flow recusou "frame inicial e frame final" com fala**; a saída é gerar à mão no modo Frames (Início = a imagem, Fim vazio, Omni 1.1 Flash, 9:16, 10 s), já escrita nos dois painéis e nas lições. Eu edito os dois pela P45 quando ele mandar o `nora48-montado` e o `nora49-montado`.
- **A sessão nova pergunta:** o que saiu em 05/11 e em 06/11 e a que horas; se o story foi repostado; o Tracker de 05 e 06/11; as leituras do nora47 (~24 h) e do nora48 e nora49 (visitas ao perfil, comentários de outras pessoas, viewers do story); se o GeeLark (vencia 05/11) e a proxy (vencia 06/11 14h52) foram renovados; créditos do Flow (~78 na conta grande depois dos dois Takes 1 e 53 na outra).
- **Regras do teste dos corpos:** uma variável por vez (mesmo gancho, muda o corpo); **só julgar um corpo com 800 a 1.000 views somadas no Insta** (Ricardo, 05/11): o corpo B já soma ~420 (0 visita ao perfil); o corpo A limpo começa no nora48. Se nenhum dos dois levar ao perfil, o próximo teste é o **gancho realista ou sem pré-gancho, com o hook no texto do topo** (Marcus, 05/11: o vídeo da 1ª venda dele foi assim), que dá para fazer sem crédito cortando o tsunami de um vídeo pronto.
- **Postagem:** horários fixos 17h, 19h30, 22h e 00h30 no Insta e no Face, ao vivo; **desde 06/11, nenhum horário vazio** (Lari): sem vídeo novo pronto, entra uma variação de 0 crédito. Face: plano da semana de volume em `COMUNIDADE-E-ESTRATEGIA.md` (05/11, "Por que o Face da Nora não anda").
- **Créditos e Muse:** sem crédito no Flow para corpo novo (8 takes = 120). O aluno decidiu tentar o Muse AI pelo vídeo que o Ricardo mandou ("sem cartão, sem verificação"); a sessão não acompanha esse passo de acesso. Com o Muse aberto (plano oficial ou não), a sessão adapta o prompt da Central e testa 1 take antes de um corpo.
- **nora50:** direção na seção 0 do `CLAUDE.md` (fatia "manifesta e nada chega", "STOP CHASING MONEY", CTA em 4 partes, quarto à noite), modelado de um viral que o aluno minerar. Antes do roteiro: a leitura obrigatória completa. Nada com portal 11:11 depois de 11/11.
- **Avatar:** a janela de 40 vídeos (corrigido em 06/11: são 40 vídeos, não uma data; eram 15 no Insta em 06/11). O teste: a Nora sem a lua e as estrelinhas pintadas, com um traço real (sardas leves ou uma pinta), o resto igual (`VALIDACAO-CONTA-E-AVATAR.md`). 2º perfil (Love Reading) realista, com 1 traço real.
- **Conversas (P44, `CONTATOS-ALUNOS.md`):** esperando resposta de Felps, Kaike, Lari, Castanho, Marcelo, Allan e Letícia (não mandar outra mensagem sem resposta). Ricardo e Marcus fechados em 05/11: voltar em 2 ou 3 dias com o resultado. Jessica: voltar em 06/11 com o resultado do teste dos corpos. Não chamar o joao nem o Rechmann de novo.
- **Datas:** call de sexta 06/11 às 19h (pedir a gravação ou a transcrição e o swipe de criativos); portal 11:11 em 11/11; Masterclass do Kobata 14/11 às 13h, ao vivo (o aluno já fez o check-in).

## 7. Painéis e métricas iguais na conta nova (pedido do aluno, 03/11/2026: "as regras dos painéis e das métricas precisam ser iguais, pro layout e o modelo continuar o mesmo")
**Painéis**
- **O modelo é um só: `PAINEL-MODELO.html`** (versão de 03/11 com as bordas do Face do P43). Não redesenhar, não trocar cores, seções nem textos fixos. Painel novo = o modelo inteiro com só a linha `const PACOTE = null;` trocada pelo pacote. Mudança no modelo só quando uma regra nova pedir, registrada nas lições e no `ferramentas-painel/LEIA.md`.
- **Regras do conteúdo do painel:** o checklist da seção 1 do `LICOES-FLOW-E-PROMPTS.md` (P36 painel enxuto; mapa da tela 720×1280; Poppins Bold e tamanhos; números espalhados; margem do Face; respostas no Face; edição enxuta; registro da leitura obrigatória).
- **Republicar sem mudar nada:** os painéis do nora48 e do nora49 vão como estão nos arquivos, idênticos aos publicados na 4ª conta em 05/11 ~13h45.
- **Conferir antes de entregar:** `node ferramentas-painel/conferir-painel.js PAINEL-NORAxx.html` (tem que dizer "ERR: nenhum").

**Métricas e dashboard**
- **A página do dashboard é a `ferramentas-painel/dashboard/index.html`** e o banco usa os arquivos de `ferramentas-painel/dashboard/store/` (título "Métricas da Nora"; filtros iniciais período "v2" e rede "Instagram"; a planilha como arquivo CSV). Recriar exatamente assim (`COMO-RECRIAR.md`) e, depois, ler de volta o `files/index.html` publicado e conferir que é igual ao do repositório.
- **A planilha é a `METRICAS-NORA.csv`:** UTF-8 com BOM e linhas em CRLF; colunas `ordem,video,rede,funil,postado,views,viewers,likes,comentarios,salvos,compart,reposts,follows,skip,ret3s,tempo,pais1,pais2,pais3,pais4,pais5,print,legenda,obs,nota_face,id`; **uma linha por vídeo e rede** (id `noraNN-ig` / `noraNN-fb`, `faceNN-fb` / `faceNN-ig`). A cada leitura nova, a linha recebe os números novos e a hora em `print`; no Face, `nota_face` acumula "Leitura dd/mm hh (~X h): …"; `ret3s` = views de 3 s ÷ views × 100 e `skip` = 100 − `ret3s`. **No Insta, anotar quantos comentários são de outras pessoas** (sem o fixado nem as respostas).
- **Cada leitura também vai para o `METRICAS-NORA-LEIA.md`** (uma entrada datada, com a leitura e a decisão); o Tracker da Appyon vai só nele.
- **Atualizar o dashboard:** `python3 -I ferramentas-painel/dashboard/preparar_csv.py <pasta>` (gera a cópia sem o BOM e o `rows.json`) → `node ferramentas-painel/dashboard/conferir-dados.js ferramentas-painel/dashboard/index.html <pasta>/rows.json` → subir a cópia como asset do dashboard → `update` em `datasets/metricas` (`source.url`, `source.name`, `updated`) com `if_version`.

**Como responder ao aluno (05/11):** começar pelo que ele faz agora; texto para copiar pronto, com quebras de linha de verdade; dizer antes qual arquivo anexar; nada de "essa aí" ou "o de cima".
