# Como recriar o dashboard "Métricas da Nora" numa conta nova do Claude (igual ao de hoje)

**Recriado em 26/10/2026 (~22h) na conta contatocaram:** https://claude.ai/artifact/CTdhXsH5PoQFRCnzpbM4wy (asset do CSV `/_blob/243a4fbb54b8fa9ba591c04cf37a560b`, versão de 30/10 01h27; banco conferido em 30/10: `store/` igual ao do Artifact, só a `source.url` e o `updated` mudam).

O dashboard é um Artifact do **tipo "Dashboard"** (não é uma página HTML comum). A página e os dados ficam no banco do próprio Artifact, em 4 documentos. Cópia exata de 27/10/2026 (conta antiga, https://claude.ai/artifact/LXyXLjNohRDcTcnYwtAZKi):

| Documento no banco | Arquivo aqui | O que é |
|---|---|---|
| `dash/meta` | `store/dash-meta.json` | título: "Métricas da Nora" |
| `dash/params` | `store/dash-params.json` | filtros iniciais: período "v2", rede "Instagram" |
| `datasets/metricas` | `store/datasets-metricas.json` | a planilha: arquivo CSV anexado (`kind: "file"`, `format: "csv"`, `name: "metricas-nora.csv"`) |
| `files/index.html` | `index.html` | a página (gráficos, tabelas, filtros), campo `text` |

## Passo a passo (sessão nova)
1. `Artifact` com `action: "quickstart"` e `intent: "other"` para achar o tipo Dashboard da conta; criar o Artifact a partir do `type_url` dele, com o título "Métricas da Nora".
2. Fazer uma cópia de `METRICAS-NORA.csv` **sem o BOM** (os 3 primeiros bytes) com o nome `metricas-nora.csv` e subir como asset do Artifact novo (`asset: true`). Guardar o `url` que voltar (`/_blob/...`).
3. Gravar os 4 documentos num `batch` do `ArtifactData`: `dash/meta` e `dash/params` iguais aos arquivos daqui; `datasets/metricas` igual ao arquivo daqui, trocando `source.url` pelo `url` novo e `updated` por `{at: <hora ISO>, by: "Claude"}`; `files/index.html` com `{text: <conteúdo de index.html>}`.
4. Fazer a checagem que o tipo pede (ler `data/users/me`, doc `check`).
5. Trocar o link do dashboard no `CLAUDE.md` (seção 3) e no `METRICAS-NORA-LEIA.md`.

**30/10/2026:** a página (`files/index.html`, versão 2; cópia em `index.html` aqui) passou a mostrar o número em cima de toda barra em qualquer largura (10 px quando a barra é estreita; na vertical quando é muito estreita) e a se redesenhar quando a janela muda de tamanho (antes só mostrava com a tela larga no momento em que a página abria). Recriar a partir desta cópia.

Para atualizar depois: editar o CSV, subir uma cópia nova sem o BOM como asset e dar `update` em `datasets/metricas` (`source.url`, `source.name`, `updated`) com `if_version`.
