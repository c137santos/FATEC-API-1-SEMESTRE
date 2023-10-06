import json

#Retorno:
#   vetor de dicionários contendo os grupos.
def obter_todos_grupos():
    with open("dados/grupos.json", 'r', encoding="utf-8") as arquivo:
        dados = arquivo.read()
        grupos = json.loads(dados)
        return grupos
    
#Retorno:
#   o último id disponível.
def obter_ultimo_id():
    return sorted(obter_todos_grupos().keys()).pop()

#Retorno:
#    o próximo id disponível para um novo grupo.
def obter_novo_id():
    ultimo_id = obter_ultimo_id()
    if ultimo_id:
        return str(int(ultimo_id) + 1)
    else:
        return str(1)

# Parâmetro: 
#   um dicionário onde cada grupo é um par chave-valor
def salvar_grupos(grupos):
    dados = json.dumps(grupos, indent=4)
    with open("dados/grupos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)

#Removendo grupos com base no seu id.
# 1° ela obtém a lista atual de grupos.
# Se id existir, remove o grupo com o ID especificado usando o método pop.
# Parâmetros: id do grupo
def remover_grupo(id):
    grupos = obter_todos_grupos()
    if id in grupos.keys():
        grupos.pop(id)
        salvar_grupos(grupos)

# Parâmetros: o id da turma associada ao novo grupo
# A função tem a finalidade de adicionar um novo grupo ao dicionário de grupos.
def inserir_grupo(id_turma):
    grupos = obter_todos_grupos()
    grupo = {}
    grupo["turma"] = id_turma
    grupos[obter_novo_id()] = grupo
    salvar_grupos(grupos)

#Parâmetros: o id do grupo existente, o id da turma que o grupo está associado
#Essa função tem a finalidade de editar as informações de um grupo existente.
def editar_grupos(id_grupo, id_turma):
    grupos = obter_todos_grupos()
    if id_grupo in grupos.keys():
        grupo = grupos[id_grupo]
        grupo["turma"] = id_turma
        salvar_grupos(grupos)
