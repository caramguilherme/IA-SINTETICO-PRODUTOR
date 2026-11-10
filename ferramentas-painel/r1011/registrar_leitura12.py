# Registra a 12ª leitura do Discord (chat-appyon 09/11 11h15 a 10/11 00h15; vitórias 09/11 11h57 a 21h16)
# nos documentos do projeto. Rodar uma vez, da raiz do repositório: python3 -I ferramentas-painel/r1011/registrar_leitura12.py
import pathlib, sys

R = pathlib.Path(__file__).resolve().parents[2]


def ler(n):
    return (R / n).read_text(encoding='utf-8')


def gravar(n, t):
    (R / n).write_text(t, encoding='utf-8')


def depois_da_linha(texto, inicio, novo):
    """Insere `novo` (linhas) logo depois da 1ª linha que começa com `inicio`."""
    linhas = texto.split('\n')
    achou = [i for i, l in enumerate(linhas) if l.startswith(inicio)]
    if len(achou) != 1:
        sys.exit(f'âncora não única ({len(achou)}): {inicio[:60]}')
    i = achou[0]
    return '\n'.join(linhas[:i + 1] + novo.split('\n') + linhas[i + 1:])


def trocar(texto, velho, novo):
    if texto.count(velho) != 1:
        sys.exit(f'trecho não único ({texto.count(velho)}): {velho[:60]}')
    return texto.replace(velho, novo)


