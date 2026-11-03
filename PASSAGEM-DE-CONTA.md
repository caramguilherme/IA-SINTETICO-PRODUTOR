# Passagem para a outra conta do Claude (03/11/2026)

O aluno vai continuar o projeto da Nora em **outra conta do Claude** (a 4ª; a conta de 30/10 chegou a 96% do uso semanal em 03/11). Este arquivo diz o que a sessão nova faz primeiro. **Todo o conhecimento do projeto está no repositório** (regras, lições, estratégia, fatos, métricas, roteiros, painéis, histórico do Discord, aulas, VSL). Fora dele ficam só os Artifacts publicados na conta de 30/10 (painéis, dashboard e o doc do MVM), que a conta nova não abre nem edita e por isso recria a partir dos arquivos daqui.

**Branch com tudo:** `claude/lucid-planck-zz5ob8` do repositório `caramguilherme/ia-sintetico-produtor` (último trabalho em 03/11/2026). A `main` ficou em 30/10: a sessão nova traz a branch, como abaixo.

## 1. Antes de colar a mensagem (aluno)
1. Na conta nova, abrir o Claude Code na nuvem (claude.ai/code) e começar uma sessão **com o repositório `caramguilherme/ia-sintetico-produtor`**.
2. Se o repositório não aparecer ou o envio (push) falhar: conectar o GitHub na conta nova e instalar o Claude GitHub App no repositório (já aconteceu em 26/10; `FATOS-DO-ALUNO.md`, GitHub).
3. Colar a mensagem abaixo como primeira mensagem.

## 2. Mensagem para colar na sessão nova
> Sou o Guilherme. Estou trazendo o projeto da Nora de outra conta do Claude. Todo o trabalho está na branch `claude/lucid-planck-zz5ob8` do repositório `caramguilherme/ia-sintetico-produtor`. Primeiro traga essa branch para a sua: `git fetch origin claude/lucid-planck-zz5ob8` e `git merge origin/claude/lucid-planck-zz5ob8`. Depois leia inteiros o `PASSAGEM-DE-CONTA.md`, a seção 0 do `CLAUDE.md` (o item da QUARTA CONTA, de 03/11, primeiro), o `FATOS-DO-ALUNO.md` e o topo do `COMUNIDADE-E-ESTRATEGIA.md` ("Regras em vigor", de 03/11), e siga o passo a passo da passagem: recriar o dashboard "Métricas da Nora" igual ao de hoje, recriar o meu doc "Plano MVM Legacy – Appyon", atualizar a skill do doc e republicar os painéis do nora47, do nora48 e do nora49. No fim, me diga os links novos e o que falta para o plano de hoje.

