# 06/11/2026: nora49 passa do corpo B para o corpo A limpo (o nora48 venceu o teste dos corpos).
# Base: o pacote do nora48 (mesma imagem, LIVRE, movimentação, corpo); troca signos, Take 1, legenda,
# comentários, montagem (a partir do nora48-montado), respostas do Face e o registro.
import json, sys, copy
R = sys.argv[1] if len(sys.argv) > 1 else '.'
def pacote(fn):
    t = open(f'{R}/{fn}', encoding='utf-8').read()
    i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
    return t, i, j, json.loads(t[i:j])
t48, _, _, p48 = pacote('PAINEL-NORA48.html')
t49, i49, j49, p49 = pacote('PAINEL-NORA49.html')
p = copy.deepcopy(p48)
FALA = p49['videos'][0]['fala']  # Take 1 de Áries/Leão/Sagitário, escrito e conferido em 01/11 e no pente fino de 05/11
MOV = p48['videos'][0]['movimentacao']  # movimentação da nora37-IMG (geodo nas duas mãos), sem palavras da fala
ARQ = 'nora49-T01-gancho-portal-aries-leao-sagitario'
r = p['roteiro']
r['id'] = 'nora49-CORPO-A-LIMPO-TAKE1-ARIES-LEAO-SAGITARIO'
r['titulo'] = 'Gancho do tsunami (espelhado) + Take 1 de Áries, Leão e Sagitário no quarto à noite + corpo A limpo (o mesmo do nora48)'
r['formato'] = 'Hook do tsunami do nora47, ESPELHADO (pronto) + Take 1 NOVO na nora37-IMG (Áries, Leão e Sagitário) + os 7 takes do corpo A limpo, tirados do nora48-montado (~80 s)'
r['molde_hook'] = 'O que venceu o teste dos corpos em 06/11: o nora48 (tsunami + corpo A limpo) fez 1.404 views, 71% nos 3 s, 20 s, 9 follows e 3 visitas ao perfil com ~10h35 no Insta, contra 287, 59%, 12 s e 0 do nora47 (corpo B). Agora é repetir o que funcionou trocando os signos (Take 1 novo) e espelhando o gancho.'
r['descricao_instagram'] = 'Aries, Leo, Sagittarius: if you know something has to change, but not how, listen before 11/11, the most powerful portal of the year. 🔮\nThe worst is finally over. Your private reading is waiting in my story.\n#manifestation #1111portal #aries #leo #sagittarius'
r['leitura_registro'] = ('06/11/2026 ~12h15 (aprovação do aluno para trocar o nora49 do corpo B para o corpo A; leitura PARCIAL, registro honesto): '
  'li o CLAUDE.md e as regras P1 a P45 (no início desta sessão, e o estado e as regras em vigor reescritos hoje), os pacotes inteiros dos painéis do nora48 e do nora49, '
  'as lições do Flow das partes de agente e modo Frames, as métricas do nora48 e do nora47 (Insta e Face) e a spec da edição do nora48. '
  'Não li hoje a lista inteira do LEIA-TUDO-ANTES.md. Não há fala nova: o Take 1 é o do nora49, escrito e conferido em 01/11 e no pente fino de 05/11; '
  'a movimentação e o texto LIVRE são os do nora48 (mesma imagem, nora37-IMG); a montagem reaproveita o nora48-montado.')
p['refs'] = ['Folha de consistência da Nora (blueprint)', 'nora37-IMG (o Take 1; já aprovada)', 'nora48-montado (o vídeo sem texto do nora48: o hook e o corpo A limpo)']
v = p['videos'][0]
v['rotulo'] = 'T01 · nora49'
v['cena'] = 'Take 1 do nora49 · Gancho no quarto à noite: Áries, Leão e Sagitário + o portal 11:11'
v['fala'] = FALA; v['movimentacao'] = MOV; v['arquivo'] = ARQ
p['texto_tela']['hook'] = 'ARIES, LEO, SAGITTARIUS\n11:11, the most powerful portal\nthe worst is finally over'
p['comentario_fixado'] = {
  'insta': 'Aries, Leo, Sagittarius: love, money or peace, what are you ready to receive first? ✨ Tell me below, then tap my photo and open my story before the 11:11 portal: your private reading starts there. 🔮',
  'face': 'Aries, Leo, Sagittarius: love, money or peace, what are you ready to receive first? ✨ Your private reading is right here, open it before the 11:11 portal 🔮 👉 https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'}
