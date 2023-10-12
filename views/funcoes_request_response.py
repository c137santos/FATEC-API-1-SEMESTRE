from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json, busca_turmas, buscar_grupos


def hola_mundinho(request):
    return HttpResponse("Olá Mundo")


def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)


def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})


def get_turmas(request):
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data)


def get_grupos(request):
    grupos_data = buscar_grupos()
    return JsonResponse(grupos_data)

def post_turma(request):
    pass
