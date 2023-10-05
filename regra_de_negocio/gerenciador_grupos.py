import json

# A função obter_todos_grupos() retorna:
#    erro: possível erro ao ler o arquivo.
#    grupos: vetor de dicionários contendo os grupos.
def obter_todos_grupos():
    try:
        with open("dados/grupos.json", 'r', encoding="utf-8") as arquivo:
            dados = arquivo.read()
            print(dados)
            grupos = json.loads(dados)
            print(grupos)
            return None, grupos
    except:
        return "erro ao ler o arquivo de grupos", {}

# A função obter_ultimo_id() retorna:
#    erro: possível erro ao obter o id.
#    grupos: o último id disponível.
def obter_ultimo_id():
    erro, grupos = obter_todos_grupos()
    if not erro:
        return sorted(grupos.keys()).pop()
    return None

# A função obter_novo_id() retorna:
#    o próximo id disponível para um novo grupo.
def obter_novo_id():
    ultimo_id = obter_ultimo_id()
    # return int(ultimo_id) + 1 if ultimo_id else 1
    if ultimo_id:
        return str(int(ultimo_id) + 1)
    else:
        return str(1)

# Parâmetro: um dicionário onde cada grupo é um par chave-valor
# Retorna: 
#   um possível erro
#   salva a lista de grupos em um arquivo JSON (grupos.json)
def salvar_grupos(grupos):
    try:
        dados = json.dumps(grupos, indent=4)
        with open("dados/grupos.json", "w", encoding="utf-8") as arquivo:
            arquivo.write(dados)
            return None
    except:
        return "erro ao serializar ou persistir a lista de grupos no arquivo"

#Removendo grupos com base no seu id.
# 1° ela obtém a lista atual de grupos.
# Se id existir, remove o grupo com o ID especificado usando o método pop.
def remover_grupo(id):
    erro, grupos = obter_todos_grupos()
    if not erro and id in grupos:
        grupos.pop(id)
        salvar_grupos(grupos)

# Parâmetros: um grupo
# A função tem a finalidade de adicionar um novo grupo ao dicionário de grupos.
def inserir_grupo(novo_grupo, id):
    erro, grupos = obter_todos_grupos()
    if not erro:
        grupo = {}
        grupo["grupo"] = novo_grupo
        grupos[id] = grupo
        salvar_grupos(grupos)

#Editando grupos:
#Essa função tem a finalidade de editar as informações de um grupo existente.
def editar_grupos(id, novo_grupo):
    erro, grupos = obter_todos_grupos()
    if not erro and id in grupos:
        grupos[id]["grupo"] = novo_grupo
        salvar_grupos(grupos)
