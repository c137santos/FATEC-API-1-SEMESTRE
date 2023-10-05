import json

# A função obter_todas_turmas() retorna:
#    erro: possível erro ao ler o arquivo.
#    turmas: vetor de dicionários contendo as turmas.
def obter_todas_turmas():
    try:
        with open("dados/turmas.json", 'r', encoding="utf-8") as arquivo:
            dados = arquivo.read()
            print(dados)
            turmas = json.loads(dados)
            print(turmas)
            return None, turmas
    except:
        return "erro ao ler o arquivo de turmas", {}

# A função obter_ultimo_id() retorna:
#    erro: possível erro ao obter o id.
#    turmas: o último id disponível.
def obter_ultimo_id():
    erro, turmas = obter_todas_turmas()
    if not erro:
        return sorted(turmas.keys()).pop()
    return None

# A função obter_novo_id() retorna:
#    o próximo id disponível para uma nova turma.
def obter_novo_id():
    ultimo_id = obter_ultimo_id()
    # return int(ultimo_id) + 1 if ultimo_id else 1
    if ultimo_id:
        return str(int(ultimo_id) + 1)
    else:
        return str(1)

# Parâmetro: um dicionário onde cada turma é um par chave-valor
# Retorna: 
#   um possível erro
#   salva a lista de turmas em um arquivo JSON (turmas.json)
def salvar_turmas(turmas):
    try:
        dados = json.dumps(turmas, indent=4)
        with open("dados/turmas.json", "w", encoding="utf-8") as arquivo:
            arquivo.write(dados)
            return None
    except:
        return "erro ao serializar ou persistir a lista de turmas no arquivo"

#Removendo turmas com base no seu id.
# 1° ela obtém a lista atual de turmas.
# Se id existir, remove a turma com o ID especificado usando o método pop.
def remover_turma(id):
    erro, turmas = obter_todas_turmas()
    if not erro and id in turmas:
        turmas.pop(id)
        salvar_turmas(turmas)

# Parâmetros: uma turma
# A função tem a finalidade de adicionar uma nova turma ao dicionário de turmas.
def inserir_turma(nome, professor, data_de_inicio):
    erro, turmas = obter_todas_turmas()
    if not erro:
        turma = {}
        turma["nome"] = nome
        turma["professor"] = professor
        turma["data_de_inicio"] = data_de_inicio
        turmas[obter_novo_id()] = turma
        salvar_turmas(turmas)

#Editando turmas:
#Essa função tem a finalidade de editar as informações de uma turma existente.
def editar_turmas(id, nome, professor, data_de_inicio):
    erro, turmas = obter_todas_turmas()
    if not erro and id in turmas:
        turma = turmas[id]
        turma["nome"] = nome
        turma["professor"] = professor
        turma["data_de_inicio"] = data_de_inicio
        salvar_turmas(turmas)


#erro, turmas = obter_todas_turmas()

# print(turmas[0])
# turma3 = {"nome":"T3"}
# turma2 = {"nome":"T2"}
# turmas = {"3":turma3, "2":turma2}
# salvar_turmas(turmas)

# editar_turmas("2", "TESTENOME", "TESTEPROFESSOR", "TESTEDATA")

# remover_turma("5")

# inserir_turma("TESTENOME", "TESTEPROFESSOR", "TESTEDATA")