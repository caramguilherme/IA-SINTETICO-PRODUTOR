import json, sys, re
P31 = sys.argv[1]; P30 = sys.argv[2]
def load(p):
    s = open(p, encoding='utf-8').read(); L = s.split('\n')
    i = [k for k, l in enumerate(L) if l.startswith('const PACOTE = ')][0]
    return s, L, i, json.loads(L[i][len('const PACOTE = '):].rstrip().rstrip(';'))
s31, L31, i31, d = load(P31)
_, _, _, d30 = load(P30)

HANDS = ("THE HANDS: slim adult feminine hands with golden sun-kissed light-to-medium tan skin and a warm golden undertone (not orange), "
         "anatomically correct, exactly five fingers on each hand, short natural nails with pale pink polish, one small gold sun-symbol ring on the "
         "index finger of each hand, and three thin gold bracelets stacked on her LEFT wrist only (on the right side of the image), none on the right "
         "wrist; the cuffs of long fitted deep forest-emerald (dark green with a slight blue tone) waffle-knit sleeves are visible at the bottom edge of the frame.")
KITCHEN = ("in a real American home kitchen at night. Behind it there is only a soft, warm, out-of-focus blur: a white kitchen cabinet at the upper left of "
           "the image, a dark night window at the upper right of the image and the warm yellow glow of a hanging pendant lamp, which is the only light.")
TAIL = ("Natural light and real skin texture with the spontaneous look of a smartphone; no CGI, no 3D render, no illustration, no plastic skin, no advertising look.")

IMG_A = ("Vertical 9:16 smartphone macro photo, photorealistic, generated from scratch with no reference image. The lens is about 22 cm from two women's hands "
         + KITCHEN + " In the center of the frame, about 20 cm from the lens, a sealed adhesive-bandage wrapper is held horizontally between the two hands: a white "
         "paper wrapper about 9 cm long and 3 cm wide with a thin red stripe along its top edge, completely closed and sealed, with NO readable text and NO brand "
         "name on it. Her LEFT hand (the hand on the RIGHT side of the image) pinches the right end of the wrapper between its thumb and index finger and holds it "
         "steady. Her RIGHT hand (the hand on the LEFT side of the image) pinches the small red pull tab at the left end of the wrapper between its thumb and index "
         "fingertips, ready to pull it. The wrapper and the fingertips are in sharp macro focus. " + HANDS + " NOT IN THE FRAME: her face, hair, chest or body; any "
         "underwear or any fabric besides the sleeve cuffs; any loose bandage; any other object, person or animal; any text, logo, watermark or date stamp. " + TAIL)
IMG_C = ("Vertical 9:16 smartphone macro photo, photorealistic, generated from scratch with no reference image. The lens is about 22 cm in front of one red "
         "satin-and-lace women's brief that hangs open and flat, " + KITCHEN + " The brief is held by her LEFT hand (the hand on the RIGHT side of the image), which "
         "grips its right waistband corner between the thumb and fingers, so the brief hangs open and flat in the center of the frame with its smooth bright-red "
         "satin front panel (about 12 cm wide and 14 cm tall) facing the lens, framed by wide scalloped red lace trim around the leg openings and the waistband; "
         "the brief is fully intact and plain, with nothing printed on it and nothing attached to it yet. Her RIGHT hand (the hand on the LEFT side of the image) "
         "holds one beige adhesive bandage about 7.5 cm long by its center between the thumb and index finger, vertically, about 6 cm in front of the satin panel "
         "and directly in front of its center, its white backing tabs already peeled off so its sticky side faces the panel, not touching it yet, with no text on "
         "it. The satin panel, the bandage and the fingertips are in sharp macro focus. " + HANDS + " NOT IN THE FRAME: her face, hair, chest or body; no body "
         "behind or through the brief; any other object, person or animal; any text, logo, watermark or date stamp. " + TAIL)
