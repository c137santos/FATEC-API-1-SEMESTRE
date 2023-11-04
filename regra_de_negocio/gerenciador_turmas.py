import json


# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def busca_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data


<<<<<<< HEAD
def editar_turma_svc(id, nome, professor, data_de_inicio):
=======
def obter_turma(id_turma):
    turmas = busca_turmas()
    id_turma_str = str(id_turma)
    if id_turma_str in turmas.keys():
        return turmas[id_turma_str]
    else:
        return None


def editar_turma_svc(id, nome, professor, data_de_inicio, duracao_ciclo):
>>>>>>> padrao_datas_MOMENTJS#142
    turmas = busca_turmas()
    if id in turmas.keys():
        turma = turmas[id]
        turma["nome"] = nome
        turma["professor"] = professor
        turma["data_de_inicio"] = data_de_inicio
<<<<<<< HEAD
=======
        turma["duracao_ciclo"] = duracao_ciclo
        _salvar_turmas(turmas)
        return True
    else:
        return False


# Função para criar uma nova turma
def criacao_turma(nova_turma):
    from regra_de_negocio.gerenciador_turmas_alunos import adicionar_turma_aluno

    id_nova_turma = _obter_novo_id_turma()
    for alunos in nova_turma["alunos_adicionados"]:
        turma_aluno = ({"id_turma": id_nova_turma, "id_aluno": alunos["RA"]},)
        adicionar_turma_aluno(turma_aluno)
    nova_turma.pop("alunos_adicionados", None)
    turmas = busca_turmas()
    nova_turma["quantidade_ciclos"] = 4
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
    return resposta


def excluir_turma_svc(id):
    turmas = busca_turmas()
    if id in turmas.keys():
        turmas.pop(id)
>>>>>>> padrao_datas_MOMENTJS#142
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
<<<<<<< HEAD
    return True


def busca_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return grupos_Data


# Função para criar uma nova turma
def criacao_turma(dados_nova_turma):
    dados_nova_turma_json = json.loads(dados_nova_turma)
    turmas = busca_turmas()
    grupos = busca_grupos()

    turma_novo_id = str(len(turmas) + 1)

    nova_turma = {
        "nome": dados_nova_turma_json["nome"],  # Acesse a propriedade "nome" do corpo
        "professor": dados_nova_turma_json[
            "professor"
        ],  # Acesse a propriedade "professor" do corpo
        "data_de_inicio": dados_nova_turma_json[
            "dataInicio"
        ],  # Acesse a propriedade "dataInicio" do corpo
    }
    turmas[turma_novo_id] = nova_turma
    turma_nome = turmas[turma_novo_id]["nome"]
    resposta = {
        "mensagem": f"Criação da turma {turma_nome.capitalize()} realizada com sucesso!",
        "detalhes": [],
    }

    if len(dados_nova_turma_json["grupos"]) >= 1:
        for idGrupo in dados_nova_turma_json["grupos"]:
            idGrupo = str(
                idGrupo
            )  # transforma o inteiro da lista em str para comparar com as chaves
            print(f"ID do grupo a ser atualizado: {idGrupo}")
            # Verifique se o ID do grupo existe nos grupos
            if idGrupo in grupos:
                print(f"Atualizando grupo {idGrupo} para turma {turma_novo_id}")
                grupo_Nome = grupos[idGrupo]["nome"]
                # Atualize a propriedade "turma" com um valor inteiro
                grupos[idGrupo]["turma"] = int(turma_novo_id)
                # Cria os detalhes de alterações nos grupos
                resposta["detalhes"].append(
                    f"Adicionado o grupo {grupo_Nome.capitalize()} a turma {turma_nome.capitalize()}"
                )
            else:
                resposta["detalhes"].append(
                    f"id {grupo_Nome.capitalize()} não encontrado nos grupos"
                )

    # Salve as alterações nos arquivos JSON
    _salvar_turmas(turmas)
    _salvar_grupos(grupos)
    return resposta


# Função para salvar grupos em um arquivo JSON
def _salvar_grupos(grupos):
    with open("dados/grupos.json", "w", encoding="utf-8") as f:
        json.dump(grupos, f, indent=4)


def excluir_turma(id):
    turmas = busca_turmas()
    if id in turmas.keys():
        turmas.pop(id)
        _salvar_turmas(turmas)
        return True
    else:
        return False
=======
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
>>>>>>> padrao_datas_MOMENTJS#142
