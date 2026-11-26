set -e
# Uso: bash rodar_2611.sh noraNN insta|face  (26/11; o separar_takes_2611.py já gravou o montado do Face, as palavras e os cortes-extra)
cd /workspace/IA-SINTETICO-PRODUTOR
NN=$1; V=$2; D=/tmp/claude-0/-workspace-IA-SINTETICO-PRODUTOR/0f1d3084-6c9c-5025-9335-535fd154c68d/scratchpad/${NN#nora}; D=${D%/*}/n${NN#nora}
mkdir -p $D/out-$V
if [ "$V" = face ]; then M=$D/$NN-montado-FACE.mp4; P=$D/palavras-$NN-FACE.json; EX=$D/cortes-extra-$NN-face.json; SUF=-FACE
else M=$D/$NN-montado.mp4; P=$D/palavras.json; EX=$D/cortes-extra-$NN-insta.json; SUF=; fi
# o corpo é gerado de novo também no Face (com o T14 novo): sem a variação do Face, como o nora77-FACE ("insta" no passo 1)
X1111=0.82 YLEG=${YLEG:-0.775} python3 -I ferramentas-painel/dia-2311/editar_simples_2311.py $M $P none $D/out-$V insta $NN $EX
if [ "$V" = face ]; then python3 -I ferramentas-painel/dia-2411/spec_face_comentario.py $D/out-$V/mapa-insta.json $D/out-$V/$NN-final$SUF.mp4 $D/out-$V/spec.json
else python3 -I ferramentas-painel/dia-2311/spec_simples_2311.py $D/out-$V/mapa-insta.json $D/out-$V/$NN-final$SUF.mp4 $D/out-$V/spec.json $V; fi
python3 -I ferramentas-painel/ferramentas/editar_video.py $D/out-$V/spec.json
echo FIM $NN $V