IMG_B = ("EDIT of the attached image (use it as the base image): keep exactly the same kitchen blur, the same warm lamp light, the same macro framing and the same "
         "two hands with their rings, bracelets and emerald sleeve cuffs. Changes: the wrapper has been torn open along its length and its two paper flaps are "
         "spread open like a book; her LEFT hand (on the RIGHT side of the image) holds the open, empty wrapper by its flaps at the lower right of the frame; her "
         "RIGHT hand (on the LEFT side of the image) has pulled a beige adhesive bandage about 7.5 cm long out of the wrapper and holds it by the pads of its thumb "
         "and index finger at its center, horizontally in the middle of the frame about 15 cm from the lens, very sharp, with the white absorbent pad and the two "
         "white paper backing tabs visible and no text on it. The wrapper does not vanish and stays in her left hand. No face, no body, no text. Change nothing else.")
IMG_D = ("EDIT of the attached image (use it as the base image): keep exactly the same kitchen blur, the same warm lamp light, the same macro framing, the same red "
         "satin-and-lace brief held by its right waistband corner in her left hand (on the RIGHT side of the image) and the same two hands with their rings, "
         "bracelets and emerald sleeve cuffs. Changes: the beige adhesive bandage is now stuck vertically in the exact center of the satin front panel, flat and "
         "smooth; the tip of her right index finger (on the LEFT side of the image) rests on the bandage and presses it; the right thumb is out of sight behind the "
         "satin. The brief stays intact and plain. No face, no body, no text. Change nothing else.")

g = d['pre_gancho']
g['com_rosto'] = False
g['conceito'] = ("Modelo nos virais w1 e w2: o curativo sai do invólucro e é colado numa calcinha de renda vermelha, só as mãos. Mesma cozinha à noite e mesmas "
                 "mangas verdes do nora30. Depois entra o Take 1, com a Nora segurando a calcinha com o curativo.")
g['imagem_prompt'] = IMG_A; g['imagem_final_prompt'] = IMG_B
E = g['etapas']
E[0]['prompt'] = IMG_A; E[0]['anexar'] = "nada (só aparecem as mãos)"
E[1]['prompt'] = IMG_B; E[1]['anexar'] = "SÓ a imagem A aprovada (é uma edição dela)"
E[3]['prompt'] = IMG_C; E[3]['anexar'] = "nada (só aparecem as mãos)"
E[4]['prompt'] = IMG_D; E[4]['anexar'] = "SÓ a imagem C aprovada (é uma edição dela)"
g['modo'] = ("Gere as 4 imagens e me mande antes dos vídeos. Não aprove se aparecer rosto, corpo, texto ou marca no invólucro; na A não pode aparecer a "
             "calcinha. Cada vídeo: modo FRAMES, 4 s, 9:16, áudio ligado.")
g['montagem'] = ("1) nora31-PRE-V1: use de 0,5 s a 2,5 s (rasga e tira o curativo).\n2) Corte seco para nora31-PRE-V2: use de 0,8 s a 3,0 s (cola e alisa).\n"
                 "3) Corte seco para o corpo cortado (nora31-cortado). O pré-gancho fica com uns 4 s, como nos virais w1 e w2.")

# IMAGEM 1 = edição da IMAGEM 1 do nora30 (mesma cozinha, mesma blusa): continuidade com os takes 2 a 9 reaproveitados
d.pop('imagem_central', None)
d['refs'] = ["nora30-IMG (a IMAGEM 1 do nora30, já aprovada): anexe só ela na IMAGEM 1 do nora31"]
d['trava_referencia'] = ("There is no pet in this project: no animal appears in any scene. The only attached image is the approved photo of this woman from the "
                         "previous video: it is both her identity reference and the base image of this edit. Keep her face, skin, eyes, hair, face gems, jewelry "
                         "and body exactly as in the attached image.")
d['figurino'] = d30['figurino'].replace("Clothing is secondary to the contrast of the amethyst geode in the hook.",
                                        "Clothing is secondary to the contrast of the red satin-and-lace brief in the hook.")