# ---------------------------------------------------------------- COMUNIDADE
COM = '''
### 10/11/2026 ~00h40 - Discord, 12ª leitura (chat-appyon 09/11 11h15 a 10/11 00h15; vitórias-dólar 09/11 11h57 a 21h16; `HISTORICO-DISCORD/`, imagens em `HISTORICO-DISCORD/imagens/09-11_10h34_a_10-11_00h15/`)
- **Sem buraco:** o chat começa 41 min depois do marcador (09/11 10h34) e não tem intervalo de mais de 2 h; no vitórias, nada de 08/11 16h32 a 09/11 11h57 (conferido voltando até 05/11). Ficaram de fora o .mov do Maycon (tela de confirmar identidade travada), o .mp4 do Ricardo (avatar no Muse) e as prévias de link.
- **Rundouglas (vitórias, 19h33; `vit_2026-11-09_19h33_Rundouglas_1.png`), "primeira semana vendendo todo dia":** 7 dias até 08/11 23h21: **32 vendas, R$ 2.410,40** (só front, R$ 75,33 por venda), 10.157 cliques, 9.756 views e 1.024 checkouts. **0,31% de clique em venda (~317 cliques por venda), a régua oficial de 0,30% em número real.** 10% dos cliques chegam ao checkout e 3,1% dos checkouts compram. Em 21/10 ele tinha 1 venda em 1.532 cliques (`PLANO-MVM`, Funil Manifestation): mesma pessoa, 3 semanas depois. Funil não dito nesta mensagem.
- **Onda de restrições no Face continua (09/11):** Messenger bloqueado 28 dias "por mensagem que não segue os Padrões" (MJ COMPANY), e acaba um, vem outro (joaozmp). **Como liberaram:** pelo **app do Messenger**, não pelo Meta Business: abrir qualquer conversa com lead → "confirmar idade/identidade" → documento → ~2 min carregando → liberado (MJ COMPANY); obreno.lopes liberou com a identidade na 5ª tentativa, só depois de pôr no perfil o nome e sobrenome iguais aos do documento. Para Maycon e Juliana Kli o botão não abre nada (ou a selfie volta em loop). **Impacto:** Dorigon, depois da restrição, não passou de 100 views e descartou a conta; o Maycon segue viralizando (um vídeo de 80 mil), mas **perdeu a maior parte das vendas, porque 80% vinham da DM**. Quando as views caem muito, o Maycon troca o formato e, se não voltar, a avatar.
- **Insta: "Você não pode compartilhar links" por 30 dias** (Belle, André Jabbour; motivo: "práticas comerciais proibidas"), em **conta nova, logo depois do 1º reel com link no story**. Solução: **Pedir análise, que costuma voltar rápido** (Jefersom, Lucas Guitel, Mary). O Vitor Garcia teve a análise aprovada e continuou bloqueado: ir nas configurações do perfil, ver se a restrição ainda aparece e pedir de novo (Jefersom).
- **Insta pedindo documento** (Marcelo, no GeeLark): o Delian disse que fez um documento "meio que falso no Canva" e a Mary indicou um bot do Telegram que vende documentos. **Falsificação: não usar, nem citar como opção.**
- **Golpe (Bruno Freitas, vitórias 20h27):** digitou um site errado, a página pediu para "confirmar que era humano", hackearam o Insta pessoal e o Face suspendeu quase todas as contas dele; páginas 3 dias fora do ar. Antes: perdeu a melhor conta e tomou restrição de DM numa página nova.
- **Flow e Creative Hub:** **não usar o Creative Hub no modo de 15 s** (Wall Estevam: ele põe 10 s de fala e 5 s só gastando crédito; no 1.2 ainda cobra o dobro); com 15 s o Flow não deixa a mesma imagem como quadro inicial e final (Paulo Infante); **agente do Flow que não trabalha = criar um projeto novo, não uma pasta nova** (joao, resolveu para o Kleber); gerar vários vídeos de uma vez com o prompt do Gustavo não funcionou para o Vercelli nem para o Carlao (só começa o 1º); Lower Priority só no Google AI Ultra de R$ 999,90 e só na conta que assina (Coelho e Yuka).
- **Muse:** o Ricardo faz ~40 por dia (limite semanal; com mais tokens) e deixou a voz consistente com um prompt base completo feito no GPT; o Carlao achou o lip sync em inglês ruim; bloqueio por região contornado com VPN (Ricardo e Carlao perderam 2 contas cada entrando sem VPN). Só registro: não usamos o Muse (o Flow fica).
- **Funis e copy:** Love Reading "tá convertendo bem mais" que o Love Chart e o Iorhan mandou dar mais atenção a ele (Maycon, 14h31; bate com a call de 06/11); a mesma copy em contas com avatares diferentes "não tem problema" (Maycon, 13h43).
- **Avatar com rosto de famosa:** o F Lopes mostrou alguém usando uma atriz brasileira conhecida como avatar; **checar no Google Lens** se o rosto é de alguém famoso (ele ainda sugere "pegar essas imagens e mudar os traços": não seguimos, nada a partir de foto de pessoa real).
- **Clone do Gustavo:** a fonte da call de 03/11 (a "67") tinha a transcrição da aula anterior do Gustavo (a "66") até a Ju corrigir, em 09/11 às 13h57 (Lucas, Kassio).
- **Call do Gustavo de 09/11 à noite ("do zero ao vídeo completo com avatar, blueprint"):** aconteceu depois das 18h40 (Graci achou que era 08/11); a gravação não apareceu nesta leitura.
- **Para a Nora (decisão minha):**
  1. **Nada muda no plano: o gargalo é clique.** O Rundouglas confirma a régua em número real (~317 cliques por venda, 0,31%). A Nora tem 22 cliques do Manifestation desde 27/10: 4 vídeos por dia, o CTA mais cedo (nora54, 11/11) e o corpo novo atacam isso.
  2. **Link do story no Insta:** a conta da Nora roda link no story desde outubro, e a restrição apareceu em contas novas. Se aparecer "Você não pode compartilhar links": **Pedir análise na hora** e me avisar; se aprovarem e continuar, conferir em Configurações → Status da conta e pedir de novo. Enquanto durar, o link segue no Face (story e comentário da Página). No 2º perfil (adiado), os 10 de aquecimento já vão sem link, como manda a regra.
  3. **DM no Face:** segue a regra da 11ª leitura (só para quem comenta, à mão, poucas, primeiro nome e texto diferente; se vier bloqueio ou "confirme sua identidade", parar e me avisar). Se vier: a Página da Nora está no perfil pessoal do aluno, com o nome dele (`FATOS-DO-ALUNO.md`), então a confirmação é legítima com o documento dele, pelo **app do Messenger** (o caminho do MJ COMPANY). O caso do Maycon (80% das vendas pela DM) mostra por que a Nora não depende da DM: o link fica no story e no comentário da Página.
  4. **Documento:** se o Insta ou o Face pedirem documento, nunca documento falso nem de outra pessoa; me avisar antes de mandar qualquer coisa.
  5. **Segurança (golpe do Bruno):** entrar no Insta e no Face só pelo app ou digitando instagram.com e facebook.com; página fora desses endereços pedindo "confirme que é humano" ou login é golpe: fechar.
  6. **Corpo novo em takes de 15 s (se o piloto do 1.2 em 360p passar):** o prompt sai daqui, com ~30 a 35 palavras de fala por take para ocupar os 15 s, não pelo modo de 15 s do Creative Hub (que deixa 5 s mudos); o Fim fica vazio, como já fazemos. O piloto do nora51 é de 10 s: não muda.
  7. **Agente do Flow parado:** projeto novo (anotado no `LICOES`).
  8. **Google Lens:** antes de usar qualquer avatar nova (2º perfil), passar a imagem no Google Lens. Na Nora vale uma conferida de 1 minuto com a `nora37-IMG`, só por garantia.
  9. **Clone do Gustavo:** as respostas R1 a R21 (07/11) foram feitas com a fonte 67 duplicada; o que elas atribuem à call de 03/11 veio da aula 66. Nada muda no plano (o corpo B foi conferido com o resumo local da aula 66, e a call de 03/11 já está aqui em `AULA-03-11-TURBINANDO-CRIATIVOS-IORHAN.md`). Antes de escrever o corpo novo, confiro o corpo C no `AULA-02-11-DO-MEDO-AO-DESEJO.md`; pergunta sugerida no fim do `CLONE-DO-GUSTAVO-RESPOSTAS.md`.
  10. **Gravação da call do Gustavo de 09/11:** pedir ao aluno o link quando sair no #gravações; serve para a cena nova do corpo novo (avatar, blueprint, animação).
  11. Love Reading e "mesma copy em várias contas" reforçam o 2º perfil, que o aluno adiou: só registro, não propor.
- **Quem responder (P44, item 6):** João Paulo (CTA de Face e Insta no mesmo vídeo: como a Nora faz), Paulo Infante (o quadro de validação), Mateus Guisolffi (Insta travado na tela do nome: a dica do `PLANO-MVM`) e o Rundouglas no #vitórias (parabéns + 1 pergunta). Bruno Freitas e Eduarda Kelly: só reagir com emoji. Textos em `CONTATOS-ALUNOS.md`. Ficaram de fora por não sabermos: Lívia (gerador no Muse), Eduardo & Sabrina (VPN), Anthonny (proxy), joao (notificação de venda), Paulo Sampaio (ordem da troca de avatar: na Nora a regra é avatar nova só em conta nova, Clone R21, mas a ordem que ele pergunta não testamos), Vercelli e Carlao (vários vídeos no Flow), Delian e Kleber (Muse grátis), Vitor Garcia (análise aprovada e bloqueado), Maycon e Juliana (botão de identidade).
'''

