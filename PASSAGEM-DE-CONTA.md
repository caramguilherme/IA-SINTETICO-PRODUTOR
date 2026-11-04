# Passagem para a outra conta do Claude (feita em 03/11/2026; estado atualizado em 04/11/2026)

O aluno vai continuar o projeto da Nora em **outra conta do Claude** (a 4ª; a conta de 30/10 chegou a 96% do uso semanal em 03/11). Este arquivo diz o que a sessão nova faz primeiro. **Todo o conhecimento do projeto está no repositório** (regras, lições, estratégia, fatos, métricas, roteiros, painéis, histórico do Discord, aulas, VSL). Fora dele ficam só os Artifacts publicados na conta de 30/10 (painéis, dashboard e o doc do MVM), que a conta nova não abre nem edita e por isso recria a partir dos arquivos daqui.

**Branch com tudo:** `claude/lucid-planck-zz5ob8` do repositório `caramguilherme/ia-sintetico-produtor` (último trabalho em 04/11/2026). A `main` ficou em 30/10: a sessão nova traz a branch, como abaixo.

## 1. Antes de colar a mensagem (aluno)
1. Na conta nova, abrir o Claude Code na nuvem (claude.ai/code) e começar uma sessão **com o repositório `caramguilherme/ia-sintetico-produtor`**.
2. Se o repositório não aparecer ou o envio (push) falhar: conectar o GitHub na conta nova e instalar o Claude GitHub App no repositório (já aconteceu em 26/10; `FATOS-DO-ALUNO.md`, GitHub).
3. Colar a mensagem abaixo como primeira mensagem.

## 2. Mensagem para colar na sessão nova
> Sou o Guilherme. Estou trazendo o projeto da Nora de outra conta do Claude. Todo o trabalho está na branch `claude/lucid-planck-zz5ob8` do repositório `caramguilherme/ia-sintetico-produtor`. Primeiro traga essa branch para a sua: `git fetch origin claude/lucid-planck-zz5ob8` e `git merge origin/claude/lucid-planck-zz5ob8`. Depois leia inteiros o `PASSAGEM-DE-CONTA.md` (a seção 6, com o estado de 04/11, primeiro), a seção 0 do `CLAUDE.md` (os itens de 03 e 04/11 no topo), o `FATOS-DO-ALUNO.md` e o topo do `COMUNIDADE-E-ESTRATEGIA.md` ("Regras em vigor", de 03/11), e siga o passo a passo da passagem, com os painéis e as métricas exatamente iguais aos de hoje (seção 7: o mesmo PAINEL-MODELO.html, a mesma página do dashboard e a mesma planilha): recriar o dashboard "Métricas da Nora" igual ao de hoje, recriar o meu doc "Plano MVM Legacy – Appyon", atualizar a skill do doc e republicar os painéis do nora47, do nora48 e do nora49 e reinstalar o `faster-whisper` para a edição automática (P45). No fim, me diga os links novos e o que falta para o plano de hoje.

