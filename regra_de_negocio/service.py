import regra_de_negocio.gerenciador_turmas as gt


def busca_turmas():  # retorna todas turmas
    turmas_data = gt.busca_turmas()
    return turmas_data


def cria_turma(dados_nova_turma):
    resposta = gt.criacao_turma(dados_nova_turma)
    return resposta
