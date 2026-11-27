#!/bin/bash
# Baixa uma aula da área de membros do MVM (Panda Video) pelo id do embed (o "v=" do link player-vz-…/embed/?v=…), em 480p.
# Precisa dos 3 endereços liberados na rede (27/11): player-vz-cf4d4554-397.tv.pandavideo.com.br, b-vz-cf4d4554-397.tv.pandavideo.com.br e cdn.pandavideo.com.
# O ffmpeg não pega o proxy sozinho: vai com -http_proxy e -ca_file. A porta do proxy pode mudar: conferir o HTTPS_PROXY.
# uso: baixar_panda.sh <video_id> <saida.mp4>
V=$1; OUT=$2
B="https://b-vz-cf4d4554-397.tv.pandavideo.com.br/$V"
H=$'Referer: https://player-vz-cf4d4554-397.tv.pandavideo.com.br/\r\nOrigin: https://player-vz-cf4d4554-397.tv.pandavideo.com.br\r\n'
P=${HTTPS_PROXY:-http://127.0.0.1:34801}; CA=/root/.ccr/ca-bundle.crt
for i in 1 2 3; do
  ffmpeg -v error -y -http_proxy $P -ca_file $CA -headers "$H" -i "$B/480p/video.m3u8" -http_proxy $P -ca_file $CA -headers "$H" -i "$B/480p/audio.m3u8" -map 0:v -map 1:a -c copy "$OUT" && break
  sleep 15
done
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
