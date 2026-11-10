# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'.')
import data, reuse
OUT='/home/user/IA-SINTETICO-PRODUTOR/'
CRED={4:7,6:10,8:12,10:15}
LEIT=("19/10/2026: antes de escrever li, com a ferramenta de leitura e inteiros, os mesmos arquivos de `LEIA-TUDO-ANTES.md` que registrei no nora25 de hoje (`CLAUDE.md`, `00-LEIA-PRIMEIRO.md`, `PROJETO-Dana.md`, `LICOES-FLOW-E-PROMPTS.md`, `DNA Visual - Dana.md`, `DNA Visual - Nora.md`, `DNA Visual - Nora v2.md`, `REGISTRO-DE-PERSONAS.md`, `hooks.md` com a seção 7, `Formatos Narrativos - Problema e Cenario.md`, `Exemplos de Roteiros - 2 Formatos.md`, `ctas.md`, `COMUNICACAO-VISCERAL-E-FALADA.md`, `BIBLIOTECA-BODIES.md`, `BIBLIOTECA-COLD-READING.md`, `BIBLIOTECA-COPY.md`, `BIBLIOTECA-COPY-100-ROTEIROS.md`, `PESQUISA-PUBLICO.md`, `BIBLIOTECA-VIDEOS-VIRAIS.md`, `BIBLIOTECA-PRE-GANCHOS.md`, `Prompts.txt`, `CHECKLIST-DE-PRODUCAO.md`, `PAPEL-AGENTE-FLOW.md`, `GUIA-CREATIVE-HUB.md`, `PLANO-CREDITOS-R004-R005.md`, `PASSO-A-PASSO-R003-HUB.md`, `PASSO-A-PASSO-R004-R005.md`, `EXEMPLO-ROTEIRO-APROVADO-FIGADO.md`, `EXEMPLO-PACOTE-FIGADO.md`, `ROTEIRO-R001` a `ROTEIRO-R005`, `STORY-R001` a `STORY-R003`, `ROTEIRO-LOVECHART-RESERVA-SEU-PADRAO-TEM-NOME.md`, `STORY-LOVECHART-RESERVA.md`, `TAKE-NOVO-R001-V6.txt`, `TAKE-NOVO-R002-V6.txt`) e o briefing do Love Chart (`BRIEFING-LOVECHART.md`, a página https://briefing-lovechart.pages.dev/). O `CLAUDE.md` foi recarregado no início deste turno com as mudanças de hoje. `PAINEL-MODELO.html` foi lido (CSS e script; linhas longas cortadas) e o formato do pacote conferido no painel do R004. `FOTO-PERFIL-DANA.md` não foi lido (só vale para foto de perfil).")
CONF=("**Conferência da seção 9 de COMUNICACAO-VISCERAL e do hook visual (hooks.md, seção 1):** dá para imaginar uma cena concreta só ouvindo cada fala: sim; as frases soam como conversa (frases curtas, firmes, segunda pessoa): sim; a espectadora reconhece uma situação real (reler a mensagem, ensaiar a conversa, sentir mais fundo à noite), não um desejo genérico: sim; o benefício preserva o alcance do fato (o quiz \"encontra o Vênus, dá nome ao padrão e mostra o par perfeito\"; a Nora não diz que a pessoa existe nem que o amor chega): sim; nenhum número, depoimento, preço ou prazo de resultado inventado: sim; o mecanismo (\"o signo solar mostra quem você é, o Vênus mostra como você ama\") é o do próprio funil e vem com \"in astrology\": sim; a promessa é anunciada antes do CTA e a entrega completa fica no story (P6): sim; o áudio contínuo cabe nos takes de 10 s (cada fala tem de 20 a 22 palavras): sim. Hook visual: o objeto está na mão, perto da lente, com contraste contra a roupa escura e neutra, e já em ação (balança, é mostrado ou apontado): sim às duas perguntas.")
def render(k,v):
    n=len(v['takes']); pre=v['pre']
    tot=pre['dur']+n*10
    cred=CRED[pre['dur']]+n*CRED[10]
    L=[]
    L.append(f"# {v['id']} — roteiro completo ({n} takes + pré-gancho), funil LOVE CHART (19/10/2026)\n")
    L.append(f"Status: **aprovado pelo aluno em 19/10/2026; atualizado para a Nora v2 no mesmo dia (identidade, figurino, cenário e IMAGEM 1 pela Central de imagens).** Persona: **Nora v2** (Nora Kensley, @norakensleytarot), a avatar nova de 19/10/2026. Funil ativo: **Love Chart** (link só no story: sem DM e sem falar de afiliado). Postagem prevista: 19/10/2026 (nora25 a nora28 sobem no mesmo dia). Créditos do Flow não são mais um limite (o aluno informou que vão cair 1000), então o roteiro é o longo, com o melhor pré-gancho que a biblioteca de virais permite, e não o micro. Falas em inglês dos EUA; a tradução é só para o aluno aprovar. Dor {v['dor']}. {v['formato']}. Duração planejada: pré-gancho de {pre['dur']} s + {n} takes de 10 s = {tot} s.\n")
    L.append("## Leitura obrigatória (registro)\n"+LEIT+"\n"+CONF+"\n")
    L.append("## Base do curso usada (registro)\n"+'\n'.join('- '+b for b in v['base'])+"\n- **Funil Love Chart:** sem desenho do rosto, iniciais ou data de encontro; sem app, preço, assinatura, comissão, afiliado, Aura, \"92%\" ou \"2.1M\"; \"free quiz\" sim, app/leitura grátis não; \"perfect match\" é o nome do que o quiz mostra. **P15 usado:** garantia pessoal, escassez e ameaça suave de azar (só onde está marcado nas notas).\n")
    L.append("## Virais usados como modelo (peça por peça)\n"+'\n'.join('- '+b for b in v['virais'])+"\n")
    import prompts as _P
    cen=_P.VAR[k]
    L.append("## Imagem única (IMAGEM 1) — primeiro e último quadro de todos os takes\n"
      "**Continuação do pré-gancho (decisão do aluno, 19/10/2026, teste do nora25 ao nora28): a IMAGEM 1 tem a MESMA roupa e o MESMO cenário do pré-gancho; a Nora só passa a falar. Nos virais R01, R04, R07 e R09 é assim.** **A partir de 19/10/2026 a IMAGEM 1 é gerada na Central de imagens do curso (caixinha “já tenho o blueprint” marcada), campo por campo, e não com um prompt nosso.** A avatar é a **Nora v2** (latina, cabelo preto longo com trança de anéis dourados, olhos verde-avelã, lua dourada com 3 estrelinhas na maçã do rosto, brincos de estrela e lua, colar de Vênus). O painel traz todos os campos, com o que está travado pelo blueprint marcado.\n"
      f"- **Roupa deste roteiro:** {v['fig']}.\n- **Objeto na mão direita, em primeiro plano:** {v['objeto']}. A mão esquerda fica livre para os gestos.\n"
      f"- **Cenário (com sinais dos EUA):** {cen['cen'].replace('LIVRE: ','')}.\n- **Luz:** {cen['hor']}; {cen['luz']}; {cen['grade']}.\n"
      "Sem celular e sem carta fora da mão (P9).\n")
    L.append(f"## Pré-gancho — {pre['dur']} s (clipe separado, sem fala, **com o rosto da Nora**)\n"
      f"Modelo nos virais: {pre['viral']}. {pre['conceito']}\n"
      f"**Texto na tela:** \"{pre['texto']}\" (modelo: {pre['texto_viral']}).\n"
      f"**Modo no Flow:** Frames. Primeiro quadro = imagem 1 (gerada a partir do blueprint da Nora, com o rosto dela). Último quadro = imagem 2 (edição da imagem 1 com o efeito terminado). O painel vai mandar comparar as duas antes de gastar os {CRED[pre['dur']]} créditos do vídeo (lição do R004).\n")
    L.append("## Takes (a fala inteira vai de uma vez na Central; o site divide em takes de 10 s)\n")
    for i,(nome,vis,en,pt) in enumerate(v['takes'],1):
        L.append(f"### Take {i}/{n} — {nome} — 10 s ({len(en.split())} palavras)\n**Nome do arquivo:** `{v['tnames'][i-1]}`\n**Visual:** {vis}\n**Fala:** \"{en}\"\n(PT: {pt})\n")
    L.append(f"## Texto de tela (edição)\n- **Início do vídeo:** \"{v['hooktext'][0]}\". Começa em \"{v['hooktext'][1]}\" e termina em \"{v['hooktext'][2]}\".\n- **Pré-gancho:** \"{pre['texto']}\"\n")
    nl=len(v['legenda'].split('\n'))
    L.append("## Legenda do post (Instagram e Facebook)\n"+v['legenda']+"\n\n(Regra do aluno, 19/10/2026: legenda curta, no máximo 2 linhas, ou 3 se tiver hashtag. Esta tem %d linhas, %s. Teste: nora25 e nora27 sem hashtag; nora26 e nora28 com hashtag. Anotar nas métricas qual foi qual.)\n"%(nl,'com hashtag' if '#' in v['legenda'] else 'sem hashtag'))
    L.append("## Comentário fixado\n- **Instagram:** "+v['pin_ig']+"\n- **Facebook:** "+v['pin_fb']+"\n")
    L.append("## Story (parte 2)\nO story do Love Chart é **um só para os quatro vídeos do dia** (nora25 a nora28): imagem sem texto (a Nora segura o pingente de cobre perto da lente), texto \"Tap below and find your Venus pattern in astrology.\" e adesivo \"Find my Venus\". O pacote completo (prompt da imagem, texto e adesivo) vem na Fase 2, no `STORY-NORA25-28-LOVECHART.md`.\n")
    L.append("## Nomes e reaproveitamento (decisão do aluno, 19/10/2026)\n"
      "Toda imagem e todo take tem um nome (lista completa no painel, seção “Nomes e reaproveitamento”, e em `BIBLIOTECA-DE-TAKES.md`). Pré-gancho: `%s-PRE-IMG1`, `%s-PRE-IMG2`, `%s-PRE`. Imagem do vídeo: `%s-IMG`. Takes: %s.\n"%(k,k,k,k,', '.join('`'+x+'`' for x in v['tnames']))
      +"Os créditos deixaram de ser limite (o aluno comprou 1000), então este vídeo é gerado completo, com o CTA dele. O que reaproveitar vem depois, peça por peça, conforme o vídeo performar (regras em `BIBLIOTECA-DE-TAKES.md`).\n")
    L.append(f"## Créditos e montagem\nPré-gancho {pre['dur']} s = {CRED[pre['dur']]} créditos; {n} takes de 10 s = {n*15} créditos. **Total do vídeo: {cred} créditos** (sem contar refações). Montagem: pré-gancho + takes 1 a {n} ≈ {tot} s. Plano geral dos quatro vídeos em `PLANO-CREDITOS-NORA25-28.md`.\n")
    L.append("## Notas editoriais e factuais\n"+'\n'.join('- '+x for x in v['notas'])+"\n- Sem nome do app, da Aura, preço, pagamento, comissão, afiliado, contador, depoimento, número, data específica nem celebridade. O que o quiz entrega, segundo o briefing: signo de Vênus (Sol e Lua), o nome do padrão, o par perfeito pela metade e a janela do amor. A Nora só diz \"finds your Venus, names your pattern, shows your perfect match\" e nunca que a pessoa existe ou que o amor chega.\n- \"Dá para fazer sem a hora de nascimento\" (briefing) está na legenda.\n- Cada fala tem de 20 a 22 palavras; conferi por simulação que a fala inteira colada de uma vez vira exatamente os takes acima (com o limite do site entre 22 e 24 palavras). Quem confirma é a lista de takes da Central, que o painel vai repetir.\n- Sem métricas de publicação.\n")
    open(OUT+v['file'],'w',encoding='utf-8').write('\n'.join(L))
    return tot,cred
t=0
for k,v in data.V.items():
    a,b=render(k,v); t+=b; print(k,a,'s',b,'cred')
print('total',t)
