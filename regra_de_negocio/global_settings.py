import json


def read_global_settings():
    with open("dados/global_settings.json", "r", encoding="utf-8") as arquivo:
        dados = arquivo.read()
    global_settings = json.loads(dados)
    return global_settings


def edit_global_settings(quantidade_sprint, dias_sprint, prazo_nota):
    settings_atual = read_global_settings()
    if quantidade_sprint != "":
        settings_atual["quant_dias_ciclo"] = dias_sprint
    if dias_sprint != "":
        settings_atual["quant_ciclos"] = quantidade_sprint
    if prazo_nota != "":
        settings_atual["prazo_insercao_nota"] = prazo_nota
    dados_global_settings = open("dados/global_settings.json", "w")
    json.dump(settings_atual, dados_global_settings)
    dados_global_settings.close()
