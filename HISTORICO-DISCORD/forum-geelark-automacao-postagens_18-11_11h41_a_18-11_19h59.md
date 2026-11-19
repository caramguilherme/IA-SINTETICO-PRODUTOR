# Fórum: post "Economize 2h por dia automatizando suas postagens no Geelark" — conversa completa

Canal: #📝︱fórum-appyon › Economize 2h por dia automatizando suas postagens no Geelark · servidor MVM Legacy
Período: 18/11/2026 11h41 até 18/11/2026 19h59 (leitura feita em 19/11 às 00h30)
Total: 11 mensagens, na ordem do canal (o post original é a 1ª, as outras são os comentários). Horário de Brasília. Imagens e anexos no zip imagens-discord_19-11.zip.


## 18/11/2026

**11h41 · Adonias Dantas [MVM]**
O hook funcionou? Era a intenção 

Galera, há uma forma de automatizar as automações do Geelark. Isso mesmo "Automatizar as automações" e economizar horas do seu dia. 


 Como automatizar suas postagens no GeeLark com IA (sem saber programar)
,
Hoje eu não abro o GeeLark para agendar post. Eu escrevo uma frase para a IA, e ela:
• pega os vídeos na pasta certa
• sobe cada vídeo para o celular certo
• agenda com legenda, horário e selo de conteúdo de IA
• me devolve uma tabela com tudo o que foi agendado

Agendar 6 contas com 6 vídeos cada levava um tempão. Agora é uma frase e uma conferida.

Entendendo as peças (bem simples):
• GeeLark = os celulares na nuvem, onde ficam as contas
• Agente de IA = um assistente que roda no seu computador e consegue mexer nos seus arquivos (eu uso o Claude Code; outros agentes funcionam de um jeito parecido)
• MCP = o "cabo" que liga o agente ao GeeLark. Com ele, a IA manda os comandos para o GeeLark por você

O que você precisa antes de começar:
Conta no GeeLark com os celulares já criados (um celular por avatar)
,
Um agente de IA instalado no computador
,
Seus vídeos organizados em pastas (explico na parte 4)
,

Bora para a instalação 


 Parte 2: ligando a IA ao GeeLark (uma vez só)
,
Passo 1: criar o seu token
No app do GeeLark, vá em GeeHub → API e gere o seu GEELARK_TOKEN. 

Veja a imagem

 O token funciona como uma senha. Não cole ele no chat da IA, no Discord nem em print. A IA vai te mostrar onde colar, no seu computador.


Próximos passos nas próximas mensagens.....
Imagem: imagens/forum-geelark_2026-11-18_11h41_AdoniasDantasMVM_1.jpg — Print do app GeeLark em GeeHub > API: Connection "Active" (destacado), APP ID borrado, API Key "Generated" (Reset key), Bearer Token "Generated" (Reset token), Webhook URL, IP whitelist, documentação. Seção CLI ("The official GeeLark CLI tool") e seção MCP ("Use GeeLark MCP to control GeeLark directly through conversations in MCP-compatible AI tools like Codex, Claude, and Cursor") com o JSON: "GEELARK_BASE_URL": "https://openapi.geelark.com", "GEELARK_BROWSER_BASE_URL": "http://localhost:40185", "GEELARK_TOKEN": (borrado, com seta vermelha). Rodapé: 501/600 perfis, 10/∞ membros, plano até 25-12-2026.

**11h42 · Adonias Dantas [MVM]**
Parte 2: ligando a IA ao GeeLark (uma vez só)
,
Passo 1: criar o seu token
No app do GeeLark, vá em GeeHub → API → MCP e gere o seu GEELARK_TOKEN.

Você deve ver a parte BEARER TOKEN e clicar em Generate Token ou Reset Token

 O token funciona como uma senha. Não cole ele no chat da IA, no Discord nem em print. A IA vai te mostrar onde colar, no seu computador.

Passo 2: pedir para a IA instalar
Abra o seu agente de IA e cole o prompt oficial do próprio GeeLark (está na próxima mensagem). A IA vai:
• ler a documentação oficial
• conferir o seu computador
• te guiar um passo de cada vez
• pedir sua permissão antes de instalar qualquer coisa

Você só segue o que ela pedir. Se travar em algum passo, mande um print do erro para ela (sem mostrar o token).

Passo 3: testar
No fim, escreva para a IA:

Liste meus celulares do GeeLark


Se aparecer a lista dos seus celulares, está tudo ligado.

**11h42 · Adonias Dantas [MVM]**
Prompt oficial do GeeLark (cole no seu agente de IA)
,
Help me connect GeeLark MCP Server to the AI agent I'm using. Assume I'm new to this and walk me through setup one step at a time.

Start by reading the official GeeLark documentation:

https://github.com/GeeLark/geelark-cli/#use-as-mcp-server

Here's how I'd like you to help:

1. Go step by step. Don't give me a long list of commands or config files upfront. Explain only the next step, wait until I finish it, and use simple language.

2. Do as much of the setup as you can. First, check my computer and choose a suitable installation method. If you can make changes on my computer, ask before installing software or changing settings. If you can't, tell me exactly where to click and what to enter.

3. Help me enter the GeeLark token locally. In the GeeLark app, open GeeHub → API → MCP. Look for GEELARK_TOKEN. Show me how to enter it on my computer. Don't ask me to paste my real token into this chat.

