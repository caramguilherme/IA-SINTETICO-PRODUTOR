# 29/10/2026 ~17h: no "Estilo de cada texto" do nora40 e do nora42 o nome da caixa do topo veio do nora37
# ("Taurus, Virgo, Capricorn"). Troca pelos signos de cada vídeo (o texto_tela e a edição já estavam certos).
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'
SIG = {40: 'Aries, Leo, Sagittarius', 42: 'Gemini, Libra, Aquarius'}
for n, sig in SIG.items():
    f = f'{BASE}/PAINEL-NORA{n}.html'
    s = open(f, encoding='utf-8').read()
    m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
    p = json.loads(m.group(1))
    st = p['mapa_tela']['estilos'][1]
    assert 'Taurus, Virgo, Capricorn' in st['nome'], st['nome']
    st['nome'] = st['nome'].replace('Taurus, Virgo, Capricorn', sig)
    assert p['texto_tela']['hook'].startswith(sig), p['texto_tela']['hook']
    open(f, 'w', encoding='utf-8').write(s[:m.start(1)] + json.dumps(p, ensure_ascii=False) + s[m.end(1):])
    print(n, '|', st['nome'], '|', p['texto_tela']['hook'], '|', p['edicao_linha'][1]['texto'] if len(p['edicao_linha']) > 1 else '')
