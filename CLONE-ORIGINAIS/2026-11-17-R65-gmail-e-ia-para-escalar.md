# R65: a pergunta do aluno ao Clone sobre criar Gmail e a IA para escalar vídeo e voz, e a resposta, texto inteiro (17/11/2026, colada às ~01h10)

**O que é:** o original que o aluno colou (regra 2b do `CLAUDE.md`). O resumo e a conferência estão em `CLONE-DO-GUSTAVO-RESPOSTAS.md` (R65). Os negritos e os emojis vieram assim; as 3 linhas do fim são as sugestões automáticas do NotebookLM.

(Na mesma mensagem veio o e-mail do Instagram "You're back on Instagram" de 17/11 01h06; ele está registrado no `FATOS-DO-ALUNO.md`, não aqui.)

---

## Pergunta (o aluno, direto no Clone)
a conta do gmail é criado pelo celular ou computador? parece que pelo celular é mais facil, pois nao pede algumas infos que no computador pediria.
outra duvida, que ia usar pra gerar video quando eu for escalar? pq ai seria mais videos, mais creditos gastos, etc. qual ia compensa pra gerar videos e voz?

## Resposta
1. Criar conta do Gmail: celular ou computador?
Pelo celular é muito mais fácil e é o método recomendado nas aulas.

* O macete das aulas: Na Aula 53 (0:25:37 a 0:26:10), o Gustavo explica exatamente esse macete:

"Rapaziada, macete para criar Gmail: celulares Android todo mundo tem em casa... Venho aqui, mano, a gente cria por dentro da Play Store, por dentro do aplicativo do Google Drive, por dentro do YouTube, por dentro do Gmail, até ele pedir código. Dá para criar, sei lá, uns dois Gmail por dia... Tenho Gmail para caralho guardado nas planilhas até hoje".

* Por que no computador complica: No navegador do PC (especialmente via proxy ou aba anônima), a proteção anti-bot do Google quase sempre barra o cadastro exigindo um número de telefone com SMS na hora.
* No celular físico: O aplicativo (Google Drive, YouTube ou Play Store) aproveita o identificador de hardware do próprio aparelho e frequentemente pula a exigência de número de telefone ou permite cadastrar 1 a 2 contas limpas direto antes de solicitar verificação. Crie as contas no celular e salve login e senha na planilha para usar no GeeLark e nas IAs.

2. Qual IA compensa para gerar Vídeo e Voz na hora da Escala?
Na operação da Appyon, a escolha das ferramentas depende do estágio entre custo de créditos versus velocidade de produção:
🎙️ Para Geração de Voz:

1. Google Flow (Omni Flash 1.2) — O Menor Custo:
   * Na Aula 51 (0:52:43 a 0:53:45) e na Aula 70 (0:45:18 a 0:49:20), o Gustavo ensina que o Omni Flash gera a voz junto com o vídeo a partir do prompt com consistência de tom ("Voice Profile").
   * Se você usa os prompts da Central ou molda a voz no Claude (ex: moça americana de 35 anos animada), o Flow entrega a locução já sincronizada sem gastar nada com plataformas externas de áudio.
2. ElevenLabs — A Qualidade Máxima para Frankenteins / AutoEditor:
   * Na Aula 21 (0:30:17), Aula 43 (0:36:00 a 0:37:32) e Aula 54 (0:54:22 a 0:54:43), Gustavo e Iorhan mostram que usam a ElevenLabs para gerar áudios em massa em blocos separados (pacotes de ganchos, corpos e CTAs).
   * Preço e escala: O plano inicial custa $5 dólares. É a melhor IA se você for montar uma esteira automatizada no AutoEditor, porque você corta os silêncios previamente e aplica espelhamento de voz no avatar.

🎬 Para Geração de Vídeo / Animação do Avatar:
O ecossistema trabalha com duas opções principais:
Opção A: Google Flow (Omni Flash) — Foco em Custo Quase Zero

* Vantagens financeiras:
   * Na Aula 53 (0:23:21 a 0:25:27), o Gustavo detalha a estratégia de assinar o plano do Google Pro ou usar múltiplas contas do Gmail que renovam créditos diariamente para gerar os takes a custo irrisório.
   * Vídeos de 10 a 15 segundos divididos em takes no Omni Flash saem muito baratos.
* Ponto de atenção na escala:
   * O Flow exige gerar cena por cena e às vezes recusa prompts por políticas de conteúdo. Como ele gera clipes curtos de 8 a 15 segundos, você precisa juntar os takes manualmente ou via ferramentas como o Fusion-Z.

Opção B: HeyGen — Foco em Praticidade, Velocidade e AutoEditor

* Vantagens operacionais:
   * Na Aula 11 (0:42:06 a 0:42:36), Aula 54 (1:00:22 a 1:01:00) e Estrutura Facebook (0:30:13 a 0:30:35), o Gustavo explica que o HeyGen é a ferramenta definitiva para quem quer velocidade de esteira.
   * Ele recebe a foto do blueprint e o áudio da cópia, aplicando lip-sync e animação facial automática em um único processo.
* Custo por vídeo (Avatar 3):
   * O plano de $29 dólares dá 600 créditos.
   * No Avatar 3, um vídeo de até 55 segundos consome 3 créditos.
   * Isso permite gerar 200 vídeos por mês, saindo a aproximadamente $0,14 dólar (~R$ 0,75 a R$ 0,80) por vídeo gerado.
* Diferença de Avatares no HeyGen:
   * Avatar 3 (Econômico): Gasta 3 créditos. Ele faz o lip-sync perfeitamente, mantém um movimento de cabeça básico e loopa suavemente. É o que a operação usa para rodar volume.
   * Avatar 4 e 5: Gastam 19 créditos por vídeo longo. Têm movimentação corporal adaptativa mais expressiva, mas custam mais de 6 vezes mais caro.

Resumo para a sua Esteira:

* Criar contas Gmail: Crie no celular Android (por dentro do app do Google Drive/YouTube) para evitar SMS e guarde as credenciais na planilha.
* Se o orçamento for curto: Gere no Google Flow com prompts divididos pelo Creative Hub, usando as vozes ajustadas no próprio prompt do Omni Flash.
* Quando for escalar em volume (10 a 20+ vídeos por dia): Assine o plano de $29 do HeyGen e gere no Avatar 3 (200 vídeos por $29). O tempo que você economiza na renderização cobre o custo da ferramenta logo nas primeiras vendas da Appyon.

💡 Deseja que eu passe a estrutura exata do prompt de voz em inglês para testar a consistência no Flow antes de decidir assinar o HeyGen?
Qual o custo e tempo de renderização no HeyGen?Como configurar o proxy no GeeLark corretamente?Me dê os prompts para os 10 vídeos de aquecimento
