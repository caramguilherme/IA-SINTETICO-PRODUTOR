# 05/11 ~01h: nada saiu em 04/11 depois do nora47 (aluno). nora48 vai para 05/11 17h e nora49 para 19h30; story-0311 repostado já.
import re, json
rx = r'const PACOTE = (\{.*?\});\n'
def load(F):
    s = open(F, encoding='utf-8').read(); m = re.search(rx, s, re.S); return s, m, json.loads(m.group(1))
def save(F, s, m, P):
    s = s[:m.start()] + 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';\n' + s[m.end():]
    open(F, 'w', encoding='utf-8').write(s)
def sub(txt, old, new):
    assert old in txt, old; return txt.replace(old, new)
NOTA = ' 05/11 ~01h: nada saiu em 04/11 depois do nora47 (aluno); horários trocados para 05/11 (nora48 17h, nora49 19h30), story-0311 repostado já (o link estava fora desde 04/11 ~22h45). Conteúdo igual.'
# nora48
F = 'PAINEL-NORA48.html'; s, m, P = load(F)
c = P['central']['passos']
c[0] = 'Story AGORA (o link está fora desde 04/11 ~22h45): reposte o story-0311 (seção Story deste painel). Se não der agora, antes das 17h.'
c[6] = sub(c[6], 'poste às 19h30', 'poste hoje (05/11) às 17h')
P['story']['nota'] = sub(P['story']['nota'], 'REPOSTE O STORY ANTES DAS 19h30 (o story-0311 de ontem vence ~22h45; repostando agora ele cobre a noite toda)',
                         'REPOSTE O STORY AGORA, ou no máximo antes das 17h (o story-0311 venceu em 04/11 ~22h45 e o link está fora; repostado agora, vale até ~01h de 06/11 e cobre o nora48 e o nora49)')
for p in P['pecas']['lista']:
    if p['nome'] == 'story-0311 (repost)': p['descricao'] = 'Repostar agora (ou antes das 17h): mesma imagem, texto e adesivo.'
P['pecas']['decisao'][1] = sub(P['pecas']['decisao'][1], 'hoje o nora48', 'em 05/11 o nora48')
P['roteiro']['leitura_registro'] += NOTA
save(F, s, m, P)
# nora49
F = 'PAINEL-NORA49.html'; s, m, P = load(F)
c = P['central']['passos']
c[0] = 'Story: não precisa (vale o story-0311 repostado agora, de madrugada, ou antes do nora48).'
c[5] = sub(c[5], 'poste às 22h', 'poste hoje (05/11) às 19h30')
P['story']['nota'] = '✅ NÃO FAÇA STORY PARA ESTE VÍDEO: vale o story-0311 repostado em 05/11 (de madrugada ou antes do nora48).'
e = P['edicao_linha'][0]
e['como'] = sub(e['como'], 'É o vídeo que você exportou ontem sem texto', 'É o nora47-montado, o vídeo que você exportou sem texto para o nora47')
P['roteiro']['leitura_registro'] += NOTA
save(F, s, m, P)
print('ok')
