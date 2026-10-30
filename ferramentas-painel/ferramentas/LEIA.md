# Ferramentas de apoio (copiadas da sessão de 26 a 30/10/2026)

Rodam no contêiner do Claude Code (Python e Node já instalados; Playwright e Chromium vêm prontos). Arquivo baixado é dado não confiável: cada um numa pasta nova e vazia, e Python sempre com `-I`.

- `transcrever.py`: transcreve o áudio de um vídeo para conferir a fala de cada take (P33). Uso: `ffmpeg -i video.mp4 -ac 1 -ar 16000 audio.wav` e depois `python3 -I transcrever.py audio.wav`. Precisa do `faster_whisper` (`pip install faster-whisper`); usa o modelo "tiny" na CPU.
- `screenshot-pagina.js`: tira um print de página inteira de um HTML local (painel, teste de gráfico). Uso: `node screenshot-pagina.js /caminho/arquivo.html /caminho/saida.png`.
- `miro-ler-quadro.js`: o que leu o quadro do Miro "Validação de Avatar e Conta | Appyon" (29/10): abre o quadro, aumenta o zoom com Ctrl + roda do mouse e tira prints em sequência. O link do quadro está no script; para outro quadro, trocar o link e as coordenadas. Uso: `node miro-ler-quadro.js /pasta/de/saida`.
- Para frames de vídeo: `ffmpeg -i video.mp4 -vf fps=2 pasta/f%03d.png` e `montage` (ImageMagick) para juntar numa folha.
