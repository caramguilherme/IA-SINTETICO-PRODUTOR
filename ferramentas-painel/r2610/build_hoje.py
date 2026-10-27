import json, re, copy, sys
SP = '/tmp/claude-0/-home-user-IA-SINTETICO-PRODUTOR/3ab4d77d-5255-5081-ab6b-bd18819fdc0d/scratchpad/'
REPO = '/home/user/IA-SINTETICO-PRODUTOR/'

def pacote_de(f):
    h = open(REPO + f, encoding='utf-8').read()
    return json.loads(re.search(r'const PACOTE = (\{.*?\});\n\(function', h, re.S).group(1))

C34 = json.load(open(SP + 'cur34.json', encoding='utf-8'))   # nora34 publicado (25/10, P40)
C33 = pacote_de('PAINEL-NORA33.html')                       # modelo do texto na tela
TRAVA = C34['trava_referencia']
VOZ = C34['perfil']['voz']
REF_TXT = "VISUAL REFERENCE LOCK: use exclusively the ATTACHED references as identity authorities. Preserve the face, build, hair, proportions and appearance of the human and the pet. Do not mix identities."
ESTILO_IMG = "UGC STYLE LOCK: vertical 9:16 image, photorealistic, shot in an American home with the spontaneous look of a smartphone. Natural light, real skin, fabric and hair textures, casual and slightly imperfect framing. The camera stays out of frame. No text, caption, logo, watermark or advertising look."

def img_com_trava(fig, cena):
    return REF_TXT + ' ' + TRAVA + '\n\nFIXED OUTFIT: ' + fig + '\n\n' + ESTILO_IMG + '\n\nSCENE: ' + cena

LEITURA = ("26/10/2026: antes de montar este painel li inteiros, com a ferramenta de leitura, nesta sessão, todos os arquivos de `LEIA-TUDO-ANTES.md`: "
           "`FATOS-DO-ALUNO.md`, `CLAUDE.md`, `00-LEIA-PRIMEIRO.md`, `PROJETO-Dana.md`, `BRIEFING-LOVECHART.md`, `LICOES-FLOW-E-PROMPTS.md`, `COMUNIDADE-E-ESTRATEGIA.md`, "
           "os três `DNA Visual`, `REGISTRO-DE-PERSONAS.md`, `hooks.md`, `Formatos Narrativos…`, `Exemplos de Roteiros…`, `ctas.md`, `COMUNICACAO-VISCERAL-E-FALADA.md`, "
           "as `BIBLIOTECA-*` (bodies, cold reading, copy, 100 roteiros, virais até a seção 38, pré-ganchos, takes), `PESQUISA-PUBLICO.md`, `Prompts.txt`, `CHECKLIST-DE-PRODUCAO.md`, "
           "`PAPEL-AGENTE-FLOW.md`, `GUIA-CREATIVE-HUB.md`, os `PLANO-CREDITOS-*` e `PASSO-A-PASSO-*`, `TAKE-NOVO-*`, os `EXEMPLO-*`, `PAINEL-MODELO.html`, `PAINEL-NORA34.html`, "
           "`METRICAS-NORA.csv`, `METRICAS-NORA-LEIA.md`, os `ROTEIRO-*` (R001 a nora36), os `RESERVA-ROTEIRO-*` e os `STORY-*`. Não li: `FOTO-PERFIL-DANA.md`, "
           "`PROMPT-BLUEPRINT-COMUNIDADE.md` e os PDFs (os resumos estão no `BRIEFING-LOVECHART.md`).")

STORY = copy.deepcopy(C34['story'])
STORY['nota'] = ("Story do dia: o do P40 (texto e adesivo abaixo, a mesma imagem de sempre). Se ainda não postou hoje, poste antes do vídeo das 17h "
                 "e ponha no Destaque “Part 2”: ele vale para os 4 vídeos de hoje (nora34 a nora37).")
STORY['adesivos'] = ["Get my Love Chart", "Take the quiz"]

FIM_MOV = (", and from the end of the final sentence of the take until the clip ends she keeps her lips closed and silent; "
           "everything else in the scene stays completely still and each hand has exactly five fingers.")

def config_com_livre(livre):
    cfg = copy.deepcopy(C34['central']['config'])
    for sec in cfg:
        for c in sec['campos']:
            if c['campo'].startswith('LIVRE'):
                c['copiar'] = livre
    return cfg

AVISO_N = ("Vou te enviar {n} prompts, cada prompt é um vídeo. Faça todos na ordem, sem pedir minha aprovação entre um e outro, e depois renomeie cada um "
           "com o devido número. Mantenha a consistência de voz em todos eles e utilize a imagem anexada como frame inicial e frame final em todos os vídeos que você gerar.")
AVISO_1 = "Irei enviar 1 prompt para você. Quero que seja feita uma animação da imagem anexada. Utilize a imagem anexada como frame inicial e frame final do vídeo."

def agente_n(img, n):
    return {"imagem": img, "aviso": AVISO_N.format(n=n), "passos": [
        "Abra uma conversa nova no agente do Flow.",
        "Nas configurações do agente, ligue a opção de gerar sem pedir aprovação e salve antes de enviar.",
        "Anexe só a " + img + " aprovada (o blueprint não vai no agente).",
        "Cole o aviso (acima) e, embaixo, o bloco “COPIAR TUDO JUNTO” da Central, sem editar nada.",
        "Envie. O agente gera os %d vídeos; confira cada um no painel e me diga qual falhou (take e problema)." % n,
        "Se ele gerar só 1 take, abra um projeto novo no Flow e mande de novo."]}

def agente_1(img, nome):
    return {"imagem": img, "aviso": AVISO_1, "aviso_tag": "obrigatório: com 1 take o prompt da Central não traz o modo agente",
            "intro": "Uma imagem e uma mensagem: anexe a " + img + ", cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take na Central; com 1 take não existe o bloco “COPIAR TUDO JUNTO”).",
            "passos": ["Abra uma conversa nova no agente do Flow.", "Anexe a " + img + " (só ela).", "Cole o aviso (acima).",
                       "Embaixo, cole o prompt do Take 1 (botão COPIAR do take na Central).",
                       "Envie. Renomeie para " + nome + ". Confira o vídeo e me diga se falhou (o que saiu errado)."]}

def pin(signos):
    return {"insta": signos + ", this one is yours. 🔥 PART 2 is in my story: a quick quiz that reads your love chart and shows what kind of partner fits you. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222.",
            "face": signos + ", this one is yours. 🔥 PART 2 is in my Story: a quick quiz that reads your love chart and shows what kind of partner fits you. Tap my profile picture NOW, it's gone in 24 hours. Comment 222."}

# ---------------------------------------------------------------- estilos comuns
EST_NUM = {"nome": "Números fixos (222 à esquerda, 11:11 à direita)", "fonte": "Poppins Bold (poppins-bd)", "cor": "amarelo-ouro #FFD21F", "tamanho": "12",
           "contorno": "Traço preto + Sombra preta, sem Plano de fundo. Luz DESLIGADA", "obs": "Os dois do mesmo tamanho e na mesma altura."}
EST_LEG = {"nome": "Legenda automática (Claude das legendas)", "fonte": "Poppins Bold", "cor": "branco, em MAIÚSCULAS; palavra-chave em amarelo-ouro #FFD21F",
           "tamanho": "uns 38 px de fonte (vídeo 720×1280)", "contorno": "preto grosso, sem caixa e sem brilho", "obs": "Blocos de 2 a 4 palavras, no máximo 2 linhas, mesma posição o vídeo todo."}
EST_FAIXA = {"nome": "Faixa do story no topo: “Your love chart quiz is in my Stories ⭐”", "fonte": "Poppins Bold (poppins-bd)", "cor": "texto preto #000000, “my Stories” em vermelho #E53935",
             "tamanho": "9, em 1 linha", "contorno": "Plano de fundo branco arredondado, sem traço. Luz DESLIGADA", "obs": "No mesmo lugar do texto do topo (X 0 · Y 397), depois que ele sai."}
def est_seta(quando):
    return {"nome": "Seta vermelha", "fonte": "o caractere ⬇ (ou um adesivo de seta)", "cor": "vermelho #E53935", "tamanho": "14", "contorno": "Traço preto. Luz DESLIGADA",
            "obs": quando + ". Embaixo à esquerda, apontando para baixo, para a foto do perfil (X e Y na tabela do CapCut)."}
def est_caixa(signos):
    return {"nome": "Caixa do topo: “" + signos + ", pay very close attention”", "fonte": "Poppins Bold (poppins-bd)",
            "cor": "texto preto #000000; a palavra “attention” em vermelho #E53935", "tamanho": "10, em 2 linhas",
            "contorno": "Plano de fundo branco arredondado, sem traço. Luz DESLIGADA", "obs": "Centralizada no topo (X 0 · Y 397), igual nos vídeos da série."}

def mapa(leg, nome=None, curto=None, estilos=(), regras=()):
    m = {"topo_app": [0, 10], "codigos": [10, 14], "hook": [14, 24], "legenda": leg, "rodape_app": [78, 100],
         "botoes": {"x": [86, 100], "y": [48, 86]}, "estilos": list(estilos), "regras": list(regras)}
    if nome: m['legenda_nome'] = nome
    if curto: m['legenda_curto'] = curto
    return m

