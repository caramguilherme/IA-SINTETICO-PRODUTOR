# Pente fino do projeto (pedido do aluno, 10/11/2026 ~04h: "encontre tudo o que está quebrado, inconsistente,
# ineficiente ou não é mais necessário; corrija o que tem certeza").
# Parte 1: o CLAUDE.md (vai em toda mensagem) fica só com o estado atual; os itens superados da seção 1 e o diário
# de 06 a 08/11 vão INTEIROS, palavra por palavra, para o HISTORICO-CLAUDE-MD.md. Seção 2: regras que mudaram em 10/11.
# Rodar uma vez, da raiz do repositório: python3 -I ferramentas-painel/r1011/pente_fino_1011.py
import pathlib, sys

R = pathlib.Path(__file__).resolve().parents[2]
C = R / 'CLAUDE.md'
H = R / 'HISTORICO-CLAUDE-MD.md'
t = C.read_text(encoding='utf-8')
if '## 1. Estado atual (10/11/2026' in t:
    sys.exit('já aplicado')

i1 = t.index('## 1. Estado atual')
i2 = t.index('## 2. Regras em vigor')
sec1 = t[i1:i2]
linhas = sec1.split('\n')
bul = [l for l in linhas if l.startswith('- ')]


def pega(prefixo):
    achou = [l for l in bul if l.startswith(prefixo)]
    if len(achou) != 1:
        sys.exit(f'bullet não único ({len(achou)}): {prefixo}')
    return achou[0]


MANTER = {
    'conta': pega('- **Conta do Claude:**'),
    'doc': pega('- **Doc do MVM:**'),
    'funil': pega('- **Funil:** Manifestation (P41)'),
    'postado_rec': pega('- **Postado (mais recente):'),
    'postado': pega('- **Postado:** nora47'),
    'creditos': pega('- **Créditos do Flow (aluno, 09/11'),
    'contatos': pega('- **Contatos (P44):**'),
    'discord': pega('- **Discord lido até:**'),
    'contenthub': pega('- **Funil (Content Hub da Appyon, 06/11):**'),
    'datas': pega('- **Datas:**'),
}
SAEM = [l for l in bul if l not in MANTER.values()]

