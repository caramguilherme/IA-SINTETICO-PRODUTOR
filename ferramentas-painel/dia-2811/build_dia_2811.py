# Painéis do dia 28/11/2026: nora85 (~22h15) e nora86 (~01h45 de 29/11, o MULTI-ÂNGULO), Insta e Face. O nora84 (~18h45) sai do build_dia_2711.py.
# A decisão do aluno (28/11 ~12h, "Pode montar" / "Sim"): o pacote do nora81 ganhou de novo (o nora81 fez 1.398 e o nora83, 505 com ~9 h; regra 13.3c)
#   e vira a base dos 3 vídeos do Insta; o "free" no CTA do Insta vai nos 3 (PENDENCIAS, item 5). Cada um com outra roupa e outro cômodo (a regra de 24/11).
# 28/11 17h30 (o aluno chegou em casa e começou a produzir os 3): o teste do dia passa a ser o MULTI-ÂNGULO no nora86 (a ideia dele: "muda a cada 2 takes"),
#   com o nora84 e o nora85 como controle (1 imagem só); os horários correm: nora84 ~18h45, nora85 ~22h15, nora86 ~01h45 (3h30 entre eles, REGRAS 7.4).
# Usa o gerador do build_dia_2711.py (o mesmo pacote, a mesma fala do nora84, com a data "before Monday, November thirtieth" e o "free").
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2811/build_dia_2811.py
import pathlib, importlib.util

R = pathlib.Path(__file__).resolve().parents[2]
s = importlib.util.spec_from_file_location('b2711', R / 'ferramentas-painel/dia-2711/build_dia_2711.py')
B27 = importlib.util.module_from_spec(s); s.loader.exec_module(B27)
FP, _img = B27.FLAG_PAREDE, B27._img
SEGURA = ('one hand holds one tarot card upright at collarbone height, below her chin, never touching or covering her face, showing only its plain gold '
          'patterned back the whole time; her other hand rests ')
STATUE = ('a colorful statue of Saint Michael the Archangel about 30 centimeters tall, standing at her left side at about the height of her waist, fully '
          'visible in the frame (never cut off and never hidden behind her)')
CONTROLE = ('ESTE VÍDEO É O CONTROLE do teste do dia: o mesmo pacote do nora81, com 1 imagem só (o ângulo parado). O teste, o multi-ângulo, vai no nora86. '
            'O “free” no CTA do Insta (o T13) vai nos 3 vídeos de hoje e se mede pelo clique, o checkout e a venda por clique no Tracker. A medida deste vídeo, '
            'com ~3 h: os compartilhamentos e os salvos, a curva (quantos chegam aos 30, 60 e 78 s) e a fatia dos EUA.')
TESTE_MULTI = ('O QUE ESTE VÍDEO TESTA: o MULTI-ÂNGULO, a sua ideia: 7 imagens do mesmo cantinho e da mesma roupa, um ângulo novo a cada 2 takes, para a tela não '
               'ficar parada. As fontes: o Robert (“Re-hook every few seconds”, v10, para a curva que cai sem parar no meio, que é a nossa); o Iorhan, 27/11 '
               '(0:26:42: “o avatar na tela, paradão, falando, tu tá muito atrás”); o vídeo do Gustavo no Muse (23/11). Contra o nora84 e o nora85 (o mesmo pacote, '
               '1 imagem só) e o nora83 (01h35, 505 com ~9 h). A medida: a curva (quantos chegam aos 30, 60 e 78 s), os compartilhamentos e os salvos com ~3 h e '
               'o tempo médio. O “free” no CTA do Insta vai nos 3. O cuidado do nora79 (os olhos e a voz mudaram entre as imagens): depois dos 4 primeiros clipes, '
               'me mande o T01 e o T03 para eu medir.')
STORY_OK = ('O story no ar é o de 01h35 de 28/11 (Insta e Face): vence ~01h35 de 29/11. Não precisa postar story agora. Antes de abrir o Insta, '
            'confira o IP e os EUA no mylocation.org.')

