# Junta camadas de impact com os picos alinhados: python3 -I montar_impact.py saida.wav arq:db arq:db ...
import sys, subprocess, numpy as np
def pico(arq, sr=22050):
    raw = subprocess.run(['ffmpeg','-v','error','-i',arq,'-ac','1','-ar',str(sr),'-f','s16le','-'],capture_output=True,check=True).stdout
    a = np.frombuffer(raw,dtype=np.int16).astype(float)/32768; w=int(0.01*sr)
    e = np.array([np.sqrt(np.mean(a[i:i+w]**2)) for i in range(0,len(a)-w,w)]); return int(e.argmax())*0.01
saida, camadas = sys.argv[1], [c.rsplit(':',1) for c in sys.argv[2:]]
pk = [pico(a) for a,_ in camadas]; base = max(pk)
args=['ffmpeg','-v','error','-y']; fs=[]
for i,((a,db),p) in enumerate(zip(camadas,pk)):
    args+=['-i',a]; fs.append(f'[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={int((base-p)*1000)}:all=1[c{i}]')
fs.append(''.join(f'[c{i}]' for i in range(len(camadas)))+f'amix=inputs={len(camadas)}:normalize=0:duration=longest,atrim={max(0,base-0.35):.2f}:{base+1.3:.2f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.12,afade=t=out:st={min(base,0.35)+0.45:.2f}:d=0.7,alimiter=limit=0.97')
subprocess.run(args+['-filter_complex',';'.join(fs),saida],check=True); print(saida,'pico',base)
