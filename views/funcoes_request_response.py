from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json, busca_turmas, busca_grupos, busca_grupo_alunos, busca_alunos


def hola_mundinho(request):
    return HttpResponse("Olá Mundo")


def get_arquivos_json(request):
    dados = busca_dados_json()
    return JsonResponse(dados)

def get_turmas(request):
    dados = busca_turmas()
    return JsonResponse(dados)

def get_grupos(request):
    dados = busca_grupos()
    return JsonResponse(dados)

def get_grupo_alunos(request):
    dados = busca_grupo_alunos()
    return JsonResponse(dados)

def get_alunos(request):
    dados = busca_alunos()
    return JsonResponse(dados)

def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})