# ================================================================= nora34 (17h)
pk34 = copy.deepcopy(C34)
pk34['roteiro']['formato'] = "Copy curta, 3 takes (gancho, corpo, CTA), com pré-gancho de 4 s (pedra escura que racha, modelo do viral x5)"
pk34['roteiro']['molde_hook'] = ("hook visual do viral x5 (pedra escura apertada que racha e mostra cristal por dentro) + gancho falado do briefing da Appyon "
                                 "(ângulo 02: “Six months to find out it wasn't working…”); signos no texto do topo (Matheus)")
pk34['roteiro']['duracao_total'] = 34
pk34['roteiro']['leitura_registro'] = LEITURA
pk34['story'] = copy.deepcopy(STORY)

P34_A = ("EDIT of the attached image (use it as the base image): keep exactly the same woman, the same face, hazel-green eyes, very long black wavy hair with the gold-ringed braid, "
         "the gold moon and star face gems, the star-and-moon earrings, the Venus necklace, the gold sun ring, the deep navy-blue ribbed knit top with the small flag pin, "
         "the same front porch, the white front door, the small American flag on the siding, the white porch column, the green lawn and the same soft overcast daylight. "
         "Changes: remove the rose quartz cluster completely. Her framing is now from the top of her head down to just below her collarbones, with her face in the upper half of the frame "
         "and her eyes at about 30 percent of the frame height. With BOTH hands she squeezes ONE closed, rough, egg-shaped stone about 12 cm tall and 9 cm wide, held upright in the center "
         "of the frame at the height of her collarbones, about 25 cm from the lens, its top just below her chin at about 46 percent of the frame height and its bottom at about 66 percent. "
         "THE STONE: dark charcoal-gray, matte and rough like natural rock, with a faint blue-green iridescent sheen in two or three small spots; completely closed: no crack, no opening, "
         "no crystal and no pink visible yet. Her RIGHT hand (the hand on the LEFT side of the image) grips the stone's left side and her LEFT hand (the hand on the RIGHT side of the image) "
         "grips its right side, fingers wrapped around it and both thumbs pressing on its front, knuckles tense, elbows bent close to her body; each hand has exactly five fingers. "
         "HER FACE: strong effort, brows pulled together, eyes on the lens, jaw clenched, lips pressed together. The stone never covers her face. "
         "No dust yet, no glow, no sparkles, no other object, no text, no logo, no watermark and no date stamp. Change nothing else.")
P34_B = ("EDIT of the attached image (use it as the base image): keep exactly the same woman, face, hair, braid, face gems, earrings, necklace, ring, the navy top with the flag pin, "
         "the same porch background, the same overcast light and the same framing. Changes: the dark stone has cracked open into two halves. Her RIGHT hand (on the LEFT side of the image) "
         "holds the left half and her LEFT hand (on the RIGHT side of the image) holds the right half; the halves are pulled about 10 cm apart, still at the height of her collarbones "
         "and about 25 cm from the lens, each with its open inner face turned toward the lens. The outside of each half is the same dark charcoal-gray rough rock. The inside of each half "
         "is a hollow lined with dense, sparkling, translucent pale-pink rose quartz crystal points inside a thin milky-white rim. A few tiny dark rock flakes and a little fine gray dust "
         "are falling below the halves. Her face shows amazed surprise: eyebrows raised, eyes wide and on the lens, lips slightly parted; she is not speaking. The pink crystals are in "
         "sharp focus and are the point of highest contrast against the navy top. Each hand has exactly five fingers. No glow, no light rays, no sparkles floating in the air, "
         "no gold, no symbol, no letters, no text, no logo and no date stamp. Change nothing else.")
P34_V = ("Create a single continuous 4-second video clip that opens exactly on the first supplied frame and ends exactly on the last supplied frame, vertical 9:16. "
         "Handheld smartphone camera about 55 cm from the woman at the height of her collarbones, only a tiny natural shake, no zoom, no cuts, no reframing.\n\n"
         "THE MAIN EVENT: on a front porch on an overcast afternoon, the woman squeezes a closed, dark, egg-shaped stone with both hands until it cracks and splits into two halves "
         "that show pale-pink rose quartz crystals inside. In the first frame the stone is closed, in the center of the frame at the height of her collarbones, her right hand "
         "(on the left side of the image) on its left side and her left hand (on the right side of the image) on its right side, and her face already shows effort. She never speaks.\n\n"
         "SECOND BY SECOND (something visible moves in EVERY second):\n"
         "0.0 to 1.0 s: she squeezes harder; her knuckles tighten, her brows pull together, her shoulders tense and the stone trembles slightly in her grip.\n"
         "1.0 to 2.0 s: one thin dark crack runs from the top of the stone down its front; a small puff of fine gray dust comes out of the crack.\n"
         "2.0 to 3.0 s: with a sharp snap the stone splits along the crack; her hands pull the two halves apart sideways, about 10 cm, and turn their open faces toward the lens, "
         "showing the sparkling pink crystals inside; tiny dark flakes and dust fall below the halves.\n"
         "3.0 to 4.0 s: she holds both halves still, open toward the lens, with her eyebrows raised in amazed surprise, exactly as in the last supplied frame.\n\n"
         "WHAT MUST NOT HAPPEN: the stone does not crack, open or show any crystal before 1.0 second; there are exactly two halves (no third piece, no crumbling into many pieces); "
         "the halves never vanish, float, merge back together or change hands; no glow, light rays, sparkles in the air or magic effects; the crystals stay pale pink; "
         "she does not speak or mouth any words; her face is never covered; each hand keeps exactly five fingers; the door, the flag, the porch column and the lawn never move; "
         "no object, person or animal appears or disappears.\n\n"
         "VISUAL: she is the same woman as in the supplied frames; realistic natural physics of rock cracking, no morphing. No text, no logos.\n\n"
         "AUDIO: real ambient sound only: the dry crack and snap of the stone and a faint sprinkle of falling grit, with soft outdoor porch ambience. No music, no voice, no added sound effects.")
pk34['pre_gancho'] = {
    "titulo_secao": "Pré-gancho (4 s, a pedra que racha, com o rosto da Nora)",
    "duracao": 4, "tomadas": 1, "com_rosto": True,
    "conceito": "Cópia do viral x5: ela aperta com as duas mãos uma pedra escura, a pedra trinca, estala e abre em duas metades com quartzo rosa por dentro. Mesma varanda e mesma blusa do vídeo.",
    "modo": ("Primeiro gere a nora34-IMG (seção “Imagens”, logo abaixo): as imagens A e B são edições dela. Me mande as 3 juntas. "
             "Depois do meu ok, o vídeo em FRAMES: primeiro quadro = nora34-PRE-A, último quadro = nora34-PRE-B, 4 s, 9:16, áudio ligado. 7 créditos."),
    "etapas": [
        {"tipo": "img", "titulo": "Imagem A: a pedra fechada, ela fazendo força", "nome": "nora34-PRE-A", "anexar": "SÓ a nora34-IMG aprovada (é uma edição dela)", "prompt": P34_A},
        {"tipo": "img", "titulo": "Imagem B: a pedra aberta, quartzo rosa por dentro", "nome": "nora34-PRE-B", "anexar": "SÓ a nora34-PRE-A aprovada (é uma edição dela)", "prompt": P34_B},
        {"tipo": "vid", "titulo": "Vídeo: a pedra racha e abre", "nome": "nora34-PRE", "duracao": 4,
         "quadros": "Modo FRAMES. Primeiro quadro: nora34-PRE-A. Último quadro: nora34-PRE-B. 4 s, 9:16, áudio ligado.", "prompt": P34_V}],
    "montagem": ("1) nora34-PRE: uns 3,5 s (corte logo depois que as metades abrem).\n2) Corte seco para o corpo cortado (nora34-cortado).\n"
                 "3) O texto do topo já entra no primeiro quadro do pré-gancho.\n"
                 "Plano B, se o Flow deformar a pedra: PRE-A por 1 s e PRE-B por 1,5 s como fotos, com zoom leve (100% a 106%), 0 crédito."),
    "texto_tela": "", "edicao": ""}
