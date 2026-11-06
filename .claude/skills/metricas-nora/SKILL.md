---
name: metricas-nora
description: Use quando o Guilherme mandar métricas da Nora (prints ou texto do Insights do Instagram, da Biblioteca do Facebook, do story ou do Tracker da Appyon) para anotar, atualizar o dashboard e dizer o que os números mostram.
---

# Métricas da Nora

## Onde vai cada número
- **`METRICAS-NORA.csv`** (UTF-8 com BOM, linhas CRLF; ler e gravar com `csv` do Python, `encoding='utf-8-sig'`, `lineterminator='\r\n'`): uma linha por vídeo e rede (`id` = `noraNN-ig` / `noraNN-fb`, `faceNN-…`). Colunas: `views, viewers, likes, comentarios, salvos, compart, reposts, follows, skip, ret3s, tempo, pais1..pais5, print, legenda, obs, nota_face`. `ret3s` = views de 3 s ÷ views × 100; `skip` = 100 − `ret3s`. `print` = a hora da leitura e o tempo de vida ("06/11 13h10 (~12 h de vida)"). No Face, `nota_face` acumula "Leitura dd/mm hh (~X h): …". No Insta, anotar quantos comentários são de outras pessoas (sem o fixado nem as respostas do aluno). Vídeo novo sem linha: criar copiando o formato da linha do vídeo anterior.
- **`METRICAS-NORA-LEIA.md`:** uma entrada datada por leitura (antes do "## Modelo para o aluno mandar as métricas"), com os números e a decisão.
- **Tracker da Appyon:** só no `METRICAS-NORA-LEIA.md` (cliques, quiz, VSL, checkout, venda; por dia e por rede).
- **Dashboard:** `python3 -I ferramentas-painel/dashboard/preparar_csv.py <pasta>` → `node ferramentas-painel/dashboard/conferir-dados.js ferramentas-painel/dashboard/index.html <pasta>/rows.json` → subir `<pasta>/metricas-nora.csv` como asset do dashboard (Artifact publish com `url` do dashboard da seção 1 do `CLAUDE.md`, `asset: true`) → `ArtifactData` `get` em `datasets/metricas` para pegar a versão → `update` com `source.url` (o `/_blob/...` novo), `source.name` e `updated` `{at, by: "Claude"}`, com `if_version`. Trocar o asset e a versão na seção 1 do `CLAUDE.md`. **Atualizar o dashboard a cada leitura, na hora, junto com a planilha** (o aluno olha o dashboard; em 06/11 eu deixei para o fim do lote e ele cobrou).

## Como ler (regras em vigor)
- Não julgar com 3 h; a régua é com ~24 h. Comparar com o vídeo do mesmo teste no mesmo tempo de vida e, se der, no mesmo horário.
- **Teste em andamento (ver `CLAUDE.md`, seção 1):** o corpo, com o gancho fixo. Julgar corpo ou CTA só com 800 a 1.000 views somadas do mesmo corpo no Insta, pelas visitas ao perfil, follows, comentários de outras pessoas, viewers do story e cliques no Tracker.
- Comentários de outras pessoas ÷ views: 2,5%+ bom, 1% a 2,5% meio, abaixo de 1% fraco (só com 300+ views).
- Insta: olhar a curva aos 8 s, a % de EUA e de Índia (Índia não compra) e o 45+ (copy de medo puxa público velho). Face: tem restrição de país, nunca atribuir view à Índia; trava entre ~240 e ~320 = gancho.
- **A medida final é o clique no Tracker** (~178 cliques por venda na comunidade em outubro).
- Vídeo com 10 curtidas ou mais: pedir o gráfico "When people liked your reel".

## Resposta ao aluno
Curta, começando pela conclusão (o que o número diz sobre o teste), depois a decisão e o que ele faz agora. Commit e push depois de anotar.
