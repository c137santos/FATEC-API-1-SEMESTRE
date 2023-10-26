import json


# Função criada para fazer a leitura do arquivo grupos.json localizado na pasta "dados"
# O módulo json é usado para carregar o conteúdo do arquivo JSON no objeto grupos_Data. O json.load() converte o JSON em um objeto Python
# Retorno: conteúdo do arquivo como um objeto Python.
def buscando_grupos_svc():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_data = json.load(f)
    return grupos_data

def buscando_grupo_alunos():
    with open("dados/grupo_alunos.json", "r", encoding="utf-8") as f:
        grupos_alunos = json.load(f)
    return grupos_alunos 

def buscando_grupos_turma_especifica_svc(id_turma):
    todos_grupos = buscando_grupos_svc()
    grupos_filtrados = [grupo for grupo in todos_grupos if grupo["turma"] == id_turma]
    return grupos_filtrados

def listando_aluno_grupo_svc(ids_grupos_de_turmas):
    grupos_alunos = buscando_grupo_alunos()
    alunos = []
    [alunos.append(grupo_aluno["aluno"]) for grupo_aluno in grupos_alunos if grupo_aluno["grupo"] in ids_grupos_de_turmas]
    return grupos_alunos

# Função para salvar informações sobre as turmas em um arquivo JSON
def salva_grupo(novo_grupo):
    with open("dados/grupos.json", "w", encoding="utf-8") as file:
        json.dump(novo_grupo, file, ensure_ascii=False, indent=4)


# Função para criar um novo grupo
def criar_grupo(nome_grupo, id_turma):
    from .gerenciador_turmas import busca_turmas

    turmas = busca_turmas()
    turma = None
    for t in turmas:
        if t["id"] == id_turma:
            turma = t
            break

    if turma is None:
        raise ValueError("Turma não encontrada")

    # Crie um novo grupo com os dados fornecidos
    novo_grupo = {
        "nome": nome_grupo,
        "turma": turma,
    }

    # Cria um Grupo
    salva_grupo(novo_grupo)


# Função para editar um grupo existente
def editar_grupo(id_grupo, nome_grupo, id_turma):
    turmas = busca_turmas()

    # Encontre a turma com base no id_turma
    turma = None
    grupo_editado = None
    for t in turmas:
        if t["id"] == id_turma:
            turma = t
            for grupo in t["grupos"]:
                if grupo["id"] == id_grupo:
                    grupo["nome"] = nome_grupo
                    grupo_editado = grupo
                    break
            break

    if turma is None:
        raise ValueError("Turma não encontrada")

    if grupo_editado is None:
        raise ValueError("Grupo não encontrado")

    # Atualize as informações das turmas no arquivo JSON
    salva_turmas(turmas)


# Função para buscar alunos pertencentes a uma turma
def buscar_alunos_turma(id_turma):
    turmas = busca_turmas()

    # Encontre a turma com base no id_turma
    turma = None
    for t in turmas:
        if t["id"] == id_turma:
            turma = t
            break

    if turma is None:
        raise ValueError("Turma não encontrada")

    alunos_turma = []
    for aluno in turma["alunos"]:
        alunos_turma.append(aluno)

    return alunos_turma


# Função para adicionar um aluno a um grupo
def adicionar_aluno_grupo(id_aluno, id_grupo):
    turmas = busca_turmas()

    # Encontre o grupo com base no id_grupo
    grupo = None
    for turma in turmas:
        for g in turma["grupos"]:
            if g["id"] == id_grupo:
                grupo = g
                break
        if grupo:
            break

    if grupo is None:
        raise ValueError("Grupo não encontrado")

    # Adicione o ID do aluno ao grupo
    grupo["alunos"].append(id_aluno)

    # Atualize as informações das turmas no arquivo JSON
    salva_turmas(turmas)


# Função para remover um aluno de um grupo
def remover_aluno_grupo(id_aluno, id_grupo):
    turmas = busca_turmas()

    # Encontre o grupo com base no id_grupo
    grupo = None
    for turma in turmas:
        for g in turma["grupos"]:
            if g["id"] == id_grupo:
                grupo = g
                break
        if grupo:
            break

    if grupo is None:
        raise ValueError("Grupo não encontrado")

    # Remova o ID do aluno do grupo, se estiver presente
    if id_aluno in grupo["alunos"]:
        grupo["alunos"].remove(id_aluno)

    # Atualize as informações das turmas no arquivo JSON
    salva_t
