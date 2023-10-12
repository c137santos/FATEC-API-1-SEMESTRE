from wgsi import HttpResponse, JsonResponse
from regra_de_negocio.service import busca_dados_json, busca_turmas
from regra_de_negocio.gerenciador_turmas import editar_turma
import json

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

def api_v1_turmas_editar(requisicao, id):
    turma = json.loads(requisicao.body)
    resultado = editar_turma(id, turma["nome"], turma["professor"], turma["data_de_inicio"])
    return JsonResponse({"mensagem": resultado})