pk34['texto_tela']['hook_comeca'] = "o primeiro quadro do pré-gancho"
pk34['edicao_linha'][0]['quando'] = "1. Do primeiro quadro do pré-gancho até o fim da primeira fala"
pk34['edicao_linha'][0]['como'] = "Texto no topo, em 3 linhas. 1ª linha “Gemini, Libra, Aquarius:” em amarelo-ouro; o resto branco. Começa no primeiro quadro do pré-gancho e termina em “in week one”."
pk34['edicao_linha'].insert(0, {"quando": "0. Antes do Take 1", "texto": "Pré-gancho (nora34-PRE, uns 3,5 s)", "como": "Corte seco para o corpo cortado. Veja a montagem na seção do pré-gancho."})
c = pk34['central']
c['passos'] = [
    "IMAGEM 1 (seção “Imagens”): no Flow, gere uma imagem 9:16 anexando SÓ o blueprint da Nora v2 e colando o prompt (botão “Copiar imagem com trava”). Aprove só se: é a Nora (lua e 3 estrelinhas no lado esquerdo da imagem); o quartzo rosa grande está na mão do lado ESQUERDO da imagem, sem letras; a outra mão não aparece; cinco dedos; sem carimbo de data. Renomeie para nora34-IMG.",
    "Pré-gancho (seção “Pré-gancho”): gere a nora34-PRE-A (anexe SÓ a nora34-IMG) e a nora34-PRE-B (anexe SÓ a PRE-A). Me mande a nora34-IMG, a PRE-A e a PRE-B juntas. Eu confiro e libero as linhas de movimentação (as de agora são provisórias).",
    "Depois do meu ok: o vídeo do pré-gancho em FRAMES (A → B), 4 s. 7 créditos. Renomeie para nora34-PRE.",
    "Central do curso: a configuração (seção “Central do curso”) e a colagem única (fala inteira + 3 linhas). Confira: 3 takes de 10 s.",
    "Agente do Flow: anexe só a nora34-IMG, cole o aviso e o “COPIAR TUDO JUNTO” da Central, sem editar. 45 créditos (na conta de 53: 7 + 45 = 52). Renomeie os takes com os nomes do painel.",
    "Me mande a transcrição dos 3 takes antes de postar.",
    "Corte de silêncio só do corpo (seção “Cortar os silêncios”): suba os 3 takes de uma vez, com “Juntar tudo” ligado e Corte seco. CapCut: pré-gancho, corpo cortado, números fixos, texto do topo (desde o pré-gancho), legenda na tela, faixa do story (do Take 2 ao fim), seta vermelha (Take 3) e a música de sempre (−18 dB).",
    "Postar em 26/10 às 17h no Insta e no Face, com a localização Los Angeles, California no Insta (se não for estar online, programe no próprio app do Insta). O story do dia tem de estar no ar. Se não ficar pronto até as 17h, poste o nora35 às 17h e este às 19h (eu acerto os números depois)."]
pk34['pecas']['lista'] = ([
    {"nome": "nora34-PRE-A", "tipo": "imagem do pré-gancho", "status": "gerar", "descricao": "Primeiro quadro: a pedra escura fechada nas duas mãos, ela fazendo força (edição da nora34-IMG).",
     "base": "Viral x5 (pedra escura apertada, careta de esforço).", "serve": "Pode virar hook de outro vídeo na mesma varanda."},
    {"nome": "nora34-PRE-B", "tipo": "imagem do pré-gancho", "status": "gerar", "descricao": "Último quadro: as duas metades abertas, quartzo rosa por dentro (edição da PRE-A)."},
    {"nome": "nora34-PRE", "tipo": "vídeo do pré-gancho", "status": "gerar", "creditos": 7, "descricao": "4 s em Frames: a pedra trinca, estala e abre.",
     "base": "Viral x5; a conta dos x usa a pedra que racha em 3 de 5 vídeos.", "serve": "Face: colar em outros corpos (receita do Lucas)."}]
    + pk34['pecas']['lista'])
pk34['pecas']['decisao'] = pk34['pecas']['decisao'] + ["Hook visual pesado em todo vídeo (aluno, 26/10): a pedra escura que racha, cópia do viral x5, nativa de cristal (P40). O geodo cinza fica para o nora36 e o nora37."]

# ================================================================= nora35 (19h): texto na tela, placa dos signos (M2)
HOOK35 = "Don't you dare scroll past this. Your Venus is why love keeps ending the same way."
FIG35 = ("fortune-teller, subtle mystic; a structured emerald-green blazer with notched lapels, worn open over a plain black fine-knit crew-neck top, both smooth and matte, "
         "no print, embroidery, logo or shine. Clothing is secondary to the red handwriting on the white card. Fixed accessories, always visible: the long gold star-and-moon drop earrings, "
         "the long thin gold chain with the small gold Venus-symbol pendant, thin gold bracelets on her left wrist, a small gold sun-symbol ring on her right index finger and the gold "
         "face gems from the reference sheet; no other jewelry, turban, cape or costume")
CENA35 = ("Vertical 9:16 close-up photo of the woman from the attached reference sheet in a dim, cozy real American living room at night. "
          "FRAMING: from the top of her head down to just below her collarbones; her knees, legs and the floor are NOT in the frame. "
          "The camera is a handheld phone at the height of her collarbones, about 55 cm in front of her, level, no tilt. "
          "Her face is large and centered in the upper half of the frame, with her eyes at about 30 percent of the frame height; a serious, intense, knowing gaze straight into the lens; "
          "lips closed; shoulders square to the lens, leaning slightly toward the camera. "
          "HANDS: she holds one handwritten card with BOTH hands in front of her, just below her chin: her RIGHT hand (the hand on the LEFT side of the image) holds the card's left edge "
          "and her LEFT hand (the hand on the RIGHT side of the image) holds its right edge, thumbs in front on the white margins and the other fingers behind the card; the small gold sun ring "
          "is on her right index finger and the thin gold bracelets are on her left wrist; each hand has exactly five fingers with natural proportions; nothing else is in her hands. "
          "THE CARD: one flat, rigid rectangle of plain matte white card stock, held horizontally, flat and facing the lens squarely, about 35 cm from the lens, centered, spanning about "
          "75 percent of the frame width, its top edge just below her chin at about 46 percent of the frame height and its bottom edge at about 68 percent; it never covers her mouth. "
          "On it, written by hand with thick felt-tip markers in neat, bold capital letters, there are exactly two centered lines and nothing else: the first line, large, in bright red marker, "
          "reads ARIES, LEO, SAGITTARIUS; the second line, smaller, in black marker, reads 26, 27 AND 28 OF OCTOBER. Spell every word exactly like that, letter by letter "
          "(S-A-G-I-T-T-A-R-I-U-S). No other words, numbers, drawings, stickers, tags or logos on the card. "
          "FOREGROUND: at the bottom center of the frame, very close to the lens and softly out of focus, the top of a raw amethyst cluster with deep purple crystal points, filling only the "
          "bottom 10 percent of the frame. "
          "BACKGROUND (soft and slightly out of focus): a plain warm-beige wall; on the LEFT side of the image, behind her shoulder, a closed dark wooden door; on the RIGHT side of the image, "
          "behind her other shoulder, a small table lamp with a cream fabric shade glowing warm and, next to it, a small American flag (about 30 by 20 cm, on a short wooden stick) standing "
          "in a plain white ceramic mug. Nothing else: no other people, no pets, no posters, no signs, no logos and no readable text except the two lines on the card. "
          "LIGHT: warm tungsten lamp light from the right side of the image as the key light, the rest of the room dim and cozy; a realistic low-light phone photo with a little natural grain. "
          "FREE ZONES: the top 14 percent of the frame shows only the wall, the top of the door and the top of her hair. No date stamp, no watermark, no caption, no logo. "
          "Do not rejuvenate or smooth her face.")
V35 = ("Create a single continuous 8-second video clip that opens exactly on the first supplied frame and ends exactly on the last supplied frame (they are the same image), vertical 9:16. "
       "Handheld smartphone camera about 55 cm from the woman at the height of her collarbones, only a tiny natural sway, no zoom, no cuts, no reframing.\n\n"
       "THE MAIN EVENT: the woman, in a dim living room at night beside a warm table lamp, holds a white handwritten card with both hands just below her chin. She pushes the card toward "
       "the lens, holds it there, gives one slow nod, and brings it back. She never speaks.\n\n"
       "SECOND BY SECOND (something visible moves in EVERY second):\n"
       "0.0 to 1.0 s: both hands push the card straight toward the lens and slightly down, from about 35 cm to about 22 cm away, so it grows to about 90 percent of the frame width; "
       "the card stays flat, horizontal and facing the lens, its top edge stays below her chin and her eyes stay on the lens above it.\n"
       "1.0 to 2.5 s: she holds the card close and still; her eyebrows lower slightly in a serious, intense look.\n"
       "2.5 to 4.0 s: she gives one slow knowing nod with her lips closed while the card stays still.\n"
       "4.0 to 5.5 s: her eyes drop to the red line on the card for one moment and come back to the lens.\n"
       "5.5 to 7.0 s: both hands move the card back to its first-frame position just below her chin.\n"
       "7.0 to 8.0 s: she holds still with a faint closed-lip half-smile, exactly as in the last supplied frame.\n\n"
       "WHAT MUST NOT HAPPEN: she does not speak or mouth any words (her lips stay closed for the whole clip); the handwriting on the card never changes, moves, blurs, fades or gains "
       "or loses letters, and no new text appears anywhere; the card never bends, folds, flips, turns, tilts away or drops, and never covers her eyes or mouth; both hands stay on the "
       "card's side edges; each hand has exactly five fingers; the amethyst cluster at the bottom of the frame, the door, the lamp, the flag, the mug and the wall never move; no object, "
       "person or animal appears or disappears; the lamp light does not flicker.\n\n"
       "VISUAL: she is the same woman as in the supplied frames; realistic natural physics, no morphing, no glow, no magic effects. No added text, no logos.\n\n"
       "AUDIO: real quiet living-room sound only, with the faint rustle of the card. No music, no voice, no added sound effects.")
