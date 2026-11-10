# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
from scripts import T29,T30
ROOT='/home/user/IA-SINTETICO-PRODUTOR/'
LEIT=("20/10/2026: antes de escrever li, com a ferramenta de leitura e inteiros, neste turno: `CLAUDE.md` (recarregado no início do turno, com P1 a P29), `00-LEIA-PRIMEIRO.md`, `PROJETO-Dana.md`, `BRIEFING-LOVECHART.md` (com a call do Gustavo de 19/10), `LICOES-FLOW-E-PROMPTS.md`, `hooks.md` (com a seção 7), `Formatos Narrativos - Problema e Cenario.md`, `Exemplos de Roteiros - 2 Formatos.md`, `ctas.md`, `COMUNICACAO-VISCERAL-E-FALADA.md`, `BIBLIOTECA-BODIES.md`, `BIBLIOTECA-COLD-READING.md`, `BIBLIOTECA-COPY.md`, `BIBLIOTECA-COPY-100-ROTEIROS.md` (as duas partes), `PESQUISA-PUBLICO.md`, `BIBLIOTECA-VIDEOS-VIRAIS.md` (inteiro, com a seção 19 do lote de 20/10), `BIBLIOTECA-PRE-GANCHOS.md`, `BIBLIOTECA-DE-TAKES.md`, o `ROTEIRO-NORA26` (modelo de formato), o início do `ROTEIRO-NORA28` e as métricas dos campeões B3, C4 e B4V. **Ainda não li neste turno** os arquivos de produção (`Prompts.txt`, `CHECKLIST-DE-PRODUCAO.md`, `PAPEL-AGENTE-FLOW.md`, `GUIA-CREATIVE-HUB.md`, `PLANO-CREDITOS-*`, `PASSO-A-PASSO-*`, `EXEMPLO-*`, `PAINEL-MODELO.html`, `DNA Visual - Nora v2.md`, `REGISTRO-DE-PERSONAS.md`, os roteiros R001 a nora25 e os de reserva): serão lidos na Fase 2, antes de qualquer prompt ou painel, e o painel registra isso.")
CONF=("**Conferência da seção 9 de COMUNICACAO-VISCERAL e do hook visual:** dá para imaginar uma cena concreta só ouvindo cada fala: sim; soa como conversa (frases curtas, segunda pessoa): sim; a espectadora reconhece uma situação real (reler a conversa, o homem quente na segunda e frio na sexta), não um desejo genérico: sim; o benefício preserva o alcance do fato (o quiz “encontra o Vênus, dá nome ao padrão e mostra o par perfeito”; a Nora não diz que a pessoa existe nem que o amor chega): sim; nenhum depoimento, número de atendidas, preço ou celebridade inventado; o prazo, a data e a escassez são liberados (P15 e P20): sim; os nomes de padrão (The Curious Heart, The Steady Heart) são resultados reais do quiz, segundo o briefing: sim; a promessa fica no story (P6): sim; cada fala tem de 19 a 22 palavras e a simulação do divisor da Central gera exatamente as 8 cenas: sim.")
def takes(T):
    out=[]
    for i,(fn,nm,en,pt,vis) in enumerate(T,1):
        out.append("### Take %d/8 — %s — 10 s (%d palavras)\n**Nome do arquivo:** `%s`\n**Visual:** %s\n**Fala:** \"%s\"\n(PT: %s)\n"%(i,fn,len(en.split()),nm,vis,en,pt))
    return '\n'.join(out)
