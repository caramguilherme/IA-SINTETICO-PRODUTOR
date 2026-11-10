# -*- coding: utf-8 -*-
import sys,json,copy
SPD='/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/44224f14-0984-54fb-bdf2-ce721dd3e853/scratchpad/'
for d in ('r10','r9','r8','r7','r6'): sys.path.insert(0,SPD+d)
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
 id='nora30-SERIE-S3-TOURO-VIRGEM-CAPRICORNIO', titulo='Touro, Virgem e Capricórnio: o portal do Soulmate',
 dor='o homem que o universo guardou (Soulmate), a solidão e o bloqueio de amor',
 formato='Corpo copiado do viral S3 (Soulmate por signos), 9 takes',
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
p8.MOVL['nora30']=mov10.lines(p8.L30)
SER={
 'nora31':dict(h='aries-leao-sagitario',titulo='Áries, Leão e Sagitário: o portal do Soulmate',leg="Aries, Leo, Sagittarius: pay very close attention. 🔮\nPart 2 is in my story. Comment 222. Tap my photo NOW.",hook=("Aries, Leo, Sagittarius: pay very close attention","Aries, Leo","watching this"),hora='21/10 21h30'),
 'nora32':dict(h='gemeos-libra-aquario',titulo='Gêmeos, Libra e Aquário: o portal do Soulmate',leg="Gemini, Libra, Aquarius: pay very close attention. 🔮\nPart 2 is in my story. Comment 222. Tap my photo NOW.\n#astrology #zodiac #usa #usareels",hook=("Gemini, Libra, Aquarius: pay very close attention","Gemini, Libra","watching this"),hora='22/10 18h30'),
 'nora33':dict(h='cancer-escorpiao-peixes',titulo='Câncer, Escorpião e Peixes: o portal do Soulmate',leg="Cancer, Scorpio, Pisces: pay very close attention. 🔮\nPart 2 is in my story. Comment 222. Tap my photo NOW.",hook=("Cancer, Scorpio, Pisces: pay very close attention","Cancer, Scorpio","watching this"),hora='22/10 21h30'),
}
for k,s in SER.items():
    t1=S10.H[k]
    V[k]=dict(id='%s-SERIE-S3-%s'%(k,s['h'].upper()),sem_pre=True,v31=True,titulo=s['titulo'],dor='o homem que o universo guardou (Soulmate), a solidão e o bloqueio de amor',
      formato='Série do S3: só o Take 1 muda (o corpo é o do nora30)',molde='cópia do viral S3 (avatar dos signos): gancho por signos + data',code='222',fixos=('222','11:11'),pre=dict(dur=0,texto=""),
      hooktext=s['hook'],dest='portal, seal e stories',objpt='a folha de louro com o símbolo de Vênus (a mesma do nora30)',legenda=s['leg'],
      pin_ig=V['nora30']['pin_ig'],pin_fb=V['nora30']['pin_fb'],T=[(t1[0],'%s-T1-gancho-%s'%(k,s['h']),t1[3],t1[4],t1[5])],tn=['gancho-'+s['h']])
