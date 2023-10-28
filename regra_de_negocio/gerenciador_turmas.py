import json
from regra_de_negocio.service import gerando_novo_id


# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def buscando_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data

def _salvar_turmas(turmas):
    dados = json.dumps(turmas, indent=4)
    with open("dados/turmas.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
    return True

def editar_turma_svc(id, nome, professor, data_de_inicio, duracao_ciclo):
    turmas = buscando_turmas()
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
# Parâmetro: um dicionário onde cada turma é um par chave-valor
# Retorna:
#   True se a operação for bem sucedida

# Função para criar uma nova turma
def criacao_turma(dados_nova_turma):
    dados_nova_turma_json = dados_nova_turma
    turmas = buscando_turmas()

    nova_turma_id = gerando_novo_id(turmas)

    nova_turma = {
        "nome": dados_nova_turma_json["nome"],  # Acesse a propriedade "nome" do corpo
        "professor": dados_nova_turma_json[
            "professor"
        ],  # Acesse a propriedade "professor" do corpo
        "data_de_inicio": dados_nova_turma_json[
            "dataInicio"
        ],  # Acesse a propriedade "dataInicio" do corpo
        "duracao_ciclo": dados_nova_turma_json["duracaoCiclo"],
        "quantidade_ciclos": 4,
    }
    turmas[nova_turma_id] = nova_turma
    turma_nome = turmas[nova_turma_id]["nome"]
    resposta = {
        "mensagem": f"Criação da turma {turma_nome.capitalize()} realizada com sucesso!",
        "detalhes": [],
    }

    # Salve as alterações nos arquivos JSON
    _salvar_turmas(turmas)
    return resposta


def excluir_turma_svc(id):
    turmas = buscando_turmas()
    if id in turmas.keys():
        turmas.pop(id)
        _salvar_turmas(turmas)
        return True
    else:
        return False