novo1 = '\n'.join([
    '## 1. Estado atual (10/11/2026 ~04h30 BRT)',
    MANTER['conta'],
    '- **Links desta conta:** dashboard Métricas da Nora https://claude.ai/artifact/GnvCkx6wnMNqcJE6BVGaUP (asset do CSV `/_blob/5ce737b87968e3e7f098155deedfe70c`, dataset na versão 13, leituras até 09/11 23h04) · painel nora48 https://claude.ai/artifact/QQpxR4dxqovuceqfrsHNU5 · painel nora49 https://claude.ai/artifact/GFB4scmCX4tDB54bmhYXv3 · painel nora50 (postado) https://claude.ai/artifact/55Ak6Ln2biRLw2mrDyoWPi · **nora51 https://claude.ai/artifact/AXQp5m7g6jjn7RvWSQXMQY · nora52 https://claude.ai/artifact/L36PatLZXAraEnD56kVqiV · nora53 https://claude.ai/artifact/6LvW1Pxu3K7DuA9DEU8qbS: ainda mostram a fórmula do corpo A, cancelada em 10/11 ~01h45 (não usar); vão ser republicados nos mesmos links com o kit do portal, mais um painel novo para o nora54.** Links das contas antigas e a história dos números (renumeração de 09/11): `HISTORICO-CLAUDE-MD.md`.',
    MANTER['doc'],
    MANTER['funil'],
    '- **Agora (10/11): o kit do portal (decisão do aluno, 10/11 ~01h45; `ROTEIRO-KIT-PORTAL-NORA51-54.md`):** modelado dos reels da @soma_chhaya (grade, números e falas em `BIBLIOTECA-VIDEOS-VIRAIS.md` 49.6 e `referencias-mineracao/soma_chhaya_2026-11-10/`; a call do Gustavo de 09/11 em `AULA-09-11-DO-ZERO-AO-VIDEO-GUSTAVO.md`), sem pré-gancho, cena nova com cara de celular (`kitportal-IMG`), 14 falas numa sessão só (~201 créditos na contatocaram). **17h nora51 curto · 19h30 nora52 longo (compara com o nora49) · 22h nora53 curto · 00h30 (já 11/11) nora54 curto**; em 11/11, os 4 horários com o portal "hoje"; depois de 11/11, kit novo sem portal. **Esperando do aluno:** as 4 imagens da `kitportal-IMG` (campos no chat de 10/11 ~01h50, ajuste dos campos do `LICOES` de 09/11 para a selfie) e a avaliação das falas no Clone do Gustavo; depois disso eu escrevo o LIVRE e as 14 movimentações (P32: pela imagem aprovada) e publico os painéis (o do nora51 traz a geração do kit inteiro). Saíram do plano: o teste da pedra e o teste do CTA curto no corpo A.',
    MANTER['postado_rec'],
    MANTER['postado'],
    '- **Métricas (resumo; o detalhe está no `METRICAS-NORA-LEIA.md` e no CSV):** o corpo A limpo venceu o corpo B (06/11); finais do Insta: nora49 2.011 views, 19 follows, 10 visitas ao perfil; nora48 1.633, 10, 5. Postar perto das 19h30 dobrou a fatia dos EUA contra a 01h. Só ~8% a 10% chegam ao CTA dos 63 s no corpo A. Tracker do Manifestation, 27/10 a 09/11 10h56: 22 cliques reais (20 Insta, 2 Face), 12 no fim do quiz, 0 checkout. Régua oficial (Central MVM, 10% melhores): ~330 cliques por venda (0,30%); o Rundouglas fez 0,31% (32 vendas em 10.157 cliques, 12ª leitura). **O gargalo é o número de cliques.**',
    '- **Contagem para a validação (`VALIDACAO-CONTA-E-AVATAR.md`):** 17 vídeos do Manifestation no Insta (os 15 até 06/11: nora36 a nora48, face01 e face02; mais o nora49 e o nora50). A janela de 40 vídeos com copy validada não fechou. Não mexer na avatar desta conta (Clone R19 e R21).',
    MANTER['creditos'],
    '- **Infraestrutura:** proxy renovada até 06/12 14h52 e GeeLark até 06/12 13h48 (renovar os dois em 05/12: nenhum tem renovação automática); minutos do GeeLark em 06/11: 766 do pacote + 60 bônus (dá até ~26/11; comprar outro pacote quando passar de ~300). **DM automática no Face adiada pelo aluno (06/11): não propor de novo até ele trazer o assunto.**',
    MANTER['contatos'],
    MANTER['discord'],
    '- **Volume:** a Central pede 2 Insta + 2 páginas do Face e 6 vídeos de venda por dia em cada; a Nora faz **4 por dia no Insta** (17h, 19h30, 22h, 00h30), cada um com Take 1 novo, e no Face os mesmos 4 + variações de 0 crédito. **O 2º perfil e os 6 por dia estão adiados pelo aluno: não propor até ele trazer o assunto** (`COMUNIDADE-E-ESTRATEGIA.md`, 07 e 09/11).',
    '- **Clone do Gustavo (NotebookLM, só abre com o login do aluno):** respostas R1 a R21 em `CLONE-DO-GUSTAVO-RESPOSTAS.md` (leitura obrigatória em todo vídeo); as regras que saíram dele estão na seção 2 e na P46; perguntas sugeridas no fim do arquivo. Restrição de país da Página: ligada (EUA, Canadá, Reino Unido, Austrália, Nova Zelândia; `FATOS-DO-ALUNO.md`). Tier 1 Bronze: 80% na 1ª cobrança, 5% na recorrência; 10% a partir de 101 vendas no mês. #AuraliTrend: fora.',
    '- **Pendente do aluno:** (1) a `kitportal-IMG` e o Clone (acima); (2) as métricas do nora50 (~10 h e ~24 h) e o Tracker de 10/11; (3) repostar o story-0311 antes das 22h55 de 10/11; (4) os prints dos comentários do nora48 e do nora49; (5) o link da pasta de vídeos da aula de 04/09 (11ª leitura); (6) os vídeos com som aprovados em 06/11 da claire_mayaus (1,4 mi e 956 mil) e da iamlinda.bennett (171 mil e 53,9 mil), se ainda valerem (`BIBLIOTECA-VIDEOS-VIRAIS.md` 49.2 e 49.3). **Aviso oficial de 22/09: não copiar vídeo de quem vende Appyon** (modelar a estrutura e reescrever a fala).',
    MANTER['contenthub'],
    MANTER['datas'],
    '',
])

t = t[:i1] + novo1 + t[i2:]

# ---------------------------------------------------------------- seção 2
def trocar(a, b):
    global t
    if t.count(a) != 1:
        sys.exit(f'trecho não único ({t.count(a)}): {a[:70]}')
    t = t.replace(a, b)

trocar('nora51 a nora54 seguem com a legenda do nora49 (testes).',
       'Já vale no kit do portal (nora51 a nora54).')