## 3. Passo a passo da sessão nova
1. **Trazer a branch** (comandos acima) e conferir que chegaram `CLAUDE.md`, `FATOS-DO-ALUNO.md`, `LICOES-FLOW-E-PROMPTS.md`, `COMUNIDADE-E-ESTRATEGIA.md`, `METRICAS-NORA.csv`, `ANALISE-FUNIL-MANIFESTATION-VSL.md` e `PAINEL-NORA47.html`. Anotar na seção 0 do `CLAUDE.md` o nome da branch nova da sessão: as próximas passagens partem dela.
2. **Ler antes de responder:** o `CLAUDE.md` inteiro (seção 0 primeiro; as regras P1 a P43 no fim), o `FATOS-DO-ALUNO.md` (nunca perguntar o que está lá) e as "Regras em vigor" do `COMUNIDADE-E-ESTRATEGIA.md`. **Antes de qualquer roteiro, fala nova ou painel: a leitura completa do `LEIA-TUDO-ANTES.md`**, com o registro no roteiro e no painel.
3. **Recriar o dashboard "Métricas da Nora"** pela receita de `ferramentas-painel/dashboard/COMO-RECRIAR.md` (tipo Dashboard da conta; CSV sem o BOM como asset; os 4 documentos do banco a partir de `ferramentas-painel/dashboard/store/` e `index.html`). O CSV atual tem 98 linhas (leituras até 03/11 01h28). Trocar o link no `CLAUDE.md` (seções 0 e 3), no `METRICAS-NORA-LEIA.md` e neste arquivo.
4. **Recriar o doc "Plano MVM Legacy – Appyon"** como um Claude Doc a partir de `PLANO-MVM-LEGACY-APPYON.md` (cópia em dia: todas as edições do doc foram espelhadas no arquivo até 03/11). É grande: criar o doc com as seções de nível 2 e encher uma por vez. Se a conta nova não tiver o conector de Docs, avisar o aluno e seguir pelo arquivo.
5. **Skill do doc:** trocar no `SKILL.md` de `ferramentas-painel/skills/doc-mvm-legacy.zip` o link e os ids do doc pelos do doc novo, refazer o zip e avisar o aluno para instalar (claude.ai, Configurações, Capacidades, Skills).
6. **Painéis a republicar (ainda não postados):** `PAINEL-NORA47.html`, `PAINEL-NORA48.html` e `PAINEL-NORA49.html` (publicar cada arquivo como Artifact, sem mudar nada; links novos no `CLAUDE.md`). Os outros já foram postados e só se republicam se o aluno pedir para consultar. Painéis novos saem do `PAINEL-MODELO.html` e dos scripts de `ferramentas-painel/` (`LEIA.md` lá; os de 31/10 a 03/11 em `r3110/`).
7. **Commit e push** na branch da sessão nova a cada mudança, com a assinatura que o sistema der.

## 4. Onde está cada coisa
| O quê | Onde |
|---|---|
| Regras do agente (P1 a P43), onde paramos, links | `CLAUDE.md` (seção 0 = diário de decisões; P43 no fim) |
| Regras em vigor, resumidas (03/11) | topo do `COMUNIDADE-E-ESTRATEGIA.md` |
| Fatos da conta, funil, telas do quiz, links do story, contatos | `FATOS-DO-ALUNO.md` |
| Lições do Flow, dos prompts, do painel e do CapCut (checklist 1 a 34) | `LICOES-FLOW-E-PROMPTS.md` |
| Discord, DMs, aulas, estratégia | `COMUNIDADE-E-ESTRATEGIA.md` (conversas inteiras em `HISTORICO-DISCORD/`, lidas até 02/11 19h59 no chat-appyon e 21h08 no vitórias-dólar) |
| Funil de Manifestation e a VSL | `BRIEFING-MANIFESTACAO.md` e `ANALISE-FUNIL-MANIFESTATION-VSL.md` (com a VSL inteira em inglês) |
| Aulas | `AULA-IORHAN-30-10-COPY-QUE-CONVERTE.md` (P42) e `AULA-07-09-ANALISE-DE-FUNIL.md` |
| Quando insistir, trocar gancho, copy ou avatar; perfis novos | `VALIDACAO-CONTA-E-AVATAR.md` |
| Números de cada vídeo e o diário das leituras | `METRICAS-NORA.csv` e `METRICAS-NORA-LEIA.md` |
| Peças geradas e postadas | `BIBLIOTECA-DE-TAKES.md` |
| Vídeos de referência, pré-ganchos, provas reais | `BIBLIOTECA-VIDEOS-VIRAIS.md`, `BIBLIOTECA-PRE-GANCHOS.md`, `PROVAS-REAIS-TRUSTPILOT.md` |
| Roteiros e painéis | `ROTEIRO-NORA*.md`, `PAINEL-NORA*.html`, `PAINEL-FACE01.html`, `PAINEL-FACE02.html`; reserva do próximo corpo em `RESERVA-ROTEIRO-CORPO-C-TEMPO-PASSANDO-PORTAL-1111.md` |
| Doc do MVM (curso, Appyon, contas, custos, dicas) | `PLANO-MVM-LEGACY-APPYON.md` |
| Dashboard, skill, ferramentas | `ferramentas-painel/dashboard/`, `ferramentas-painel/skills/`, `ferramentas-painel/ferramentas/LEIA.md` |

