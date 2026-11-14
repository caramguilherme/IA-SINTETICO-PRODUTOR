# Ferramentas do projeto (atualizado no pente fino de 11/11/2026)
Só ficam aqui as ferramentas em uso. Os scripts antigos (painéis de 22/10 a 10/11, um por dia, com caminhos de sessões antigas e que reescreveriam painéis já postados) estão em `arquivo/ferramentas-antigas/`, com o guia antigo em `arquivo/ferramentas-antigas/LEIA-ANTIGO.md`. **Não rodar nenhum deles sem ler e adaptar.**

## Painéis
- `../PAINEL-MODELO.html`: o modelo; todo painel novo é ele com a linha `const PACOTE = …;` trocada pelo pacote do vídeo (formato do pacote: `REGRAS-DO-AGENTE.md`, P12, e o pacote de um painel recente). O script que gera os painéis de um dia é novo e fica em `arquivo/ferramentas-antigas/` depois de usado.
- **Mudanças no `PAINEL-MODELO.html` em 10/11 (`LICOES-FLOW-E-PROMPTS.md`, 10/11):** a caixa de aviso (`.tip`) quebra links longos (o painel não estica mais no celular); a frase da edição não supõe pré-gancho; seção nova `clone` ("Clone do Gustavo (antes de gerar)", campo `clone` do pacote: `nota` e `pergunta`; sem o campo, some).
- `kit-portal/build_kit_portal.py` (10/11; **o kit já foi postado e os painéis estão em `arquivo/paineis/`: não rodar de novo, ele reescreveria os painéis na raiz**; **para fechar o LIVRE e as movimentações pela `kitportal-IMG` aprovada, mudar as constantes `LIVRE`, `BASE_MOV`, `GESTO` e a posição dos números (`nums`) e rodar de novo**): gera o PAINEL-NORA51 a 54 a partir do modelo, com as falas do `ROTEIRO-KIT-PORTAL-NORA51-54.md`, a Central e a voz do nora46 e o mapa, o story e as respostas do nora49; confere até 22 palavras por fala e que a movimentação não repete palavras da fala. Uso: `python3 -I ferramentas-painel/kit-portal/build_kit_portal.py` e depois o `conferir-painel.js` nos 4.
- `dia-1111/build_dia_1111.py` (11/11; **postado, não rodar de novo**; a `manha1111-IMG`, o LIVRE e as mãos dela, usados também em 12/11, estão no dicionário `CENAS`): gera os 6 painéis do dia 11 (nora55 a nora60, 2 cenas, a prova do Trustpilot às 12h, 18h e 00h). Para fechar o LIVRE e as movimentações pela `manha1111-IMG` ou pela `noite1111-IMG` aprovada: mudar o dicionário `CENAS` (repouso da mão, fundo, luz) e os `nums` de cada vídeo e rodar de novo. Ele confere até 22 palavras e que a movimentação não repete palavras da fala.
- `dia-1211/` (12/11): `build_dia_1211.py` gera os painéis do dia 12 (nora59 o longo, nora60 o curto em 2 versões, nora61 o POV), na `manha1111-IMG`, com as peças já geradas marcadas como "reutilizar"; é o molde dos próximos dias. `pov/montar_pov.py` monta o POV narrado (paisagens com zoom lento, transição de 0,5 s e a voz; uso no topo do script). `slideshow/fazer_slideshow.py` fez o slideshow do Face de 12/11 (o formato saiu da fila do Face: 4 a 8 views; o vídeo foi apagado do repositório em 13/11, a pedido do aluno).
- `conferir-painel.js`: abre painéis no Chromium e mostra os erros ("ERR: nenhum" = abre certo). Uso: `node ferramentas-painel/conferir-painel.js PAINEL-NORA59.html`.
- `conferir_signos.py`: confere se um painel cita signos de outro vídeo. Uso: `python3 -I ferramentas-painel/conferir_signos.py . 51:Taurus,Virgo,Capricorn`.

## Pente fino (P47)
- `buscar.py`: procura um assunto em todos os documentos (raiz, `HISTORICO-DISCORD/`, `MATERIAIS-CALL-*`, `ferramentas-painel/`, `referencias-mineracao/` e `arquivo/`), sem acento nem maiúscula, com o `FATOS` primeiro. Uso: `python3 -I ferramentas-painel/buscar.py "termo 1" "termo 2" "termo 3"` (`--tudo` mostra todas as linhas).

## Edição automática (P45): `ferramentas/`
- `editar_video.py` (render), `previa_edicao.py` (prévia antes do render), `transcrever_palavras.py` (tempo de cada palavra, faster-whisper "small"), `transcrever.py` (transcrição simples de vídeos de referência), `variacao_face.py` (o `-FACE`: espelho, mais claro, 1,1x, com a mesma spec), `screenshot-pagina.js`, `capa_face.py`, `miro-ler-quadro.js`; fontes em `ferramentas/fontes/`; guia em `ferramentas/LEIA.md`.
- `ferramentas/specs/`: as specs e as transcrições das edições (nora47 = corpo B; nora48 a nora50 = corpo A; nora51, nora53 e nora54 = curtos do kit; nora52 = longo do kit, com o corte das repetições do Flow em `corte-repeticoes-nora52.txt`; nora54 também com `corte-repeticoes-nora54.txt`); cada edição nova salva a sua aqui.

## Métricas: `dashboard/`
- `preparar_csv.py`, `conferir-dados.js`, `index.html`, `store/` e a receita `COMO-RECRIAR.md`.
- **`METRICAS-NORA.csv`:** BOM e CRLF; ler e gravar com `newline=''`, `encoding='utf-8-sig'` e `csv.DictWriter(..., lineterminator='\r\n')` (com `\n` o git mostra o arquivo inteiro mudado).

## Outros
- `imagens-fixas/`: imagens do desejo do nora46 e a capa do Face; as avaliações reais ficam em `../provas-trustpilot/` (as `-sem-hora` são as de uso).
- `manifestacao/`: a mineração de 26 e 27/10 (`lista.json`, `indice.json` com 148 vídeos transcritos, seção 39 da `BIBLIOTECA-VIDEOS-VIRAIS.md`) e os scripts dela (baixar com yt-dlp e transcrever).
- `prompts/capa-face-nora.md`: o prompt da capa do Face.
- `destaques/` (14/11): os stories e as capas dos Destaques do Insta (About me, Reviews, How it works) e os scripts `capas.py` (capa creme com lua, estrela ou brilho terracota; uso: `python3 -I ferramentas-painel/destaques/capas.py <pasta>`) e `fundo_reviews.py` (fundo desfocado + 2 prints do Trustpilot em cartão; uso: `python3 -I ferramentas-painel/destaques/fundo_reviews.py foto.jpg saida.jpg print1.png print2.png`, depois o `texto_story.py` por cima).
- `skills/`: as skills do claude.ai do aluno (`leitura-discord-mvm`, `doc-mvm-legacy`), em pasta e em zip.
