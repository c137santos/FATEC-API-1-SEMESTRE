from funcoes_request_response import hola_mundinho

def url_match(url):
    url_dict = {
        "/" : hola_mundinho
    }
    return url_dict[url]