from wgsi import JsonResponse
from regra_de_negocio.service import (
    busca_turmas,
    cria_turma,
)

from regra_de_negocio.gerenciador_turmas import excluir_turma_svc, editar_turma_svc
import regra_de_negocio.gerenciador_turmas as gerenciador_turmas
import regra_de_negocio.gerenciador_ciclos as gerenciador_ciclos
import regra_de_negocio.gerenciador_notas as gerenciador_notas
import regra_de_negocio.gerenciador_turmas_alunos as gerenciador_turmas_alunos
import regra_de_negocio.gerenciador_alunos as gerenciador_alunos
import regra_de_negocio.global_settings as global_settings

import json


def criar_aluno(request):
    novo_aluno = json.loads(request.body)
    gerenciador_alunos.criar_aluno(novo_aluno)
    return JsonResponse({"message": "Aluno criado"})


def deletar_aluno(request, id):
    gerenciador_alunos.apagar_aluno(id)
    return JsonResponse({"message": f"Deletado o aluno com ID {id}."})


def listar_alunos(request):
    alunos_data = gerenciador_alunos.listar_alunos()
    return JsonResponse(alunos_data)


def editar_aluno(request, id):
    aluno = json.loads(request.body)
    gerenciador_alunos.editar_aluno_svc(id, aluno)
    return JsonResponse({"message": f"Editando o aluno com ID {id}."})


def listar_turmas(request):
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data)


def obter_turma(request, id):
    turmas_data = busca_turmas()
    return JsonResponse(turmas_data[id])


def editar_turma(request, id):
    turma = json.loads(request.body)
    resultado = editar_turma_svc(
        id,
        turma["nome"],
        turma["professor"],
        turma["data_de_inicio"],
        turma["alunos_adicionados"],
    )
    return JsonResponse({"mensagem": resultado})


def criar_turma(request):
    nova_turma = json.loads(request.body)
    resposta = cria_turma(nova_turma)
    return JsonResponse(resposta)


def excluir_turma(request, id):
    """
    A exclusão de turma está em modo cascata.
    """
    print(f"\n> Excluindo turmas...\n")
    try:
        excluir_turma_svc(id)
    except Exception as e:
        return JsonResponse(
            {"mensagem": f"Falha na exclusão de turma_aluno: {str(e)}"},
            status="500 Internal Server Error",
        )
    gerenciador_turmas_alunos.remover_turma_aluno(id)
    gerenciador_ciclos.excluir_ciclo_da_turma(id)
    gerenciador_notas.excluir_notas_relacionadas_turma(id)
    return JsonResponse({"mensagem": "Sucesso"}, status="200 ok")


def criar_ciclo(request):
    novo_ciclo = json.loads(request.body)
    resultado = gerenciador_ciclos.adicionar_ciclo(novo_ciclo)
    return JsonResponse({"mensagem": resultado})


def listar_ciclos(request):
    ciclos = gerenciador_ciclos.listar_ciclos()
    return JsonResponse(ciclos)


def listar_ciclos_por_id_turma(request, id_turma):
    ciclos = gerenciador_ciclos.listar_ciclos_por_id_turma(id_turma)
    return JsonResponse(ciclos)


def editar_ciclo(request, id_ciclo):
    ciclo = json.loads(request.body)
    resultado = gerenciador_ciclos.editar_ciclo(id_ciclo, ciclo)
    return JsonResponse({"mensagem": resultado})


def criar_nota(request):
    nova_nota = json.loads(request.body)
    if not gerenciador_notas.verificar_existencia_nota_por_ciclo(nova_nota):
        resultado = gerenciador_notas.adicionar_nota(nova_nota)
        return JsonResponse({"mensagem": resultado})
    else:
        return JsonResponse({"mensagem": False})


def editar_nota(request):
    notas_atualizada = json.loads(request.body)
    print(notas_atualizada)
    resultado = gerenciador_notas.editar_nota(notas_atualizada)
    return JsonResponse({"mensagem": resultado})


def excluir_nota(request, id_nota):
    resultado = gerenciador_notas.remover_nota(id_nota)
    return JsonResponse({"mensagem": resultado})


def listar_notas(request):
    notas = gerenciador_notas.listar_notas()
    for id_nota in notas:
        notas[id_nota][
            "edicao_habilitada"
        ] = gerenciador_notas.verificar_edicao_habilitada(notas, id_nota)
    return JsonResponse(notas)


def listar_notas_por_id_turma_id_aluno(request, id_turma, id_aluno):
    notas = gerenciador_notas.listar_notas_por_turma_aluno(id_turma, id_aluno)
    print(notas)
    for id_nota in notas:
        notas[id_nota][
            "edicao_habilitada"
        ] = gerenciador_notas.verificar_edicao_habilitada(notas, id_nota)
    print(notas)
    return JsonResponse(notas)


def filtrar_notas_por_id_turma(request, id_turma):
    notas = gerenciador_notas.listar_notas()
    notas_por_turma = gerenciador_notas.filtrar_notas_por_id_turma_svc(notas, id_turma)
    for id_nota in notas_por_turma:
        notas_por_turma[id_nota][
            "edicao_habilitada"
        ] = gerenciador_notas.verificar_edicao_habilitada(notas_por_turma, id_nota)
    return JsonResponse(notas_por_turma)


def listar_notas_por_id_aluno(request, id_aluno):
    notas = gerenciador_notas.listar_notas()
    notas_por_aluno = gerenciador_notas.listar_notas_por_id_aluno(notas, id_aluno)
    for id_nota in notas_por_aluno:
        notas_por_aluno[id_nota][
            "edicao_habilitada"
        ] = gerenciador_notas.verificar_edicao_habilitada(notas_por_aluno, id_nota)
    return JsonResponse(notas_por_aluno)


def obter_fee_turma_aluno(request, id_turma, id_aluno):
    fee = gerenciador_notas.obter_fee_turma_aluno(id_turma, id_aluno)
    return JsonResponse(fee)


def criar_turmas_alunos(request):
    turma_aluno = json.loads(request.body)
    resultado = gerenciador_turmas_alunos.adicionar_turma_aluno(turma_aluno)
    return JsonResponse({"mensagem": resultado})


def remover_turmas_alunos(request, id_turmas_alunos):
    resultado = gerenciador_turmas_alunos.remover_turma_aluno(id_turmas_alunos)
    return JsonResponse({"mensagem": resultado})


def listar_turmas_alunos(request):
    turmas_alunos = gerenciador_turmas_alunos.listar_turmas_alunos()
    return JsonResponse(turmas_alunos)


def listar_alunos_turma(request, id_turma):
    alunos = gerenciador_turmas_alunos.listar_alunos_turma(id_turma)
    return JsonResponse(alunos)

def listar_turmas_aluno(request, id_aluno):
    turmas = gerenciador_turmas_alunos.listar_turmas_aluno(id_aluno)
    return JsonResponse(turmas)


def listar_detalhes_ciclos_por_id_turma(request, id_turma):
    turma = gerenciador_turmas.obter_turma(id_turma)
    resposta = gerenciador_ciclos.detalhesCicloTurma(turma, id_turma)
    return JsonResponse(resposta)

def listar_global_settings(request):
    global_settings_resp = global_settings.read_global_settings()
    return JsonResponse(global_settings_resp)

def editar_global_settings(request):
    info_editar_settings = json.loads(request.body)
    global_settings.edit_global_settings(
        info_editar_settings["sprints"],
        info_editar_settings["dias"],
        info_editar_settings["prazo_nota"]
    )
    return JsonResponse({"mensagem": "concluido"})
