# 29/10/2026: falas e movimentação do longo do corpo A (nora40) e dos Takes 1 de nora42 e nora43.
# Checa palavras por take, simulação do divisor da Central (22 a 25 palavras) e sobreposição fala x movimentação.
import re

SIGNOS = {
    'nora40': ('Aries, Leo or Sagittarius', 'Aries, Leo, Sagittarius', 'aries-leao-sagitario'),
    'nora42': ('Gemini, Libra or Aquarius', 'Gemini, Libra, Aquarius', 'gemeos-libra-aquario'),
    'nora43': ('Taurus, Virgo or Capricorn', 'Taurus, Virgo, Capricorn', 'touro-virgem-capricornio'),
}
def t01(v):
    return SIGNOS[v][0] + ': keep your mouth shut if this video showed up for you on October 29th, 30th or 31st.'

CORPO = [  # (sufixo do arquivo, cena, fala, chave da expressão) dos takes 2 a 11 (corpo A dos virais x1 a x5, w3 a w5, L1, a4/a5).
    # 29/10 ~12h (pedido do aluno): o Take 2 pede seguir, 222 e enviar logo no começo ("claim this energy" dos virais curtos:
    # R03/R05, R11 e os reels de manifestação da seção 39), porque quase todo mundo sai antes dos selos do fim; os selos do fim continuam.
    ('T02-cta-claim-seguir-222-enviar', 'Pedido no começo: seguir, 222 e mandar para si',
     "Before you scroll, claim this energy: make sure you're following me, comment 222 and send this video to yourself.", 'CLAIM'),
    ('T03-corpo-segredo-fe', 'Segredo + “the universe saw your faith”',
     "Don't tell anyone what's about to happen. I don't know your name or what you did, but the universe saw your faith.", 'T02'),
    ('T04-corpo-virada-incomum', 'A virada nos próximos dias',
     'A major turnaround is coming your way over the next few days. I see something very unusual happening in your life.', 'T03'),
    ('T05-corpo-dinheiro-prosperidade', 'Dinheiro, prosperidade e alguém maravilhoso',
     "There's money, prosperity and someone incredibly wonderful about to show up unexpectedly. The universe chose you for this.", 'T04'),
    ('T06-corpo-bencaos-ameaca', 'Se virar as costas (a única ameaça)',
     'But if you turn your back on this message, the blessings will turn their backs on you too. So take this seriously.', 'T05'),
    ('T07-corpo-sao-miguel', 'São Miguel: o pior passou',
     'Archangel Michael has sent a warning. A phase of victory and prosperity is approaching your life. The worst is finally over.', 'T06'),
    ('T08-corpo-correntes', 'As correntes da escassez',
     'I can already see the chains keeping you trapped in scarcity being broken. Closed financial doors are starting to open.', 'T07'),
    ('T09-corpo-sete-minutos', 'Os 7 minutos',
     'In the next seven minutes, the energy of scarcity that was following you is going to be destroyed forever.', 'T08'),
    ('T10-corpo-mande-para-si', 'Mande para você mesma',
     "So send this video to yourself right now, because in seven minutes you're going to come back and confirm the shift.", 'T09'),
    ('T11-cta-selos-seguir', 'Os 2 selos: salvar e seguir',
     'Now save this video, that will be your first seal. Tap the follow button down below, that will be your second seal.', 'T10'),
]
T11_FALA = 'Comment 222 to claim this energy, then tap my profile picture. The second part of this sign is waiting in my stories.'

ABRE = ('Throughout the whole 10 seconds both of her hands keep holding the two open halves of the gray geode at the height of her collarbones '
        'with their pink crystal insides facing the lens, her right hand on the left side of the frame holding the left half and her left hand '
        'on the right side of the frame holding the right half with the small gold symbol, and the halves never change hands, never close, never '
        'turn away, never drop and never cover her face, both hands stay on the halves with no other gestures, ')
FECHA = (', and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; everything else in '
         'the scene stays completely still and each hand has exactly five fingers.')
