from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import (
    busca_dados_json,
    busca_turmas,
    buscar_grupos,
    cria_turma,
)

from regra_de_negocio.service import busca_dados_json, busca_turmas
from regra_de_negocio.global_settings import read_global_settings
from regra_de_negocio.gerenciador_turmas import excluir_turma

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

def get_turmas(request):
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data)


def get_grupos(request):
    grupos_data = buscar_grupos()
    return JsonResponse(grupos_data)

def post_turma(request):
    dados_nova_turma = request.body
    resposta = cria_turma(dados_nova_turma)
    return JsonResponse(resposta)

def api_v1_turmas_excluir(request, id):
    resultado = excluir_turma(id)
    return JsonResponse({"mensagem":resultado})
