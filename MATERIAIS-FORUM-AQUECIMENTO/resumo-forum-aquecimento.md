# Resumo — fórum, aquecimento automático no GeeLark

Leitura feita em 16/11 às 18h30. Os dois posts inteiros, do primeiro ao último comentário. Conferi cada um duas vezes indo do início ao fim em janelas contínuas e não faltou nada.

## Conferência

| Post | Autor | Período | Mensagens | Imagens |
|---|---|---|---|---|
| "Programe Seu Aquecimento Apenas uma Vez e Vá Trabalhar #godmode" | joanfran.co | 16/05 a 28/07/2026 | 54 | 2 |
| "Aquecimento AUTOMATICO de instragram NO GEELARK????" | Delian | 10/05 a 15/11/2026 | 468 | 70 |

- 72 imagens no zip. 10 fotos de celular foram diminuídas pra 1536x2048 e viraram jpg. Os GIFs ficaram como estão.
- Ficaram fora do zip (vídeo), com o link no .md:
  - **Aula_geelark_MVM.mp4** (135 MB). É a aula do post #godmode, o conteúdo principal dele. Grande demais pra baixar por aqui. Dá pra ver direto no post.
  - export-1778448261459.mp4 (33 MB, victor rhea, 10/05 18h26): o passo a passo em vídeo.
  - 2026-05-10_20-15-26.mp4 (Kaike de Lima, 10/05 20h21): tutorial em vídeo, que o Gustavo fixou no post.
  - Vídeo .mov da Manu Torres (13/05 23h02): dúvida sobre aquecimento de página do Facebook.
- No post do Delian tem 2 avisos de "mensagem fixada", sem texto.

## Passo a passo (post do Delian, 10/05, com as imagens 1 a 6)

1. GeeLark > **Automation** > **Marketplace**.
2. Procurar **"Instagram AI account warmup"** e clicar em **Add**.
3. Em Cloud phone profile, clicar em **Add** e marcar os celulares. Dá pra marcar vários, e todos rodam ao mesmo tempo, sem limite. O próprio GeeLark avisa pra deixar o app do Instagram em inglês e não mudar.
4. Preencher:
   - **PubDate**: data e hora de começar.
   - **NumberOfVideosViewed**: quantos vídeos ver inteiros. Pela conta do Delian, 10 vídeos são uns 3 minutos e 100 vídeos uns 30 minutos. Na prática deu de 30 a 47 minutos.
   - **SearchKeyword**: a palavra de pesquisa, sempre em inglês. Ele usa SOULMATE, ASTROLOGY, SIGNS, TAROT, CARD READING.
5. **Save**. Na aba **Logs** aparece "Waiting for execution", depois "Executing" e no fim "Task completed". O tempo só aparece quando termina. A página atualiza sozinha ou pela setinha.

O que a automação faz: assiste vídeos inteiros e segue alguns perfis de vez em quando (o Delian seguiu uns 15). Não curte nem comenta. Existe outra automação de curtir e comentar aleatório, mas ele acha que não precisa.

Frequência: o Delian faz 2 vezes por dia, de 12 em 12 horas, uns 30 minutos cada.

Regras:
- **Não abrir o celular enquanto roda**, senão dá falha. O GeeLark pode ficar aberto e minimizado.
- Não repete sozinho. Pra rodar de novo, cria de novo. O "Execute again" não serve pra repetir.
- Dá pra agendar várias de uma vez, mas o Delian diz que o agendamento nem sempre funciona.
- Precisa ser perfil de **celular**, não desktop, e **com proxy**. O recomendado é Android 13 pra cima. O plano Base do GeeLark resolve.
- **Gasta minutos do GeeLark.** A assinatura dá só 60 minutos e o resto é recarga. A Mari pagou $15 em 2.000 minutos (o Delian achava que era $9). O Delian acha melhor comprar minutos do que pacote.

Palavras-chave: o André Costa postou uma lista de 20.
- Tarot reading, Tarot reader, Psychic reading, Fortune telling, Card reading
- Spiritual reading, Energy reading, Love tarot reading, Breakup tarot, Relationship reading
- Twin flame reading, Soulmate reading, Love psychic, Career tarot reading, Money tarot
- Life guidance tarot, Timeless tarot, Urgent message tarot, Hidden truth tarot

O Delian prefere 1 palavra por automação, variando a cada uma, "pra não bugar".

Resultado: o feed das contas ficou só de tarot e espiritualidade, como na imagem `automatico_10-05_15h21_CelaeGui_1.png`. Uma conta ganhou 10 seguidores sem postar.

## Post #godmode (joanfran.co, 16/05)

- Testado só no GeeLark. O conteúdo está na aula em vídeo, que não baixou. Pelos comentários dá pra pegar isto:
  - Programar **no máximo pra uma semana** e conferir todo dia: "Confie... mas cheque!"
  - Palavras de pesquisa misturadas: ele criou mais duas categorias com palavras aleatórias. "Quanto menos coisas em comum nas contas... melhor!"
  - Dá pra criar "playlists" de palavras: clica em palavras no segundo campo e aparece a opção de criar uma playlist.
  - Se marcar todos os celulares, todos rodam no horário marcado.
  - Ele divide **100 vídeos em 4 rodadas por dia**: 6h (25 vídeos), 9h (25), 11h (25) e 12h30 (25).
