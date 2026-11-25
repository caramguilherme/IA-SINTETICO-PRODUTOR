# Fórum: post "🏭 Fábrica de Vídeos com IA — tutorial passo a passo (do zero ao lote automático)" — conversa completa

Canal: #📝︱fórum-appyon › 🏭 Fábrica de Vídeos com IA · servidor MVM Legacy
Período: 24/11/2026 12h05 até 24/11/2026 20h55 (leitura feita em 24/11 às 23h50)
Total: 22 mensagens, na ordem do canal (o post original é a 1ª, as outras são os comentários). Horário de Brasília. Imagens e anexos no zip imagens-discord_24-11_23h50.zip.


## 24/11/2026

**12h05 · Kyk.**
como vcs lidam com o aviso de atividade incomum?

**12h06 · Kyk.**
aqui o claude ta parando a fabrica e aguardando meus comandos eeu nao consigo reverter isso de jeito nenhum

**14h46 · Kyk.**
consegui dar uma burlada, projeto ficou top demais obrigado mano!
Imagem: imagens/forum-fabrica_2026-11-24_14h46_Kyk_1.jpg — Painel "Escritório da Fábrica" (abas Gerente / Mensagem). Topo: "kayque@fabrica: openbot --escritorio · ao vivo · postagem 2026-11-24 · HeyGen 938/1000 cr · Arkon ok · conversa · religar fábrica · resetar fábrica · assistir · demo". Faixa vermelha: "FÁBRICA PARADA desde 14:40:11 · nenhum robô roda até você clicar em religar fábrica". Centro: escritório em pixel art com robôs (Gerente, Produtor, Analista, Editor, Consultor, Estagiário, Spy, Roteirista) em volta de um globo; tela "APPYON TIKTOK SHOP". Lado direito "esteira --video": lovealicia02 (AliciaNovak · rotação A · Arkon+Flow · imagens no Flow, vídeos no Arkon), 39%, "agora: Produtor · Gerar o vídeo do gancho — Arkon gerando o vídeo de gancho · pedido de 4 versões, tentativa 1 de 2 · esperando há 5 min". Etapas: Escrever a copy (texto falado + plano do vídeo, Roteirista) ✓; Criar a foto do gancho (1º frame do vídeo do gancho · Nano Banana no Google Flow, Produtor) ✓; Gerar o vídeo do gancho (primeiros segundos, só som de ação · Veo 3 no Arkon) 76%; Criar a foto da persona falando (Nano Banana no Google Flow); Gerar os vídeos da persona falando (a copy em clipes de 8 s · Veo 3 no Arkon); Montar o vídeo final (junta gancho + falas, legendas e cortes · editar.mjs, Editor); Conferir e entregar (checa a régua e manda para PRONTOS · lote.mjs, Editor). "SAÍDA · TAKES PRONTOS 0/3" e "LOTE · VÍDEOS JÁ FEITOS 3/4 · 23/11, 3/6". Embaixo à esquerda "openbot htop": Gerente, Consultor, Spy, Roteirista, Produtor, Editor, todos "parado — fábrica parada pelo botão". Embaixo no meio, log "tail -f banco/producao.log" de 13:04 a 14:40 (flow-img ClaraClark/lote7 e AliciaNovak/lote8 enviados ao Nano Banana e prontos; produzir lovealicia02 estrutura Arkon+Flow: imagem → gancho → body → falas; flow imagem.jpg upload único no Arkon; AliciaNovak/A/gancho enviado (Vídeo · 720p · 8s · 9:16 x4, custo 0 cr)). Rodapé: "personagens: Universal LPC (créditos) · cenário, plantas e esfera: desenhados por código".

**15h32 · Maicon Dionis**
> respondendo a: @Kyk. consegui dar uma burlada, projeto ficou top demais obrigado mano!
caramba irmao. que foda. tudo isso só com o claude?

**15h33 · Maicon Dionis**
foi algum repositorio ou tu fez do jeito que voce queria do zero?

**15h35 · Kyk.**
Eu usei os repositorios que o pessoal colocou aqui mesmo, tudo que eu usei pra construir a fabrica foi explicado e enviado nesse chat do forum

