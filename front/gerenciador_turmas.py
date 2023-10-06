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
    return grupo_data

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


# Esta função busca grupos de uma turma específica e os nomes dos alunos associados a esses grupos
def busca_info_turmas(id):
    grupos = busca_grupos_turma(id)
    alunos = busca_grupos_alunos(grupos)
    return grupos, alunos


# Esta função busca grupos de uma turma específica
def busca_grupos_turma(id):
    grupo_data = {}  # Dicionário para armazenar grupos
    grupo_data_raw = busca_grupos()  # Buscar dados brutos dos grupos
    for grupo_id, grupo_info in grupo_data_raw.items():
        if grupo_info["turma"] == int(id):  # Verificar se o grupo pertence à turma especificada
            nome_grupo = grupo_info["nome"]  # Obter o nome do grupo
            grupo_data[grupo_id] = nome_grupo  # Adicionar o grupo ao dicionário de grupos
    return grupo_data  # Retornar os grupos

# Esta função busca alunos associados a grupos
def busca_grupos_alunos(grupos):
    alunos_data_raw = busca_alunos()  # Buscar dados brutos dos alunos
    alunos_data = {}  # Dicionário para armazenar alunos
    for id_aluno, aluno_info in alunos_data_raw.items():
        if id_aluno in grupos:  # Verificar se o aluno está associado a um dos grupos
            nome_aluno = aluno_info["nome"]  # Obter o nome do aluno
            alunos_data[id_aluno] = nome_aluno  # Adicionar o aluno ao dicionário de alunos
    return alunos_data  # Retornar os alunos associados aos grupos

# Esta função busca os nomes dos alunos
def busca_info_alunos(alunos):
    alunos_data_raw = busca_alunos()  # Buscar dados brutos dos alunos
    alunos_data = {}  # Dicionário para armazenar nomes de alunos
    for id_aluno, nome_aluno in alunos.items():
        alunos_data[id_aluno] = nome_aluno  # Adicionar o nome do aluno ao dicionário de nomes de alunos
    return alunos_data  # Retornar os nomes dos alunos