assert 'red satin-and-lace brief' in d['figurino']
SCENE = ("EDIT of the attached image (the approved photo of this woman from the previous video). Use it as the base image and change only what is listed "
         "below. KEEP EXACTLY: the same woman and face, her hazel-green eyes, her very long softly wavy jet-black hair with the thin gold-ringed braid, the "
         "single gold crescent-moon gem with three tiny gold stars on her cheekbone on the left side of the image, her clean forehead, her long gold "
         "star-and-moon earrings, her thin gold Venus-symbol necklace, her deep forest-emerald waffle-knit top with the small American flag pin on her left chest "
         "(the right side of the image), the same home kitchen at night (the white cabinet at the upper left of the image, the black coffee machine at the left "
         "edge, the dark night window and the hanging pendant lamp at the upper right, the granite counter with the soap dispenser at the right), the same warm "
         "yellow lamp light, the same camera height, distance, angle and framing, and her calm, firm gaze into the lens with her lips closed. CHANGES (only "
         "these): (1) remove the amethyst slab completely: no crystal, stone or geode anywhere in the image; (2) both of her hands are now raised in front of her "
         "upper chest, elbows bent and close to her body, holding one red satin women's brief open and flat with its front facing the lens: her RIGHT hand (the "
         "hand on the LEFT side of the image) pinches the left side edge of the brief and her LEFT hand (the hand on the RIGHT side of the image) pinches the right "
         "side edge, each with the thumb in front and the other fingers behind the fabric; (3) the brief has a smooth bright-red satin front panel about 12 cm "
         "wide and 14 cm tall and wide scalloped red lace trim around the leg openings and the waistband; its top edge is at the height of her collarbones and its "
         "bottom edge is no lower than the middle of her chest, so it never covers her chin, mouth or face and the bandage sits at about half of the frame height; "
         "(4) in the exact center of the satin panel there is one beige adhesive bandage about 7.5 cm long and 2 cm wide, stuck vertically, flat and smooth, with "
         "its white pad and perforated edges visible and no text or logo on it. MUST NOT HAPPEN: no body visible through the brief, no second brief, no second "
         "bandage, nothing printed on the brief, nothing else in her hands, no change to her face, skin, hair or top, no new object or person in the kitchen, no "
         "text, no date stamp, no watermark, no logo. Below about two thirds of the frame height only her top is visible: no hands, brief or object there. Each "
         "hand has exactly five fingers with natural proportions. Do not rejuvenate or smooth the skin.")
d['imagens'] = [{"rotulo": "IMAGEM 1", "cena": SCENE}]

# Só o Take 1 é gerado
T1_FALA = d['videos'][0]['fala']
T1_MOV = ("Throughout the whole 10 seconds both of her hands keep holding the red satin-and-lace brief open and still in front of her upper chest by its two "
          "side edges, her right hand on the left side of the frame and her left hand on the right side of the frame, with its front panel and the beige bandage "
          "facing the lens, and the brief never changes hands, never turns away, never drops, never rises to her face and never leaves the frame, her fingers "
          "stay on the side edges and never touch the bandage, her eyes stay on the lens, during the first sentence of the take she raises her eyebrows in "
          "playful surprise, during the second sentence she gives one slow nod, during the final sentence she holds a firm steady gaze with a faint knowing half "
          "smile, and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; the camera, the kitchen and the "
          "lamp light stay completely still and each hand has exactly five fingers.")
v1 = d['videos'][0]; v1['movimentacao'] = T1_MOV
d['videos'] = [v1]