g = p['pre_gancho']
g['titulo_secao'] = 'Hook: o tsunami do nora47, ESPELHADO (já pronto, 0 crédito)'
g['conceito'] = 'O mesmo gancho do nora48 (o tsunami), ESPELHADO, já pronto: 0 crédito. O nora48 com esse gancho e o corpo A limpo fez 1.404 views, 71% nos 3 s e 9 follows com ~10h35 no Insta. Espelhado, o quadro não fica igual ao do nora48.'
g['modo'] = 'Não gere nada aqui. No CapCut, espelhe só o trecho do hook (Editar → Espelhar).'
g['montagem'] = '1) Projeto novo no CapCut com o nora48-montado (o vídeo SEM texto do nora48).\n2) Divida no fim do hook (~7,9 s, quando entra o quarto) e espelhe só o hook (Editar → Espelhar).\n3) Divida também no começo do Take 2 ("Don\'t tell anyone", ~16,6 s), apague o Take 1 do nora48 e encoste o nora49-T01-cortado no lugar.\n4) No hook fica só o som da onda.'
c = p['central']
c['conferir'] = 'Conferir no Take 1: é a Nora (rosto, lua com as estrelinhas, trança, blusa preta), no quarto à noite com o abajur rosa, segurando as duas metades do geodo; fala uma vez só, em inglês, com os signos certos (Aries, Leo or Sagittarius), e termina em "eleven eleven, the year\'s most powerful portal"; as metades não fecham nem trocam de mão; sem texto, legenda ou música.'
c['passos'] = [
  'Story: o story-0311 repostado ontem às 18h23 vence hoje ~18h23. Reposte antes do nora49 (~16h50), com a mesma imagem, o mesmo texto e o adesivo com o link certo de cada rede.',
  'Take 1 na Central com a MESMA configuração do nora48 (o texto LIVRE do quarto à noite, nesta seção). Cole só a fala e a linha de movimentação do Take 1. Gere: 1 take de 10 s.',
  'Agente do Flow: conversa nova, anexe só a nora37-IMG, cole o aviso de 1 prompt e, embaixo, o prompt do take. 15 créditos. Renomeie para ' + ARQ + '. Use o Omni 1.1 Flash (o 1.2 cobra o dobro).',
  'Corte de silêncio só do nora49-T01 (nora49-T01-cortado).',
  'CapCut: projeto novo com o nora48-montado. Espelhe só o hook (0 a ~7,9 s). Divida no começo do Take 1 e no começo do Take 2 ("Don\'t tell anyone", ~16,6 s), apague o Take 1 do nora48 e ponha o nora49-T01-cortado no lugar. Música −18 dB só no Take 1 novo (o resto já tem). Exporte SEM texto como nora49-montado e me mande aqui (se passar de 30 MB, link do Drive).',
  'Eu devolvo o nora49-final (caixa do topo com os signos, números, legenda, faixa do story e seta). Confira no celular e poste hoje (06/11) às 17h no Insta e no Face, ao vivo. Comentário: no Insta, comente e fixe (sem link); no Face, comente COMO A PÁGINA (já tem o link).']
