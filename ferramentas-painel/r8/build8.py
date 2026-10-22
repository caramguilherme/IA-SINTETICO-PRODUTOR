# -*- coding: utf-8 -*-
import sys,json,copy
sys.path.insert(0,'/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/r8')
import p8
P=p8.P
import reuse
SP=p8.SP+'/'
ROOT='/home/user/IA-SINTETICO-PRODUTOR/'
sys.path.insert(0,SP+'r7')
import scripts as S
base=json.load(open(SP+'pacote_r004.json'))
VOZ='Voz feminina adulta americana (inglês dos EUA), natural e espontânea, calorosa e firme.'
LEIT=("20/10/2026: antes de montar os prompts reli, com a ferramenta de leitura e neste turno: `LEIA-TUDO-ANTES.md`, `LICOES-FLOW-E-PROMPTS.md` (inteiro, com o checklist da seção 1, itens 1 a 27), `DNA Visual - Nora v2.md`, `GUIA-CREATIVE-HUB.md`, `PAPEL-AGENTE-FLOW.md`, `CHECKLIST-DE-PRODUCAO.md`, `Prompts.txt`, `BIBLIOTECA-PRE-GANCHOS.md`, `BIBLIOTECA-DE-TAKES.md`, `PASSO-A-PASSO-NORA25-28.md`, `PLANO-CREDITOS-NORA25-28.md`, `REGISTRO-DE-PERSONAS.md`, `EXEMPLO-ROTEIRO-APROVADO-FIGADO.md`, `EXEMPLO-PACOTE-FIGADO.md` (as primeiras 120 linhas) e o roteiro aprovado deste vídeo. O `CLAUDE.md` (P1 a P29) foi recarregado no início do turno. Os documentos de método e do curso (hooks, formatos, exemplos, ctas, comunicação visceral, bibliotecas, virais, pesquisa, briefing do Love Chart, PROJETO) foram lidos inteiros antes de escrever o roteiro; a lista completa está no registro do roteiro. O `PAINEL-MODELO.html` não foi reaberto: o formato do pacote é o do painel do nora28, que usei como base, conferido no código de montagem e no teste do navegador.")
V={}
V['nora29']=dict(
 id='nora29-CONTAGEM-3-2-1-ELE-SOME', sem_pre=True, titulo='3, 2, 1: ele some',
 dor='2 (o homem que some), com a 3 (reler a conversa, adivinhar cada mensagem)',
 formato='Formato 1 (problema + crença + solução), 8 takes',
 molde='gancho do viral w8 (contagem 3, 2, 1) + data como gancho (w3 a w9) + ângulo 3 do curso',
 code='222', fixos=('222','11:11'),
 pre=dict(dur=6,texto="When he goes quiet and you don't know why:"),
 hooktext=("American women: if you're seeing this on October 20th or 21st, it's a sign.","3, 2, 1","meant for you"),
 dest='Venus, quiet e pattern',
 objpt='o meio geodo de ametista aberto, com o anel dourado',
 legenda="American women, 3, 2, 1. 🔮\nPart 2 is in my story. Comment 222. Tap my photo NOW.",
 pin_ig="PART 2 is in my story. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222 if this found you. 🔥",
 pin_fb="PART 2 is in my Story. Tap my profile picture NOW, it's gone in 24 hours. Comment 222 if this found you. 🔥",
 cortepre="corte seco do vídeo 1 para o vídeo 2 e, depois do anel erguido, entra o Take 1",
 quadro_i="a pedra cinza está fechada e inteira nas duas mãos dela, apertada (nenhum cristal aparece)",
 quadro_f="a pedra está aberta em duas metades de cristais roxos, uma em cada mão, com o anel dourado entre os cristais",
 etapas=p8.ETAPAS29, mont=p8.MONT29, T=S.T29,
 conceito="Modelo nos virais: w4 (a pedra que ela aperta, trinca e abre, mostrando cristais, ouro e anéis; rosto grande; 8 ações em uns 3 s) e R01/S2 (corte seco para o macro). Duas tomadas de 4 s: (1) rosto grande, ela aperta o geodo fechado, ele racha e abre em duas metades de cristais roxos; (2) macro: dois dedos tiram um anel dourado de entre os cristais e o erguem para a lente.",
 modo="Quatro imagens e dois vídeos, na ordem dos números. Os dois vídeos são em FRAMES (primeiro e último quadro). A tomada 1 mostra o rosto da Nora: se a imagem A não vier com o rosto dela, descarte e gere de novo. A tomada 2 não mostra o rosto, só as mãos e o geodo.",
 PRE_EDIT="Aviso do pré-gancho: se o Flow não rachar a pedra (ela continua fechada ou abre sozinha antes de 1 s), refaça uma vez; se falhar de novo, me chame antes de gastar mais.",
 peça_desc=[('A','Tomada 1, primeiro quadro: o rosto dela e as duas mãos apertando a pedra cinza fechada (gerada do blueprint).'),('B','Tomada 1, último quadro: edição da A, com a pedra aberta em duas metades de cristais roxos e o anel dourado.'),('V1','Tomada 1 (4 s, Frames A para B): ela aperta, a pedra racha e abre.'),('C','Tomada 2, primeiro quadro: macro do meio geodo com o anel entre os cristais (gerada do blueprint, sem o rosto).'),('D','Tomada 2, último quadro: edição da C, com o anel erguido pelos dedos diante da lente.'),('V2','Tomada 2 (4 s, Frames C para D): os dedos tiram o anel e o erguem para a lente.')],
 mapa={'A':'IMG','B':'IMG','C':'IMG','D':'IMG'},
 tn=['gancho-contagem','corpo-ele-some','corpo-nao-e-azar','corpo-curious-heart','corpo-sem-adivinhar','corpo-nao-passe','cta-a-quiz-venus','cta-b-comente-222'],
)
V['nora30']=dict(
 id='nora30-QUARTO-SINAL-QUENTE-E-FRIO', sem_pre=True, titulo='O quarto sinal: quente e frio',
 dor='4 (sinal ou ilusão: quente e frio, sem planos), com a 2',
 formato='Formato 1 (problema + crença + solução), 8 takes',
 molde='gancho do viral w9 (a quarta vez que o universo tenta chegar até você) + ângulo 4 do curso (você estava certa) + campeões B4V e C4',
 code='444', fixos=('444','11:11'),
 pre=dict(dur=6,texto="When he's hot, then cold:"),
 hooktext=("American women: your fourth sign about him.","American women, this is the fourth","all along"),
 dest='Venus, fourth e pattern',
 objpt='a folha de louro com o símbolo de Vênus',
 legenda="American women: your 4th sign about him. 💔\nPart 2 is in my story. Comment 444. Tap my photo NOW.\n#astrology #venus #usa #usareels",
 pin_ig="PART 2 is in my story. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 444 if you saw the signs. 🔥",
 pin_fb="PART 2 is in my Story. Tap my profile picture NOW, it's gone in 24 hours. Comment 444 if you saw the signs. 🔥",
 cortepre="corte seco do vídeo 1 para o vídeo 2 e, depois do sal cobrir as folhas, entra o Take 1",
 quadro_i="o tapete de borracha está deitado no carro, as folhas de louro estão no punho dela e não há folha nenhuma no carpete",
 quadro_f="o tapete está levantado, o carpete cinza está à mostra com as folhas de louro espalhadas e a mão direita está vazia",
 etapas=p8.ETAPAS30, mont=p8.MONT30, T=S.T30,
 conceito="Modelo nos virais: w6 (carro americano: levantar o tapete do chão, jogar folhas de louro, despejar sal, repor o tapete; 3 cortes em uns 4,8 s) e S2 (sal caindo em primeiro plano, corte seco). Duas tomadas de 4 s: (1) câmera no chão da garagem, rosto grande, ela levanta o tapete do SUV e joga o louro no carpete; (2) macro: o sal cai em fio grosso e enterra as folhas.",
 modo="Quatro imagens e dois vídeos, na ordem dos números. Os dois vídeos são em FRAMES (primeiro e último quadro). A tomada 1 mostra o rosto da Nora: se a imagem A não vier com o rosto dela, descarte e gere de novo. A tomada 2 não mostra o rosto, só a mão e o pote de sal.",
 PRE_EDIT="Aviso do pré-gancho: se o tapete não subir ou as folhas já aparecerem no carpete no primeiro segundo, refaça uma vez; se falhar de novo, me chame antes de gastar mais.",
 peça_desc=[('A','Tomada 1, primeiro quadro: o rosto dela ao lado da porta do SUV, a mão no tapete e o punho com folhas de louro (gerada do blueprint).'),('B','Tomada 1, último quadro: edição da A, com o tapete levantado e as folhas espalhadas no carpete.'),('V1','Tomada 1 (4 s, Frames A para B): ela levanta o tapete e joga o louro.'),('C','Tomada 2, primeiro quadro: macro do carpete com as folhas e o pote de sal inclinado por cima (gerada do blueprint, sem o rosto).'),('D','Tomada 2, último quadro: edição da C, com o monte de sal cobrindo as folhas.'),('V2','Tomada 2 (4 s, Frames C para D): o sal cai e cobre as folhas.')],
 tn=['gancho-quarto-sinal','corpo-rele-a-noite','corpo-padrao-venus','corpo-steady-heart-story','corpo-sem-adivinhar','corpo-nao-espera','cta-a-quiz-venus','cta-b-comente-444'],
)
CRED={4:7,6:10,8:12,10:15}
def tnames(k):
    return ['%s-T%d-%s'%(k,i+1,V[k]['tn'][i]) for i in range(8)]
