# -*- coding: utf-8 -*-
import sys,json,copy
SPD='/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/'
for d in ('r10','r9','r8','r7','r6'): sys.path.insert(0,SPD+d)
import p11
import p12
import build9 as B
import scripts10 as S10, mov10
p8=B.p8; P=B.P
ROOT=B.ROOT
LEIT=("21/10/2026: antes de reescrever (a pedido do aluno) reli neste turno e nesta sessão, com a ferramenta de leitura: `CLAUDE.md` (P1 a P37, recarregado), `LICOES-FLOW-E-PROMPTS.md`, `BIBLIOTECA-VIDEOS-VIRAIS.md` (as seções 13 a 19 do viral S3/w3 a w5 e a nova seção 20 com a transcrição inteira feita hoje), `BIBLIOTECA-DE-TAKES.md`, `PROJETO-Dana.md`, `BRIEFING-LOVECHART.md`, `DNA Visual - Nora v2.md`, `GUIA-CREATIVE-HUB.md`, `PAPEL-AGENTE-FLOW.md`, `CHECKLIST-DE-PRODUCAO.md`, `Prompts.txt`, `EXEMPLO-ROTEIRO-APROVADO-FIGADO.md`, `EXEMPLO-PACOTE-FIGADO.md`, `PASSO-A-PASSO-NORA25-28.md`, `PASSO-A-PASSO-NORA29-30.md`, `PLANO-CREDITOS-NORA29-30.md`, `STORY-NORA25-28-LOVECHART.md`, os métricas e o chat com o Eduardo. **Não reabri neste turno:** `hooks.md`, `Formatos Narrativos…`, `Exemplos de Roteiros…`, `ctas.md`, `COMUNICACAO-VISCERAL…`, `BIBLIOTECA-BODIES/COLD-READING/COPY/COPY-100/PRE-GANCHOS`, `PESQUISA-PUBLICO.md` (lidos inteiros hoje, às 15h32 da sessão, antes de montar os roteiros do nora31 e nora32), os planos de créditos antigos, os DNAs da Dana e da Nora v1, os roteiros antigos e o `PAINEL-MODELO.html`. O corpo deste vídeo é uma cópia do viral S3, a pedido do aluno; não é um roteiro novo.")
B.LEIT=LEIT
B.tnames=lambda k:['%s-T%d-%s'%(k,i+1,B.V[k]['tn'][i]) for i in range(len(B.V[k]['tn']))]
# --- nora30: cópia do S3, 9 takes
V=B.V
T30=S10.full('nora30')
V['nora30'].update(dict(
 id='nora30-SERIE-S3-TOURO-VIRGEM-CAPRICORNIO', titulo='Touro, Virgem e Capricórnio: o portal do amor',
 dor='o homem que o universo guardou, a solidão e o bloqueio de amor',
 formato='Corpo copiado do viral S3 (por signos), 9 takes',
 molde='cópia do viral S3 (avatar dos signos): gancho por signos + data, corpo quase palavra por palavra, 222 e story (decisão do aluno em 21/10/2026, a partir da conversa com o Eduardo Pinaffi)',
 code='222', fixos=('222','11:11'),
 hooktext=("Taurus, Virgo, Capricorn: pay very close attention","Taurus, Virgo","watching this"),
 dest='portal, seal e stories',
 legenda="Taurus, Virgo, Capricorn: pay very close attention. 🔮\nPart 2 is in my story. Comment 222. Tap my photo NOW.\n#astrology #zodiac #usa #usareels",
 pin_ig="PART 2 is in my story. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222 if this found you. 🔥",
 pin_fb="PART 2 is in my Story. Tap my profile picture NOW, it's gone in 24 hours. Comment 222 if this found you. 🔥",
 T=T30,
 tn=[t[1].split('-T',1)[1].split('-',1)[1] for t in T30],
))
V['nora30']['objpt']='o geodo de ametista grande'
for k,(hook_,leg,hora,base,hh) in {
 'nora32':(("Gemini, Libra, Aquarius: pay very close attention","Gemini, Libra","watching this"),"Gemini, Libra, Aquarius: pay very close attention. 🔮\nPart 2 is in my story. Comment 222. Tap my photo NOW.\n#astrology #zodiac #usa #usareels",'22/10 18h30',None,'gemeos-libra-aquario')}.items():
    T=S10.full(k)
    V[k]=dict(id='%s-SERIE-S3-GEMEOS-LIBRA-AQUARIO'%k,sem_pre=True,v31=True,titulo='Gêmeos, Libra e Aquário: o portal do amor',dor='o homem que o universo guardou, a solidão e o bloqueio de amor',
      formato='Corpo copiado do viral S3, 9 takes',molde='cópia do viral S3 (avatar dos signos): gancho por signos + data, corpo quase palavra por palavra',code='222',fixos=('222','11:11'),pre=dict(dur=0,texto=""),
      hooktext=hook_,dest='portal, seal e stories',objpt='o cristal de quartzo rosa grande',legenda=leg,pin_ig=V['nora30']['pin_ig'],pin_fb=V['nora30']['pin_fb'],T=T,
      tn=[t[1].split('-T',1)[1].split('-',1)[1] for t in T])
