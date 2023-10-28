from regra_de_negocio import gerenciador_turmas


def buscando_turmas():  # retorna todas turmas
    turmas_data = gerenciador_turmas.buscando_turmas()
    return turmas_data


def cria_turma(dados_nova_turma):
    resposta = gerenciador_turmas.criacao_turma(dados_nova_turma)
    return resposta