## 3. Passo a passo da sessão nova
1. **Trazer a branch** (comandos acima) e conferir que chegaram `CLAUDE.md`, `FATOS-DO-ALUNO.md`, `LICOES-FLOW-E-PROMPTS.md`, `COMUNIDADE-E-ESTRATEGIA.md`, `METRICAS-NORA.csv`, `ANALISE-FUNIL-MANIFESTATION-VSL.md` e `PAINEL-NORA47.html`. Anotar na seção 0 do `CLAUDE.md` o nome da branch nova da sessão: as próximas passagens partem dela.
2. **Ler antes de responder:** o `CLAUDE.md` inteiro (seção 0 primeiro; as regras P1 a P45 no fim), o `FATOS-DO-ALUNO.md` (nunca perguntar o que está lá) e as "Regras em vigor" do `COMUNIDADE-E-ESTRATEGIA.md`. **Antes de qualquer roteiro, fala nova ou painel: a leitura completa do `LEIA-TUDO-ANTES.md`**, com o registro no roteiro e no painel.
3. **Recriar o dashboard "Métricas da Nora"** pela receita de `ferramentas-painel/dashboard/COMO-RECRIAR.md` (tipo Dashboard da conta; CSV sem o BOM como asset; os 4 documentos do banco a partir de `ferramentas-painel/dashboard/store/` e `index.html`). O CSV atual tem 98 linhas (leituras até 03/11 01h28). Trocar o link no `CLAUDE.md` (seções 0 e 3), no `METRICAS-NORA-LEIA.md` e neste arquivo.
4. **Recriar o doc "Plano MVM Legacy – Appyon"** como um Claude Doc a partir de `PLANO-MVM-LEGACY-APPYON.md` (cópia em dia: todas as edições do doc foram espelhadas no arquivo até 03/11). É grande: criar o doc com as seções de nível 2 e encher uma por vez. Se a conta nova não tiver o conector de Docs, avisar o aluno e seguir pelo arquivo.
5. **Skill do doc:** trocar no `SKILL.md` de `ferramentas-painel/skills/doc-mvm-legacy.zip` o link e os ids do doc pelos do doc novo, refazer o zip e avisar o aluno para instalar (claude.ai, Configurações, Capacidades, Skills).
6. **Painéis a republicar (ainda não postados):** `PAINEL-NORA47.html` (já na versão do gancho do tsunami, de 04/11), `PAINEL-NORA48.html` e `PAINEL-NORA49.html` (publicar cada arquivo como Artifact, sem mudar nada; links novos no `CLAUDE.md`). Os outros já foram postados e só se republicam se o aluno pedir para consultar. Painéis novos saem do `PAINEL-MODELO.html` e dos scripts de `ferramentas-painel/` (`LEIA.md` lá; os de 31/10 a 03/11 em `r3110/`).
7. **Edição automática (P45):** `pip install faster-whisper` (o modelo "small" baixa sozinho no 1º uso); a fonte, as imagens do desejo e as avaliações já estão no repositório (`ferramentas-painel/ferramentas/fontes/`, `ferramentas-painel/imagens-fixas/`, `provas-trustpilot/`). O aluno só anexa o vídeo `noraNN-montado` com o texto fixo de `ferramentas-painel/ferramentas/LEIA.md`.
8. **Commit e push** na branch da sessão nova a cada mudança, com a assinatura que o sistema der.

## 4. Onde está cada coisa
| O quê | Onde |
|---|---|
| Regras do agente (P1 a P45), onde paramos, links | `CLAUDE.md` (seção 0 = diário de decisões; P43 a P45 no fim) |
| Regras em vigor, resumidas (03/11) | topo do `COMUNIDADE-E-ESTRATEGIA.md` |
| Fatos da conta, funil, telas do quiz, links do story, contatos | `FATOS-DO-ALUNO.md` |
| Lições do Flow, dos prompts, do painel e do CapCut (checklist 1 a 36; o 35 é a edição automática e o 36 o checklist da Appyon) | `LICOES-FLOW-E-PROMPTS.md` |
| Discord, DMs, aulas, estratégia | `COMUNIDADE-E-ESTRATEGIA.md` (conversas inteiras em `HISTORICO-DISCORD/`, lidas até 03/11 22h04 no chat-appyon e 21h26 no vitórias-dólar) |
| Conversas com outros alunos (P44): método e quadro de cada contato | `CONTATOS-ALUNOS.md` (detalhe de cada conversa na linha da pessoa em `FATOS-DO-ALUNO.md`) |
| Funil de Manifestation e a VSL | `BRIEFING-MANIFESTACAO.md` e `ANALISE-FUNIL-MANIFESTATION-VSL.md` (com a VSL inteira em inglês) |
| Aulas e materiais | `AULA-IORHAN-30-10-COPY-QUE-CONVERTE.md` (P42), `AULA-02-11-DO-MEDO-AO-DESEJO.md`, `AULA-03-11-TURBINANDO-CRIATIVOS-IORHAN.md` (com os materiais oficiais da Appyon resumidos na seção 4; arquivos em `MATERIAIS-CALL-03-11/`) e `AULA-07-09-ANALISE-DE-FUNIL.md` |
| Base do nora50 em diante | `REFERENCIA-VIDEO-*.md` (Letícia, Mariana, Mabel, Genevieve), `BANCO-DE-HEADLINES.md`, guia de manifestação em `MATERIAIS-CALL-03-11/` |
| Quando insistir, trocar gancho, copy ou avatar; perfis novos | `VALIDACAO-CONTA-E-AVATAR.md` |
| Números de cada vídeo e o diário das leituras | `METRICAS-NORA.csv` e `METRICAS-NORA-LEIA.md` |
| Peças geradas e postadas | `BIBLIOTECA-DE-TAKES.md` |
| Vídeos de referência, pré-ganchos, provas reais | `BIBLIOTECA-VIDEOS-VIRAIS.md`, `BIBLIOTECA-PRE-GANCHOS.md`, `PROVAS-REAIS-TRUSTPILOT.md` |
| Roteiros e painéis | `ROTEIRO-NORA*.md`, `PAINEL-NORA*.html`, `PAINEL-FACE01.html`, `PAINEL-FACE02.html`; reserva do próximo corpo em `RESERVA-ROTEIRO-CORPO-C-TEMPO-PASSANDO-PORTAL-1111.md` |
| Doc do MVM (curso, Appyon, contas, custos, dicas) | `PLANO-MVM-LEGACY-APPYON.md` |
| Dashboard, skill, ferramentas | `ferramentas-painel/dashboard/`, `ferramentas-painel/skills/`, `ferramentas-painel/ferramentas/LEIA.md` (edição automática `editar_video.py`, fonte Poppins, transcrição) |
| Imagens para a edição | `ferramentas-painel/imagens-fixas/` (as 3 do desejo) e `provas-trustpilot/` (4 avaliações reais) |