SER={
 'nora33':dict(base='nora32',h='cancer-escorpiao-peixes',titulo='Câncer, Escorpião e Peixes: o portal do amor',leg="Cancer, Scorpio, Pisces: pay very close attention. 🔮\nPart 2 is in my story. Comment 222. Tap my photo NOW.",hook=("Cancer, Scorpio, Pisces: pay very close attention","Cancer, Scorpio","watching this")),
}
for k,s_ in SER.items():
    t1=S10.H[k]
    V[k]=dict(id='%s-SERIE-S3-%s'%(k,s_['h'].upper()),sem_pre=True,v31=True,titulo=s_['titulo'],dor='o homem que o universo guardou, a solidão e o bloqueio de amor',
      formato='Série do S3: só o Take 1 muda (o corpo é o do %s)'%s_['base'],molde='cópia do viral S3 (avatar dos signos): gancho por signos + data',code='222',fixos=('222','11:11'),pre=dict(dur=0,texto=""),
      hooktext=s_['hook'],dest='portal, seal e stories',objpt=V[s_['base']]['objpt'],legenda=s_['leg'],
      pin_ig=V['nora30']['pin_ig'],pin_fb=V['nora30']['pin_fb'],T=[(t1[0],'%s-T1-gancho-%s'%(k,s_['h']),t1[3],t1[4],t1[5])],tn=['gancho-'+s_['h']],base=s_['base'])
T31=S10.full('nora31')
V['nora31']=dict(id='nora31-SERIE-S3-ARIES-LEAO-SAGITARIO-CURATIVO',sem_pre=False,titulo='Áries, Leão e Sagitário: o curativo na calcinha',
  dor='o homem que o universo guardou, a solidão e o bloqueio de amor',formato='Corpo copiado do viral S3, 9 takes, com o pré-gancho dos virais w1 e w2',
  molde='pré-gancho copiado dos virais w1 e w2 (curativo colado numa calcinha de renda vermelha, só mãos) + gancho “What the hell did you just do?” + corpo do S3',
  code='222',fixos=('222','11:11'),pre=dict(dur=5,texto="What the hell did you just do?"),
  hooktext=("Aries, Leo, Sagittarius: pay very close attention","Aries, Leo","watching this"),dest='portal, seal e stories',objpt='a calcinha vermelha de renda com o curativo',
  legenda="Aries, Leo, Sagittarius: pay very close attention. 🔮\nPart 2 is in my story. Comment 222. Tap my photo NOW.\n#astrology #zodiac #usa #usareels",
  pin_ig=V['nora30']['pin_ig'],pin_fb=V['nora30']['pin_fb'],T=T31,tn=[t[1].split('-T',1)[1].split('-',1)[1] for t in T31],
  cortepre="corte seco do vídeo 1 para o vídeo 2 e, depois do curativo colado, entra o Take 1",
  quadro_i="o invólucro do curativo está fechado e a mão direita pinça a lingueta vermelha",quadro_f="o invólucro está aberto na mão esquerda e o curativo bege está erguido na mão direita",
  etapas=p12.ETAPAS,mont=p12.MONT,conceito="Modelo nos virais w1 e w2 (macro das mãos: o curativo é tirado do invólucro e colado numa calcinha de renda vermelha, 3 cortes em ~2,5 s, depois a mulher fala segurando a calcinha). Duas tomadas de 4 s só com as mãos da Nora, sem corpo e sem a peça vestida: (1) o invólucro rasga e o curativo sai; (2) o curativo é colado no centro da calcinha e alisado. Depois a Nora fala segurando a mesma calcinha com o curativo, com as duas mãos.",
  modo="Quatro imagens e dois vídeos, na ordem dos números. Os dois vídeos são em FRAMES (primeiro e último quadro). Só aparecem as mãos da Nora; o rosto dela entra no Take 1.",
  PRE_EDIT="Aviso do pré-gancho: se o curativo aparecer pronto no primeiro quadro, ou o invólucro sumir, refaça uma vez; se falhar de novo, me chame antes de gastar mais.",
  peça_desc=[('A','Tomada 1, primeiro quadro: as duas mãos com o invólucro fechado do curativo, a mão direita puxando a lingueta (gerada do blueprint, sem o rosto).'),('B','Tomada 1, último quadro: edição da A, com o invólucro aberto e o curativo erguido.'),('V1','Tomada 1 (4 s, Frames A para B): as mãos rasgam o invólucro e tiram o curativo.'),('C','Tomada 2, primeiro quadro: macro da calcinha vermelha de cetim e renda, com o curativo na mão direita acima do centro (gerada do blueprint, sem o rosto).'),('D','Tomada 2, último quadro: edição da C, com o curativo colado no centro da calcinha.'),('V2','Tomada 2 (4 s, Frames C para D): a mão cola o curativo e alisa.')],
  mapa={})
