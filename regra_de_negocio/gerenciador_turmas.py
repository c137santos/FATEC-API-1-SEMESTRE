import json


# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def busca_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data

#Editando turmas:
#Essa função tem a finalidade de editar as informações de uma turma existente.
# Parâmetros: 
#   id da turma existente, 
#   nome, professor e data de início (campos a serem modificados)
# Retorno:
#   True se bem sucedido / False caso não exista o id solicitado
def editar_turma(id, nome, professor, data_de_inicio):
    turmas = _listar_todas_turmas()
    if id in turmas.keys():
        turma = turmas[id]
        turma["nome"] = nome
        turma["professor"] = professor
        turma["data_de_inicio"] = data_de_inicio
        _salvar_turmas(turmas)
        return True
    else:
        return False
    
# Retorna:
#    um dicionário onde cada turma é um par chave-valor
def _listar_todas_turmas():
    return {
        "1": {
            "nome": "turma1",
            "professor": "Nadalete",
            "data_de_inicio": "21/02/2023"
        }
    }

# Parâmetro: um dicionário onde cada turma é um par chave-valor
# Retorna:
#   True se a operação for bem sucedida
def _salvar_turmas(turmas):
    dados = json.dumps(turmas, indent=4)
    with open("dados/turmas.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
    return True
