# Registra a grade da @soma_chhaya (5 prints do aluno, 10/11/2026 00h55) e os reels escolhidos para o corpo novo.
# Rodar uma vez, da raiz do repositório: python3 -I ferramentas-painel/r1011/registrar_soma_grade.py
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


SEC = '''### 49.6 soma_chhaya (Soma Chhaya, pessoa real, não avatar; 3,3 mi de seguidores, 777 posts, verificada; 5 prints do aluno de 10/11 00h55: o perfil e 36 reels)
- **Por que ela:** é a 3ª indicação (Matheus Baffa modela os cenários dela desde 23/10; Felps, 07/11: "a sensação de gravado no celular", "tipo a Soma Chaya"; Gustavo, call de 09/11: "uma aula de manifestação, uma aula de copy", "fazer um NotebookLM dela é uma boa ideia"). Não vende Appyon (vende os próprios rituais): pode ser modelada, sempre reescrevendo a fala (aviso de 22/09). Já tínhamos 3 falas dela (297, 125 e 52 mil) na seção 39.
- **Perfil:** bio "The #1 most followed manifestation expert / Click the link for spells & rituals ☕✨ / 💍 @antoinemmartel" (noiva do Antoine Martel, da seção 39); link na bio para o ritual 11:11 da loja dela (luckygirl.com; conta grande com produto próprio: a regra da Nora de não pôr link na bio continua); Destaques **FREE, my story, how-to, Press!, affirmations** (ideia para os Destaques da Nora, hoje planejados "About me" e "Reviews"); 3 posts fixados (8M, o noivado, a placa de 1M do YouTube). Seguida por scarlletmorgantarot e philjones.p92 (contas da nossa lista da 49).
- **Grade (36 reels, do mais novo ao mais velho, ~9 por dia de 06 a 09/11; datas pelo texto na tela):** "If you are watching this on or before November 11th" 58,1 mil · "11:11 manifesting portal" (um aparelhinho na mão) 61 mil · "November 11th reading" (carta Queen of Pentacles) 51,6 mil · "if you are watching this video on November 9th" (caneca de cereja) 91,6 mil · "this video will find you on Monday November 9th, 2026" (cartas) 129 mil · "if you are watching this video on November 9th" (caneta, caderno) 140 mil · "Thursday November 9th 2026 / if you are watching" (café gelado) 63,7 mil · **"if you see this on Monday November 9th" (11:11, sem objeto, close) 1,2 mi** · **"this video will find you on Monday November 9th" (olhando de lado, mão no rosto) 548 mil** · "this video will find you on Monday November 9th" (cristal e vela) 222 mil · idem (vela) 92 mil · idem (olhando de lado) 188 mil · **"I APOLOGIZE FOR DISRUPTING YOUR SCROLL... but, YOU are going to have so many wins in NOVEMBER" (ao ar livre, mão na testa) 201 mil** · "you are gonna see this video on Sunday" (3 cartas) 223 mil · "if this video found you on November 8th" (caneta) 142 mil · "this video will find you on Sunday November 8th" (carta) 119 mil · **"this video will find you on Sunday November 8th and if it does" (carta da Roda) 463 mil** · "1111 portal is now OPEN / if you are watching this video on November 8th, 9th or 10th" (caneca) 94,5 mil · "if you are watching this on Sunday November 8th" (cartas) 146 mil · "this video will find you on Sunday November 8th" (3 cartas) 247 mil · "if this video found you on November 7th" (caderno, caneta) 146 mil · "The 1111 portal is now OPEN / November 7th, 8th or 9th" (caneta) 121 mil · "Saturday, November 7th, 2026" (carta, 11:11) 133 mil · "Nov 7th, 2026" (caderno) 86,8 mil · "if you are watching this on November 7th" (11:11) 117 mil · "if this video found you on Saturday November 7th" (carta da Roda) 236 mil · "Thursday November 7th 2026" (café gelado) 82,7 mil · "if you are watching this on Saturday November 7th" 87,4 mil · "this video will find you on Saturday November 7th" (sorrindo, dedo no lábio) 163 mil · idem (sorrindo) 83,6 mil · "this video is going to find you on Friday November 6th" (ao ar livre) 154 mil · "Nov 6th, 7th & 8th" (carta) 140 mil · "if this video found you on Friday November 6th" (ao ar livre, 11:11) 100 mil · "this video is gonna find you on November 6th" (abrindo 3 cartas na mesa, ao ar livre) 268 mil · "Friday November 6, 2026" (3 cartas) 114 mil · **"if you see this on Friday November 6th" (dedo levantado, anel) 453 mil**.
- **Leitura dos 36 (minha):** mediana **~137 mil** (4% dos seguidores), média ~194 mil; conta **em alta** (os maiores são de 06 a 09/11). Os 4 fora da curva: **1,2 mi (8,8x a mediana), 548 mil (4x), 463 mil (3,4x) e 453 mil (3,3x)**.
  1. **O formato inteiro é o gancho da data:** todo reel abre com "this video will find you on [dia da semana] November [N]th" / "if you see this on…" / "if you are watching this on…", escrito no meio da tela (legenda branca pequena) e repetido em letra maior no alto ("Nov 9th 2026"), muitas vezes com "11:11" pequeno no canto. É o "gancho da data é o campeão" do `PLANO-MVM` (Copy › Gancho), agora em escala.
  2. **"if you see this on…" fez os 2 de cima de "frase da data" (1,2 mi e 453 mil)**; "this video will find you on…" vai de 83 a 548 mil; "if you are watching this…" de 58 a 146 mil. Amostra pequena, mas é a 1ª pista de qual frase usar.
  3. **Objeto não decide:** os maiores são close no rosto, sem nada na mão (1,2 mi, 548 mil, 453 mil); com cartas, 114 a 463 mil; caneta e caderno, 87 a 146 mil. Quem decide é a fala.
  4. **Cara de celular:** selfie, rosto perto da lente, parede lisa ou escritório em casa, luz de janela, roupa de casa (moletom, camiseta, suéter), unhas escuras e anéis; nada de estúdio. É o visual que o Felps pediu para a Nora.
  5. **Volume em sessão:** ~9 reels por dia; o 1,2 mi, o 548 mil, o 222 mil, o 188 mil e o 92 mil são da mesma sessão (mesma camiseta, mesma luz, 09/11), cada um com outra abertura ou objeto: é a "variação" do Iorhan (call de 06/11).
  6. **Para a Nora:** ela usa carta de tarô em muitos (a Nora não: o funil não tem cartas antes do quiz); fala de dinheiro e "claim" aparecem nas falas antigas da seção 39 (na Nora, sem promessa de dinheiro e sem "claim").
- **Escolhidos (etapa 2, 10/11 ~01h10):** **1,2 mi**, **548 mil**, **463 mil**, **453 mil** (os 4 fora da curva) e **201 mil** (o único com gancho de texto diferente da data, "I APOLOGIZE FOR DISRUPTING YOUR SCROLL…", útil depois do 11/11 e para o `BANCO-DE-HEADLINES.md`); se der, o **222 mil** (cristal e vela na mão: objeto do nicho, o pré-gancho do Kaike). Pedido: o vídeo com som (Baixar do Insta ou gravação de tela; acima de 30 MB, Drive), o print dos números (curtidas, comentários, envios, salvos) e a legenda inteira ("mais") de cada um. Eu transcrevo aqui e monto a estrutura do corpo novo.
'''

