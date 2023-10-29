import json

# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def busca_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data

def obter_turma(id_turma):
    turmas = busca_turmas()
    id_turma_str = str(id_turma)
    if id_turma_str in turmas.keys():
        return turmas[id_turma_str]
    else:
        return None

def editar_turma_svc(id, nome, professor, data_de_inicio, duracao_ciclo):
    turmas = busca_turmas()
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
def criacao_turma(nova_turma):
    turmas = busca_turmas()
    id_nova_turma = _obter_novo_id_turma()
    nova_turma["quantidade_ciclos"] = 4
    turmas[id_nova_turma] = nova_turma
    turma_nome = turmas[id_nova_turma]["nome"]
    resposta = {
        "mensagem": f"Criação da turma {turma_nome.capitalize()} realizada com sucesso!",
        "detalhes": [],
        "nova_turma": nova_turma,
        "id_nova_turma": id_nova_turma
    }

    # Salve as alterações nos arquivos JSON
    _salvar_turmas(turmas)
    return resposta

def excluir_turma_svc(id):
    turmas = busca_turmas()
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

def _obter_novo_id_turma():
    ids_numericos = []
    turmas = busca_turmas()
    for id_str in turmas.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    id_max_int = max(ids_numericos)
    novo_id = str(id_max_int + 1)
    return novo_id