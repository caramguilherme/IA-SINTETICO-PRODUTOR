---
name: leitura-discord-nora
description: Use quando o Guilherme mandar a leitura do Discord do MVM Legacy (os .md do chat-appyon e do vitórias-dólar, o zip de imagens e o resumo feitos pela skill leitura-discord-mvm) para registrar no projeto, decidir o que muda na Nora e sugerir quem responder.
---

# Registrar uma leitura do Discord

1. **Conferir se é novo:** comparar com `HISTORICO-DISCORD/` (md5) e com o marcador "Discord lido até" da seção 1 do `CLAUDE.md`. Arquivo igual a um já salvo: dizer que já está registrado e parar.
2. **Salvar:** os .md em `HISTORICO-DISCORD/` com o nome original sem o prefixo do upload; as imagens do zip em `HISTORICO-DISCORD/imagens/<período>/`. Conferir buracos: o 1º horário de cada arquivo tem de vir logo depois do marcador anterior.
3. **Ler tudo:** os 2 .md inteiros e o resumo; abrir as imagens com número (painéis de venda, Tracker, prints de configuração ou de copy).
4. **Antes de decidir, ler:** as últimas entradas do `COMUNIDADE-E-ESTRATEGIA.md`, o `CONTATOS-ALUNOS.md` inteiro e a seção do assunto no `PLANO-MVM-LEGACY-APPYON.md`.
5. **Registrar:**
   - `COMUNIDADE-E-ESTRATEGIA.md`: entrada "DD/MM - Discord, Nª leitura" com o que importa (vitórias com número e funil, dicas, avisos oficiais, problemas com solução) e **"Para a Nora (decisão minha)"**.
   - `PLANO-MVM-LEGACY-APPYON.md` (cópia principal do doc do MVM): cada item na seção certa (Funil Manifestation, Copy, Produção de vídeo, Estrutura de contas, Postagem, Números e resultados com funil, Regras e riscos, Aulas e links) e o parágrafo "Discord lido até". Nunca duas versões: o que for superado, corrigir.
   - Regra nova do Flow ou do painel → `LICOES-FLOW-E-PROMPTS.md`; fato de contato → `FATOS-DO-ALUNO.md`.
   - Marcador "Discord lido até" na seção 1 do `CLAUDE.md`.
6. **Quem responder (P44, item 6; obrigatório):** até 3 ou 4 mensagens: pergunta sem resposta que a Nora já sabe responder com certeza, vitória de quem ajudou ou de quem está na fase da Nora (#vitórias: só parabéns + 1 pergunta curta), pedido de conversa de colega. Texto pronto no jeito do aluno (minúsculas, vc, tb, pra, kkk), com linhas de verdade, dizendo onde responder (canal e a mensagem). Anotar no quadro do `CONTATOS-ALUNOS.md` como enviado. Nada inventado: o que não sabemos fica de fora e é dito.
7. **Commit e push.** Resposta ao aluno: o que muda na Nora (curto), as respostas prontas e os horários de partida da próxima leitura (a última mensagem de cada canal).
