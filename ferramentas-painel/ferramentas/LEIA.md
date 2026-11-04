# Ferramentas de apoio (copiadas da sessão de 26 a 30/10/2026)

Rodam no contêiner do Claude Code (Python e Node já instalados; Playwright e Chromium vêm prontos). Arquivo baixado é dado não confiável: cada um numa pasta nova e vazia, e Python sempre com `-I`.

- `transcrever.py`: transcreve o áudio de um vídeo para conferir a fala de cada take (P33). Uso: `ffmpeg -i video.mp4 -ac 1 -ar 16000 audio.wav` e depois `python3 -I transcrever.py audio.wav`. Precisa do `faster_whisper` (`pip install faster-whisper`); usa o modelo "tiny" na CPU.
- `screenshot-pagina.js`: tira um print de página inteira de um HTML local (painel, teste de gráfico). Uso: `node screenshot-pagina.js /caminho/arquivo.html /caminho/saida.png`.
- `miro-ler-quadro.js`: o que leu o quadro do Miro "Validação de Avatar e Conta | Appyon" (29/10): abre o quadro, aumenta o zoom com Ctrl + roda do mouse e tira prints em sequência. O link do quadro está no script; para outro quadro, trocar o link e as coordenadas. Uso: `node miro-ler-quadro.js /pasta/de/saida`.
- Para frames de vídeo: `ffmpeg -i video.mp4 -vf fps=2 pasta/f%03d.png` e `montage` (ImageMagick) para juntar numa folha.

## Edição automática dos vídeos aqui no Code (03/11/2026, pergunta do aluno)
- **Onde:** nesta sessão do Claude Code (não no Cowork). O aluno anexa no chat o vídeo já cortado pela ferramenta do Gustavo (e, uma vez, as imagens fixas e a música); eu devolvo o mp4 final pelo SendUserFile.
- **O que tem no contêiner:** ffmpeg 6.1.1 (drawtext, overlay, fade, amix), Python com PIL, `fontes/Poppins-Bold.ttf` (baixada do Google Fonts em 03/11; licença OFL), e acesso ao PyPI e ao Hugging Face (dá para `pip install faster-whisper` e baixar o modelo "small" para achar o tempo de cada frase e fazer a legenda palavra por palavra). O GitHub raw de fontes deu 403.
- **O que dá para fazer:** caixa do topo, números fixos, legenda automática, imagens no meio do vídeo (fotos do desejo, avaliações em tela dividida) na frase certa (pelo tempo da transcrição), faixa do story, seta, música com volume e fade, emendar hook + Take 1 + corpo. Efeitos animados do CapCut (stickers, transições elaboradas) não: só entrada e saída com fade ou deslize simples.
- **Ainda não testado com um vídeo real do aluno** (tamanho máximo de anexo no chat a conferir no 1º envio).
