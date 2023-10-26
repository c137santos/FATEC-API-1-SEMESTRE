import json

def read_global_settings():
    with open("dados/global_setting.json", "r", encoding="utf-8") as arquivo:
        dados = arquivo.read()
        global_settings = json.loads(dados)
        return global_settings

def edit_global_settings(quantidade_sprint, dias_sprint):
    settings_atual = read_global_settings()
    if quantidade_sprint != "":
        settings_atual["quantidade_sprint"] = quantidade_sprint
    if dias_sprint != "":
        settings_atual["dias_sprint"] = dias_sprint
    dados_global_settings = open("dados/global_setting.json", "w")
    json.dump(settings_atual, dados_global_settings)
    dados_global_settings.close()

def obter_quantidade_sprint():
    gs = read_global_settings()
    return gs["quantidade_sprint"]