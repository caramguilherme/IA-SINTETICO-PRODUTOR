import sys,os,glob,json,time,subprocess
import numpy as np
from faster_whisper import WhisperModel
M=sys.argv[1]
def audio(a):
    raw=subprocess.run(['ffmpeg','-nostdin','-v','quiet','-i',a,'-f','s16le','-ac','1','-ar','16000','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.int16).astype(np.float32)/32768.0
m=WhisperModel('small',device='cpu',compute_type='int8',cpu_threads=4)
arqs=sorted(glob.glob(M+'/ig/*.mp4'))+sorted(glob.glob(M+'/drive/*.mp4'))
for a in arqs:
    sub='ig' if '/ig/' in a else 'drive'
    out=f"{M}/txt/{sub}-{os.path.basename(a)[:-4]}.txt"
    if os.path.exists(out) or os.path.getsize(a)<10000: continue
    t0=time.time()
    try:
        segs,info=m.transcribe(audio(a),beam_size=1,vad_filter=True)
        linhas=[f"[{s.start:6.1f}-{s.end:6.1f}] {s.text.strip()}" for s in segs]
        open(out,'w',encoding='utf-8').write(f"# {sub} {os.path.basename(a)} lang={info.language} dur={info.duration:.0f}s\n"+'\n'.join(linhas)+'\n')
        print(time.strftime('%H:%M'),'ok',sub,os.path.basename(a),f'{info.duration:.0f}s em {time.time()-t0:.0f}s',flush=True)
    except Exception as e:
        print('erro',a,e,flush=True)
