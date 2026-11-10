# 09/11/2026 ~23h15, pedido do aluno: os números seguem a ordem de postagem.
# Antes: nora50 = pedra (teste), nora51 = terra, nora52 = água, nora53 = fogo (00h30 de 09/11).
# Agora: nora50 = fogo (postado na 00h30 de 09 para 10/11), nora51 = terra (10/11 17h),
#        nora52 = pedra, o teste do gancho (10/11 19h30), nora53 = água (10/11 22h).
# Rodar UMA vez, depois de patch_nora50.py, patch_nora50_0911.py e patch_nora51_53.py.
import json, re, sys
R = sys.argv[1] if len(sys.argv) > 1 else '.'
MAPA = {'50': '52', '51': '51', '52': '53', '53': '50'}
def ler(n):
    t = open(f'{R}/PAINEL-NORA{n}.html', encoding='utf-8').read()
    i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
    return t, i, j, json.loads(t[i:j])
STORY_PASSO = ('Story: o story-0311 está no ar desde 09/11 às 22h55 (Face e Insta) e vence ~22h55 de 10/11. '
               'Reposte antes disso, com o mesmo texto ("Tap below: your private reading is waiting for you before the 11:11 portal.") e o adesivo "Open my reading".')
novos = {}
for velho, novo in MAPA.items():
    t, i, j, p = ler(velho)
    s = json.dumps(p, ensure_ascii=False)
    s = re.sub(r'nora(5[0-3])', lambda m: 'nora' + MAPA[m.group(1)], s)
    s = re.sub(r'NORA(5[0-3])', lambda m: 'NORA' + MAPA[m.group(1)], s)
    p = json.loads(s)
    c = p['central']
    for k, x in enumerate(c['passos']):
        if x.startswith('Story:'):
            c['passos'][k] = STORY_PASSO if novo != '50' else 'Story: já está no ar (story-0311, postado às 22h55 de 09/11). Nada a fazer aqui.'
        x = c['passos'][k]
        x = x.replace('poste hoje (09/11) às 17h', 'poste em 10/11 às 17h').replace('poste hoje (09/11) às 22h', 'poste em 10/11 às 22h')
        x = x.replace('poste hoje (09/11) às 19h30', 'poste em 10/11 às 19h30').replace('me mande até umas 18h de hoje (09/11)', 'me mande até umas 18h30 de 10/11')
        c['passos'][k] = x
    p['story']['nota'] = ('STORY: o story-0311 está no ar desde 09/11 às 22h55 (Face e Insta), com o texto "Tap below: your private reading is waiting for you before the 11:11 portal." '
                          'e o adesivo "Open my reading" (imagem story-3110). Vence ~22h55 de 10/11: reposte antes, igual. ' +
                          p['story']['nota'][p['story']['nota'].find('Insta (STORYIG)'):] if 'Insta (STORYIG)' in p['story']['nota'] else STORY_PASSO)
    for peca in p['pecas']['lista']:
        if peca.get('tipo') == 'story':
            peca['nome'] = 'story-0311 (no ar desde 09/11 22h55)'
            peca['descricao'] = 'Já postado às 22h55 de 09/11; vence ~22h55 de 10/11: repostar antes, igual.'
    dec = [d for d in p['pecas']['decisao'] if not d.startswith('09/11: o nora')]
    dec = [d.replace('Horário: 17h de 09/11', 'Horário: 17h de 10/11').replace('Horário: 22h de 09/11', 'Horário: 22h de 10/11') for d in dec]
    dec.append(f'Renumerado em 09/11 ~23h15 (pedido do aluno: os números seguem a ordem de postagem): era o nora{velho}. '
               'nora50 = Áries, Leão e Sagitário (00h30 de 09 para 10/11) · nora51 = terra (10/11 17h) · nora52 = a pedra, o teste do gancho (10/11 19h30) · nora53 = água (10/11 22h).')
    p['pecas']['decisao'] = dec
    if novo == '52':
        p['roteiro']['leitura_registro'] += ' | 09/11 ~23h15: renumerado de nora50 para nora52 (o arquivo do Take 1 passa a ser nora52-T01-gancho-portal-gemeos-libra-aquario).'
    novos[novo] = (t, i, j, p)
for novo, (t, i, j, p) in novos.items():
    html = t[:i] + json.dumps(p, ensure_ascii=False) + t[j:]
    html = re.sub(r'<title>Painel nora5[0-3]', f'<title>Painel nora{novo}', html)
    open(f'{R}/PAINEL-NORA{novo}.html', 'w', encoding='utf-8').write(html)
    print('ok', novo, p['videos'][0]['arquivo'])