trocar('Take 1 diz para quem é nos 3 primeiros segundos.',
       'Take 1 diz para quem é nos 3 primeiros segundos (no kit do portal: a data do dia na fala + a qualificação na caixa do topo, "if you keep seeing 11:11").')
trocar('- **Uma variável por vez** (Allan): o gancho do tsunami fica (dobrou as views); agora testa o corpo. Até a 1ª venda,',
       '- **Uma variável por vez** (Allan), salvo decisão do aluno (o kit do portal de 10/11 muda várias de uma vez; o controle é o nora49). Até a 1ª venda,')
linha_n50 = [l for l in t.split('\n') if l.startswith('- **nora50:** fatia "manifesta e nada chega"')]
if len(linha_n50) != 1:
    sys.exit('linha do nora50 não achada')
trocar(linha_n50[0] + '\n', '')
trocar('**A medida final é o clique no Tracker** (~178 cliques por venda na comunidade).',
       '**A medida final é o clique no Tracker** (régua oficial: ~330 cliques por venda, 0,30%; ~178 era a média da comunidade em outubro).')
trocar('**Ordem dos testes (uma variável por vez, Clone R13):** gancho (nora50) → CTA com motivos (nora51) → prova do Trustpilot antes do CTA → efeitos sonoros (impact no corte do pré-gancho) → música emocional (~20% a 25%); do 3º em diante, 0 crédito, na edição.',
       '**Ordem dos testes (uma variável por vez, Clone R13):** o gancho e o CTA foram para o kit do portal (curto x longo, contra o nora49); depois: prova do Trustpilot antes do CTA → efeitos sonoros (impact no corte do pré-gancho) → música emocional (~20% a 25%), todos a 0 crédito, na edição.')
trocar('- **Pré-gancho (Clone R8 e R10):** do nicho,',
       '- **Pré-gancho (Clone R8 e R10; o kit do portal não tem, como os maiores da Soma Chhaya):** do nicho,')

# ---------------------------------------------------------------- seção 4: diário de 06 a 08/11 vai para o histórico
j1 = t.index('## 4. Diário de decisões')
j2 = t.index('## 5. Status das regras')
sec4 = t[j1:j2].split('\n')
fica, vai = [], []
for l in sec4:
    if l.startswith('- **06/11/2026') or l.startswith('- **07/11/2026') or l.startswith('- **08/11/2026'):
        vai.append(l)
    else:
        fica.append(l)
fica[0] = '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 09/11 estão em `HISTORICO-CLAUDE-MD.md`)'
# entrada do pente fino
fica.insert(1, '- **10/11/2026 ~04h30, pente fino do projeto (pedido do aluno: "encontre tudo o que está quebrado, inconsistente, ineficiente ou não é mais necessário"):** a seção 1 ficou só com o estado atual e o diário de 06 a 08/11 foi para o `HISTORICO-CLAUDE-MD.md` (inteiros, palavra por palavra); regras da seção 2 atualizadas com as decisões de 10/11 (legenda do kit, data no Take 1, régua de ~330 cliques, ordem dos testes); P1 a P47 corrigido nos cabeçalhos; artefatos apagados (`undefined/`, `__pycache__`). Lista completa do que foi corrigido e do que ficou para o aluno decidir em `COMUNIDADE-E-ESTRATEGIA.md` (10/11 ~04h30).')
t = t[:j1] + '\n'.join(fica) + t[j2:]
C.write_text(t, encoding='utf-8')

# ---------------------------------------------------------------- histórico
h = H.read_text(encoding='utf-8').rstrip('\n')
h += ('\n\n## Movido do CLAUDE.md em 10/11/2026 (pente fino): estados da seção 1 superados de 06 a 10/11\n'
      'Copiados palavra por palavra. O que vale hoje está na seção 1 do `CLAUDE.md`. Atenção: nestes itens, "nora50" antes de 09/11 23h15 é a pedra (depois renumerada para nora52 e cancelada em 10/11), e "nora51 a nora54" são os planos antigos do corpo A, substituídos pelo kit do portal (10/11 ~01h45).\n\n'
      + '\n'.join(SAEM)
      + '\n\n## Movido do CLAUDE.md em 10/11/2026 (pente fino): diário de decisões de 06 a 08/11\n\n'
      + '\n'.join(vai) + '\n')
H.write_text(h, encoding='utf-8')
print('ok: saíram', len(SAEM), 'itens da seção 1 e', len(vai), 'do diário; CLAUDE.md agora com', len(t), 'caracteres')