def pack_pre(k):
    d=B.pack(k)
    d['central']['passos']=[
     "Comece pelo pré-gancho (seção “Pré-gancho”): 4 imagens e 2 vídeos em FRAMES, na ordem dos números. Só aparecem as mãos da Nora. Compare a imagem A com a B e a C com a D: a primeira mostra o antes (invólucro fechado, curativo ainda na mão) e a segunda o depois.",
     "Gere a IMAGEM 1 do vídeo na Central de imagens (seção “Imagem 1 na Central de imagens”, com a caixinha “já tenho o blueprint” marcada), campo por campo: a Nora segura a calcinha vermelha com o curativo, com as DUAS mãos, na frente do peito. Anexe só o blueprint. Aprove só se for a Nora v2 (olhos verde-avelã, lua com 3 estrelinhas na maçã do rosto, testa limpa, trança com anéis dourados, colar de Vênus), sem carimbo de data nos cantos e com o curativo no centro da calcinha.",
     "Na Central do curso, preencha a configuração (seção “Central do curso: o que preencher”) e faça a colagem única do nora31 (a fala inteira de uma vez, 9 takes). Clique em GERAR PROMPT DE ANIMAÇÃO e confira a lista de takes. Não clique em “Resetar valores” nem em “REGERAR BLOCO”.",
     "No agente do Flow, anexe a IMAGEM 1 aprovada (só ela; o blueprint não vai no agente), cole o aviso e, embaixo, o “COPIAR TUDO JUNTO” da Central, sem editar. Depois renomeie cada arquivo com o nome do painel. Custo dos takes: 132 créditos; o pré-gancho custa uns 14."]
    d['central']['conferir']="Conferir em cada take: é a Nora v2 da IMAGEM 1; a calcinha com o curativo fica nas duas mãos do começo ao fim e não cobre o rosto; o cenário fica parado; a fala sai completa, uma vez só, em inglês; sem texto, legenda ou música."
    d['mapa_tela']['legenda']=[69,77]
    d['mapa_tela']['regras'].insert(0,'Neste vídeo a calcinha com o curativo fica na frente do peito, até uns 65% da altura: a legenda fica MAIS BAIXO (69% a 77%), em blocos de 2 a 3 palavras. Y da legenda no CapCut: −294.')
    d['videos'][8]['duracao']=8
    for x in d['pecas']['lista']:
        if x['nome'].endswith('T9-cta-b-parte-dois'): x['creditos']=12
        if '-T1-' in x['nome']: x['base']='Gancho dos virais w1 e w2 (“What the hell did you just do?”) + signos do S3.'; x['serve']='Só deste vídeo.'
        elif x['nome'].endswith('-IMG'): x['descricao']='Primeiro e último quadro de todos os takes: a Nora segura a calcinha vermelha com o curativo, com as duas mãos (gerada na Central de imagens).'; x['serve']='Variações futuras do mesmo gancho.'
        elif x['tipo'] in ('corpo','CTA'): x['base']='Corpo copiado do viral S3.'; x['serve']='Corpo da série.'
    d['pecas']['decisao']=["Pré-gancho copiado dos virais w1 e w2, só mãos (sem corpo e sem a peça vestida). O corpo é o mesmo do nora30."]
    return d
