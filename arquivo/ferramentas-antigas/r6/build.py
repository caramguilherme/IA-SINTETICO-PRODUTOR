# -*- coding: utf-8 -*-
import sys,json,copy; sys.path.insert(0,'.'); sys.path.insert(0,'..')
import data, reuse, prompts as P
SP='/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/'
ROOT='/home/user/IA-SINTETICO-PRODUTOR/'
base=json.load(open(SP+'pacote_r004.json'))
VOZ='Voz feminina adulta americana (inglês dos EUA), natural e espontânea, calorosa e firme.'
LEIT=("19/10/2026: li inteiros todos os arquivos de LEIA-TUDO-ANTES.md e o briefing do Love Chart (BRIEFING-LOVECHART.md) antes de escrever o roteiro; a lista completa está no registro do roteiro. Antes de gerar os prompts conferi o checklist de LICOES-FLOW-E-PROMPTS.md (seção 1), o GUIA-CREATIVE-HUB.md e o CHECKLIST-DE-PRODUCAO.md.")
OBJ_PT={'nora25':'o pingente de cobre com o ♀','nora26':'a pedra-da-lua','nora27':'a carta Os Enamorados','nora28':'o mapa astral com o círculo vermelho'}
PRE_EDIT={
'nora25':'Aviso do pré-gancho: se o Flow não soltar o pó da palma (a nuvem não aparece), refaça o vídeo; não gaste mais de 2 tentativas antes de me chamar.',
'nora26':'Aviso do pré-gancho: a linha de fogo já falhou no R003. Se a imagem 1 já sair com a linha toda em chamas, ou se o vídeo não espalhar o fogo, não insista: peça o plano B (fumaça, como no nora28).',
'nora27':'Aviso do pré-gancho: se o Flow não entender a portinhola, plano B: uma caixa de madeira escura, a tampa se abrindo e a carta dentro.',
'nora28':''}
CODE={'nora25':'VENUS','nora26':'MOON','nora27':'MATCH','nora28':'CHART'}
DEST={'nora25':'Venus e pattern','nora26':'Moon','nora27':'second','nora28':'Venus'}
CORTE={'nora25':'corte quando a nuvem de pó cobrir o quadro e entre o Take 1','nora26':'corte seco do vídeo 1 para o vídeo 2 e, depois do fogo correr pelo corredor, entra o Take 1','nora27':'corte seco do vídeo 1 para o vídeo 2 e, depois da carta aparecer, entra o Take 1','nora28':'corte seco do vídeo 1 para o vídeo 2 e, depois da fumaça encher o quadro, entra o Take 1'}
def EDLINE(k):
    v=data.V[k]; w=CODE[k]; ht=v['hooktext']; pre=v['pre']
    return [
     {"quando":"1. Pré-gancho (%s, no começo do vídeo)"%("2 tomadas, uns %d s no total"%(5 if k=="nora26" else 6) if k in ("nora26","nora27","nora28") else "o arquivo de %d s"%pre['dur']),"texto":pre['texto'],"como":"Texto no topo, em até 2 linhas, durante os primeiros 3 segundos. Some junto com o pré-gancho (%s). Sem música."%CORTE[k]},
     {"quando":"2. Take 1 (o gancho falado)","texto":ht[0],"como":"Aparece na frase que começa em “%s” e some quando a frase termina em “%s”."%(ht[1],ht[2])},
     {"quando":"3. Do take 1 até o último segundo (o corpo todo)","texto":w,"como":"A palavra-código fica FIXA no canto superior direito, pequena, em maiúsculas, branca com contorno, durante o corpo inteiro. É o que a pessoa vai digitar nos comentários. Estilo dos virais V3, R03, R04, R06, R08, R09 (222 e 11:11 fixos no topo)."},
     {"quando":"4. Do take 1 até o último segundo","texto":"Legenda palavra a palavra","como":"Legendas automáticas do CapCut, letra grande no meio da tela. Destaque em cor (amarelo ou dourado) nas palavras: %s."%DEST[k]},
     {"quando":"5. No pedido final (“%s”)"%("tap my photo, open my story" if k=="nora27" else "Tap my photo and open my story…"),"texto":"Seta vermelha","como":"Uma seta vermelha pequena apontando para a foto do perfil, no canto superior esquerdo, só durante essa frase."}]
