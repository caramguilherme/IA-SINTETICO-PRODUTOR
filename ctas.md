# Banco de CTAs — linha editorial UGC Pet

Válido para **roteiros novos a partir de 01/10/2026**. Os CTAs dos roteiros já aprovados permanecem como foram salvos. A linha TikTok Shop segue suas regras próprias.

## Atualização de 02/10/2026 — ponte específica para o Manual

Nos próximos roteiros, a conclusão apresenta uma miniobjeção real de execução. A parte A do CTA conecta esse detalhe a uma orientação que exista no Manual; a parte B pede a ação no estilo sorteado. Esta atualização substitui a exigência de copiar literalmente as matrizes abaixo nos roteiros futuros. As matrizes continuam como registro histórico e base dos quatro estilos, preservando os CTAs dos roteiros anteriores, inclusive S027.

- Sortear uma vez os estilos 1–4 sem reposição, como antes. Registrar por perfil tanto o número sorteado quanto as falas finais adaptadas em A/B, antes da aprovação.
- **Estilo 1:** receita apresentada como parte do Manual; ligar o detalhe de execução à orientação do material e manter chamada por comentário/direct ou bio.
- **Estilo 2:** comentário Receita como caminho para receber o Manual; explicar primeiro como o material ajuda no detalhe levantado e incluir convite para seguir.
- **Estilo 3:** repertório de mais de 100 receitas como oferta; conectar medidas ou preparo explicado ao tema e terminar com comentário e convite para seguir.
- **Estilo 4:** desejo de agradar o pet com receitas fáceis; conectar o Manual à dúvida prática e manter comentário Receita ou link na bio para adquirir.
- A adaptação acontece somente na fase de roteiro. Depois de aprovada, copiar a fala registrada literalmente nos prompts, sem retornar à matriz antiga nem sortear novamente.
- Humanização solicitada pelo responsável em 02/10/2026: preferir ponte em primeira pessoa, falando diretamente com o público (“para você acertar o ponto de primeira, deixei…”), em vez de linguagem de catálogo (“o Manual traz…”). Conectar medida e preparo ao detalhe da receita, com tom natural e pessoal, mantendo a chamada para adquirir e conferindo a leitura em até 10 segundos por parte. Esta preferência não autoriza reescrever os prompts já aprovados.
- Refinamento solicitado em 02/10/2026: a parte A deve responder ao erro de execução levantado na conclusão, com o mesmo vocabulário concreto (ponto, textura, medida ou formato). Evitar a oferta solta de variedade que não responde à objeção. A parte B usa chamada direta de compra; quando o Manual for vendido, esclarecer que o direct entrega o link ou os detalhes para adquirir, sem insinuar envio gratuito do ebook. Só prometer a receita e o detalhe específico quando confirmados no material. Preservar o estilo sorteado e a divisão A/B, sem novo sorteio na revisão.
- Não prometer orientações ausentes no Manual. Não inventar riscos de saúde nem reter uma instrução essencial de segurança para exigir a compra. O convite para seguir não deve afirmar um impedimento técnico da plataforma sem comprovação.
- Preservar as duas partes finais 5A/5B ou 6A/6B, cada uma com até 10 segundos de fala natural. Não usar a miniobjeção como CTA antecipado.

## Sorteio por roteiro

- Comunicação desde 03/10/2026: seguir `COMUNICACAO-VISCERAL-E-FALADA.md` ao adaptar os quatro estilos. A objeção deve evocar um detalhe físico real do preparo; a parte A responde ao mesmo detalhe com fala pessoal e apoio existente no Manual, e a parte B faz o convite transparente para adquirir. Não inventar experiência da persona, exclusividade ou promessa clínica. Essa regra não autoriza novo sorteio ou reescrita de CTA já aprovado na fase de prompts.
- Antes de escrever as falas de um roteiro novo, sortear os quatro CTAs abaixo **sem reposição** entre Mariana, Miguel, Vera e Rodrigo: cada perfil recebe um CTA diferente naquele roteiro. Usar `python src/draw_ctas.py IDENTIFICADOR-DO-ROTEIRO` na raiz do projeto; o resultado fica guardado em `data/cta-draws.json`.
- Registrar o resultado uma única vez no arquivo de desenvolvimento do roteiro, com perfil, número do CTA e falas finais divididas. Não sortear de novo na aprovação, na criação dos prompts ou na reconstrução do painel.
- As cenas de conteúdo, formato, fatos, ordem e durações continuam compartilhados pelos quatro perfis. A única variação de fala entre perfis é o CTA final; a voz e o figurino seguem a respectiva persona.
- O CTA ocupa exclusivamente a última cena: `5A/5B` em um roteiro de cinco cenas ou `6A/6B` em um de seis. Não criar mini CTA anterior nem uma cena narrativa extra.
- Nos roteiros anteriores à atualização de 02/10/2026, manter as palavras sorteadas como foram fornecidas. Nos próximos, escrever e registrar as duas partes adaptadas conforme a atualização acima; depois da aprovação, preservá-las integralmente. Ler A/B como um único texto, sem repetir nem omitir palavras. Cada parte deve caber naturalmente em até 10 segundos; ajustar a redação na fase de roteiro antes da aprovação, sem acelerar a voz.
- O Manual físico com a capa oficial já aparece discretamente na Imagem 2. A pessoa o pega ao mencioná-lo na parte A e mantém o mesmo exemplar na parte B. Nos CTAs que não dizem o nome do Manual na parte A, mostrar a capa ao dizer “manual”.

