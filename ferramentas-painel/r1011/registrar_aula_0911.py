# Registra a call do Gustavo de 09/11 ("Do zero ao vídeo que vende", Loom colado pelo aluno em 10/11 ~01h)
# nos documentos. Rodar uma vez, da raiz do repositório: python3 -I ferramentas-painel/r1011/registrar_aula_0911.py
import pathlib, sys

R = pathlib.Path(__file__).resolve().parents[2]
LOOM = 'https://www.loom.com/share/322a1f37ec7648ef9035b10643e98b0b'


def ler(n):
    return (R / n).read_text(encoding='utf-8')


def gravar(n, t):
    (R / n).write_text(t, encoding='utf-8')


def trocar(texto, velho, novo):
    if texto.count(velho) != 1:
        sys.exit(f'trecho não único ({texto.count(velho)}): {velho[:70]}')
    return texto.replace(velho, novo)


def depois_da_linha(texto, inicio, novo):
    linhas = texto.split('\n')
    achou = [i for i, l in enumerate(linhas) if l.startswith(inicio)]
    if len(achou) != 1:
        sys.exit(f'âncora não única ({len(achou)}): {inicio[:60]}')
    i = achou[0]
    return '\n'.join(linhas[:i + 1] + novo.split('\n') + linhas[i + 1:])


# ---------------------------------------------------------------- LEIA-TUDO-ANTES
t = ler('LEIA-TUDO-ANTES.md')
t = depois_da_linha(t, '- `AULA-06-11-VARIACOES-E-COPY-COM-IA-IORHAN.md`',
                    '- `AULA-09-11-DO-ZERO-AO-VIDEO-GUSTAVO.md` (call do Gustavo de 09/11, "Do zero ao vídeo que vende": avatar pelo blueprint, pré-gancho e corpo na mesma cena, Agente do Flow, FusionZ, CapCut, constância da voz, mineração e a Soma Chhaya como referência; resumo de tudo, a transcrição está no Loom; colado pelo aluno em 10/11/2026)')
gravar('LEIA-TUDO-ANTES.md', t)

# ---------------------------------------------------------------- PLANO-MVM
p = ler('PLANO-MVM-LEGACY-APPYON.md')
p = trocar(p, '- **Call do Gustavo de 09/11 à noite ("do zero ao vídeo que vende", avatar, blueprint, animação):** aconteceu; gravação ainda não vista (procurar no #gravações).',
           f'- **Call do Gustavo de 09/11 à noite, "Do zero ao vídeo que vende – Step by step" (Loom, ~1h06, colado pelo aluno em 10/11 ~01h):** {LOOM}. Resumo inteiro em `AULA-09-11-DO-ZERO-AO-VIDEO-GUSTAVO.md`: avatar pelo blueprint (Pinterest e Pexels como ideia, nunca famoso), pré-gancho de 4 s com a avatar fazendo a ação e a imagem do corpo editada a partir da do gancho, Agente do Flow com o Gerador de animação, FusionZ (nomes 0, 1, 2… e corte seco), CapCut, constância da voz (prompt de voz ou Personagens do Flow), mineração no começo do dia e a Soma Chhaya como "aula de manifestação e de copy".')
p = depois_da_linha(p, '- **Lower Priority no Flow (Coelho e Yuka, 09/11 21h50):**',
                    '- **Da call do Gustavo de 09/11 (`AULA-09-11-DO-ZERO-AO-VIDEO-GUSTAVO.md`):** no Agente, "Nunca pedir", 9:16, 1 saída; se um clipe falhar, "gere o prompt N"; se não renomear, "renomeie os arquivos conforme especificado"; se continuar falhando, gerar aquele à mão. Ele pediu 15 s e o Flow fez 10. **Recusa por política:** mandar a imagem e o erro ao Claude e pedir um prompt limpo, ou só tentar de novo. **Voz constante:** salvar o prompt de voz (é ele que define a voz no Omni Flash; o recomendado) ou criar um **Personagem** no Flow (projeto → Personagens → imagem, nome, voz, "personalizar performance" → usar @Nome no prompt; precisa ser criado em cada conta do Flow). Low Priority: voz pior e áudio de fundo.\n'
                    '- **Pré-gancho e corpo na mesma cena (Gustavo, 09/11):** a imagem do corpo sai da imagem do gancho editada no Nano Banana, mostrando o resultado da ação (o pote inteiro do gancho aparece quebrado na mesa no corpo).')
p = depois_da_linha(p, '- **Golpe do "confirme que é humano" (Bruno Freitas, vitórias 09/11 20h27):**',
                    '- **Quando a conta flopou (Gustavo, call de 09/11):** ~30 a 40 vídeos, todos abaixo de 100 views. Insta: resetar o emulador e criar conta nova; Face: passar a página para outro perfil e criar página nova. Nos 10 primeiros reels, 3 dígitos de views = conta boa. Conta que entrega 200 a 300 views e não vende: o problema são os vídeos (repetitivos, iguais aos dos outros, fatia de público errada), não a conta.')
gravar('PLANO-MVM-LEGACY-APPYON.md', p)

