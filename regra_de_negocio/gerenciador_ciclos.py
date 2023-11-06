import json


def listar_ciclos():
    with open("dados/ciclos.json", "r", encoding="utf-8") as f:
        return json.load(f)


def listar_ciclos_por_id_turma(id_turma):
    if not id_turma:
        return {}
    id_turma_str = str(id_turma)
    ciclos = listar_ciclos()
    ciclos_encontrados = {}
    for id_ciclo in ciclos.keys():
        if id_turma_str == ciclos[id_ciclo]["id_turma"]:
            ciclos_encontrados[id_ciclo] = ciclos[id_ciclo]
    return ciclos_encontrados


def obter_ciclo(id_ciclo):
    id_ciclo_str = str(id_ciclo)
    ciclos = listar_ciclos()
    if id_ciclo_str in ciclos.keys():
        return ciclos[id_ciclo_str]
    else:
        return None


def obter_ultimo_ciclo_por_id_turma(id_turma):
    id_turma_str = str(id_turma)
    ciclos = listar_ciclos_por_id_turma(id_turma_str)
    if len(ciclos) == 0:
        return None
    else:
        id_ultimo_ciclo = None
        ultimo_ciclo = None
        for id_ciclo in ciclos.keys():
            if not ultimo_ciclo:
                ultimo_ciclo = ciclos[id_ciclo]
                id_ultimo_ciclo = id_ciclo
            if ultimo_ciclo["numero_ciclo"] > ciclos[id_ciclo]["numero_ciclo"]:
                ultimo_ciclo = ciclos[id_ciclo]["numero_ciclo"]
                id_ultimo_ciclo = id_ciclo
        return id_ultimo_ciclo, ultimo_ciclo


def adicionar_ciclo(ciclo):
    ciclos = listar_ciclos()
    ciclos_por_id_turma = listar_ciclos_por_id_turma(ciclo["id_turma"])
    numero_ciclo = (
        len(ciclos_por_id_turma) + 1
    )  # em caso de remoção de ciclo, alterar essa linha ou tratar na remoção
    ciclo["numero_ciclo"] = numero_ciclo
    novo_id_ciclo = _obter_novo_id_ciclo()
    ciclos[novo_id_ciclo] = ciclo
    return _salvar_ciclos(ciclos)


def editar_ciclo(id_ciclo, ciclo_atualizado):
    try:
        id_ciclo_str = str(id_ciclo)
        ciclos = listar_ciclos()
        if id_ciclo_str in ciclos.keys():
            ciclos[id_ciclo_str]["id_turma"] = ciclo_atualizado["id_turma"]
            ciclos[id_ciclo_str]["duracao"] = int(ciclo_atualizado["duracao"])
            ciclos[id_ciclo_str]["peso_nota"] = float(ciclo_atualizado["peso_nota"])
            ciclos[id_ciclo_str]["numero_ciclo"] = int(ciclo_atualizado["numero_ciclo"])
            ciclos[id_ciclo_str]["prazo_insercao_nota"] = int(
                ciclo_atualizado["prazo_insercao_nota"]
            )
            return _salvar_ciclos(ciclos)
        else:
            raise KeyError("Ciclo não encontrado.")
    except KeyError as e:
        return f"Falha na edição: {str(e)}"


def _obter_novo_id_ciclo():
    ids_numericos = []
    ids_numericos.append(0)
    ciclos = listar_ciclos()
    for id_str in ciclos.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    ids_numericos.sort()
    id_max_int = ids_numericos.pop()
    novo_id = str(id_max_int + 1)
    return novo_id


def _salvar_ciclos(ciclos):
    dados = json.dumps(ciclos, indent=4)
    with open("dados/ciclos.json", "w", encoding="utf-8") as f:
        f.write(dados)
        return True


def excluir_ciclo_da_turma(id_turma):
    print(f'\n> Excluindo ciclos relacionados a turma...\n')
    ciclos_da_turma = listar_ciclos_por_id_turma(id_turma)
    if not ciclos_da_turma:
        return

    todos_os_ciclos = listar_ciclos()
    ciclos_a_manter = {
        id_ciclo: ciclo
        for id_ciclo, ciclo in todos_os_ciclos.items()
        if ciclo["id_turma"] != id_turma
    }

    _salvar_ciclos(ciclos_a_manter)


