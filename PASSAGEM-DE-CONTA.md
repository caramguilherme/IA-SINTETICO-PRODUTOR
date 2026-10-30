# Passagem para a outra conta do Claude (30/10/2026)

O aluno vai continuar o projeto da Nora em outra conta do Claude Code, que já tem o repositório do GitHub instalado. Este arquivo diz o que a sessão nova faz primeiro. **Todo o conhecimento do projeto está no repositório** (regras, lições, estratégia, fatos, métricas, roteiros, painéis, histórico do Discord). Fora dele ficam só os Artifacts publicados nesta conta (painéis, dashboard e o doc do MVM), que a conta nova não consegue editar e por isso recria a partir dos arquivos daqui.

**30/10/2026 ~11h50 (aluno: "pode"): todo o trabalho também foi levado para a `main`** (fast-forward, sem mudar nada). A sessão nova que começar na `main` já tem tudo; trazer a branch abaixo continua valendo e não muda nada se já estiver igual.

## 1. Mensagem para colar na sessão nova (o aluno cola isto como primeira mensagem)

> Sou o Guilherme. Estou trazendo o projeto da Nora de outra conta do Claude. Todo o trabalho está na branch `claude/loving-lamport-uuuom5` do repositório `caramguilherme/ia-sintetico-produtor`. Primeiro traga essa branch para a sua: `git fetch origin claude/loving-lamport-uuuom5` e `git merge origin/claude/loving-lamport-uuuom5`. Depois leia o `PASSAGEM-DE-CONTA.md` e a seção 0 do `CLAUDE.md` (o item "ONDE PARAMOS" mais recente) e siga o passo a passo da passagem: recriar o dashboard "Métricas da Nora" igual ao de hoje e recriar o meu doc "Plano MVM Legacy – Appyon". No fim, me diga os links novos e o que falta para o plano de hoje.

## 2. Passo a passo da sessão nova
1. **Trazer a branch** (comando acima) e conferir que `CLAUDE.md`, `FATOS-DO-ALUNO.md`, `LICOES-FLOW-E-PROMPTS.md`, `COMUNIDADE-E-ESTRATEGIA.md` e `METRICAS-NORA.csv` chegaram. Anotar no `CLAUDE.md` (seção 0) o nome da branch nova da sessão: as próximas passagens partem dela.
2. **Ler antes de responder:** o `CLAUDE.md` inteiro (seção 0 primeiro), o `FATOS-DO-ALUNO.md` (nunca perguntar o que está lá) e o topo do `COMUNIDADE-E-ESTRATEGIA.md` ("Regras em vigor", atualizado em 30/10). Antes de qualquer roteiro ou painel, a leitura completa do `LEIA-TUDO-ANTES.md`.
3. **Recriar o dashboard "Métricas da Nora"** pela receita de `ferramentas-painel/dashboard/COMO-RECRIAR.md`: tipo Dashboard da conta, CSV sem o BOM como asset, os 4 documentos do banco (`store/` + `index.html`, que já tem o número em cima das barras). Trocar o link no `CLAUDE.md` (seções 0 e 3) e no `METRICAS-NORA-LEIA.md`.
4. **Recriar o doc "Plano MVM Legacy – Appyon"** como um Claude Doc a partir de `PLANO-MVM-LEGACY-APPYON.md` (exportado inteiro em 30/10/2026, ~450 KB, todas as seções). É grande: criar o doc com as seções de nível 2 e encher uma seção por vez. Se o conector de Docs não existir na conta nova, dizer ao aluno e seguir usando o arquivo do repositório.
5. **Skill do doc:** o aluno instala na conta nova a skill `doc-mvm-legacy` (arquivo `ferramentas-painel/skills/doc-mvm-legacy.zip`; no claude.ai, em Configurações, Capacidades, Skills, enviar o zip). Antes, a sessão troca no `SKILL.md` o link e os ids do doc pelos do doc novo, refaz o zip e avisa o aluno.
6. **Painéis:** os do nora25 ao nora43 estão no repositório (`PAINEL-NORA*.html`) e já foram postados; não precisam ser republicados. Os próximos são publicados na conta nova a partir do `PAINEL-MODELO.html` e dos scripts de `ferramentas-painel/` (os de 29/10 em `r2910/`, com `regerar_com_modelo.py`, `check.js` e `conferir_signos.py`). Se o aluno quiser consultar um painel antigo, republicar a partir do arquivo dele.
7. **GitHub:** se o envio falhar, o aluno conecta o GitHub e instala o Claude GitHub App na conta nova (já aconteceu em 26/10; `FATOS-DO-ALUNO.md`, GitHub).

