# 07/11/2026: painel do nora50 = teste do gancho do nicho (pedra escura, nora34-PRE) contra o tsunami (nora49),
# mesmo Take 1 no mesmo molde (signos de ar), mesmo corpo A limpo, mesmo horário (19h30).
# Base: o pacote do nora49. Uso: python3 -I ferramentas-painel/r0711/patch_nora50.py  (na raiz do repositório)
import json, copy, sys
R = sys.argv[1] if len(sys.argv) > 1 else '.'
t = open(f'{R}/PAINEL-NORA49.html', encoding='utf-8').read()
i = t.index('const PACOTE = ') + len('const PACOTE = '); j = t.index(';\n', i)
p = json.loads(t[i:j])
FB = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=facebook&utm_content=FACE&aff=dl7zx6ks'
IG = 'https://app.auralyapp.com/6a90ad82719e8d2b35da8a7c?rt_ad=norakensleytarot&utm_source=instagram&utm_content=STORYIG&aff=dl7zx6ks'
FALA_OLD = "Aries, Leo or Sagittarius: if you know something has to change, but not how, listen before 11:11, the year's most powerful portal."
FALA = "Gemini, Libra or Aquarius: if your mind won't stop asking what comes next, listen before 11:11, the year's most powerful portal."
assert len(FALA.split()) == 21
ARQ = 'nora50-T01-gancho-portal-gemeos-libra-aquario'
# troca geral de signos e de número (depois os campos do teste são reescritos um por um)
s = json.dumps(p, ensure_ascii=False)
for a, b in [(FALA_OLD, FALA), ('ARIES, LEO, SAGITTARIUS', 'GEMINI, LIBRA, AQUARIUS'), ('Aries, Leo, Sagittarius', 'Gemini, Libra, Aquarius'),
             ('Aries, Leo or Sagittarius', 'Gemini, Libra or Aquarius'), ('Áries, Leão e Sagitário', 'Gêmeos, Libra e Aquário'),
             ('aries-leao-sagitario', 'gemeos-libra-aquario'), ('#aries #leo #sagittarius', '#gemini #libra #aquarius'),
             ('ARIES-LEAO-SAGITARIO', 'GEMEOS-LIBRA-AQUARIO'), ('“Aries”', '“Gemini”'), ('Aries, Leo, Sagittarius', 'Gemini, Libra, Aquarius'),
             ('nora49', 'nora50')]:
    s = s.replace(a, b)
p = json.loads(s)
r = p['roteiro']
r['id'] = 'nora50-HOOK-PEDRA-TAKE1-GEMEOS-LIBRA-AQUARIO'
r['titulo'] = 'Gancho da pedra escura que racha (do nicho) + Take 1 de Gêmeos, Libra e Aquário no quarto à noite + corpo A limpo (o mesmo do nora48 e do nora49)'
r['dor'] = 'a cabeça que não para de perguntar o que vem depois; o desejo de clareza, dinheiro, amor e paz (ângulo positivo, P42)'
r['formato'] = 'Hook nora34-PRE (a pedra escura que racha e mostra o quartzo rosa; pronto, 0 crédito) + Take 1 NOVO na nora37-IMG (Gêmeos, Libra e Aquário) + os 7 takes do corpo A limpo, tirados do nora48-montado (~64 s)'
r['molde_hook'] = ('Teste de uma variável: o gancho. O nora49 (tsunami + corpo A, 19h31) levou 5,5 pessoas ao perfil a cada 1.000 views no Insta; '
                   'o nora43 (esta mesma pedra + corpo A antigo, à 01h15) levou ~10. Mesmo corpo, mesmo molde de Take 1 e mesmo horário do nora49 (19h30): '
                   'só o gancho muda.')
r['duracao_total'] = 64
r['descricao_instagram'] = ("Gemini, Libra, Aquarius: if your mind won't stop asking what comes next, listen before 11/11, the most powerful portal of the year. 🔮\n"
                            "The worst is finally over. Your private reading is waiting in my story.\n#manifestation #1111portal #gemini #libra #aquarius")
