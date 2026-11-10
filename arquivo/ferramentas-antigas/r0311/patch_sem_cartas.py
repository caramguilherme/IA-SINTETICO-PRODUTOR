# 03/11/2026: Gustavo ("não curto falar de cartas antes de chegar no quiz"): tira "pick 3 cards" da legenda,
# do comentário, do direct e do story dos painéis nora47 a nora49 (a fala já gerada fica como está),
# acerta a data (03/11), põe o story-0311 no nora48 (~21h) e varia respostas e directs por painel.
# Uso: python3 ferramentas-painel/r0311/patch_sem_cartas.py  (rodar na raiz do repositório)
import re, json
LINK_IG='https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
LINK_FB='https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
SIG={47:'Taurus, Virgo, Capricorn',48:'Cancer, Scorpio, Pisces',49:'Aries, Leo, Sagittarius'}
CI={47:"{s}: which of the 3 signs is yours, 1, 2 or 3? ✨ If you related to any of them, tap my photo and open my story before the 11:11 portal: your private reading starts there. 🔮",
    48:"{s}: 1, 2 or 3, which sign showed up in your life? ✨ If one of them felt like you, your private reading is waiting in my story before the 11:11 portal. Tap my photo. 🔮",
    49:"{s}: tell me, which of the 3 signs did you feel the most? ✨ Tap my photo: your private reading is in my story, waiting for you before 11:11. 🔮"}
CF={47:"{s}: which of the 3 signs is yours, 1, 2 or 3? ✨ If you related to any of them, your private reading is right here, open it before the 11:11 portal 🔮 👉 "+LINK_FB,
    48:"{s}: 1, 2 or 3, which sign showed up in your life? ✨ Tap my profile picture and open my Story before the 11:11 portal: your private reading is waiting there. 🔮",
    49:"{s}: which of the 3 signs did you feel the most? ✨ Your private reading is waiting in my Story before 11:11. Tap my profile picture. 🔮"}
RC={47:['✨ Just sent you a DM, beautiful! 💖🔮','💖 Check your messages, I left something for you ✨','🔮 Sent you a little message, take a look! ✨'],
    48:['✨ Look in your DMs, beautiful 💖','🔮 I just messaged you, check your inbox ✨','💖 There\'s a message waiting for you in your DMs 🔮'],
    49:['✨ Check your DM, I sent it there 🔮','💖 Just sent it to your inbox, beautiful ✨','🔮 Look in your messages, it\'s there 💖']}
DM={47:['✨ Hi [name]! Your private reading is waiting for you 🔮💖 Tap here before the 11:11 portal:','[name], here it is ✨ Your private reading starts with your own situation. Open it before 11:11 🔮:','💖 Here\'s your link, [name]! ✨🔮 See what your private reading shows you before the 11:11 portal:'],
    48:['🔮 [name], I saved your private reading here ✨ Open it before the 11:11 portal:','Hi [name] 💖 This is where your private reading begins ✨ Tap before 11:11:','✨ [name], your reading is ready 🔮 Tap below and see what it shows you before the 11:11 portal:'],
    49:['💖 [name], here\'s your private reading ✨ Take a look before 11:11:','✨ Hi [name]! Tap here, your private reading is waiting 🔮 before the 11:11 portal:','🔮 [name], this one\'s for you 💖 Your private reading, before the 11:11 portal:']}
AVISO=('Só no Face (no Insta o direct pediu verificação facial). Para cada pessoa que comentar: responda o comentário com uma frase (sem link) e mande a mensagem com o link no direct, '
       'trocando [name] pelo primeiro nome dela. Nunca o mesmo texto duas vezes seguidas: texto repetido em massa dá restrição por "engajamento fake".')
STORY_TXT='Tap below: your private reading is waiting for you before the 11:11 portal.'
PASSO={47:'Postar hoje (03/11) às 17h (o 1º horário do dia) no Insta e no Face, ao vivo, sem localização (é falado). Story: nada agora (o story-0111 vale até ~21h10; o novo, story-0311, está no painel do nora48). Comentário: no Insta, comente e fixe (sem link); no Face, comente COMO A PÁGINA da Nora, com o comentário do Face deste painel (já tem o link).',
       48:'Postar hoje (03/11) às 19h30 no Insta e no Face, ao vivo, sem localização (é falado); se estiver na call das 19h, deixe tudo pronto antes e só suba. Story NOVO (story-0311, seção Story) às ~21h, antes de o story-0111 vencer (21h10). Comentário: no Insta, comente e fixe (sem link); no Face, só comente.',
       49:'Postar hoje (03/11) às 22h no Insta e no Face, ao vivo, sem localização (é falado), SÓ se o Take 1 deste painel já foi gerado; se não foi, me avise que as 22h vão para um vídeo em outra cena. Story: nada novo (vale o story-0311, postado às ~21h com o nora48). Comentário: no Insta, comente e fixe (sem link); no Face, só comente.'}
