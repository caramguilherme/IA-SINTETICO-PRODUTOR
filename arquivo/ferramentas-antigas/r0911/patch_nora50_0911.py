# 09/11/2026: o nora50 não saiu em 07/11 (fim de semana sem post). Datas e story do painel atualizados para hoje.
# Uso: python3 -I ferramentas-painel/r0911/patch_nora50_0911.py  (na raiz do repositório)
import json, sys
R = sys.argv[1] if len(sys.argv) > 1 else '.'
t = open(f'{R}/PAINEL-NORA50.html', encoding='utf-8').read()
i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
p = json.loads(t[i:j])
c = p['central']
for k, txt in enumerate(c['passos']):
    if txt.startswith('Story:'):
        c['passos'][k] = ('Story: poste AGORA (o link está fora desde 07/11 18h43), no Insta e no Face: imagem story-3110, texto do story-0311 '
                          '("Tap below: your private reading is waiting for you before the 11:11 portal.") e adesivo "Open my reading" (seção Story). '
                          'Se o do Face travar em "Finalizando..." por mais de ~10 min, poste pelo Meta Business Suite.')
    c['passos'][k] = c['passos'][k].replace('me mande até umas 18h', 'me mande até umas 18h de hoje (09/11)')
    c['passos'][k] = c['passos'][k].replace('poste hoje (07/11) às 19h30', 'poste hoje (09/11) às 19h30')
    c['passos'][k] = c['passos'][k].replace('Use o Omni 1.1 Flash (o 1.2 cobra o dobro).', '**Troque para o Omni 1.1 Flash, 720p, antes de gerar** (o Flow abre no 1.2, que cobra o dobro).')
st = p['story']
st['nota'] = ('STORY (09/11): o story-0611 venceu em 07/11 18h43 e não houve repost no fim de semana. Poste agora, no Insta e no Face, '
              'o texto do story-0311 (3 toques em 18 viewers, contra 0 em 18 do story-0611). Se o do Face travar em "Finalizando...", poste pelo Meta Business Suite. '
              + st['nota'][st['nota'].find('Insta (STORYIG)'):] if 'Insta (STORYIG)' in st['nota'] else st['nota'])
for peca in p['pecas']['lista']:
    if peca.get('tipo') == 'story':
        peca['nome'] = 'story-0311 (repost agora, 09/11)'
        peca['descricao'] = ('Postar agora (link fora desde 07/11 18h43): imagem story-3110, texto "Tap below: your private reading is waiting for you before the 11:11 portal.", '
                             'adesivo "Open my reading".')
p['pecas']['decisao'] = [d.replace('07/11', '09/11') if 'Postar' in d or 'postar' in d else d for d in p['pecas']['decisao']]
p['pecas']['decisao'].append('09/11: o nora50 não saiu em 07/11 (fim de semana sem post); sai hoje às 19h30, no mesmo horário do nora49, junto com o nora51 (17h), o nora52 (22h) e o nora53 (00h30).')
novo = t[:i] + json.dumps(p, ensure_ascii=False) + t[j:]
open(f'{R}/PAINEL-NORA50.html', 'w', encoding='utf-8').write(novo)
print('ok')
