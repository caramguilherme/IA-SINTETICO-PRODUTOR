# Registra as falas dos 6 reels da Soma Chhaya (vídeos do aluno, 10/11 ~01h20) e o esqueleto do corpo novo.
# Rodar uma vez, da raiz do repositório: python3 -I ferramentas-painel/r1011/registrar_soma_falas.py
import pathlib, sys

R = pathlib.Path(__file__).resolve().parents[2]


def ler(n):
    return (R / n).read_text(encoding='utf-8')


def gravar(n, t):
    (R / n).write_text(t, encoding='utf-8')


def trocar(texto, velho, novo):
    if texto.count(velho) != 1:
        sys.exit(f'trecho não único ({texto.count(velho)}): {velho[:70]}')
    return texto.replace(velho, novo)


BIB = '''- **Falas (vídeos do aluno, 10/11 ~01h20; transcrições inteiras em `referencias-mineracao/soma_chhaya_2026-11-10/transcricoes.md`):**
  - **1,2 mi (15 s, 2 falas):** "If you see this on Monday, November 9th, this message is 100% meant for you. Congratulations. Good news is coming to you tomorrow at 11:11 a.m. The better you treat this video, the bigger the blessing will be. Karma is real."
  - **453 mil (15 s):** "If you see this on Friday, November 6th, it is a sign. You are about to have the luckiest weekend of your [palavrão] life. Anything you desire is coming your way this weekend. The better you treat this video, the better this weekend treats you."
  - **548 mil (36 s):** data + "100% meant for you" → "A massive miracle is coming towards you. The worst is finally over." → "the person who shares this video will receive a blessing in the next hour" → "Claim this energy. Comment 'I accept'. Make sure you are following me. Then share this video. Karma is real… You must follow all three steps…"
  - **222 mil (34 s):** data + "100% meant for you" → "You are about to get paid by the universe… 13 minutes after watching this video, you will receive money, but you must claim this energy" → envio para 3 pessoas, seguir, "comment I accept" (é a fala do reel de 297 mil da seção 39, de outubro: ela recicla a copy vencedora).
  - **463 mil (2 min 47 s, o que vende):** data + "100% meant for you" → **promessa com prazo** ("extreme blessings coming your way in exactly two days"; "you are two days away from your entire life changing") → bênçãos em todas as áreas ("love, money, success, joy, fulfillment, beauty, magnetism, ease") → **bloco de engajamento aos ~32 s** (claim, mandar para 3 pessoas, comentar "thank you universe", seguir: "you must be following me in order to receive this reading") → **re-gancho: "Now here's everything you need to know about these blessings"** → dinheiro (forte: "money keeps pouring in", "more money than you know how to spend") e amor ("a connection is going to strengthen, or somebody new is walking into your life") → **mecanismo** (o portal 11:11, "a cosmic gateway between your current self and your future self"; "whatever intention you set in the next 48 hours has no choice but to manifest") → **CTA do produto com prova** ("I highly recommend you do the 11:11 ritual… Thousands of people have done this ritual… You can see these screenshots for yourself" + print de depoimento real na tela + "the link is in my bio") → "In two days, everything changes."
  - **201 mil (4,5 s):** sem fala, só música e o texto "I APOLOGIZE FOR DISRUPTING YOUR SCROLL…".
- **O que a fala mostra (minha leitura, 10/11 ~01h30):**
  1. **Dois formatos.** Os de alcance (15 a 36 s) não vendem nada: data → uma promessa boa com prazo → engajamento ("the better you treat this video, the bigger the blessing will be"). **Os 2 maiores (1,2 mi e 453 mil) têm 15 s.** O que vende é o longo (463 mil): a mesma abertura e, no fim, o produto com prova real e o link.
  2. **A abertura é sempre a mesma frase:** "This video will find you on [dia], and if it does, this message is 100% meant for you" (ou "If you see this on [dia]…").
  3. **A promessa tem prazo curto e data:** "tomorrow at 11:11 a.m.", "in exactly two days", "this weekend". Depois do 11/11, o prazo precisa de outro motivo (o dia da semana, "this week", "before Sunday").
  4. **No longo, o engajamento vem cedo (~32 s) e o re-gancho segura** ("Now here's everything you need to know…"); o produto fica no fim, com prova real (prints de clientes).
  5. **Fora da Nora:** promessa de dinheiro com hora ("13 minutes after watching this video, you will receive money", "get paid by the universe": o Face restringe promessa de ganho e é a "alegação enganosa" do Felps), "karma is real" e "you must… in order to receive" (pressão), palavrão, "massive miracle" (o Iorhan: "milagroso" levanta resistência), "link in my bio" (regra da Nora) e o print de depoimento (só Trustpilot real, P46).
'''

b = ler('BIBLIOTECA-VIDEOS-VIRAIS.md')
if '- **Falas (vídeos do aluno, 10/11 ~01h20;' in b:
    sys.exit('já registrado')
