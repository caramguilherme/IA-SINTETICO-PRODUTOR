# Ferramentas do projeto (atualizado no pente fino de 10/11/2026)
Só ficam aqui as ferramentas em uso. Os scripts antigos (painéis de 22/10 a 10/11, um por dia, com caminhos de sessões antigas e que reescreveriam painéis já postados) estão em `arquivo/ferramentas-antigas/`, com o guia antigo em `arquivo/ferramentas-antigas/LEIA-ANTIGO.md`. **Não rodar nenhum deles sem ler e adaptar.**

## Painéis
- `../PAINEL-MODELO.html`: o modelo; todo painel novo é ele com a linha `const PACOTE = …;` trocada pelo pacote do vídeo (formato do pacote: `REGRAS-DO-AGENTE.md`, P12, e o pacote de um painel recente). O script que gera os painéis de um dia é novo e fica em `arquivo/ferramentas-antigas/` depois de usado.
- **Mudanças no `PAINEL-MODELO.html` em 10/11 (`LICOES-FLOW-E-PROMPTS.md`, 10/11):** a caixa de aviso (`.tip`) quebra links longos (o painel não estica mais no celular); a frase da edição não supõe pré-gancho; seção nova `clone` ("Clone do Gustavo (antes de gerar)", campo `clone` do pacote: `nota` e `pergunta`; sem o campo, some).
- `kit-portal/build_kit_portal.py` (10/11, em uso até o fim do kit do portal; **para fechar o LIVRE e as movimentações pela `kitportal-IMG` aprovada, mudar as constantes `LIVRE`, `BASE_MOV`, `GESTO` e a posição dos números (`nums`) e rodar de novo**): gera o PAINEL-NORA51 a 54 a partir do modelo, com as falas do `ROTEIRO-KIT-PORTAL-NORA51-54.md`, a Central e a voz do nora46 e o mapa, o story e as respostas do nora49; confere até 22 palavras por fala e que a movimentação não repete palavras da fala. Uso: `python3 -I ferramentas-painel/kit-portal/build_kit_portal.py` e depois o `conferir-painel.js` nos 4.
- `conferir-painel.js`: abre painéis no Chromium e mostra os erros ("ERR: nenhum" = abre certo). Uso: `node ferramentas-painel/conferir-painel.js PAINEL-NORA51.html`.
- `conferir_signos.py`: confere se um painel cita signos de outro vídeo. Uso: `python3 -I ferramentas-painel/conferir_signos.py . 51:Taurus,Virgo,Capricorn`.

## Pente fino (P47)
- `buscar.py`: procura um assunto em todos os documentos (raiz, `HISTORICO-DISCORD/`, `MATERIAIS-CALL-*`, `ferramentas-painel/`, `referencias-mineracao/` e `arquivo/`), sem acento nem maiúscula, com o `FATOS` primeiro. Uso: `python3 -I ferramentas-painel/buscar.py "termo 1" "termo 2" "termo 3"` (`--tudo` mostra todas as linhas).

## Edição automática (P45): `ferramentas/`
- `editar_video.py` (render), `previa_edicao.py` (prévia antes do render), `transcrever_palavras.py` (tempo de cada palavra, faster-whisper "small"), `transcrever.py` (transcrição simples de vídeos de referência), `screenshot-pagina.js`, `capa_face.py`, `miro-ler-quadro.js`; fontes em `ferramentas/fontes/`; guia em `ferramentas/LEIA.md`.
- `ferramentas/specs/`: as specs e as transcrições das edições (nora47 = corpo B; nora48 a nora50 = corpo A); cada edição nova salva a sua aqui.

## Métricas: `dashboard/`
- `preparar_csv.py`, `conferir-dados.js`, `index.html`, `store/` e a receita `COMO-RECRIAR.md`.
- **`METRICAS-NORA.csv`:** BOM e CRLF; ler e gravar com `newline=''`, `encoding='utf-8-sig'` e `csv.DictWriter(..., lineterminator='\r\n')` (com `\n` o git mostra o arquivo inteiro mudado).

## Outros
- `imagens-fixas/`: imagens do desejo do nora46; as avaliações reais ficam em `../provas-trustpilot/`.
- `manifestacao/`: a mineração de 26 e 27/10 (`lista.json`, `indice.json` com 148 vídeos transcritos, seção 39 da `BIBLIOTECA-VIDEOS-VIRAIS.md`) e os scripts dela (baixar com yt-dlp e transcrever).
- `prompts/capa-face-nora.md`: o prompt da capa do Face.
- `skills/`: as skills do claude.ai do aluno (`leitura-discord-mvm`, `doc-mvm-legacy`), em pasta e em zip.
