from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json, busca_turmas
from regra_de_negocio.global_settings import read_global_settings, edit_global_settings
import json


def hola_mundinho(request):
    return HttpResponse("Olá Mundo")


def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)


def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})


def get_global_settings(request):
    global_settings = read_global_settings()
    return JsonResponse(global_settings)


def alterar_global_settings(request):
    alteracoes = json.loads(request.body)
    try:
        edit_global_settings(alteracoes["sprints"], alteracoes["dias"])
        return JsonResponse({"message": "Editou global settings"})

    except Exception as error:
        JsonResponse(error)


def get_turmas(request):
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data)
