import json,re,sys
D='/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/manif2710/'
exec(open(D+'falas.py').read())
s=open('PAINEL-NORA36.html',encoding='utf-8').read()
m=re.search(r'const PACOTE = (.*?);\n',s,re.S); p=json.loads(m.group(1))
pre="Throughout the whole 10 seconds both of her hands keep holding the two open halves of the gray geode at the height of her collarbones with their pink crystal insides facing the lens, her right hand on the left side of the frame holding the left half and her left hand on the right side of the frame holding the right half with the small gold symbol, and the halves never change hands, never close, never turn away, never drop and never cover her face, both hands stay on the halves with no other gestures, her eyes stay on the lens, and "
fim=", and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; everything else in the scene stays completely still and each hand has exactly five fingers."
mid=[
"during the first sentence of the take she holds a firm, serious look with her brows slightly lowered, during the last sentence she gives one short slow nod",
"during the first half of the take she tilts her head slightly to one side with a soft understanding look, during the second half she slowly straightens her head and narrows her eyes a little as if reading something",
"during the first sentence of the take she raises her eyebrows slightly, during the second sentence her eyes drop to the open halves for one moment and come back to the lens",
"during the first sentence of the take she takes one slow breath and her shoulders drop slightly with a soft half-smile, during the last sentence she gives one short nod",
"during the first sentence of the take her face turns serious and she leans her head and shoulders a little toward the lens, during the last sentence she slowly leans back to her first position",
"during the first sentence of the take she brings both open halves about 8 centimeters closer to the lens, keeping them apart and facing the lens, during the last sentence she slowly brings them back to their first position",
"during the first sentence of the take she slowly narrows her eyes as if looking at something far away, during the last sentence a soft half-smile appears and stays",
"during the whole take she holds a calm, steady look with her chin slightly raised, and during the last sentence she gives one slow nod",
"during the first half of the take she gives one short nod, during the second half she holds a warm, steady look",
"during the first sentence of the take she gives one short nod, during the last sentence she gives a second short nod",
"during the first sentence of the take her eyes drop to the open halves for one moment and come back to the lens, during the last sentence she holds a warm, steady look with a soft half-smile",
"during the whole take she keeps a warm, soft half-smile while speaking, and during the last sentence she raises both open halves about 5 centimeters and holds them there",
]
mov=[pre+x+fim for x in mid]
# checagem de sobreposição (P32): nenhuma sequência de 2 palavras da fala dentro da linha
comuns={'and it','of the','in the','on the','to the','the end','the lens','of her','her head','the take','the first','the last','she gives','one short','her eyes','for one','the open','a soft','and her','at the','her face','her first','the clip','she keeps'}
def bigr(t): w=re.findall(r"[a-z0-9:%']+",t.lower()); return {' '.join(w[i:i+2]) for i in range(len(w)-1)}
for i,(n,c,f) in enumerate(T):
    ov=(bigr(f)&bigr(mov[i]))-comuns
    if ov: print('SOBREPOSIÇÃO take',i+1,ov)
vids=[]
for i,(n,c,f) in enumerate(T):
    vids.append({'rotulo':'V%d'%(i+1),'cena':'Take %d/12 · %s'%(i+1,c),'duracao':'10','primeiro_quadro':'IMAGEM 1','acao':'(ver movimentação)','b_roll':'','fala':f,'movimentacao':mov[i],'arquivo':'nora36-'+n})
