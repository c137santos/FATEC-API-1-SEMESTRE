import json
import front.gerenciador_turmas as gt

def busca_dados_json():
    with open("dados/alunos.json", "r") as f:
        data = json.load(f)
        return data
    
def  busca_turmas_json(): #retorna todas turmas
    turmas_data = gt.busca_turmas()
    return turmas_data
    
def busca_info_turmas_json(id): #retorna grupos e alunos de um turma_id
    grupos_data, alunos_data = gt.busca_info_turmas(id)
    return grupos_data, alunos_data

def busca_grupo_semTurma():
    grupos_Data, grupo_semTurma_data = gt.busca_grupos()
    return grupos_Data, grupo_semTurma_data