CRED={4:7,6:10,8:12,10:15}
def pack(k):
    v=data.V[k]; n=len(v['takes']); d=copy.deepcopy(base)
    full=' '.join(t[2] for t in v['takes'])
    pre=v['pre']
    d['roteiro']={"id":v['id'],"titulo":v['titulo'],"dor":v['dor'],"formato":v['formato'],"molde_hook":v['molde'],"duracao_total":pre['dur']+n*10,"descricao_instagram":v['legenda'],"leitura_registro":LEIT}
    d['perfil']={"nome":"Nora","teste":"A","voz":VOZ}
    d['refs']=['blueprint da Nora v2 (folha de consistência do personagem, baixada em 1K)']
    d['trava_referencia']=P.TRAVA
    d['figurino']=P.FIG[k]
    d['imagens']=[{"rotulo":"IMAGEM 1","cena":"Gerada na Central de imagens (campos no painel)."}]
    ic=P.CENTRAL(k); ic['titulo']='IMAGEM 1 (Central de imagens)'; ic['nome']=k+'-IMG'
    d['imagem_central']=[ic]
    d.pop('instrucoes_agente',None)
    d['videos']=[{"rotulo":"V%d"%(i+1),"cena":"Take %d/%d · %s"%(i+1,n,t[0]),"duracao":10,"primeiro_quadro":"IMAGEM 1","acao":"(ver movimentação)","b_roll":"","fala":t[2],"movimentacao":P.MOVL[k][i],"arquivo":v['tnames'][i]} for i,t in enumerate(v['takes'])]
    d['texto_tela']={"hook":v['hooktext'][0],"hook_comeca":v['hooktext'][1],"hook_termina":v['hooktext'][2],"hook_alt":"","extras":[]}
    d['comentario_fixado']={"insta":v['pin_ig'],"face":v['pin_fb']}
    d['edicao_linha']=EDLINE(k)
    d['pre_gancho']={"duracao":pre['dur'],"com_rosto":True,
      "nome_img1":k+"-PRE-IMG1","nome_img2":k+"-PRE-IMG2","nome_video":k+"-PRE",
      "conceito":"Modelo nos virais: "+pre['viral']+". "+pre['conceito'],
      "imagem_prompt":P.PRE[k]['img1'],"imagem_final_prompt":P.PRE[k]['img2'],"video_prompt":P.PRE[k]['vid'],
      "texto_tela":pre['texto'],"edicao":PRE_EDIT[k],
      "quadro_inicial":{'nora25':'o pó dourado está todo na palma estendida para a lente e ela faz biquinho para soprar; não há pó no ar; o pingente de cobre pende da outra mão',
        'nora26':'NENHUMA folha está queimando (a linha inteira, que vem para a câmera, está apagada); o palito está ACESO na mão direita dela, apoiada na coxa; a vela perto da câmera está acesa',
        'nora27':'a portinhola do chão está FECHADA e a mão dela está na argola',
        'nora28':'o círculo de sal parado e só um fio fino de fumaça sobe da brasa'}[k],
      "quadro_final":{'nora25':'o pó dourado enche a frente do quadro, grande e desfocado perto da lente, e o rosto dela aparece suave por trás; a palma está quase vazia',
        'nora26':'a linha inteira de folhas de louro está em chamas, dos joelhos dela até a vela perto da câmera; a mão direita está vazia na coxa (o palito sumiu); nenhuma chama toca a roupa dela',
        'nora27':'a portinhola está ABERTA e a carta aparece no vão',
        'nora28':'uma coluna grossa de fumaça sobe do centro do círculo e enche o meio do quadro'}[k]}
    if k=='nora26':
        d['pre_gancho'].update(etapas=P.ETAPAS26,duracao=5,tomadas=2,montagem=P.MONT26,
          conceito="Modelo nos virais: R09 (câmera rente ao chão, rosto grande, fogo alto que corre pelo corredor escuro com o fogo iluminando tudo) e R01 e S2 (duas tomadas com corte seco, algo novo a cada segundo). Duas tomadas de 4 s: (1) ela acende a primeira folha de louro com o palito e o fogo salta, o rosto dela se ilumina; (2) a câmera no chão vê o fogo correr pela linha até a vela, o corredor todo laranja. Corredor escuro: a única luz é o fogo e a vela.",
          modo="Quatro imagens e dois vídeos, na ordem dos números. Os dois vídeos são em FRAMES (primeiro e último quadro). A tomada 1 mostra o rosto da Nora: se a imagem A não vier com o rosto dela, descarte e gere de novo. A tomada 2 não mostra o rosto.")
    if k=='nora27':
        d['pre_gancho'].update(etapas=P.ETAPAS27,duracao=6,tomadas=2,montagem=P.MONT27,
          conceito="Modelo nos virais: U7 (ela levanta o tapete e uma tábua do piso e revela um compartimento escondido, com o texto \"It happens so fast, it's almost scary\"; 8 ações em uns 4 s) e R01 (corte seco para um plano bem perto do objeto). Duas tomadas de 4 s: (1) a câmera no chão, ela arranca o tapete, abre o vão com uma barra de ferro e o pó sobe; (2) bem perto do esconderijo, duas mãos tiram um pacote de veludo e abrem, e a carta Os Enamorados aparece na frente da lente.",
          modo="Quatro imagens e dois vídeos, na ordem dos números. Os dois vídeos são em FRAMES (primeiro e último quadro). A tomada 1 mostra o rosto da Nora: se a imagem A não vier com o rosto dela, descarte e gere de novo. A tomada 2 não mostra o rosto, só as mãos e a carta.")
    if k=='nora28':
        d['pre_gancho'].update(etapas=P.ETAPAS28,duracao=6,tomadas=2,montagem=P.MONT28,
          conceito="Modelo nos virais: S2 e R01 (sal caindo em primeiro plano, mãos e objetos, corte seco) e V4 (círculo de sal com canela e louro; ela sopra e sobe muita fumaça, 2,5 s, corte seco para o plano principal). Duas tomadas de 4 s: (1) câmera no chão olhando de cima o círculo de sal: o sal cai fazendo barulho e fecha o círculo, e um isqueiro acende o feixe de canela e louro; (2) a imagem que você já tem, ela inclinada e soprando: a fumaça explode em direção à lente. Sem chama aberta grande.",
          modo="Quatro imagens e dois vídeos, na ordem dos números. A imagem C é a que você já gerou (a Nora inclinada, soprando): não precisa gerar de novo. Os dois vídeos são em FRAMES (primeiro e último quadro). A tomada 1 não mostra o rosto, só as mãos; a tomada 2 mostra o rosto.")
    cen=copy.deepcopy(base['central'])
    for sec in cen['config']:
        for c in sec['campos']:
            if c['campo'].startswith('Perfil de voz'):
                c['copiar']=c['copiar'].replace("Woman, late 30s, American, warm and steady voice — sounds like a straight-talking friend who has been through her own heartbreaks and says things plainly.","Woman, mid-30s, American, warm, magnetic and confident voice — sounds like a straight-talking friend who knows astrology and says things plainly, with a bright, high-vibe warmth.").replace("Tone: Calm, firm and warm.","Tone: Warm, confident and firm, with an upbeat, high-vibe energy.")
            if c['campo']=='Velocidade da fala': c['valor']=c['valor'].replace('padrão da Nora (voz calma e firme)','padrão da Nora (voz calorosa e firme)')
    cen['colagens']=[{"titulo":"%s completo (%d takes)"%(k,n),"fala":full,"movimentacao":P.MOVL[k],"takes":list(range(n))}]
    cen.pop('copia',None)
    cen['passos']=[
      "Gere o pré-gancho (seção “Pré-gancho”): (1) a imagem 1, no Nano Banana Pro 9:16, anexando SÓ o blueprint da Nora v2 e colando o prompt (é uma geração nova, com o rosto dela); (2) a imagem 2, anexando SÓ a imagem 1 aprovada (é uma edição dela); (3) compare as duas imagens; (4) só então gere o vídeo no modo Frames, imagem 1 no início e imagem 2 no fim. Nunca cole o prompt de geração junto com outra imagem da Nora.",
      "Gere a IMAGEM 1 do vídeo na Central de imagens (seção “Imagem 1 na Central de imagens”, com a caixinha “já tenho o blueprint” marcada), campo por campo. **Ela é a continuação do pré-gancho: mesma roupa e mesmo cenário, e a Nora passa a falar.** Use o prompt que a Central gerar, anexando o blueprint (e, se a Central aceitar, a imagem 1 do pré-gancho só como guia de roupa, cenário e luz). Aprove só se for a Nora v2 (olhos verde-avelã, lua dourada com 3 estrelinhas na maçã do rosto, testa limpa, trança com anéis dourados, colar de Vênus) segurando %s na mão direita, com a esquerda livre."%OBJ_PT[k],
      "Na Central do curso, preencha a configuração (seção “Central do curso: o que preencher”) e faça a colagem única do %s (a fala inteira de uma vez, %d takes de 10 s). Clique em GERAR PROMPT DE ANIMAÇÃO e confira a lista de takes. Não clique em “Resetar valores” nem em “REGERAR BLOCO”."%(k,n),
      "No agente do Flow, anexe a IMAGEM 1 aprovada (só ela; o blueprint não vai no agente), cole o aviso e, embaixo, o “COPIAR TUDO JUNTO” da Central, sem editar nada. Depois de gerar, renomeie cada arquivo com o nome que o painel mostra. Custo: %d créditos de takes (+ %d do pré-gancho)."%(n*15,{4:7,6:10}[pre['dur']])]
    cen['conferir']="Conferir em cada vídeo: é a Nora v2 (rosto, lua com as estrelinhas, trança e roupa iguais à imagem); %s fica na mesma mão do começo ao fim; o resto do cenário fica parado; a fala sai completa, uma vez só, em inglês, com voz americana calorosa; sem texto, legenda ou música; renomeie o arquivo com o nome da lista."%OBJ_PT[k]
    cen['agente']={"imagem":"IMAGEM 1","aviso":"Irei enviar %d prompts para você. A cada prompt, quero que seja feita uma animação da imagem anexada. Utilize a imagem anexada como frame inicial e frame final, em todos os vídeos que você gerar."%n,
      "passos":["Abra uma conversa nova no agente do Flow.","Anexe a IMAGEM 1 aprovada (a única imagem; o blueprint não vai no agente).","Se quiser, cole antes o seu aviso (acima). O bloco da Central já traz as orientações ao agente.","Embaixo do aviso, cole o bloco copiado com “COPIAR TUDO JUNTO” da Central, sem editar nada.","Envie. O agente gera os %d vídeos; confira cada um no painel e me diga qual falhou (clipe e problema)."%n]}
    d['central']=cen
    d['story']={"prompt_imagem":P.STORY_PROMPT,"textos":[{"posicao":"Uma frase só, no centro, uma cor (creme #F1E6D3), 1 a 2 linhas","texto":"Tap below and find your Venus pattern in astrology."},{"posicao":"PROVISÓRIO: use esta frase (no lugar da de cima) ENQUANTO o Love Chart não estiver no ar. O Gustavo avisou em 19/10, 18h, que o link ainda abre o quiz do Soulmate e que vai trocar sozinho. Quando ele avisar que entrou, volte para a frase do Venus.","texto":"Tap below and take the free love quiz."}],"adesivos":["Find my Venus (só com o Love Chart no ar)","Take the free quiz (provisório, serve para os dois quizzes)","Open Part 2"]}
    d['pecas']=reuse.pecas(k,CRED)
    return d
