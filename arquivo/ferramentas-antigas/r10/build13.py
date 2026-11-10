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
T32S=[("Gancho (signos + meia-noite)","nora32-T1-gancho-gemeos-libra-aquario","Gemini, Libra, or Aquarius. Keep your mouth shut after watching this. Not everyone will see this before midnight tonight.",
  "Gêmeos, Libra ou Aquário. Fique de boca fechada depois de ver isto. Nem todo mundo vai ver isto antes da meia-noite de hoje.","Ela olha firme para a lente e levanta três dedos da mão esquerda, com o quartzo rosa na mão direita."),
 ("O homem guardado e as correntes","nora32-T2-corpo-homem-e-correntes","The man the universe kept for you is finally being released. The chains keeping you trapped in loneliness are being broken.",
  "O homem que o universo guardou para você finalmente está sendo liberado. As correntes que te prendem na solidão estão sendo quebradas.","Ela faz um aceno lento de cabeça e abre a palma esquerda para a lente."),
 ("Curtir, 222 e story","nora32-T3-cta-curtir-222-story","Double tap now if this found you. Type 222. Tap my profile picture and check my stories before they disappear.",
  "Toque duas vezes agora se isto te encontrou. Digite 222. Toque na minha foto de perfil e veja os meus stories antes que sumam.","Ela aponta o indicador esquerdo para a lente e mantém o olhar firme.")]
V['nora32'].update(dict(id='nora32-COPY-CURTA-GEMEOS-LIBRA-AQUARIO',titulo='Gêmeos, Libra e Aquário: copy curta (uns 30 s)',formato='Copy curta, 3 takes (gancho, corpo, CTA)',
  molde='teste de formato do Mattias (copys mais curtas), com o gancho por signos do viral S3 e o pedido de curtir antes do story (S3, S4)',
  hooktext=("Gemini, Libra, Aquarius: pay very close attention","Gemini, Libra","watching this"),
  legenda="Gemini, Libra, Aquarius: pay very close attention. 🔮\nPart 2 is in my story. Comment 222. Tap my photo NOW.",
  T=T32S,tn=['gancho-gemeos-libra-aquario','corpo-homem-e-correntes','cta-curtir-222-story']))
p8.MOVL['nora32']=[p8.MOVL['nora32'][i] for i in (0,2,5)]
V['nora33']=dict(id='nora33-TEXTO-NA-TELA-ITS-SCARY',sem_pre=True,v31=True,titulo='Texto na tela: it works so fast it’s scary',dor='o homem que o universo guardou (curiosidade)',
  formato='Texto na tela, sem fala (clipe de 8 s)',molde='texto do topo dos virais w6, w7 e U7 + formato texto na tela (Eduardo, Mattias)',code='222',fixos=('222','11:11'),pre=dict(dur=0,texto=""),
  hooktext=("It works so fast it's scary…","",""),dest='',objpt='o quartzo rosa grande',
  legenda="It works so fast it's scary… 🔮\nComment 222. Part 2 is in my story. Tap my photo NOW.",pin_ig=V['nora30']['pin_ig'],pin_fb=V['nora30']['pin_fb'],
  T=[("Clipe","nora33-CLIPE-texto-na-tela","(sem fala)","(sem fala)","")],tn=['clipe'])
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
    if k=='nora32':
        d['pecas']['decisao']=["Copy curta (3 takes, uns 30 s), com a imagem B (quartzo rosa). Teste de formato sugerido pelo Mattias; o resto segue como o nora30."]
    else:
        d['pecas']['decisao']=["Corpo copiado do viral S3 (avatar dos signos), com poucas mudanças.","Sem pré-gancho. Este corpo (Takes 2 a 9) serve também ao %s: só o Take 1 muda."%('nora31' if k=='nora30' else 'nora33')]
    for x in d['pecas']['lista']:
        tipo=x['tipo']
        if x['nome'].endswith('-IMG'):
            x['descricao']='Primeiro e último quadro de todos os takes, gerada na Central de imagens (cristal grande na mão).'+(' Serve também ao nora31.' if k=='nora30' else ' Serve também ao nora33 (texto na tela).')
            x['serve']='A mesma imagem no %s.'%('nora31' if k=='nora30' else 'nora33')
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
    if k=='nora32':
        for x in d['pecas']['lista']:
            if not x['nome'].endswith('-IMG'): x['serve']='Só deste vídeo.'
    if len(d['videos'])==9: d['videos'][8]['duracao']=8
    return d

