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
- **CTA do formato micro (R004 e R005, 18/10/2026):** um clipe só de 8 s e até 22 palavras, o mesmo nos dois vídeos: "Send this to yourself. Comment 222. Open my story, pick 3 cards, and see his possible face and when you might meet." (condensa a 6A e a 6B; sem as iniciais por causa do limite de palavras).

## Exemplos validados do curso MVM — CTAs orgânicos (17/10/2026)

Fonte: curso MVM (Mind · Values · Money), Copy Hub, aba CTAs: 21 chamadas para ação orgânicas (8 do Instagram, 7 do Facebook e 6 do TikTok). O aluno informou em 17/10/2026 que tudo o que vem do curso é validado e aprovado para uso; nenhuma regra do projeto o proíbe, exceto o que puder derrubar a conta na Meta. Os textos estão **como o curso entregou** (só em PT; o curso não traz versão em inglês). Mudanças minhas: só as marcas de uso.

**Como usar na Dana:**
- Estes CTAs são frases para o fim do vídeo. A 6B da Dana segue a regra do projeto: 1 ou 2 selos + tocar na foto do perfil + abrir o story, até 22 palavras, em inglês dos EUA. Usar estes CTAs como **banco de ações e de jeito de falar**, traduzindo e encurtando.
- **Ações que o curso usa** (podem ser os "selos"): comentar um número ou palavra-código (222, "rosto", "Alma", "sim", "Minha alma gêmea", ✨), comentar o signo, seguir o perfil, enviar o vídeo para si mesmo ou para uma amiga, compartilhar, dar dois toques na tela, curtir, deixar um coração, se inscrever, ler a legenda, tocar na foto do perfil, ver o story, usar o som.
- **Jeito de falar que se repete:** "reivindique/clame esta energia", "não foi por acaso", "o universo tem uma mensagem", "este é um sinal", "o destino sabia que hoje seria o dia". Liberado como tom.
- **Marcas:** [DM] promete mandar link por DM (na Dana o link fica só no story, regra do funil Love Chart); [SITE] e [LINK NA BIO] levam para fora do story; [ROSTO] promete rosto (o Love Chart não entrega: trocar por VENUS/pattern); [ATENÇÃO] pode gerar denúncia.
- **Pergunta de signo** ("Qual é o seu signo? Comenta aqui embaixo"): gera comentário e combina com o Love Chart, que parte da data de nascimento e do Vênus.
- **Comentário com palavra-código:** a palavra pode ser 222 (marca da Dana) ou VENUS; combinar a palavra do vídeo com a do comentário fixado.


### Instagram

**Instagram #1** [REF: o curso tem vídeo de referência]
- PT: Então, se você quer progredir para algo novo e saudável com essa pessoa, para ser capaz de abrir esse novo capítulo, acesse o meu site spiritualistpenelope.com para encomendar o caminho da alma gêmea comigo.
  - Marca: [SITE] manda para o site de outra pessoa; não usar o endereço

**Instagram #2**
- PT: Se esse vídeo apareceu pra você, não foi por acaso. O universo tem uma mensagem. Comente ✨ aqui que eu te mando o link da leitura completa na DM.
  - Marca: [DM] promete mandar link por DM; na Dana o link fica só no story

**Instagram #3**
- PT: Ele está prestes a lhe fazer algum tipo de proposta ou confissão nos próximos dias. Clame esta energia, siga esse perfil, comente o número 222 e mande este vídeo para você.

**Instagram #4**
- PT: A única coisa que você precisa fazer é comentar, e clicar na foto do meu perfil para responder três pequenas perguntas no meu teste de alma gêmea.
  - Marca: Já é o formato da Dana (comentar + tocar na foto do perfil).

**Instagram #5**
- PT: Comente "rosto", e clique na minha foto de perfil para ver sua resposta.
  - Marca: [ROSTO] no Love Chart trocar a palavra-código (por exemplo VENUS) e a promessa.

