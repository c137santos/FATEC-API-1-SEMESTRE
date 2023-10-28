from regra_de_negocio import gerenciador_turmas


def buscando_turmas():  # retorna todas turmas
    turmas_data = gerenciador_turmas.buscando_turmas()
    return turmas_data


def cria_turma(dados_nova_turma):
    resposta = gerenciador_turmas.criacao_turma(dados_nova_turma)
    return resposta

def gerando_novo_id(entidade):
    """Percorre as chaves do objeto json e procura o maior valor entre elas, 
    soma esse valor com 1 e retorna o novo ID"""
    lista_ids = []
    for id in entidade.keys():
        id = int(id)
        lista_ids.append(id)
    novo_id = max(lista_ids) + 1
    novo_id = str(novo_id)

    return novo_id

