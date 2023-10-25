import json
from regra_de_negocio.gerenciador_alunos import listar_alunos_svc

# Listar grupos do Json
def listar_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupo_data = json.load(f)
        return grupo_data

# Relaciona alunos pertencentes ao grupo que estou editando verificando o id do grupo ao id do aluno e retorna como lista
def listar_grupos_alunos_svc():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupo_data = json.load(f)
        return grupo_data

def obter_grupos_svc(id):
    grupos = listar_grupos ()
    grupo = grupos[id]
    return grupo

def listar_grupo_alunos(id):
    grupo_alunos = listar_grupos_alunos_svc()
    alunos = listar_alunos_svc()
    resultado = {}
    for idaluno in grupo_alunos.keys():
        if idaluno in alunos.keys() and grupo_alunos[idaluno]["grupo"] == id:
            resultado[idaluno] = alunos[idaluno]
    return resultado

def editar_grupo_svc(id, turma,nome):
    grupos = listar_grupos()
    if id in grupos.keys():
        grupo = grupos[id]
        grupo["turma"] = turma
        grupo["nome"] = nome
        _salvar_grupos(grupo)
        return True
    else:
        return False
    
# Parâmetro: um dicionário onde cada grupo é um par chave-valor
# Retorna:
#   True se a operação for bem sucedida
def _salvar_grupos(grupos):
    dados = json.dumps(grupos, indent=4)
    with open("dados/grupos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
    return True

def adicionar_grupo_aluno_svc(id, grupo_id):
    grupo_alunos = listar_grupos_alunos_svc()
    grupo_alunos[id] = {}
    grupo_alunos[id]["grupo"] = grupo_id
    _salvar_grupo_alunos(grupo_alunos)
    return True

def remover_grupo_aluno_svc(aluno_id, grupo_id):
    grupo_alunos = listar_grupos_alunos_svc()
    grupo_alunos_manter = {}
    for id in grupo_alunos:
        grupo_aluno = grupo_alunos[id]
        if id != aluno_id:
            grupo_alunos_manter[id] = grupo_aluno
        elif grupo_aluno["grupo"] != grupo_id:
            grupo_alunos_manter[id] = grupo_aluno
        else:
            print("Removido!")
    _salvar_grupo_alunos(grupo_alunos_manter)

# Parâmetro: um dicionário onde cada turma é um par chave-valor
# Retorna:
#   True se a operação for bem sucedida
def _salvar_grupo_alunos(grupo_alunos):
    dados = json.dumps(grupo_alunos, indent=4)
    with open("dados/grupo_alunos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
    return True

#Função criada para fazer a leitura do arquivo grupos.json localizado na pasta "dados"
#O módulo json é usado para carregar o conteúdo do arquivo JSON no objeto grupos_Data. O json.load() converte o JSON em um objeto Python
#Retorno: conteúdo do arquivo como um objeto Python.
def buscando_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return grupos_Data
