set -e
cd /workspace/IA-SINTETICO-PRODUTOR
V=$1
mkdir -p /tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/n74/out-$V
if [ "$V" = face ]; then EX=ferramentas-painel/ferramentas/specs/cortes-extra-nora74-FACE.json; else EX=; fi
python3 -I ferramentas-painel/dia-1911/editar_simples_1911.py /tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/n74/nora74-montado.mp4 /tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/n74/palavras.json ferramentas-painel/dia-2011/nora47-PRE-tsunami-inteiro-AB.mp4 /tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/n74/out-$V $V nora74 $EX
SUF=; [ "$V" = face ] && SUF=-FACE
python3 -I ferramentas-painel/dia-2311/spec_nora74.py /tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/n74/out-$V/mapa-$V.json /tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/n74/out-$V/nora74-final$SUF.mp4 /tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/n74/out-$V/spec.json $V
python3 -I ferramentas-painel/ferramentas/editar_video.py /tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/n74/out-$V/spec.json
echo FIM $V
