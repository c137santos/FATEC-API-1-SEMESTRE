from collections import OrderedDict


def cria_relatorio_csv(info_turma=dict, info_alunos=dict):
    ordem_colunas_info_turma = OrderedDict()
    for chave, _ in info_turma.items():
        if chave == "nome":
            ordem_colunas_info_turma["Nome da Turma"] = info_turma.get(chave, "")
        elif chave == "professor":
            ordem_colunas_info_turma["Professor Responsável"] = info_turma.get(
                chave, ""
            )
        elif chave == "data_de_inicio":
            ordem_colunas_info_turma["Data de início da Turma"] = info_turma.get(
                chave, ""
            )
        elif chave == "duracao_ciclo":
            ordem_colunas_info_turma["Duração Ciclo em dias"] = info_turma.get(
                chave, ""
            )
        elif chave == "quantidade_ciclos":
            ordem_colunas_info_turma["Quantidade ciclos da turma"] = info_turma.get(
                chave, ""
            )
        else:
            ordem_colunas_info_turma[chave] = None
    dados_csv = []

    dados_csv.append(list(ordem_colunas_info_turma.keys()))
    dados_csv.append(list(ordem_colunas_info_turma.values()))

    info_alunos = list(info_alunos.values())

    ordem_colunas_info_alunos = OrderedDict()
    for chave, _ in info_alunos[0].items():
        if chave == "nome":
            ordem_colunas_info_alunos["Nome do aluno"] = None
        elif chave == "data_nascimento":
            ordem_colunas_info_alunos["Data de nascimento"] = None
        elif chave == "genero":
            ordem_colunas_info_alunos["Gênero"] = None
        else:
            ordem_colunas_info_alunos[chave] = None

    dados_csv.append(list(ordem_colunas_info_alunos.keys()))

    for aluno_info in info_alunos:
        dados_csv.append(list(aluno_info.values()))

    return dados_csv
