set -e
# Uso: bash rodar_nora77.sh insta|face   (24/11: o montado único; separar_takes_2411.py já gravou o montado do Face e os cortes-extra)
cd /workspace/IA-SINTETICO-PRODUTOR
V=$1; D=/tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/n77
mkdir -p $D/out-$V
if [ "$V" = face ]; then M=$D/nora77-montado-FACE.mp4; P=$D/palavras-nora77-FACE.json; EX=$D/cortes-extra-nora77-face.json; SUF=-FACE
else M=$D/drive/nora77-montado.mp4; P=$D/palavras-nora77-insta.json; EX=$D/cortes-extra-nora77-insta.json; SUF=; fi
# o corpo é novo também no Face (gerado de novo, com o T14 novo): sem a variação do Face, como o nora75-FACE ("insta" no passo 1)
X1111=0.82 python3 -I ferramentas-painel/dia-2311/editar_simples_2311.py $M $P none $D/out-$V insta nora77 $EX
if [ "$V" = face ]; then python3 -I ferramentas-painel/dia-2411/spec_face_comentario.py $D/out-$V/mapa-insta.json $D/out-$V/nora77-final$SUF.mp4 $D/out-$V/spec.json
else python3 -I ferramentas-painel/dia-2311/spec_simples_2311.py $D/out-$V/mapa-insta.json $D/out-$V/nora77-final$SUF.mp4 $D/out-$V/spec.json $V; fi
python3 -I ferramentas-painel/ferramentas/editar_video.py $D/out-$V/spec.json
echo FIM $V