NOVOS = {
    'nora85': dict(
        dia='d2811', hora='~22h15 de 28/11 (era 20h30; 3h30 depois do nora84)', prazo='até ~21h45 de 28/11', pref='cozinha', img='d2811-cozinha-IMG',
        roupa_pt='suéter rosa antigo de tricô', obj_pt='uma carta (o verso dourado) na mão',
        lugar_pt='à mesa redonda da cozinha, à noite, com a estátua de São Miguel em cima dela',
        roupa='her plain dusty-rose knit sweater with no logo',
        cena=('Casual real video in the evening in a cozy American kitchen, she sits at a round wooden kitchen table; on the table a colorful statue of Saint '
              'Michael the Archangel, a white ceramic mug and a small potted plant (the statue at her left side, fully visible in the frame); ' + FP + ', filmed '
              'from a static camera about one meter in front of her at collarbone height, looking exactly like a real phone video, warm kitchen light. '),
        cam='the camera stays static about one meter in front of her at collarbone height with an unchanged framing',
        segura=SEGURA + 'on the kitchen table',
        objeto='the tarot card with its plain gold back in her hand, the kitchen table with the statue, the mug and the plant, and the framed flag',
        som='quiet kitchen sound', lugar_en='at the round table in her kitchen', luz='warm kitchen light in the evening',
        prompt_img=_img('she sits at a round wooden kitchen table in a cozy real American kitchen in the evening, warm kitchen light',
                        'a plain dusty-rose knit sweater with no logo',
                        'on the table, ' + STATUE + ', a white ceramic mug and a small potted plant',
                        'on the kitchen table', 'in the evening'),
        copia='o pacote do nora81 (as letras, a carta na mão, a estátua de São Miguel, as 2 frases de reinício), à mesa da cozinha',
        fix_muse=True, data='Monday, November thirtieth', free=True, teste_txt=CONTROLE, story=STORY_OK),
    'nora86': dict(
        dia='d2811', hora='~01h45 de 29/11 (era 0h00; 3h30 depois do nora85)', prazo='até ~01h15 de 29/11', pref='leitura', img='d2811-leitura-IMG-A',
        roupa_pt='cardigã mostarda sobre uma blusa branca lisa', obj_pt='uma carta (o verso dourado) na mão',
        lugar_pt='na poltrona do cantinho de leitura, tarde da noite, com a estante de livros atrás e a estátua de São Miguel na mesinha',
        roupa='her plain mustard-yellow knit cardigan over a plain white top, with no logo',
        cena=('Casual real video late at night in the reading corner of a cozy American home, she sits in a soft armchair with a tall wooden bookshelf behind her '
              'on the right; on a small round side table beside her a colorful statue of Saint Michael the Archangel and a stack of two books; the framed American '
              'flag hangs on the light wall; each pair of takes is filmed from its own static camera angle, always looking exactly like a real phone video, warm '
              'floor lamp light. '),
        cam='the camera stays static with exactly the framing and the angle of the reference image of this take, unchanged',
        segura=('one hand holds one tarot card with its plain gold patterned back, exactly as in the reference image, never touching or covering her face; '
                'her other hand stays exactly as in the reference image'),
        objeto='the tarot card with its plain gold back in her hand, the armchair, the side table with the statue and the books, the bookshelf and the framed flag',
        som='quiet room sound at night', lugar_en='in the armchair of her reading corner', luz='warm floor lamp light at night',
        prompt_img=_img('she sits in a soft armchair in the reading corner of her real American home late at night, a tall wooden bookshelf with books behind her '
                        'on the right, warm floor lamp light',
                        'a plain mustard-yellow knit cardigan over a plain white top, with no logo',
                        'on a small round side table beside her, ' + STATUE + ', and a stack of two books',
                        'on the armrest of the armchair', 'late at night'),
        copia='o pacote do nora81 (as letras, a carta na mão, a estátua de São Miguel, as 2 frases de reinício), no cantinho de leitura, em 7 ângulos',
        fix_muse=True, data='Monday, November thirtieth', free=True, teste_txt=TESTE_MULTI, multi=True,
        story=('ANTES DA 01h35 (o story de 28/11 vence ~01h35 de 29/11): reposte o story no Insta e no Face, com o adesivo de link de sempre (STORYIG no Insta, '
               'FACE no Face), mesmo que o nora86 ainda não esteja pronto. Antes de abrir o Insta, confira o IP e os EUA no mylocation.org.')),
}
for k, v in NOVOS.items():
    for w in ('chest', 'skin', 'body', 'breast', 'underwear', 'wine', 'powder', 'paint', 'shining', 'glowing', 'sparkling'):
        assert w not in v['prompt_img'].lower(), (k, w)