**Instagram #6**
- PT: Qual é o seu signo? Comenta aqui embaixo. Tem uma leitura esperando por você nos meus stories agora, as cartas revelaram algo sobre o seu amor esse mês que você precisa saber.
  - Marca: Pergunta de signo gera comentário; no Love Chart combina com "your Venus".

**Instagram #7**
- PT: Se esse vídeo chegou até você, não foi por acaso. Me segue e manda "rosto" na DM. Te mando o link gratuito agora mesmo.
  - Marca: [DM] [ROSTO]

**Instagram #8**
- PT: Reivindique essa energia me seguindo, comente 222 e também envie este vídeo para você mesmo, porque você está manifestando essa notícia incrível e bênçãos em sua vida. Reivindique a magia.


### Facebook

**Facebook #1** [REF: o curso tem vídeo de referência]
- PT: Confie em mim. Se você está vendo isso, está acontecendo. Tire alguns segundos para usar o som e interagir. Compartilhe e reivindique esta mensagem.

**Facebook #2** [REF: o curso tem vídeo de referência]
- PT: Mas antes disso, dê um 'gostei' neste vídeo e comente para reivindicar a energia. Você está pronto?

**Facebook #3** [REF: o curso tem vídeo de referência]
- PT: Mas antes disso, para se conectarem com a minha energia, dê dois toques neste vídeo. E para reivindicarem esta leitura de tarô, comenta aqui embaixo: 'Minha alma gêmea'.

**Facebook #4** [REF: o curso tem vídeo de referência]
- PT: Portanto, por favor, deixe um coração nos comentários para afirmar isto, e clique em 'gostei' (like), compartilhe e se inscreva no canal.

**Facebook #5** [REF: o curso tem vídeo de referência]
- PT: Curta o vídeo e leia a legenda para ver a descrição/resposta do tarô.
  - Marca: Leva à legenda; a legenda da Dana é agressiva e leva ao story.

**Facebook #6** [REF: o curso tem vídeo de referência]
- PT: Respira fundo. Dê dois toques na tela. Imagina o rosto dele e lê a legenda para ver a descrição.

**Facebook #7**
- PT: Você está manifestando uma notícia incrível. Bênçãos reais estão se movendo em direção à sua vida neste exato momento. Isso é um sinal, digite 222 e dê o próximo passo para receber o que o universo já separou para você.


### TikTok

**TikTok #1** [REF: o curso tem vídeo de referência]
- PT: Faça qualquer pessoa te amar. Traga seu ex de volta, link do feitiço na bio.
  - Marca: [ATENÇÃO] feitiço/amarração e "faça qualquer pessoa te amar" soam como promessa de controle sobre outra pessoa; risco de denúncia. O aluno decide.

**TikTok #2**
- PT: Uma oportunidade para conquistar o coração dele, mesmo que esteja frio, inseguro ou emocionalmente distante! Escolha o horóscopo dele no link da bio.
  - Marca: [LINK NA BIO] a Dana usa story, não bio.

**TikTok #3** [REF: o curso tem vídeo de referência]
- PT: Para aceitar, use este som e interaja 3 vezes IMEDIATAMENTE. Uma leitura gratuita está disponível no link da bio.
  - Marca: [LINK NA BIO]

**TikTok #4** [REF: o curso tem vídeo de referência]
- PT: E a prova de que esse vídeo é para você, é quando você clicar no botão verde e a segunda pessoa que aparecer ser da sua família. Agora é sua hora de brilhar, este é um sinal, digite 'sim' para reivindicar.
  - Marca: Específico do TikTok (botão verde); não serve para Instagram/Facebook.

**TikTok #5**
- PT: Isso não foi o algoritmo. Foi o universo querendo falar com você. Comenta aqui o seu signo, quero saber quem o universo trouxe até esse vídeo.
  - Marca: Pergunta de signo; combina com o Love Chart.

**TikTok #6**
- PT: O destino sabia que hoje seria o dia em que a sua alma finalmente receberia a resposta que estava procurando. Comente 'Alma' para receber a sua leitura.
  - Marca: Comentário com palavra-código.