t = ler('COMUNIDADE-E-ESTRATEGIA.md')
if '12ª leitura' in t:
    sys.exit('COMUNIDADE já tem a 12ª leitura')
gravar('COMUNIDADE-E-ESTRATEGIA.md', t.rstrip('\n') + '\n' + COM)

# ---------------------------------------------------------------- PLANO-MVM
p = ler('PLANO-MVM-LEGACY-APPYON.md')
p = trocar(p, ' (avisos-appyon olhado em 17/10).',
           ' Depois, até 10/11: chat até 10/11 00h15 e vitórias-dólar até 09/11 21h16 (12ª leitura, feita em 10/11 às 00h20; 149 mensagens no chat e 7 no vitórias, 10 imagens; conferido: no chat, nenhum intervalo de mais de 2 h; no vitórias, nada de 08/11 16h32 a 09/11 11h57 nem de 13h46 a 18h16; ficaram de fora o .mov do Maycon, o .mp4 do Ricardo e as prévias de link) (avisos-appyon olhado em 17/10).')

p = depois_da_linha(p, '- **Love Reading na call de 06/11 (Iorhan):**',
                    '- **Love Reading converte mais que o Love Chart (Maycon Douglas, chat 09/11 14h31):** "love reading, tá convertendo bem mais"; o Iorhan falou para dar mais atenção a ele.')