p['videos']=vids
r=p['roteiro']
r['titulo']='Série do geodo (Manifestation): Touro, Virgem e Capricórnio (o corpo A dos virais quase inteiro)'
r['dor']='as bênçãos e o dinheiro que não chegam; a virada que nunca vem (Manifestation, ângulo positivo de predestinação, P41)'
r['formato']='Hook visual pesado (geodo que racha, 4 s) + copy falada de 12 takes (corpo A dos virais, quase palavra por palavra)'
r['duracao_total']=95
r['descricao_instagram']="Taurus, Virgo, Capricorn: if this reached you, it's not by chance. 🔮\nComment 222. Tap my photo NOW: the second part of this sign is in my story.\n#manifestation #astrology #zodiac #usa #usareels"
r['leitura_registro']="27/10/2026 (troca para o Manifestation, P41): li nesta sessão, com a ferramenta de leitura, FATOS-DO-ALUNO.md, CLAUDE.md, 00-LEIA-PRIMEIRO.md, BRIEFING-MANIFESTACAO.md, PROJETO-Dana.md, LICOES-FLOW-E-PROMPTS.md (inteiro), ROTEIRO-NORA36 (inteiro), BIBLIOTECA-VIDEOS-VIRAIS.md (seções 20 a 39, com o corpo A inteiro e os 148 vídeos da pesquisa) e PAINEL-MODELO.html; COMUNIDADE-E-ESTRATEGIA.md e o Discord de 26/10 foram lidos e escritos nesta sessão. Os outros arquivos de LEIA-TUDO-ANTES.md foram lidos inteiros na montagem original deste painel (26/10). Mudaram só as falas, os textos da edição, a legenda, o comentário, o story e a lista de peças; as imagens, o pré-gancho e a Central não mudam."
p['texto_tela']['hook_termina']='this message is 100% meant for you'
p['comentario_fixado']={'insta':"Taurus, Virgo, Capricorn, this one is yours. 🔥 PART 2 of this sign is in my story: pick 3 cards and see what's coming for you. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222.",
 'face':"Taurus, Virgo, Capricorn, this one is yours. 🔥 PART 2 of this sign is in my Story: pick 3 cards and see what's coming for you. Tap my profile picture NOW, it's gone in 24 hours. Comment 222."}
c=p['central']
c['colagens']=[{'titulo':'nora36 completo (12 takes)','fala':' '.join(t[2] for t in T),'movimentacao':mov,'takes':list(range(12))}]
c['passos']=[
 'Pré-gancho e imagem (seção “Pré-gancho” e seção “Imagens”), na conta de 385 (a antiga de 437): gere a nora36-PRE-A (anexe SÓ o blueprint), a nora36-PRE-B (anexe SÓ a A) e a nora36-IMG (anexe SÓ a B). Imagem não gasta crédito. Me mande as 3 juntas.',
 'Depois do meu ok: o vídeo do pré-gancho em FRAMES (A → B), 4 s. 7 créditos. Renomeie para nora36-PRE. As linhas de movimentação de agora são provisórias: eu confirmo com a nora36-IMG.',
 'Central do curso: a configuração (seção “Central do curso”, com o texto LIVRE) e a colagem única (fala inteira + 12 linhas). Confira: 12 takes de 10 s.',
 'Agente do Flow: anexe só a nora36-IMG, cole o aviso e o “COPIAR TUDO JUNTO” da Central, sem editar. 180 créditos. Renomeie os takes com os nomes do painel. Guarde os takes 2 a 12 separados: o nora37 usa as cópias.',
 'Me mande a transcrição dos 12 takes antes de postar.',
 'Corte de silêncio só do corpo (seção “Cortar os silêncios”): suba os 12 takes de uma vez, com “Juntar tudo” ligado e Corte seco. CapCut: pré-gancho, corpo cortado, caixa do topo (desde o pré-gancho), legenda na tela, faixa do story (do Take 10 ao fim), seta vermelha (Takes 11 e 12) e a música de sempre (−18 dB).',
 'Antes de postar: troque o link do story, da bio e das respostas no Face para o link do Manifestation e poste o story novo (seção “Story”).',
 'Postar em 27/10 às 19h no Insta e no Face, ao vivo, com a localização Los Angeles, California no Insta. Se não ficar pronto, vai às 21h e o nora37 às 23h.']
c['agente']['aviso']='Vou te enviar 12 prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um com o devido número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.'
c['agente']['passos']=[x.replace('10 vídeos','12 vídeos') for x in c['agente']['passos']]
for sec in c['config']:
    for k in sec['campos']:
        if 'valor' in k and isinstance(k['valor'],str): k['valor']=k['valor'].replace('10 takes','12 takes')
