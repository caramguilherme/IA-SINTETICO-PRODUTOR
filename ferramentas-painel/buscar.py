#!/usr/bin/env python3
"""Pente fino antes de responder ao aluno (regra de 07/11/2026, CLAUDE.md seção 0).

Procura um assunto em todos os documentos do projeto, sem ligar para acento nem
maiúscula, e mostra cada linha encontrada, na ordem dos arquivos que mais importam.

Uso:
    python3 -I ferramentas-painel/buscar.py "restrição de país" "países" "Tier 1" "Canadá"

Cada argumento é um termo; a linha aparece se tiver QUALQUER um deles.
Opções: --tudo (sem limite de linhas por arquivo), --largura N (tamanho do trecho, padrão 260).
"""
import os
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ordem de leitura: fatos e estado primeiro, depois decisões, contatos, números, curso.
PRIORIDADE = [
    "FATOS-DO-ALUNO.md",
    "CLAUDE.md",
    "COMUNIDADE-E-ESTRATEGIA.md",
    "CONTATOS-ALUNOS.md",
    "METRICAS-NORA-LEIA.md",
    "METRICAS-NORA.csv",
    "CLONE-DO-GUSTAVO-RESPOSTAS.md",
    "PLANO-MVM-LEGACY-APPYON.md",
    "REGRAS-DO-AGENTE.md",
    "LICOES-FLOW-E-PROMPTS.md",
    "BIBLIOTECA-DE-TAKES.md",
    "VALIDACAO-CONTA-E-AVATAR.md",
    "BRIEFING-MANIFESTACAO.md",
    "HISTORICO-CLAUDE-MD.md",
]
PASTAS = [".", "HISTORICO-DISCORD", "MATERIAIS-CALL-03-11", "MATERIAIS-CALL-06-11", "ferramentas-painel", "referencias-mineracao", "arquivo"]
EXTENSOES = (".md", ".csv")


def normal(texto):
    t = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in t if not unicodedata.combining(c))


def arquivos():
    vistos = []
    for nome in PRIORIDADE:
        caminho = os.path.join(RAIZ, nome)
        if os.path.isfile(caminho):
            vistos.append(caminho)
    for pasta in PASTAS:
        base = os.path.join(RAIZ, pasta)
        if not os.path.isdir(base):
            continue
        for raiz, _dirs, nomes in os.walk(base):
            if pasta == "." and raiz != base:
                continue  # na raiz, só os arquivos de primeiro nível
            for nome in sorted(nomes):
                caminho = os.path.join(raiz, nome)
                if nome.endswith(EXTENSOES) and caminho not in vistos:
                    vistos.append(caminho)
    return vistos


def main():
    args = sys.argv[1:]
    tudo = "--tudo" in args
    largura = 260
    if "--largura" in args:
        k = args.index("--largura")
        largura = int(args[k + 1])
        del args[k:k + 2]
    termos = [a for a in args if a != "--tudo"]
    if not termos:
        print(__doc__)
        sys.exit(1)
    alvos = [normal(t) for t in termos]
    total = 0
    for caminho in arquivos():
        try:
            linhas = open(caminho, encoding="utf-8-sig").read().split("\n")
        except (UnicodeDecodeError, OSError):
            continue
        achados = []
        for n, linha in enumerate(linhas, 1):
            ln = normal(linha)
            pos = [ln.find(a) for a in alvos if a in ln]
            if pos:
                p = max(0, min(pos) - largura // 3)
                achados.append((n, linha[p:p + largura].strip()))
        if achados:
            rel = os.path.relpath(caminho, RAIZ)
            print(f"\n=== {rel} ({len(achados)} linha(s))")
            mostrar = achados if tudo else achados[:12]
            for n, trecho in mostrar:
                print(f"  {n}: {trecho}")
            if len(achados) > len(mostrar):
                print(f"  ... mais {len(achados) - len(mostrar)} (use --tudo)")
            total += len(achados)
    print(f"\nTotal: {total} linha(s) para {termos}")
    if total == 0:
        print("Nada achado: tentar outras palavras (inglês, nome do menu, um valor provável) antes de dizer que não há registro.")


if __name__ == "__main__":
    main()