r['leitura_registro'] = ('07/11/2026 ~01h40, leitura focada (decisão do aluno, 07/11, para painel que só troca peças dentro de uma fórmula testada): '
    'REGRAS-DO-AGENTE.md (P1 a P45) inteiro, LICOES-FLOW-E-PROMPTS.md inteiro (checklist 1 a 37), FATOS-DO-ALUNO.md inteiro, BIBLIOTECA-DE-TAKES.md inteiro, '
    'DNA Visual - Nora v2.md, os pacotes dos painéis do nora48 e do nora49, CLAUDE.md (seções 0 a 6), METRICAS-NORA-LEIA.md (leituras de 06 e 07/11), '
    'as linhas do nora43, nora48 e nora49 no METRICAS-NORA.csv e a seção 49 da BIBLIOTECA-VIDEOS-VIRAIS.md (mineração de 06/11).')
p['texto_tela']['hook_termina'] = "the year's most powerful portal."
p['comentario_fixado'] = {
    'insta': "Gemini, Libra, Aquarius: what's the one question your mind keeps asking lately? ✨ Tell me below, then tap my photo and open my story before 11:11: your private reading starts there. 🔮",
    'face': "Gemini, Libra, Aquarius: what's the one question your mind keeps asking lately? ✨ Your private reading is right here, open it before the 11:11 portal 🔮 👉 " + FB}
p['pre_gancho'] = {
    'titulo_secao': 'Hook: a pedra escura que racha (nora34-PRE, já pronto, 0 crédito)', 'duracao': 4, 'tomadas': 1, 'com_rosto': True, 'etapas': [],
    'conceito': 'Gancho do nicho: a Nora abre a pedra escura e aparece o quartzo rosa. É o mesmo do nora43, que levou ~10 pessoas ao perfil a cada 1.000 views. Só o gancho muda em relação ao nora49.',
    'modo': 'Não gere nada aqui. Use o arquivo nora34-PRE como está, sem espelhar.',
    'montagem': ('1) Projeto novo no CapCut com o nora48-montado (o vídeo SEM texto do nora48).\n'
                 '2) Divida no começo do Take 2 ("Don\'t tell anyone", ~16,6 s) e apague tudo o que vem antes (o tsunami e o Take 1 do nora48).\n'
                 '3) No começo, ponha o nora34-PRE inteiro (~4 s, com o som dele) e, logo depois, o nora50-T01-cortado.\n'
                 '4) No hook fica só o som da pedra.'),
    'texto_tela': '', 'edicao': ''}
c = p['central']
c['conferir'] = ('Conferir no Take 1: é a Nora (rosto, lua com as estrelinhas, trança, blusa preta), no quarto à noite com o abajur rosa, segurando as duas metades do geodo; '
                 'fala uma vez só, em inglês, com os signos certos (Gemini, Libra or Aquarius), e termina em "eleven eleven, the year\'s most powerful portal"; '
                 'as metades não fecham nem trocam de mão; sem texto, legenda ou música.')
c['passos'] = [
    'Take 1 na Central com a MESMA configuração do nora48 e do nora49 (o texto LIVRE do quarto à noite, nesta seção). Cole só a fala e a linha de movimentação do Take 1. Gere: 1 take de 10 s.',
    f'Agente do Flow: conversa nova, anexe só a nora37-IMG, cole o aviso de 1 prompt e, embaixo, o prompt do take. 15 créditos. Renomeie para {ARQ}. Use o Omni 1.1 Flash (o 1.2 cobra o dobro).',
    'Corte de silêncio só do nora50-T01 (nora50-T01-cortado).',
    'CapCut: projeto novo com o nora48-montado. Divida no começo do Take 2 ("Don\'t tell anyone", ~16,6 s) e apague tudo antes. No começo, ponha o nora34-PRE (~4 s, com o som dele) e o nora50-T01-cortado. Música −18 dB só no Take 1 novo (o resto já tem). Exporte SEM texto como nora50-montado e me mande até umas 18h (se passar de 30 MB, link do Drive).',
    'Story: ~17h me mande os números do story-0611 (vence às 18h43); eu digo com que texto repostar. Reposte antes das 19h30.',
    'Eu devolvo o nora50-final (caixa do topo com os signos, números, legenda, faixa do story e seta). Confira no celular e poste hoje (07/11) às 19h30 no Insta e no Face, ao vivo (o mesmo horário do nora49, para comparar só o gancho). Comentário: no Insta, comente e fixe (sem link); no Face, comente COMO A PÁGINA (já tem o link).']
