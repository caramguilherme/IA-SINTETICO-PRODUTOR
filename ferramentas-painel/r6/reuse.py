# -*- coding: utf-8 -*-
import data
NAMES={
'nora25':['gancho-azar','corpo-prova','corpo-venus-x-sol','corpo-reconhecimento','corpo-lua-segredo','corpo-escassez','cta-a-quiz-venus','cta-b-comente-venus'],
'nora26':['gancho-lua','corpo-sente-mais','corpo-sol-venus-lua','corpo-duas-coisas','corpo-segunda-coisa','corpo-garantia','cta-a-segunda-coisa','cta-b-toque-dois-toques'],
'nora27':['gancho-dois-tipos','corpo-voce-conhece','corpo-nao-e-quebrada','corpo-depende-venus','corpo-imagine','corpo-nao-passe-direto','cta-condensado-match'],
'nora28':['gancho-signos-fogo','corpo-cai-rapido','corpo-ninguem-contou','corpo-venus-fora-do-signo','cta-a-quiz-venus','cta-b-salve-chart'],
}
for k,v in data.V.items():
    assert len(NAMES[k])==len(v['takes']),k
    v['own']=len(v['takes'])
    v['tnames']=['%s-T%d-%s'%(k,i+1,NAMES[k][i]) for i in range(len(v['takes']))]

