# Sons da edição da Nora (efeitos sonoros, desde 12/11/2026)

Pedido do aluno (12/11 ~13h): "quem vai pôr o riser é você"; ele só monta no CapCut o vídeo cortado, o pré-gancho e a música.
Regras: Clone R34 e R13 (`CLONE-DO-GUSTAVO-RESPOSTAS.md`); mapa de momentos em `COMUNIDADE-E-ESTRATEGIA.md` (12/11 ~12h55).

| Arquivo | O que é | Pico no arquivo | Onde entra | db padrão |
|---|---|---|---|---|
| `riser-nora.wav` | "Cinematic trailer riser" (Mixkit 790), 2,5 s, fade in 0,25 s, cortado logo depois do pico | 2,40 s | termina no corte do pré-gancho para a fala | 0 |
| `impact-nora.wav` | "Cinematic whoosh deep impact" (Mixkit 1143: whoosh entrando + batida grave) + "Space impact" (Mixkit 774, a batida média que o alto-falante do celular toca) | 0,60 s | no 1º quadro da fala | 0 |
| `whoosh-nora.wav` | "Air woosh" (Mixkit 1489) | 0,70 s | troca de paisagem no POV, troca de tela no slideshow | −8 |
| `sparkle-nora.wav` | "Magic sparkle whoosh" (Mixkit 2350) | 0,45 s | imagens do desejo, prova do Trustpilot (teste depois) | −12 |

- **Fonte e licença:** mixkit.co, "Sound Effects Free License" (uso grátis em projetos pessoais e comerciais, sem crédito; não revender o som sozinho). Baixados em 12/11/2026 das prévias (`https://assets.mixkit.co/active_storage/sfx/<id>/<id>-preview.mp3`).
- **Volume:** o `db` é o pico do som (janelas de 50 ms) em relação à referência, o mais alto entre a voz (depois do corte) e o som do pré-gancho (antes). O pré-gancho costuma vir ~10 dB acima da voz; com a voz de referência, o riser sumia no tsunami (teste no nora55, 12/11). Conferido também com passa-alta de 300 Hz (alto-falante de celular): o riser sobe 3 a 8 dB no fim do pré-gancho e o impact ~15 dB no corte.
- **Uso:** no spec do `editar_video.py`, `"sons": [{"som":"riser","pico_em":"corte"}, {"som":"impact","pico_em":"corte"}]` ("corte" acha sozinho a 1ª troca de cena forte entre 1 e 9 s; ou o segundo exato). O áudio sai em AAC 192k (sem "sons", copiado sem mexer).
- **Fora:** boom, bass drop, sub drop, heartbeat, reverse, glitch e o "moan" (R13, P42).
- **Ajuste de 12/11 ~13h25 (aluno: "o impact achei meio fraquinho"):** o volume passou a ser medido com passa-alta de 250 Hz (o que o alto-falante do celular toca; o grave do impact quase não sai no celular), com teto de −3 dBFS no pico cheio; impact a +4 dB da referência; `"respiro": 0.1` na spec baixa o som do montado nos 0,1 s antes do corte e o riser termina 0,1 s antes (`"pico_em": "corte-0.1"`), para a batida vir depois de um vazio. 3 impacts mais fortes de trailer em teste (A = Mixkit 2919 + 3057 + 2655; B = 2901 + 3057; C = 2903 + 3057 + 2655), montados com `montar_impact.py` (camadas com os picos alinhados, cauda de ~1 s para não cobrir a fala); o escolhido vira o `impact-nora.wav`.
