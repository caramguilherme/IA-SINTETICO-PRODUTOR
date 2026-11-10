# Pente fino de 10/11/2026, parte 2: cabeçalhos e referências velhas nos outros documentos (só correções certas).
# Rodar uma vez, da raiz do repositório: python3 -I ferramentas-painel/r1011/pente_fino_1011_parte2.py
import pathlib, sys

R = pathlib.Path(__file__).resolve().parents[2]
feitos = []


def editar(nome, pares):
    p = R / nome
    t = p.read_text(encoding='utf-8')
    for a, b in pares:
        if t.count(a) != 1:
            sys.exit(f'{nome}: trecho não único ({t.count(a)}): {a[:70]}')
        t = t.replace(a, b)
    p.write_text(t, encoding='utf-8')
    feitos.append(nome)


def linha_inteira(nome, inicio):
    linhas = (R / nome).read_text(encoding='utf-8').split('\n')
    achou = [l for l in linhas if l.startswith(inicio)]
    if len(achou) != 1:
        sys.exit(f'{nome}: linha não única ({len(achou)}): {inicio[:60]}')
    return achou[0]


# CLAUDE.md: linha em branco antes da seção 2 e o piloto do 1.2 nos créditos
editar('CLAUDE.md', [
    ('\n## 2. Regras em vigor', '\n\n## 2. Regras em vigor'),
    ('Muse fora do ar para vários: não contar com ele.',
     'Muse fora do ar para vários: não contar com ele. **Kit do portal (10/11): ~201 créditos na contatocaram; o piloto do 1.2 em 360p, que estava no painel antigo do nora51, volta no painel do kit.**'),
])

# REGRAS-DO-AGENTE.md: cabeçalho, o 00-LEIA-PRIMEIRO e a régua velha da P46
editar('REGRAS-DO-AGENTE.md', [
    ('# REGRAS DO AGENTE (P1 a P45)', '# REGRAS DO AGENTE (P1 a P47)'),
    ('- 00-LEIA-PRIMEIRO.md: quais regras estão vigentes.',
     '- 00-LEIA-PRIMEIRO.md: o modelo de origem (UGC Pet e Dana), só histórico; as regras vigentes estão no `CLAUDE.md`, seções 2 e 5 (nota de 10/11/2026).'),
    ('(12) a régua das aulas: checkout de 18% a 20% dos cliques, abaixo de 10% = falta qualificação;',
     '(12) a régua das aulas: checkout de 18% a 20% dos cliques, abaixo de 10% = falta qualificação (**superada em 09/11**: a régua oficial da Central MVM dá checkout em ~3% dos cliques e venda em 0,30%, ~330 cliques por venda; `COMUNIDADE-E-ESTRATEGIA.md`, 11ª leitura);'),
])

# 00-LEIA-PRIMEIRO.md: aviso no topo
editar('00-LEIA-PRIMEIRO.md', [
    ('# Leia antes dos documentos de origem\n',
     '# Leia antes dos documentos de origem\n\n> **Nota de 10/11/2026 (pente fino):** este arquivo é do modelo de origem (Projeto UGC Pet e a Dana) e não descreve a Nora de hoje. As regras vigentes estão no `CLAUDE.md` (seções 2 e 5) e em `REGRAS-DO-AGENTE.md` (P1 a P47); os itens abaixo ficam só como histórico.\n'),
])

# LEIA-TUDO-ANTES.md: P1 a P47 e o Clone na lista principal (é obrigatório em todo vídeo, P46)
clone = linha_inteira('LEIA-TUDO-ANTES.md', '- `CLONE-DO-GUSTAVO-RESPOSTAS.md`')
editar('LEIA-TUDO-ANTES.md', [
    ('(as regras P1 a P45, movidas do `CLAUDE.md` em 06/11/2026)', '(as regras P1 a P47, movidas do `CLAUDE.md` em 06/11/2026)'),
    (clone + '\n', ''),
    ('**Método de roteiro e falas**\n', clone + ' **(obrigatório em todo vídeo, P46; estava por engano em "Só quando o pedido envolver" até 10/11)**\n\n**Método de roteiro e falas**\n'),
])

