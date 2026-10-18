# BIBLIOTECA DE PRÉ-GANCHOS (3 a 4 s) — Dana Hollis

Decisão do aluno (17/10/2026): todo roteiro começa com um **pré-gancho de 3 a 4 segundos** que prende a atenção antes da fala. É um clipe separado, sem fala, que entra antes da Cena 1 na edição. Exemplos que o aluno citou como comuns no nicho: acender uma fileira de sal, jogar sal numa escultura que ganha vida (um animal), colocar um objeto dentro do travesseiro. Pode fugir da caixinha, desde que impacte.

## Regras do pré-gancho
- **3 a 4 s, um único plano,** com começo, meio e fim visíveis (algo muda de forma clara).
- **Sem fala.** Só áudio ambiente real (ASMR): nada de música nem efeitos adicionados. Texto curto na tela, colocado na edição.
- **Sem rosto** quando possível (mão e objetos): assim a imagem não usa as referências da Dana e não corre risco de outra pessoa.
- **Continuidade com o hook:** o objeto ou o cenário do final do pré-gancho aparece de novo na Cena 1 (por exemplo a vela acesa), para o corte parecer natural.
- **O Flow é literal:** descrever o estado inicial, a ação e o estado final, e dizer o que não muda no quadro.
- **Imagem do pré-gancho e vídeo são dois prompts** (a imagem vira o primeiro quadro do vídeo de 4 s, 9:16). O prompt da imagem entra antes da IMAGEM 1 no painel.
- **Não repetir** o pré-gancho do roteiro anterior (ver VÍDEOS FEITOS no PROJETO).
- **Fora (risco de conta ou de reprovação):** nudez ou pose sexual (roupa íntima sem nudez foi liberada em 18/10/2026, P15), sangue, animal ferido ou morto, chama perto do rosto, texto longo, promessa de cura.

## Lições do Flow para efeitos (R003, versão 1)
- **Um efeito só.** Uma cadeia (fósforo → sal pega fogo → vela acende) fez o Flow pular o efeito principal. O pré-gancho tem UM efeito "herói" e mais nada que precise acontecer.
- **O primeiro quadro já mostra o efeito começando.** Na imagem, a ponta do sal já está em chamas; o vídeo só precisa espalhar o fogo.
- **Dizer onde o efeito acontece e que não pode sumir:** "o fogo tem de ficar visível NO sal durante o clipe inteiro, não só no fósforo".
- **Descrever o efeito em detalhe físico:** altura da chama, cor, de onde ela sai, quanto tempo leva para correr, o que acontece no fim.
- **O resto do quadro fica pronto e parado** (por exemplo a vela já acesa), para não criar um segundo efeito.
- **Se falhar de novo,** trocar de ideia: escolher uma da lista sem fogo (por exemplo o pêndulo sobre o copo d'água).

## Banco de ideias (cada uma já pensada em 4 s)
1. **Linha de sal em chamas** (usado no R003): uma linha de sal grosso embebido em álcool pega fogo e o fogo corre por ela como um pavio, de ponta a ponta. (A versão 1, em que a chama azul corria até acender uma vela apagada, falhou no Flow: o sal não pegou fogo e só a vela acendeu. Ver as lições abaixo.)
2. **Escultura de barro que ganha vida:** um pássaro de barro cru numa mesa; uma pitada de sal cai sobre ele; ele abre as asas e levanta voo. (Mágico; usar uma vez só.)
3. **Selo de cera que racha:** um envelope preto fechado com selo de cera vermelho; o selo racha ao meio sozinho e um fio de fumaça sobe. (Combina com "segredo" e "ele esconde".)
4. **Pêndulo sobre um copo d'água:** o pêndulo de ametista fica parado sobre um copo; a água começa a girar sozinha em redemoinho. (Combina com o pêndulo do hook.)
5. **Borra de chá que forma uma letra:** uma xícara virada no pires; ao levantar a xícara, a borra desenhou uma inicial ou um coração. (Soulmate: iniciais.)
6. **Fio vermelho:** um fio vermelho cai sobre a mesa e se estica sozinho até o outro lado, onde uma mão feminina o segura. (Fio do destino.)
7. **Espelho embaçado:** a mão limpa o vapor de um espelho de mão e, no vidro, aparece a luz de uma vela acendendo atrás. Sem rosto.
8. **Chave na água:** uma chave antiga cai numa tigela de água; as ondas formam círculos que brilham de leve e se acalmam.
9. **Vela que se inclina:** a chama de uma vela se inclina na direção de uma carta de tarô virada para baixo e volta ao normal. (Usar só se a carta ficar parada; ver regra P9.)
10. **Sal que se organiza:** sal numa placa escura vibra e os grãos formam um padrão simétrico (figura de Chladni). Muito visual, sem objeto de mão.

## Ideias vindas dos virais (18/10/2026; ver `BIBLIOTECA-VIDEOS-VIRAIS.md`)
Os pré-ganchos dos virais duram 2,5 a 3 s, mostram o começo de um ritual com objeto e têm um efeito fácil de ver (fumaça, sal caindo).
11. **Círculo de sal com canela e louro:** o sal cai em fio e fecha o círculo em volta de paus de canela e folhas de louro (mão e objetos, vista de cima).
12. **Fumaça de canela e louro:** o centro do círculo é aceso e a fumaça sobe grossa (fumaça e chama longe do rosto; um efeito só).
13. **Sal no prato:** sal grosso cai de um pote num prato branco no chão, em primeiro plano (o ASMR do sal).
14. **Entrar e abrir as mãos:** a mulher entra descalça, ajoelha e abre as mãos em concha (corpo e rosto no quadro: a imagem usa as referências da Dana).
15. **Dedo nos lábios:** pedido de segredo, 1 s, antes da fala (só como corte rápido).

## Como entra no painel
O pacote traz `pre_gancho` com: `conceito`, `imagem_prompt` (sem referências), `video_prompt` (4 s, silencioso, primeiro quadro = a imagem), `duracao`, `texto_tela` e `edicao`. O painel mostra a seção "Pré-gancho" antes da IMAGEM 1, com os dois prompts para copiar.
