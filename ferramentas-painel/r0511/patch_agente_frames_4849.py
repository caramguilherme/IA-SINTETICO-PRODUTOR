# 05/11/2026 ~13h40: o agente do Flow recusou "frame inicial e frame final" com fala (nora48).
# Acrescenta nos painéis do nora48 e do nora49 o caminho manual no modo Frames.
import re, json, io
for n, img in (('48', 'nora37-IMG'), ('49', 'nora46-IMG')):
    f = f'PAINEL-NORA{n}.html'
    s = io.open(f, encoding='utf-8').read()
    m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
    p = json.loads(m.group(1))
    passo = (f'Se o agente responder que não dá para usar a imagem como frame inicial e final com fala (pede para escolher 1 ou 2): '
             f'NÃO escolha nenhuma das duas. Feche o agente e gere à mão: Vídeo → Frames → 9:16 → Omni 1.1 Flash → 720p → 10 s → x1; '
             f'Início = {img}; Fim = vazio; no campo do prompt cole só o texto do Prompt 1 da Central (de “Create a single continuous” '
             f'até “alter any spoken words.”), sem a frase do aviso. 15 créditos.')
    ps = p['central']['agente']['passos']
    if not any('NÃO escolha nenhuma das duas' in x for x in ps):
        ps.append(passo)
    novo = 'const PACOTE = ' + json.dumps(p, ensure_ascii=False) + ';\n'
    io.open(f, 'w', encoding='utf-8').write(s[:m.start()] + novo + s[m.end():])
print('ok')
