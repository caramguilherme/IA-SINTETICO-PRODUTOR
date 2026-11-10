# Registra a resposta do joao (Sargento, joao00527) de 09/11 17h29 à DM de 03/11 e a resposta sugerida.
# Rodar uma vez, da raiz do repositório: python3 -I ferramentas-painel/r1011/registrar_joao.py
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


def depois_da_linha(texto, inicio, novo):
    linhas = texto.split('\n')
    achou = [i for i, l in enumerate(linhas) if l.startswith(inicio)]
    if len(achou) != 1:
        sys.exit(f'âncora não única ({len(achou)}): {inicio[:60]}')
    i = achou[0]
    return '\n'.join(linhas[:i + 1] + novo.split('\n') + linhas[i + 1:])


RESP = ('"Salve irmão, perdão pela demora / Então, com certeza oque me fez destravar foram os ganchos / '
        'Eu aprimorei os ganchos e os videos começaram a entregar / No stories eu coloco algo bem basico como '
        '\'Essa mensagem nao chegou pra voce por acaso, o universo preparou algo grandioso para voce, clique aqui e descubra\' / '
        'Tipo isso / Só não para irmão, vc vai destravar também"')

STORY_EN = ('"This message didn\'t reach you by chance. ✨ The universe has prepared something big for you. '
            'Tap below and find out." + adesivo "Open my reading"')

# ---------------------------------------------------------------- CONTATOS
k = ler('CONTATOS-ALUNOS.md')
k = trocar(k, 'DM do aluno em 03/11 14h57: (1) o que fez o Manifestation funcionar (formato, copy, Insta ou Face)? (2) o que põe no story para clicarem? **Sem resposta até 04/11 ~12h** | | Não mandar outra DM; reagir em público; se responder, anotar e responder | |',
           'DM do aluno em 03/11 14h57: (1) o que fez o Manifestation funcionar (formato, copy, Insta ou Face)? (2) o que põe no story para clicarem? **Respondeu em 09/11 17h29:** o que destravou "com certeza" foram os **ganchos** ("aprimorei os ganchos e os vídeos começaram a entregar"); no story, "algo bem básico": "Essa mensagem não chegou pra você por acaso, o universo preparou algo grandioso para você, clique aqui e descubra" | Teste do gancho em curso (nora52, a pedra, contra o tsunami); o texto dele entra no rodízio do story a partir de 12/11 (sem portal) | **Resposta enviada em 10/11** (obrigado + 1 pergunta: o gancho que ele aprimorou foi a cena do começo ou a frase). Esperar; voltar com o resultado do story | Sim, se ajudar |')
k = trocar(k, '- **12ª leitura (10/11):**',
           '- **joao (Sargento):** respondeu em 09/11 17h29 (ganchos + texto do story); resposta enviada em 10/11. Esperar.\n- **12ª leitura (10/11):**')
k = k.rstrip('\n') + '''

## ENVIADO (10/11/2026; DM ao joao (Sargento), depois da resposta dele de 09/11 17h29; uma mensagem só)
```
valeu demais joao, ajudou mt!!
aqui foi igual, quando troquei o gancho a view dobrou
vou testar esse teu texto no story, o meu tá bem direto, só "toca aqui que tua leitura tá te esperando"
quando vc fala que aprimorou os ganchos, foi mais a cena do começo ou a frase que a avatar fala?
```
'''
gravar('CONTATOS-ALUNOS.md', k)

# ---------------------------------------------------------------- FATOS
f = ler('FATOS-DO-ALUNO.md')
f = depois_da_linha(f, '- **DMs de 03/11/2026 sem resposta (prints do aluno, 04/11 ~12h):**',
                    f'- **joao (Sargento) (joao00527) respondeu em 09/11/2026 às 17h29** (print do aluno, 10/11 ~00h40): {RESP}. Resposta do aluno enviada em 10/11 (`CONTATOS-ALUNOS.md`).')
gravar('FATOS-DO-ALUNO.md', f)

# ---------------------------------------------------------------- COMUNIDADE
COM = f'''
### 10/11/2026 ~00h45 - joao (Sargento, 347 vendas em outubro no Manifestation): ganchos e um story "bem básico"
- **O que ele disse (DM, 09/11 17h29, resposta à DM de 03/11):** {RESP}
- **Para a Nora (decisão minha):**
  1. **Gancho:** bate com o que já fazemos (o tsunami dobrou as views; hoje às 19h30 o nora52 testa o gancho do nicho, a pedra, contra o nora49). A pergunta de volta (cena ou frase) decide onde mexer primeiro nos próximos: pré-gancho (cena) ou Take 1 (frase).
  2. **Story:** o texto dele é parecido com o do story-0611 ("You're not here by accident. / Your private reading is waiting below."), que deu 0 toque em 18 viewers, contra 3 em 18 do story-0311 (instrução direta). Amostras pequenas, e o dele tem duas coisas que o 0611 não tinha: a promessa de algo bom ("o universo preparou algo grandioso") e a ação clara ("clique aqui e descubra"). **Hoje e amanhã (até o portal de 11/11) fica o story-0311.** **A partir de 12/11** o story-0311 perde o portal e entra o rodízio de 2 textos, um por dia, medindo toques ÷ viewers: (a) "Tap below: your private reading is waiting for you." e (b) o do joao em inglês: {STORY_EN}. Os dois com o link, a mesma imagem (story-3110) e o mesmo adesivo, para só o texto mudar. O que tiver mais toques vira a base do lote de 7.
'''
c = ler('COMUNIDADE-E-ESTRATEGIA.md')
gravar('COMUNIDADE-E-ESTRATEGIA.md', c.rstrip('\n') + '\n' + COM)

# ---------------------------------------------------------------- CLAUDE.md
m = ler('CLAUDE.md')
m = trocar(m, '- **Contatos (P44):** Jessica (respondida em 06/11, esperar);',
           '- **Contatos (P44):** joao (Sargento) respondeu em 09/11 17h29 (ganchos; story "bem básico"), resposta enviada em 10/11, esperar; Jessica (respondida em 06/11, esperar);')
m = trocar(m, '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n',
           '## 4. Diário de decisões (as novas entram aqui, datadas; as anteriores a 06/11 ~02h30 estão em `HISTORICO-CLAUDE-MD.md`)\n'
           '- **10/11/2026 ~00h45, joao (Sargento):** destravou pelos ganchos; story "bem básico" ("essa mensagem não chegou por acaso... clique aqui e descubra"). O story-0311 fica até 11/11; a partir de 12/11, rodízio de 2 textos de story (o 0311 sem o portal x o do joao em inglês), um por dia, mesma imagem e adesivo, medindo toques ÷ viewers. Detalhe em `COMUNIDADE-E-ESTRATEGIA.md` (10/11 ~00h45).\n')
gravar('CLAUDE.md', m)

print('ok')