p['videos'][0]['arquivo'] = ARQ
p['videos'][0]['cena'] = 'Take 1 do nora50 · Gancho no quarto à noite: Gêmeos, Libra e Aquário + o portal 11:11'
p['story']['nota'] = ('STORY: o story-0611 (mesma imagem story-3110, texto "You\'re not here by accident. ✨ / Your private reading is waiting below.", adesivo "Your reading 🗝️") vence hoje às 18h43. '
                      'Perto das 17h me mande os números dele (viewers e toques no link): se tiver toque, repostamos igual; se continuar com 0, repostamos com o texto antigo. '
                      'Reposte antes do nora50 (19h30), no Insta e no Face, com o link certo de cada rede. Insta (STORYIG): ' + IG + ' · Face (FACE): ' + FB)
mt = p['mapa_tela']
mt['numeros'] = [
    {'t': '222', 'x': 18, 'y': 10.5, 'onde': 'alto à esquerda', 'cor_nome': 'verde-limão', 'cor': '#7CFF4F', 'tamanho': 15},
    {'t': '11:11', 'x': 82, 'y': 30, 'onde': 'no meio à direita, na parede acima do abajur', 'cor_nome': 'amarelo-ouro', 'cor': '#FFD21F', 'tamanho': 13},
    {'t': '888', 'x': 18, 'y': 46.9, 'onde': 'à esquerda, na altura do ombro, sobre o cabelo', 'cor_nome': 'rosa-choque', 'cor': '#FF4FD8', 'tamanho': 11}]
for e in mt['estilos']:
    if e['nome'].startswith('Números fixos'):
        e['obs'] = 'Lugar, cor e tamanho novos (item 28): 222 verde-limão, 15, X -230 · Y 506; 11:11 amarelo-ouro, 13, X 230 · Y 256; 888 rosa-choque, 11, X -230 · Y 40. Do 1º quadro do hook ao fim. Eu ponho (P45) e confiro na prévia.'
    if e['nome'].startswith('Caixa do topo'):
        e['nome'] = 'Caixa do topo: “GEMINI, LIBRA, AQUARIUS” / “11:11, the most powerful portal” / “the worst is finally over”'
    if e['nome'].startswith('Legenda'):
        e['obs'] = 'Do Take 1 ao fim, Y -294, blocos de 2 a 4 palavras. Destaques: Gemini, Libra, Aquarius, 11:11, portal, money, prosperity, Michael, seal, follow, 222 e stories. Sem legenda no hook.'
p['edicao_linha'] = [
    {'quando': 'A. Antes de tudo', 'texto': 'Projeto novo no CapCut com o nora48-montado (sem texto)', 'como': 'É o vídeo que você me mandou pelo Drive para o nora48 (o tsunami, o Take 1 do nora48 e o corpo A limpo).'},
    {'quando': '0. Tirar o começo', 'texto': 'Apague o tsunami e o Take 1 do nora48', 'como': 'Divida no começo do Take 2 ("Don\'t tell anyone", ~16,6 s) e apague tudo antes.'},
    {'quando': '1. No começo', 'texto': 'nora34-PRE (a pedra escura que racha), sem espelhar', 'como': 'O arquivo inteiro (~4 s), com o som dele.'},
    {'quando': '2. Depois do hook', 'texto': 'nora50-T01-cortado', 'como': 'Encoste no fim do hook e antes do Take 2. Ouça a emenda: termina em "before eleven eleven, the year\'s most powerful portal".'},
    {'quando': '3. Só no Take 1 novo', 'texto': 'Música de sempre ("Ambient Mystical Drone"), −18 dB', 'como': 'O resto do vídeo já tem a música do nora48.'},
    {'quando': '4. Exportar e me mandar', 'texto': 'Exporte SEM nenhum texto e mande aqui no chat do Code', 'como': '720×1280 ou 1080×1920, qualidade alta, nome nora50-montado (se passar de 30 MB, link do Drive). Eu ponho a caixa do topo, os números, a legenda, a faixa do story e a seta e devolvo o nora50-final.'}]