def pack_series(k):
    base=B.pack('nora30')                       # imagem, config e story do nora30
    v=V[k]; d=copy.deepcopy(base); t1=v['T'][0]
    line=p8.MOVL['nora30'][0]
    d['roteiro'].update({"id":v['id'],"titulo":v['titulo'],"dor":v['dor'],"formato":v['formato'],"molde_hook":v['molde'],"duracao_total":90,"descricao_instagram":v['legenda'],"leitura_registro":LEIT+" Este vídeo usa o corpo do nora30; só o Take 1 é novo."})
    d['refs']=['IMAGEM 1 do nora30 (arquivo já gerado e aprovado)']
    d['imagens']=[{"rotulo":"IMAGEM 1","cena":"A mesma do nora30 (não gerar)."}]
    d.pop('imagem_central',None)
    d['imagem_reutilizada']={"arquivo":"nora30-IMG (a IMAGEM 1 do nora30)","aviso":"Use a MESMA IMAGEM 1 do nora30 (a Nora com a folha de louro na mão direita). Anexe só ela no agente do Flow. Não gere imagem nova."}
    d['videos']=[{"rotulo":"V1","cena":"Take 1/9 · "+t1[0],"duracao":10,"primeiro_quadro":"IMAGEM 1","acao":"(ver movimentação)","b_roll":"","fala":t1[2],"movimentacao":line,"arquivo":t1[1]}]
    d['texto_tela']={"hook":v['hooktext'][0],"hook_comeca":v['hooktext'][1],"hook_termina":v['hooktext'][2],"hook_alt":"","extras":[]}
    d['comentario_fixado']={"insta":v['pin_ig'],"face":v['pin_fb']}
    d['edicao_linha']=B.EDLINE(k)
    cen=d['central']
    cen['colagens']=[{"titulo":"%s: só o Take 1 (gancho dos signos)"%k,"fala":t1[2],"movimentacao":[line],"takes":[0]}]
    cen['passos']=["Este vídeo é da série do S3: o corpo (Takes 2 a 9) é o do nora30, que você já gera. Aqui você gera SÓ o Take 1 (15 créditos).",
      "Não gere imagem: use a IMAGEM 1 do nora30.",
      "Na Central do curso, preencha a configuração (seção “Central do curso: o que preencher”) e cole a fala e a linha de movimentação do Take 1 (uma colagem de 1 take). Clique em GERAR PROMPT DE ANIMAÇÃO e confira que saiu 1 take. Não clique em “Resetar valores” nem em “REGERAR BLOCO”.",
      "No agente do Flow, anexe a IMAGEM 1 do nora30 (só ela), cole o aviso e, embaixo, o “COPIAR TUDO JUNTO”, sem editar. Renomeie o arquivo com o nome do painel.",
      "Depois junte, nesta ordem: o Take 1 novo (%s) + os takes T2 a T9 do nora30, passe pelo corte de silêncio e ponha textos e legenda."%t1[1]]
    cen['conferir']="Conferir: é a Nora v2 da IMAGEM 1 do nora30; a folha de louro fica na mesma mão do começo ao fim; a fala sai completa, uma vez só, em inglês, com a data e os signos certos; sem texto, legenda ou música."
    cen['agente']={"imagem":"IMAGEM 1","aviso":"Irei enviar 1 prompt para você. Quero que seja feita uma animação da imagem anexada. Utilize a imagem anexada como frame inicial e frame final no vídeo que você gerar.","passos":["Abra uma conversa nova no agente do Flow.","Anexe a IMAGEM 1 do nora30 (a única imagem).","Cole o aviso e, embaixo, o bloco copiado com “COPIAR TUDO JUNTO” da Central, sem editar nada.","Envie, confira o vídeo e renomeie o arquivo."]}
    L=[dict(nome=t1[1],tipo='gancho',status='gerar',creditos=15,descricao='Take 1: “%s”'%t1[2],base='Gancho do viral S3 (signos + data): é o único take novo deste vídeo.',serve='Só deste vídeo.')]
    for i,t in enumerate(V['nora30']['T'][1:],start=2):
        L.append(dict(nome='%s-T%d-%s'%(k,i,V['nora30']['tn'][i-1]),de=t[1],tipo='corpo' if i<8 else 'CTA',status='reutilizar',creditos=15 if i<9 else 12,descricao='Take %d (o mesmo do nora30)'%i,fala=t[2]))
    d['pecas']=dict(lista=L,decisao=["Série do S3: o corpo e o CTA são os do nora30 e só o gancho muda (15 créditos). É a receita dos seus campeões e é como o viral faz."])
    return d
def pack_nora30():
    d=B.pack('nora30')
    d['pecas']['decisao']=["Corpo copiado do viral S3 (avatar dos signos), com poucas mudanças, a pedido do Eduardo e seu.","Sem pré-gancho (teste), IMAGEM 1 já aprovada (folha de louro). Este corpo (Takes 2 a 9) serve também ao nora31, nora32 e nora33: só o Take 1 muda."]
    for x in d['pecas']['lista']:
        if x['nome'].endswith('T9-cta-b-parte-dois'): x['creditos']=12
    d['videos'][8]['duracao']=8
    return d
if __name__=='__main__':
    t=open(ROOT+'PAINEL-MODELO.html',encoding='utf-8').read()
    for k in ('nora30','nora31','nora32','nora33'):
        d=pack_nora30() if k=='nora30' else pack_series(k)
        json.dump(d,open(SPD+'pacote_%s.json'%k,'w'),ensure_ascii=False,indent=1)
        h=t.replace('<title>Painel de Produção</title>','<title>Painel %s</title>'%k).replace('const PACOTE = null;','const PACOTE = '+json.dumps(d,ensure_ascii=False)+';')
        for a,b in (("Faça depois que os takes do corpo (sem o pré-gancho) estiverem prontos","Faça depois que os takes estiverem prontos"),
            ("O pré-gancho é outro arquivo: não entra nesta ferramenta, entra no CapCut depois. Arraste o vídeo do corpo","Este vídeo NÃO tem pré-gancho: o vídeo começa direto no Take 1 e vai inteiro nesta ferramenta. Arraste o vídeo"),
            ("No CapCut: pré-gancho primeiro, depois o corpo cortado, e então os textos da seção seguinte.","No CapCut: abra o vídeo cortado (sem pré-gancho) e ponha os textos da seção seguinte; o primeiro texto entra no segundo 0."),
            ("Já com o pré-gancho e os takes aprovados, monte o vídeo","Já com os takes aprovados (este vídeo não tem pré-gancho), monte o vídeo")):
            assert h.count(a)==1,a[:40]
            h=h.replace(a,b)
        open(ROOT+'PAINEL-%s.html'%k.upper(),'w',encoding='utf-8').write(h)
        print(k,'ok',len(d['videos']),len(d['pecas']['lista']))