b = ler('BIBLIOTECA-VIDEOS-VIRAIS.md')
if '### 49.6 soma_chhaya' in b:
    sys.exit('já registrado')
b = trocar(b, '### 49.S Stories das contas mineradas', SEC + '\n### 49.S Stories das contas mineradas')
gravar('BIBLIOTECA-VIDEOS-VIRAIS.md', b)

c = ler('COMUNIDADE-E-ESTRATEGIA.md')
c = c.rstrip('\n') + '''

### 10/11/2026 ~01h10 - Grade da @soma_chhaya (5 prints do aluno, 00h55): o corpo novo vai pelo gancho da data
- **O que a grade mostra (detalhe na seção 49.6 da `BIBLIOTECA-VIDEOS-VIRAIS.md`):** 3,3 mi de seguidores, ~9 reels por dia, mediana ~137 mil; **todo reel é o gancho da data** ("this video will find you on Monday November 9th", "if you see this on…"), selfie com cara de celular, em casa; os maiores (1,2 mi, 548 mil, 453 mil) são close no rosto, sem objeto.
- **Para a Nora (decisão minha):** o corpo novo (a partir de 12/11, sem portal) sai neste molde: **Take 1 com a data do dia do post** ("If you see this on Thursday, November 12th…"), o que encaixa no Take 1 novo que já geramos a cada post (a data troca todo dia, sem gastar mais); a qualificação por signo pode continuar logo depois da data; cena com cara de celular. Escolha final da frase e do corpo depois de transcrever os 5 escolhidos (1,2 mi, 548 mil, 463 mil, 453 mil e 201 mil; se der, o 222 mil). Fora: cartas de tarô na mão (funil sem cartas antes do quiz), promessa de dinheiro e "claim".
'''
gravar('COMUNIDADE-E-ESTRATEGIA.md', c)

m = ler('CLAUDE.md')
m = trocar(m, '**Pedido ao aluno:** 4 ou 5 reels mais vistos da @soma_chhaya (baixados ou gravados com som) + print da grade com as views.',
           '**Grade recebida (10/11 00h55; seção 49.6 da `BIBLIOTECA-VIDEOS-VIRAIS.md`):** todo reel dela é o gancho da data ("if you see this on Monday November 9th"), selfie de celular, mediana ~137 mil; o corpo novo vai nesse molde (Take 1 com a data do dia). **Pedido ao aluno:** os vídeos com som de 1,2 mi, 548 mil, 463 mil, 453 mil e 201 mil (se der, o 222 mil), com o print dos números e a legenda de cada um.')
m = trocar(m, '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n',
           '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n'
           '- **10/11/2026 ~01h10, grade da @soma_chhaya:** o corpo novo vai pelo gancho da data (Take 1 com a data do dia do post), selfie com cara de celular; escolhidos 5 reels para transcrever. Detalhe em `BIBLIOTECA-VIDEOS-VIRAIS.md` (49.6) e `COMUNIDADE-E-ESTRATEGIA.md` (10/11 ~01h10).\n')
gravar('CLAUDE.md', m)
print('ok')