p['pecas']['lista'] = [
    {'nome': 'nora34-PRE', 'de': 'nora34', 'tipo': 'hook (pronto)', 'status': 'reutilizar', 'descricao': 'A pedra escura que racha e mostra o quartzo rosa (varanda, blusa azul-marinho), sem espelhar. É o hook do nora43.'},
    {'nome': 'nora37-IMG', 'de': 'nora37-IMG', 'tipo': 'imagem 1', 'status': 'reutilizar', 'descricao': 'Quarto à noite, abajur rosa, blusa preta canelada, as duas metades do geodo nas mãos (a imagem do Take 1 e do corpo do nora48 e do nora49).'},
    {'nome': ARQ, 'tipo': 'take', 'status': 'gerar', 'creditos': 15, 'descricao': '“' + FALA + '”'},
    {'nome': 'nora48-T02 a nora48-T08 (o corpo A limpo)', 'de': 'nora48', 'tipo': 'corpo', 'status': 'reutilizar', 'descricao': 'O corpo do nora48 a partir do Take 2, SEM texto, como está no nora48-montado. Não gere, não corte e não junte de novo.', 'onde': 'No nora48-montado (o vídeo sem texto do nora48), a partir do Take 2.'},
    {'nome': 'story-0611 (repost)', 'de': 'story-3110', 'tipo': 'story', 'status': 'reutilizar', 'descricao': 'Repostar antes das 19h30 (vence 18h43), com o texto que eu disser às ~17h.'}]
p['pecas']['decisao'] = [
    'Teste de uma variável: o gancho. O tsunami (bizarro) dá view, mas traz curioso: no Insta, o nora48 levou 2,1 pessoas ao perfil a cada 1.000 views (à 01h10) e o nora49, 5,5 (às 19h31, com o dobro de EUA). O nora43, com esta pedra do nicho, levou ~10 à 01h15.',
    'Por isso o nora50 sai às 19h30, no mesmo horário do nora49, com o mesmo corpo e o mesmo molde de Take 1: só o gancho muda. Régua: visitas ao perfil por 1.000 views, viewers do story e cliques no Tracker.',
    'Signos de ar (Gêmeos, Libra, Aquário), os que estão há mais tempo sem vídeo (desde o nora42, 29/10).',
    'Total: 15 créditos (só o Take 1). Créditos: 53 + 122.']
p['silencio']['intro'] = 'Só o Take 1 novo (nora50-T01) passa por aqui: o resto vem do nora48-montado. Arraste só o nora50-T01 na ferramenta “M2M FusionZ – Cortar e juntar vídeos” e deixe assim:'
p['respostas_face'] = {
    'aviso': p['respostas_face']['aviso'],
    'comentario': ['💫 Sent it to your messages, take a look ✨', '🔮 It\'s in your DMs now 💖', '✨ Just messaged you, check your inbox 🔮'],
    'dm': ['✨ [name], your private reading is ready 🔮 Open it before the 11:11 portal:', '💖 Hey [name]! This is the reading I mentioned ✨ Here it is:', '🔮 [name], I saved this for you 💫 Your private reading, before 11:11:']}
novo = t[:i] + json.dumps(p, ensure_ascii=False) + t[j:]
novo = novo.replace('<title>Painel nora49', '<title>Painel nora50')
open(f'{R}/PAINEL-NORA50.html', 'w', encoding='utf-8').write(novo)
print('ok', len(novo))
