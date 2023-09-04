from funcoes_request_response import hola_mundinho, busca_arquivos_json

def url_match(url):
    url_dict = {
        "/" : hola_mundinho,
        "/get_json": busca_arquivos_json,
    }
    return url_dict[url]