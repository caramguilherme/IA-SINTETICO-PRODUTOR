# Painéis do dia 20/11/2026 ("pode montar o 73 e o 74", ~17h40).
# nora73 (Insta 19h30; Face 0h00 de 21/11): o nora72 inteiro (a canela no carro + a fala dos 3 sinais) com UMA frase nova na frente,
#   as letras do nome ("If your name starts with the letter A, J, M, K, C, E, S, L, R, T or H, pay close attention."). 1 take no Muse.
#   Fontes: o viral 52.2 (16/11), o v4 da @takedanaomi_ (20/11, a mesma frase) e o ini1811 (o único post que levou gente ao perfil).
# nora74 (Insta 0h00; só no Insta): o campeão de volta (o nora48 a nora50), feito do zero no Muse. Ver build_nora74 abaixo.
# Uso (raiz do repositório): python3 -I ferramentas-painel/dia-2011/build_dia_2011.py
import sys, json, copy, re, pathlib, importlib.util

R = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('b1911', R / 'ferramentas-painel' / 'dia-1911' / 'build_dia_1911.py')
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
MODELO = B.MODELO
FB = B.FB

# ------------------------------------------------------------------ nora73
C = dict(B.CARRO); C.update(nn='nora73', d='d2011')
FALA73 = 'If your name starts with the letter A, J, M, K, C, E, S, L, R, T or H, pay close attention.'
assert len(FALA73.split()) <= 22, len(FALA73.split())
NOME73 = 'd2011-carro-T00-letras'
MOV73 = (f'Throughout the whole 10 seconds {C["cam"]}; {C["segura"]}; with her other hand she raises it beside her shoulder and taps her thumb against each '
         'fingertip in turn as if counting, then points at the lens, with a curious, knowing look; her eyes stay on the lens; from the end of the final sentence '
         'of the take until the clip ends she keeps her lips closed and silent; no zoom and no cuts, the braid stays in place and each hand has exactly five fingers.')
fw = re.findall(r"[a-z']+", FALA73.lower()); mw = re.findall(r"[a-z']+", MOV73.lower())
assert not ((set(zip(fw, fw[1:])) & set(zip(mw, mw[1:]))) - B.COMUNS), 'a movimentação repete palavras da fala'
PROMPT73 = B.prompt_manual(C, FALA73, MOV73)
NORA72_DRIVE = 'https://drive.google.com/file/d/1-pAb4VN_F6kT5b-yVYJckpfMt1dVu1-s/view?usp=sharing'