anc = '\n### 49.S Stories das contas mineradas'
b = trocar(b, anc, '\n' + BIB.rstrip('\n') + '\n' + anc)
gravar('BIBLIOTECA-VIDEOS-VIRAIS.md', b)

COM = '''
### 10/11/2026 ~01h30 - As falas da Soma Chhaya (6 vídeos transcritos) e o esqueleto do corpo novo
- **O que saiu (detalhe na seção 49.6 da `BIBLIOTECA-VIDEOS-VIRAIS.md`; falas inteiras em `referencias-mineracao/soma_chhaya_2026-11-10/transcricoes.md`):** os 2 maiores (1,2 mi e 453 mil) têm **15 s**: data → "this message is 100% meant for you" → uma promessa boa com prazo curto → "the better you treat this video, the bigger the blessing will be". O que vende é o longo (463 mil, 2 min 47 s): data → promessa com prazo ("you are two days away from your entire life changing") → bênçãos em todas as áreas → engajamento aos ~32 s → re-gancho ("Now here's everything you need to know…") → dinheiro e amor → mecanismo (portal 11:11 como "cosmic gateway") → produto com prova real e link.
- **Para a Nora (decisão minha): o corpo novo sai como um kit de 2 versões na mesma cena (cara de celular, close, em casa), como as sessões dela:**
  1. **Take 1 do dia (troca a cada post, 15 créditos):** "This video will find you on [Thursday, November 12th], and if it does, this message is 100% meant for you." A data é a do dia nos EUA em que o vídeo vai rodar (17h, 19h30 e 22h: o mesmo dia; **00h30: o dia seguinte**, porque o vídeo vive a manhã dos EUA). Sai a qualificação por signo (é outra abertura; os signos podem voltar na caixa do topo).
  2. **Versão curta (~20 s, 2 takes, ~30 créditos):** Take 1 + uma promessa boa com prazo ("you are two days away from your life turning around: love, peace, ease, success") + o CTA em 3 partes compacto ("three quick questions and your private reading is ready: tap my photo and open my story") + "the better you treat this video, the bigger the blessing will be" (engajamento positivo, sem "karma").
  3. **Versão longa (~50 a 60 s):** o esqueleto do 463 mil com o CTA do story **cedo (~25 s, onde ainda estão ~25% a 30%)** e repetido no fim: data → promessa com prazo → bênçãos (amor primeiro; dinheiro leve, sem valor nem hora) → CTA → "Now here's everything you need to know…" → mecanismo (o "cosmic receiver" da nossa VSL, no lugar do portal, R16) → prova real (Trustpilot, `provas-trustpilot/`) → CTA de novo → engajamento (comentário com palavra variada, seguir, mandar para alguém).
  4. **Ordem:** escrevo a fala com a leitura obrigatória completa (roteiro novo) durante 10/11; o aluno passa a fala no Clone do Gustavo (regra da 11ª leitura); gera em 11/11 na contatocaram (~120 créditos o kit + os Takes 1 do dia); primeiro post em 12/11. O resultado do nora54 (versão curta do corpo A, 11/11 19h30) ajuda a decidir quanto das 4 vagas do dia vai para a curta e quanto para a longa.
'''
c = ler('COMUNIDADE-E-ESTRATEGIA.md')
gravar('COMUNIDADE-E-ESTRATEGIA.md', c.rstrip('\n') + '\n' + COM)

m = ler('CLAUDE.md')
m = trocar(m, '**Pedido ao aluno:** os vídeos com som de 1,2 mi, 548 mil, 463 mil, 453 mil e 201 mil (se der, o 222 mil), com o print dos números e a legenda de cada um.',
           '**Os 6 vídeos chegaram e foram transcritos (10/11 ~01h25; `referencias-mineracao/soma_chhaya_2026-11-10/transcricoes.md`).** **Corpo novo = kit de 2 versões na mesma cena:** Take 1 do dia com a data ("This video will find you on [dia], and if it does, this message is 100% meant for you"; à 00h30, a data do dia seguinte), versão curta de ~20 s (2 takes) e versão longa de ~50 a 60 s (esqueleto do 463 mil, CTA do story aos ~25 s e no fim, mecanismo "cosmic receiver", prova do Trustpilot). Eu escrevo a fala com a leitura completa em 10/11; o aluno passa no Clone; gera em 11/11 na contatocaram; 1º post em 12/11 (`COMUNIDADE-E-ESTRATEGIA.md`, 10/11 ~01h30).')
m = trocar(m, '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n',
           '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n'
           '- **10/11/2026 ~01h30, falas da Soma Chhaya e esqueleto do corpo novo:** os maiores dela têm 15 s (data + promessa com prazo + engajamento); o que vende é o longo de 2 min 47 s. Corpo novo = kit de 2 versões (curta ~20 s e longa ~50 a 60 s) na mesma cena, Take 1 com a data do dia; fala escrita em 10/11 com a leitura completa, Clone, geração em 11/11, post em 12/11. Detalhe em `COMUNIDADE-E-ESTRATEGIA.md` (10/11 ~01h30).\n')
gravar('CLAUDE.md', m)
print('ok')
