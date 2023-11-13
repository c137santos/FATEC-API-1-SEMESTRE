import os
import json

def salvar_arquivo_csv(requisicao):
    """formato requisicao:
    """
    requisicao = requisicao
    print(requisicao)
    nome_arquivo = requisicao['nome_arquivo'].value
    # Salvar o arquivo no disco
    arquivo = requisicao['arquivo']
    caminho_arquivo = os.path.join("../importacao", nome_arquivo)
    with open(caminho_arquivo, 'wb') as f:
        f.write(arquivo.file.read())


