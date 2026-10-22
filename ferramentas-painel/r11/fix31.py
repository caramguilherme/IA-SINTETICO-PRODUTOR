import json, sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
i = [k for k, l in enumerate(lines) if l.startswith('const PACOTE = ')][0]
d = json.loads(lines[i][len('const PACOTE = '):].rstrip().rstrip(';'))
before = json.dumps({k: d[k] for k in ('videos', 'imagem_central', 'pre_gancho')}, ensure_ascii=False)

# 1) Passos: imagens primeiro, conferência antes de gastar crédito com vídeo
c = d['central']
c['passos'] = [
 "Pré-gancho (seção “Pré-gancho”): gere as 4 imagens, A, B, C e D, na ordem. Só aparecem as mãos da Nora. Ainda não gere os 2 vídeos.",
 "IMAGEM 1 na Central de imagens (seção “Imagem 1 na Central de imagens”, caixinha “já tenho o blueprint” marcada), campo por campo, anexando só o blueprint: a Nora segura a calcinha vermelha com o curativo com as DUAS mãos, na frente do peito. Aprove só se for a Nora v2 (olhos verde-avelã, lua com 3 estrelinhas na maçã do rosto, testa limpa, trança com anéis dourados, colar de Vênus), com o curativo no centro da calcinha e sem carimbo de data nos cantos.",
 "Me mande as 5 imagens (A, B, C, D e IMAGEM 1). Eu confiro as mãos, o curativo e a faixa da legenda e devolvo as 9 linhas de movimentação finais. Não gere os vídeos nem os takes antes disso.",
 "Depois do meu ok: os 2 vídeos do pré-gancho em FRAMES (A→B e C→D), 7 créditos cada.",
 "Na Central do curso, preencha a configuração (seção “Central do curso: o que preencher”) e faça a colagem única do nora31 (a fala inteira de uma vez, 9 takes). Clique em GERAR PROMPT DE ANIMAÇÃO e confira a lista de takes. Não clique em “Resetar valores” nem em “REGERAR BLOCO”.",
 "No agente do Flow, anexe a IMAGEM 1 aprovada (só ela; o blueprint não vai no agente), cole o aviso e, embaixo, o “COPIAR TUDO JUNTO” da Central, sem editar. Depois renomeie cada arquivo com o nome do painel. Custo: 132 créditos dos takes + 14 do pré-gancho = 146."
]

# 2) Critério de aprovação da IMAGEM 1 (estava "objeto na mão direita, esquerda livre")
ic = d['imagem_central'][0]
ic['passos'][3] = "Aprove só se for a Nora (olhos verde-avelã, a lua dourada com as 3 estrelinhas na maçã do rosto, testa limpa, trança com anéis dourados, colar de Vênus) segurando a calcinha vermelha com o curativo com as DUAS mãos, na frente do peito, sem cobrir o rosto."

# 3) Pré-gancho: título (sem rosto), duração, montagem e conferência das imagens
g = d['pre_gancho']
g['titulo_secao'] = "Pré-gancho (uns 4 s, 2 tomadas, só as mãos)"
g['duracao'] = 4
g['modo'] = "Gere as 4 imagens e me mande antes dos vídeos. Não aprove a A nem a C se aparecer o rosto, o corpo, texto ou marca no invólucro; na A não pode aparecer a calcinha. Cada vídeo: modo FRAMES, 4 s, 9:16, áudio ligado."
g['montagem'] = ("1) nora31-PRE-V1: use de 0,5 s a 2,5 s (rasga e tira o curativo).\n"
                 "2) Corte seco para nora31-PRE-V2: use de 0,8 s a 3,0 s (cola e alisa).\n"
                 "3) Corte seco para o corpo cortado (Take 1). O pré-gancho fica com uns 4 s, como nos virais w1 e w2.")

# 4) Texto na tela, em ordem
el = d['edicao_linha']
el[0] = {"quando": "1. Pré-gancho (2 tomadas, uns 4 s) até o fim da 1ª frase do Take 1",
         "texto": "What the hell did you just do?",
         "como": "Texto no topo, em 2 linhas, do segundo 0 do pré-gancho até o fim da frase falada “What the hell did you just do?” no Take 1."}
el[1]['como'] = "Caixa branca no topo. Entra na frase que começa em “Aries, Leo” e sai quando a frase termina em “watching this”."
el[2]['como'] = "Dois números fixos nos cantos de cima, em amarelo-ouro com contorno, do Take 1 até o fim: 222 à esquerda e 11:11 à direita (faixa azul do mapa da tela)."
el[3]['como'] = "Faixa verde do mapa da tela (69% a 77% da altura), sempre no mesmo lugar. Blocos de 2 a 3 palavras, nunca uma palavra só. Destaque amarelo-ouro em: portal, seal e stories."
el[4]['quando'] = "5. No pedido final (“Tap my profile picture and check my stories…”)"
el[4]['como'] = "Seta vermelha pequena apontando para a foto do perfil, no canto superior esquerdo, só durante essa frase."

# 5) Story: só o que vale enquanto o link abre o Soulmate (P37)
st = d['story']
st['textos'] = [{"posicao": "Uma frase só, no centro, uma cor (creme #F1E6D3), 1 a 2 linhas", "texto": "Tap below and take the free love quiz."}]
st['adesivos'] = ["Take the free quiz", "Open Part 2"]

# 6) Mapa da tela: faixa a confirmar com a IMAGEM 1
d['mapa_tela']['regras'][0] = "Neste vídeo a calcinha com o curativo fica na frente do peito: a legenda fica mais baixo (69% a 77%), em blocos de 2 a 3 palavras. Y da legenda no CapCut: −294. Confirmo a faixa quando você me mandar a IMAGEM 1."

# 7) Registro de leitura desta revisão
d['roteiro']['leitura_registro'] = ("22/10/2026 (conta nova): painel revisado com `CLAUDE.md`, `FATOS-DO-ALUNO.md`, `LEIA-TUDO-ANTES.md`, `LICOES-FLOW-E-PROMPTS.md` (inteiro), `BIBLIOTECA-VIDEOS-VIRAIS.md` (w1 e w2) e `PAINEL-MODELO.html`; corrigidos só os textos do painel, nenhum prompt nem fala mudou. " + d['roteiro']['leitura_registro'])

after = json.dumps({k: d[k] for k in ('videos', 'imagem_central', 'pre_gancho')}, ensure_ascii=False)
lines[i] = 'const PACOTE = ' + json.dumps(d, ensure_ascii=False) + ';'
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
# Conferência: falas, movimentação e prompts das imagens/vídeos iguais aos de antes
b, a = json.loads(before), json.loads(after)
assert b['videos'] == a['videos']
assert [x['prompt'] for x in b['pre_gancho']['etapas']] == [x['prompt'] for x in a['pre_gancho']['etapas']]
assert b['imagem_central'][0]['grupos'] == a['imagem_central'][0]['grupos']
assert d['central']['colagens'] == json.loads(open(p,encoding='utf-8').read().split('const PACOTE = ')[1].split(';\n')[0])['central']['colagens']
print('ok')