p = depois_da_linha(p, '- **Renomear os takes no Flow (Daniel7, 07/11):**',
                    '- **Não usar o Creative Hub no modo de 15 s (Wall Estevam, 09/11 20h33):** ele usa 10 s para a fala e 5 s "só para gastar crédito", e o Omni 1.2 já cobra o dobro. Com 15 s, o Flow não deixa usar a mesma imagem como quadro inicial e final (Paulo Infante, 20h35). **Na Nora:** se um corpo sair em takes de 15 s, o prompt vem do painel com ~30 a 35 palavras de fala por take, e o Fim fica vazio.\n'
                    '- **Agente do Flow que não trabalha (Kleber, 09/11 19h22; limpou cache e trocou de navegador):** criar um **projeto novo**, não uma pasta nova (joao, 19h26; resolveu).\n'
                    '- **Vários vídeos de uma vez com o prompt do Gustavo:** não funcionou para o Vercelli nem para o Carlao (09/11 20h36 e 21h13: só começa o 1º). Sem solução no chat.\n'
                    '- **Lower Priority no Flow (Coelho e Yuka, 09/11 21h50):** só no Google AI Ultra de R$ 999,90 e só na conta que assina; o Ultra de R$ 779,90 não tem (`chat_2026-11-09_21h48_MarciaPolettoMVM_1.png`).')

p = depois_da_linha(p, '- **Muse (04/11):**',
                    '- **Muse (09/11, chat):** o Ricardo Santana faz ~40 vídeos por dia (limite semanal, "com mais tokens") e deixou a voz consistente montando um prompt base completo no GPT e colando no Muse; o Carlao achou o lip sync em inglês ruim. Bloqueio por região: o pessoal entra com VPN (TunnelBear, Urban VPN) ou multilogin, e quem entrou sem VPN perdeu conta (Ricardo e Carlao, 2 cada). Na Nora, o Flow fica.')

p = depois_da_linha(p, '- **Insta novo no GeeLark pedindo selfie e banindo (Gustavo, 08/11):**',
                    '- **"Você não pode compartilhar links" por 30 dias (Belle e André Jabbour, 09/11; `chat_2026-11-09_19h01_BelleMVM_1.jpg`, `chat_2026-11-09_23h31_AndreJabbour_1.jpeg`):** em conta nova, logo depois do 1º reel com link no story; motivo dado: "práticas comerciais proibidas". **Pedir análise, que costuma voltar rápido** (Jefersom, Lucas Guitel, Mary; há 30 dias para pedir). O Vitor Garcia teve a análise aprovada e seguiu bloqueado: ir nas configurações do perfil, ver se a restrição ainda aparece e pedir de novo (Jefersom).\n'
                    '- **Insta pedindo documento ("Upload your ID", Marcelo, 09/11 21h48, no GeeLark):** circularam documento "meio que falso no Canva" (Delian) e um bot do Telegram que vende documentos (Mary). **Isso é falsificação: não usar.**\n'
                    '- **Travou no "next" depois de digitar o nome (Mateus Guisolffi, 09/11 20h08):** é o passo 5 abaixo (criar pelo navegador do celular).')

p = depois_da_linha(p, '- **Onda de restrições no Face (07 e 08/11, Discord):**',
                    '- **A onda continua (09/11, chat):** bloqueio de 28 dias no Messenger "por mensagem que não segue os Padrões da Comunidade" (`chat_2026-11-09_13h16_MJCOMPANY_1.png`); para muitos, acaba um e vem outro (joaozmp). **Como liberaram:** pelo **app do Messenger**, não pelo Meta Business: entrar em qualquer conversa com lead, tocar em "confirmar idade", mandar o documento e esperar ~2 min (MJ COMPANY, 14h10 e 17h12); obreno.lopes liberou com foto da identidade na ~5ª tentativa, só depois de deixar o nome e o sobrenome do perfil iguais aos do documento. Para Maycon Douglas e Juliana Kli o botão não abre nada, ou a selfie volta em loop. **Impacto:** Dorigon não passou mais de 100 views e descartou a conta; o Maycon segue viralizando (80 mil num vídeo), mas as vendas caíram muito, porque 80% vinham da DM. **Lição:** não depender só da DM.\n'
                    '- **Golpe do "confirme que é humano" (Bruno Freitas, vitórias 09/11 20h27):** digitou um site errado, a página pediu para confirmar que era humano, hackearam o Insta pessoal (sem vínculo com a Appyon) e o Face suspendeu quase todas as contas; as páginas ficaram 3 dias fora do ar. Entrar só pelo app ou digitando o endereço oficial.')

