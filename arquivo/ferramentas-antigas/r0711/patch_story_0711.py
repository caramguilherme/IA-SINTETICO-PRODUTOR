# 07/11/2026 ~09h20: o story-0611 ("You're not here by accident…") teve 0 toque em 18 viewers com ~14h22;
# o story-0311 ("Tap below: your private reading is waiting for you before the 11:11 portal.") teve 3 em 18.
# Decisão: repostar com o texto do story-0311, às ~18h (antes de vencer às 18h43 e antes do nora50 das 19h30).
# Uso: python3 -I ferramentas-painel/r0711/patch_story_0711.py  (na raiz do repositório)
import json, sys
R = sys.argv[1] if len(sys.argv) > 1 else '.'
t = open(f'{R}/PAINEL-NORA50.html', encoding='utf-8').read()
i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
p = json.loads(t[i:j])
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
IG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
st = p['story']
st['prompt_imagem'] = '(Não gere imagem: use a story-3110 de novo. Volta o texto e o adesivo do story-0311.)'
st['anexar'] = 'Nada: a imagem é a story-3110, que você já tem.'
st['textos'][0]['texto'] = 'Tap below: your private reading is waiting for you before the 11:11 portal.'
st['adesivos'] = ['Open my reading']
st['nota'] = ('STORY (decidido em 07/11 ~09h20, com os números das 09h05): o story-0611 ("You\'re not here by accident…") teve 19 views, 18 viewers, '
              '89,5% seguidores e 0 toque no link; o story-0311 ("Tap below: your private reading is waiting for you before the 11:11 portal.") '
              'teve 3 toques em 18 viewers. Volta o texto do story-0311, que diz o que fazer e o que tem lá. '
              'Reposte às ~18h (o story-0611 vence às 18h43; o nora50 sai às 19h30), no Insta e no Face, com o link certo de cada rede. '
              'Não precisa me mandar os números do story às 17h. '
              f'Insta (STORYIG): {IG} · Face (FACE): {FB}')
for peca in p['pecas']['lista']:
    if peca.get('tipo') == 'story':
        peca['nome'] = 'story-0311 (repost às ~18h)'
        peca['descricao'] = ('Repostar às ~18h, antes de vencer o story-0611 (18h43) e antes do nora50 (19h30): imagem story-3110, '
                             'texto "Tap below: your private reading is waiting for you before the 11:11 portal.", adesivo "Open my reading".')
novo = t[:i] + json.dumps(p, ensure_ascii=False) + t[j:]
open(f'{R}/PAINEL-NORA50.html', 'w', encoding='utf-8').write(novo)
print('ok', len(novo))
