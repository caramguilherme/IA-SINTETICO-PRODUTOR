# 27/10 ~16h: link só no story (Insta e Face), sem link na bio nem nos comentários;
# no Face não dá mais para fixar comentário. O story do Manifestation vai antes do nora36 (17h).
import re, json, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else '.'
COMENT = " Comentário: no Insta, comente e fixe (sem link); no Face, só comente (não fixa mais)."
STORY_36 = ("Antes do nora36 (17h): troque o link do story para o do Manifestation, no Insta e no Face "
            "(o story é o único lugar com link), e poste este story nos dois. Use a imagem do story que você já tem: "
            "troque só o texto e o adesivo. Confira nos prints que o link abre as 3 cartas; se abrir outra coisa, "
            "me avise antes de postar.")
STORY_DEPOIS = "O story do Manifestation postado antes do nora36 (3 cartas) vale para este vídeo: não precisa postar outro."

def patch(nome, fn):
    path = f"{BASE}/{nome}"
    s = open(path, encoding='utf-8').read()
    m = re.search(r'const PACOTE = (\{.*?\});\n', s, re.S)
    p = json.loads(m.group(1))
    fn(p)
    novo = json.dumps(p, ensure_ascii=False)
    s = s[:m.start(1)] + novo + s[m.end(1):]
    open(path, 'w', encoding='utf-8').write(s)

def n36(p):
    p['story']['nota'] = STORY_36
    ps = p['central']['passos']
    ps[4] = ("Antes de postar: troque o link do story (Insta e Face) para o do Manifestation e poste o story novo (seção “Story”). "
             "Postar em 27/10 às 17h no Insta e no Face, ao vivo, com a localização Los Angeles, California no Insta." + COMENT)

def n37(p):
    p['story']['nota'] = STORY_DEPOIS
    ps = p['central']['passos']
    assert ps[6].startswith('Antes de postar: troque o link')
    del ps[6]
    ps[6] = ps[6] + " O story do Manifestation (3 cartas) tem de estar no ar." + COMENT

def n39(p):
    p['story']['nota'] = STORY_DEPOIS
    p['central']['passos'][6] += COMENT

def placa(p):
    p['central']['passos'][4] += COMENT

patch('PAINEL-NORA36.html', n36)
patch('PAINEL-NORA37.html', n37)
patch('PAINEL-NORA38.html', placa)
patch('PAINEL-NORA39.html', n39)
patch('PAINEL-NORA40.html', placa)
print('ok')