Os vídeos e prints que o aluno mandou ficaram só nas sessões antigas; a análise de cada um está nos arquivos acima. Se a sessão nova precisar rever algum, o aluno manda de novo.

## Links da 4ª conta (feita em 03/11/2026 ~02h, os que valem)
- Dashboard Métricas da Nora: https://claude.ai/artifact/BzjxbGkWRRKcJdBSnUpzyd (asset do CSV `/_blob/2eea2cdfa775d1c3b34f4b4271b7c254`, leituras até 04/11 01h51, dataset na versão 6; página conferida igual à do repositório)
- Doc Plano MVM Legacy – Appyon: https://claude.ai/artifact/Km3GMYScCPw44sR57wyiLm (projeto 97ea9e11-09da-4f48-8716-9082a424ec1e · tab 196695a6-55f2 · corpo c385a971-4b8e; conferido linha a linha com `PLANO-MVM-LEGACY-APPYON.md`)
- Painéis: **nora47** https://claude.ai/artifact/SoqFZUhSwEr8SDUQMbCk7a · **nora48** https://claude.ai/artifact/JyeRSyXZzdbCq2h6afNzz7 · **nora49** https://claude.ai/artifact/CsKv1MzDjzcZ4akJGRZ3wM
- Skill: `ferramentas-painel/skills/doc-mvm-legacy.zip` com o link novo (instalar nesta conta)
- Branch: a mesma, `claude/lucid-planck-zz5ob8`.

## 5. Links da conta de 30/10 (só abrem naquela conta; não são mais atualizados depois da passagem)
- Dashboard Métricas da Nora: https://claude.ai/artifact/7ZArpHDLZZcuA8DPEMAZGR (asset do CSV `/_blob/64869fe38eb4e2785b6ada83736434bd`, dataset na versão 26)
- Doc Plano MVM Legacy – Appyon: https://claude.ai/artifact/HsK6QVZRWUK1pdD2xi7JfF
- Painéis: nora44 https://claude.ai/artifact/SY78kS7dxiSFjrBFnoogxj · nora45 https://claude.ai/artifact/WzqX4wBDdeZo9G1dSHc8Bx · nora46 https://claude.ai/artifact/W6EBF2bdfPQ6YhCM4MaEF1 · **nora47** https://claude.ai/artifact/SoyRmVkQWNAEVXQ9mwtg5K · **nora48** https://claude.ai/artifact/CAbhHw2pxw6N3ytWS46Bwj · **nora49** https://claude.ai/artifact/1N7U8uiBXuEgKGwH3hE84s · face01 https://claude.ai/artifact/MUke2u5Yx5ELCnQ5jv5ULn · face02 https://claude.ai/artifact/KeXyFoszrLZx7BZr42765U
- Conta contatocaram (27 a 30/10, só para ver): dashboard https://claude.ai/artifact/CTdhXsH5PoQFRCnzpbM4wy, doc https://claude.ai/artifact/Dd3bgq9RuSKyoKT2z2bLh6.

