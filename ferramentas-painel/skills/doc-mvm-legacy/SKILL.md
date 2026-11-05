---
name: "doc-mvm-legacy"
description: "Use quando o Guilherme mandar material do MVM Legacy/Appyon (aula, print, Discord, link) ou falar do doc Plano MVM Legacy – Appyon."
---

# Doc Plano MVM Legacy – Appyon

O Guilherme está testando o curso MVM Legacy (vender o app Auraly da Appyon como afiliado, com vídeos de avatar de IA no Instagram e no Facebook). Tudo fica num Claude Doc só.

- Doc atual: https://claude.ai/artifact/2KP736NhHJUXjF4s4JkANs
- Projeto: 0aaa260d-18c9-48de-a9f4-eafa2d73e8e0 · node 0d0724eb-ab64 · tab (file) 5b5b5c61-f3e5
- O doc antigo (projeto 66360a6e-25af-49e3-927b-64dc74004f01) não é mais usado.

## Quando ele mandar qualquer material

1. Ler o doc atual antes de mexer (search pelo assunto, ou view da seção).
2. Extrair só o que é útil pra rodar os funis. Nada de resumo de enrolação.
3. Colocar na seção certa. Seções: Status · Próximos passos · Como o negócio funciona · Funil Soulmate · Funil Manifestation · Copy · Produção de vídeo · Estrutura de contas · Postagem, automação e métricas · Números e resultados · Custos · Nota fiscal e CNPJ · Regras, campanhas e riscos · Novidades e Discord · Perguntas · Aulas, gravações e links.
4. Separar sempre o que é do Soulmate e o que é do Manifestation.
5. Se a informação nova desmente ou substitui algo, corrigir ou apagar o antigo. Nunca deixar duas versões. Pergunta respondida sai das abertas e vai pra tabela de respondidas.
6. Não inventar dado. Se algo não foi confirmado, marcar como dúvida ou "a testar".
7. Deixar claro o que é oficial (aula, aviso, material da Appyon) e o que é rascunho nosso (personas, ganchos).
8. Responder curto: o que era, o que importa, onde entrou no doc.

## Como editar rápido

`mcp__Claude_Docs__update` com ref {object:"node",id:"0d0724eb-ab64"}, engine "prose", container {kind:"project",id:"0aaa260d-18c9-48de-a9f4-eafa2d73e8e0"}. Dá pra mandar vários ops numa chamada só:
- inserir no fim de uma lista: `{"op":"insert","target":{"kind":"blocks","ids":["mr0r4t1kgnk.<lista>"]},"side":"end","source":{"as":"markdown","from":{"kind":"inline","content":"- **...**"}}}`
- trocar texto: `{"op":"replace","target":{"kind":"find","text":"..."},"with":{"as":"text","from":{"kind":"inline","content":"..."}}}`

Ids das listas (prefixo mr0r4t1kgnk.): 242477 Facebook · 227050 Insta/GeeLark · 281811 Validar/copy · 309140 Postagem e agendamento · 150854 Produção (Nora/Flow) · 178330 HeyGen · 79477 Manifestation (números) · 18244 Love Chart · 334685 Vitórias · 323884 Encurtador · 356180 Campanha · 289866 Índia. Parágrafo "Discord lido até": .4568. Se um id falhar, ler a seção e pegar o id novo.

Exportar: `mcp__Claude_Docs__export` (file 5b5b5c61-f3e5, formato docx ou markdown).

## Estilo das respostas

Português do Brasil coloquial. Frases curtas. Sem conectivo formal, sem inglês fora de nome próprio e das copies. Sem "não é X, é Y:". Números concretos. Um passo de cada vez: não empurrar tarefa nova que ele não pediu.

## Copy

Ajudar de verdade com copy emocional, gancho forte e urgência real. Limites: não prometer resultado garantido (dinheiro caindo, "você vai conhecer ele este mês"), não apresentar depoimento inventado como real, não mirar vício, dívida ou "maldição".