def pack_series(k):
    bk=V[k]['base']
    base=B.pack(bk)                       # imagem, config e story do vídeo-base
    v=V[k]; d=copy.deepcopy(base); t1=v['T'][0]
    d['mapa_tela']['legenda']=[69,77]
    if not any('MAIS BAIXO' in r for r in d['mapa_tela']['regras']): d['mapa_tela']['regras'].insert(0,'Neste vídeo a legenda fica MAIS BAIXO (69% a 77%) e em blocos de 2 a 3 palavras: o pulso da mão que segura o objeto desce até uns 75% da altura, no lado direito. Y da legenda no CapCut: −294.')
    line=p8.MOVL[bk][0]
    d['roteiro'].update({"id":v['id'],"titulo":v['titulo'],"dor":v['dor'],"formato":v['formato'],"molde_hook":v['molde'],"duracao_total":90,"descricao_instagram":v['legenda'],"leitura_registro":LEIT+" Este vídeo usa o corpo do nora30; só o Take 1 é novo."})
    d['refs']=['IMAGEM 1 do %s (arquivo já gerado e aprovado)'%bk]
    d['imagens']=[{"rotulo":"IMAGEM 1","cena":"A mesma do %s (não gerar)."%bk}]
    d.pop('imagem_central',None)
    d['imagem_reutilizada']={"arquivo":"%s-IMG (a IMAGEM 1 do %s)"%(bk,bk),"aviso":"Use a MESMA IMAGEM 1 do %s (a Nora com %s na mão direita). Anexe só ela no agente do Flow. Não gere imagem nova."%(bk,V[bk]['objpt'])}
    d['videos']=[{"rotulo":"V1","cena":"Take 1/9 · "+t1[0],"duracao":10,"primeiro_quadro":"IMAGEM 1","acao":"(ver movimentação)","b_roll":"","fala":t1[2],"movimentacao":line,"arquivo":t1[1]}]
    d['texto_tela']={"hook":v['hooktext'][0],"hook_comeca":v['hooktext'][1],"hook_termina":v['hooktext'][2],"hook_alt":"","extras":[]}
    d['comentario_fixado']={"insta":v['pin_ig'],"face":v['pin_fb']}
    d['edicao_linha']=B.EDLINE(k)
    cen=d['central']
    cen['colagens']=[{"titulo":"%s: só o Take 1 (gancho dos signos)"%k,"fala":t1[2],"movimentacao":[line],"takes":[0]}]
    cen['passos']=["Este vídeo é da série do S3: o corpo (Takes 2 a 9) é o do %s, que você já gera. Aqui você gera SÓ o Take 1 (15 créditos)."%bk,
      "Não gere imagem: use a IMAGEM 1 do %s."%bk,
      "Na Central do curso, preencha a configuração (seção “Central do curso: o que preencher”) e cole a fala e a linha de movimentação do Take 1 (uma colagem de 1 take). Clique em GERAR PROMPT DE ANIMAÇÃO e confira que saiu 1 take. Não clique em “Resetar valores” nem em “REGERAR BLOCO”.",
      "No agente do Flow, anexe a IMAGEM 1 do %s (só ela), cole o aviso e, embaixo, o “COPIAR TUDO JUNTO”, sem editar. Renomeie o arquivo com o nome do painel."%bk,
      "Depois junte, nesta ordem: o Take 1 novo (%s) + os takes T2 a T9 do %s, passe pelo corte de silêncio e ponha textos e legenda."%(t1[1],bk)]
    cen['conferir']="Conferir: é a Nora v2 da IMAGEM 1 do %s; o objeto fica na mesma mão do começo ao fim; a fala sai completa, uma vez só, em inglês, com a data e os signos certos; sem texto, legenda ou música."%bk
    cen['agente']={"imagem":"IMAGEM 1","aviso":"Irei enviar 1 prompt para você. Quero que seja feita uma animação da imagem anexada. Utilize a imagem anexada como frame inicial e frame final no vídeo que você gerar.","passos":["Abra uma conversa nova no agente do Flow.","Anexe a IMAGEM 1 do %s (a única imagem)."%bk,"Cole o aviso e, embaixo, o bloco copiado com “COPIAR TUDO JUNTO” da Central, sem editar nada.","Envie, confira o vídeo e renomeie o arquivo."]}
    L=[dict(nome=t1[1],tipo='gancho',status='gerar',creditos=15,descricao='Take 1: “%s”'%t1[2],base='Gancho do viral S3 (signos + data): é o único take novo deste vídeo.',serve='Só deste vídeo.')]
    for i,t in enumerate(V[bk]['T'][1:],start=2):
        L.append(dict(nome='%s-T%d-%s'%(k,i,V[bk]['tn'][i-1]),de=t[1],tipo='corpo' if i<8 else 'CTA',status='reutilizar',creditos=15 if i<9 else 12,descricao='Take %d (o mesmo do %s)'%(i,bk),fala=t[2]))
    d['pecas']=dict(lista=L,decisao=["Série do S3: o corpo e o CTA são os do %s e só o gancho muda (15 créditos)."%bk])
    return d
