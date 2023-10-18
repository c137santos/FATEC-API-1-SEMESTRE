import json

def buscando_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return grupos_Data