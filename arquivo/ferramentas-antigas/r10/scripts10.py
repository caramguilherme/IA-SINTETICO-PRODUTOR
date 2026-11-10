# -*- coding: utf-8 -*-
# Série S3 (Soulmate por signos): corpo copiado do viral S3 (avatar dos signos), 9 takes. Só o Take 1 muda por vídeo.
BODY=[
 ("Segredo e escassez (não é para todos)","T2","corpo-nao-sei-seu-nome",
  "I do not know your name, but do not scroll. This is a final warning. The love portal has opened.",
  "Eu não sei o seu nome, mas não role a tela. Este é um aviso final. O portal do amor se abriu.",
  "Ela mantém um olhar firme e sério para a lente."),
 ("O homem que o universo guardou","T3","corpo-homem-guardado",
  "The man the universe kept for you is finally being released. Close your right hand and listen until the end.",
  "O homem que o universo guardou para você finalmente está sendo liberado. Feche a mão direita e ouça até o fim.",
  "Ela faz um aceno lento de cabeça e abre a palma esquerda para a lente."),
 ("O universo escolheu você (correntes)","T4","corpo-universo-escolheu",
  "The universe has chosen you. If you skip now, the energy breaks. The chains keeping you trapped in loneliness are being broken.",
  "O universo escolheu você. Se você pular agora, a energia se quebra. As correntes que te prendem na solidão estão sendo quebradas.",
  "Ela ergue um dedo da mão esquerda e depois aponta para a lente."),
 ("O bloqueio de amor volta + enviar","T5","corpo-bloqueio-de-amor",
  "The love block that was cast on you is going straight back to whoever sent it. Send this video to yourself.",
  "O bloqueio de amor que foi lançado sobre você está voltando direto para quem o mandou. Mande este vídeo para você mesma.",
  "Ela balança a cabeça uma vez com uma expressão firme e aponta para a lente."),
 ("Prazo de sete minutos + salvar","T6","corpo-sete-minutos",
  "In seven minutes, you're going to come back to confirm the shift. Open your hand and save this video.",
  "Em sete minutos, você vai voltar para confirmar a mudança. Abra a mão e salve este vídeo.",
  "Ela abre a palma esquerda para a lente e faz um aceno de cabeça."),
 ("Os dois selos","T7","corpo-dois-selos",
  "That will be your first seal. Double tap quickly on your screen. That will be your second seal.",
  "Esse será o seu primeiro selo. Toque duas vezes na tela rapidamente. Esse será o seu segundo selo.",
  "Ela ergue um dedo e depois dois dedos da mão esquerda."),
 ("Código 222 + o story","T8","cta-a-comente-222-story",
  "Type 222 so I can see you did everything. Tap my profile picture and check my stories before they disappear.",
  "Digite 222 para eu ver que você fez tudo. Toque na minha foto de perfil e veja os meus stories antes que sumam.",
  "Ela aponta o indicador esquerdo para a lente e mantém o olhar firme."),
 ("Fecho (a parte dois está no story)","T9","cta-b-parte-dois",
  "The second part of this sign is waiting for you there. Don't leave without it.",
  "A segunda parte deste sinal está esperando por você lá. Não saia sem ela.",
  "Ela abre a palma esquerda para a lente, com um meio sorriso."),
]
def hook(signs,date,sfile):
    return ("Gancho (signos + data)","T1","gancho-%s"%sfile,
      "%s. Keep your mouth shut after watching this. Not everyone will see this before %s."%(signs,date),
      "%s. Fique de boca fechada depois de ver isto. Nem todo mundo vai ver isto antes de %s."%(signs,date),
      "Ela olha firme para a lente e levanta três dedos da mão esquerda, com o objeto na mão direita.")
H={
 'nora30':hook("Taurus, Virgo, or Capricorn","Thursday, October 22nd","touro-virgem-capricornio"),
 'nora31':hook("Aries, Leo, or Sagittarius","Thursday, October 22nd","aries-leao-sagitario"),
 'nora32':hook("Gemini, Libra, or Aquarius","Friday, October 23rd","gemeos-libra-aquario"),
 'nora33':hook("Cancer, Scorpio, or Pisces","Friday, October 23rd","cancer-escorpiao-peixes"),
}
H['nora31']=("Gancho (o que você fez?)","T1","gancho-o-que-voce-fez",
 "What the hell did you just do? Aries, Leo, or Sagittarius. Keep your mouth shut after watching this.",
 "O que diabos você acabou de fazer? Áries, Leão ou Sagitário. Fique de boca fechada depois de ver isto.",
 "Ela olha para o curativo e depois para a lente, com as sobrancelhas levantadas, segurando a calcinha com as duas mãos.")
def full(k,body=None):
    body=body or k
    T=[(H[k][0],'%s-T1-%s'%(k,H[k][2]),H[k][3],H[k][4],H[k][5])]
    for (t,tn,nm,en,pt,vis) in BODY:
        T.append((t,'%s-%s-%s'%(body,tn,nm),en,pt,vis))
    return T
if __name__=='__main__':
    import re
    T=full('nora30')
    print([len(t[2].split()) for t in T],sum(len(t[2].split()) for t in T))
    s=' '.join(t[2] for t in T); sents=re.findall(r'[^.!?]+[.!?]',s)
    for cap in (22,23,24):
        takes=[];cur=[]
        for x in sents:
            n=len(x.split())
            if cur and sum(len(y.split()) for y in cur)+n>cap: takes.append(cur);cur=[]
            cur.append(x)
        takes.append(cur); print(cap,[sum(len(y.split()) for y in t) for t in takes])