# PASSAGEM-DE-CONTA.md: regras P1 a P47 e o quadro "Onde está cada coisa"
editar('PASSAGEM-DE-CONTA.md', [
    ('o `REGRAS-DO-AGENTE.md` (P1 a P45)', 'o `REGRAS-DO-AGENTE.md` (P1 a P47)'),
    ('| Regras completas do agente (P1 a P45) |', '| Regras completas do agente (P1 a P47) |'),
    (linha_inteira('PASSAGEM-DE-CONTA.md', '| Regras em vigor, resumidas |'),
     '| Regras em vigor, resumidas | `CLAUDE.md`, seção 2 (a versão única desde 06/11) |'),
    (linha_inteira('PASSAGEM-DE-CONTA.md', '| Discord, DMs, aulas, estratégia |'),
     '| Discord, DMs, aulas, estratégia | `COMUNIDADE-E-ESTRATEGIA.md` (conversas inteiras em `HISTORICO-DISCORD/`; até onde foi lido: o marcador "Discord lido até" da seção 1 do `CLAUDE.md`) |'),
    (linha_inteira('PASSAGEM-DE-CONTA.md', '| Aulas e materiais |'),
     '| Aulas e materiais | `AULA-IORHAN-30-10-COPY-QUE-CONVERTE.md` (P42), `AULA-02-11-DO-MEDO-AO-DESEJO.md`, `AULA-03-11-TURBINANDO-CRIATIVOS-IORHAN.md` (materiais em `MATERIAIS-CALL-03-11/`), `AULA-06-11-VARIACOES-E-COPY-COM-IA-IORHAN.md` (links em `MATERIAIS-CALL-06-11/LEIA.md`), `AULA-09-11-DO-ZERO-AO-VIDEO-GUSTAVO.md`, `AULA-07-09-ANALISE-DE-FUNIL.md`, `CLONE-DO-GUSTAVO-RESPOSTAS.md` |'),
    (linha_inteira('PASSAGEM-DE-CONTA.md', '| Base do nora50 em diante |'),
     '| Base dos vídeos de hoje | `ROTEIRO-KIT-PORTAL-NORA51-54.md` (kit do portal, 10 e 11/11), `BIBLIOTECA-VIDEOS-VIRAIS.md` (seção 49: contas mineradas; 49.6: Soma Chhaya), `referencias-mineracao/`, `BANCO-DE-HEADLINES.md` |'),
])

# LICOES-FLOW-E-PROMPTS.md: o "claim" e o pedido de comentário foram revistos em 10/11
editar('LICOES-FLOW-E-PROMPTS.md', [
    ('- **Legenda (R17 e R20):** 3 a 5 hashtags do nicho; sem 222, "claim", "free", link (no Insta) e nome do app.',
     '- **Legenda (R17 e R20):** 3 a 5 hashtags do nicho; sem "free", link (no Insta) e nome do app. **Revisto em 10/11 ~01h15:** no Insta, a legenda pode pedir comentário com "claim" (palavra diferente a cada vídeo); no Face, sem pedido; na fala, pedido só depois do CTA (`COMUNIDADE-E-ESTRATEGIA.md`, 10/11 ~01h15).'),
])
cta = linha_inteira('LICOES-FLOW-E-PROMPTS.md', '- **CTA:** 3 partes (ganho → o que tem do outro lado, nas palavras do funil → a ação)')
editar('LICOES-FLOW-E-PROMPTS.md', [(cta, cta + ' **(Revisto em 10/11 ~01h15: o "claim" e o 222 voltam só no engajamento, depois do CTA.)**')])

# skill de métricas: régua nova e teste atual
editar('.claude/skills/metricas-nora/SKILL.md', [
    ('- **Teste em andamento (ver `CLAUDE.md`, seção 1):** o corpo, com o gancho fixo. Julgar corpo ou CTA',
     '- **Teste em andamento:** o que a seção 1 do `CLAUDE.md` disser (em 10/11: o kit do portal, curto x longo, contra o nora49). Julgar corpo ou CTA'),
    ('- **A medida final é o clique no Tracker** (~178 cliques por venda na comunidade em outubro).',
     '- **A medida final é o clique no Tracker** (régua oficial da Central MVM: ~330 cliques por venda, 0,30%; ~178 era a média da comunidade em outubro).'),
])

# CONTATOS-ALUNOS.md: o "nora54" mudou de sentido (o CTA curto no corpo A saiu do plano em 10/11)
editar('CONTATOS-ALUNOS.md', [
    ('## Pendências (06/11/2026)', '## Pendências (atualizado em 10/11/2026)'),
    ('voltar com o resultado do nora54 (versão curta). **Marcus:** voltar com o resultado do nora54 (CTA mais cedo).',
     'voltar com o resultado do kit do portal (versão curta x longa, CTA mais cedo; o "nora54 do corpo A" saiu do plano em 10/11). **Marcus:** voltar com o mesmo resultado (CTA mais cedo).'),
])

# PLANO-MVM: o estado de 19/10 e os itens do checklist que não valem mais
editar('PLANO-MVM-LEGACY-APPYON.md', [
    ('**Onde a Nora está (19/10, 20h15):**', '**(Estado de hoje: seção 1 do `CLAUDE.md`. O parágrafo abaixo é de 19/10 e ficou como histórico.)** **Onde a Nora está (19/10, 20h15):**'),
    ('- [ ] Esperar o aviso do Gustavo de que o Love Chart entrou no ar', '- [x] (superado: o Love Chart entrou em 24/10 e a Nora passou para o Manifestation em 27/10) Esperar o aviso do Gustavo de que o Love Chart entrou no ar'),
    ('- [ ] Comprar o Flow por 1 dólar no bot do Telegram', '- [x] (superado: a promoção de 1 dólar acabou, Discord de 09/11; e não ajudamos a comprar conta de bot) Comprar o Flow por 1 dólar no bot do Telegram'),
])

print('ok:', ', '.join(dict.fromkeys(feitos)))
