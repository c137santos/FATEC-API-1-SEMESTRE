import csv
from collections import OrderedDict
import os 
import re

def cria_relatorio_csv(info_turma=dict, info_alunos=dict):
    nome_da_turma = info_turma['nome']
    nome_do_arquivo_normalizado = re.sub(r'[^a-zA-Z0-9]', '', nome_da_turma).lower()
    ordem_colunas_info_turma = OrderedDict()
    for chave, _ in info_turma.items():
        ordem_colunas_info_turma[chave] = None
    info_alunos = list(info_alunos.values())

    ordem_colunas_info_alunos = OrderedDict()
    for chave, _ in info_alunos[0].items():
        ordem_colunas_info_alunos[chave] = None
    path = f"dados/{nome_do_arquivo_normalizado}"
    with open(path+".csv", "w", newline="") as relatorio:
        csv_w = csv.writer(relatorio)
        csv_w.writerow(ordem_colunas_info_turma.keys())
        csv_w.writerow(
            info_turma.get(chave, "") for chave in ordem_colunas_info_turma.keys()
        )

        csv_w.writerow(ordem_colunas_info_alunos.keys())

        for aluno_info in info_alunos:
            csv_w.writerow(
                aluno_info.get(chave, "") for chave in ordem_colunas_info_alunos.keys()
            )
    return path