c = d['central']
LIVRE = ("Casual handheld smartphone video in a home kitchen at night with warm yellow lamp light. CONTINUITY LOCKS for every take: the woman, her face, her "
         "long black wavy hair, her braid with gold rings, her gold moon and star face gems, her star-and-moon earrings, her Venus necklace, her deep forest-green "
         "waffle-knit top, her flag pin, her gold rings and bracelets stay exactly as in the reference image; she sits upright facing the camera, leaning slightly "
         "toward it, framed exactly as in the reference image, and both of her hands hold the red satin-and-lace brief open and still in front of her upper chest "
         "by its two side edges, her right hand on the left side of the frame and her left hand on the right side of the frame, with its front panel and the "
         "beige bandage facing the lens, for the whole clip; the brief never changes hands, never turns away, never drops and never rises to her face, and her "
         "fingers never touch the bandage; the camera is a handheld phone at chest height about 60 centimeters from her with only a tiny natural sway, no zoom, "
         "no cuts and no reframing; the white cabinet at the upper left, the black coffee machine at the left edge, the window with the dark night and the "
         "hanging pendant lamp at the upper right, the granite counter with the soap dispenser at the right stay exactly where they are and never move; no "
         "object, person, animal or text appears or disappears, and no crystal or amethyst appears; each hand always has exactly five fingers; no on-screen "
         "text, no captions, no logos; real quiet kitchen room sound only, no music. SPEECH RULE for every take: she says only the exact words of that take's "
         "script, each word exactly once and in order, with no repeated word, no extra word and no added sentence before, between or after; when she finishes "
         "the last word she closes her lips, stays silent and keeps a calm still expression until the clip ends.")
n = 0
for sec in c['config']:
    for k in sec['campos']:
        if k['campo'].startswith('LIVRE'):
            k['copiar'] = LIVRE; n += 1
        if k['campo'] == 'COLE SUA COPY AQUI':
            k['valor'] = 'colar só a fala do Take 1 (seção “A fala e a movimentação”)'
        if k['campo'] == 'Movimentação':
            k['valor'] = 'colar a linha do Take 1 (seção “A fala e a movimentação”)'
        if k['campo'] == 'Conferir':
            k['valor'] = '1 take de 10 s (seção “A fala e a movimentação”)'
        if k['campo'] == 'Copiar':
            k['valor'] = 'o botão COPIAR do Take 1'
assert n == 1
c['colagens'] = [{"titulo": "só o Take 1 (gancho)", "fala": T1_FALA, "movimentacao": [T1_MOV], "takes": [0]}]
c['conferir'] = ("Conferir no Take 1: é a Nora da IMAGEM 1, na mesma cozinha e com a mesma blusa do nora30; a calcinha com o curativo fica nas duas mãos do "
                 "começo ao fim e não cobre o rosto; a fala sai completa, uma vez só, em inglês; a voz parece a do nora30 (ouça a emenda do Take 1 para o "
                 "Take 2); sem texto, legenda ou música.")
c['agente'] = {"imagem": "IMAGEM 1 do nora31",
               "aviso": "Irei enviar 1 prompt para você. Quero que seja feita uma animação da imagem anexada. Utilize a imagem anexada como frame inicial e frame final do vídeo.",
               "passos": ["Abra uma conversa nova no agente do Flow.", "Anexe a IMAGEM 1 do nora31 (só ela).", "Cole o aviso (acima).",
                          "Embaixo, cole o prompt do Take 1 (botão COPIAR do take na Central).",
                          "Envie. Confira o vídeo e me diga se falhou (o que saiu errado)."]}
c['passos'] = [
 "Pré-gancho (seção “Pré-gancho”): gere as 4 imagens, A, B, C e D, na ordem. Na A e na C não anexe nada; na B anexe só a A e na D só a C. Só aparecem as mãos. Ainda não gere os vídeos.",
 "IMAGEM 1 (seção “Imagem 1”): no Flow, gere uma imagem 9:16 anexando SÓ a nora30-IMG (a imagem 1 do nora30) e colando o prompt. É uma edição: a mesma Nora, na mesma cozinha e com a mesma blusa, segurando a calcinha com o curativo com as duas mãos no lugar do geodo. Aprove só se o rosto, a roupa e a cozinha estiverem iguais aos do nora30, o geodo tiver sumido e não houver carimbo de data nos cantos. Renomeie para nora31-IMG.",
 "Me mande as 5 imagens (A, B, C, D e IMAGEM 1). Eu confiro e libero. Não gere os vídeos nem o take antes disso.",
 "Depois do meu ok: os 2 vídeos do pré-gancho em FRAMES (A→B e C→D), 7 créditos cada.",
 "Central do curso: preencha a configuração (seção “Central do curso: o que preencher”) e cole só a fala do Take 1 e a linha de movimentação dele. Clique em GERAR PROMPT DE ANIMAÇÃO e confira: 1 take de 10 s. Não clique em “Resetar valores” nem em “REGERAR BLOCO”.",
 "Agente do Flow: anexe a IMAGEM 1 do nora31 (só ela), cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take). Renomeie para nora31-T1-gancho-o-que-voce-fez. 15 créditos.",
 "Os takes 2 a 9 NÃO são gerados: são os do nora30 (lista em “Nomes e reaproveitamento”). Baixe e renomeie cada cópia de nora30-T… para nora31-T… (a ferramenta de corte junta pela ordem do nome).",
 "Corte de silêncio (seção “Cortar os silêncios”): suba nora31-T1 a nora31-T9 juntos e junte tudo com Corte seco. Se você não tiver mais os takes do nora30 separados, me avise antes.",
 "Custo total: 29 créditos (pré-gancho 14 + Take 1 15)."]