def EDLINE(k):
    v=V[k]; a,b=v['fixos']
    if v.get('sem_pre'):
        return [
     {"quando":"1. Take 1 (o gancho falado), desde o segundo 0","texto":v['hooktext'][0],"como":"Este vídeo NÃO tem pré-gancho (teste de 20/10/2026): o texto entra no segundo 0, em caixa branca no topo. Aparece na frase que começa em “%s” e some quando a frase termina em “%s”."%(v['hooktext'][1],v['hooktext'][2])},
     {"quando":"2. Do take 1 até o último segundo (o corpo todo)","texto":"%s  e  %s"%(a,b),"como":"Dois números FIXOS, pequenos, em maiúsculas, brancos com contorno, durante o vídeo inteiro: %s no canto superior esquerdo e %s no canto superior direito. O %s é o código que a pessoa digita nos comentários. Estilo dos virais U1, U2, U4, w9 e w10 (par de números no topo). Posição: faixa azul do mapa da tela, abaixo."%(a,b,a)},
     {"quando":"3. Do take 1 até o último segundo","texto":"Legenda em blocos de 2 a 4 palavras","como":"POSIÇÃO: faixa verde do mapa da tela, abaixo (60%% a 70%% da altura, abaixo do queixo e acima do rodapé do app), sempre no mesmo lugar. Legendas automáticas do CapCut, letra grossa, em blocos de 2 a 4 palavras por vez (NÃO uma palavra só por vez: no Face, uma conta teve o post limitado por “baixa qualidade da legenda” com legenda de uma palavra por vez, e o aviso parou quando passou a mostrar frases curtas). Destaque em cor (amarelo ou dourado) nas palavras: %s."%v['dest']},
     {"quando":"4. No pedido final (“Tap my photo and open my story…”)","texto":"Seta vermelha","como":"Uma seta vermelha pequena apontando para a foto do perfil, no canto superior esquerdo, só durante essa frase."}]
    return [
     {"quando":"1. Pré-gancho (2 tomadas, uns 6 s no total)","texto":v['pre']['texto'],"como":"Texto no topo, em até 2 linhas, durante os primeiros 3 segundos. Some junto com o pré-gancho (%s). Sem música."%v['cortepre']},
     {"quando":"2. Take 1 (o gancho falado)","texto":v['hooktext'][0],"como":"Caixa branca no topo. Aparece na frase que começa em “%s” e some quando a frase termina em “%s”."%(v['hooktext'][1],v['hooktext'][2])},
     {"quando":"3. Do take 1 até o último segundo (o corpo todo)","texto":"%s  e  %s"%(a,b),"como":"Dois números FIXOS, pequenos, em maiúsculas, brancos com contorno, durante o corpo inteiro: %s no canto superior esquerdo e %s no canto superior direito. O %s é o código que a pessoa digita nos comentários. Estilo dos virais U1, U2, U4, w9 e w10 (par de números no topo)."%(a,b,a)},
     {"quando":"4. Do take 1 até o último segundo","texto":"Legenda em blocos de 2 a 4 palavras","como":"Legendas automáticas do CapCut, letra grande no meio da tela, em blocos de 2 a 4 palavras por vez (NÃO uma palavra só por vez: no Face, uma conta teve o post limitado por “baixa qualidade da legenda” com legenda de uma palavra por vez, e o aviso parou quando passou a mostrar frases curtas). Destaque em cor (amarelo ou dourado) nas palavras: %s."%v['dest']},
     {"quando":"5. No pedido final (“Tap my photo and open my story…”)","texto":"Seta vermelha","como":"Uma seta vermelha pequena apontando para a foto do perfil, no canto superior esquerdo, só durante essa frase."}]