# ---------------------------------------------------------------- LICOES
L = '''
### 10/11/2026 - Call do Gustavo de 09/11 ("Do zero ao vídeo que vende"; `AULA-09-11-DO-ZERO-AO-VIDEO-GUSTAVO.md`)
- **Nomes em ordem para a FusionZ:** ela junta em ordem alfanumérica. Todo painel nomeia as peças na ordem do vídeo: `noraNN-PRE` < `noraNN-T01` < `noraNN-T02`… (com 2 dígitos: T01 a T09, depois T10). Pré-gancho reaproveitado de outro vídeo (ex.: `nora34-PRE`) também tem de cair antes; na dúvida, renomear para `noraNN-00-PRE`. Juntar sem transição (corte seco): com transição a FusionZ desfoca a troca de take.
- **Recusa por política no Flow:** o aluno me manda o print do erro e a imagem usada; eu devolvo o prompt limpo (o mesmo que o Gustavo faz com o Claude). Antes, uma nova tentativa igual às vezes passa.
- **Duração:** pedir 15 s não garante 15 s (na aula saiu de 10). Conferir a duração do clipe antes de baixar.
- **Voz:** continua o perfil de voz no LIVRE (o prompt de voz é o método que o Gustavo recomenda). Personagem do Flow (@Nome) só se a voz variar entre takes do corpo novo; ele vale só na conta do Flow em que foi criado.
- **Corpo novo:** a imagem do corpo sai da imagem do pré-gancho editada (o "depois" da ação, na mesma cena), para o gancho e o corpo parecerem um vídeo só.
'''
l = ler('LICOES-FLOW-E-PROMPTS.md')
gravar('LICOES-FLOW-E-PROMPTS.md', l.rstrip('\n') + '\n' + L)

# ---------------------------------------------------------------- COMUNIDADE
COM = f'''
### 10/11/2026 ~01h - Call do Gustavo de 09/11, "Do zero ao vídeo que vende" (Loom colado pelo aluno; `AULA-09-11-DO-ZERO-AO-VIDEO-GUSTAVO.md`)
- **Link:** {LOOM} (~1h06; a gravação que pedi na 12ª leitura).
- **O que é:** produção do zero ao vídeo, sem foco em copy: avatar pelo blueprint, pré-gancho de 4 s (a avatar põe o pêndulo num pote e ele estilhaça), imagem do corpo editada a partir da do gancho, Gerador de animação + Agente do Flow (Omni 1.2), FusionZ (nomes 0, 1, 2…, corte seco), CapCut (legenda na altura dos olhos, piano sem copyright). Nas perguntas: voz constante pelo prompt de voz (recomendado) ou Personagens do Flow; texto na tela converte pouco; mineração ~30 min no começo do dia; **"Ctrl+C, Ctrl+V é preguiça"**: referências de fora, adaptadas; **Soma Chhaya = "aula de manifestação e de copy", "fazer um NotebookLM dela é uma boa ideia"**; flopou = 30 a 40 vídeos abaixo de 100; conta com 200 a 300 views que não vende = problema nos vídeos e na fatia de público.
- **Para a Nora (decisão minha):** nada muda nos vídeos de hoje. No corpo novo: (1) gancho e corpo na mesma cena (a imagem do corpo sai da do pré-gancho, editada, 0 crédito); (2) **a copy modelada da Soma Chhaya**, a 3ª indicação dela (Matheus Baffa, Felps, Gustavo): pedido ao aluno, 4 ou 5 reels mais vistos dela (baixados ou gravados com som) + print da grade com as views; eu transcrevo e monto a estrutura, sem copiar a fala; (3) voz no prompt de voz de sempre; (4) nomes em ordem para a FusionZ. Fora: avatar a partir de foto de Pinterest/Pexels, o CTA genérico da aula ("some people even get emotional…") e "comment 1111 to seal this energy". Detalhe na seção 7 da aula.
'''
c = ler('COMUNIDADE-E-ESTRATEGIA.md')
gravar('COMUNIDADE-E-ESTRATEGIA.md', c.rstrip('\n') + '\n' + COM)

# ---------------------------------------------------------------- CLAUDE.md
m = ler('CLAUDE.md')
m = trocar(m, '- **09/11/2026 ~23h15, RENUMERAÇÃO (pedido do aluno: o número segue a ordem de postagem):**',
           f'- **10/11/2026 ~01h, call do Gustavo de 09/11 ("Do zero ao vídeo que vende", {LOOM}; `AULA-09-11-DO-ZERO-AO-VIDEO-GUSTAVO.md`):** o corpo novo sai **modelado da Soma Chhaya** (3ª indicação: Matheus Baffa, Felps e o Gustavo, "aula de manifestação e de copy"), com gancho e corpo na mesma cena (imagem do corpo editada a partir da do pré-gancho). **Pedido ao aluno:** 4 ou 5 reels mais vistos da @soma_chhaya (baixados ou gravados com som) + print da grade com as views.\n'
           '- **09/11/2026 ~23h15, RENUMERAÇÃO (pedido do aluno: o número segue a ordem de postagem):**')
m = trocar(m, '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n',
           '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n'
           '- **10/11/2026 ~01h, call do Gustavo de 09/11 (Loom colado pelo aluno):** nada muda nos vídeos de hoje; corpo novo modelado da Soma Chhaya, gancho e corpo na mesma cena, voz no prompt de voz de sempre, nomes dos arquivos em ordem para a FusionZ. Detalhe em `AULA-09-11-DO-ZERO-AO-VIDEO-GUSTAVO.md` (seção 7) e `COMUNIDADE-E-ESTRATEGIA.md` (10/11 ~01h).\n')
gravar('CLAUDE.md', m)

print('ok')