DECISAO=[
 "Créditos não são mais um limite (você comprou 1000). Por isso cada vídeo sai completo, com o CTA que combina com o gancho, o objeto e o código dele. Não economizei nada que valesse menos conversão.",
 "O reaproveitamento fica para depois de gerar, e eu decido peça por peça. Dos seus 24 vídeos, os dois campeões (B3 com 2.551 views e C4 com 1.427) vieram da receita \"corpo e CTA gerados uma vez, só o gancho muda\". Então os melhores candidatos a reaproveitar são sempre o corpo e o CTA de um vídeo que performar.",
 "O que prende no começo (pré-gancho, gancho e texto na tela) nunca é reaproveitado: nos campeões era gancho direto, com promessa e \"this message is not for everyone\".",
 "Só reaproveito com a mesma Nora e a mesma imagem de base (o mesmo \"kit\"). Um corpo ou CTA de outro vídeo, com outra roupa e outro objeto na mão, aparece como um corte estranho. Takes da Nora antiga (nora01 a nora24) e da Dana não entram.",
 "Regra para escolher: depois de 2 a 3 dias de postagem, o vídeo que tiver mais retenção nos 3 s, mais tempo médio e mais comentários vira o \"kit campeão\": o corpo, o CTA e a imagem dele ganham ganchos novos (nora29 em diante, uns 22 créditos cada).",
]
BASE_TIPO={
 'PRE-IMG':"Pré-gancho com o rosto da avatar, já em ação: o que segurou 41 a 67% nos 3 s nos seus vídeos foi o pré-gancho curto, começando na ação.",
 'GANCHO':"Gancho direto, com promessa e a virada \"não é azar, é o padrão\" (briefing do Love Chart); molde dos campeões B3 e C4.",
 'CORPO':"Corpo de cold reading + mecanismo (Sol x Vênus) + escassez, no molde dos corpos que seguraram até o fim nos seus campeões.",
 'CTA':"Fecho validado: mandar para si, comentar a palavra e abrir o story; o código é o do vídeo.",
}
PROX=[
 dict(nome="nora29-T1-gancho-nunca-foi-seu",modelo="modelo B3 (2.551 views)",custo="22",gancho="Wipe your tears. The man who keeps leaving was never your person. It's not bad luck. It's your Venus.",texto="He was never your person."),
 dict(nome="nora30-T1-gancho-ultimo-sinal",modelo="modelo C4 (1.427 views)",custo="22",gancho="This is the last sign the universe will send you about him. Don't scroll past it. Your Venus has been telling you.",texto="Your last sign about him"),
 dict(nome="nora31-T1-gancho-para-de-olhar",modelo="modelo B1 / R1V",custo="22",gancho="If you still check his Instagram at night, stop. What I'm about to show you explains why you keep going back.",texto="Stop checking his Instagram."),
 dict(nome="nora32-T1-gancho-nao-era-ele",modelo="modelo B2 / B2V",custo="22",gancho="He wasn't the one. And in the next few days, you're going to understand why. It starts with your Venus.",texto="He wasn't the one."),
]
def pecas(k,CRED):
    v=data.V[k]; n=len(v['takes']); pre=v['pre']
    L=[]
    if k in ('nora26','nora27','nora28'):
      if k=='nora28':
        LST=[('A','imagem do pré-gancho','Tomada 1, primeiro quadro: câmera no chão olhando o círculo de sal aberto, com o pote inclinado (gerada do blueprint, sem o rosto).',None),('B','imagem do pré-gancho','Tomada 1, último quadro: edição da A, com o círculo fechado e a brasa acesa.',None),('V1','pré-gancho (vídeo)','Tomada 1 (4 s, Frames A para B): o sal cai e o isqueiro acende o feixe.',7),('C','imagem do pré-gancho','Tomada 2, primeiro quadro: a Nora inclinada, soprando, com o fio de fumaça (já gerada pelo aluno).',None),('D','imagem do pré-gancho','Tomada 2, último quadro: edição da C, com a coluna grossa de fumaça.',None),('V2','pré-gancho (vídeo)','Tomada 2 (4 s, Frames C para D): ela sopra e a fumaça cresce até a lente.',7)]
      elif k=='nora27':
        LST=[('A','imagem do pré-gancho','Tomada 1, primeiro quadro: o rosto dela e as duas mãos agarrando o canto do tapete (gerada do blueprint).',None),('B','imagem do pré-gancho','Tomada 1, último quadro: edição da A, com o tapete jogado e a tábua levantada.',None),('V1','pré-gancho (vídeo)','Tomada 1 (4 s, Frames A para B): ela arranca o tapete e levanta a tábua.',7),('C','imagem do pré-gancho','Tomada 2, primeiro quadro: câmera no chão olhando o esconderijo, com o pacote de veludo (gerada do blueprint, sem o rosto).',None),('D','imagem do pré-gancho','Tomada 2, último quadro: edição da C, com o veludo aberto e a carta Os Enamorados.',None),('V2','pré-gancho (vídeo)','Tomada 2 (4 s, Frames C para D): as mãos abrem o veludo e a carta aparece.',7)]
      else:
        LST=[('A','imagem do pré-gancho','Tomada 1, primeiro quadro: o rosto dela, a câmera no chão e o palito aceso sobre a primeira folha (gerada do blueprint).',None),('B','imagem do pré-gancho','Tomada 1, último quadro: edição da A, com as 3 primeiras folhas em chamas altas.',None),('V1','pré-gancho (vídeo)','Tomada 1 (4 s, Frames A para B): ela acende e o fogo salta.',7),('C','imagem do pré-gancho','Tomada 2, primeiro quadro: câmera no chão, 4 folhas em chamas enormes na frente da lente (gerada do blueprint, sem o rosto).',None),('D','imagem do pré-gancho','Tomada 2, último quadro: edição da C, com a linha inteira em chamas até a vela.',None),('V2','pré-gancho (vídeo)','Tomada 2 (4 s, Frames C para D): o fogo corre pelo corredor escuro.',7)]
      for sfx,tp,ds,cr in LST:
            d=dict(nome=k+'-PRE-'+sfx,tipo=tp,status='gerar',descricao=ds)
            if cr: d['creditos']=cr
            if sfx=='A': d['base']=BASE_TIPO['PRE-IMG']; d['serve']='Só deste vídeo (o começo é sempre novo).'
            L.append(d)
    else:
      L.append(dict(nome=k+'-PRE-IMG1',tipo='imagem do pré-gancho',status='gerar',descricao='Primeiro quadro do pré-gancho, com o rosto da Nora (gerada a partir do blueprint).',base=BASE_TIPO['PRE-IMG'],serve='Só deste vídeo (o começo é sempre novo).'))
      L.append(dict(nome=k+'-PRE-IMG2',tipo='imagem do pré-gancho',status='gerar',descricao='Último quadro: a edição da imagem 1 com o efeito terminado.'))
      L.append(dict(nome=k+'-PRE',tipo='pré-gancho (vídeo)',status='gerar',creditos=CRED[pre['dur']],descricao='Vídeo de %d s, silencioso, no modo Frames: %s'%(pre['dur'],pre['conceito'].replace('**','')[:140].rstrip()+'…')))
    L.append(dict(nome=k+'-IMG',tipo='imagem 1 do vídeo',status='gerar',descricao='Primeiro e último quadro de todos os takes (gancho, corpo e CTA), gerada na Central de imagens. É a CONTINUAÇÃO do pré-gancho: mesma roupa e mesmo cenário, e a Nora passa a falar (teste do nora25 ao nora28).',serve=('É o "kit" do nora25: se ele performar, as variações nora29 a nora32 usam esta mesma imagem.' if k=='nora25' else 'Se este vídeo performar, ela vira o kit de variações com gancho novo.')))
    for i,t in enumerate(v['takes']):
        cta=i>=n-(1 if k=='nora27' else 2)
        tipo='gancho' if i==0 else ('CTA' if cta else 'corpo')
        serve=('Só neste vídeo (cada gancho é novo).' if i==0 else 'Candidato a reaproveitar depois, em variações do mesmo kit, se o vídeo performar.')
        L.append(dict(nome=v['tnames'][i],tipo=tipo,status='gerar',creditos=15,descricao='Take %d, %s: “%s”'%(i+1,t[0],t[2][:110]+('…' if len(t[2])>110 else '')),base=BASE_TIPO['GANCHO' if i==0 else ('CTA' if cta else 'CORPO')],serve=serve))
    out=dict(lista=L,decisao=DECISAO)
    if k=='nora25':
        out['proximos_intro']="Se o nora25 performar, o corpo, o CTA e a imagem dele viram o kit campeão: cada variação custa só um pré-gancho novo (uns 7) mais um take de gancho (15). Eu monto o painel de cada uma quando você pedir. Os ganchos abaixo seguem os seus campeões."
        out['proximos']=PROX
    return out