pk35 = {
  "roteiro": {"id": "nora35-TEXTO-NA-TELA-PLACA-ARIES-LEAO-SAGITARIO",
              "titulo": "Texto na tela: a placa de Áries, Leão e Sagitário (modelo M2)",
              "dor": "o amor que sempre termina do mesmo jeito (ângulo 01 da Appyon, padrões)",
              "formato": "Texto na tela, sem fala (clipe de 8 s): placa escrita à mão com os signos e as datas",
              "molde_hook": "viral M2 (placa “ARIES, LEO, SAGITARIUS” + datas, drusa de ametista desfocada na frente) + abertura do M2 “Don't you dare scroll past this” no texto do topo",
              "duracao_total": 8,
              "descricao_instagram": "Aries, Leo, Sagittarius: if this found you, it's not by chance. 🔮\nComment 222. Tap my photo NOW: a quick quiz builds your love chart.\n#astrology #zodiac #usa #usareels",
              "leitura_registro": LEITURA},
  "perfil": {"nome": "Nora", "teste": "A", "voz": VOZ},
  "refs": ["Blueprint da Nora v2 (a folha de consistência), só ele, na IMAGEM 1"],
  "trava_referencia": TRAVA, "figurino": FIG35,
  "excecao_estilo": "for the two handwritten lines on the white card",
  "ocultar_bloco_agente_imagem": True, "clipe_unico": True,
  "imagens": [{"rotulo": "IMAGEM 1", "cena": CENA35, "anexar": "só o blueprint da Nora v2 (a folha de consistência). Nenhuma outra imagem."}],
  "videos": [{"rotulo": "V1", "cena": "Clipe único · texto na tela (sem fala)", "duracao": 8, "primeiro_quadro": "IMAGEM 1", "acao": "(ver seção Clipe)", "b_roll": "",
              "fala": "(sem fala) texto na tela: " + HOOK35, "movimentacao": "(sem Central: o prompt do clipe está na seção Clipe)", "arquivo": "nora35-CLIPE-placa"}],
  "texto_tela": {"hook": HOOK35, "hook_comeca": "do segundo 0", "hook_termina": "o fim do clipe", "hook_alt": "", "extras": []},
  "comentario_fixado": pin("Aries, Leo, Sagittarius"),
  "pre_gancho": {"titulo_secao": "Clipe (8 s, sem fala, Frames)", "duracao": 8, "tomadas": 1, "com_rosto": True, "nome_video": "nora35-CLIPE-placa",
                 "conceito": "Cópia do viral M2: a Nora segura com as duas mãos uma placa escrita à mão com os signos em vermelho e as datas em preto, com uma drusa de ametista desfocada na frente. Ela não fala: empurra a placa até a lente, acena e volta.",
                 "modo": "Gere só depois da IMAGEM 1 aprovada (seção “Imagens”, logo abaixo) e do meu ok na grafia da placa. Um vídeo só, em FRAMES: primeiro e último quadro = nora35-IMG. 8 s, 9:16, áudio ligado. 12 créditos (conta de 437). Se o Flow recusar por política, não repita o texto: me mande o print.",
                 "etapas": [{"tipo": "vid", "titulo": "Clipe: ela empurra a placa até a lente e acena", "nome": "nora35-CLIPE-placa", "duracao": 8,
                             "quadros": "Modo FRAMES. Primeiro quadro: nora35-IMG. Último quadro: a mesma nora35-IMG. 8 s, 9:16, áudio ligado.", "prompt": V35}],
                 "montagem": "1) Use o clipe inteiro (8 s).\n2) Ponha os números fixos, o texto do topo e, dos 5 aos 8 s, o texto do story com a seta (seção de texto na tela).\n3) Música de sempre, −18 dB. Sem legenda na tela (ela não fala).\n4) Se a escrita da placa mudar, se ela mexer a boca ou se a placa cobrir o rosto, refaça uma vez; se falhar de novo, me chame.",
                 "texto_tela": "", "edicao": ""},
  "central": {"imagem_unica": True,
              "conferir": "Conferir: é a Nora da nora35-IMG; ela não fala; a escrita da placa não muda; a placa fica nas duas mãos e não cobre o rosto; a sala fica parada.",
              "passos": [
                  "Vídeo de 8 s SEM fala. Não usa a Central do curso nem o agente. Tudo na conta de 437.",
                  "IMAGEM 1 (seção “Imagens”, mais abaixo): no Flow, gere uma imagem 9:16 anexando SÓ o blueprint da Nora v2 e colando o prompt (botão “Copiar imagem com trava”). Aprove só se: é a Nora (lua e 3 estrelinhas no lado esquerdo da imagem); a placa diz exatamente ARIES, LEO, SAGITTARIUS (vermelho) e 26, 27 AND 28 OF OCTOBER (preto), sem outra palavra; as duas mãos nas bordas da placa; cinco dedos; sem carimbo de data. Se a grafia sair errada, gere de novo (imagem não gasta crédito). Renomeie para nora35-IMG e me mande.",
                  "Depois do meu ok: o clipe (seção “Clipe”) em FRAMES, primeiro e último quadro = nora35-IMG, 8 s, 9:16, áudio ligado. Renomeie para nora35-CLIPE-placa. 12 créditos.",
                  "CapCut: números fixos, texto do topo, texto do story com a seta (dos 5 aos 8 s) e a música de sempre (−18 dB). Sem legenda na tela e sem corte de silêncio: a Nora não fala.",
                  "Postar em 26/10 às 21h no Insta e no Face, com a localização Los Angeles, California no Insta (se não for estar online, programe no próprio app do Insta). O story do dia tem de estar no ar."],
              "config": [], "agente": {}, "colagens": [{"titulo": "clipe sem fala", "fala": "(sem fala)", "movimentacao": ["(sem fala)"], "takes": [0]}]},
  "story": copy.deepcopy(STORY),
  "edicao_linha": [
      {"quando": "1. O clipe todo (8 s)", "texto": HOOK35, "como": "Texto no topo, em 3 linhas, do segundo 0 ao fim do clipe. A 1ª frase (“Don't you dare scroll past this.”) em amarelo-ouro; o resto branco."},
      {"quando": "2. O clipe todo", "texto": "222  e  11:11", "como": "Números fixos nos cantos de cima, em amarelo-ouro: 222 à esquerda e 11:11 à direita."},
      {"quando": "3. Dos 5 aos 8 s", "texto": "Your love chart quiz is in my story  +  seta vermelha", "como": "Texto do story: branco, tamanho 9, em 1 linha, logo abaixo da placa (faixa verde do mapa da tela). Junto, a seta vermelha embaixo à esquerda, apontando para baixo, para a foto do perfil."},
      {"quando": "4. O clipe todo", "texto": "Música de sempre, −18 dB", "como": "Sem legenda na tela (ela não fala) e sem corte de silêncio."}],
  "mapa_tela": mapa([70, 77], "Texto do story (dos 5 aos 8 s)", "STORY", [
      EST_NUM,
      {"nome": "Texto do topo (o clipe todo)", "fonte": "Poppins Bold (poppins-bd)", "cor": "branco #FFFFFF; a 1ª frase em amarelo-ouro #FFD21F", "tamanho": "12",
       "contorno": "Traço preto + Sombra preta, sem Plano de fundo. Luz DESLIGADA", "obs": "Centralizado, em 3 linhas, do segundo 0 ao fim do clipe."},
      {"nome": "Texto do story (dos 5 aos 8 s): “Your love chart quiz is in my story”", "fonte": "Poppins Bold (poppins-bd)", "cor": "branco #FFFFFF", "tamanho": "9, em 1 linha",
       "contorno": "Traço preto + Sombra preta, sem Plano de fundo. Luz DESLIGADA", "obs": "Centralizado, logo abaixo da placa (faixa verde)."},
      est_seta("Dos 5 aos 8 s, junto com o texto do story")],
      ["Este vídeo não tem fala, então não tem legenda na tela. São 4 textos: os números fixos e o texto do topo (o clipe todo) e, dos 5 aos 8 s, o texto do story na faixa verde e a seta vermelha embaixo à esquerda.",
       "A faixa verde (70% a 77%) é provisória: eu confirmo quando você me mandar a nora35-IMG. Nada em cima do rosto, da placa ou das mãos.",
       "Confira o quadro dos 5 s: se o texto do story tocar a placa, comece o texto e a seta aos 6 s."]),
  "pecas": {"lista": [
      {"nome": "nora35-IMG", "tipo": "imagem 1", "status": "gerar", "descricao": "A Nora de blazer esmeralda, à noite, com a placa escrita à mão (signos em vermelho, datas em preto) e a ametista desfocada na frente.",
       "base": "Viral M2 (placa dos signos com as datas, drusa de ametista na frente, sala escura com abajur).", "serve": "Outros textos na tela da série (outra placa = outra imagem)."},
      {"nome": "nora35-CLIPE-placa", "tipo": "clipe sem fala", "status": "gerar", "creditos": 12, "descricao": "8 s: ela empurra a placa até a lente, acena e volta.",
       "base": "Texto na tela (nora31 e nora33: os maiores do Insta) + placa do M2.", "serve": "Face: versões -ESP e -VEL."}],
      "decisao": ["Texto na tela: o formato com mais views no Insta (nora33 195, nora31 145).",
                  "Placa do M2 (Matheus): os signos escritos à mão param quem é desses signos; as datas são de quando ela vê o vídeo (P39).",
                  "Áries, Leão e Sagitário: o grupo que faltava hoje (nora34 Gêmeos/Libra/Aquário, nora36 Touro/Virgem/Capricórnio, nora37 Câncer/Escorpião/Peixes)."]}}