c['agente']['passos'] = [x.replace('nora48-T01-gancho-portal-cancer-escorpiao-peixes', ARQ) for x in p48['central']['agente']['passos']]
c['colagens'][0]['titulo'] = 'só o Take 1 do nora49'
c['colagens'][0]['fala'] = FALA; c['colagens'][0]['movimentacao'] = [MOV]
p['story']['nota'] = 'REPOSTE O STORY ~16h50, antes do nora49 das 17h (o repost de ontem foi às 18h23 e vence hoje ~18h23): a mesma imagem (story-3110), o mesmo texto e o adesivo com o link certo de cada rede; confira na prévia. Insta (STORYIG): https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks · Face (FACE): https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
mt = p['mapa_tela']
mt['numeros'][0].update({'y': 10.5, 'tamanho': 15})
mt['numeros'][2].update({'y': 46.9, 'onde': 'à esquerda, na altura do ombro, sobre o cabelo'})
mt['estilos'][0]['obs'] = 'Os mesmos do nora48 (já ajustados na edição dele): 11:11 branco, 15, X -230 · Y 506; 888 ciano, 12, X 230 · Y 256; 222 amarelo-ouro, 11, X -230 · Y 40. Do 1º quadro do hook ao fim. Eu ponho (P45).'
mt['estilos'][1]['nome'] = 'Caixa do topo: “ARIES, LEO, SAGITTARIUS” / “11:11, the most powerful portal” / “the worst is finally over”'
mt['estilos'][2]['obs'] = mt['estilos'][2]['obs'].replace('Cancer, Scorpio, Pisces', 'Aries, Leo, Sagittarius')
mt['regras'][1] = 'Os números ficam onde ficaram no nora48 (o 11:11 acima da caixa do topo; o 222 fora da mão e do geodo).'
p['edicao_linha'] = [
  {'quando': 'A. Antes de tudo', 'texto': 'Projeto novo no CapCut com o nora48-montado (sem texto)', 'como': 'É o vídeo que você me mandou pelo Drive para o nora48 (o hook do tsunami, o Take 1 do nora48 e o corpo A limpo).'},
  {'quando': '0. No começo', 'texto': 'Hook do tsunami ESPELHADO', 'como': 'Divida no fim do hook (~7,9 s, quando entra o quarto) e espelhe só esse trecho (Editar → Espelhar). Só o som da onda.'},
  {'quando': '1. Trocar o Take 1', 'texto': 'nora49-T01-cortado no lugar do Take 1 do nora48', 'como': 'Divida também no começo do Take 2 ("Don\'t tell anyone", ~16,6 s), apague o Take 1 do nora48 e encoste o nora49-T01-cortado. Ouça a emenda: termina em "before eleven eleven, the year\'s most powerful portal".'},
  {'quando': '2. Só no Take 1 novo', 'texto': 'Música de sempre ("Ambient Mystical Drone"), −18 dB', 'como': 'O resto do vídeo já tem a música do nora48.'},
  {'quando': '3. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code', 'como': '720×1280 ou 1080×1920, qualidade alta, nome nora49-montado (se passar de 30 MB, link do Drive). Eu ponho a caixa do topo, os números, a legenda, a faixa do story e a seta e devolvo o nora49-final.'}]
p['pecas']['lista'] = [
  {'nome': 'nora47-PRE-A e nora47-PRE-B (no nora48-montado)', 'de': 'nora47', 'tipo': 'hook (pronto)', 'status': 'reutilizar', 'descricao': 'O tsunami, ESPELHADO no CapCut.'},
  {'nome': 'nora37-IMG', 'de': 'nora37-IMG', 'tipo': 'imagem 1', 'status': 'reutilizar', 'descricao': 'Quarto à noite, abajur rosa, blusa preta canelada, as duas metades do geodo nas mãos (a imagem do Take 1 e do corpo do nora48).'},
  {'nome': ARQ, 'tipo': 'take', 'status': 'gerar', 'creditos': 15, 'descricao': '“' + FALA + '”'},
  {'nome': 'nora48-T02 a nora48-T08 (o corpo A limpo)', 'de': 'nora48', 'tipo': 'corpo', 'status': 'reutilizar', 'descricao': 'O corpo do nora48 a partir do Take 2, SEM texto, como está no nora48-montado. Não gere, não corte e não junte de novo.', 'onde': 'No nora48-montado (o vídeo sem texto do nora48), a partir do Take 2.'},
  {'nome': 'story-0311 (repost)', 'de': 'story-3110', 'tipo': 'story', 'status': 'reutilizar', 'descricao': 'Repostar ~16h50 (vence ~18h23): mesma imagem, texto e adesivo.'}]
p['pecas']['decisao'] = [
  'O teste dos corpos acabou: com o mesmo gancho e quase o mesmo horário, o nora48 (corpo A limpo) fez 1.404 views, 71% nos 3 s, 20 s, 9 follows, 3 visitas e 25 comentários de outras pessoas no Insta com ~10h35; o nora47 (corpo B) fez 287, 59%, 12 s e 0. No Face, 167 x 103 views.',
  'Agora é repetir o que funcionou: o mesmo corpo, o mesmo gancho espelhado e um Take 1 novo com outros signos (no Insta, cada post leva um Take 1 novo).',
  'Total: 15 créditos (só o Take 1).']
p['silencio'] = p49['silencio']
p['respostas_face'] = p49['respostas_face']
novo = t49[:i49] + json.dumps(p, ensure_ascii=False) + t49[j49:]
open(f'{R}/PAINEL-NORA49.html', 'w', encoding='utf-8').write(novo)
print('ok', len(novo))
