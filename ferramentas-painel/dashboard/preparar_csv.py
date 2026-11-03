# Prepara a planilha para o dashboard: cópia SEM o BOM (para subir como asset) e rows.json (para o conferir-dados.js).
# Uso, na pasta do repositório: python3 -I ferramentas-painel/dashboard/preparar_csv.py <pasta de saída>
# O METRICAS-NORA.csv do repositório fica como está: UTF-8 COM o BOM e linhas em CRLF (o Excel do aluno abre certo).
import csv, json, os, sys
saida = sys.argv[1] if len(sys.argv) > 1 else '.'
os.makedirs(saida, exist_ok=True)
texto = open('METRICAS-NORA.csv', encoding='utf-8-sig', newline='').read()
open(os.path.join(saida, 'metricas-nora.csv'), 'w', encoding='utf-8', newline='').write(texto)
linhas = list(csv.DictReader(open('METRICAS-NORA.csv', encoding='utf-8-sig', newline='')))
json.dump(linhas, open(os.path.join(saida, 'rows.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('linhas:', len(linhas), '| arquivos em', saida)
