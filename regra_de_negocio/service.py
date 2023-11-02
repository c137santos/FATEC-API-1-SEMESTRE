from regra_de_negocio import gerenciador_turmas, gerenciador_ciclos


def criar_turma(dados_nova_turma):
    turmas = gerenciador_turmas.buscar_turmas()
    nova_turma_id = gerar_novo_id_svc(turmas)
    resposta, quantidade_ciclos, duracao_ciclo = gerenciador_turmas.criacao_turma(
        dados_nova_turma, nova_turma_id, turmas
    )
    gerenciador_ciclos.criar_ciclo_turma(
        duracao_ciclo, nova_turma_id, quantidade_ciclos
    )
    return resposta


def gerar_novo_id_svc(entidade):
    """Percorre as chaves do objeto json e procura o maior valor entre elas,
    soma esse valor com 1 e retorna o novo ID"""
    lista_ids = []
    for id in entidade.keys():
        id = int(id)
        lista_ids.append(id)
    novo_id = max(lista_ids) + 1
    novo_id = str(novo_id)

    return novo_id