**15h36 · Kyk.**
pra gerar gráficos bonitinhos e só ficar pedindo pra claude ficar refinando o grafico e ascrescentando os detalhes e animaçoes que vc quer, mais isso e o de menos torra muito token kk se tiver sem ideias apenas peça pra claude refinar o grafico

**15h44 · Maicon Dionis**
ja real o que eu mais foi a parte do lado esquerdo de poder ver tudo acontecendo e o resultado . foda demais . vou tentar aqui isso . valeu mesmo

**16h15 · Diogo**
> respondendo a: @Kyk. como vcs lidam com o aviso de atividade incomum?
no flow?

**16h15 · Kyk.**
> respondendo a: @Diogo no flow?
sim

**16h15 · Diogo**
> respondendo a: @Kyk. consegui dar uma burlada, projeto ficou top demais obrigado mano!
caraca, que top ahahahaha

**16h17 · Diogo**
> respondendo a: @Kyk. sim
O meu só deu na hora dele entender o processo e acho que era pq ele tava tirando print via script.
dps na produção teste não deu mais, mas acho que o @João postou uma solução no drive sobre isso.

**16h18 · Kyk.**
entao ele postou a soluçao mais ele moveu o arquivo pra lixeira entao n da pra baixar ele kk

**16h18 · Kyk.**
@João

**16h30 · Kyk.**
mais falar pra vcs o cara soltou o ouro aqui só aplicar o passo a passo, sem erro

**17h25 · João [MVM]**
https://docs.google.com/document/d/1d7LPtehl2zyGjUK4_hWNAaHbMWEOZBxT/edit?usp=drivesdk&ouid=114790101876638115398&rtpof=true&sd=true tá aqui o arquivo
Prévia de link: Google Docs IA leia isso e aplique v3(1).md IA leia isso e aplique — v3 (portátil) Projeto: Fábrica de vídeos (package.json → name: fabrica-de-videos) Data: 22/10/2026 · Motivo: a fila noturna quebra no passo de envio por falso positivo de regra de automação Versão portátil: nenhum caminho fixo de usuário. A raiz do projeto é descoberta na...
Links desta mensagem:
- https://docs.google.com/document/d/1d7LPtehl2zyGjUK4_hWNAaHbMWEOZBxT/edit?usp=drivesdk&ouid=114790101876638115398&rtpof=true&sd=true
- https://lh7-us.googleusercontent.com/docs/AHkbwyJq-GKirRwy15SUTM1_8lZcBdYa_RpwBXKVVlkVYqI2SPYrLjjnVpeVYKrVm1V-UDqG6hK9cS5K7_XrURwEEEFHIzBQIt19UVGH=w1200-h630-p

**17h25 · João [MVM]**
> respondendo a: @Diogo Nunca pensei que o Tibia fosse trabalhar pra mim kkkkk. Muito bom o conhecimento compartilhado. Adaptei full aqui pro flow e fazendo os ajustes finos. Acho que vai ajudar bastante na rotina corrida por enquanto. v
Parabéns mano muito top

**17h26 · João [MVM]**
> respondendo a: @Kyk. consegui dar uma burlada, projeto ficou top demais obrigado mano!
Boas ficou bem boa a interface

**17h31 · Kyk.**
vlws eu to refinando o bot agr, to aceitando dicas KKKK

**17h31 · Kyk.**
irmao de verdade valorizo muito esse conteúdo aqui ouro demais parabens

**18h26 · Maicon Dionis**
> respondendo a: @João https://docs.google.com/document/d/1d7LPtehl2zyGjUK4_hWNAaHbMWEOZBxT/edit?usp=drivesdk&ouid=114790101876638115398&rtpof=true&sd=true tá aqui o arquivo
esse no caso a gente usa só quando der o erro, corre? ou logo no inicio de criar a fabrica ja usa

**20h55 · Kleber**
Quem ta usando só o flow pra gerar os vídeos , vocês estão usando o gerador de prompts do Gustavo ou deixaram o fluxo normal ?