# Nomes e reaproveitamento
old = {x['nome']: x for x in d['pecas']['lista']}
lista = [old[k] for k in ['nora31-PRE-A', 'nora31-PRE-B', 'nora31-PRE-V1', 'nora31-PRE-C', 'nora31-PRE-D', 'nora31-PRE-V2']]
lista[0]['base'] = "Pré-gancho dos virais w1 e w2: curto, só as mãos, começando na ação."
lista[0]['descricao'] = "Tomada 1, primeiro quadro: as duas mãos com o invólucro fechado do curativo (sem referência anexada)."
lista[3]['descricao'] = "Tomada 2, primeiro quadro: macro da calcinha vermelha, com o curativo na mão direita acima do centro (sem referência anexada)."
lista.append({"nome": "nora30-IMG", "de": "nora30-IMG", "tipo": "imagem 1 do nora30", "status": "reutilizar",
              "descricao": "Base da edição: anexe só ela para gerar a IMAGEM 1 do nora31."})
lista.append({"nome": "nora31-IMG", "tipo": "imagem 1 do vídeo", "status": "gerar",
              "descricao": "Edição da nora30-IMG: a mesma cozinha e a mesma blusa, com a calcinha com o curativo nas duas mãos. Primeiro e último quadro do Take 1."})
t1 = old['nora31-T1-gancho-o-que-voce-fez']; t1['serve'] = "Só deste vídeo."; lista.append(t1)
for p in d30['pecas']['lista']:
    if re.match(r'nora30-T[2-9]-', p['nome']):
        novo = 'nora31-' + p['nome'][len('nora30-'):]
        fala = [v['fala'] for v in d30['videos'] if v.get('arquivo') == p['nome']][0]
        lista.append({"nome": p['nome'], "de": p['nome'], "tipo": p['tipo'] + " (do nora30)", "status": "reutilizar", "creditos": p['creditos'],
                      "fala": fala, "descricao": "Para a ferramenta de corte, renomeie a cópia para " + novo + "."})
d['pecas'] = {"lista": lista, "decisao": [
    "Versão barata (decisão do aluno, 22/10/2026): pré-gancho e Take 1 novos; os takes 2 a 9 são os do nora30.",
    "A IMAGEM 1 é uma edição da imagem do nora30 (mesma cozinha e mesma blusa): no Take 2 só muda o objeto na mão."]}

# Texto na tela e mapa
d['mapa_tela']['regras'][0] = ("Mesma faixa do nora30 (69% a 77%, Y −294 no CapCut), porque os takes 2 a 9 são os dele. Blocos de 2 a 3 palavras. "
                               "Confirmo o Take 1 quando você me mandar a IMAGEM 1.")

