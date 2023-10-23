import json

#Função criada para fazer a leitura do arquivo grupos.json localizado na pasta "dados"
#O módulo json é usado para carregar o conteúdo do arquivo JSON no objeto grupos_Data. O json.load() converte o JSON em um objeto Python
#Retorno: conteúdo do arquivo como um objeto Python.
def buscando_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return grupos_Data

