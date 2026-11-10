# Revisão da regra do "claim" e do pedido de comentário (pergunta do aluno, 10/11/2026 ~01h10:
# "pq no nora fica fora? quem falou pra ficar fora? é alguma lei/regra?").
# Rodar uma vez, da raiz do repositório: python3 -I ferramentas-painel/r1011/revisao_claim_comentario.py
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


# ---------------------------------------------------------------- COMUNIDADE
COM = '''
### 10/11/2026 ~01h15 - Revisão: o "claim" e o pedido de comentário (o aluno perguntou quem mandou tirar)
- **Pergunta do aluno:** "pq no nora fica fora? quem falou pra ficar fora? é alguma lei/regra?"
- **De onde a regra veio (busca nos documentos):** não é lei nem regra oficial que proíba. Foi decisão minha, de 30/10 a 03/11, juntando três coisas: (1) **a aula do Iorhan de 30/10 (P42):** "comente 222, feche a mão, salve" está no slide de "engaja, mas não vende", e o loop **antes** do CTA tira gente da passagem para o story; mas a própria aula diz "**se quiser engajamento, depois do CTA do story**" (não proíbe); (2) **o Garbellotto (03/11):** a melhor conta dele foi punida por "engajamento fake"; ele pedia comentário, mas não disse que foi a causa ("não sei dizer o motivo"); somei com o Mattias e o Adão (mesmo CTA e respostas iguais em massa) e tirei por precaução; (3) **o "claim"** saiu junto com os "rituais" e a "escolhida" (Clone R20, `BANCO-DE-HEADLINES.md`): **nenhuma fonte oficial falou da palavra.** O que existe de regra de plataforma: o Facebook reduz a entrega de post com "isca de engajamento" (pedir comentário, curtida ou compartilhamento em troca de algo): é distribuição menor no Face, não banimento.
- **Contra a regra, nos nossos números e nas fontes:** o corpo A, o nosso melhor, **ainda fala "Comment 222 to claim this energy"** no fim (só a legenda e o comentário fixado ficaram sem); o nora40 com "claim this energy: follow me, comment 222, send this video to yourself" foi o de mais envios e salvos da época; os virais do nicho com "comment 222" têm 2,5% a 4% de comentários, contra 0,8% a 1,7% sem (03/11); o Kaike pede comentário em toda copy e mede comentários ÷ views; a Soma Chhaya pede em toda legenda, e no 548 mil o pedido explícito ("Comment "I accept"") deu 5x mais comentário que o 1,2 mi da mesma sessão.
- **Decisão (minha, 10/11 ~01h15): fui duro demais; o pedido de comentário e o "claim" voltam, com 3 cuidados:** (1) **na fala, sempre depois do CTA do story** (a regra do Iorhan, que continua); (2) **no Insta, a legenda pode pedir** ("Comment "I accept" to claim this ✨"), com **palavra diferente a cada vídeo** ("I accept", "I receive", "thank you universe", "yes"…), nunca o mesmo pedido em todos (o padrão repetido é o que aparece nos casos de punição); **no Face, a legenda fica sem pedido** (isca de engajamento reduz a entrega lá), e o comentário da Página continua com o link; (3) nunca "claim" no gancho, na caixa do topo nem no story (o story é a leitura: "Open my reading"). **Quando:** do corpo novo em diante. Os vídeos de hoje (nora51 a nora53) e o nora54 ficam com a legenda igual à do nora49, para não misturar mais uma variável nos testes do gancho e do CTA.
- **Efeito na régua:** com o pedido na legenda, comentários ÷ views sobe sozinho; a comparação com os vídeos antigos passa a valer só entre vídeos com pedido. A medida final continua o clique no Tracker.
'''
c = ler('COMUNIDADE-E-ESTRATEGIA.md')
gravar('COMUNIDADE-E-ESTRATEGIA.md', c.rstrip('\n') + '\n' + COM)

