# 28/10 ~13h: nora37-IMG aprovada. Ajusta o LIVRE da Central (nora37 e nora39) ao enquadramento real da imagem
# (da cabeça à cintura, metades logo abaixo do queixo, trança não aparece) e tira o "levantar as metades" do Take 3.
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'
REPS = [
 ("her long black wavy hair, her braid with gold rings, her gold moon", "her long black wavy hair, her gold moon"),
 ("she is framed from the top of her head to just below her collarbones, with her face large and centered in the upper half of the frame;",
  "the framing is exactly the one of the reference image, from a little above the top of her head down to her waist, with her face large and centered in the upper half of the frame and her eyes at about 35 percent of the frame height;"),
 ("both hands hold the two open halves of the gray geode at the height of her collarbones with",
  "both hands hold the two open halves of the gray geode just below her chin, at the height of her collarbones, with"),
 ("the camera is a handheld phone at the height of her collarbones about 55 centimeters from her",
  "the camera is a handheld phone at the height of her collarbones about 70 centimeters from her"),
 ("during the last sentence she raises both open halves about 5 centimeters and holds them there,",
  "during the last sentence she tilts her head slightly to one side with a knowing look,"),
]
def troca(o):
    if isinstance(o, dict): return {k: troca(v) for k, v in o.items()}
    if isinstance(o, list): return [troca(v) for v in o]
    if isinstance(o, str):
        for a, b in REPS: o = o.replace(a, b)
    return o
for nome in ('PAINEL-NORA37.html', 'PAINEL-NORA39.html'):
    s = open(f'{BASE}/{nome}', encoding='utf-8').read()
    m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
    p = troca(json.loads(m.group(1)))
    novo = json.dumps(p, ensure_ascii=False)
    for a, b in REPS[:4]:
        assert a not in novo, (nome, a[:40])
    open(f'{BASE}/{nome}', 'w', encoding='utf-8').write(s[:m.start(1)] + novo + s[m.end(1):])
print('ok')