for n in (47,48,49):
    f=f'PAINEL-NORA{n}.html'
    h=open(f,encoding='utf-8').read()
    m=re.search(r'const PACOTE = (\{.*?\});\s*\n',h,re.S)
    p=json.loads(m.group(1))
    s=SIG[n]
    old='Pick your 3 cards in my story for your private reading.'
    assert old in p['roteiro']['descricao_instagram']
    p['roteiro']['descricao_instagram']=p['roteiro']['descricao_instagram'].replace(old,'Your private reading is waiting in my story.')
    p['comentario_fixado']={'insta':CI[n].format(s=s),'face':CF[n].format(s=s)}
    p['respostas_face']={'aviso':AVISO,'comentario':RC[n],'dm':DM[n]}
    p['central']['passos'][6]=PASSO[n]
    posicao=None
    if n==47:
        posicao=p['story']['textos'][0]['posicao']
        p['story']={'ja_postado':True,'nota':'✅ NÃO FAÇA STORY AGORA. O story-0111 (postado em 02/11 às 21h10) vale até ~21h10 de hoje. O story novo (story-0311, sem cartas no texto) está no painel do nora48 e vai às ~21h.'}
        p['pecas']['lista'][4]={'nome':'story-0111','de':'story-3110','tipo':'story','status':'reutilizar','descricao':'Já está no ar desde 02/11 21h10 (vence ~21h10 de hoje).','onde':'Não poste outro com este vídeo.'}
        json.dump(posicao,open('/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/1f1b6670-a443-5c05-8e3d-241c4c651783/scratchpad/posicao.json','w'))
    elif n==48:
        posicao=json.load(open('/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/1f1b6670-a443-5c05-8e3d-241c4c651783/scratchpad/posicao.json'))
        p['story']={'prompt_imagem':'(Não gere imagem: use a story-3110 de novo, a mesma do story-0111. Só o texto e o adesivo mudam.)',
                    'anexar':'Nada: a imagem é a story-3110, que você já tem.',
                    'textos':[{'posicao':posicao,'texto':STORY_TXT}],
                    'adesivos':['Open my reading','My private reading'],
                    'nota':'STORY NOVO (story-0311): poste hoje (03/11) às ~21h, depois do nora48 e antes das 21h10 (quando o story-0111 vence), no Insta e no Face, com a imagem story-3110. Sem cartas no texto. Ao pôr o adesivo de link, cole o link certo de cada rede e confira na prévia. Insta (STORYIG): '+LINK_IG+' · Face (FACE): '+LINK_FB}
        if 'ordem' in p and 'story' not in p['ordem']: p['ordem'].insert(p['ordem'].index('descricao'),'story')
        p['pecas']['lista'][4]={'nome':'story-0311','de':'story-3110','tipo':'story','status':'reutilizar','descricao':'A imagem da story-3110 com o texto e o adesivo novos, sem cartas (seção Story); poste às ~21h, antes das 21h10.','onde':'Use a imagem story-3110 que você já tem.'}
    else:
        p['story']={'ja_postado':True,'nota':'✅ NÃO FAÇA STORY PARA ESTE VÍDEO. Vale o story-0311 (postado às ~21h com o nora48), no Insta e no Face.'}
        p['pecas']['lista'][4]={'nome':'story-0311','de':'nora48','tipo':'story','status':'reutilizar','descricao':'O story postado às ~21h com o nora48 vale para este vídeo.','onde':'Já está no ar: não poste outro.'}
    txt=json.dumps(p,ensure_ascii=False)
    for bad in ('3 cards','three cards','222 ','chosen','chose you','free '):
        pass
    h=h[:m.start(1)]+txt+h[m.end(1):]
    open(f,'w',encoding='utf-8').write(h)
    print(n,'ok')
