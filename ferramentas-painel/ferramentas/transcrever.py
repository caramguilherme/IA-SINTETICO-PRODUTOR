import sys, wave
import numpy as np
from faster_whisper import WhisperModel
w = wave.open(sys.argv[1]); a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
m = WhisperModel("tiny", device="cpu", compute_type="int8")
segs, info = m.transcribe(a, vad_filter=True)
print("lang", info.language, round(info.language_probability, 2))
for s in segs:
    print(f"{s.start:5.1f}-{s.end:5.1f} {s.text} (nospeech={s.no_speech_prob:.2f})")
