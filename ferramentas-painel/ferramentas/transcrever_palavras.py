import sys, wave, json
import numpy as np
from faster_whisper import WhisperModel
w = wave.open(sys.argv[1]); a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
m = WhisperModel("small", device="cpu", compute_type="int8")
segs, info = m.transcribe(a, language="en", word_timestamps=True, vad_filter=False,
    initial_prompt="Cancer, Scorpio or Pisces: 11:11, the year's most powerful portal. Archangel Michael. Comment 222.")
out=[]
for s in segs:
    print(f"{s.start:6.2f}-{s.end:6.2f} {s.text}")
    for wd in s.words: out.append([wd.word.strip(), round(wd.start,2), round(wd.end,2)])
json.dump(out, open(sys.argv[2],'w'), ensure_ascii=False)