def pecas(k):
    v=V[k]; L=[]
    for sfx,ds in ([] if v.get('sem_pre') else v['peça_desc']):
        cr=7 if sfx in ('V1','V2') else None
        d=dict(nome=k+'-PRE-'+sfx,tipo=('pré-gancho (vídeo)' if cr else 'imagem do pré-gancho'),status='gerar',descricao=ds)
        if cr: d['creditos']=cr
        if sfx=='A': d['base']=reuse.BASE_TIPO['PRE-IMG']; d['serve']='Só deste vídeo (o começo é sempre novo).'
        L.append(d)
    L.append(dict(nome=k+'-IMG',tipo='imagem 1 do vídeo',status='gerar',descricao=('Primeiro e último quadro de todos os takes (gancho, corpo e CTA), gerada na Central de imagens. Como este vídeo NÃO tem pré-gancho (teste), ela é o primeiro quadro do vídeo e prende o scroll sozinha: rosto grande, objeto bem à vista.' if v.get('sem_pre') else 'Primeiro e último quadro de todos os takes (gancho, corpo e CTA), gerada na Central de imagens. É a CONTINUAÇÃO do pré-gancho: mesma roupa e mesmo cenário, e a Nora passa a falar (teste do nora25 ao nora28, mantido).'),serve='Se este vídeo performar, ela vira o kit de variações com gancho novo.'))
    n=len(v['T']); tn=tnames(k)
    for i,t in enumerate(v['T']):
        cta=i>=n-2
        tipo='gancho' if i==0 else ('CTA' if cta else 'corpo')
        L.append(dict(nome=tn[i],tipo=tipo,status='gerar',creditos=15,descricao='Take %d, %s: “%s”'%(i+1,t[0],t[2][:110]+('…' if len(t[2])>110 else '')),base=reuse.BASE_TIPO['GANCHO' if i==0 else ('CTA' if cta else 'CORPO')],serve=('Só neste vídeo (cada gancho é novo).' if i==0 else 'Candidato a reaproveitar depois, em variações do mesmo kit, se o vídeo performar.')))
    dec=[x.replace('nora29 em diante, uns 22 créditos cada','nora31 em diante, só o gancho de 15 créditos, porque este vídeo não tem pré-gancho') for x in reuse.DECISAO]
    if v.get('sem_pre'): dec.insert(0,"TESTE DE 20/10/2026: este vídeo NÃO tem pré-gancho. O nora27 e o nora28 têm; o nora29 (sem hashtag) é comparado ao nora27 e o nora30 (com hashtag) ao nora28, para a hashtag não confundir. Compare a retenção nos 3 s nos mesmos tempos de vida (3 h e 24 h). Só vale se a diferença passar de uns 10 pontos. O pré-gancho que sobrou (%s) fica guardado para outro vídeo."%('geodo que racha com o anel dourado' if k=='nora29' else 'tapete do carro com louro e sal'))
    return dict(lista=L,decisao=dec)
