import views.funcoes_request_response as view
from wgsi import JsonResponse
import re


def URL(pattern):
    return re.sub(r":(\w+)", r"(?P<\1>[^/]+)", pattern) + "$"


# Essa função tem objetivo de compreender os IDs que são passados na URL por meio da aplicação de regex.

URLS = {
    URL("/"): view.hola_mundinho,
    URL("/get_json"): view.get_arquivos_json,
    URL("/api/v1/turmas/get"): view.get_turmas,
    URL("/api/v1/grupo_semTurma/get"): view.grupo_semTurma,
    URL("/api/v1/alunos/:id/edit"): view.edit_aluno,
    URL("/api/v1/get_grupos_alunos/:id/get"): view.get_grupos_alunos
}


def url_match(path):
    for pattern, view_func in URLS.items():
        match = re.match(pattern, path)
        if match:
            return lambda req, match=match: view_func(req, **match.groupdict())
    return lambda req: JsonResponse({"error": "URL not found."}, status="404 NOT FOUND")