4. Follow the official documentation. Don't guess at settings or use a third-party MCP server. If you can't access the docs, ask me to paste the relevant section.

5. Test the connection. When setup is complete, check that GeeLark MCP works by trying to retrieve my cloud phone list.

Most importantly, don't send me the entire setup process at once. Tell me only the first step for now.
Links desta mensagem:
- https://github.com/GeeLark/geelark-cli/#use-as-mcp-server

**11h42 · Adonias Dantas [MVM]**
Parte 4: como eu organizo as pastas
,
A IA só acha os vídeos sozinha se tudo tiver sempre o mesmo lugar e o mesmo nome. Este é o meu modelo (com nomes de exemplo):


Operacao/
├─ nicho-tarot/
│  ├─ avatares/
│  │  ├─ AV-01_luna-hart/
│  │  │  ├─ ficha.md          ← quem é o avatar (aparência, voz, estilo)
│  │  │  ├─ Video 12/         ← um lote de vídeos
│  │  │  │  ├─ criativo_001_H1.mp4
│  │  │  │  ├─ criativo_002_H2.mp4
│  │  │  │  └─ ... até 006
│  │  │  └─ Video 13/
│  │  └─ AV-02_mark-stone/
│  └─ producao/
│     └─ lote-1118.md         ← hooks, legendas e headlines do dia
└─ planilha.xlsx              ← registro de tudo que foi postado


Minhas regras:
• Uma pasta por avatar, com um ID na frente (AV-01, AV-02...)
• Uma pasta por lote de vídeos (Video 12, Video 13...)
• O arquivo criativo_00N usa o hook N. Assim eu sei qual vídeo é qual sem abrir nenhum
• No GeeLark, cada celular tem o nome do avatar. A IA cruza o nome da pasta com o nome do celular
• As legendas do dia ficam escritas no arquivo do lote. A IA lê dali, e eu não preciso colar nada

**11h43 · Adonias Dantas [MVM]**
Parte 5: horários quebrados + o pedido de agendamento
,
Por que quebrar os horários?
Robô posta às 12:00 cravado, todo dia. Gente de verdade, não. Quando várias contas postam sempre no minuto zero, fica com cara de automação.

Como eu faço:
• Horários base: 04h, 08h, 12h, 16h, 20h e 00h
• A IA sorteia o minuto entre 01 e 05, sem repetir o minuto do post anterior
• Cada conta tem o próprio sorteio

O resultado fica assim: 04:03, 08:05, 12:01, 16:04, 20:02, 00:05. Fica natural, e não precisa pensar em nada.

O pedido que eu mando para a IA (adapte para o seu caso):

Agende os 6 vídeos da pasta "AV-01_luna-hart/Video 12" no celular "Luna Hart" do GeeLark, para amanhã:
- criativo_001 às 04h, 002 às 08h, 003 às 12h, 004 às 16h, 005 às 20h e 006 à 00h do dia seguinte (horário de Brasília)
- minuto sorteado entre 01 e 05, sem repetir o minuto do post anterior
- legendas: as do arquivo producao/lote-1118.md, uma por vídeo
- nome de cada tarefa = ID do vídeo (AV-01-1118-01, -02...)
- marque o selo de conteúdo de IA
No fim, me mostre uma tabela com vídeo, horário e ID da tarefa.


 Na primeira vez, faça só 1 conta e confira no GeeLark (na lista de tarefas) se ficou certo. Depois mande todas de uma vez.

**11h43 · Adonias Dantas [MVM]**
Parte 6: a rotina e os cuidados
,
Minha rotina diária:
Produzo os vídeos e salvo na pasta do lote
,
Escrevo as legendas no arquivo do lote
,
Mando uma frase para a IA agendar
,
Confiro a tabela que ela devolve
,
Peço para a IA registrar os posts na planilha (assim eu sei depois qual hook vendeu)
,

Dica de ouro: depois que der certo a primeira vez, peça:

Salve esse processo num arquivo "como-agendar.md" para repetir igual da próxima vez


A partir daí, o pedido vira só: "Agende os vídeos de amanhã como sempre."

Cuidados:
 O token é senha. Nunca mostre a ninguém
 Confira sempre a tabela final antes de fechar
 Diga sempre o fuso horário (Brasília ou o horário dos EUA)
 Na minha experiência, não precisa ligar o celular para agendar: a tarefa roda sozinha no horário marcado
 Teste com 1 conta antes de mandar 10

Qualquer dúvida, manda aqui no fórum

**12h02 · Douglas**
Muito massa! Valeu por mandar, a questão de não precisar ligar o celular ainda usa os minutos? @Adonias Dantas

**12h14 · Adonias Dantas [MVM]**
Infelizmente usa, Douglas. Mas gastaria de toda forma, mesmo que você crie a automação manualmente no Geelark.

**17h51 · Vitor Garcia**
> respondendo a: @Adonias Dantas Infelizmente usa, Douglas. Mas gastaria de toda forma, mesmo que você crie a automação manualmente no Geelark.
voce ta usando proxy ip royal ou proxycheap? Pq eu tava agendando as postagens com a proxycheal e demorava demais e ai acabava a tarefa e não postava porque tava lenta a conexao

**18h21 · Adonias Dantas [MVM]**
Tô usando IPRoyal, Vitor

**19h59 · Vitor Garcia**
> respondendo a: @Adonias Dantas Tô usando IPRoyal, Vitor
e não da falha de postagem?
