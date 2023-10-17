import json

def busca_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return grupos_Data

def _salvar_grupos(grupos):
    with open("dados/grupos.json", "w", encoding="utf-8") as f:
        json.dump(grupos, f, indent=4)

def excluir_grupo(id):
    grupos = busca_grupos()
    grupo_nome = None #Inicializa o nome do grupo como None em caso de nao ser encontrado
    id = str(id) #transforma o ID em String para comparar com as chaves
    if id in grupos.keys(): #keys retorna uma lista de strings com os ids
        grupo_nome = grupos[id]['nome']
        grupos.pop(id)
        _salvar_grupos(grupos)
        print(f"Grupo {grupo_nome} deletado.")
        return True
    else:
        print(f"Grupo {grupo_nome} não encontrado.")
        return False