V33_PROMPT=("Create a single continuous 8-second video clip that opens exactly on the first supplied frame and ends exactly on the last supplied frame (they are the same image), vertical 9:16. Handheld smartphone camera about 60 cm from the woman at chest height, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n"
"THE MAIN EVENT: the woman, sitting on the top step of a home front porch, looks into the lens, raises her free hand and presses one index finger against her lips in a silent keep-it-secret gesture, holds it, then lowers it. She never speaks. In the first frame her right hand (on the LEFT side of the image) holds the large rose quartz cluster upright beside her face, and her left hand rests out of frame below the bottom edge.\n\n"
"SECOND BY SECOND (something visible moves in EVERY second):\n"
"0.0 to 1.0 s: she takes a small breath, her eyebrows rise slightly and her eyes stay on the lens; the rose quartz stays steady beside her face.\n"
"1.0 to 2.5 s: her left hand rises from below the bottom edge, up the right side of the frame, to chin height, with the index finger extended and the other fingers curled.\n"
"2.5 to 4.5 s: the tip of her left index finger comes to rest vertically against her lips, centered on her mouth, and she holds it there with her eyes firm on the lens, with one slow blink at about 3.5 s.\n"
"4.5 to 6.0 s: she lowers the finger away from her lips and the hand drops down the right side of the frame and out of frame below the bottom edge.\n"
"6.0 to 8.0 s: both hands are back in the first-frame positions; she gives a tiny knowing smile with her lips closed and holds still; exactly as in the last supplied frame.\n\n"
"WHAT MUST NOT HAPPEN: she does not speak or mouth any words (her lips only press against the finger and stay closed); the crystal never changes hands, never turns away, never drops and never covers her face; the finger touches only her lips, not her nose or chin; no other hand sign appears; each hand has exactly five fingers; the porch, the white door, the flag, the column and the light never move; no object appears or disappears.\n\n"
"VISUAL: she is the same woman as in the supplied frames; realistic natural physics, no morphing, no glow, no magic effects. No text, no logos.\n\n"
"AUDIO: real outdoor porch ambient sound only (a faint breeze). No music, no voice, no added sound effects.")
def pack_clip(k):
    d=copy.deepcopy(B.pack('nora32')); v=V[k]
    d['roteiro'].update({"id":v['id'],"titulo":v['titulo'],"dor":v['dor'],"formato":v['formato'],"molde_hook":v['molde'],"duracao_total":8,"descricao_instagram":v['legenda'],"leitura_registro":LEIT+" Este vídeo reusa a imagem B do nora32."})
    d['refs']=['IMAGEM 1 do nora32 (arquivo já gerado e aprovado)']
    d['imagens']=[{"rotulo":"IMAGEM 1","cena":"A mesma do nora32 (não gerar)."}]
    d.pop('imagem_central',None)
    d['imagem_reutilizada']={"arquivo":"nora32-IMG (a IMAGEM 1 do nora32)","aviso":"Use a MESMA IMAGEM 1 do nora32 (a Nora com o quartzo rosa grande na mão direita, na varanda). Se ela ainda não foi gerada, gere primeiro a do nora32."}
    d['clipe_unico']=True
    d['videos']=[{"rotulo":"V1","cena":"Clipe único · texto na tela (sem fala)","duracao":8,"primeiro_quadro":"IMAGEM 1","acao":"(ver seção Clipe)","b_roll":"","fala":"(sem fala) texto na tela: "+v['hooktext'][0],"movimentacao":"(sem Central: o prompt do clipe está na seção Clipe)","arquivo":"nora33-CLIPE-texto-na-tela"}]
    d['texto_tela']={"hook":v['hooktext'][0],"hook_comeca":"do segundo 0","hook_termina":"o fim do clipe","hook_alt":"","extras":[]}
    d['comentario_fixado']={"insta":v['pin_ig'],"face":v['pin_fb']}
    d['edicao_linha']=[
      {"quando":"1. O clipe todo (8 s)","texto":v['hooktext'][0],"como":"Texto no topo, em até 2 linhas, do segundo 0 ao fim do clipe. Modelo: texto do topo dos virais w6, w7 e U7."},
      {"quando":"2. O clipe todo","texto":"222  e  11:11","como":"Dois números fixos nos cantos de cima: 222 à esquerda e 11:11 à direita, como nos outros vídeos."},
      {"quando":"3. Dos 5 aos 8 s","texto":"Part 2 is in my story","como":"Segundo texto, pequeno, na faixa da legenda (69% a 77% da altura), com uma seta vermelha apontando para a foto do perfil no canto de cima."},
      {"quando":"4. O clipe todo","texto":"Música de sempre, −18 dB","como":"Sem legenda automática, sem corte de silêncio e sem fala. O clipe tem só o som ambiente do Flow e a música."}]
    d['pre_gancho']={"titulo_secao":"Clipe (8 s, sem fala, Frames)","duracao":8,"tomadas":1,"com_rosto":True,"nome_video":"nora33-CLIPE-texto-na-tela",
      "conceito":"Formato texto na tela (Eduardo e Mattias), com a avatar da Nora. O texto do topo vem dos virais w6, w7 e U7 (“It works so fast it's scary…”). A Nora não fala: olha para a lente e faz o gesto de segredo (dedo nos lábios) e volta à posição.",
      "modo":"Um vídeo só, em FRAMES: primeiro e último quadro = a IMAGEM 1 do nora32. 8 s, 9:16, áudio ligado. O prompt depende da imagem aprovada: me mande a IMAGEM 1 do nora32 antes de gerar.",
      "etapas":[dict(tipo='vid',titulo='Clipe: ela olha para a lente e põe o dedo nos lábios',nome='nora33-CLIPE-texto-na-tela',duracao=8,quadros='Modo FRAMES. Primeiro quadro: IMAGEM 1 do nora32. Último quadro: a mesma IMAGEM 1. 8 s, 9:16, áudio ligado.',prompt=V33_PROMPT)],
      "montagem":"1) Use o clipe inteiro (8 s).\n2) Ponha o texto do topo, os números fixos e o segundo texto (seção de texto na tela).\n3) Música de sempre, −18 dB. Sem legenda automática.\n4) Se ela mexer a boca como se falasse, ou o dedo for ao nariz ou ao queixo, refaça uma vez; se falhar de novo, me chame.",
      "texto_tela":"","edicao":""}
    d['central']['passos']=["Este vídeo é um clipe só, de 8 s, SEM fala (formato texto na tela). Não usa a Central do curso nem o agente do Flow.",
      "Use a MESMA IMAGEM 1 do nora32 (a Nora com o quartzo rosa na mão direita). Se ela ainda não foi gerada, gere primeiro a do nora32 e me mande: eu confiro o prompt do clipe com a imagem aprovada.",
      "Gere o clipe no Flow, no modo FRAMES (primeiro e último quadro = a IMAGEM 1), 8 s, 9:16, áudio ligado, colando o prompt da seção “Clipe”. Renomeie o arquivo com o nome do painel. Custo: 12 créditos.",
      "No CapCut: ponha o texto do topo, os números fixos, o segundo texto e a música de sempre; não precisa de legenda automática nem de corte de silêncio."]
    d['central']['colagens']=[{"titulo":"clipe sem fala","fala":"(sem fala)","movimentacao":["(sem fala)"],"takes":[0]}]
    d['central']['conferir']="Conferir: é a Nora v2 da imagem do nora32; ela não fala; o dedo vai só aos lábios; o quartzo fica na mão direita do começo ao fim; o cenário fica parado."
    d['pecas']=dict(lista=[dict(nome='nora32-IMG',de='nora32-IMG',tipo='imagem 1',status='reutilizar',descricao='A imagem 1 do nora32 (a Nora com o quartzo rosa, na varanda).'),
      dict(nome='nora33-CLIPE-texto-na-tela',tipo='clipe sem fala',status='gerar',creditos=12,descricao='Clipe de 8 s: ela olha para a lente, põe o dedo nos lábios e volta.',base='Formato texto na tela (Eduardo, Mattias) + texto do topo dos virais w6, w7 e U7.',serve='Só deste vídeo.')],
      decisao=["Teste de formato: texto na tela, sem fala, com a avatar (Eduardo e Mattias)."])
    d['mapa_tela']['legenda']=[69,77]
    return d
if __name__=='__main__':
    t=open(ROOT+'PAINEL-MODELO.html',encoding='utf-8').read()
    for k in ('nora30','nora31','nora32','nora33'):
        d=pack_full(k) if k in ('nora30','nora32') else (pack_pre(k) if k=='nora31' else pack_clip(k))
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