NP={'nora29':dict(pose="LIVRE: Seated on the edge of a gray sofa, leaning toward the camera and facing it head-on, framed from the shoulders up with the camera at chest height about 60 cm away so her face is large, her right hand raised close to the lens on the left side of the frame beside her face holding the half geode, which fills about a third of the frame without covering her face, her left hand resting on her knee"),
 'nora30':dict()}
def pack(k):
    P.VAR[k].update(NP[k])
    v=V[k]; T=v['T']; n=len(T); d=copy.deepcopy(base)
    full=' '.join(t[2] for t in T)
    pre=v['pre']
    d['roteiro']={"id":v['id'],"titulo":v['titulo'],"dor":v['dor'],"formato":v['formato'],"molde_hook":v['molde'],"duracao_total":(n*10 if v.get('sem_pre') else pre['dur']+n*10),"descricao_instagram":v['legenda'],"leitura_registro":LEIT}
    d['perfil']={"nome":"Nora","teste":"A","voz":VOZ}
    d['refs']=['blueprint da Nora v2 (folha de consistência do personagem, baixada em 1K)']
    d['trava_referencia']=P.TRAVA
    d['figurino']=P.FIG[k]
    d['imagens']=[{"rotulo":"IMAGEM 1","cena":"Gerada na Central de imagens (campos no painel)."}]
    ic=P.CENTRAL(k); ic['titulo']='IMAGEM 1 (Central de imagens)'; ic['nome']=k+'-IMG'
    d['imagem_central']=[ic]
    d.pop('instrucoes_agente',None)
    tn=tnames(k)
    d['videos']=[{"rotulo":"V%d"%(i+1),"cena":"Take %d/%d · %s"%(i+1,n,t[0]),"duracao":10,"primeiro_quadro":"IMAGEM 1","acao":"(ver movimentação)","b_roll":"","fala":t[2],"movimentacao":p8.MOVL[k][i],"arquivo":tn[i]} for i,t in enumerate(T)]
    d['texto_tela']={"hook":v['hooktext'][0],"hook_comeca":v['hooktext'][1],"hook_termina":v['hooktext'][2],"hook_alt":"","extras":[]}
    d['comentario_fixado']={"insta":v['pin_ig'],"face":v['pin_fb']}
    d['edicao_linha']=EDLINE(k)
    E=v['etapas']
    d['pre_gancho']={"duracao":pre['dur'],"com_rosto":True,
      "nome_img1":k+"-PRE-A","nome_img2":k+"-PRE-B","nome_video":k+"-PRE-V1",
      "conceito":v['conceito'],
      "imagem_prompt":E[0]['prompt'],"imagem_final_prompt":E[1]['prompt'],"video_prompt":E[2]['prompt'],
      "texto_tela":pre['texto'],"edicao":v['PRE_EDIT'],
      "quadro_inicial":v['quadro_i'],"quadro_final":v['quadro_f'],
      "etapas":E,"tomadas":2,"montagem":v['mont'],"modo":v['modo']}
    d['mapa_tela']={"topo_app":[0,10],"codigos":[10,14],"hook":[14,24],"legenda":[60,70],"rodape_app":[78,100],"botoes":{"x":[86,100],"y":[48,86]},"estilos":[
      {"nome":"Números fixos (222 ou 444 à esquerda, 11:11 à direita)","fonte":"Poppins Bold (poppins-bd)","cor":"amarelo-ouro #FFD21F","tamanho":"12","contorno":"Traço preto + Sombra preta, sem Plano de fundo. Luz DESLIGADA","obs":"Os dois do mesmo tamanho e na mesma altura."},
      {"nome":"Texto do hook (início do vídeo)","fonte":"Poppins Bold (poppins-bd)","cor":"branco #FFFFFF (uma palavra em amarelo-ouro #FFD21F, se quiser)","tamanho":"12","contorno":"Traço preto + Sombra preta, sem Plano de fundo. Luz DESLIGADA","obs":"Centralizado, em 2 linhas."},
      {"nome":"Legenda automática (Claude das legendas)","fonte":"Poppins Bold","cor":"branco, em MAIÚSCULAS; palavra-chave em amarelo-ouro #FFD21F","tamanho":"uns 38 px de fonte (vídeo 720×1280)","contorno":"preto grosso, sem caixa e sem brilho","obs":"Blocos de 2 a 4 palavras, no máximo 2 linhas, mesma posição o vídeo todo."}],
    "regras":[
      "Hook e números ficam em cima; a legenda só na faixa verde. Nada nas faixas vermelhas nem em cima do rosto, da mão que segura o objeto ou do objeto.",
      "Antes de exportar confira 3 quadros (o primeiro, um com a mão levantada e o do último take). Se a legenda tocar o rosto, a mão ou o objeto, desça no máximo até 74% da altura."]}
    if k=='nora30':
        d['mapa_tela']['legenda']=[69,77]
        d['mapa_tela']['regras'].insert(0,'Neste vídeo a legenda fica MAIS BAIXO (69% a 77%): a mão que segura a folha termina a 70% da altura. Y da legenda no CapCut: −294.')
    if v.get('sem_pre'):
        d.pop('pre_gancho',None)
        d['roteiro']['leitura_registro']+=" Teste de 20/10/2026 (aprovado pelo aluno): este vídeo NÃO tem pré-gancho; começa direto no Take 1, com o texto do hook no segundo 0."
        a=d['imagem_central'][0]['aviso']; i=a.index('A IMAGEM 1 é gerada')
        d['imagem_central'][0]['aviso']="SEM PRÉ-GANCHO (teste de 20/10/2026): esta imagem é o primeiro quadro do vídeo e precisa prender o scroll sozinha: rosto grande e olhar firme, o objeto bem perto da lente e à vista, boa luz. "+a[i:]
    NOTA={'nora29':" DETALHE DO OBJETO: o anel dourado fino entre os cristais é o que dá o brilho ao hook. Se ele sair grudado na borda, duplicado ou sumido, gere de novo; prefira a opção em que o geodo mostra os cristais roxos para a lente e o anel está visível.",
          'nora30':" DETALHE DO OBJETO: o símbolo de Vênus desenhado na folha é um bônus. Se sair torto, ilegível ou virar letras, não rejeite a imagem por isso: o essencial é a folha de louro grande, nítida e perto da lente, sem texto escrito. Rejeite só se aparecerem palavras ou números na folha."}
    if v.get('sem_pre'): d['imagem_central'][0]['aviso']+=NOTA[k]
    cen=copy.deepcopy(base['central'])
    for sec in cen['config']:
        for c in sec['campos']:
            if c['campo'].startswith('Perfil de voz'):
                c['copiar']=c['copiar'].replace("Woman, late 30s, American, warm and steady voice — sounds like a straight-talking friend who has been through her own heartbreaks and says things plainly.","Woman, mid-30s, American, warm, magnetic and confident voice — sounds like a straight-talking friend who knows astrology and says things plainly, with a bright, high-vibe warmth.").replace("Tone: Calm, firm and warm.","Tone: Warm, confident and firm, with an upbeat, high-vibe energy.")
            if c['campo'].startswith('LIVRE — descreva'): c['copiar']=p8.GLOBAL[k]
            for kk in list(c):
                if isinstance(c[kk],str) and 'in a home setting with natural window light' in c[kk]:
                    c[kk]=c[kk].replace('in a home setting with natural window light',{'nora29':'in a home living room at dusk with warm lamp light','nora30':'outdoors on a home driveway at dusk with soft natural light and the warm dome light of a car'}[k])
            if c['campo']=='Velocidade da fala': c['valor']=c['valor'].replace('padrão da Nora (voz calma e firme)','padrão da Nora (voz calorosa e firme)')
    cen['colagens']=[{"titulo":"%s completo (%d takes)"%(k,n),"fala":full,"movimentacao":p8.MOVL[k],"takes":list(range(n))}]
    cen.pop('copia',None)
    cen['passos']=[
      "Este vídeo NÃO tem pré-gancho (teste de 20/10/2026, aprovado por você): não gere imagens nem vídeos de pré-gancho. O vídeo começa direto no Take 1, e o texto do hook entra no segundo 0.",
      "Gere a IMAGEM 1 do vídeo na Central de imagens (seção “Imagem 1 na Central de imagens”, com a caixinha “já tenho o blueprint” marcada), campo por campo. **Sem pré-gancho, ela é o primeiro quadro do vídeo e precisa prender o scroll sozinha (rosto grande, objeto bem à vista).** Use o prompt que a Central gerar, anexando só o blueprint. Aprove só se for a Nora v2 (olhos verde-avelã, lua dourada com 3 estrelinhas na maçã do rosto, testa limpa, trança com anéis dourados, colar de Vênus) segurando %s na mão direita, com a esquerda livre, e sem carimbo de data nos cantos."%v['objpt'],
      "Na Central do curso, preencha a configuração (seção “Central do curso: o que preencher”) e faça a colagem única do %s (a fala inteira de uma vez, %d takes de 10 s). Clique em GERAR PROMPT DE ANIMAÇÃO e confira a lista de takes. Não clique em “Resetar valores” nem em “REGERAR BLOCO”."%(k,n),
      "No agente do Flow, anexe a IMAGEM 1 aprovada (só ela; o blueprint não vai no agente), cole o aviso e, embaixo, o “COPIAR TUDO JUNTO” da Central, sem editar nada. Depois de gerar, renomeie cada arquivo com o nome que o painel mostra. Custo: %d créditos de takes (sem pré-gancho)."%(n*15)]
    cen['passos']=[x.replace('**','') for x in cen['passos']]
    if k=='nora29':
        cen['passos']=[x.replace('na mão direita, com a esquerda livre','na mão ESQUERDA dela (o lado direito da imagem), com a direita livre. O painel e as linhas de movimentação foram ajustados para a imagem aprovada em 20/10/2026, em que o geodo está na mão esquerda; se você gerar outra, o geodo tem de estar na mesma mão') for x in cen['passos']]
    cen['conferir']="Conferir em cada vídeo: é a Nora v2 (rosto, lua com as estrelinhas, trança e roupa iguais à imagem); %s fica na mesma mão do começo ao fim; o resto do cenário fica parado; a fala sai completa, uma vez só, em inglês, com voz americana calorosa; sem texto, legenda ou música; renomeie o arquivo com o nome da lista."%v['objpt']
    cen['agente']={"imagem":"IMAGEM 1","aviso":"Irei enviar %d prompts para você. A cada prompt, quero que seja feita uma animação da imagem anexada. Utilize a imagem anexada como frame inicial e frame final, em todos os vídeos que você gerar."%n,
      "passos":["Abra uma conversa nova no agente do Flow.","Anexe a IMAGEM 1 aprovada (a única imagem; o blueprint não vai no agente).","Se quiser, cole antes o seu aviso (acima). O bloco da Central já traz as orientações ao agente.","Embaixo do aviso, cole o bloco copiado com “COPIAR TUDO JUNTO” da Central, sem editar nada.","Envie. O agente gera os %d vídeos; confira cada um no painel e me diga qual falhou (clipe e problema)."%n]}
    d['central']=cen
    d['story']={"prompt_imagem":P.STORY_PROMPT,"textos":[{"posicao":"Uma frase só, no centro, uma cor (creme #F1E6D3), 1 a 2 linhas","texto":"Tap below and find your Venus pattern in astrology."},{"posicao":"PROVISÓRIO: use esta frase (no lugar da de cima) ENQUANTO o Love Chart não estiver no ar. O Gustavo avisou em 19/10, 18h, que o link ainda abre o quiz do Soulmate e que vai trocar sozinho. Quando ele avisar que entrou, volte para a frase do Venus.","texto":"Tap below and take the free love quiz."}],"adesivos":["Find my Venus (só com o Love Chart no ar)","Take the free quiz (provisório, serve para os dois quizzes)","Open Part 2"]}
    d['story']['prompt_imagem']=p8.STORY_DET
    if k=='nora30':
        for g in d['imagem_central'][0]['grupos']:
            for c in g['campos']:
                if c['campo'].startswith('Acessórios'):
                    c['valor']="Long gold star-and-moon drop earrings (a small gold star above a crescent moon, hanging about 6 cm below each earlobe), a long thin gold chain necklace with a small gold Venus-symbol pendant (a circle about 1 cm wide with a short cross below it) resting on the sweater at the center of the chest, three thin gold bracelets stacked on her LEFT wrist only (none on the right wrist), one small gold sun-symbol ring on the index finger of each hand, exactly ONE small flat shiny gold crescent-moon face gem on the outer edge of the cheekbone on the left side of the image near the temple with three tiny flat gold star gems trailing diagonally below it, a completely clean forehead with nothing on it, and hazel-green eyes with a golden ring around the pupil"
    d['pecas']=pecas(k)
    return d