# Os textos: o pedido de comentário do Insta muda a cada post (o nora84 pediu "222"); o comentário da Página é novo (nenhum usado nas últimas 2 semanas).
TEXTOS = {
    'nora85': dict(
        insta=("If your letter is on this list, the doors that wouldn't open are about to open 🍀 Your private reading is waiting in my story 🔮\n"
               'Comment the first letter of your name ✨\n#manifestation #archangelmichael #2027 #lawofattraction #newchapter'),
        face=("If your letter is on this list, the doors that wouldn't open are about to open 🍀 Your reading is waiting in the first comment 🔮\n"
              '#manifestation #2027 #newchapter'),
        fix_insta='The doors are opening for you 🍀 tap my profile picture above, your reading is in my story',
        fix_face='Your next step is waiting right here 🍀 👉 '),
    'nora86': dict(
        insta=("If you're still awake and this found you, it's not by chance 🌙 Your private reading is waiting in my story 🔮\n"
               'Comment ✨ if you felt this message\n#manifestation #angelnumbers #2027 #lawofattraction #archangelmichael'),
        face=("If you're still awake and this found you, it's not by chance 🌙 Your reading is waiting in the first comment 🔮\n"
              '#manifestation #2027 #archangelmichael'),
        fix_insta="If you're still awake, this was meant for you 🌙 tap my profile picture above and check my story",
        fix_face='Read this before the weekend ends ✨ 👉 '),
}
usados = {t['fix_face'] for t in B27.TEXTOS.values()}
assert not usados & {t['fix_face'] for t in TEXTOS.values()}
B27.V.update(NOVOS)
B27.TEXTOS.update(TEXTOS)

# ---------- o multi-ângulo do nora86: 7 imagens, uma a cada 2 takes; os 2 do Face reusam a A (as letras) e a G (o CTA) ----------
LETRA = 'ABCDEFG'
ANG = [None,
       ('a câmera um pouco à esquerda dela e mais perto (dos ombros para cima, um pouco mais aberto)',
        'the camera moves a little to her left and closer, framing her from just below the shoulders up; part of the bookshelf shows behind her'),
       ('a câmera uns 30° à direita, com mais da estante ao fundo',
        'the camera moves about 30 degrees to her right, at the same height; more of the tall wooden bookshelf with books fills the background; the side table '
        'with the statue stays at her left side, partly visible'),
       ('a câmera mais longe e um pouco mais baixa: a poltrona inteira, a mesinha com a estátua inteira e o abajur de chão',
        'the camera moves farther back and a little lower: the whole armchair, the small round side table with the colorful statue of Saint Michael the '
        'Archangel fully visible, the stack of two books and the warm floor lamp are all in the frame'),
       ('a câmera na altura dos olhos, uns 45° à esquerda dela, o abajur atrás do ombro',
        'the camera is at seated eye level, about 45 degrees to her left; the warm floor lamp glows behind her shoulder; she turns her face to the lens'),
       ('de frente e perto, dos ombros para cima, a luz do abajur de um lado do rosto',
        'a close shot from the front, from the shoulders up, a little above her eye level, the warm lamp light on one side of her face; the gold back of the '
        'card shows at the bottom of the frame'),
       ('de frente e bem perto, como uma selfie com o braço esticado (o CTA mais perto, a ideia do Iorhan de 27/11)',
        'the camera comes back to the front and very close, like a selfie held at arm\'s length but with no phone visible, framing her from the shoulders '
        'up, the card in her hand near her collarbone, the bookshelf visible behind her')]


def prompt_angulo(i):
    return ('Generate exactly ONE photorealistic vertical 9:16 image. The attached images are: first, the approved photo of this woman in this scene '
            '(d2811-leitura-IMG-A); second, her character sheet. Keep exactly her face, her warm medium-brown eyes (never green, hazel, gray, blue, amber or '
            'black), her complexion, her long black wavy hair worn loose, her small plain gold stud earrings and her thin gold chain necklace; no paint, no moon, '
            'no stars and no marks on her face. Same woman, the same plain mustard-yellow knit cardigan over the same plain white top, the same reading corner '
            'late at night with the same warm floor lamp light, the same armchair, the same tall wooden bookshelf, the same small round side table with the same '
            'colorful statue of Saint Michael the Archangel and the same stack of two books, and the same framed American flag on its wall (visible only if this '
            'angle shows that wall). She holds the same tarot card upright near her collarbone, a hand\'s width away from her face, showing only its plain gold '
            'patterned back with no text and no picture; she looks straight into the camera with a calm, serious look and her lips closed. Change only the '
            'camera position: ' + ANG[i][1] + '. ' + B27.FIM)