p['story']['textos']=[{'posicao':'Uma frase só, no centro, uma cor (creme #F1E6D3), 1 a 2 linhas','texto':"Tap below: pick 3 cards and see what's coming for you."}]
p['story']['adesivos']=['Pick my 3 cards','See my cards']
p['story']['nota']='Use a imagem do story que você já tem: troque só o texto e o adesivo. Poste quando trocar o link para o do Manifestation, antes do nora36. Confira nos prints que o link abre as 3 cartas; se abrir outra coisa, me avise antes de postar.'
E=p['edicao_linha']
E[1]['quando']='1. Do primeiro quadro do pré-gancho até o fim do Take 1'
E[2]['como']='Faixa verde do mapa. Destaque em amarelo-ouro: money, prosperity, blessings, seal e 222.'
E[3]={'quando':'3. Do Take 10 até o fim','texto':'The second part is in my Stories ⭐','como':'Faixa no topo, no mesmo lugar da caixa (X 0 · Y 397): caixa branca arredondada, texto preto, “my Stories” em vermelho. Começa em “Now save this video”.'}
E[4]={'quando':'4. Nos Takes 11 e 12','texto':'Seta vermelha','como':'Embaixo à esquerda, apontando para baixo, para a foto do perfil, do “Comment 222” até o fim.'}
for e in p['mapa_tela']['estilos']:
    if e['nome'].startswith('Faixa do story'):
        e['nome']='Faixa do story no topo: “The second part is in my Stories ⭐”'
    if e['nome']=='Seta vermelha': e['obs']=e['obs'].replace('Takes 9 e 10','Takes 11 e 12')
nomes=[('nora36-T%s'%t[0][1:]) for t in T]
P=p['pecas']
keep=[x for x in P['lista'] if not x['nome'].startswith('nora36-T')]
for i,(n,cn,f) in enumerate(T):
    keep.append({'nome':'nora36-'+n,'tipo':'gancho' if i==0 else ('CTA' if i>=9 else 'corpo'),'status':'gerar','creditos':15,'descricao':'Take %d: “%s”'%(i+1,f),'base':'Corpo A dos virais (x1 a x5, a2, a3, w3 a w5, L1), frase %d, quase palavra por palavra (P41).'%(i+1),'serve':'Só deste vídeo (cada grupo de signos tem o seu Take 1).' if i==0 else 'nora37 e os próximos da série (cópia renomeada).'})
P['lista']=keep
P['decisao']=['Manifestation (P41): o corpo A dos virais volta quase palavra por palavra (dinheiro, prosperidade, São Miguel, 7 minutos, selos, 222, a notícia de amanhã); saem só a inveja e o bloqueio de amor, para o ângulo positivo mandar (aula do funil).','Hook visual pesado: o geodo que racha (3 de 5 vídeos da conta dos x).','Corpo gerado uma vez: o nora37 e os próximos só trocam o Take 1 (15 créditos cada).']
for x in P['proximos']:
    x['gancho']=re.sub(r"if this reached you on October 26th, 27th or 28th, it's meant for you\. Don't tell anyone\.|if this reached you on October 27th, 28th or 29th, it's meant for you\. Don't tell anyone\.","if this video reached you on October 27th, 28th or 29th, this message is 100% meant for you.",x['gancho'])
P['proximos'][0]['gancho']="Cancer, Scorpio or Pisces: if this video reached you on October 27th, 28th or 29th, this message is 100% meant for you."
open(D+'p36_novo.json','w',encoding='utf-8').write(json.dumps(p,ensure_ascii=False,indent=1))
novo=s[:m.start(1)]+json.dumps(p,ensure_ascii=False)+s[m.end(1):]
open('PAINEL-NORA36.html','w',encoding='utf-8').write(novo)
print('ok',len(p['videos']),sum(x.get('creditos',0) for x in P['lista'] if x['status']=='gerar'))
print([x['gancho'] for x in P['proximos']])
