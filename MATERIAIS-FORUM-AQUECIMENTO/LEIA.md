# Fórum do MVM: o aquecimento automático no GeeLark (mandado pelo aluno em 16/11/2026 ~18h25)

> **Revisão de 17/11/2026 00h50: a automação fica fora para a Nora.** A aula 14 (1:43:23 a 1:43:32, conferida na transcrição) diz: "Tem que aquecer a conta antes e depois de postar? Não, pode entrar, postar e sair. O aquecimento você só tem que fazer no começo da conta." Em 17/11, a rajada à mão antes do nora68 (2 curtidas, 2 comentários e 1 seguir em 2 a 3 min) disparou a 2ª verificação facial (Clone R62, `CLONE-DO-GUSTAVO-RESPOSTAS.md`). O plano abaixo vale só para uma conta nova, nos primeiros dias. Se os planos "01 - 18:50" e "02 - 23:20" tiverem sido criados, apagar.

O aluno perguntou no #chat-appyon como fazer a automação de aquecimento (15h16) e trouxe os 2 posts do fórum, lidos pela skill `leitura-discord-mvm`:
- `forum-aquecimento-automatico.md`: o post do Delian, "Aquecimento AUTOMATICO de instragram NO GEELARK????", de 10/05 a 15/11/2026, com 468 mensagens. **Lido inteiro.**
- `forum-aquecimento-godmode.md`: o post do joanfran.co, "Programe Seu Aquecimento Apenas uma Vez e Vá Trabalhar #godmode", de 16/05 a 28/07, com 54 mensagens. **Lido inteiro.**
- `resumo-forum-aquecimento.md`: o resumo da skill.
- `imagens/`: as 72 imagens do zip (passo a passo, logs, erros). As descrições estão nos .md, e não abri cada uma.

**Os 4 vídeos que tinham ficado fora do zip chegaram depois (16/11 ~18h30, pasta do Drive do aluno) e foram vistos e transcritos inteiros:**
- a aula do #godmode (joanfran.co, 4min43);
- o passo a passo do victor rhea (1min48);
- o tutorial do Kaike de Lima, fixado pelo Gustavo (2min33);
- o vídeo da Manu Torres sobre a Página do Face (33 s).

