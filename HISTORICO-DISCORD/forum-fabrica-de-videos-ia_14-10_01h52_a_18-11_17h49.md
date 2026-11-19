# Fórum: post "🏭 Fábrica de Vídeos com IA — tutorial passo a passo (do zero ao lote automático)" — conversa completa

Canal: #📝︱fórum-appyon › 🏭 Fábrica de Vídeos com IA · servidor MVM Legacy
Período: 14/10/2026 01h52 até 18/11/2026 17h49 (leitura feita em 19/11 às 00h30)
Total: 101 mensagens, na ordem do canal (o post original é a 1ª, as outras são os comentários). Horário de Brasília. Imagens e anexos no zip imagens-discord_19-11.zip.


## 14/10/2026

**01h52 · João [MVM]**
O que é É NECESSÁRIO LER ATÉ O PASSO 3
,
Uma esteira que transforma uma copy + uma persona em vídeos  prontos pra postar. Robôs operam as ferramentas pelo navegador e um analista confere cada vídeo antes de liberar.

Por que gasta pouco token: a IA (Claude Code / Codex) só constrói e conserta os scripts. Quem produz os vídeos são os scripts, rodando no seu PC sem IA.


O fluxo
,
SPY → copy → voz → imagens → gancho (5s) → avatar falando → edição → controle de qualidade → entrega