t=open(ROOT+'PAINEL-MODELO.html',encoding='utf-8').read()
assert t.count('const PACOTE = null;')==1
for k in data.V:
    d=pack(k)
    json.dump(d,open(SP+'pacote_%s.json'%k.lower(),'w'),ensure_ascii=False,indent=1)
    out=ROOT+'PAINEL-%s.html'%k.upper()
    open(out,'w',encoding='utf-8').write(t.replace('<title>Painel de Produção</title>','<title>Painel %s</title>'%k).replace('const PACOTE = null;','const PACOTE = '+json.dumps(d,ensure_ascii=False)+';'))
    print(k,'ok',len(d['videos']))
# story file
open(ROOT+'STORY-NORA25-28-LOVECHART.md','w',encoding='utf-8').write("""# STORY (parte 2) do Love Chart — um só para os quatro vídeos (nora25, nora26, nora27 e nora28)

O aluno posta **um** story para os quatro vídeos de 19/10/2026. Regra do aluno: nenhuma menção a afiliado, link, preço ou assinatura no story. O adesivo de link usa 3 a 4 palavras, não o endereço. Poste este story **antes** do primeiro vídeo.

## 1. Prompt da imagem do story (Nano Banana Pro, 9:16; em inglês)
Anexe só o blueprint da Nora e a IMAGEM 1 aprovada do **nora25** (é uma edição dela). A imagem sai sem texto; o texto entra no editor do Instagram.

"""+P.STORY_PROMPT+"""

## 2. Texto na tela do story (uma frase só, 1 a 2 linhas, uma cor creme #F1E6D3, no centro)
"Tap below and find your Venus pattern in astrology."
Fonte grossa e legível, com leve sombra, sem outros textos. Deixe livres os 14% do topo e os 20% de baixo.

## 3. Texto do adesivo de link (3 a 4 palavras)
1. **"Find my Venus"** (recomendada SÓ quando o Love Chart estiver no ar: é o botão da tela 11 do quiz). **PROVISÓRIO enquanto o link ainda abre o Soulmate:** texto do story "Tap below and take the free love quiz." e adesivo **"Take the free quiz"**.
2. "Name my pattern"
3. "Open Part 2"
""")
