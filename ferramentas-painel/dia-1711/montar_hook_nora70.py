"""Hook do nora70 (modelo do v6 da claire_mayaus): 2 tomadas, ~6,5 s, sem texto (o v6 não tem), o som do ambiente de cada clipe,
e o flash branco nos últimos 0,15 s. Os clipes do Muse saem em 672x1216 ou 704x1232: escala pela largura e corta o alto e o baixo
(sem esticar). A tomada 1 para em 4,6 s porque depois dos ~4,7 s o Muse trocou o rosto e a estátua (19/11)."""
import subprocess, sys, os
C1, C2, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
W, H = 1080, 1920
SEG = [(C1, 0.00, 4.60),   # aberto, de costas: abre o alçapão, põe a mão lá dentro e tira a estátua
       (C2, 0.55, 2.45)]   # close: sopra a poeira da estátua na direção da lente
pasta = os.path.dirname(os.path.abspath(OUT)); parts = []
for n, (f, a, b) in enumerate(SEG):
    p = os.path.join(pasta, f"h70seg{n}.mp4"); dur = b - a
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a}", "-t", f"{dur}", "-i", f,
        "-vf", f"scale={W}:-2,crop={W}:{H},fps=30,setsar=1",
        "-af", f"aresample=48000,afade=t=in:d=0.015,afade=t=out:st={dur-0.015:.3f}:d=0.015",
        "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", p], check=True)
    parts.append(p)
lst = os.path.join(pasta, "h70lista.txt"); open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
cru = os.path.join(pasta, "hook70-sem-texto.mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264", "-crf", "16",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", cru], check=True)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", cru], capture_output=True, text=True).stdout)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", cru, "-vf", f"fade=t=out:st={dur-0.15:.3f}:d=0.15:color=white",
                "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "copy", OUT], check=True)
print("hook:", round(dur, 2), "s ->", OUT)
