from funcoes_request_response import hola_mundinho, get_arquivos_json

def url_match(url):
    url_dict = {
        "/" : hola_mundinho,
        "/index.html" : hola_mundinho,
        "/get_json": get_arquivos_json,
    }
    return url_dict[url]