O que precisa
,
PC: mínimo 4 núcleos, 8 GB RAM, SSD com 100 GB livres · recomendado 6 núcleos, 16 GB, SSD 250–500 GB. Não precisa de placa de vídeo boa (o pesado roda na nuvem). Internet de 20 Mbps pra cima. ( caso o seu pc não atenda os requisitos mande a IA se virar e tentar otimizar(é serio pode funcionar)
Contas pagas (o custo real): HeyGen (avatar), ElevenLabs (voz), Google Flow (imagem e vídeo curto).
Pra construir: Claude Code ou Codex.

Custo por vídeo (referência): imagens 0 · gancho ~12 créditos Flow · avatar ~4 créditos HeyGen · edição e conferência 0.

 O arquivo CONSTRUIR-FABRICA-DE-VIDEOS.md vai anexado no tópico — é ele que você entrega pra IA.



Passo 1 — Instalar (tudo grátis) (  A IA INSTALA PRA TI NO .MD)
,
Node.js 20+ (nodejs.org → LTS)
,
Python 3 (marque Add Python to PATH)
,
FFmpeg → no terminal: winget install ffmpeg
,
Google Chrome
,
Claude Code ou Codex
,
Teste no terminal: node -v · python --version · ffmpeg -version


Passo 2 — Contas CASO ESTEJA COM PREGUICINHA MANDE A IA FAZER ISSO
,
• HeyGen/Muse/FLOW: crie um avatar por foto para cada persona, com a voz dela
• ElevenLabs: escolha a voz e gere uma chave de API
• Flow: tenha uma imagem de rosto de cada persona (referência de identidade)
 Tenha uma 2ª conta do Flow para quando os créditos da primeira acabarem.
Imagem: imagens/forum-fabrica_2026-10-14_01h52_JoaoMVM_1.jpg — Ilustração de capa: bicho-preguiça de óculos e moletom com notebook, cercado de telas de automação, braços robóticos, banco de dados e nuvem. Sem texto.

**01h57 · João [MVM]**
Passo 3 — Pasta do projeto
,
Crie uma pasta vazia (ex.: fabrica)
,
Coloque o CONSTRUIR-FABRICA-DE-VIDEOS.md nela (pode renomear para CLAUDE.md ou AGENTS.md)
,
Defina suas personas: idade, aparência marcante, roupa, cenário e estética da capa
,

 Regra de ouro: nunca coloque senha ou chave dentro do código. Chave vai no .env e o login nas contas é sempre você que faz.


Passo 4 — A primeira ordem
,
Abra o Claude Code/Codex na pasta e mande:

Leia CONSTRUIR-FABRICA-DE-VIDEOS.md e construa a fábrica seguindo os marcos, um de cada vez. Ao terminar cada marco, rode o teste dele e me mostre o resultado antes de seguir.

Um marco por vez, testado. Não peça tudo de uma vez.
(OS MARCOS SÃO APENAS PRA VOCÊ SABER O QUE ELA ESTA FAZENDO A PARTIR DAQUI VOCÊ NÃO FAZ NADA ELA QUE FAZ TUDO SOZINHA)

 Passo 5 em diante é apenas relatório do que ela faz MUITO resumido só para curiosos, mas pra vc que quer saber de rodar é so colar .md e ja era.


Passo 5 — Chrome e config (Marco 1)
,
A IA cria um Chrome com perfil próprio → você loga no HeyGen, Flow e ElevenLabs uma vez → preencha o config.json (personas, avatares, rosto no Flow, voz, limite de vídeos com data por conta).


Passo 6 — Voz e transcrição (Marcos 2–3)
,
Teste: gerar um áudio de 15 s e transcrever. "two two two" tem que virar 222 na legenda.


Passo 7 — Imagens e gancho (Marcos 4–5)
,
• 3 imagens por vídeo: início do gancho, corpo (olhando pra câmera) e capa
• Realismo: pele fosca com poros, rugas pela idade, mãos com 5 dedos. Sem "8K" e sem "hyper-realistic" (dá cara de IA)
• Gancho de 3-5 s, sem fala, só som ASMR, com algo absurdo e inesperado ligado ao tema no 1º segundo
• O robô precisa conferir a conta logada e parar se acabar o crédito

**01h59 · João [MVM]**
Passo 8 — O primeiro vídeo (Marcos 6–7)
,
O avatar fala no HeyGen (o robô envia e depois baixa em 4K) → o FFmpeg(OU Auto editor) monta: gancho, riser, avatar, legendas curtas, texto no topo e música baixa, em 1080×1920. Assista inteiro e ajuste.


Passo 9 — Primeiro lote (Marcos 8–10)
,
• Analista: compara a fala com a copy, confere data, legenda, tela preta e congelamento. Teste com um vídeo errado de propósito, que tem que ir pra REVISAR.
• Um comando = a mesma referência pra várias personas → PRONTOS/<data>/<conta>/ com a capa ao lado
• Ative a limpeza automática (senão o disco enche)


Passo 10 — Fila de madrugada (Marco 11)
,
Um script em sequência: imagens → ganchos → avatares → lote. Roda sem IA = 0 token. Deixe o PC sem hibernar e a janela do Chrome NÃO minimizada.


 Problemas comuns
,
• Gancho na conta errada → o robô confere o e-mail antes de cada pedido
• "Sem créditos" → troque pra 2ª conta; o lote retoma de onde parou
• Flow recusou o prompt → troque o elemento barrado
• HeyGen "sem rosto detectado" → use uma foto mais de frente (não cobra)
• Legenda com "□" → tire o emoji
• Robô não baixa o que já gerou → o Chrome estava minimizado
• Travou? Olhe a tela primeiro: conta, créditos e erro

 A IA constrói, os scripts produzem, você decide. SPY, copy e estratégia continuam com você.

**02h03 · João [MVM]**
https://drive.google.com/drive/folders/1dvXWaSBrPxKZT63pIW1XXIqHlz8HUZmR?usp=sharing Arquivo .md + aula em vídeo mostrando o processo, mas como falei é simples só mandar .md a aula é so a teoria de tudo
Timestamps aula 01:

00:00> 17;36 TEORIA
17;36> 27;14 Ensinando como usar pra spy e aplicar o .md no claude ou codex.
27;14> 32:20 Resultado com tudo criado por ela e criação de avatar por ela ou seja um video pronto
32.20>34;33 Organização de pastas  e criação de preset
34;33+ O que se esperar dela pronta, como ela ta rodando escritorio virtual e etc
Prévia de link: Google Drive
Links desta mensagem:
- https://drive.google.com/drive/folders/1dvXWaSBrPxKZT63pIW1XXIqHlz8HUZmR?usp=sharing

**02h03 · João [MVM]**
Resultado esperado
Imagem: imagens/forum-fabrica_2026-10-14_02h03_JoaoMVM_1.jpg — Infográfico "OPERAÇÃO AUTOMATIZADA – Como funciona a esteira. A IA faz o trabalho braçal. Você fica com o que escala: SPY, copy e estratégia." O CÉREBRO: Você — estratégia (analisa relatórios, aprova, dá ideias; copy e SPY nunca 100% na mão da IA). INTELIGÊNCIA: SPY automático (monitora perfis escalados, acha virais, transcreve e analisa a estrutura) → Banco de dados (Supabase guarda referências, copies, estruturas e ganchos) → Criação (novas copies, ganchos visuais e avatares a partir dos padrões). GERENTE IA: "A gerente da operação – tem voz própria, administra o PC e as tarefas, roda a rotina todo dia sem comando e encaminha tudo para a fábrica" (fala com você, distribui tarefas, avisa no WhatsApp). FÁBRICA DE PRODUÇÃO: robôs Node.js + Playwright: 1 Voz (ElevenLabs), 2 Imagens + gancho (Google Flow), 3 Avatar falando (HeyGen), 4 Edição (FFmpeg + faster-whisper), 5 Controle de qualidade (analista automático), 6 Pronto para postar (separado por dia e conta). Escritório ao vivo (painel em pixel art com cada agente trabalhando). "Quase tudo roda local → gasto de tokens baixo. Construído com Claude Code + Codex."

**03h42 · João [MVM]**
Repositorios para criação do escritório virtual: (Opcional, serve para entender melhor o que eles estão fazendo)

Os dois repositórios que usamos no escritório pixel:


Pixel Agents
,
 https://github.com/pixel-agents-hq/pixel-agents

É um “escritório em pixel art” para agentes de IA, em que cada agente aparece como um bonequinho trabalhando numa mesa.



Universal LPC Spritesheet Character Generator
,
 https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator

É um gerador de personagens em pixel art feito pela comunidade Liberated Pixel Cup, com milhares de peças combináveis (corpo, cabelo, roupa, acessório) e animações prontas de andar, sentar, digitar e outras.
Prévia de link: GitHub GitHub - pixel-agents-hq/pixel-agents: Pixel office. Pixel office. Contribute to pixel-agents-hq/pixel-agents development by creating an account on GitHub.
Prévia de link: GitHub GitHub - LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Gene... Character Generator based on Universal-LPC-Spritesheet - LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator
Links desta mensagem:
- https://github.com/pixel-agents-hq/pixel-agents
- https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator

**15h55 · Ewerton Itonaga**
> respondendo a: @João Passo 3 — Pasta do projeto , Crie uma pasta vazia (ex.: fabrica) , Coloque o CONSTRUIR-FABRICA-DE-VIDEOS.md nela (pode renomear para CLAUDE.md ou AGENTS.md) , Defina suas personas: idade, aparência marcante, roupa,
Muito Top, eu subi aqui para ver, mas eu estava com um problema de geração, e pensei que talvez sua forma era diferente, mas no primeiro teste já deu ruim aqui, o FLOW está bloqueando a geração dos videos, e não estou enviando varios não, somente 1 por vez, se tiver alguma dica ai?
Imagem: imagens/forum-fabrica_2026-10-14_15h55_EwertonItonaga_1.png — Erro do Google Flow: "Notamos uma atividade incomum. As extensões do navegador que modificam a página podem causar problemas. Acesse a Central de Ajuda (support.google.com/flow)…" Botão "Tentar de novo".

**16h08 · João [MVM]**
> respondendo a: @Ewerton Itonaga Muito Top, eu subi aqui para ver, mas eu estava com um problema de geração, e pensei que talvez sua forma era diferente, mas no primeiro teste já deu ruim aqui, o FLOW está bloqueando a geração dos video
Cara que tremendo azar basicamente o flow identificou alguma automação e bloqueou faz parte, o certo pra complementar isso é conectar por API o flow mas ai sai muito caro, o que vc pode fazer é mudar a conta e usar em um chrome limpo sem extensoes ou algo do tipo

**16h08 · João [MVM]**
mas não fica repetindo isso como deu o erro nessa mesma conta pq ai pode dar b.o

**16h18 · João [MVM]**
pode ser que o seu esteja gerando por PRINTSCREEN invés de codigo, vou te mandar esse prompt pra reforçar ele a gerar por coisa que já era pra ta gerando

**16h21 · João [MVM]**
https://drive.google.com/file/d/1XdXTywi3HQx2koYfpSxJk2XouOdsd_41/view?usp=sharing baixa ai e joga nele, mas não comenta sobre o erro pq vc vai ta burlando o flow e tem vez que ele  não vai querer fazer
Prévia de link: Google Docs Caso ele ainda faça por printscreen
Links desta mensagem:
- https://drive.google.com/file/d/1XdXTywi3HQx2koYfpSxJk2XouOdsd_41/view?usp=sharing

**16h21 · João [MVM]**
e faz isso em outra conta por segurança pq ficar repetindo isso é perigoso

**16h26 · Ewerton Itonaga**
> respondendo a: @João https://drive.google.com/file/d/1XdXTywi3HQx2koYfpSxJk2XouOdsd_41/view?usp=sharing baixa ai e joga nele, mas não comenta sobre o erro pq vc vai ta burlando o flow e tem vez que ele não vai querer fazer
já fiz varios testes, tudo com gmail e perfis de crhome diferentes, tudo zero sem extensão nenhuma, e cpmeçar a pedir video, já trava, acho q é IP

**16h26 · Ewerton Itonaga**
vc ta gerando como, no Flow mesmo?

**16h28 · João [MVM]**
É que assim vc precisa acompanhar e ver como ele ta fazendo isso pra ti, pq é pra ele rodar de acordo com aquele prompt tudo por codigo basicamente ele vai abrir seu chrome sozinho ( sem mexer mouse nem nada)  e vai clicar nas coisas ali tudo por codigo, pq a IA vai mapear sua tela, é como se ela se movesse por cordenadas entende?

**16h29 · João [MVM]**
e basicamente isso ela vai clicar e dar colando os prompt de geração, por isso o flow não me identifica por causa que é como se fosse eu mexendo

**16h29 · João [MVM]**
O que pode acontecer é a IA invés de fazer isso teimar e usar por printscreen, que é basicamente ela tira um print da tela identifica e vai mexendo e assume o seu PC mexendo no mouse e etc, ai qualquer empresa te pega

**16h30 · Ewerton Itonaga**
sim, mas foi desse jeito mesmo, estava usando a ferramenta que vc disponibilizou

**16h30 · Ewerton Itonaga**
dei acesso ao claude, ele que estava fazendo

**16h31 · João [MVM]**
A IA ta gravando um video de exemplo dela fazendo aqui mas é como eu falei ali, se não der pelo prompt.md ai acho que realmente ta indo por IP

**16h32 · João [MVM]**
no caso esse  novo que mandei ali

**16h34 · João [MVM]**
Ele lê a estrutura da página (o código do site) e clica direto no campo de texto, no botão de anexar e no botão de enviar, sem precisar “ver” a tela. Por isso a janela minimizada atrapalhou: com ela minimizada, o Chrome para de atualizar a página é assim que funciona isso pra heygen e qualquer outra ferramenta
Anexo: anexos/forum-fabrica_2026-10-14_16h34_JoaoMVM_1.mp4 — vídeo anexado ao post

**16h35 · João [MVM]**
A IA censurou mal pra cacete KKK mas é basicamente isso vai clicando sozinho se eles estão te pegando mesmo fazendo isso realmente é azar msm

**16h50 · João [MVM]**
Manda isso pra outra ia mais black tipo o gpt pq o claude vai se ligar, isso dai é algo mais violento pra burlar o sistema do chrome, basicamente ele vai acrescentar delay no clique do mouse  e vai remover a ''marca'' de robozao no seu chrome  e vai forçar vc a não minimizar o chrome

**16h53 · João [MVM]**
Talvez o gpt não aceite fazer ai tu faz manual ou faz com jailbreak, mas isso é bemmm alem pq aqui na minha ela não tem nada disso e ta indo de boa dessa forma é basicamente a forma mais forte pra nao ser pego, já que vai simular mt um huamno msm assim for pego ai realmente foi algo de ip, teria que colocar outro


## 15/10/2026

**15h21 · Amanda Bartolo**
> respondendo a: @Ewerton Itonaga Muito Top, eu subi aqui para ver, mas eu estava com um problema de geração, e pensei que talvez sua forma era diferente, mas no primeiro teste já deu ruim aqui, o FLOW está bloqueando a geração dos video
é por causa de script... eu usava uma extensão que não consigo mais usar por causa desse erro aí. o flow tá detectando robô. uma saída é você pedir pro claude ajustar o script para cliques e passos mais lentos. e a outra opção é pedir pro próprio claude fazer pra você (tem a extensão claude in chrome, que o próprio claude usa seu navegador; ou o navegador embutido do claude, que você loga lá e ele vai usando por lá)

**16h18 · Ewerton Itonaga**
> respondendo a: @Amanda Bartolo é por causa de script... eu usava uma extensão que não consigo mais usar por causa desse erro aí. o flow tá detectando robô. uma saída é você pedir pro claude ajustar o script para cliques e passos mais l
Boa tarde. a minha é uma ferramenta criada dentro do flow, sabe?, não tem extensão, esses prompts estão configurados dentro pra programação
Imagem: imagens/forum-fabrica_2026-10-15_16h18_EwertonItonaga_1.jpg — Tela do Flow em "Ferramentas" > Favoritos: card "FÁBRICA DE REELS – Você – Produção automatizada de vídeos UGC com controle total de avatar e cenário" (ferramenta criada dentro do Flow).

**16h20 · Ewerton Itonaga**
nessa parte, mas é isso , ele identifica muito pedido, e block

**17h04 · Amanda Bartolo**
> respondendo a: @Ewerton Itonaga nessa parte, mas é isso , ele identifica muito pedido, e block
pede pro claude fazer pra vc, ou pra ele usar um script mais lento. aqui eu faço assim... ele gera as imagens e os vídeos pra mim, pelo claude in chrome, e ai já baixa tudo no meu pc e depois edita

**17h11 · João [MVM]**
> respondendo a: A mensagem original foi excluída
esse script aqui ele faz isso que ela disse é o prompt pra jogar nele e colocar delay no mouse e etc

**18h15 · Zéff**
opa

**18h16 · Zéff**
alguem aqui ta usando o lower priority

**18h17 · Ewerton Itonaga**
> respondendo a: @João esse script aqui ele faz isso que ela disse é o prompt pra jogar nele e colocar delay no mouse e etc
Fala João, blz, eu sou leigo blz, eu sei que precisa desse delay, vou dar um exemplo, tenho uma automação aqui que eu consigo colocar deley nele manualmente, dai o mouse vai lá e clica e cola o prompt e o agente faz, o outro que eu tenho a ferramenta é no flow, então não aparece mouse, nem campo, nem nada, ele não usa o campo que fica na direita ali, a ferramenta já vai fazendo, e claro, vou pedir esse delay nessas ações, mas a pergunta e duvida que tenho, leigo tá, mesmo rodando internamente, vcs chamam isso de script?, pra mim são os prompts e os codigos, entendeu?, mas obrigado a vcs pela ajuda

**18h47 · João [MVM]**
> respondendo a: @Ewerton Itonaga Fala João, blz, eu sou leigo blz, eu sei que precisa desse delay, vou dar um exemplo, tenho uma automação aqui que eu consigo colocar deley nele manualmente, dai o mouse vai lá e clica e cola o prompt e 
Sim rodando internamente seria um script mas ai que ta mano, se essa ferramenta ai sua estiver rodando direto por codigo na pagina ela vai ser pega

**18h47 · João [MVM]**
mas capaz mano se tiver qualquer duvida pode mandar nem se apega, estamos todos aqui pra aprender

**18h51 · João [MVM]**
Isso vocês precisam tomar cuidado tipo:


O Flow olha como a requisição chega no servidor, não o que você faz na tela.

Quando você navega normal, o navegador carrega imagens, fontes, demora entre cliques e tem cookies de login. Quando você usa script (código que manda comando direto pro servidor), chega tudo rápido demais, sem carregar a página direito. O Flow vê isso e bane, porque detecta que não é humano navegando.

E isso é importante pq a forma que é pra ser executada ali nos prompt que passei é justamente dando comando pra IA mexer o mouse e clipar entende? se for usada de outra forma como por exemplo a IA enviando codigos pra fazer isso dentro do servidor o flow pega, pode ser que funcione mas a chance de ser pego é maior

**18h55 · João [MVM]**
Aqui ta uma tierlist mostrando os metodos de stealth que você pode usar, é bom saberem isso pra analisar se a IA faz isso corretamente
Imagem: imagens/forum-fabrica_2026-10-15_18h55_JoaoMVM_1.png — Tabela de métodos de automação (parte 1): "Seu método (CDP/DOM)" – Chrome real, selectors, sem screenshots – detectável: Média (falha em timing/mouse/visibility); "Puppeteer stealth-plugin" – patches webdriver, delays – Baixa-Média; "Browser real + extensão" – usuário real navega + extensão intercepta – Baixa; "CDP + stealth evasions" – remove flags, spoof properties – Baixa se fizer direito.
Imagem: imagens/forum-fabrica_2026-10-15_18h55_JoaoMVM_2.png — Tabela de métodos (parte 2): "Image/Sikuli" (screenshot → OCR → clicar) – ALTA, canvas/webgl fingerprint; "HTTP requests direto" – MUITO ALTA, TLS/header fingerprint; "Selenium básico" (webdriver visível, timing zero) – "GARANTE BAN".

**18h57 · Ewerton Itonaga**
> respondendo a: @João Aqui ta uma tierlist mostrando os metodos de stealth que você pode usar, é bom saberem isso pra analisar se a IA faz isso corretamente
Entendi, obrigado

**23h21 · Angelo Vinicius**
Aqui deu bom
Imagem: imagens/forum-fabrica_2026-10-15_23h21_AngeloVinicius_1.jpg — Foto da tela do escritório virtual em pixel art: bonecos em mesas com etiquetas "Concluído – Entrega", "Em espera – Edição", "Trabalhando – Flow", "Em espera – Qualidade"; legenda embaixo "Flow → Edição → Qualidade → Entrega". Abas do navegador incluem "Appyon Creato…".


## 16/10/2026

**12h29 · victor rhea**
@João daora demais mano, parabéns pelo trampo aí. Vou configurar aqui

**12h29 · victor rhea**
e obrigado kk

**20h13 · Maicon Dionis**
> respondendo a: @João Aqui ta uma tierlist mostrando os metodos de stealth que você pode usar, é bom saberem isso pra analisar se a IA faz isso corretamente
Irmao , que foda. vou fazer agora aqui no meu. só uma duvida, acha que da para fazer a automação para usar só o musi?  audio, video hook , videos com o audio . porque tenho umas 6 contas do musi ai coloca para roletar as contas .

**20h13 · Maicon Dionis**
acha que rola ?

**21h01 · João [MVM]**
sim pode tentar ai so avisa ali que vc n vai usar as outras ferramentas mas sim o muse

**21h01 · João [MVM]**
que é pra otimizar tudo isso pra ele

**21h22 · Maicon Dionis**
> respondendo a: @João que é pra otimizar tudo isso pra ele
é o que pensei . ai nao precisa de elevenlabs, heygen e nem o flow.

**21h23 · Maicon Dionis**
> respondendo a: @João que é pra otimizar tudo isso pra ele
show . mas ai eu sigo o passo a passo que voce mostrou ou altero ja desde o começo para ele funcionar somente com o muse?

**23h42 · João [MVM]**
manda o .md pra ele e junto com arquivo fala ''adapte isso levando em conta que irei usar o MUSE da META para criação dos videos invés das ferramentas citadas no prompt''


## 17/10/2026

**03h45 · Zéff**
pessoal e obrigatorio ter o claude?

**11h20 · victor rhea**
> respondendo a: @Zéff pessoal e obrigatorio ter o claude?
se tu tiver codex ou agy (antigravity da google) dá pra fazer.

É que claude code (especialmente opus 5.5) é o padrão de qualidade hoje, o codex gpt-astra-6 lá é pica e eu pessoalmente acho no mesmo nível do claude, só que os limites duram muito menos.

Com agy agora tem o Argon 4 que eles falam que é o novo modelo pica, mas só pra plano Ultra pra usar ele via agy, então pra plano pro tu tem o gemini 3.8 flash que é bom, só é lento e acho que gera um código bem ruim - tem o gemini 3.1 pro mas no que eu testei ficou bem fraco.

Dito isso, se puder pagar 110 reais por mês pra ter o claude, vai ser otimo, se não, ou paga GPT ou paga Google. ai tu escolhe

**11h20 · victor rhea**
agora se nao quiser gastar nada, ai nao posso te ajudar, mas talvez outros colegas tenham uma saída

**20h30 · João [MVM]**
> respondendo a: @Zéff pessoal e obrigatorio ter o claude?
Olha, obrigatorio não é tem outras opcoes como o codex ou outra IA como a antigravity que ele citou mas sinceramente claude poupa bastante tempo alem de ser bem barato e ele se paga muito rapido

**20h31 · João [MVM]**
1 venda ali ja cai 70 pila no seu bolso o claude acho q ta uns 100pila por ai se paga mt faci

**20h32 · João [MVM]**
mas se tu quiser ter algo de graça e bom ai tu teria que instalar uma LLM local porem sugaria MUITO do seu pc

**20h32 · João [MVM]**
e gastaria tempo fazendo isso por isso compensa mt o claude ou codex mas entre eles pegue o cladue

**20h37 · João [MVM]**
SKILLS BOAS PARA VC INSTALAR NA SUA AUTOMAÇÃO E ECONOMIZAR TOKENS

Ponytail
https://github.com/DietrichGebert/ponytail

Pacote de instruções para agentes de programação trabalharem de forma mais objetiva. Ajuda a evitar código desnecessário, excesso de planejamento, respostas enormes e soluções complicadas. Ele não reduz os tokens automaticamente, mas orienta o agente a gastar menos código e raciocínio em coisas que não trazem resultado.

OmniRoute
https://github.com/diegosouzapw/OmniRoute

Roteador para modelos de IA. Permite colocar diferentes APIs e modelos atrás de um único endpoint, criando regras de fallback, orçamento, compressão e escolha automática do modelo. É útil numa operação com vários agentes, mas só funciona nas aplicações configuradas para enviar chamadas por ele.

Graphify
https://github.com/bunkerlab-net/graphify

Transforma códigos, documentos e outros arquivos em um grafo de conhecimento. Ele consegue mapear componentes, dependências, conceitos e relações dentro de projetos grandes. Pode ser usado como uma memória estrutural da operação, facilitando perguntas como “qual agente depende deste serviço?” ou “onde está configurada esta função?”.

Agent Skills
https://github.com/addyosmani/agent-skills

Coleção de skills para agentes de programação. Inclui planejamento, depuração, segurança, testes, performance, documentação, APIs, interfaces, automação e revisão de código. As skills funcionam como manuais especializados que o agente carrega quando encontra determinado tipo de tarefa.
Prévia de link: GitHub GitHub - DietrichGebert/ponytail: Makes your AI agent think like th... Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. - DietrichGebert/ponytail
Prévia de link: GitHub GitHub - diegosouzapw/OmniRoute: Never stop coding. Free MIT AI gat... Never stop coding. Free MIT AI gateway: one endpoint, 359 providers (150+ free), 1200+ models Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cli...
Prévia de link: GitHub GitHub - bunkerlab-net/graphify: Rust reimplementation of Graphify ... Rust reimplementation of Graphify (Python). Contribute to bunkerlab-net/graphify development by creating an account on GitHub.
Prévia de link: GitHub GitHub - addyosmani/agent-skills: Production-grade engineering skil... Production-grade engineering skills for AI coding agents. - addyosmani/agent-skills
Links desta mensagem:
- https://github.com/DietrichGebert/ponytail
- https://github.com/diegosouzapw/OmniRoute
- https://github.com/bunkerlab-net/graphify
- https://github.com/addyosmani/agent-skills

**21h10 · Zéff**
funciona pro lower priority do flow tbm?

**21h10 · João [MVM]**
> respondendo a: @Zéff funciona pro lower priority do flow tbm?
sim a forma que tu vai gerar o video é bem tanto faz ali

**21h11 · Zéff**
se consegue gravar um video pra mim ver?

**21h11 · Zéff**
achei muito legal essa automaçao

**22h10 · Maicon Dionis**
> respondendo a: @João Repositorios para criação do escritório virtual: (Opcional, serve para entender melhor o que eles estão fazendo) Os dois repositórios que usamos no escritório pixel: Pixel Agents , https://github.com/pixel-agents-h
Men, e repositorio jogo junto na mesma conversa da automação?

**22h12 · João [MVM]**
> respondendo a: @Zéff se consegue gravar um video pra mim ver?
tem ali no drive a aula e no final eu mostro ela ali e tals

**22h13 · João [MVM]**
> respondendo a: @Maicon Dionis Men, e repositorio jogo junto na mesma conversa da automação?
isso joga la e manda ele colocar pra ti

**22h13 · João [MVM]**
isso é opcional mas eu coloquei hj nas minhas aqui

**22h22 · Zéff**
caramba joao

**22h22 · Zéff**
dei uma olhada de leve

**22h22 · Zéff**
mano

**22h22 · Zéff**
voce e muito foda

**22h23 · Zéff**
nunca vi um negocio desse na vida


## 18/10/2026

**00h50 · João [MVM]**
KKK é nois

**08h09 · Maicon Dionis**
> respondendo a: @João KKK é nois
cara da ficando foda, o desafio de fazer tudo no muse ta sendo manter a mesma voz. mas cara, vai ficar muito foda . valeu mesmo por criar essa parada e compartilhar

**12h17 · João [MVM]**
> respondendo a: @Maicon Dionis cara da ficando foda, o desafio de fazer tudo no muse ta sendo manter a mesma voz. mas cara, vai ficar muito foda . valeu mesmo por criar essa parada e compartilhar
Manda a sua IA ai conectar o Muse pela API do elevenlabs, ai tu pode gerar e manter a msm voz

**13h06 · Maicon Dionis**
> respondendo a: @João Manda a sua IA ai conectar o Muse pela API do elevenlabs, ai tu pode gerar e manter a msm voz
po vou tentar isso hoje.  mas uma duvida, a api do elevenlabs vai consumir os tokens que temos comprando o mental, ou a cobrança é diferente?

**13h23 · João [MVM]**
sim consome os toekns do mensal


## 04/11/2026

**19h34 · Cassia Y**
Caramba, bom demais, João!   Incrível a fábrica e obrigada pela generosidade em compartilhar algo tão TOP!


## 09/11/2026

**15h19 · Geisa Maria**
Oi, João! Onde eu baixo o arquivo CONSTRUIR-FABRICA-DE-VIDEOS.md que você cita no Passo 3? Quero testar com o Codex.

**16h14 · Maicon Dionis**
> respondendo a: @João https://drive.google.com/drive/folders/1dvXWaSBrPxKZT63pIW1XXIqHlz8HUZmR?usp=sharing Arquivo .md + aula em vídeo mostrando o processo, mas como falei é simples só mandar .md a aula é so a teoria de tudo Timestamps 
ola, Geisa. está no drive.


## 10/11/2026

**18h47 · João [MVM]**
Quem quer um caminho mais facil agora tem o grokbot ele faz tudo isso ai o primeiro plano mensal sai por 78 reais dps volta a 150 por ai to testando ele é bem bom mas ta gastando bastante token to tentando otimizar pra isso, pra quem ja ta fazendo da forma que falei n recomendo mt nao so se tu for fazer junto rodando os 2 ao msm tempo como to fazendo
Imagem: imagens/forum-fabrica_2026-11-10_18h47_JoaoMVM_1.png — Lista de bots no grokbot com tema Turma da Mônica: Cebolinha (principal), Chico Bento ("Rascunho: a pasta dos…"), Franjinha ("O levantamento de ganchos v…"), Magali ("O radar da manhã (10/11) ach…"), Maicão dos Reels, Zé ("Salvei essa regra para as próx…"), Rogerinho da Maldade ("Salvei a lista e passei a atualiz…"), Cascão ("Terminei a v1 do estudo de púb…").

**18h48 · João [MVM]**
ele tu cria varios bots, sim eu coloquei tematica turma da monica  , e ele tem o seu proprio pc nao pesa muito, e é bem rapido e inteligente dps mando o prompt que usei pra fazer mas é um prompt simples

**18h52 · Maicon Dionis**
> respondendo a: @João Quem quer um caminho mais facil agora tem o grokbot ele faz tudo isso ai o primeiro plano mensal sai por 78 reais dps volta a 150 por ai to testando ele é bem bom mas ta gastando bastante token to tentando otimizar
consegui fazer adaptado para o muse e ta suave.  esse grokbot é outro que mais pre frente preciso da uma olhada porque tava vendo o pessoal fazer um processo muito foda com ele, usando a parte de agentes com ele e code com o claude, mas tudo por ele. foda demais

**20h24 · Diogo**
Galera, boa noite! To querendo seguir o processo principal aqui para tentar poupar um tempo diante da rotina atual que tenho agora no inicio e ficar focado mais na estratégia e copy, como é o objetivo. Ainda ta funcionando o tuto para o flow?

**21h31 · Diogo**
Outra dúvida que tenho é que queria trabalhar com toda construção no flow. Lá ja tenho um avatar com voz pré configurada. Se puder dar um alô se preciso mudar parâmetros no código ou então se posso fazer após o projeto implementado em alguma config específica.


## 11/11/2026

**11h57 · João [MVM]**
sim ta funcionando padrão

**11h59 · João [MVM]**
> respondendo a: @Diogo Outra dúvida que tenho é que queria trabalhar com toda construção no flow. Lá ja tenho um avatar com voz pré configurada. Se puder dar um alô se preciso mudar parâmetros no código ou então se posso fazer após o pr
envia o codigo normal e avisa a IA que invés de fazer por heygen vc vai fazer tudo pelo FLOW que ela adapta pra isso, so se atenta na hora da criação pelo FLOW de verificar se ela vai estar fazendo por codigos via script de acordo com o prompt que mandei se tu ver ela tirando PRINT da tela pra enxergar o flow tu manda ela parar e fazer so em script,  pq o certo é ela> gravar a tela e entender cada lugar ali da tela e dps ela roda tudo por script sem mais tirar print e nem gravar nada

**12h05 · João [MVM]**
Caso o flow te pegar> https://drive.google.com/file/d/1d7LPtehl2zyGjUK4_hWNAaHbMWEOZBxT/view?usp=sharing manda isso pra IA mas nunca de a entender nas suas conversas que vc ta usando ela pra burlar o flow com automacao e etc pq ai o claude fica brabinho e nao faz mais nada
Links desta mensagem:
- https://drive.google.com/file/d/1d7LPtehl2zyGjUK4_hWNAaHbMWEOZBxT/view?usp=sharing

**12h07 · João [MVM]**
esse arquivo vai fazer com que ele coloque delay em mouse e simule melhor um usuario comum e mude algumas coisinhas no seu navegador pro flow nao te pegar, mas na cabeça do claude vc ta ''resolvendo um bug'' caso ele perceba que vc ta burlando o flow kkk ai tu da uma persuadida nele que o seu flow não gera mais nada pq deu um bug no navegador serio rolou com seus amigos tb se precisa disso pra poder trabalhar e sobreviver e se conversou com o suporte do flow e eles mandaram fazer isso mas vc não sabe mexer e blabla

**12h08 · João [MVM]**
Isso dai é mais pro claude, o gpt é parceria

**13h15 · Diogo**
Opa, blz! Obrigado! Vou tentar levantar e estou usando o gpt codex mesmo


## 18/11/2026

**14h00 · João [MVM]**
“Tenho uma automação na pasta AUTOMACAO-PUBLICADOR-LIMPO. Configure tudo para mim.

Leia primeiro o README.md e examine os arquivos antes de alterar qualquer coisa.

Suas tarefas:

Confirme que Node.js 22 ou superior e Google Chrome estão instalados.

Execute a instalação e os testes.

Pergunte somente:

o nome exato de cada página do Facebook;

o ID numérico de cada página;

qual pasta pertence a cada página;

intervalo desejado entre publicações;

limite diário por página.

Preencha o config.json com essas informações.

Organize as subpastas dentro de entrada.

Abra ENTRAR-NO-FACEBOOK.cmd para eu fazer o login manualmente. Não peça minha senha e não copie cookies ou tokens.

Execute primeiro TESTAR-SEM-PUBLICAR.cmd.

Confira a captura gerada em data/previews e confirme que a página, o vídeo e a legenda estão corretos.

Não ative publicação real sem minha autorização explícita.

Depois da autorização, altere allowPublishing para true e faça apenas uma publicação de teste.

Confirme o resultado no Facebook antes de iniciar o monitor.

Se o Facebook mudar de interface ou a página ativa não puder ser confirmada, pare. Não clique às cegas e não tente publicar em outra conta.

Nunca publique o mesmo vídeo duas vezes, mesmo que ele tenha sido renomeado.

Ao terminar, explique de forma curta:

o que foi configurado;

onde colocar novos vídeos;

como adicionar legendas;

como iniciar e parar o monitor;

o que ainda não foi possível verificar.

Importante: esta versão trabalha somente com Facebook Reels. Não diga que Instagram ou TikTok estão configurados.”

Quando estiver funcionando, coloque os vídeos MP4 na pasta correspondente dentro de entrada. Para uma legenda específica, a IA também pode criar um arquivo video.mp4.json ao lado do vídeo.

**14h02 · João [MVM]**
Só passar isso pra sua IA e ja era e faça isso ''Faça assim:

Baixe e extraia o ZIP em uma pasta.

Abra a pasta extraída e execute INSTALAR.cmd.

Depois, envie o prompt abaixo para sua IA — Claude Code, Codex ou outra IA que consiga acessar os arquivos do computador.

Quando a IA solicitar, você fará o login manualmente no Facebook.

Primeiro teste sem publicar. Só autorize publicação real depois de conferir que a página e o vídeo estão corretos.''

**14h02 · João [MVM]**
vai automatizar as publicação de facebook

**14h04 · João [MVM]**
Só tomem cuidado com mesmo eu passando isso ai pra vcs ela pode ser meio burrinha então tenha paciencia de explicar pra ela as parada, pq ela vai precisar gravar a sua tela interface pra botar em codigo dps

**14h07 · João [MVM]**
E outra baixem o OPENBOT> https://openbot.run/pt e conecta suas IA ai e manda a sua IA principal configurar a automação pra ficar em BOTS organizadas por cada função isso vai fazer com que economize mais token e o melhor vc vai ter uma interface bonita pra interagir com suas IA e poder conversar por celular, por exemplo ta na academia treinando e mandando elas fazer os trabalho e th falar com cada Bot separado mas recomendo so falar com o principal vai economizar uma grana bem alta pq o grok bot ai ta todo hypado mas com isso dai fica bem bom
Prévia de link: OpenBot OpenBot: uma equipe de agentes de IA no seu computador Um app de desktop gratuito que executa agentes de IA como uma equipe no seu próprio computador, com o plano do ChatGPT, Claude, Gemini ou Grok que você já paga, ou com seu próprio modelo.
Links desta mensagem:
- https://openbot.run/pt
- https://openbot.run/social/home.jpg
Imagem: imagens/forum-fabrica_2026-11-18_14h07_JoaoMVM_1.png — Canais do OpenBot criados em 12/11: "produção" (Víd…), "postagem" (Po…), "spy" (Radar de…), "geral" (Turma in…), todos com "Nenhuma mensagem ainda" e avatares dos bots.

**17h35 · Maicon Dionis**
> respondendo a: @João E outra baixem o OPENBOT> https://openbot.run/pt e conecta suas IA ai e manda a sua IA principal configurar a automação pra ficar em BOTS organizadas por cada função isso vai fazer com que economize mais token e o 
man, acha que usando aquele esquema de armazenas as apis frees que tem disponivel em um sistema que vi do github, acha que da para usar nesses bots? ou a entrega vai ser muito pior  que nem compensa .

**17h39 · João [MVM]**
> respondendo a: @Maicon Dionis man, acha que usando aquele esquema de armazenas as apis frees que tem disponivel em um sistema que vi do github, acha que da para usar nesses bots? ou a entrega vai ser muito pior que nem compensa .
Qual sistema? Tem vários mas a maioria  não compensa nesse caso específico

**17h40 · João [MVM]**
Pq ele já roda localmente no seu pc por script os bots são tudo scriptado então eles n gasta token

**17h40 · João [MVM]**
E o que Administra eles precisa ser um sistema melhor como claude ou códex da vida pela inteligência deles de gerir os bots pra doou a msm coisa

**17h41 · Maicon Dionis**
ahhh achei que os bots consumiam o token da ia tipo, gpt, claude

**17h41 · João [MVM]**
Mas esse adm gasta bem pouco token

**17h41 · Maicon Dionis**
showww então nao tem porque colocar outro sistema

**17h49 · João [MVM]**
Assim que fica os gastos basicamente so o adm ali que admnistra todos os bots que gasta token, os bot é uma miseria
Imagem: imagens/forum-fabrica_2026-11-18_17h49_JoaoMVM_1.png — Trecho de relatório: "Ou seja: o Big Boss no Opus representou aproximadamente 99,5% do custo medido." (o bot administrador é quem gasta token).
