import json

# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def busca_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data

# Esta função busca informações sobre os grupos a partir de um arquivo JSON e as retorna
def busca_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupo_data = json.load(f)
        grupo_semTurma = {}
        for grupoId, info_grupo in grupo_data.items():
            if info_grupo["turma"] == int(0):
                nome_grupo = info_grupo["nome"]
                grupo_semTurma[grupoId] = nome_grupo
    return grupo_data, grupo_semTurma

# Esta função busca informações sobre os grupos de alunos a partir de um arquivo JSON e as retorna
def busca_grupo_alunos():
    with open("dados/grupo_alunos.json", "r", encoding="utf-8") as f:
        grupo_alunos_data = json.load(f)
    return grupo_alunos_data

# Esta função busca informações sobre os alunos a partir de um arquivo JSON e as retorna
def busca_alunos():
    with open("dados/alunos.json", "r", encoding="utf-8") as f:
        alunos_data = json.load(f)
    return alunos_data


# Esta função busca grupos e alunos de uma turma específica
def busca_info_turmas(id):
    grupos = busca_grupos_turma(id)
    alunos_grupo = busca_grupos_alunos(grupos)
    alunos = busca_info_alunos(alunos_grupo)
    return grupos, alunos

# Esta função busca grupos de uma turma específica
def busca_grupos_turma(id):
    grupo_data_raw, grupo_semTurma = busca_grupos()  # Buscar dados brutos dos grupos
    grupo_data = {}  # Dicionário para armazenar grupos
    for grupo_id, grupo_info in grupo_data_raw.items():
        if grupo_info["turma"] == int(id):  # Verificar se o grupo pertence à turma especificada
            nome_grupo = grupo_info["nome"]  # Obter o nome do grupo
            grupo_data[grupo_id] = nome_grupo  # Adicionar o grupo ao dicionário de grupos
    return grupo_data  # Retornar os grupos

# Esta função busca alunos associados a grupos
def busca_grupos_alunos(grupos):
    grupos_alunos_data_raw = busca_grupo_alunos()  # Buscar dados brutos de alunos e seus respectivos grupos
    alunos = []
    grupos =  grupos.keys()
    # Iterar sobre os grupos da turma especificada
    for grupo_id in grupos:
        for aluno_id, aluno_info in grupos_alunos_data_raw.items():
            if aluno_info["grupo"] == int(grupo_id):  # Comparar a chave do grupo com o valor de "grupo" em aluno_info
                alunos.append(aluno_id)
    return alunos

# Esta função busca os nomes dos alunos
def busca_info_alunos(alunos_grupo):
    alunos_data_raw = busca_alunos()  # Buscar dados brutos dos alunos
    alunos_data = {}  # Dicionário para armazenar informações dos alunos
    for aluno_id, aluno_info in alunos_data_raw.items():
        if aluno_id in alunos_grupo:
            nome_aluno = aluno_info["nome"]  # Obter o nome do aluno
            alunos_data[aluno_id] = nome_aluno  # Adicionar o nome do aluno ao dicionário de nomes de alunos
    return alunos_data  # Retornar as informações dos alunos
