from wgsi import JsonResponse
from regra_de_negocio.service import (
    busca_turmas,
    cria_turma,
)

from regra_de_negocio.gerenciador_turmas import excluir_turma_svc, editar_turma_svc

import regra_de_negocio.gerenciador_ciclos as gerenciador_ciclos
import regra_de_negocio.gerenciador_notas as gerenciador_notas

import json


def edit_aluno(request, id):
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})

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
    for i in range(resposta["nova_turma"]["quantidade_ciclos"]):
        gerenciador_ciclos.adicionar_ciclo(resposta["id_nova_turma"])
    return JsonResponse(resposta)

def excluir_turma(request, id):
    resultado = excluir_turma_svc(id)
    return JsonResponse({"mensagem": resultado})

def criar_ciclo(request):
    novo_ciclo = json.loads(request.body)
    resultado = gerenciador_ciclos.adicionar_ciclo(novo_ciclo)
    return JsonResponse({"mensagem":resultado})

def listar_ciclos(request):
    ciclos = gerenciador_ciclos.listar_ciclos()
    return JsonResponse(ciclos)

def listar_ciclos_por_id_turma(request, id_turma):
    ciclos = gerenciador_ciclos.listar_ciclos_por_id_turma(id_turma)
    return JsonResponse(ciclos)

def criar_nota(request):
    nova_nota = json.loads(request.body)
    if gerenciador_notas.verificar_existencia_nota_por_ciclo(nova_nota):
        resultado = gerenciador_notas.adicionar_nota(nova_nota)
        return JsonResponse({"mensagem": resultado})
    else:
        return JsonResponse({"mensagem": False})

def editar_nota(request, id_nota):
    nota_atualizada = json.loads(request.body)
    resultado = gerenciador_notas.editar_nota(id_nota, nota_atualizada)
    return JsonResponse({"mensagem": resultado})

def excluir_nota(request, id_nota):
    resultado = gerenciador_notas.remover_nota(id_nota)
    return JsonResponse({"mensagem": resultado})

def listar_notas(request):
    notas = gerenciador_notas.listar_notas()
    for id_nota in notas:
        notas[id_nota]["edicao_habilitada"] = gerenciador_notas.verificar_edicao_habilitada(notas,id_nota)
    return JsonResponse(notas)

def listar_notas_por_id_turma_id_aluno(request, id_turma, id_aluno):
    notas = gerenciador_notas.listar_notas_por_id_turma_id_aluno(id_turma, id_aluno)
    for id_nota in notas:
        notas[id_nota]["edicao_habilitada"] = gerenciador_notas.verificar_edicao_habilitada(notas,id_nota)
    return JsonResponse(notas)

def listar_notas_por_id_turma(request, id_turma):
    notas = gerenciador_notas.listar_notas_por_id_turma(id_turma)
    for id_nota in notas:
        notas[id_nota]["edicao_habilitada"] = gerenciador_notas.verificar_edicao_habilitada(notas,id_nota)
    return JsonResponse(notas)

def listar_notas_por_id_aluno(request, id_aluno):
    notas = gerenciador_notas.listar_notas_por_id_aluno(id_aluno)
    for id_nota in notas:
        notas[id_nota]["edicao_habilitada"] = gerenciador_notas.verificar_edicao_habilitada(notas,id_nota)
    return JsonResponse(notas)