- Custo calculado pelo Marcos Passold (17/05):
  - Uma rodada de 25 a 30 vídeos gasta de 11 a 13,5 minutos.
  - 5 rodadas por dia dão de 56 a 67 minutos por conta.
  - Com 5 contas são 280 a 335 minutos por dia.
  - Plano de 2.000 minutos a US$14, uns R$70,84 com o dólar a R$5,06. Dá R$0,035 por minuto, ou R$9,90 a R$11,90 por dia, e dura de 6 a 7 dias com 5 contas.
- É só pro Instagram (Marcos Passold). A Mari fez um post à parte de aquecimento automático de Facebook, que não li.
- paklto: tomou shadowban por pôr link na bio cedo demais. Fez 30 minutos de aquecimento e o vídeo seguinte voltou a ter alcance.
- Wisney: rodou e ficou verde, mas o relatório mostrava erros "No element found" (botão de login e ALLOW) em uns 40% das ações.

## Erros e o que resolveu

- **"Proxy detection failed"** (o mais comum):
  - Reiniciar o celular dentro do GeeLark.
  - Se não resolver, tirar o proxy, reiniciar e pôr o proxy de novo (Delian).
  - Testar o proxy no perfil antes de criar a automação (Delian, Kailane).
  - Clicar na bolinha azul de executar de novo 2 ou 3 vezes, ou esperar um pouco e tentar de novo (Kaike, Manu Torres, victor rhea).
- **"Please set a time to publish"**: com vários celulares, todos precisam ter horário. Ao pôr as palavras-chave o horário de outro celular pode sumir (victor rhea).
- **"Not logged in"**: o Instagram não estava logado naquele celular. Conferir a conta por dentro.
- **Terminou em 18 a 24 segundos**: conferir o número de vídeos ou reiniciar o celular.
- **Instagram pedindo permissão de notificação** trava a automação. Aceitar uma vez (Heitor).
- **Sem opção de escolher o perfil**: perfil sem proxy (Gustavo Alves) ou GeeLark em modo desktop (ihago).
- **"Insufficient ..."**: acabaram os minutos. Recarregar em Billing.
- 26 e 27/05: Android 14 e 16 ficaram em manutenção no GeeLark e as tarefas não terminavam (CARLOS LOBO).

## Riscos

- **Marcos Daniel, 01/10**: perdeu uma conta no 3º dia de vida, 2º usando a automação, por "suspeita de automação". Fazia de 50 a 100 vídeos (testou 75). No dia seguinte as contas estavam deslogadas e pediram selfie. Uma voltou, a outra caiu.
  - O Delian respondeu que verificação de selfie é comum até em conta que já vende (quase perdeu uma de 50 mil seguidores). Sugere testar uma conta com aquecimento manual e outra com automático.
- Hosana (05/10): a conta pedia selfie de novo mesmo depois de verificar 2 vezes. Ficou sem resposta.

## Facebook, celular físico e postagem

- **Facebook**: o GeeLark 4.3.9 lançou o template "Facebook Reels Account Warm-up".
  - O Delian testou em 2 contas e não deu problema. Mas avisa do risco: o Face ver a conta "uma hora no Brasil, outra na China, outra nos EUA" se cada celular tiver um IP.
  - A ideia dele: um emulador só pro Facebook, com um proxy só.
  - Página é aquecida uma por uma, não pelo perfil dono.
  - Ele prefere aquecer o Face na mão.
- **Celular físico e tablet**: não tem automação, é manual. Só funciona nos celulares virtuais do GeeLark (tem um tutorial pro VMOS também).
- **Migrar do celular físico pro GeeLark**: não cai se usar o mesmo proxy (Delian).
- **Postagem automática**: o GeeLark tem template, e a BRISA mandou um vídeo do YouTube ensinando (https://youtu.be/cKDlPXs0Fr8). Pontos levantados:
  - O Delian usa o programador de postagem.
  - Às vezes o Insta bloqueia a postagem e aí ele posta pelo Meta Business Suite. Com 4 posts por dia geralmente não dá violação.
  - O Ricardo Santana tomou restrição e só consegue postar pelo Suite.
  - O Aloncio reclamou de vídeo repetido. O Delian diz que, organizando certinho, não repete.

## Perguntas sem resposta nos posts

- Luccas Rosa (20/07): esse aquecimento salva conta que levou violação e perdeu engajamento?
- Hosana (05/10): o que fazer quando pede selfie de novo depois de verificar 2 vezes?
- Renata (01/10): renova sozinho todo dia? Pelo resto do post, não: tem que programar de novo.
- Wisney (17/05): muitos erros "No element found" mesmo com a tarefa verde.