# ================================================================= nora36 (21h): geodo, 10 takes
F36 = [
 "Taurus, Virgo or Capricorn: if this reached you on October 26th, 27th or 28th, it's meant for you. Don't tell anyone.",
 "I don't know your name or what you've been through, but I can see the pattern you keep repeating in love.",
 "You know something's off in love, but you can't say what. And I see a cycle opening that favors new connections.",
 "If you scroll past this, you'll live the same story again with a different man. So take this seriously.",
 "In astrology, your sun sign isn't the problem. Your Venus, your Moon and your 7th house decide who you keep choosing.",
 "When they clash, you fall for the wrong man and blame yourself. It's not bad luck. It's a pattern.",
 "Imagine finally understanding why, before you give another year to someone who doesn't fit you. Send this video to yourself now.",
 "Now save this video, that will be your first seal. Double tap quickly on your screen, that will be your second seal.",
 "Comment 222 so I can see you did everything. Then tap my profile picture and check my stories before they disappear.",
 "The second part is waiting there: a quick quiz that reads your love chart and shows what kind of partner fits you.",
]
N36 = ["T01-gancho-touro-virgem-capricornio", "T02-corpo-nao-sei-seu-nome", "T03-corpo-algo-errado-ciclo", "T04-corpo-mesma-historia", "T05-corpo-venus-lua-casa-7",
       "T06-corpo-nao-e-azar", "T07-corpo-imagine-mande", "T08-cta-selos", "T09-cta-222-story", "T10-cta-quiz-mapa"]
T36 = ["Gancho (signos e datas)", "Não sei o seu nome + o padrão", "Algo errado + o ciclo", "A mesma história (ameaça, uma vez)", "Vênus, Lua e casa 7 (a prova)",
       "Não é azar", "Imagine + mande para si", "Os dois selos", "222 e o story", "O que tem no story (o quiz)"]
BASE36 = ("Throughout the whole 10 seconds both of her hands keep holding the two open halves of the gray geode at the height of her collarbones with their pink crystal insides facing the lens, "
          "her right hand on the left side of the frame holding the left half and her left hand on the right side of the frame holding the right half with the small gold symbol, "
          "and the halves never change hands, never close, never turn away, never drop and never cover her face, both hands stay on the halves with no other gestures, her eyes stay on the lens, and ")
G36 = [
 "during the first sentence of the take she holds a firm, serious look with her brows slightly lowered, during the last sentence she gives one short slow nod",
 "during the first half of the take she tilts her head slightly to one side with a soft understanding look, during the second half she slowly straightens her head and narrows her eyes a little as if reading something",
 "during the first sentence of the take she raises her eyebrows slightly, during the second sentence her eyes drop to the open halves for one moment and come back to the lens",
 "during the first sentence of the take her face turns serious and she leans her head and shoulders a little toward the lens, during the last sentence she slowly leans back to her first position",
 "during the first sentence of the take she brings both open halves about 8 centimeters closer to the lens, keeping them apart and facing the lens, during the second sentence she slowly brings them back to their first position",
 "during the first sentence of the take she gives one slow head shake, during the last two short sentences she holds a calm, steady look",
 "during the first sentence of the take she takes one slow breath and her shoulders drop slightly with a soft half-smile, during the last sentence she gives one short nod",
 "during the first sentence of the take she gives one short nod, during the last sentence she gives a second short nod",
 "during the first sentence of the take her eyes drop to the open halves for one moment and come back to the lens, during the last sentence she holds a warm, steady look",
 "during the whole take she keeps a warm, soft half-smile while speaking, and during the last sentence she raises both open halves about 5 centimeters and holds them there",
]
MOV36 = [BASE36 + g + FIM_MOV for g in G36]
FIG36 = ("fortune-teller, subtle mystic; plain black fine ribbed knit top with a round crew neckline and long fitted sleeves, smooth matte finish, no print, embroidery, logo or shine. "
         "Clothing is secondary to the contrast of the pale-pink rose quartz inside the geode. Fixed accessories, always visible: the long gold star-and-moon drop earrings, the long thin "
         "gold chain with the small gold Venus-symbol pendant, thin gold bracelets on her left wrist, a small gold sun-symbol ring on her right index finger and the gold face gems from the "
         "reference sheet; no flag pin, no other jewelry, turban, cape or costume")
CENA36A = ("Vertical 9:16 close-up photo of the woman from the attached reference sheet in a real American bedroom at night. "
           "FRAMING: from the top of her head down to just below her collarbones; her knees, legs, the bed and the floor are NOT in the frame. "
           "The camera is a handheld phone at the height of her collarbones, about 55 cm in front of her, level, no tilt. "
           "Her face is large and centered in the upper half of the frame, with her eyes at about 30 percent of the frame height. "
           "HANDS AND STONE: with BOTH hands she squeezes one closed, rough, egg-shaped stone about 13 cm tall and 10 cm wide, held upright in the center of the frame at the height of her "
           "collarbones, about 25 cm from the lens, its top just below her chin at about 46 percent of the frame height and its bottom at about 66 percent. Her RIGHT hand (the hand on the "
           "LEFT side of the image) grips the stone's left side and her LEFT hand (the hand on the RIGHT side of the image) grips its right side, fingers wrapped around it and both thumbs "
           "pressing on its front, knuckles tense, elbows bent close to her body; the small gold sun ring is on her right index finger and the thin gold bracelets are on her left wrist; "
           "each hand has exactly five fingers with natural proportions. "
           "THE STONE: a natural uncut geode, matte light-gray rough rock with darker gray speckles and a slightly bumpy surface, completely closed: no crack, no opening, no crystal and no "
           "color visible yet; it never covers her face. "
           "HER FACE: strong effort, brows pulled together, eyes on the lens, jaw clenched, lips pressed together. "
           "BACKGROUND (soft and slightly out of focus): a plain light-cream wall; on the LEFT side of the image, behind her shoulder, a small American flag about 30 cm wide pinned flat to "
           "the wall; on the RIGHT side of the image, behind her other shoulder, a small bedside lamp with a pink fabric shade glowing a warm pink. Nothing else: no other people, no pets, "
           "no posters, no signs, no logos, no readable text. "
           "LIGHT: the room is dim; the warm pink lamp light from the right side of the image is the key light and tints her skin and the wall softly pink; a realistic low-light phone photo "
           "with a little natural grain. FREE ZONES: the top 14 percent of the frame shows only the wall and the top of her hair. "
           "No dust, no glow, no sparkles, no date stamp, no watermark, no caption, no logo. Do not rejuvenate or smooth her face.")
P36_B = ("EDIT of the attached image (use it as the base image): keep exactly the same woman, the same face, hazel-green eyes, very long black wavy hair with the gold-ringed braid, "
         "the gold moon and star face gems, the star-and-moon earrings, the Venus necklace, the gold sun ring, the thin gold bracelets, the plain black ribbed top, the same bedroom wall, "
         "the same small American flag, the same pink lamp, the same dim pink light and the same framing. Changes: the gray stone has split open into two halves. Her RIGHT hand "
         "(on the LEFT side of the image) holds the left half and her LEFT hand (on the RIGHT side of the image) holds the right half; the halves are pulled about 10 cm apart, still at the "
         "height of her collarbones and about 25 cm from the lens, each with its open inner face turned toward the lens. The outside of each half is the same light-gray rough rock. "
         "The inside of each half is a hollow lined with dense, sparkling, translucent pale-pink rose quartz crystal points inside a thin white rim. In the center of the RIGHT half "
         "(in her left hand, on the RIGHT side of the image), resting among the pink crystals, there is one small flat polished gold Venus symbol about 2 cm tall (a small circle with a "
         "short cross below it), facing the lens. A few tiny gray rock flakes and a little fine gray dust are falling below the halves. Her face shows amazed surprise: eyebrows raised, "
         "eyes wide and on the lens, lips slightly parted; she is not speaking. The pink crystals and the gold symbol are in sharp focus and are the point of highest contrast against the "
         "black top. Each hand has exactly five fingers. No glow, no light rays, no sparkles floating in the air, no other gold object, no letters, no text, no logo and no date stamp. "
         "Change nothing else.")
CENA36IMG = ("EDIT of the attached image (use it as the base image): keep exactly the same woman, face, hair, braid, face gems, earrings, necklace, ring, bracelets and black top, the same "
             "two open geode halves in the same hands at the same height and distance, with the pink rose quartz crystals and the small gold Venus symbol in the right half (on the RIGHT "
             "side of the image), the same bedroom wall, flag, pink lamp, light and framing. Changes: remove all falling dust and rock flakes; her expression is now calm and knowing: "
             "eyebrows relaxed, an intense, direct gaze into the lens, lips closed in a faint knowing half-smile. Each hand has exactly five fingers. No text, no logo, no date stamp. "
             "Change nothing else.")