p = depois_da_linha(p, '- Joao Paulo tem mais visitas no funil (20.794)',
                    '- **Rundouglas, "primeira semana vendendo todo dia" (vitórias 09/11 19h33, painel da Appyon, 7 dias até 08/11 23h21; funil não dito, em 21/10 era Manifestation):** 32 vendas, R$ 2.410,40 (R$ 75,33 por venda, sem recorrência), 10.157 cliques, 9.756 views, 1.024 checkouts. **0,31% de clique em venda (~317 cliques por venda)**, igual à régua oficial dos 10% melhores (0,30%); 10% dos cliques chegam ao checkout e 3,1% dos checkouts compram. Vendas por dia: ~6, 2, 4, 9, 8, 1, 3. Em 21/10 ele tinha 1 venda em 1.532 cliques.')

p = depois_da_linha(p, '- **Avatar sozinha não resolve.**',
                    '- **Avatar com rosto de famoso (F Lopes, 10/11 00h06):** alguém usava uma atriz brasileira conhecida como avatar; conferir no **Google Lens** se o rosto é de alguém famoso antes de usar. A mesma copy em contas com avatares diferentes "não tem problema" (Maycon, 09/11).')

p = depois_da_linha(p, '- **Clone do Gustavo / "Pergunte ao Gustavo"',
                    '- **Fonte da call de 03/11 no Clone corrigida (Ju Santos, 09/11 13h57):** até então a fonte 67 trazia a transcrição da aula anterior do Gustavo (a 66; Lucas e Kassio). As respostas R1 a R21 (07/11) foram feitas antes da correção.\n'
                    '- **Call do Gustavo de 09/11 à noite ("do zero ao vídeo que vende", avatar, blueprint, animação):** aconteceu; gravação ainda não vista (procurar no #gravações).')
gravar('PLANO-MVM-LEGACY-APPYON.md', p)

# ---------------------------------------------------------------- LICOES
L = '''
### 10/11/2026 - Discord, 12ª leitura: Flow e Creative Hub
- **Modo de 15 s do Creative Hub: não usar** (Wall Estevam, 09/11): ele gera 10 s de fala e deixa 5 s só gastando crédito. Se um corpo sair em takes de 15 s (Omni 1.2 em 360p, depois do piloto), o prompt é escrito aqui com ~30 a 35 palavras de fala por take, para a fala ocupar os 15 s; o Fim continua vazio (com 15 s o Flow não aceita a mesma imagem no início e no fim, Paulo Infante).
- **Agente do Flow parado** (não responde mesmo com cache limpo e outro navegador): criar um **projeto novo** no Flow, não uma pasta nova (joao, resolveu para o Kleber).
- **Vários vídeos ao mesmo tempo** com o prompt do Gustavo: não funcionou para ninguém no chat (só começa o 1º). Seguimos 1 take por geração.
'''
l = ler('LICOES-FLOW-E-PROMPTS.md')
gravar('LICOES-FLOW-E-PROMPTS.md', l.rstrip('\n') + '\n' + L)

# ---------------------------------------------------------------- CLONE
c = ler('CLONE-DO-GUSTAVO-RESPOSTAS.md')
c = c.rstrip('\n') + '''

**Nota (10/11, 12ª leitura do Discord):** até 09/11 13h57 a fonte 67 do notebook (call de 03/11, Iorhan) tinha a transcrição da aula 66; a Ju corrigiu. As respostas R1 a R21 foram feitas antes: o que citam como "67" veio da 66. **Pergunta sugerida, agora com a fonte certa:** "Na call de 03/11 (Turbinando criativos), o que o Iorhan diz sobre a diferença entre copy que engaja e copy que vende no Manifestation, e que estrutura de corpo ele mostra funcionando? Cite trechos."
'''
gravar('CLONE-DO-GUSTAVO-RESPOSTAS.md', c)

# ---------------------------------------------------------------- CONTATOS
k = ler('CONTATOS-ALUNOS.md')
k = trocar(k, '- **11ª leitura (09/11):** respostas a sordisss (Índia: horário) e Eduarda Fernandes (texto do story) enviadas.',
           '- **11ª leitura (09/11):** respostas a sordisss (Índia: horário) e Eduarda Fernandes (texto do story) enviadas.\n'
           '- **12ª leitura (10/11):** respostas a João Paulo (CTA de Face e Insta), Paulo Infante (quadro de validação) e Mateus Guisolffi (Insta travado no nome), no #chat-appyon, e parabéns ao Rundouglas no #vitórias: enviadas (toda resposta sugerida conta como enviada). Bruno Freitas e Eduarda Kelly: só reação.')