Ficaram em `videos/`. Os dois pequenos são os originais; a aula (135 MB) e o do victor (33 MB) estão comprimidos, porque o GitHub não aceita arquivo acima de 100 MB, e os originais seguem no Drive do aluno (https://drive.google.com/drive/folders/18iybA2cevHveTD8iCXB0j4ngbnQTiG68). As telas, de 8 em 8 segundos, estão em `videos/quadros/`, e as transcrições inteiras em `TRANSCRICOES/2026-05-16-forum-aquecimento-geelark-videos.md`. O que eles mudam está na seção "O que os vídeos mostram", abaixo.

**Ficou sem ler:** o post da Mari, "Aquecimento AUTOMÁTICO de Facebook", porque não veio.

## Como faz (o post do Delian, 10/05)
1. GeeLark > Automation > Marketplace > **"Instagram AI account warmup"** > Add.
2. Cloud phone profile > Add > marcar o celular. O GeeLark avisa: **"Please set the App's language to English and do not change it."**
3. Preencher:
   - **PubDate**: a hora de começar;
   - **NumberOfVideosViewed**: quantos vídeos assistir inteiros;
   - **SearchKeyword**: a palavra de pesquisa, sempre em inglês.
4. Save. Na aba Logs aparece "Waiting for execution", depois "Executing" e no fim "Task completed".
- **O que a automação faz:** assiste vídeos inteiros e segue alguns perfis de vez em quando. Não curte nem comenta (para isso existe outra automação, que o Delian não acha necessária).
- **As regras:**
  - não abrir o celular enquanto roda, senão falha; o GeeLark pode ficar minimizado;
  - no post do Delian, a tarefa não repete sozinha e é preciso criar de novo a cada vez. **A aula do #godmode mostra o contrário: na versão atual dá para escolher "Diariamente" e repetir por uma semana** (ver a seção dos vídeos);
  - o agendamento nem sempre funciona;
  - precisa de perfil de celular (não desktop), com proxy e Android 13 ou mais.
- **Erros:**
  - "Proxy detection failed": reiniciar o celular dentro do GeeLark; se não resolver, tirar o proxy, reiniciar e pôr de novo; ou clicar 2 a 3 vezes na bolinha azul de executar de novo;
  - "Not logged in": o Insta não estava logado;
  - "Please set a time to publish": falta horário em algum celular;
  - o pedido de permissão de notificação do Insta trava a tarefa: aceitar uma vez;
  - "Insufficient": acabaram os minutos.
- **O custo em minutos do GeeLark:**
  - 25 a 30 vídeos gastam de 11 a 13,5 min (Marcos Passold);
  - 50 vídeos, ~27 min (André Costa);
  - 100 vídeos, de 30 a 47 min.
  - O pacote de 2.000 min sai por US$ 14 a 15.
- **O risco:** o Marcos Daniel (01/10) perdeu uma conta nova no 3º dia de vida, o 2º usando a automação, com 50 a 100 vídeos por vez: "suspeita de automação", deslogou e pediu selfie. O Delian respondeu que selfie é comum até em conta que vende e sugeriu testar uma conta no manual e outra no automático. O #godmode avisa: "temos que evitar ao máximo atividade de ser um robô… programem pra uma semana no máximo e vão checando diariamente".
- **O ganho relatado:**
  - o paklto tinha um shadowban por pôr o link na bio cedo demais; fez 30 min de aquecimento e o vídeo seguinte "voltou a pegar tração";
  - contas novas ganharam seguidores sem postar (Cela e Gui, Delian);
  - o Felps já disse que aquecer antes de postar aumentou a conversão dele (22ª leitura).
- **No Face:** existe o "Facebook Reels Account Warm-up" (GeeLark 4.3.9), mas o Delian avisa que o Face pode ver a conta "uma hora no Brasil, outra na China, outra nos EUA" e prefere aquecer o Face na mão. A Página é aquecida uma por uma.

## O que os vídeos mostram (vistos e transcritos em 16/11 18h40)
- **A aula do #godmode (joanfran.co, 16/05) corrige o "não repete sozinho":**
  - Na tela em português: Automação > Marketplace > "Aquecimento de conta do Instagram com IA" (o nome em português do "Instagram AI account warmup") > criar tarefa recorrente.
  - Em "Definir tempo em lote", ele escolhe **Frequência: Diariamente**, desliga o "Horário de publicação aleatório", põe o **Tempo de execução** (a hora) e a **Hora de início e de término** (17/05 00:00 a 23/05 00:00, uma semana). Assim, "vai ser postado diariamente".
  - Ele dá ao plano um nome com o número e a hora, nas Observações ("05 - 13:00"): "vocês são uma empresa".
- **Nada de 100 vídeos de uma vez:** "não é uma atividade muito suspeita… sempre 100 vídeos de uma vez só no dia? … Atividades em comum é shadow ban" (1:39 a 1:54).
  - Ele usa **20 a 30 vídeos por rodada**, com um número diferente em cada celular (23, 24, 25): "sempre bom que seja aleatório pra não virar uma atividade comum".
- **"Fractais de aquecimento e de pré-postagem" (3:38 a 4:06):**
  - São 5 rodadas na manhã: 6h, 7h45, 9h20, 12h e 13h.
  - A última termina antes de ele postar à mão, depois das 13h: "quando você for postar, a sua conta está aquecida".
  - Ele aquece todo dia, mesmo a conta que já está aquecida.
- **Quanto tempo leva (a tela de Registros da aula, 16/05):**
  - O teste das 21h22 levou de **23 a 33 min por celular**, para ~25 vídeos;
  - as rodadas das 19h40 levaram de 10 a 13 min;
  - 2 celulares deram "Not logged in" em 27 s.
- **O Kaike (10/05):**
  - O mesmo caminho em inglês, com o **Keyword manager**: ele cria um grupo de palavras ("CARTOMANTE", com soulmate e outras) e escolhe o grupo no SearchKeyword.
  - Com 100 vídeos, os Registros dele mostram **36 a 40 min** por conta.
- **O victor rhea (10/05):** o mesmo caminho, com 30 vídeos, o grupo "astrology", 3 celulares (Android 15) e "Waiting for execution" nos Logs.
- **A Manu (13/05):** filmou a Página dela ("Selena Tarot Cards") no PC, entrando no Reels como a Página e assistindo e curtindo os vídeos de cartomante até o fim. Pergunta: "é isso o aquecimento da Página?". A resposta do Delian está no post: a Página se aquece uma por uma, e ele faz o Face na mão.
- **Conferência com o post:**
  - O custo do Marcos Passold (25 a 30 vídeos = 11 a 13,5 min) fica abaixo do que a aula mostra (23 a 33 min para ~25 vídeos). Conto com **~25 a 30 min por rodada de 25 vídeos**, o número maior.
  - O "não repete sozinho" do Delian (10/05) era da versão antiga, ou de quem não usou o "Diariamente".

## O que serve para a Nora (decisão minha, revista em 16/11 18h40 com os vídeos; o aluno decide se liga)
- **O celular dela serve:** o "#4 GeeLarkPhone|Nora" tem Android 15 e o proxy de Los Angeles (`FATOS-DO-ALUNO.md`). Antes, conferir se o app do Insta está em inglês (não está anotado no projeto).
- **O plano, só no Insta, programado uma vez por semana (o método da aula, em versão leve):** 2 planos "Diariamente", de 17/11 00:00 a 23/11 23:59, com o "Horário de publicação aleatório" desligado:
  - **"01 - 18:50"**, com **22** vídeos e a palavra **manifestation**. Termina antes do post das 19h30.
  - **"02 - 23:20"**, com **25** vídeos e a palavra **law of attraction**. Termina antes do post da 0h00.
  - Os números são diferentes entre os planos, como a aula pede, e ficam bem abaixo dos 100 de uma vez.
  - Na semana seguinte, outras palavras (tarot reading, astrology, spiritual awakening) e outros números.
- **Conferir todo dia em Registros** ("Confie... mas cheque"):
  - Se o horário agendado sair diferente do de Brasília, ajustar. O relógio do celular dela é BRT −4 h (`FATOS`), e não sei qual relógio o GeeLark usa no agendamento.
  - Não abrir o celular dela enquanto a rodada roda (18h50 a ~19h20 e 23h20 a ~23h50).
- **O custo:** ~50 a 60 min de GeeLark por dia, além do uso normal. Com isso, o pacote de 06/11 (766 + 60) acaba antes de 26/11: comprar o de 2.000 min (US$ 14 a 15) quando passar de ~300 (`Faturamento`).
- **O risco:** a conta da Nora tem mais de um mês e posts no ar. O que derrubou a conta do Marcos Daniel foram 50 a 100 vídeos por vez numa conta de 3 dias. Aqui são 22 a 25 por vez.
- **O Face fica de fora:** a Página está no perfil pessoal do aluno, aberto no PC, e logar esse perfil no GeeLark com o IP de Los Angeles é o risco que o Delian descreve. No Face, o aquecimento é à mão, como a Manu: entrar no Reels como a Página, ver até o fim e curtir 5 a 10 vídeos do nicho antes de postar (opcional).
- **Fora:** a automação de curtir e comentar e a postagem automática. Postar é sempre ao vivo, à mão (seção 2 do `CLAUDE.md`).