def nora73():
    P = copy.deepcopy(B.pacote('PAINEL-NORA72.html'))
    P['roteiro'].update({
        'id': 'nora73-CARRO-LETRAS-2011',
        'titulo': 'nora73 · Insta às 19h30 de hoje (20/11) · o nora72 com as letras do nome na frente',
        'duracao_total': 57,
        'descricao_instagram': ('If your name starts with one of these letters, this is for you 👀 Your private reading is waiting in my story 🔮\n'
                                'Comment the first letter of your name 👇\n'
                                '#manifestation #angelnumbers #messagefromtheuniverse #2027 #lawofattraction'),
        'descricao_face': ('If your name starts with one of these letters ✨ Most people never notice these 3 signs. Your reading is waiting in my story and in the comments 🔮\n'
                           '#manifestation #1111 #messagefromtheuniverse #2027'),
    })
    P['videos'] = [{'rotulo': 'T00', 'cena': 'as letras do nome (entra antes do T01 do nora72)', 'duracao': 10,
                    'primeiro_quadro': 'IMAGEM 1 (d1711-PRE-carro-IMG-C)', 'acao': '', 'b_roll': '', 'fala': FALA73, 'movimentacao': MOV73, 'arquivo': NOME73}]
    P['texto_tela'] = {'hook': 'If your name starts with\n[one of these letters]', 'hook_comeca': 'o 1º quadro do hook', 'hook_termina': 'o fim da frase das letras',
                       'hook_alt': '', 'extras': []}
    P['comentario_fixado'] = {'insta': 'If your initial is one of them ✨ tap my profile picture above, your 2027 reading is waiting in my story',
                              'face': 'Your reading for 2027 is right here ✨ 👉 ' + FB}
    P['story'] = {'ja_postado': True,
                  'nota': 'Antes de postar, confira se o story repostado hoje (o adesivo “TAP TO CONTINUE 🎁”, com o link STORYIG) está no ar no Insta e no Face.'}
    ct = P['central']
    ct['config'] = []
    ct['colagens'] = [{'titulo': 'nora73: 1 take só (no Muse, sem a Central)', 'fala': FALA73, 'movimentacao': [MOV73], 'takes': [0]}]
    ct['conferir'] = ('Conferir o take: é a Nora da imagem C (rosto, lua com as 3 estrelinhas, trança, brincos, colar de Vênus), no carro, a mão no volante, o cinto e a '
                      'rua passando; ela diz as 11 letras uma vez só, em inglês, e fecha a boca no fim. Renomeie para ' + NOME73 + '.')
    ct['agente'] = {
        'imagem': 'd1711-PRE-carro-IMG-C',
        'intro': 'Não precisa da Central hoje: é 1 take só. No Muse, na conversa da Nora, anexe a d1711-PRE-carro-IMG-C e cole o prompt abaixo.',
        'aviso_tag': 'cole no Muse, com a d1711-PRE-carro-IMG-C anexada',
        'aviso': PROMPT73,
        'passos': [
            'No Muse, na conversa da Nora: anexe a d1711-PRE-carro-IMG-C (a mesma do nora72) e cole o prompt acima, numa mensagem só. ~1 min.',
            f'Renomeie o clipe para {NOME73}.',
            'Confira se ela diz as 11 letras (A, J, M, K, C, E, S, L, R, T, H) uma vez só e fecha a boca no fim. Se o Muse recusar: “Generate it again, exactly as '
            'written.” Se errar uma letra, gere de novo.',
        ],
    }
    P['edicao_linha'] = [
        {'quando': 'A. O montado do nora72', 'texto': 'Baixe o NORA72.mp4 do seu Drive (o montado que você me mandou)', 'como': NORA72_DRIVE},
        {'quando': 'B. Projeto novo no CapCut', 'texto': f'1º o {NOME73}, logo depois o NORA72.mp4', 'como': 'Sem FusionZ: eu corto os silêncios do take novo aqui.'},
        {'quando': 'C. O hook: NÃO põe no CapCut', 'texto': 'O hook da canela já está comigo', 'como': 'Eu emendo o hook e o flash branco antes do take novo.'},
        {'quando': 'D. Música', 'texto': 'A de sempre (“Ambient Mystical Drone”), −18 dB, só embaixo do take novo', 'como': 'O NORA72.mp4 já tem a música dele.'},
        {'quando': 'E. Exportar e me mandar (até ~19h10)', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code',
         'como': '1080×1920, nome nora73-montado (acima de 30 MB, link do Drive). Se for mais rápido, me mande só o take novo, que eu emendo aqui (ele fica sem música embaixo, ~8 s). Eu devolvo o nora73-final (Insta, 19h30) e o nora73-final-FACE (Face, 0h00).'},
    ]
    P['pecas'] = {
        'titulo_decisao': 'Resumo',
        'lista': [
            {'nome': 'd1711-PRE-carro-IMG-C', 'tipo': 'imagem', 'status': 'reutilizar', 'onde': 'A mesma do nora72. Anexe ela no Muse.', 'descricao': 'A mesma do nora72.'},
            {'nome': 'hook da canela no carro', 'tipo': 'hook', 'status': 'reutilizar', 'onde': 'Já está comigo.', 'descricao': 'Eu emendo antes do take novo.'},
            {'nome': NOME73, 'tipo': 'take', 'status': 'gerar', 'descricao': f'“{FALA73}”'},
            {'nome': 'NORA72.mp4 (o montado do nora72)', 'tipo': 'corpo', 'status': 'reutilizar', 'onde': 'No seu Drive.', 'descricao': 'Os 6 takes do nora72, como estão.'},
        ],
        'decisao': [
            '1 take no Muse: a frase das letras do nome na frente do nora72 inteiro. Só a abertura muda.',
            'Insta às 19h30 de hoje (o montado até ~19h10). Face à 0h00 (21/11), com a variação do Face; nada no Face às 19h30 (o nora72-FACE foi hoje à 01h16).',
            'Hipótese: a abertura pelas iniciais (o único post que levou gente ao perfil foi o curto das iniciais: 21 visitas) leva gente ao perfil também no falado.',
            'O story vence às ~18h15: reposte antes, no Insta e no Face.',
        ],
    }
    P['ordem'] = ['pecas', 'agente', 'cenas', 'textotela', 'story', 'descricao', 'comentario', 'respostasface']
    return P


def salvar(P, nn, rotulo):
    html = MODELO.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(P, ensure_ascii=False) + ';')
    html = re.sub(r'<title>[^<]*</title>', '<title>' + rotulo + '</title>', html, count=1)
    (R / f'PAINEL-{nn.upper()}.html').write_text(html, encoding='utf-8')
    print('ok', nn, len(html), 'bytes')


if __name__ == '__main__':
    salvar(nora73(), 'nora73', 'Painel nora73 · letras do nome · 20/11')
