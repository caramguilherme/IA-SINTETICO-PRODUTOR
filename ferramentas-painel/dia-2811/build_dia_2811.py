# Painéis do dia 28/11/2026: nora85 (20h30) e nora86 (0h00 de 29/11), Insta e Face. O nora84 (17h) saiu do build_dia_2711.py.
# A decisão do aluno (28/11 ~12h, "Pode montar" / "Sim"): o pacote do nora81 ganhou de novo (o nora81 fez 1.398 e o nora83, 505 com ~9 h; regra 13.3c)
#   e vira a base dos 3 vídeos do Insta; o "free" no CTA do Insta é o teste do dia, nos 3 (PENDENCIAS, item 5). Cada um com outra roupa e outro cômodo
#   (a regra de 24/11). O teste do CTA mais cedo (FILA, 28/11 ~10h40) fica para 29/11.
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
TESTE = ('O QUE ESTE VÍDEO TESTA: o “free” no CTA do Insta (o T13: “a quick, free reading in my stories”), o teste do dia nos 3 vídeos de hoje (o nora84, '
         'o nora85 e o nora86). O resto é o pacote do nora81, que ganhou 2 vezes (1.398 e 505 com ~9 h; regra 13.3c), com outra roupa e outro cômodo. '
         'No Face o CTA fica sem o “free”. A medida do “free” é o clique, o checkout e a venda por clique no Tracker; a do vídeo, com ~3 h, os compartilhamentos '
         'e os salvos (o que tira um vídeo dos ~125) e a fatia dos EUA.')
STORY_OK = ('O story no ar é o de 01h35 de 28/11 (Insta e Face): vence ~01h35 de 29/11. Não precisa postar story agora. Antes de abrir o Insta, '
            'confira o IP e os EUA no mylocation.org.')

NOVOS = {
    'nora85': dict(
        dia='d2811', hora='20h30 de 28/11', prazo='até ~20h00 de 28/11', pref='cozinha', img='d2811-cozinha-IMG',
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
        fix_muse=True, data='Monday, November thirtieth', free=True, teste_txt=TESTE, story=STORY_OK),
    'nora86': dict(
        dia='d2811', hora='0h00 de 29/11', prazo='até ~23h30 de 28/11', pref='leitura', img='d2811-leitura-IMG',
        roupa_pt='cardigã mostarda sobre uma blusa branca lisa', obj_pt='uma carta (o verso dourado) na mão',
        lugar_pt='na poltrona do cantinho de leitura, tarde da noite, com a estante de livros atrás e a estátua de São Miguel na mesinha',
        roupa='her plain mustard-yellow knit cardigan over a plain white top, with no logo',
        cena=('Casual real video late at night in the reading corner of a cozy American home, she sits in a soft armchair with a tall wooden bookshelf behind her '
              'on the right; on a small round side table beside her a colorful statue of Saint Michael the Archangel and a stack of two books (the statue at her '
              'left side, fully visible in the frame); ' + FP + ', filmed from a static camera about one meter in front of her at collarbone height, looking '
              'exactly like a real phone video, warm floor lamp light. '),
        cam='the camera stays static about one meter in front of her at collarbone height with an unchanged framing',
        segura=SEGURA + 'on the armrest of the armchair',
        objeto='the tarot card with its plain gold back in her hand, the armchair, the side table with the statue and the books, the bookshelf and the framed flag',
        som='quiet room sound at night', lugar_en='in the armchair of her reading corner', luz='warm floor lamp light at night',
        prompt_img=_img('she sits in a soft armchair in the reading corner of her real American home late at night, a tall wooden bookshelf with books behind her '
                        'on the right, warm floor lamp light',
                        'a plain mustard-yellow knit cardigan over a plain white top, with no logo',
                        'on a small round side table beside her, ' + STATUE + ', and a stack of two books',
                        'on the armrest of the armchair', 'late at night'),
        copia='o pacote do nora81 (as letras, a carta na mão, a estátua de São Miguel, as 2 frases de reinício), no cantinho de leitura',
        fix_muse=True, data='Monday, November thirtieth', free=True, teste_txt=TESTE,
        story=('ANTES do nora86, à 0h00: reposte o story no Insta e no Face, com o adesivo de link de sempre (STORYIG no Insta, FACE no Face). O de 01h35 de 28/11 '
               'vence ~01h35 de 29/11; repostando junto com o nora86, ele fica no ar até a 0h00 de 30/11. Antes de abrir o Insta, confira o IP e os EUA no mylocation.org.')),
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

if __name__ == '__main__':
    for nn, rot in (('nora85', 'Painel nora85 · o pacote do nora81 com o “free”, na cozinha · 28/11 20h30'),
                    ('nora86', 'Painel nora86 · o pacote do nora81 com o “free”, no cantinho de leitura · 29/11 0h00')):
        P, n, pal = B27.montar(nn)
        print(nn, n, 'takes,', pal, 'palavras')
        B27.salvar(P, nn, rot)