if __name__=='__main__':
    t=open(ROOT+'PAINEL-MODELO.html',encoding='utf-8').read()
    assert t.count('const PACOTE = null;')==1
    for k in V:
        d=pack(k)
        json.dump(d,open(SP+'pacote_%s.json'%k,'w'),ensure_ascii=False,indent=1)
        out=ROOT+'PAINEL-%s.html'%k.upper()
        h=t.replace('<title>Painel de Produção</title>','<title>Painel %s</title>'%k).replace('const PACOTE = null;','const PACOTE = '+json.dumps(d,ensure_ascii=False)+';')
        if V[k].get('sem_pre'):
            for a,b in (("Faça depois que os takes do corpo (sem o pré-gancho) estiverem prontos","Faça depois que os takes estiverem prontos"),
                ("O pré-gancho é outro arquivo: não entra nesta ferramenta, entra no CapCut depois. Arraste o vídeo do corpo","Este vídeo NÃO tem pré-gancho (teste de 20/10/2026): o vídeo começa direto no Take 1 e vai inteiro nesta ferramenta. Arraste o vídeo"),
                ("No CapCut: pré-gancho primeiro, depois o corpo cortado, e então os textos da seção seguinte.","No CapCut: abra o vídeo cortado (sem pré-gancho) e ponha os textos da seção seguinte; o primeiro texto entra no segundo 0."),
                ("Já com o pré-gancho e os takes aprovados, monte o vídeo","Já com os takes aprovados (este vídeo não tem pré-gancho), monte o vídeo")):
                assert h.count(a)==1,a[:40]
                h=h.replace(a,b)
        open(out,'w',encoding='utf-8').write(h)
        print(k,'ok',len(d['videos']),'pre_gancho' in d)