P36_V = ("Create a single continuous 4-second video clip that opens exactly on the first supplied frame and ends exactly on the last supplied frame, vertical 9:16. "
         "Handheld smartphone camera about 55 cm from the woman at the height of her collarbones, only a tiny natural shake, no zoom, no cuts, no reframing.\n\n"
         "THE MAIN EVENT: in a dim bedroom at night lit by a pink lamp, the woman squeezes a closed, gray, egg-shaped geode with both hands until it cracks and splits into two halves "
         "that show pale-pink rose quartz crystals inside, with a small gold Venus symbol among the crystals of the right half. In the first frame the stone is closed, in the center of "
         "the frame at the height of her collarbones, her right hand (on the left side of the image) on its left side and her left hand (on the right side of the image) on its right side, "
         "and her face already shows effort. She never speaks.\n\n"
         "SECOND BY SECOND (something visible moves in EVERY second):\n"
         "0.0 to 1.0 s: she squeezes harder; her knuckles tighten, her brows pull together, her shoulders tense and the stone trembles slightly in her grip.\n"
         "1.0 to 2.0 s: one thin dark crack runs from the top of the stone down its front; a small puff of fine gray dust comes out of the crack.\n"
         "2.0 to 3.0 s: with a sharp snap the stone splits along the crack; her hands pull the two halves apart sideways, about 10 cm, and turn their open faces toward the lens, "
         "showing the sparkling pink crystals and the small gold symbol in the right half; tiny gray flakes and dust fall below the halves.\n"
         "3.0 to 4.0 s: she holds both halves still, open toward the lens, with her eyebrows raised in amazed surprise, exactly as in the last supplied frame.\n\n"
         "WHAT MUST NOT HAPPEN: the stone does not crack, open or show any crystal before 1.0 second; there are exactly two halves (no third piece, no crumbling into many pieces); "
         "the halves never vanish, float, merge back together or change hands; the gold symbol appears only when the stone opens and then stays in the right half; no glow, light rays, "
         "sparkles in the air or magic effects; the crystals stay pale pink; she does not speak or mouth any words; her face is never covered; each hand keeps exactly five fingers; "
         "the wall, the flag and the lamp never move; no object, person or animal appears or disappears.\n\n"
         "VISUAL: she is the same woman as in the supplied frames; realistic natural physics of rock cracking, no morphing. No text, no logos.\n\n"
         "AUDIO: real ambient sound only: the dry crack and snap of the stone and a faint sprinkle of falling grit, in a quiet room. No music, no voice, no added sound effects.")
LIVRE36 = ("Casual handheld smartphone video in a dim real American bedroom at night, lit by a small pink bedside lamp. "
           "CONTINUITY LOCKS for every take: the woman, her face, her long black wavy hair, her braid with gold rings, her gold moon and star face gems, her star-and-moon earrings, "
           "her Venus necklace, her thin gold bracelets, her gold ring and her plain black ribbed top stay exactly as in the reference image; she is framed from the top of her head to "
           "just below her collarbones, with her face large and centered in the upper half of the frame; both hands hold the two open halves of the gray geode at the height of her "
           "collarbones with the pink crystal insides facing the lens for the whole clip, her right hand on the left side of the frame and her left hand on the right side of the frame "
           "holding the half with the small gold symbol; the halves never change hands, never close, never join, never turn away, never drop and never cover her face, and the gold symbol "
           "never moves or disappears; there are no other hand gestures; the camera is a handheld phone at the height of her collarbones about 55 centimeters from her with only a tiny "
           "natural sway, no zoom, no cuts and no reframing; the cream wall, the small American flag and the pink lamp stay exactly where they are and never move; no dust, no glow and "
           "no sparkles; no object, person, animal or text appears or disappears; each hand always has exactly five fingers; no on-screen text, no captions, no logos; real quiet bedroom "
           "ambient sound only, no music. "
           "SPEECH RULE for every take: she says only the exact words of that take's script, each word exactly once and in order, with no repeated word, no extra word and no added "
           "sentence before, between or after; when she finishes the last word she closes her lips, stays silent and keeps a calm still expression until the clip ends.")
CFG36 = config_com_livre(LIVRE36)

def videos_de(prefixo, falas, movs, nomes, titulos, n_total):
    return [{"rotulo": "V%d" % (i + 1), "cena": "Take %d/%d · %s" % (i + 1, n_total, titulos[i]), "duracao": 10, "primeiro_quadro": "IMAGEM 1",
             "acao": "(ver movimentação)", "b_roll": "", "fala": falas[i], "movimentacao": movs[i], "arquivo": prefixo + '-' + nomes[i]} for i in range(len(falas))]

def edicao_serie(signos, nome_pre):
    return [
        {"quando": "0. Antes do Take 1", "texto": "Pré-gancho (" + nome_pre + ", uns 3,5 s)", "como": "Corte seco para o corpo cortado. Veja a montagem na seção do pré-gancho."},
        {"quando": "1. Do primeiro quadro do pré-gancho até o fim do Take 1", "texto": signos + ", pay very close attention",
         "como": "Caixa branca arredondada no topo (X 0 · Y 397), texto preto, a palavra “attention” em vermelho. Igual em todos os vídeos da série."},
        {"quando": "2. Do Take 1 ao fim", "texto": "Legenda na tela (automática), em blocos de 2 a 4 palavras", "como": "Faixa verde do mapa. Destaque em amarelo-ouro: pattern, Venus, Moon, 7th house e quiz."},
        {"quando": "3. Do Take 8 até o fim", "texto": "Your love chart quiz is in my Stories ⭐", "como": "Faixa no topo, no mesmo lugar da caixa (X 0 · Y 397): caixa branca arredondada, texto preto, “my Stories” em vermelho. Começa em “Now save this video”."},
        {"quando": "4. Nos Takes 9 e 10", "texto": "Seta vermelha", "como": "Embaixo à esquerda, apontando para baixo, para a foto do perfil, do “Comment 222” até o fim."},
        {"quando": "5. O vídeo todo", "texto": "Música de sempre, −18 dB", "como": "Sem números fixos (os virais da série não usam)."}]

def mapa_serie(signos, img):
    return mapa([69, 77], None, None, [est_caixa(signos), EST_LEG, EST_FAIXA, est_seta("Nos Takes 9 e 10")],
                ["Sem números fixos neste vídeo: a faixa azul do mapa fica vazia.",
                 "A faixa da legenda (69% a 77%, logo abaixo das metades do geodo) é provisória: eu confirmo quando você me mandar a " + img + ".",
                 "Nada nas faixas vermelhas nem em cima do rosto, das mãos ou do geodo. Se a legenda tocar o geodo, desça no máximo até 77%."])

