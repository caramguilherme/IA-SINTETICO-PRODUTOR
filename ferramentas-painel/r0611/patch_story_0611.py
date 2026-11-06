# 06/11/2026 ~18h15: story-0611 no painel do nora49 (mesma imagem story-3110; texto e adesivo no padrão
# das contas mineradas: claire_mayaus, iamlinda.bennett, eduardameirelless, jonhsonclark5).
import json, sys
R = sys.argv[1] if len(sys.argv) > 1 else '.'
f = f'{R}/PAINEL-NORA49.html'
t = open(f, encoding='utf-8').read()
i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
p = json.loads(t[i:j])
IG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
s = p['story']
s['prompt_imagem'] = '(Não gere imagem: use a story-3110 de novo. Só o texto e o adesivo mudam: story-0611.)'
s['textos'][0]['texto'] = "You're not here by accident. ✨\nYour private reading is waiting below."
s['adesivos'] = ['Your reading 🗝️']
s['nota'] = ('STORY NOVO (story-0611): poste agora, no Insta e no Face, com a mesma imagem (story-3110), o texto novo em 2 linhas '
             'e o adesivo de link "Your reading 🗝️" (no lugar de sempre, na mesa). Se der: um GIF de mãozinha apontando para o link '
             '(busque "tap here" nos GIFs) e uma música de piano calma (busque "Andrea Vanzo"). Confira na prévia o link de cada rede. '
             'Insta (STORYIG): ' + IG + ' · Face (FACE): ' + FB)
for x in p['pecas']['lista']:
    if x.get('tipo') == 'story':
        x.update({'nome': 'story-0611', 'de': 'story-3110', 'status': 'reutilizar',
                  'descricao': 'A imagem story-3110 com o texto e o adesivo novos (seção Story); poste agora, antes do nora49.'})
p['central']['passos'] = [('Story: poste agora o story-0611 (seção Story): mesma imagem story-3110, texto e adesivo novos, '
                'com o link certo de cada rede.') if x.startswith('Story:') else x for x in p['central']['passos']]
novo = t[:i] + json.dumps(p, ensure_ascii=False) + t[j:]
open(f, 'w', encoding='utf-8').write(novo)
print('ok', len(novo))