## 6. Estado em 04/11/2026 ~03h (o que a sessão nova pede ao aluno)
- **Últimos posts:** nora46 (corpo B) em 31/10 às 18h30; face02 em 02/11 às 21h13; **story-0311 em 03/11 às ~22h45** (Insta e Face; vence ~22h45 de 04/11: o próximo story vai antes disso). Nada de vídeo em 01, 02 (fora o face02) e 03/11.
- **nora47 em produção (painel no link SoqFZUhSwEr8SDUQMbCk7a):** gancho do tsunami (praia, onda, bunker) + Take 1 no estúdio com a `nora46-IMG` ("Taurus, Virgo or Capricorn: if love hasn't caught up with who you've become, this wave came to clear the way before 11:11.") + o vídeo final do nora46 a partir do Take 2. **Imagens aprovadas em 04/11:** `nora47-PRE-IMG1` (2ª variação), `nora47-PRE-IMG2` (1ª), `nora47-PRE-IMG3` (2ª) (`BIBLIOTECA-DE-TAKES.md`). Faltam os 2 vídeos em Frames (PRE-A e PRE-B, 7 cada), o Take 1 (15) e a montagem no CapCut; o aluno manda o `nora47-montado` e eu edito (P45). Julgar pelo clique no story e no Tracker (Iorhan: bizarro fora do nicho dá view sem compra), contra o nora46.
- **nora48 e nora49:** esperam a leitura de ~3 h do nora47; se o tsunami segurar, reaproveitam o gancho (0) e geram só o Take 1 (15 cada). Tudo com portal 11:11 para de ir ao ar depois de 11/11.
- **nora50:** direção na seção 0 do `CLAUDE.md` (fatia "manifesta e nada chega", ângulo quebra de crença "STOP CHASING MONEY", estrutura "Most women who...", CTA em 4 partes, quarto à noite com imperfeição), modelado de uma referência validada (viral minerado pelo aluno ou vídeo do YouTube com "x" alto). Antes do roteiro: a leitura obrigatória completa.
- **Créditos (03/11 ~23h15):** 53 numa conta e 137 na outra (o nora47 gasta 29 da de 137).
- **Pedir ao aluno:** o `nora47-montado`; leituras de ~3 h e ~24 h do nora47 (Insta e Face, com os comentários de outras pessoas); story e Tracker de 03 e 04/11; o swipe de ~30 criativos e o briefing do Love Reading quando saírem (call de sexta 06/11 às 19h); os virais minerados para o nora50.
- **Conversas (P44, `CONTATOS-ALUNOS.md`):** voltar à Jessica em 2 a 3 dias com o resultado do CTA novo; ao Vinicius Almeida com o resultado do gancho novo; Allan Mayer esperando a resposta (de onde ele tira as copys virais); os outros fechados até haver resultado.
- **Datas:** GeeLark vence em 05/11 (~US$ 5) e a proxy da Nora em 06/11 às 14h52 (~US$ 3,59); janela dos 40 vídeos da Nora fecha ~06 a 08/11 (depois: Nora sem as joias no rosto num corpo validado, ou o 2º perfil); call de sexta 06/11 às 19h; portal 11:11 em 11/11.