pk36 = {
  "roteiro": {"id": "nora36-GEODO-TOURO-VIRGEM-CAPRICORNIO",
              "titulo": "Série do geodo: Touro, Virgem e Capricórnio (cópia fiel do corpo A, promessas do Love Chart)",
              "dor": "repetir o mesmo padrão no amor sem saber por quê (ângulo 01 da Appyon, padrões)",
              "formato": "Hook visual pesado (geodo que racha, 4 s) + copy falada de 10 takes (corpo A dos virais)",
              "molde_hook": "viral x1/x2/x5 (geodo que racha) + corpo A dos x1/x2/x3/x5 e do @antoiinehayes (a2, a3); caixa do topo “[signos], pay very close attention”",
              "duracao_total": 75,
              "descricao_instagram": "Taurus, Virgo, Capricorn: if this reached you, it's meant for you. 🔮\nComment 222. Tap my photo NOW: a quick quiz reads your love chart.\n#astrology #zodiac #usa #usareels",
              "leitura_registro": LEITURA},
  "perfil": {"nome": "Nora", "teste": "A", "voz": VOZ},
  "refs": ["Blueprint da Nora v2 (a folha de consistência), só na nora36-PRE-A"],
  "trava_referencia": TRAVA, "figurino": FIG36, "excecao_estilo": "", "ocultar_bloco_agente_imagem": True,
  "imagens": [{"rotulo": "IMAGEM 1", "cena": CENA36IMG, "anexar": "SÓ a nora36-PRE-B aprovada (é uma edição dela). Nenhuma outra imagem."}],
  "videos": videos_de("nora36", F36, MOV36, N36, T36, 10),
  "texto_tela": {"hook": "Taurus, Virgo, Capricorn, pay very close attention", "hook_comeca": "o primeiro quadro do pré-gancho", "hook_termina": "Don't tell anyone", "hook_alt": "", "extras": []},
  "comentario_fixado": pin("Taurus, Virgo, Capricorn"),
  "pre_gancho": {"titulo_secao": "Pré-gancho (4 s, o geodo que racha, com o rosto da Nora)", "duracao": 4, "tomadas": 1, "com_rosto": True,
                 "conceito": "Cópia dos virais x1, x2 e x5: ela aperta com as duas mãos uma pedra cinza em forma de ovo, a pedra trinca, estala e abre em duas metades com quartzo rosa e um pequeno símbolo de Vênus dourado por dentro. A imagem do vídeo (nora36-IMG) é a continuação, com o rosto calmo.",
                 "modo": "Tudo na conta de 437. Gere a A (anexe SÓ o blueprint), a B (anexe SÓ a A) e a nora36-IMG (seção “Imagens”, anexe SÓ a B). Me mande as 3 juntas. Depois do meu ok, o vídeo em FRAMES: primeiro quadro = nora36-PRE-A, último quadro = nora36-PRE-B, 4 s, 9:16, áudio ligado. 7 créditos.",
                 "etapas": [
                     {"tipo": "img", "titulo": "Imagem A: a pedra fechada, ela fazendo força", "nome": "nora36-PRE-A", "anexar": "SÓ o blueprint da Nora v2 (a folha de consistência)", "prompt": img_com_trava(FIG36, CENA36A)},
                     {"tipo": "img", "titulo": "Imagem B: o geodo aberto, quartzo rosa e o símbolo de Vênus", "nome": "nora36-PRE-B", "anexar": "SÓ a nora36-PRE-A aprovada (é uma edição dela)", "prompt": P36_B},
                     {"tipo": "vid", "titulo": "Vídeo: o geodo racha e abre", "nome": "nora36-PRE", "duracao": 4,
                      "quadros": "Modo FRAMES. Primeiro quadro: nora36-PRE-A. Último quadro: nora36-PRE-B. 4 s, 9:16, áudio ligado.", "prompt": P36_V}],
                 "montagem": "1) nora36-PRE: uns 3,5 s (corte logo depois que as metades abrem).\n2) Corte seco para o corpo cortado (nora36-cortado).\n3) A caixa do topo já entra no primeiro quadro do pré-gancho.\nPlano B, se o Flow deformar a pedra: PRE-A por 1 s e PRE-B por 1,5 s como fotos, com zoom leve (100% a 106%), 0 crédito.",
                 "texto_tela": "", "edicao": ""},
  "central": {"imagem_unica": True,
              "conferir": "Conferir em cada vídeo: é a Nora v2 (rosto, lua com as estrelinhas, trança e blusa preta iguais à imagem); as duas metades do geodo ficam nas mesmas mãos, abertas, com o símbolo dourado na metade da direita da imagem; sem poeira; a fala sai completa, uma vez só, em inglês; sem texto, legenda ou música. Renomeie com o nome da lista.",
              "passos": [
                  "Pré-gancho e imagem (seção “Pré-gancho” e seção “Imagens”), na conta de 437: gere a nora36-PRE-A (anexe SÓ o blueprint), a nora36-PRE-B (anexe SÓ a A) e a nora36-IMG (anexe SÓ a B). Imagem não gasta crédito. Me mande as 3 juntas.",
                  "Depois do meu ok: o vídeo do pré-gancho em FRAMES (A → B), 4 s. 7 créditos. Renomeie para nora36-PRE. As linhas de movimentação de agora são provisórias: eu confirmo com a nora36-IMG.",
                  "Central do curso: a configuração (seção “Central do curso”, com o texto LIVRE novo) e a colagem única (fala inteira + 10 linhas). Confira: 10 takes de 10 s.",
                  "Agente do Flow: anexe só a nora36-IMG, cole o aviso e o “COPIAR TUDO JUNTO” da Central, sem editar. 150 créditos. Renomeie os takes com os nomes do painel. Guarde os takes 2 a 10 separados: o nora37 usa as cópias.",
                  "Me mande a transcrição dos 10 takes antes de postar.",
                  "Corte de silêncio só do corpo (seção “Cortar os silêncios”): suba os 10 takes de uma vez, com “Juntar tudo” ligado e Corte seco. CapCut: pré-gancho, corpo cortado, caixa do topo (desde o pré-gancho), legenda na tela, faixa do story (do Take 8 ao fim), seta vermelha (Takes 9 e 10) e a música de sempre (−18 dB).",
                  "Postar em 26/10 às 23h no Insta e no Face, com a localização Los Angeles, California no Insta (se não for estar online, programe no próprio app do Insta). Se não ficar pronto, vai para 27/10 às 19h: me avise antes de gerar, porque as datas do Take 1 mudam."],
              "config": CFG36, "agente": agente_n("nora36-IMG", 10),
              "colagens": [{"titulo": "nora36 completo (10 takes)", "fala": " ".join(F36), "movimentacao": MOV36, "takes": list(range(10))}]},
  "story": copy.deepcopy(STORY),
  "edicao_linha": edicao_serie("Taurus, Virgo, Capricorn", "nora36-PRE"),
  "mapa_tela": mapa_serie("Taurus, Virgo, Capricorn", "nora36-IMG"),
  "pecas": {"lista": [
      {"nome": "nora36-PRE-A", "tipo": "imagem do pré-gancho", "status": "gerar", "descricao": "Primeiro quadro: a pedra cinza fechada nas duas mãos, ela fazendo força (do blueprint).",
       "base": "Virais x1, x2 e x5 (e w4, M1): o primeiro quadro já é a pedra apertada.", "serve": "Só deste kit."},
      {"nome": "nora36-PRE-B", "tipo": "imagem do pré-gancho", "status": "gerar", "descricao": "Último quadro: as metades abertas, quartzo rosa e o símbolo de Vênus dourado (edição da A)."},
      {"nome": "nora36-PRE", "tipo": "vídeo do pré-gancho", "status": "gerar", "creditos": 7, "descricao": "4 s em Frames: o geodo trinca, estala e abre.",
       "base": "O mesmo clipe dos x1 e x2 (o x2 é ele espelhado).", "serve": "nora37 (espelhado) e os próximos da série; no Face, colado em outros corpos."},
      {"nome": "nora36-IMG", "tipo": "imagem 1", "status": "gerar", "descricao": "As metades abertas, sem poeira, rosto calmo (edição da B). Primeiro e último quadro dos 10 takes.",
       "base": "Continuação do pré-gancho (P26).", "serve": "Todos os Takes 1 da série (nora37 e os próximos)."}]
      + [{"nome": "nora36-" + N36[i], "tipo": ("gancho" if i == 0 else ("CTA" if i >= 7 else "corpo")), "status": "gerar", "creditos": 15,
          "descricao": "Take %d: “%s”" % (i + 1, F36[i]),
          "base": ("Corpo A dos virais, frase %d, com as promessas do Love Chart (P39/P40)." % (i + 1)),
          "serve": ("Só deste vídeo (cada grupo de signos tem o seu Take 1)." if i == 0 else "nora37 e os próximos da série (cópia renomeada).")} for i in range(10)],
      "decisao": ["Cópia fiel do corpo A (aluno: “Fiel, promessas do Love Chart”): o molde da conta de 173 mil (157 mil e 127 mil views).",
                  "Hook visual pesado: o geodo que racha (3 de 5 vídeos da conta dos x).",
                  "Corpo gerado uma vez: o nora37 (01h de 27/10) e os próximos só trocam o Take 1."],
      "proximos_intro": "Mesma nora36-IMG, só o Take 1 novo (15 créditos cada), pré-gancho espelhado um sim, um não.",
      "proximos": [
          {"nome": "nora37-T01-gancho-cancer-escorpiao-peixes", "modelo": "x2 (espelhado)", "custo": "15", "gancho": "Cancer, Scorpio or Pisces: if this reached you on October 26th, 27th or 28th, it's meant for you. Don't tell anyone.", "texto": "Cancer, Scorpio, Pisces, pay very close attention"},
          {"nome": "noraNN-T01-gancho-aries-leao-sagitario", "modelo": "x1", "custo": "15", "gancho": "Aries, Leo or Sagittarius: if this reached you on October 27th, 28th or 29th, it's meant for you. Don't tell anyone.", "texto": "Aries, Leo, Sagittarius, pay very close attention"},
          {"nome": "noraNN-T01-gancho-gemeos-libra-aquario", "modelo": "x2 (espelhado)", "custo": "15", "gancho": "Gemini, Libra or Aquarius: if this reached you on October 27th, 28th or 29th, it's meant for you. Don't tell anyone.", "texto": "Gemini, Libra, Aquarius, pay very close attention"}]}}

