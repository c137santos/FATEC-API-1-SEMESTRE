import json

def buscando_alunos():
    with open("dados/alunos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return grupos_Data