Os vídeos e prints que o aluno mandou ficaram só nas sessões antigas; a análise de cada um está nos arquivos acima. Se a sessão nova precisar rever algum, o aluno manda de novo.

## 5. Links da conta de 30/10 (só abrem naquela conta; não são mais atualizados depois da passagem)
- Dashboard Métricas da Nora: https://claude.ai/artifact/7ZArpHDLZZcuA8DPEMAZGR (asset do CSV `/_blob/64869fe38eb4e2785b6ada83736434bd`, dataset na versão 26)
- Doc Plano MVM Legacy – Appyon: https://claude.ai/artifact/HsK6QVZRWUK1pdD2xi7JfF
- Painéis: nora44 https://claude.ai/artifact/SY78kS7dxiSFjrBFnoogxj · nora45 https://claude.ai/artifact/WzqX4wBDdeZo9G1dSHc8Bx · nora46 https://claude.ai/artifact/W6EBF2bdfPQ6YhCM4MaEF1 · **nora47** https://claude.ai/artifact/SoyRmVkQWNAEVXQ9mwtg5K · **nora48** https://claude.ai/artifact/CAbhHw2pxw6N3ytWS46Bwj · **nora49** https://claude.ai/artifact/1N7U8uiBXuEgKGwH3hE84s · face01 https://claude.ai/artifact/MUke2u5Yx5ELCnQ5jv5ULn · face02 https://claude.ai/artifact/KeXyFoszrLZx7BZr42765U
- Conta contatocaram (27 a 30/10, só para ver): dashboard https://claude.ai/artifact/CTdhXsH5PoQFRCnzpbM4wy, doc https://claude.ai/artifact/Dd3bgq9RuSKyoKT2z2bLh6.

## 6. Estado em 03/11/2026 (o que a sessão nova pede ao aluno)
- **Últimos posts:** nora46 (corpo B) em 31/10 às 18h30 (Insta e Face); nada em 01/11; em 02/11 o **story-0111 às 21h10** e o **face02 às 21h13** (Insta e Face; imagem parada de 5 s com o texto do face01). O story-0111 **vence ~21h10 de 03/11**.
- **Plano de 03/11 (horários fixos 17h, 19h30, 22h, 00h30):** nora47 às 17h, nora48 às 19h30, nora49 às 22h (cada um gera só o Take 1: 15 créditos, conta grande). Story novo ou repost **antes das 21h10** (proposta: "Tap below: pick 3 cards for your free private reading before 11:11.", adesivo "Pick my 3 cards"). O 4º horário (00h30) fica para o nora50, que ainda não existe: fala nova pede a leitura obrigatória completa antes (candidatos: o próximo corpo com o gancho dos sinais da VSL, ou uma fita com o texto da aula).
- **Pedir ao aluno:** leituras do face02 com ~12 h e ~24 h (Insta e Face); leitura final do nora46, nora43, nora44, nora45 e face01 no Insta, **sempre com quantos comentários são de outras pessoas**; números do story-0111 (viewers e cliques); Tracker de 31/10 a 03/11; saldo de créditos das duas contas do Flow; se conferiu de uma conta que não é admin o comentário com link do face02; a aula de 02/11.
- **Régua do corpo B:** com ~24 h de cada vídeo (nora47 a nora49), comentários de outras pessoas ÷ views (2,5%+ bom; só com 300+ views), seguidores e cliques no Tracker. Ângulo só se troca depois de 10 a 15 vídeos.
- **Datas:** GeeLark vence em 05/11 (~US$ 5) e a proxy da Nora em 06/11 às 14h52 (~US$ 3,59; renovar a mesma e conferir se o GeeLark conecta). Janela dos 40 vídeos da Nora fecha ~06 a 08/11 (decisão do 2º perfil ou avatar nova depois disso). Portal 11:11 em 11/11: até lá, todo vídeo fecha no portal.