## 3. Onde está cada coisa (para não perder nada)
| O quê | Onde |
|---|---|
| Regras do agente, onde paramos, links | `CLAUDE.md` (seção 0 = diário de decisões de 26 a 30/10) |
| Fatos da conta, funil, links do story, contatos | `FATOS-DO-ALUNO.md` |
| Lições do Flow, dos prompts, do painel e do CapCut | `LICOES-FLOW-E-PROMPTS.md` |
| Discord, DMs (Lucas, Matheus, Adão, Mattias, Thiago, Eduarda), estratégia e regras em vigor | `COMUNIDADE-E-ESTRATEGIA.md` |
| Quando insistir, trocar gancho, copy ou avatar | `VALIDACAO-CONTA-E-AVATAR.md` |
| Números de cada vídeo e o diário das leituras | `METRICAS-NORA.csv` e `METRICAS-NORA-LEIA.md` |
| Peças geradas e postadas (takes, hooks, imagens) | `BIBLIOTECA-DE-TAKES.md` |
| Vídeos de referência e pré-ganchos | `BIBLIOTECA-VIDEOS-VIRAIS.md` e `BIBLIOTECA-PRE-GANCHOS.md` |
| Roteiros e painéis | `ROTEIRO-NORA*.md` e `PAINEL-NORA*.html` |
| Doc do MVM (curso, Appyon, contas, custos, dicas) | `PLANO-MVM-LEGACY-APPYON.md` (cópia de 30/10) |
| Conversas do Discord, inteiras, de 20 a 30/10 | `HISTORICO-DISCORD/` (as leituras e decisões estão no `COMUNIDADE-E-ESTRATEGIA.md`) |
| Dashboard | `ferramentas-painel/dashboard/` |
| Ferramentas (transcrição, print de página, leitura do Miro) | `ferramentas-painel/ferramentas/LEIA.md` |

Os vídeos de referência (.mp4) que o aluno mandou ficaram só nesta sessão (são grandes). A análise de cada um está em `BIBLIOTECA-VIDEOS-VIRAIS.md`. Se a sessão nova precisar rever algum, o aluno manda de novo.

## 4. Links
**Conta nova (recriados em 30/10/2026 ~12h, branch `claude/lucid-planck-zz5ob8`):**
- Dashboard Métricas da Nora: https://claude.ai/artifact/7ZArpHDLZZcuA8DPEMAZGR (asset do CSV `/_blob/407220399bffc0eada95e89c4dd895af`)
- Doc Plano MVM Legacy – Appyon: https://claude.ai/artifact/HsK6QVZRWUK1pdD2xi7JfF (conferido linha a linha com `PLANO-MVM-LEGACY-APPYON.md`)
- Skill `doc-mvm-legacy`: `ferramentas-painel/skills/doc-mvm-legacy.zip`, já com o link do doc novo

**Conta contatocaram (só para ver, não são mais atualizados):**
- Dashboard: https://claude.ai/artifact/CTdhXsH5PoQFRCnzpbM4wy
- Doc: https://claude.ai/artifact/Dd3bgq9RuSKyoKT2z2bLh6
- Painéis: nora35 https://claude.ai/artifact/ERJ4RidnZeZyfj3JNq75FJ · nora36 https://claude.ai/artifact/YQPugZp8AjVxe7MTPrPivB · nora37 https://claude.ai/artifact/3HJDVrNnA5aW6rFt5RkjUx · nora38 https://claude.ai/artifact/XQH3xb4hdfCUucX6wMdhUV · nora39 https://claude.ai/artifact/VuLfrzqxYUMF696Ka1kXg9 · nora40 https://claude.ai/artifact/PWCTPWqbrYKXvqzHCJ3PD7 · nora41 https://claude.ai/artifact/BRUoE4pFqnWzGVCdhoZLNq · nora42 https://claude.ai/artifact/HzVWXJiyNpGHey53cyU8sH · nora43 https://claude.ai/artifact/SWAxQnxgWc8EAZxKvSVhjH

## 5. Estado em 30/10/2026 ~11h30 (o que a sessão nova pede ao aluno)
- **Dia 29/10 fechado:** Insta nora40 17h20, nora41 19h50, nora42 22h40, nora43 01h15 de 30/10; Face os mesmos + `nora39-VAR` às 16h27.
- **Leituras da madrugada de 30/10** (no CSV, no diário e no dashboard): nora41 (fita) 888 no Insta com 5h30 e 24% de EUA; nora40 (longo) 489 com 5 envios, 7 salvos e 3 seguidores; nora42 (fita + longo) 114 com 59% nos 3 s; Face nora41 265, nora40 234, `nora39-VAR` 232 (+1,3x), nora42 41.
- **Pedido ao aluno às 11h28 (ainda sem resposta):** prints do Insta dos 4 vídeos (Overview, Engagement e Audience), print da Biblioteca do Face, Tracker de 29/10 e de 30/10, números do story de 29/10, créditos das duas contas do Flow.
- **Discord lido até:** chat-appyon até **29/10 às 22h54** e vitórias-dólar até **30/10 às 00h21** (leitura feita em 30/10 às 00h55; arquivos em `HISTORICO-DISCORD/`, resumo e decisões em `COMUNIDADE-E-ESTRATEGIA.md`, seção de 30/10 ~01h). A próxima leitura começa depois desses horários.
- **Prazo do dia:** o `story-2810` vence às ~16h30 (Insta e Face): repostar ou fazer novo antes.
- **Plano provisório de 30/10** (fechar com os números): Insta 17h longo do corpo A (takes do nora40) com Take 1 novo de Câncer, Escorpião e Peixes, datas "October 30th, 31st or November 1st" (~15) · 19h30 fita na boca com outros signos (~12, conta de 53) · 22h e 00h30 longos com outro hook e outro Take 1 (~15 a 22 cada). Face: os mesmos 4 + a variação (espelho + filtro "Dias claros" 30% + 1,1x) do melhor vídeo. Créditos antes do dia: conta grande ~199, conta de 53 ~34.
