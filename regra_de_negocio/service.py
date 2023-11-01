from regra_de_negocio import gerenciador_turmas

def criar_turma(dados_nova_turma):
    turmas = gerenciador_turmas.buscar_turmas()
    nova_turma_id = gerando_novo_id_svc(turmas)
    resposta = gerenciador_turmas.criacao_turma(dados_nova_turma, nova_turma_id, turmas)
    return resposta

def gerando_novo_id_svc(entidade):
    """Percorre as chaves do objeto json e procura o maior valor entre elas, 
    soma esse valor com 1 e retorna o novo ID"""
    lista_ids = []
    for id in entidade.keys():
        id = int(id)
        lista_ids.append(id)
    novo_id = max(lista_ids) + 1
    novo_id = str(novo_id)

    return novo_id

