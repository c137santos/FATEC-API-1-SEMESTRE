import json


def read_global_settings():
    with open("dados/global_setting.json", "r", encoding="utf-8") as arquivo:
        dados = arquivo.read()
    global_settings = json.loads(dados)
    return global_settings