## CTA 1

**Parte A — 5A ou 6A:** `ESSA RECEITA É UMA DAS MAIS DE 100 RECEITAS QUE EU USO TODOS OS DIAS AQUI EM CASA. E A MELHOR PARTE É QUE TUDO ESTÁ NESSE MANUAL.`

**Parte B — 5B ou 6B:** `COMENTA RECEITA QUE EU TE ENVIO NO DIRECT OU CLIQUE NO LINK DA MINHA BIO. MAS CONFIRME QUE ESTÁ ME SEGUINDO PARA EU CONSEGUIR ENVIAR A MENSAGEM.`

## CTA 2

**Parte A — 5A ou 6A:** `SE VOCÊ COMENTAR RECEITA EU TE ENVIO O MEU MANUAL DE PETISCOS GOURMET DE GELADEIRA. COM VÁRIAS RECEITAS QUE VOCÊ CONSEGUE FAZER NA SUA CASA.`

**Parte B — 5B ou 6B:** `MAS VOCÊ TEM QUE ME SEGUIR ANTES, SE NÃO NÃO CONSIGO TE ENVIAR..`

## CTA 3

**Parte A — 5A ou 6A:** `EU TENHO UM MANUAL COM MAIS DE 100 RECEITAS DE PETISCOS GOURMET DE GELADEIRA QUE MEU PET AMA.`

**Parte B — 5B ou 6B:** `SE VOCÊ QUISER QUE EU TE MANDE COMENTE RECEITA, MAS VOCÊ TEM QUE ME SEGUIR ANTES, SE NÃO NÃO CONSIGO TE ENVIAR..`

## CTA 4

**Parte A — 5A ou 6A:** `Você ama seu pet, e quer agradar ele com receitas fáceis de fazer? Conheça o Manual do Petisco Gourmet de Geladeira, ele possui mais de 100 receitas`

**Parte B — 5B ou 6B:** `que seu pet vai amar, com ingredientes que você encontra na sua casa. Comenta Receita ou Clique no link da bio para adquirir.`

O CTA 4 era o CTA fixo do S025. Ele agora integra o sorteio, sem alterar o S025 ou qualquer artefato anterior.

## Dana — CTA de funil (17/10/2026; substitui os estilos do Manual neste projeto)

Sem Manual, sem capa e sem sorteio. O CTA continua em duas partes, cada uma com até 10 s e até 22 palavras:
- **A (ponte):** a virada ("You can.") e o que o story mostra: um desenho do possível rosto, as iniciais e quando vocês podem se conhecer, com "possível" e "pode". Sem nome do app, preço, pagamento nem comissão.
  - **A partir de 19/10/2026 (funil Love Chart; aviso oficial de 17/10):** a 6A diz o que o quiz faz, na ordem oficial: "a free quiz that finds your Venus sign, names your love pattern and shows your perfect match and the months love is most open for you", encurtado para caber em 22 palavras, com "astrology". Exemplo aprovado: "In my story, a free astrology quiz finds your Venus, names your love pattern and shows your perfect match." Sem desenho do rosto, iniciais nem data de encontro. A 6B continua com os selos e o story, sem DM. Para vídeos prontos com a 6A antiga, entregar só o take novo (arquivo TAKE-NOVO). Ver PROJETO-Dana.md, seção FUNIL LOVE CHART.
- **B (ação):** 1 ou 2 selos conforme o roteiro (comentar um código como 222 ou YES, salvar, mandar para si ou para uma amiga, seguir), e depois tocar na foto do perfil e abrir o story antes que ele suma em 24 h. Exemplo: "Save this: first seal. Comment 222: second seal. Then tap my profile photo and open my story before it disappears."
- Nunca prometer mandar algo por DM. O link está só no story.
