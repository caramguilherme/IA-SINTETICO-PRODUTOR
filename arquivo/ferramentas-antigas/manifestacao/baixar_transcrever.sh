#!/bin/bash
# baixa os reels e os ads do Drive da pesquisa de Manifestation e transcreve tudo
S="$1"; M="$S/manif"; LOG="$M/progresso.log"
cd "$M" || exit 1
python3 -I -c "
import json;d=json.load(open('$M/lista.json'))
open('$M/ig_ids.txt','w').write('\n'.join(x['id'] for x in d['ig'])+'\n')
open('$M/dr_ids.txt','w').write('\n'.join(x['id'] for x in d['drive'])+'\n')"
echo "$(date +%H:%M) baixando reels" >> "$LOG"
cat "$M/ig_ids.txt" | xargs -P 4 -I{} sh -c 'cd "'"$M"'/ig" && [ -f {}.mp4 ] || timeout 120 yt-dlp -q --no-warnings --write-info-json -o "%(id)s.%(ext)s" "https://www.instagram.com/reel/{}/" >/dev/null 2>&1 || echo "falhou ig {}" >> "'"$LOG"'"'
echo "$(date +%H:%M) reels: $(ls "$M"/ig/*.mp4 2>/dev/null | wc -l)" >> "$LOG"
cat "$M/dr_ids.txt" | xargs -P 4 -I{} sh -c 'f="'"$M"'/drive/{}.mp4"; [ -s "$f" ] || timeout 300 curl -sS -L -o "$f" "https://drive.usercontent.google.com/download?id={}&export=download&confirm=t" || echo "falhou drive {}" >> "'"$LOG"'"'
echo "$(date +%H:%M) ads: $(ls "$M"/drive/*.mp4 2>/dev/null | wc -l)" >> "$LOG"
python3 -I "$S/scripts/transcrever.py" "$M" >> "$LOG" 2>&1
echo "$(date +%H:%M) FIM" >> "$LOG"