k = trocar(k, '| carloscs, Lucas Dusi |',
           '| João Paulo | Pergunta no chat (10/11 00h01): vídeos diferentes para Face e Insta? | | | **Resposta pública enviada em 10/11** (12ª leitura) | |\n'
           '| Paulo Infante | Pergunta no chat (09/11 20h21): Página do Face com 7 de 12 vídeos acima de 100 views, já pode pôr link? | | | **Resposta pública enviada em 10/11** (12ª leitura) | |\n'
           '| Mateus Guisolffi | Pergunta no chat (09/11 20h08): Insta novo travado no "next" do nome | | | **Resposta pública enviada em 10/11** (12ª leitura) | |\n'
           '| Rundouglas | 32 vendas em 7 dias (até 08/11), 10.157 cliques, 0,31% de clique em venda | | | **Parabéns enviado no #vitórias em 10/11** (12ª leitura), com 1 pergunta (de onde vieram os cliques). Se responder, só reagir | Se ajudar |\n'
           '| carloscs, Lucas Dusi |')
k = k.rstrip('\n') + '''

## ENVIADO (10/11/2026; respostas da 12ª leitura do Discord, no jeito do aluno)
**1. João Paulo, no #chat-appyon (responder a mensagem dele de 10/11 00h01):**
```
aqui faço o mesmo vídeo pros dois, sem automação
o cta manda pro story nos dois, e o link fica no story
no face eu tb comento como a página com o link, e quem comenta eu respondo e mando o link no direct na mão
aí não precisa de 2 versões
```
**2. Paulo Infante, no #chat-appyon (responder a mensagem dele de 09/11 20h21):**
```
pelo quadro de validação que passaram aqui no chat:
acima de 200 views nos 10 primeiros, a conta tá saudável e já pode ir pros de venda com copy validada
entre 100 e 200 é zona cinzenta: olha a retenção nos 3s
se tá acima de 50%, posta mais uns 5 a 10 e reavalia
se tá abaixo, o problema é o gancho, não a conta
```
**3. Mateus Guisolffi, no #chat-appyon (responder a mensagem dele de 09/11 20h08):**
```
já passaram essa dica aqui: quando trava no nome, cria pelo navegador do celular em vez do app
aí ele pede número e foto, mas vai
```
**4. Rundouglas, no #vitórias (responder a mensagem dele de 09/11 19h33):**
```
parabéns mano!! 32 numa semana é absurdo
esses cliques vieram mais do story ou da dm?
```
**Só reagir com emoji (sem texto):** a mensagem do Bruno Freitas (09/11 20h27) e a da Eduarda Kelly (09/11 13h46) no #vitórias.
'''
gravar('CONTATOS-ALUNOS.md', k)

# ---------------------------------------------------------------- CLAUDE.md
m = ler('CLAUDE.md')
m = trocar(m, '- **Discord lido até:** chat-appyon 09/11 10h34; vitórias-dólar 08/11 16h32 (11ª leitura, feita em 09/11 às 11h20; `HISTORICO-DISCORD/`; decisões em `COMUNIDADE-E-ESTRATEGIA.md`, 09/11 ~12h40). A próxima leitura começa daí.',
           '- **Discord lido até:** chat-appyon 10/11 00h15; vitórias-dólar 09/11 21h16 (12ª leitura, feita em 10/11 às 00h20; `HISTORICO-DISCORD/`; decisões em `COMUNIDADE-E-ESTRATEGIA.md`, 10/11 ~00h40). A próxima leitura começa daí.')
m = trocar(m, '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n',
           '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n'
           '- **10/11/2026 ~00h40, Discord, 12ª leitura:** nada muda no plano (o Rundouglas confirma ~317 cliques por venda: o gargalo é clique). Se o Insta der "Você não pode compartilhar links": pedir análise na hora e avisar; DM no Face segue a regra da 11ª leitura (se travar, a confirmação é com o documento do aluno, pelo app do Messenger: a Página está no perfil dele); nunca documento falso; corpo em takes de 15 s só com o prompt daqui (o modo de 15 s do Creative Hub deixa 5 s mudos); agente do Flow parado = projeto novo. Detalhe em `COMUNIDADE-E-ESTRATEGIA.md` (10/11 ~00h40).\n')
gravar('CLAUDE.md', m)

print('ok')