EXPR = {  # só rosto, cabeça e olhos (as mãos estão no geodo); nada da fala (P32), de acordo com o sentido (Bruno Freitas)
    'CLAIM': 'her eyes stay on the lens, and during the first half of the take her eyebrows lift with an urgent, inviting look and she leans her head slightly toward the lens, during the second half she gives two small quick nods with a warm smile',
    'T01': 'her eyes stay on the lens, and during the first half of the take she holds a firm, serious look with her brows slightly lowered, during the second half she gives one short slow nod',
    'T02': 'her eyes stay on the lens, and during the first sentence of the take she leans her head a little toward the lens with a secretive look and her eyes narrow slightly, during the last sentence her face softens into a warm half-smile and she gives one small nod',
    'T03': 'her eyes stay on the lens, and during the first sentence of the take her eyebrows lift slightly with a hopeful look, during the last sentence she tilts her head a little to one side and her eyes widen slightly with quiet amazement',
    'T04': 'her eyes stay on the lens, and during the first sentence of the take a bright, warm smile grows on her face, during the last sentence she gives one slow, firm nod with a proud, knowing look',
    'T05': 'her eyes stay on the lens, and during the first sentence of the take her smile fades and her brows draw together in a serious, warning look, during the last sentence she slowly shakes her head once with a stern look',
    'T06': 'her eyes stay on the lens, and during the first sentence of the take she holds a solemn, intense look with her eyes wide open, during the middle sentence her chin lifts slightly with a confident look, during the last sentence she lets out one slow breath, her shoulders drop and a relieved soft smile appears',
    'T07': 'her eyes stay on the lens, and during the first sentence of the take her eyes narrow slightly with an intense, focused look, during the last sentence her eyebrows rise and her face opens into a hopeful smile',
    'T08': 'her eyes stay on the lens, and during the first half of the take she leans her head slightly toward the lens with a very serious, intense look, during the second half she gives one firm, decisive nod',
    'T09': 'her eyes stay on the lens, and during the first half of the take her eyebrows lift with an urgent, encouraging look, during the second half a small confident smile appears and she gives one short nod',
    'T10': 'her eyes stay on the lens except for one quick glance, and during the first sentence of the take she gives one short nod with a warm smile, during the last sentence her eyes glance down toward the bottom of the frame for one moment and come back to the lens with a warm smile',
}
def mov(k): return ABRE + EXPR[k] + FECHA

def takes(v):
    # lista de (arquivo, cena, fala, movimentacao) dos takes gerados do nora40 (10) ou do Take 1 (nora42, nora43)
    T = [(f'{v}-T01-gancho-{SIGNOS[v][2]}', 'Gancho (signos, segredo e datas)', t01(v), mov('T01'))]
    if v == 'nora40':
        for suf, cena, fala, ex in CORPO:
            T.append((f'nora40-{suf}', cena, fala, mov(ex)))
    return T

wc = lambda s: len(s.split())
COMUNS = {'and it','of the','in the','on the','to the','the end','the lens','of her','her head','the take','the first','the last','she gives',
          'one short','her eyes','for one','the open','a soft','and her','at the','her face','her first','the clip','she keeps','the second',
          'and the','with the','the left','the right','is the','for the'}
def bigr(t):
    w = re.findall(r"[a-z0-9:%']+", t.lower()); return {' '.join(w[i:i+2]) for i in range(len(w)-1)}

def checar(T):
    F = [t[2] for t in T]
    for t in T:
        n = wc(t[2]); assert 18 <= n <= 22, (t[0], n)
        ov = (bigr(t[2]) & bigr(t[3])) - COMUNS
        assert not ov, ('SOBREPOSICAO', t[0], ov)
    full = ' '.join(F); sents = [s.strip() for s in re.findall(r'[^.!?]+[.!?]', full)]
    for L in (22, 23, 24, 25):
        tk, cur = [], []
        for s in sents:
            if cur and wc(' '.join(cur + [s])) > L: tk.append(' '.join(cur)); cur = [s]
            else: cur.append(s)
        tk.append(' '.join(cur))
        assert tk == F, ('DIVISOR', L, tk)
    return True

if __name__ == '__main__':
    for v in SIGNOS:
        T = takes(v); checar(T)
        for t in T: print(v, wc(t[2]), t[0], '|', t[2])
    # o T11 (cópia do nora37-T03) não passa pela Central; o corpo + T11 também não pode ter sobreposição com nada
    print('ok')
