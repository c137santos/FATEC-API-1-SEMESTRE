import json


# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def buscar_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data


def obter_turma(id_turma):
    turmas = buscar_turmas()
    id_turma_str = str(id_turma)
    if id_turma_str in turmas.keys():
        return turmas[id_turma_str]
    else:
        return None


def editar_turma_svc(id, nome, professor, data_de_inicio, duracao_ciclo):
    turmas = buscar_turmas()
    if id in turmas.keys():
        turma = turmas[id]
        turma["nome"] = nome
        turma["professor"] = professor
        turma["data_de_inicio"] = data_de_inicio
        turma["duracao_ciclo"] = duracao_ciclo
        _salvar_turmas(turmas)
        return True
    else:
        return False


# Função para criar uma nova turma
def criacao_turma(dados_nova_turma, nova_turma_id, turmas):
    dados_nova_turma_json = dados_nova_turma
    duracao_ciclo = int(dados_nova_turma_json["duracao_ciclo"])
    quantidade_ciclos = int(dados_nova_turma_json["quantidade_ciclos"])

    nova_turma = {
        "nome": dados_nova_turma_json["nome"],  # Acesse a propriedade "nome" do corpo
        "professor": dados_nova_turma_json[
            "professor"
        ],  # Acesse a propriedade "professor" do corpo
        "data_de_inicio": dados_nova_turma_json[
            "data_de_inicio"
        ],  # Acesse a propriedade "dataInicio" do corpo
        "duracao_ciclo": dados_nova_turma_json["duracao_ciclo"],
        "quantidade_ciclos": dados_nova_turma_json["quantidade_ciclos"],
    }

    turmas[nova_turma_id] = nova_turma
    turma_nome = turmas[nova_turma_id]["nome"]
    resposta = {
        "mensagem": f"Criação da turma {turma_nome.capitalize()} realizada com sucesso!",
        "nova_turma": nova_turma,
        "id_nova_turma": nova_turma_id,
        "quantidade_ciclos": quantidade_ciclos,
    }

    # Salve as alterações nos arquivos JSON
    _salvar_turmas(turmas)
    return resposta, quantidade_ciclos, duracao_ciclo


def excluir_turma_svc(id):
    turmas = buscar_turmas()
    if id in turmas.keys():
        turmas.pop(id)
        _salvar_turmas(turmas)
        return True
    else:
        return False


# Parâmetro: um dicionário onde cada turma é um par chave-valor
# Retorna:
#   True se a operação for bem sucedida
def _salvar_turmas(turmas):
    dados = json.dumps(turmas, indent=4)
    with open("dados/turmas.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
        return True
