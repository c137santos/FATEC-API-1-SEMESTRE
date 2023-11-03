import json
from regra_de_negocio import service


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
def criacao_turma(nova_turma):
    from regra_de_negocio.gerenciador_turmas_alunos import adicionar_turma_aluno

    id_nova_turma = service.gerar_novo_id_svc()
    for alunos in nova_turma["alunos_adicionados"]:
        turma_aluno = ({"id_turma": id_nova_turma, "id_aluno": alunos["RA"]},)
        adicionar_turma_aluno(turma_aluno)
    nova_turma.pop("alunos_adicionados", None)
    turmas = buscar_turmas()
    nova_turma["quantidade_ciclos"] = 4
    turmas[id_nova_turma] = nova_turma
    turma_nome = turmas[id_nova_turma]["nome"]
    resposta = {
        "mensagem": f"Criação da turma {turma_nome.capitalize()} realizada com sucesso!",
        "nova_turma": nova_turma,
        "id_nova_turma": id_nova_turma,
        "quantidade_ciclos": 4,
    }

    # Salve as alterações nos arquivos JSON
    _salvar_turmas(turmas)
    return resposta


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