## 7. Painéis e métricas iguais na conta nova (pedido do aluno, 03/11/2026: "as regras dos painéis e das métricas precisam ser iguais, pro layout e o modelo continuar o mesmo")
**Painéis**
- **O modelo é um só: `PAINEL-MODELO.html`** (sha256 começa com `49f4c6308119`, versão de 03/11 com as bordas do Face do P43). Não redesenhar, não trocar cores, seções nem textos fixos. Painel novo = o modelo inteiro com só a linha `const PACOTE = null;` trocada pelo pacote (P1 a P45; o jeito de montar está nos scripts de `ferramentas-painel/r3110/`, o mais novo é o `build_4749.py`). Mudança no modelo só quando uma regra nova pedir, registrada nas lições e no `ferramentas-painel/LEIA.md`.
- **Regras do conteúdo do painel:** o checklist 1 a 36 da seção 1 do `LICOES-FLOW-E-PROMPTS.md` (P36 painel enxuto; mapa da tela 720×1280; Poppins Bold e tamanhos; números espalhados; margem do Face; respostas no Face; edição enxuta; registro da leitura obrigatória).
- **Republicar sem mudar nada:** os painéis do nora47 ao nora49 vão como estão nos arquivos (`PAINEL-NORA47.html`…), que são idênticos aos publicados na 4ª conta em 04/11 (o nora47 já com o tsunami; scripts `ferramentas-painel/r0311/`).
- **Conferir antes de entregar:** `node ferramentas-painel/conferir-painel.js PAINEL-NORAxx.html` (tem que dizer "ERR: nenhum").

**Métricas e dashboard**
- **A página do dashboard é a `ferramentas-painel/dashboard/index.html`** (sha256 começa com `8e557cc13571`, conferida em 03/11 igual à publicada) e o banco usa os 3 arquivos de `ferramentas-painel/dashboard/store/` (título "Métricas da Nora"; filtros iniciais período "v2" e rede "Instagram"; a planilha como arquivo CSV). Recriar exatamente assim (`COMO-RECRIAR.md`) e, depois, ler de volta o `files/index.html` publicado e conferir que é igual ao do repositório.
- **A planilha é a `METRICAS-NORA.csv`:** UTF-8 com BOM e linhas em CRLF; colunas `ordem,video,rede,funil,postado,views,viewers,likes,comentarios,salvos,compart,reposts,follows,skip,ret3s,tempo,pais1,pais2,pais3,pais4,pais5,print,legenda,obs,nota_face,id`; **uma linha por vídeo e rede** (id `noraNN-ig` / `noraNN-fb`, `faceNN-fb` / `faceNN-ig`; `ordem` = número do vídeo, e os testes do Face com decimal, como 45.1 e 46.1). A cada leitura nova, a linha recebe os números novos e a hora em `print`; no Face, `nota_face` acumula "Leitura dd/mm hh (~X h): …"; `ret3s` = views de 3 s ÷ views × 100 e `skip` = 100 − `ret3s`. **No Insta, anotar quantos comentários são de outras pessoas** (sem o fixado nem as respostas).
- **Cada leitura também vai para o `METRICAS-NORA-LEIA.md`** (uma entrada datada, com a leitura e a decisão), e o aluno manda os números pelo modelo do fim desse arquivo.
- **Atualizar o dashboard:** `python3 -I ferramentas-painel/dashboard/preparar_csv.py <pasta>` (gera a cópia sem o BOM e o `rows.json`) → `node ferramentas-painel/dashboard/conferir-dados.js ferramentas-painel/dashboard/index.html <pasta>/rows.json` (sem ids repetidos ou vazios) → subir a cópia como asset do dashboard → `update` em `datasets/metricas` (`source.url`, `source.name`, `updated`) com `if_version`.

- **Conversas com outros alunos (P44, 03/11/2026):** a sessão nova segue o método de `CONTATOS-ALUNOS.md` (criar laço, colher dicas, aplicar, voltar com resultado, agradecer em público) e continua o quadro de onde parou.

**03/11/2026 noite:** regra P45 (edição automática aqui no Code; `ferramentas-painel/ferramentas/editar_video.py`). Numa sessão nova, reinstalar `faster-whisper` antes do 1º vídeo. Resumo das regras novas da noite no topo da seção 0 do `CLAUDE.md`.
