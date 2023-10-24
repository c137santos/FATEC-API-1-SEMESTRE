import json


# Função criada para fazer a leitura do arquivo grupos.json localizado na pasta "dados"
# O módulo json é usado para carregar o conteúdo do arquivo JSON no objeto grupos_Data. O json.load() converte o JSON em um objeto Python
# Retorno: conteúdo do arquivo como um objeto Python.
def buscando_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return grupos_Data

def _salvar_grupos(grupos):
    with open("dados/grupos.json", "w", encoding="utf-8") as f:
        json.dump(grupos, f, indent=4)

def excluindo_grupo(id):
    grupos = buscando_grupos()
    grupo_nome = (
        None  # Inicializa o nome do grupo como None em caso de nao ser encontrado
    )
    id = str(id)  # transforma o ID em String para comparar com as chaves
    if id in grupos.keys():  # keys retorna uma lista de strings com os ids
        grupo_nome = grupos[id]["nome"]
        grupos.pop(id)
        _salvar_grupos(grupos)
        print(f"Grupo {grupo_nome} deletado.")
        return True
    else:
        print(f"Grupo {grupo_nome} não encontrado.")
        return False