def pack_full(k):
    d=B.pack(k)
    d['pecas']['decisao']=["Corpo copiado do viral S3 (avatar dos signos), com poucas mudanças.","Sem pré-gancho. Este corpo (Takes 2 a 9) serve também ao %s: só o Take 1 muda."%('nora31' if k=='nora30' else 'nora33')]
    for x in d['pecas']['lista']:
        tipo=x['tipo']
        if x['nome'].endswith('-IMG'):
            x['descricao']='Primeiro e último quadro de todos os takes, gerada na Central de imagens (cristal grande na mão). Serve também ao %s.'%('nora31' if k=='nora30' else 'nora33')
            x['serve']='Série do S3: a mesma imagem no %s.'%('nora31' if k=='nora30' else 'nora33')
        elif '-T1-' in x['nome']:
            x['base']='Gancho do viral S3 (signos + data).'; x['serve']='Só deste vídeo.'
        elif tipo=='CTA':
            x['base']='Selos, código 222 e story do viral S3.'; x['serve']='Corpo e CTA da série: o %s reaproveita.'%('nora31' if k=='nora30' else 'nora33')
        else:
            x['base']='Corpo copiado do viral S3.'; x['serve']='Corpo da série: o %s reaproveita.'%('nora31' if k=='nora30' else 'nora33')
        if x['nome'].endswith('T9-cta-b-parte-dois'): x['creditos']=12
    d['central']['passos']=[x.replace('135 créditos','132 créditos') for x in d['central']['passos']]
    d['mapa_tela']['legenda']=[69,77]
    if k!='nora30': d['mapa_tela']['regras'].insert(0,'Neste vídeo a legenda fica MAIS BAIXO (69% a 77%) e em blocos de 2 a 3 palavras: o pulso da mão que segura o objeto desce até uns 75% da altura, no lado direito. Y da legenda no CapCut: −294.')
    d['videos'][8]['duracao']=8
    return d
if __name__=='__main__':
    t=open(ROOT+'PAINEL-MODELO.html',encoding='utf-8').read()
    for k in ('nora30','nora31','nora32','nora33'):
        d=pack_full(k) if k in ('nora30','nora32') else (pack_pre(k) if k=='nora31' else pack_series(k))
        if k=='nora30':
            js=json.dumps(d,ensure_ascii=False)
            for x,y in (("na mão direita, com a esquerda livre","na mão ESQUERDA dela (o lado DIREITO da imagem), com a direita livre (imagem aprovada em 21/10/2026: as linhas de movimentação foram escritas para ela; se você gerar outra, o geodo tem de estar na mesma mão)"),
                        ("grande na mão direita)","grande na mão ESQUERDA dela, o lado DIREITO da imagem)"),
                        ("A mão que segura é a direita dela (o lado ESQUERDO da imagem).","Imagem aprovada em 21/10/2026: o geodo está na mão ESQUERDA dela (o lado DIREITO da imagem).")):
                js=js.replace(x,y)
            d=json.loads(js)
        json.dump(d,open(SPD+'pacote_%s.json'%k,'w'),ensure_ascii=False,indent=1)
        h=t.replace('<title>Painel de Produção</title>','<title>Painel %s</title>'%k).replace('const PACOTE = null;','const PACOTE = '+json.dumps(d,ensure_ascii=False)+';')
        for a,b in (() if k=='nora31' else (("Faça depois que os takes do corpo (sem o pré-gancho) estiverem prontos","Faça depois que os takes estiverem prontos"),
            ("O pré-gancho é outro arquivo: não entra nesta ferramenta, entra no CapCut depois. Arraste o vídeo do corpo","Este vídeo NÃO tem pré-gancho: o vídeo começa direto no Take 1 e vai inteiro nesta ferramenta. Arraste o vídeo"),
            ("No CapCut: pré-gancho primeiro, depois o corpo cortado, e então os textos da seção seguinte.","No CapCut: abra o vídeo cortado (sem pré-gancho) e ponha os textos da seção seguinte; o primeiro texto entra no segundo 0."),
            ("Já com o pré-gancho e os takes aprovados, monte o vídeo","Já com os takes aprovados (este vídeo não tem pré-gancho), monte o vídeo"))):
            assert h.count(a)==1,a[:40]
            h=h.replace(a,b)
        open(ROOT+'PAINEL-%s.html'%k.upper(),'w',encoding='utf-8').write(h)
        print(k,'ok',len(d['videos']),len(d['pecas']['lista']))
