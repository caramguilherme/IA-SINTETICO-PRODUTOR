---
name: editar-video-nora
description: Use quando o Guilherme mandar um vídeo da Nora montado sem texto (arquivo ou link do Google Drive com "noraNN" no nome) para a edição automática da regra P45: caixa do topo, números, legenda, imagens, faixa do story e seta, devolvendo o noraNN-final.
---

# Edição automática da Nora (P45)

O aluno manda o `noraNN-montado` (hook + takes + música, sem texto). Eu ponho tudo por cima pelo painel do vídeo, sem mexer no áudio, e devolvo o `noraNN-final`. Ele não precisa escrever nada: o número no nome diz o painel.

## Passo a passo
1. **Painel:** abrir `PAINEL-NORANN.html` e tirar do pacote (`const PACOTE = {...}`): `texto_tela.hook` (caixa do topo), `mapa_tela.numeros` (x e y em % → X = x/100·720−360, Y = 640−y/100·1280), `mapa_tela.estilos` (cores, tamanhos, quando cada coisa entra), `mapa_tela.seta`, as imagens (desejo, avaliações) e o que é corpo A ou B.
2. **Baixar:** arquivo anexado = usar direto. Link do Drive = `curl -sS -L -o <pasta>/noraNN-montado.mp4 "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"` (o ID fica entre `/d/` e `/view`; o `gdown` cai num servidor que a rede não libera). Pasta nova e vazia no scratchpad. Se der 403, o ambiente da conta não libera o Drive: `PASSAGEM-DE-CONTA.md`, passo 1b.
3. **Conferir o arquivo:** `ffprobe` (tamanho, fps, duração, áudio).
4. **Transcrever com o tempo de cada palavra:** `ffmpeg -i video -ac 1 -ar 16000 -c:a pcm_s16le a.wav` e `HF_HUB_DISABLE_XET=1 python3 -I ferramentas-painel/r0611/transcrever_palavras.py a.wav palavras.json` (modelo "small"; no 1º uso baixa de huggingface.co e us.aws.cdn.hf.co). Comparar com as falas do painel, take por take (P33): palavra faltando, repetida ou trocada vai para o aluno antes de postar. Trocar "1111" por "11:11" nas palavras.
5. **Achar os cortes:** `ffmpeg -i video -an -vf "scale=270:480,select='gt(scene\,0.12)',metadata=print" -f null -` (o hook → quarto ou estúdio dá ~0,6; os cortes de silêncio com zoom dão ~0,15). Corte fino perto de um take: limiar 0,03 só naquele trecho (`-ss A -to B`). Confirmar com quadros (`ffmpeg -ss t -frames:v 1`).
6. **Spec:** partir da spec pronta do mesmo corpo (corpo A limpo: `ferramentas-painel/r0611/spec-nora48.json`; corpo B: `ferramentas-painel/r0411/spec-nora47.json`) e trocar entrada, saída, tempos, signos da caixa, números e palavras. Regras: caixa do topo do 1º quadro do hook até o fim do Take 1; números do começo ao fim; legenda do Take 1 ao fim (nunca no hook; no corpo B, não durante as imagens do desejo e as avaliações); faixa do story ("Your private reading is in my story", "my story" em vermelho) do Take 2 ao fim no corpo A, do CTA ao fim no corpo B; seta (X −288, Y −333, tamanho 14) do CTA ao fim; margem do Face (P43): texto entre 8% e 92% da largura, centro dos números entre X −230 e +230.
7. **Prévia antes do render:** `python3 -I ferramentas-painel/ferramentas/previa_edicao.py spec.json previa.png <8 tempos>` (um quadro do hook, do Take 1, do corpo, das imagens, do CTA e do fim) e olhar a folha. Ela imprime onde cada caixa e número cai (% da tela): **número que encosta na caixa do topo, no rosto, na mão ou no objeto muda de lugar** (no nora48: o 11:11 subiu para Y 506 e ficou no tamanho 15; o 222 foi para Y 40). Anotar a mudança e dizer ao aluno em 1 linha.
8. **Render:** `python3 -I ferramentas-painel/ferramentas/editar_video.py spec.json` (crf 21, preset medium; ~8 min para 67 s em 1080×1920). Rodar em segundo plano se passar de 10 min.
9. **Conferir o final:** um quadro de cada trecho do arquivo final, numa folha; áudio igual ao do montado (`ffprobe` do stream de áudio).
10. **Entregar:** `SendUserFile` com o `noraNN-final.mp4` (display attach). Mensagem curta: o que entrou, o que mudou de posição e por quê, e o próximo passo (conferir no celular, postar ao vivo no horário do painel, comentário de cada rede, story no ar).
11. **Registrar:** spec e transcrição em `ferramentas-painel/rDDMM/`; linha na `BIBLIOTECA-DE-TAKES.md` (tempos dos cortes, ajustes, tamanho); commit e push. Quando o aluno disser que postou: linhas no `METRICAS-NORA.csv`, entrada no `METRICAS-NORA-LEIA.md` e o `CLAUDE.md` seção 1.

## Não fazer
- Não mexer no áudio. Não pôr efeitos animados (só entrada e saída com fade).
- Não pôr imagem do desejo nem avaliações no corpo A (são do corpo B).
- Não inventar número, avaliação ou depoimento: as avaliações são as reais de `provas-trustpilot/`.
