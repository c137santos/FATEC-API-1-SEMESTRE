import json
import regra_de_negocio.global_settings as global_settings


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


def editar_turma_svc(
    id, nome, professor, data_de_inicio, alunos_adicionados, alunos_excluidos
):
    from regra_de_negocio.gerenciador_turmas_alunos import (
        adicionar_turma_aluno,
        remover_aluno_da_turma,
    )

    turmas = busca_turmas()
    id_turma = 0
    if id in turmas.keys():
        id_turma = id
        turma = turmas[id]
        turma["nome"] = nome
        turma["professor"] = professor
        turma["data_de_inicio"] = data_de_inicio
        _salvar_turmas(turmas)

        for alunos in alunos_adicionados:
            turma_aluno = ({"id_turma": id_turma, "id_aluno": str(alunos["RA"])},)
            adicionar_turma_aluno(turma_aluno)

        for alunos in alunos_excluidos:
            remover_aluno_da_turma(id_turma, alunos["RA"])
    else:
        return False


# Função para criar uma nova turma
def criacao_turma(nova_turma):
    from regra_de_negocio.gerenciador_turmas_alunos import adicionar_turma_aluno

    id_nova_turma = _obter_novo_id_turma()
    turmas = busca_turmas()
    nova_turma["quantidade_ciclos"] = global_settings.read_global_settings()[
        "quant_ciclos"
    ]
    nova_turma["duracao_ciclo"] = global_settings.read_global_settings()[
        "quant_dias_ciclo"
    ]
    alunos_adicionados = nova_turma.pop("alunos_adicionados")
    turmas[id_nova_turma] = nova_turma
    turma_nome = turmas[id_nova_turma]["nome"]
    resposta = {
        "mensagem": f"Criação da turma {turma_nome.capitalize()} realizada com sucesso!",
        "detalhes": [],
        "nova_turma": nova_turma,
        "id_nova_turma": id_nova_turma,
    }

    # Salve as alterações nos arquivos JSON
    _salvar_turmas(turmas)
    for alunos in alunos_adicionados:
        turma_aluno = ({"id_turma": id_nova_turma, "id_aluno": str(alunos["RA"])},)
        adicionar_turma_aluno(turma_aluno)
    return resposta


def excluir_turma(id):
    turma = obter_turma(id)
    if not turma:
        raise ValueError(f"Turma com o ID {id} não encontrada.")

    turmas = busca_turmas()
    turmas.pop(id)
    _salvar_turmas(turmas)

    return {"message": f"Turma {id} excluída com sucesso."}


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
    ids_numericos.append(0)
    turmas = busca_turmas()
    for id_str in turmas.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    ids_numericos.sort()
    id_max_int = ids_numericos.pop()
    novo_id = str(id_max_int + 1)
    return novo_id