# ================================================================= nora37 (23h): série, só o Take 1
F37 = "Cancer, Scorpio or Pisces: if this reached you on October 26th, 27th or 28th, it's meant for you. Don't tell anyone."
N37_T1 = "nora37-T01-gancho-cancer-escorpiao-peixes"
pk37 = {
  "roteiro": {"id": "nora37-GEODO-CANCER-ESCORPIAO-PEIXES",
              "titulo": "Série do geodo: Câncer, Escorpião e Peixes (só o Take 1 novo)",
              "dor": "repetir o mesmo padrão no amor sem saber por quê (ângulo 01 da Appyon, padrões)",
              "formato": "Série: pré-gancho do nora36 espelhado + Take 1 novo + Takes 2 a 10 do nora36",
              "molde_hook": "viral x2 (o mesmo clipe do geodo do x1, espelhado, com outros signos e o mesmo corpo A)",
              "duracao_total": 75,
              "descricao_instagram": "Cancer, Scorpio, Pisces: if this reached you, it's meant for you. 🔮\nComment 222. Tap my photo NOW: a quick quiz reads your love chart.\n#astrology #zodiac #usa #usareels",
              "leitura_registro": LEITURA},
  "perfil": {"nome": "Nora", "teste": "A", "voz": VOZ},
  "refs": ["Nenhuma imagem nova: a nora36-IMG"],
  "trava_referencia": TRAVA, "figurino": FIG36, "excecao_estilo": "",
  "imagem_reutilizada": {"arquivo": "nora36-IMG (a imagem dos takes do nora36)", "aviso": "O Take 1 usa a nora36-IMG, a mesma dos takes 2 a 10 (as metades do geodo, rosto calmo). Não gere imagem nova."},
  "imagens": [{"rotulo": "IMAGEM 1", "cena": "(a nora36-IMG, não gerar)"}],
  "videos": [{"rotulo": "V1", "cena": "Take 1/10 · Gancho (Câncer, Escorpião e Peixes)", "duracao": 10, "primeiro_quadro": "IMAGEM 1", "acao": "(ver movimentação)", "b_roll": "",
              "fala": F37, "movimentacao": MOV36[0], "arquivo": N37_T1}],
  "texto_tela": {"hook": "Cancer, Scorpio, Pisces, pay very close attention", "hook_comeca": "o primeiro quadro do pré-gancho", "hook_termina": "Don't tell anyone", "hook_alt": "", "extras": []},
  "comentario_fixado": pin("Cancer, Scorpio, Pisces"),
  "pre_gancho": {"titulo_secao": "Pré-gancho (o do nora36, espelhado: não gerar)", "duracao": 4, "tomadas": 1, "com_rosto": True,
                 "conceito": "Cópia do viral x2: o mesmo clipe do geodo do nora36, espelhado (como a conta dos x faz do x1 para o x2).",
                 "modo": "Não gere nada aqui. No CapCut, use a nora36-PRE e espelhe só esse clipe (Editar → Espelhar). O corpo NÃO é espelhado.",
                 "etapas": [],
                 "montagem": "1) nora36-PRE espelhado: uns 3,5 s.\n2) Corte seco para o corpo cortado (nora37-cortado: o Take 1 novo + as cópias dos takes 2 a 10).\n3) A caixa do topo já entra no primeiro quadro do pré-gancho.",
                 "texto_tela": "", "edicao": ""},
  "central": {"imagem_unica": True,
              "conferir": "Conferir: é a Nora da nora36-IMG; as metades do geodo nas mesmas mãos; a fala sai completa, uma vez só, com a mesma voz dos takes do nora36. Ouça a emenda do Take 1 com o Take 2.",
              "passos": [
                  "Imagem: não gere. O Take 1 usa a nora36-IMG (conta de 437).",
                  "Central do curso: a MESMA configuração do nora36 (seção “Central do curso”, com o texto LIVRE do nora36). Cole só a fala do Take 1 e a linha de movimentação dele. Clique em GERAR PROMPT DE ANIMAÇÃO e confira: 1 take de 10 s.",
                  "Agente do Flow: anexe a nora36-IMG (só ela), cole o aviso e, embaixo, o prompt do Take 1 (botão COPIAR do take). 15 créditos. Renomeie para " + N37_T1 + ".",
                  "Os takes 2 a 10 NÃO são gerados: são os do nora36 (lista em “Nomes e reaproveitamento”). Faça uma cópia de cada um e renomeie de nora36-T02… para nora37-T02… (a ferramenta de corte junta pela ordem do nome; por isso os números têm 2 dígitos).",
                  "Me mande a transcrição do Take 1 e a emenda com o Take 2 antes de postar.",
                  "Corte de silêncio (seção “Cortar os silêncios”): suba nora37-T01 a nora37-T10 de uma vez, com “Juntar tudo” ligado e Corte seco. CapCut: pré-gancho espelhado, corpo cortado e os textos da seção de texto na tela.",
                  "Postar em 27/10 à 01h no Insta e no Face, com a localização Los Angeles, California no Insta (se não for estar online, programe no próprio app do Insta). É o teste de variação no Insta (no lugar do -ESP): mesmo corpo do nora36, hook e signos novos."],
              "config": CFG36, "agente": agente_1("nora36-IMG", N37_T1),
              "colagens": [{"titulo": "só o Take 1", "fala": F37, "movimentacao": [MOV36[0]], "takes": [0]}]},
  "story": copy.deepcopy(STORY),
  "edicao_linha": edicao_serie("Cancer, Scorpio, Pisces", "nora36-PRE espelhado"),
  "mapa_tela": mapa_serie("Cancer, Scorpio, Pisces", "nora36-IMG"),
  "pecas": {"lista": [
      {"nome": "nora36-PRE", "de": "nora36-PRE", "tipo": "pré-gancho (do nora36)", "status": "reutilizar", "creditos": 7, "descricao": "Espelhado no CapCut, como o x2."},
      {"nome": "nora36-IMG", "de": "nora36-IMG", "tipo": "imagem 1 (do nora36)", "status": "reutilizar", "descricao": "Primeiro e último quadro do Take 1, a mesma dos takes 2 a 10."},
      {"nome": N37_T1, "tipo": "gancho", "status": "gerar", "creditos": 15, "descricao": "Take 1: “" + F37 + "”",
       "base": "Take 1 da série (corpo A: signos + datas em que ela vê o vídeo + segredo).", "serve": "Só deste vídeo."}]
      + [{"nome": "nora36-" + N36[i], "de": "nora36-" + N36[i], "tipo": ("CTA" if i >= 7 else "corpo") + " (do nora36)", "status": "reutilizar", "creditos": 15,
          "fala": F36[i], "descricao": "Para a ferramenta de corte, renomeie a cópia para nora37-" + N36[i] + "."} for i in range(1, 10)],
      "decisao": ["Série do geodo (x1 → x2): mesmo corpo e mesmo clipe de hook espelhado, outros signos. A conta dos x posta assim no mesmo dia (x2 e x3).",
                  "À 01h é o teste de variação no Insta (Lucas): compara com o nora36 das 23h."]}}

STORY2 = copy.deepcopy(STORY)
STORY2['nota'] = 'O story de hoje (26/10, 18h20) já está no ar e vale para este vídeo: não precisa postar outro.'
for _p in (pk35, pk36, pk37): _p['story'] = copy.deepcopy(STORY2)
PACOTES = {'34': pk34, '35': pk35, '36': pk36, '37': pk37}

# ================================================================= checagens
def wc(s): return len(s.split())
def simula(falas):
    sents = []
    for f in falas:
        sents += [x.strip() for x in re.findall(r'[^.!?]+[.!?]', f)]
    res = {}
    for L in (22, 23, 24, 25):
        takes, cur = [], []
        for s in sents:
            if cur and wc(' '.join(cur + [s])) > L:
                takes.append(' '.join(cur)); cur = [s]
            else:
                cur.append(s)
        takes.append(' '.join(cur))
        res[L] = (takes == falas)
    return res
COMUNS = {('and', 'it'), ('in', 'the'), ('of', 'the'), ('the', 'lens'), ('of', 'her'), ('to', 'the'), ('on', 'the'), ('at', 'the')}
def pares(s):
    w = re.findall(r"[a-z0-9']+", s.lower())
    return {(w[i], w[i + 1]) for i in range(len(w) - 1)}
erros = []
for k, pk in PACOTES.items():
    vids = pk['videos']
    if not pk.get('clipe_unico'):
        falas = [v['fala'] for v in vids]
        print('nora' + k, 'palavras:', [wc(f) for f in falas], 'divisor:', simula(falas))
        if not all(simula(falas).values()) and len(falas) > 1: erros.append('divisor nora' + k)
        for v in vids:
            inter = (pares(v['fala']) & pares(v['movimentacao'])) - COMUNS
            if inter: erros.append('sobreposição nora%s %s %s' % (k, v['rotulo'], inter))
            if wc(v['fala']) > 22: erros.append('fala longa nora%s %s' % (k, v['rotulo']))
    textos = [pk['roteiro']['descricao_instagram'], pk['comentario_fixado']['insta'], pk['comentario_fixado']['face'], pk['texto_tela']['hook']] + [v['fala'] for v in vids] \
             + [x.get('fala', '') for x in pk['pecas']['lista']] + [e['texto'] for e in pk['edicao_linha']] + [t['texto'] for t in pk['story']['textos']] + pk['story']['adesivos']
    for t in textos:
        low = t.lower()
        for w in ['free', 'guarantee', 'minutes', 'soulmate', 'will find', 'psychic', 'come back', 'twin flame', 'initials', 'money', 'prosper', 'tomorrow', 'saint', 'portal', 'jealous', 'envy']:
            if w in low: erros.append('P39/P40 "%s" em nora%s: %s' % (w, k, t[:60]))
    prompts = [pk['figurino']] + [im['cena'] for im in pk['imagens']] + [e['prompt'] for e in pk.get('pre_gancho', {}).get('etapas', [])] \
              + [v['movimentacao'] for v in vids] + [x.get('copiar', '') for s in pk['central'].get('config', []) for x in s['campos'] if x['campo'].startswith('LIVRE')]
    for p in prompts:
        low = p.lower()
        for w in ['chest', 'breast', 'panties', 'underwear', 'thigh', 'torso', 'lap', 'bra', 'cleavage']:
            if re.search(r'\b' + w + r'\b', low): erros.append('palavra de corpo "%s" em nora%s' % (w, k))
    for v in vids:
        if v['duracao'] not in (4, 6, 8, 10): erros.append('duração')
print('hooks chars:', {k: len(p['texto_tela']['hook']) for k, p in PACOTES.items()})
print('créditos:', {k: sum(x.get('creditos', 0) for x in p['pecas']['lista'] if x['status'] == 'gerar') for k, p in PACOTES.items()})
if erros:
    print('ERROS:'); [print(' -', e) for e in erros]
    sys.exit(1)

modelo = open(REPO + 'PAINEL-MODELO.html', encoding='utf-8').read()
assert modelo.count('const PACOTE = null;') == 1
for k, pk in PACOTES.items():
    html = modelo.replace('const PACOTE = null;', 'const PACOTE = ' + json.dumps(pk, ensure_ascii=False) + ';')
    html = html.replace('<title>Painel de Produção</title>', '<title>Painel nora' + k + '</title>')
    open(REPO + 'PAINEL-NORA' + k + '.html', 'w', encoding='utf-8').write(html)
    json.dump(pk, open(SP + 'pacotes/nora' + k + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('ok nora' + k, len(html))
