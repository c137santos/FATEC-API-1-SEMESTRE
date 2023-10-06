import json

# Retorna:
#    um dicionário onde cada turma é um par chave-valor
def obter_todas_turmas():
    with open("dados/turmas.json", 'r', encoding="utf-8") as arquivo:
        dados = arquivo.read()
        turmas = json.loads(dados)
        return turmas

# Retorna
#    o último id disponível.
def obter_ultimo_id():
    return sorted(obter_todas_turmas().keys()).pop()

# Retorna:
#    o próximo id disponível para uma nova turma.
def obter_novo_id():
    ultimo_id = obter_ultimo_id()
    if ultimo_id:
        return str(int(ultimo_id) + 1)
    else:
        return str(1)

# Parâmetro: um dicionário onde cada turma é um par chave-valor
def salvar_turmas(turmas):
    dados = json.dumps(turmas, indent=4)
    with open("dados/turmas.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)

# Remove uma turma com base no seu id.
# Parâmetro: o id da turma a ser removida.
def remover_turma(id):
    turmas = obter_todas_turmas()
    if id in turmas.keys():
        turmas.pop(id)
        salvar_turmas(turmas)

# Parâmetros: nome, professor e data de início (campos da nova turma)
# A função tem a finalidade de adicionar uma nova turma ao dicionário de turmas.
def inserir_turma(nome, professor, data_de_inicio):
    turmas = obter_todas_turmas()
    turma = {}
    turma["nome"] = nome
    turma["professor"] = professor
    turma["data_de_inicio"] = data_de_inicio
    turmas[obter_novo_id()] = turma
    salvar_turmas(turmas)

#Editando turmas:
#Essa função tem a finalidade de editar as informações de uma turma existente.
# Parâmetros: 
#   id da turma existente, 
#   nome, professor e data de início (campos a serem modificados)
def editar_turmas(id, nome, professor, data_de_inicio):
    turmas = obter_todas_turmas()
    if id in turmas.keys():
        turma = turmas[id]
        turma["nome"] = nome
        turma["professor"] = professor
        turma["data_de_inicio"] = data_de_inicio
        salvar_turmas(turmas)