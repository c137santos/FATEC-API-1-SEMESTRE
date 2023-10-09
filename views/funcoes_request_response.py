from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json
from regra_de_negocio.global_settings import read_global_settings


def hola_mundinho(request):
    return HttpResponse("Olá Mundo")


def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)


def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})


def get_global_settings():
    global_settings = global_settings.read_global_settings()
    return JsonResponse(global_settings)

