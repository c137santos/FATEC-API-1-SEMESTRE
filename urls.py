import views.funcoes_request_response as view
import re
import sys
from wgsi import JsonResponse

sys.path.append(".")


def URL(pattern):
    return re.sub(r":(\w+)", r"(?P<\1>[^/]+)", pattern) + "$"


# Essa função tem objetivo de compreender os IDs que são passados na URL por meio da aplicação de regex.

URLS = {
    URL("/api/v1/alunos/atualizar/:id"): view.editar_aluno,
    
    URL("/api/v1/turmas/listar"): view.listar_turmas,
    URL("/api/v1/turmas/listar/:id"): view.obter_turma,
    URL("/api/v1/turmas/editar/:id"): view.editar_turma,
    URL("/api/v1/turmas/criar"): view.criar_turma,
    URL("/api/v1/turmas/excluir/:id"): view.excluir_turma,
    
    URL("/api/v1/ciclos/listar"): view.listar_ciclos,
    URL("/api/v1/ciclos/listar/:id_turma"): view.listar_ciclos_por_id_turma,
    #URL("/api/v1/ciclos/criar"): view.criar_ciclo,
    # editar ciclo e remover ciclo serão implementados ao final

    URL("/api/v1/notas/listar"): view.listar_notas,
    URL("/api/v1/notas/listar/:id_turma/:id_aluno"): view.listar_notas_por_id_turma_id_aluno,
    URL("/api/v1/notas/turma/listar/:id_turma"): view.listar_notas_por_id_turma,
    URL("/api/v1/notas/aluno/listar/:id_aluno"): view.listar_notas_por_id_aluno,
    URL("/api/v1/notas/criar"): view.criar_nota,
    URL("/api/v1/notas/editar/:id_nota"): view.editar_nota,
    URL("/api/v1/notas/excluir/:id_nota"): view.excluir_nota,
    URL("/api/v1/notas/fee/obter/:id_turma/:id_aluno"): view.obter_fee_turma_aluno,

    URL("/api/v1/turmas_alunos/criar"): view.criar_turmas_alunos,
    URL("/api/v1/turmas_alunos/remover/:id"): view.remover_turmas_alunos,
    URL("/api/v1/turmas_alunos/listar"): view.listar_turmas_alunos,
    URL("/api/v1/turmas_alunos/listar_alunos_da_turma/:id_turma"): view.listar_alunos_turma,
    URL("/api/v1/turmas_alunos/listar_turmas_do_aluno/:id_aluno"): view.listar_turmas_aluno,
}

def url_match(path):
    for pattern, view_func in URLS.items():
        match = re.match(pattern, path)
        if match:
            return lambda req, match=match: view_func(req, **match.groupdict())
    return lambda req: JsonResponse({"error": "URL not found."}, status="404 NOT FOUND")
