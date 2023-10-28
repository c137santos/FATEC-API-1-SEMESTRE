from wgsi import JsonResponse
from regra_de_negocio.service import (
    busca_turmas,
    cria_turma,
)

from regra_de_negocio.global_settings import read_global_settings, edit_global_settings
from regra_de_negocio.gerenciador_turmas import excluir_turma_svc, editar_turma_svc

import json


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


def obtem_turma_especifica(request, id):
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data[id])


def editar_turma(request, id):
    turma = json.loads(request.body)
    resultado = editar_turma_svc(
        id,
        turma["nome"],
        turma["professor"],
        turma["data_de_inicio"],
        turma["duracao_ciclo"],
    )
    return JsonResponse({"mensagem": resultado})


def criar_turma(request):
    dados_nova_turma = json.loads(request.body)
    resposta = cria_turma(dados_nova_turma)
    return JsonResponse(resposta)


def excluir_turma(request, id):
    resultado = excluir_turma_svc(id)
    return JsonResponse({"mensagem": resultado})
