# Sons da edição da Nora (efeitos sonoros, desde 12/11/2026)

Pedido do aluno (12/11 ~13h): "quem vai pôr o riser é você"; ele só monta no CapCut o vídeo cortado, o pré-gancho e a música.
Regras: Clone R34 e R13 (`CLONE-DO-GUSTAVO-RESPOSTAS.md`); mapa de momentos em `COMUNIDADE-E-ESTRATEGIA.md` (12/11 ~12h55).

| Arquivo (nome na spec) | O que é | Onde entra | db padrão |
|---|---|---|---|
| `riser-nora.wav` (`riser`) | **escolhido pelo aluno (o "2"):** "Cinematic drama riser" (Mixkit 632), trecho de 23,0 a 26,05 s: tensão de orquestra que explode no fim; 3,05 s, fade in 0,35 s, termina no pico | termina 0,1 s antes do corte do pré-gancho para a fala | 0 |
| `riser-lento-nora.wav` (`riser-lento`) | **a outra escolhida (o "4"):** o "riser sound effect" de outubro do aluno (`riser sound effect (aluno).mp3`), de 1,7 s ao fim: 3,6 s de subida contínua | idem; **alternar com o `riser` entre posts seguidos da mesma rede** (e o Face nunca ouve o mesmo áudio do Insta do mesmo dia no mesmo pré-gancho) | 0 |
| `impact-nora.wav` (`impact`) | **o "B" ajustado:** "Epic movie impact" (Mixkit 2901) + "Apocalyptic stomp impact" (Mixkit 3057, −3 dB), picos alinhados (`montar_impact.py`), sem a faixa da voz (−8 dB em 2,5 kHz, −4 dB em 800 Hz) e cauda curta (fade exponencial de 0,47 s a 0,87 s): a voz volta ao nível original ~0,3 s depois do corte | no 1º quadro da fala | +1 |
| `whoosh-nora.wav` (`whoosh`) | "Air woosh" (Mixkit 1489) | troca de paisagem no POV, troca de tela no slideshow | −8 |
| `sparkle-nora.wav` (`sparkle`) | "Magic sparkle whoosh" (Mixkit 2350) | imagens do desejo, prova do Trustpilot (teste depois) | −12 |

**Histórico da escolha (12/11):** o 1º impact (Mixkit 1143 + 774) o aluno achou "meio fraquinho"; dos 3 mais fortes (A, B, C) ele ficou entre o B e o C, mas "altinho, a fala dela fica meio apagada": ficou o B, mais curto, sem a faixa da voz e mais baixo. O 1º riser (Mixkit 790, "Cinematic trailer riser") saiu: o aluno pediu "um riser meio de suspense, que a pessoa ouve e acha que vai acontecer algo mirabolante". Dos 5 testados (1 coro Mixkit 662, 2 orquestra 632, 3 metálico 670, 4 e 5 os de outubro do aluno) ele escolheu "2 ou 4". Os 2 mp3 de outubro do aluno estão guardados aqui com "(aluno)" no nome.

- **Fonte e licença:** mixkit.co, "Sound Effects Free License" (uso grátis em projetos pessoais e comerciais, sem crédito; não revender o som sozinho). Baixados em 12/11/2026 das prévias (`https://assets.mixkit.co/active_storage/sfx/<id>/<id>-preview.mp3`).
- **Volume:** o `db` é o pico do som (janelas de 50 ms) em relação à referência, o mais alto entre a voz (depois do corte) e o som do pré-gancho (antes). O pré-gancho costuma vir ~10 dB acima da voz; com a voz de referência, o riser sumia no tsunami (teste no nora55, 12/11). Conferido também com passa-alta de 300 Hz (alto-falante de celular): o riser sobe 3 a 8 dB no fim do pré-gancho e o impact ~15 dB no corte.
- **Uso:** no spec do `editar_video.py`, `"respiro": 0.1, "sons": [{"som":"riser","pico_em":"corte-0.1"}, {"som":"impact","pico_em":"corte"}]` (ou `"riser-lento"`; "corte" acha sozinho a 1ª troca de cena forte entre 1 e 9 s, "corte-0.1" é 0,1 s antes; ou o segundo exato). O áudio sai em AAC 192k (sem "sons", copiado sem mexer).
- **Fora:** boom, bass drop, sub drop, heartbeat, reverse, glitch e o "moan" (R13, P42).
- **Ajuste de 12/11 ~13h25 (aluno: "o impact achei meio fraquinho"):** o volume passou a ser medido com passa-alta de 250 Hz (o que o alto-falante do celular toca; o grave do impact quase não sai no celular), com teto de −3 dBFS no pico cheio; impact a +4 dB da referência; `"respiro": 0.1` na spec baixa o som do montado nos 0,1 s antes do corte e o riser termina 0,1 s antes (`"pico_em": "corte-0.1"`), para a batida vir depois de um vazio. 3 impacts mais fortes de trailer em teste (A = Mixkit 2919 + 3057 + 2655; B = 2901 + 3057; C = 2903 + 3057 + 2655), montados com `montar_impact.py` (camadas com os picos alinhados, cauda de ~1 s para não cobrir a fala); o escolhido vira o `impact-nora.wav`.

## O pack de efeitos sonoros do Gustavo (`pack-aula19/`, mandado pelo aluno em 16/11/2026 com a aula 19)
- **O que é:** o pack que o Gustavo promete na aula 19 (0:49:46: "eu tenho um pack… vou achar e lanço pra vocês"), da pasta do Drive `1wX4AZAUy6evj_M2yfcarxBz2rSSMs-H0`. Ela tem 255 arquivos; aqui estão os 110 úteis, com os `.wav` em `.flac` (sem perda):
  - Rise (15; 10 "Cyber Rise", eletrônicos; o "Cinematic Riser…mp3" tem 84,7 s com vários risers seguidos, para cortar um novo);
  - Impact (45: AMZA de 2,3 a 3,3 s, Artillery de 3,4 a 4,4 s, USFX de 4,5 a 8 s com cauda longa, e Water Impact de 0,2 a 0,7 s, o respingo);
  - Swoosh (42), Slow Motion (2), Dinheiro (3, só no Insta) e Flares (3).
- **Ficaram de fora:** Horror (93, é medo), Glitch (20) e High-Tech (27) (o som de computador não é da Nora) e Relógio (5 faixas de tique-taque de 60 a 124 s; baixar da pasta se um dia servir para o 11:11).
- **Uso:** os sons em uso (o riser "2", o riser "4" e o impact "B") **não mudam sem o aluno escolher pelo ouvido**. O pack é para o rodízio entre posts (uma variação horizontal; fila, item 6). Para entrar no `editar_video.py`, o som escolhido é cortado e ajustado como os de 12/11 (pico, cauda e sem a faixa da voz) e ganha um nome aqui na tabela.
