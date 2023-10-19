import json


def buscando_grupos():
    return {
            "1": {
            "turma": 1,
            "nome": "team bee"
            },
            "2": {
                "turma": 2,
                "nome": "team tatata"
            },
            "3": {
                "turma": 1,
                "nome": "team barbuleta"
            },
            "4": {
                "turma": 0,
                "nome": "strangers"
            }
    }


def _salvar_grupos(grupos):
    with open("dados/grupos.json", "w", encoding="utf-8") as f:
        json.dump(grupos, f, indent=4)