# ---------------------------------------------------------------- CLAUDE.md
m = ler('CLAUDE.md')
m = trocar(m, '- **Legenda:** o gancho + "Your private reading is waiting in my story." + 3 a 5 hashtags do nicho (#manifestation e os signos; Clone R17 e R20); sem 222, "claim", "free" e nome do app (nada de #AuraliTrend).',
           '- **Legenda:** o gancho + "Your private reading is waiting in my story." + 3 a 5 hashtags do nicho (#manifestation e os signos; Clone R17 e R20); sem "free" e nome do app (nada de #AuraliTrend). **Revisto em 10/11 ~01h15 (o aluno perguntou quem mandou tirar o "claim": foi precaução minha, não regra oficial; `COMUNIDADE-E-ESTRATEGIA.md`):** do corpo novo em diante, **no Insta a legenda pode pedir comentário com "claim"** (molde da Soma Chhaya: "Comment "I accept" to claim this ✨"), com palavra diferente a cada vídeo; **no Face, sem pedido na legenda** (o Face reduz a entrega de isca de engajamento). nora51 a nora54 seguem com a legenda do nora49 (testes).')
m = trocar(m, '- Sem medo, ameaça, "keep your mouth shut", "antes que desapareça", loops antes do CTA, "chosen", rituais na caixa, 222 na legenda e no comentário (o 222 fica só como número fixo na tela).',
           '- Sem medo, ameaça, "keep your mouth shut", "antes que desapareça", loops antes do CTA, "chosen", rituais na caixa. Pedido de comentário (com "claim", 222 ou outra palavra) só **depois do CTA do story** na fala, e na legenda do Insta com palavra variada (revisão de 10/11); nunca no gancho, na caixa do topo nem no story.')
m = trocar(m, '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n',
           '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n'
           '- **10/11/2026 ~01h15, "claim" e pedido de comentário revistos (pergunta do aluno: "quem falou pra ficar fora?"):** não era regra oficial; foi precaução minha (Iorhan: loop antes do CTA atrapalha, "engajamento depois do CTA"; Garbellotto punido por "engajamento fake" sem saber a causa). Os nossos números e a Soma mostram que o pedido ajuda. Volta do corpo novo em diante: na fala depois do CTA, na legenda do Insta com palavra variada, fora da legenda do Face. Detalhe em `COMUNIDADE-E-ESTRATEGIA.md` (10/11 ~01h15).\n')
gravar('CLAUDE.md', m)

# ---------------------------------------------------------------- BIBLIOTECA (49.6)
b = ler('BIBLIOTECA-VIDEOS-VIRAIS.md')
b = trocar(b, 'Na Nora, comentário só como pergunta de verdade e sem "claim" (Garbellotto: punição por engajamento fake): "I accept" fica registrado, não entra.',
           '**Revisto em 10/11 ~01h15:** o pedido volta na Nora do corpo novo em diante (legenda do Insta com palavra variada, fala depois do CTA; Face sem pedido na legenda), `COMUNIDADE-E-ESTRATEGIA.md`.')
b = trocar(b, '(5) a legenda sempre pede o comentário com "claim", e quando o pedido é explícito ("Comment \\"I accept\\"") o comentário sobe 5x: na Nora, nada disso (pergunta de verdade, sem "claim").',
           '(5) a legenda sempre pede o comentário com "claim", e quando o pedido é explícito ("Comment \\"I accept\\"") o comentário sobe 5x: **na Nora, volta do corpo novo em diante** (revisão de 10/11 ~01h15: legenda do Insta com palavra variada, fala depois do CTA, Face sem pedido na legenda).')
gravar('BIBLIOTECA-VIDEOS-VIRAIS.md', b)

# ---------------------------------------------------------------- CLONE (R20)
k = ler('CLONE-DO-GUSTAVO-RESPOSTAS.md')
k = trocar(k, 'Fora: 222 e "claim" na legenda, "free", "money gifts",',
           'Fora: 222 e "claim" na legenda (**revisto em 10/11: volta na legenda do Insta do corpo novo em diante, com palavra variada; no Face, não**; `COMUNIDADE-E-ESTRATEGIA.md`, 10/11 ~01h15), "free", "money gifts",')
gravar('CLONE-DO-GUSTAVO-RESPOSTAS.md', k)
print('ok')