r = d['roteiro']
r['titulo'] = "Áries, Leão e Sagitário: o curativo na calcinha (corpo do nora30)"
r['formato'] = "Pré-gancho dos virais w1 e w2 + Take 1 novo + takes 2 a 9 do nora30 (reaproveitados)"
r['duracao_total'] = 94
r['leitura_registro'] = ("22/10/2026 (versão barata, pedido do aluno): antes de mudar os prompts li inteiros, com a ferramenta de leitura, todos os "
    "arquivos de `LEIA-TUDO-ANTES.md`: `FATOS-DO-ALUNO.md`, `CLAUDE.md`, `00-LEIA-PRIMEIRO.md`, `PROJETO-Dana.md`, `BRIEFING-LOVECHART.md`, "
    "`LICOES-FLOW-E-PROMPTS.md`, `DNA Visual - Dana.md`, `DNA Visual - Nora.md`, `DNA Visual - Nora v2.md`, `REGISTRO-DE-PERSONAS.md`, `hooks.md`, "
    "`Formatos Narrativos - Problema e Cenario.md`, `Exemplos de Roteiros - 2 Formatos.md`, `ctas.md`, `COMUNICACAO-VISCERAL-E-FALADA.md`, "
    "`BIBLIOTECA-BODIES.md`, `BIBLIOTECA-COLD-READING.md`, `BIBLIOTECA-COPY.md`, `BIBLIOTECA-COPY-100-ROTEIROS.md`, `PESQUISA-PUBLICO.md`, "
    "`BIBLIOTECA-VIDEOS-VIRAIS.md`, `BIBLIOTECA-PRE-GANCHOS.md`, `Prompts.txt`, `CHECKLIST-DE-PRODUCAO.md`, `PAPEL-AGENTE-FLOW.md`, `GUIA-CREATIVE-HUB.md`, "
    "os `PLANO-CREDITOS-*`, os `PASSO-A-PASSO-*`, `EXEMPLO-ROTEIRO-APROVADO-FIGADO.md`, `EXEMPLO-PACOTE-FIGADO.md`, `PAINEL-MODELO.html`, "
    "`METRICAS-NORA.csv`, `BIBLIOTECA-DE-TAKES.md`, `ROTEIRO-R001` a `ROTEIRO-NORA30-33`, os `STORY-*`, `ROTEIRO-LOVECHART-RESERVA-SEU-PADRAO-TEM-NOME.md` "
    "e os `TAKE-NOVO-*`. `FOTO-PERFIL-DANA.md` não (só vale para foto de perfil).")

L31[i31] = 'const PACOTE = ' + json.dumps(d, ensure_ascii=False) + ';'
out = '\n'.join(L31)
# Seção fixa do corte de silêncio: aqui os takes são juntados na ferramenta
a91 = [l for l in out.split('\n') if 'Arraste o vídeo do corpo na ferramenta' in l or 'Arraste o vídeo na ferramenta' in l]
assert len(a91) == 1
out = out.replace(a91[0], '      <p style="color:var(--ink2);margin:0 0 12px;font-size:14.5px">Suba na ferramenta “M2M FusionZ – Cortar e juntar vídeos” os 9 takes do corpo, com os nomes nora31-T1 a nora31-T9 (o Take 1 novo e as cópias renomeadas dos takes do nora30). O pré-gancho não entra. Deixe assim:</p>')
a102 = '<div><b>Juntar tudo num arquivo só:</b> DESLIGADO (o vídeo já está junto)</div>'
assert out.count(a102) == 1
out = out.replace(a102, '<div><b>Juntar tudo num arquivo só:</b> LIGADO, transição Corte seco (junta pela ordem do nome: nora31-T1 a nora31-T9)</div>')
open(P31, 'w', encoding='utf-8').write(out)

# Checagem P32: a linha de movimentação não cita a fala (nenhum par de palavras da fala, fora pares comuns)
def bigr(t):
    w = re.findall(r"[a-z0-9']+", t.lower()); return set(zip(w, w[1:]))
comuns = {('of', 'the'), ('and', 'the'), ('the', 'take'), ('and', 'it')}
over = (bigr(T1_FALA) & bigr(T1_MOV)) - comuns
print('sobreposicao fala x movimentacao:', over or 'nenhuma')
print('palavras T1:', len(T1_FALA.split()), '| frases na linha:', T1_MOV.count('. '))
print('creditos gerar:', sum(x.get('creditos', 0) for x in lista if x['status'] == 'gerar'), '| economia:', sum(x.get('creditos', 0) for x in lista if x['status'] == 'reutilizar'))
