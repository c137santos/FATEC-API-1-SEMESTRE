import json

#Função criada para fazer a leitura do arquivo grupos.json localizado na pasta "dados"
#O módulo json é usado para carregar o conteúdo do arquivo JSON no objeto grupos_Data. O json.load() converte o JSON em um objeto Python
#Retorno: conteúdo do arquivo como um objeto Python.
def buscando_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return import json

# Função para buscar informações sobre as turmas a partir de um arquivo JSON
def busca_turmas():
    with open("dados/criar_grupo.json", "r", encoding="utf-8") as file:
        turmas = json.load(file)
    return turmas

# Função para salvar informações sobre as turmas em um arquivo JSON
def salva_turmas(turmas):
    with open("http://127.0.0.1:5500/dados/criar_grupo.json", "w", encoding="utf-8") as file:
        json.dump(turmas, file, ensure_ascii=False, indent=4)

# Função para criar um novo grupo
def criar_grupo(nome_grupo, id_turma):
    turmas = busca_turmas()
    
    # Encontre a turma com base no id_turma
    turma = None
    for t in turmas:
        if t['id'] == id_turma:
            turma = t
            break
    
    if turma is None:
        raise ValueError('Turma não encontrada')
    if any(grupo['nome'] == nome_grupo for grupo in turma['grupos']):
        raise ValueError('Um grupo com o mesmo nome já existe nesta turma')

    # Crie um novo grupo com os dados fornecidos
    novo_grupo = {
        'nome': nome_grupo,
        'alunos': [],
    }
    
    # Adicione o novo grupo à turma
    turma['grupos'].append(novo_grupo)

    # Atualize as informações das turmas no arquivo JSON
    salva_turmas(turmas)

# Função para editar um grupo existente
def editar_grupo(id_grupo, nome_grupo, id_turma):
    turmas = busca_turmas()
    
    # Encontre a turma com base no id_turma
    turma = None
    grupo_editado = None
    for t in turmas:
        if t['id'] == id_turma:
            turma = t
            for grupo in t['grupos']:
                if grupo['id'] == id_grupo:
                    grupo['nome'] = nome_grupo
                    grupo_editado = grupo
                    break
            break
    
    if turma is None:
        raise ValueError('Turma não encontrada')
    
    if grupo_editado is None:
        raise ValueError('Grupo não encontrado')

    # Atualize as informações das turmas no arquivo JSON
    salva_turmas(turmas)

# Função para buscar alunos pertencentes a uma turma
def buscar_alunos_turma(id_turma):
    turmas = busca_turmas()
    
    # Encontre a turma com base no id_turma
    turma = None
    for t in turmas:
        if t['id'] == id_turma:
            turma = t
            break
    
    if turma is None:
        raise ValueError('Turma não encontrada')
    
    alunos_turma = []
    for aluno in turma['alunos']:
        alunos_turma.append(aluno)
    
    return alunos_turma

# Função para adicionar um aluno a um grupo
def adicionar_aluno_grupo(id_aluno, id_grupo):
    turmas = busca_turmas()
    
    # Encontre o grupo com base no id_grupo
    grupo = None
    for turma in turmas:
        for g in turma['grupos']:
            if g['id'] == id_grupo:
                grupo = g
                break
        if grupo:
            break
    
    if grupo is None:
        raise ValueError('Grupo não encontrado')

    # Adicione o ID do aluno ao grupo
    grupo['alunos'].append(id_aluno)

    # Atualize as informações das turmas no arquivo JSON
    salva_turmas(turmas)

# Função para remover um aluno de um grupo
def remover_aluno_grupo(id_aluno, id_grupo):
    turmas = busca_turmas()
    
    # Encontre o grupo com base no id_grupo
    grupo = None
    for turma in turmas:
        for g in turma['grupos']:
            if g['id'] == id_grupo:
                grupo = g
                break
        if grupo:
            break
    
    if grupo is None:
        raise ValueError('Grupo não encontrado')

    # Remova o ID do aluno do grupo, se estiver presente
    if id_aluno in grupo['alunos']:
        grupo['alunos'].remove(id_aluno)

    # Atualize as informações das turmas no arquivo JSON
    salva_t