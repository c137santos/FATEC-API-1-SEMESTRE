import views.funcoes_request_response as view
from wgsi import JsonResponse
import re


def URL(pattern):
    return re.sub(r":(\w+)", r"(?P<\1>[^/]+)", pattern) + "$"


# Essa função tem objetivo de compreender os IDs que são passados na URL por meio da aplicação de regex.

URLS = {
    URL("/"): view.hola_mundinho,
    URL("/get_json"): view.get_arquivos_json,
    URL("/api/v1/alunos/:id/edit"): view.edit_aluno,
    URL("/api/v1/globalsettings/"): view.get_global_settings,
    URL("/api/v1/turmas/get"): view.get_turmas,
    URL("/api/v1/turmas/excluir/:id"):view.api_v1_turmas_excluir,
}


def url_match(path):
    for pattern, view_func in URLS.items():
        match = re.match(pattern, path)
        if match:
            return lambda req, match=match: view_func(req, **match.groupdict())
    return lambda req: JsonResponse({"error": "URL not found."}, status="404 NOT FOUND")