# ---------------- nora29
md29=f"""# nora29-CONTAGEM-3-2-1-ELE-SOME — roteiro completo (8 takes + pré-gancho em 2 tomadas), funil LOVE CHART (20/10/2026)

Status: **PARA APROVAR.** Persona: **Nora v2**. Funil: **Love Chart** (link só no story; o link ainda pode abrir o Soulmate, então o story usa a frase provisória). Postagem prevista: **20/10/2026 às 19h** (sem hashtag, teste da legenda). Falas em inglês dos EUA; a tradução é só para o aluno aprovar. Dor 2 (conversa por dias e o homem some), com a 3 (reler a conversa, adivinhar cada mensagem). Formato 1 (problema + crença + introdução da solução), 8 takes de 10 s + pré-gancho de 2 tomadas. Os créditos não são limite (P23).

## Leitura obrigatória (registro)
{LEIT}
{CONF}

## Base do curso usada (registro)
- **Hook:** gancho dos virais do lote de 20/10: **w8 (contagem “3, 2, 1” + “don't be one of them”; troquei “two people ignored this video” por “most people scrolled past this”, para não inventar número)** + **a data como gancho (w3 a w7, w9: “if this found you on October 20th or 21st”)** + ângulo 3 do curso (previsão com prazo). Não repete o molde do nora25 (#40), nora26 (duas coisas), nora27 (dois homens) nem nora28 (signos).
- **Cold reading:** “I don't know your name” (viral, w3 a w9) + #88 (sinais mistos) e #23 (você relê as conversas) + o fecho “Tell me I'm wrong”.
- **Body:** AD09/AD23 (o homem que se aproxima e depois se afasta) como ordem das emoções; a virada oficial do funil (“it's not bad luck, it's a pattern, and it depends on your Venus”); **nome real de um padrão do quiz** (tela 20 do briefing: “AIR VENUS · The Curious Heart”); “Stop guessing. Start knowing.” do funil.
- **Pesquisa e copy:** MUP = “o silêncio dele tem um padrão”; MUS = “Venus” + o nome do padrão; loop de Zeigarnik (a próxima parte só fecha no story); 3ª camada (“não é você, não é azar”); nível 2–3; future pacing (abrir o mapa e ver por que a história se repete).
- **CTA:** “send this to yourself” + código **222** (marca da conta e do curso) + tocar na foto + story (U1, w1 a w9).
- **P15/P20 usados:** data na fala, escassez (“most people scrolled past this”), ameaça suave (“this sign won't reach you again”). **Fora:** depoimento, número de atendidas, celebridade, preço, app, comissão, afiliado, parente falecido.

## Virais usados como modelo (peça por peça)
- **Pré-gancho:** **w4** (a pedra que ela aperta, trinca e abre, mostrando cristais, ouro e dois anéis; rosto grande; 8 ações em ~3 s) + **R01/S2** (corte seco para o macro). Duas tomadas, como o P29: (1) rosto grande, ela aperta o geodo e ele racha e abre; (2) macro: uma mão tira um anel dourado dos cristais e o ergue para a lente.
- **Gancho e texto do topo:** w8 e R08 (“If you are seeing this on Oct 2, 3 or 4, It's a Sign”): caixa branca no topo; pré-gancho com a situação em 2 linhas (V4/R01: “When you need…”).
- **Objeto na mão o vídeo todo:** w3/w4/w5 (geodo de ametista) e S1/S4: **meio geodo de ametista aberto, com um anel dourado fino entre os cristais**, na mão direita.
- **Edição:** número fixo no canto (222 à esquerda e 11:11 à direita, U1/U2/U4 e w10), legenda palavra a palavra com “Venus” e “quiet” em destaque, seta vermelha no fim.

## Imagem única (IMAGEM 1) — primeiro e último quadro de todos os takes
Continuação do pré-gancho (P26): **mesma roupa e mesmo cenário**; a Nora só passa a falar. A IMAGEM 1 é gerada na **Central de imagens** (campos no painel, P22).
- **Roupa:** blusa de malha canelada fina **terracota (cobre queimado)**, gola redonda, sem estampa, calça escura reta, broche esmaltado de bandeira dos EUA no peito (o roxo do geodo contrasta com a terracota).
- **Objeto na mão direita, em primeiro plano:** **meio geodo de ametista aberto (uns 12 cm), com um anel dourado fino entre os cristais**, perto da lente. A mão esquerda fica livre.
- **Cenário (sinais dos EUA):** sala de uma casa americana real: piso de madeira, uma parede clara com uma bandeirinha dos EUA pendurada, o canto de um sofá cinza, luz suave de fim de tarde de uma janela.
- **Luz e câmera:** luz natural quente de fim de tarde; Kodak Portra 400; câmera de celular. Sem carimbo de data (lição do nora25).

## Pré-gancho — 2 tomadas (clipes separados, sem fala, **com o rosto da Nora na tomada 1**)
**Tomada 1 (4 s, usa uns 2,5 s):** câmera no chão, perto, o rosto da Nora grande e sério, as duas mãos apertando um geodo redondo cinza (ainda fechado). Ela faz esforço, uma trinca aparece, abre e racha ao meio, e o geodo se abre mostrando cristais roxos. **Tomada 2 (4 s, usa uns 3 s):** macro do interior do geodo: uma mão tira um anel dourado fino de entre os cristais e o ergue em direção à lente; o ouro brilha. Corte seco entre elas. A Nora não fala. Prompts como roteiro de cena com tempos (P28) e imagens A, B, C, D virão no painel.
**Texto na tela:** "When he goes quiet and you don't know why:" (modelo: V4/R01).

## Takes (a fala inteira vai de uma vez na Central; o site divide em takes de 10 s)

{takes(T29)}
## Texto de tela (edição)
- **Pré-gancho:** "When he goes quiet and you don't know why:"
- **Início do vídeo (caixa branca no topo):** "If you're seeing this on October 20th or 21st, it's a sign." Começa em “3, 2, 1” e termina em “meant for you”.
- **Fixos no corpo:** “222” no canto superior esquerdo e “11:11” no canto superior direito (teste do lote de 20/10, na primeira vez que usamos o par).
- **Legenda:** palavra a palavra, com “Venus”, “quiet” e “pattern” em destaque; seta vermelha pequena no pedido final.

## Legenda do post (Instagram e Facebook) — SEM hashtag (alternância do teste)
3, 2, 1. Most people scrolled past this. 🔮
Part 2 is in my story. Comment 222. Tap my photo NOW.

## Comentário fixado
- **Instagram:** PART 2 is in my story. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 222 if this found you. 🔥
- **Facebook:** PART 2 is in my Story. Tap my profile picture NOW, it's gone in 24 hours. Comment 222 if this found you. 🔥

## Story (parte 2)
O mesmo story do Love Chart dos outros vídeos. **Enquanto o link abrir o Soulmate:** texto “Tap below and take the free love quiz.” e adesivo “Take the free quiz”. Quando o Gustavo avisar que o Love Chart entrou: “Tap below and find your Venus pattern in astrology.” e “Find my Venus”.

## Nomes e reaproveitamento
Pré-gancho: `nora29-PRE-A`, `-PRE-B`, `-PRE-V1`, `-PRE-C`, `-PRE-D`, `-PRE-V2`. Imagem do vídeo: `nora29-IMG`. Takes: {', '.join('`'+t[1]+'`' for t in T29)}. Vídeo completo (créditos não são limite): pré-gancho 2 vídeos de 4 s = 14 + 8 takes de 10 s = 120, **134 créditos**.

## Notas editoriais e factuais
- “The Curious Heart” é o nome de um padrão que o quiz dá (tela 20 do briefing), não o resultado de ninguém; a Nora diz “one pattern is called…”.
- “That quiet has a pattern, and it depends on your Venus” é a virada oficial do funil, com “in astrology”.
- A data “October 20th or 21st” é a da postagem (20/10 às 19h); se o vídeo for postado em outro dia, trocar só o Take 1 e o texto do topo.
- Sem nome do app, preço, pagamento, comissão ou afiliado, sem prometer que a pessoa existe nem que o amor chega.
- Sem métricas de publicação ainda.
"""
# ---------------- nora30
md30=f"""# nora30-QUARTO-SINAL-QUENTE-E-FRIO — roteiro completo (8 takes + pré-gancho em 2 tomadas), funil LOVE CHART (20/10/2026)

Status: **PARA APROVAR.** Persona: **Nora v2**. Funil: **Love Chart** (link só no story; story provisório enquanto o link abrir o Soulmate). Postagem prevista: **20/10/2026 às 21h** (**com hashtag**, teste da legenda). Falas em inglês dos EUA. Dor 4 (sinal ou ilusão?: “quente e frio, sem planos”, do briefing) com a 2. Formato 1 (problema + crença + solução), 8 takes de 10 s + pré-gancho de 2 tomadas.

## Leitura obrigatória (registro)
{LEIT}
{CONF}

## Base do curso usada (registro)
- **Hook:** gancho do viral **w9 (“This is the fourth time the universe has tried to reach you”)** + ângulo 4 do curso (**“você estava certa o tempo todo”**: gancho #31, Novo #2 e o campeão B4V “You were right about him”, 1.629 views) + o campeão C4 (“your last sign about him”). Não repete a data do nora29 nem os moldes do nora25 a nora28.
- **Cold reading:** #88 (“mixed signals, this is not in your head”) e #87 (diz que ama mas não aparece), em “quente na segunda, frio na sexta, e nunca faz planos de verdade” (dor do briefing: relação quente e fria, sem planos).
- **Body:** AD09 e AD23 (se aproxima e depois se afasta) como ordem das emoções; a virada oficial (“not bad luck… depends on your Venus”); **dois nomes reais de padrão do quiz** (tela 20 e 2º teste do briefing: “The Curious Heart”, “The Steady Heart”); “a love that doesn't make you guess” (tela 25 do quiz); a Lua da noite em que nasceu (tela 17).
- **Pesquisa e copy:** MUP = “quente e frio é um padrão”; MUS = Vênus + a Lua do nascimento; loop (a parte dois só fecha no story); 3ª camada (“não é você”); nível 2–3.
- **CTA:** selo **salvar** + código **444** (numérico, como w9) + tocar na foto + story.
- **P15/P20 usados:** escassez (“not everyone will see this”), ameaça (“I can't send it again”), garantia leve (“you were right”). **Fora:** depoimento, número de atendidas, celebridade, preço, app, comissão, afiliado, parente falecido.

## Virais usados como modelo (peça por peça)
- **Pré-gancho:** **w6** (carro americano: levantar o tapete do chão, jogar folhas de louro, despejar sal, repor o tapete; 3 cortes em ~4,8 s) + **S2** (sal caindo em primeiro plano, corte seco). Duas tomadas (P29): (1) câmera no chão do carro, ela levanta o tapete de borracha e joga o louro; (2) macro: o sal cai em fio e cobre as folhas, e o tapete volta ao lugar.
- **Gancho e texto do topo:** w9/w8 (texto curto no topo): “Your fourth sign about him.” (C4: “Your last sign about him”). Pré-gancho: “It works so fast it's scary…” é do nora27; aqui o texto do pré-gancho é “When he's hot, then cold:” (V4/R01).
- **Objeto na mão o vídeo todo:** uma **folha de louro seca** (a do pré-gancho) com um pequeno símbolo de Vênus desenhado à mão em tinta preta, segurada na mão direita (S1/S4: objeto ligado ao tema).
- **Edição:** “444” fixo no canto superior esquerdo e “11:11” no direito (w9, U1), legenda palavra a palavra com “Venus” e “fourth” em destaque, seta vermelha no fim.

## Imagem única (IMAGEM 1) — primeiro e último quadro de todos os takes
Continuação do pré-gancho (P26): mesma roupa e mesmo cenário. Gerada na **Central de imagens** (P22).
- **Roupa:** malha fina **ameixa (plum) escura**, gola redonda, sem estampa, calça escura reta, broche esmaltado de bandeira dos EUA no peito.
- **Objeto na mão direita, em primeiro plano:** **uma folha de louro seca** (uns 8 cm) com um pequeno símbolo de Vênus (♀) desenhado à mão em tinta preta, segurada entre o polegar e o indicador, perto da lente. A mão esquerda fica livre.
- **Cenário (sinais dos EUA):** entrada de uma casa americana de bairro: a Nora ajoelhada ao lado da porta traseira aberta de um SUV cinza, no concreto da garagem, com uma bandeirinha americana num suporte da casa ao fundo; luz suave de fim de tarde, sem texto legível.
- **Luz e câmera:** luz natural; Kodak Portra 400; câmera de celular. Sem carimbo de data.

## Pré-gancho — 2 tomadas (clipes separados, sem fala, **com o rosto da Nora na tomada 1**)
**Tomada 1 (4 s, usa uns 2,5 s):** câmera no chão do carro, perto: o rosto da Nora aparece grande atrás do tapete de borracha preto do SUV; ela o levanta com as duas mãos, mostra o carpete limpo embaixo e solta uma mão cheia de folhas de louro secas. **Tomada 2 (4 s, usa uns 3 s):** macro do chão do carro: um fio de sal grosso cai sobre as folhas, cobrindo-as, e o tapete volta ao lugar. A Nora não fala. Os prompts (roteiro de cena com tempos, P28) e as imagens A, B, C e D vêm no painel.
**Texto na tela:** "When he's hot, then cold:" (modelo: V4/R01).

## Takes (a fala inteira vai de uma vez na Central; o site divide em takes de 10 s)

{takes(T30)}
## Texto de tela (edição)
- **Pré-gancho:** "When he's hot, then cold:"
- **Início do vídeo (caixa branca no topo):** "Your fourth sign about him." Começa em “This is the fourth time” e termina em “all along”.
- **Fixos no corpo:** “444” no canto superior esquerdo e “11:11” no direito.
- **Legenda:** palavra a palavra, com “Venus”, “fourth” e “pattern” em destaque; seta vermelha pequena no pedido final.

## Legenda do post (Instagram e Facebook) — COM hashtag (alternância do teste)
Your 4th sign about him. 💔
Part 2 is in my story. Comment 444. Tap my photo NOW.
#astrology #venus #lovereading

## Comentário fixado
- **Instagram:** PART 2 is in my story. 👆 Tap my photo NOW, it's gone in 24 hours. Comment 444 if you saw the signs. 🔥
- **Facebook:** PART 2 is in my Story. Tap my profile picture NOW, it's gone in 24 hours. Comment 444 if you saw the signs. 🔥

## Story (parte 2)
O mesmo story dos outros vídeos. **Enquanto o link abrir o Soulmate:** “Tap below and take the free love quiz.” e adesivo “Take the free quiz”. Com o Love Chart no ar: “Tap below and find your Venus pattern in astrology.” e “Find my Venus”.

## Nomes e reaproveitamento
Pré-gancho: `nora30-PRE-A`, `-PRE-B`, `-PRE-V1`, `-PRE-C`, `-PRE-D`, `-PRE-V2`. Imagem do vídeo: `nora30-IMG`. Takes: {', '.join('`'+t[1]+'`' for t in T30)}. **134 créditos** (2 vídeos de pré-gancho de 4 s = 14 + 8 takes = 120).

## Notas editoriais e factuais
- “The fourth time the universe has tried to reach you” é teatro de leitura (w9), sem número de pessoas nem fato verificável; “you were right about him” é o gancho do curso (#31) e o B4V.
- “The Curious Heart” e “The Steady Heart” são nomes reais de padrões do quiz (briefing); a Nora diz “some Venus patterns…”, sem dizer qual é o da espectadora.
- “May show why” mantém a promessa no que o quiz mostra (Vênus e a Lua do nascimento), sem prometer que o amor chega.
- Sem nome do app, preço, pagamento, comissão ou afiliado.
- Sem métricas de publicação ainda.
"""
open(ROOT+'ROTEIRO-NORA29-CONTAGEM-3-2-1-ELE-SOME.md','w').write(md29)
open(ROOT+'ROTEIRO-NORA30-QUARTO-SINAL-QUENTE-E-FRIO.md','w').write(md30)
print('ok',len(md29),len(md30))