for i in range(1, 7):
    for w in ('chest', 'skin', 'body', 'breast', 'underwear', 'wine', 'powder', 'paint', 'shining', 'glowing', 'sparkling'):
        assert w not in prompt_angulo(i).lower().replace('no paint', ''), (i, w)


def multi(P, n):
    # n = 14 takes do Insta; os 2 do Face no fim (T15 as letras, T16 o CTA do comentário)
    assert n == 14
    imgs = [f'd2811-leitura-IMG-{LETRA[k]}' for k in range(7)]
    img_do_take = [imgs[i // 2] for i in range(n)] + [imgs[0], imgs[6]]
    nomes = [vd['arquivo'] for vd in P['videos']]
    assert len(nomes) == n + 2
    for i, vd in enumerate(P['videos']):
        k = imgs.index(img_do_take[i])
        vd['primeiro_quadro'] = f'IMAGEM {LETRA[k]} ({img_do_take[i]})'
    P['imagens_titulo'] = 'As 7 imagens das falas (o mesmo cantinho e a mesma roupa, um ângulo a cada 2 takes)'
    P['refs'] = [f'{imgs[k]} no T{2 * k + 1:02d} e no T{2 * k + 2:02d}' for k in range(7)] + [f'{imgs[0]} no T15 e {imgs[6]} no T16 (só Face)']
    P['imagens'] = [{'rotulo': f'IMAGEM {LETRA[k]} · {imgs[k]}', 'cena': 'gerada no Muse (seção das imagens)', 'anexar': f'a {imgs[k]}'} for k in range(7)]
    et = P['pre_gancho']['etapas']
    assert len(et) == 1
    et[0]['titulo'] = 'Imagem A (T01 e T02, e o T15 do Face): de frente, a estátua inteira à esquerda dela; no Muse, só com o blueprint'
    for k in range(1, 7):
        et.append({'titulo': f'Imagem {LETRA[k]} (T{2 * k + 1:02d} e T{2 * k + 2:02d}' + (', e o T16 do Face' if k == 6 else '') + f'): {ANG[k][0]}',
                   'nome': imgs[k], 'tipo': 'img', 'anexar': f'a {imgs[0]} (a imagem A) + a nora-v3-blueprint (em 1K)',
                   'quadros': ('1 imagem por vez. Confira contra a imagem A: o mesmo rosto, os olhos CASTANHOS, o cardigã mostarda sobre a blusa branca, a carta '
                               'com o verso dourado, a mesma estante e a mesma estátua (quando o ângulo mostra); 5 dedos em cada mão; nada escrito em lugar nenhum. '
                               f'Salve como {imgs[k]}. Se o rosto ou a roupa mudarem: “Generate it again, exactly the same prompt, one new version.”'),
                   'prompt': prompt_angulo(k)})
    P['pre_gancho']['titulo_secao'] = 'As 7 imagens (no Muse, antes dos takes)'
    P['pre_gancho']['conceito'] = ('O MULTI-ÂNGULO: 7 imagens do mesmo cantinho de leitura, com a mesma roupa (o cardigã mostarda sobre a blusa branca), a carta na mão '
                                   'e a estátua de São Miguel, cada uma de um ângulo. Cada par de takes usa uma (T01 e T02 = A, T03 e T04 = B… T13 e T14 = G); o T15 '
                                   'do Face usa a A e o T16, a G. A A sai só com o blueprint; as outras 6, com a A + o blueprint, para manter o rosto e a roupa.')
    P['pre_gancho']['modo'] = 'Muse, na conversa da Nora: a A só com a nora-v3-blueprint; da B à G, a A + a nora-v3-blueprint. Uma imagem por vez.'
    # as peças e o Resumo
    pc = P['pecas']
    assert pc['lista'][0]['tipo'] == 'imagem das falas'
    pc['lista'] = ([{'nome': imgs[k], 'tipo': 'imagem das falas', 'status': 'gerar', 'onde': 'No Muse (seção das imagens).',
                     'descricao': ('de frente, a estátua inteira à esquerda (o 1º quadro)' if k == 0 else ANG[k][0])} for k in range(7)]
                   + [it for it in pc['lista'] if it['tipo'] != 'imagem das falas'])
    for j, it in enumerate(pc['lista']):
        if it['tipo'] in ('take', 'take do Face'):
            i = nomes.index(it['nome'])
            it['descricao'] = f'{it["descricao"]} · imagem {LETRA[imgs.index(img_do_take[i])]}'
    pc['decisao'] = [d.replace('clipes no Muse, todos com 1 imagem só', 'clipes no Muse, em 7 imagens (uma a cada 2 takes)') for d in pc['decisao']]
    assert any('em 7 imagens' in d for d in pc['decisao'])
    # a Central: a mesma colagem; no Muse, um par de prompts por mensagem, cada par com a sua imagem
    ct = P['central']
    ct['colagens'][0]['titulo'] = ct['colagens'][0]['titulo'].replace('(na d2811-leitura-IMG-A;', '(nas 7 imagens, A a G;')
    ct['conferir'] = ct['conferir'] + ' O ângulo muda a cada 2 takes (A a G), mas o rosto, os olhos castanhos, a roupa e a carta são os mesmos em todos.'
    ag = ct['agente']
    ag['imagem'] = 'a imagem de cada par (A a G)'
    velho = 'using the attached image as the first frame of every clip (never a frame from another clip).'
    assert velho in ag['aviso'], ag['aviso'][:400]
    v2 = 'in order, without asking for my approval between them, '
    assert v2 in ag['aviso']
    ag['aviso'] = ag['aviso'].replace(v2, 'in order, ')
    ag['aviso'] = ag['aviso'].replace(velho, 'each pair of prompts with its own attached image as the first frame of both clips (never a frame from another clip). '
                                      'Generate NOW ONLY Prompt 1 and Prompt 2, using the attached image as the first frame of both; then stop and wait: I will send '
                                      'a new image with each next pair of prompts.')
    def msg(a, b, img):
        quais = f'Prompt {a + 1} and Prompt {b + 1}' if b is not None else f'Prompt {a + 1}'
        nomes_msg = f'Prompt {a + 1} = {nomes[a]}' + (f', Prompt {b + 1} = {nomes[b]}' if b is not None else '')
        return (f'Anexe a {img} e mande: “Now generate {quais} from my first message, exactly as written, using the attached image as the first frame '
                f'{"of both clips" if b is not None else "of the clip"}; each clip says only the words of its own Prompt, once. Name {"them" if b is not None else "it"} '
                f'exactly: {nomes_msg}. Then stop and wait.”')
    passos = [ag['passos'][0],
              (f'Mensagem 1: no Muse, anexe a {imgs[0]} (a imagem A) + o aviso do Muse + o “COPIAR TUDO JUNTO” da Central. O aviso já pede só o T01 e o T02.'),
              'Mensagem 2: ' + msg(2, 3, imgs[1]),
              ('PARE AQUI e me mande o T01 e o T03 (pelo Drive ou aqui no chat): eu meço os olhos e o tom da voz em ~3 min (no nora79, os olhos e a voz mudaram '
               'entre as imagens). Se estiver tudo certo, siga.')]
    for k in range(2, 7):
        passos.append(f'Mensagem {k + 1}: ' + msg(2 * k, 2 * k + 1, imgs[k]))
    passos.append('Mensagem 8 (só Face, as letras): ' + msg(14, None, imgs[0]))
    passos.append('Mensagem 9 (só Face, o CTA do comentário): ' + msg(15, None, imgs[6]))
    passos += ag['passos'][2:]
    ag['passos'] = passos
    ag['intro'] = (f'No Muse, na mesma conversa da Nora (a voz). São 16 clipes em 9 mensagens: a 1ª com a imagem A e o bloco inteiro da Central (ele gera só o T01 '
                   'e o T02), e depois uma mensagem por par, cada uma com a sua imagem. Os 2 últimos são só do Face.')
    return P


if __name__ == '__main__':
    for nn, rot in (('nora85', 'Painel nora85 · o pacote do nora81 com o “free”, na cozinha · 28/11 ~22h15'),
                    ('nora86', 'Painel nora86 · o MULTI-ÂNGULO: o pacote do nora81 em 7 ângulos, no cantinho de leitura · 29/11 ~01h45')):
        P, n, pal = B27.montar(nn)
        if B27.V[nn].get('multi'):
            P = multi(P, n)
        print(nn, n, 'takes,', pal, 'palavras')
        B27.salvar(P, nn, rot)
