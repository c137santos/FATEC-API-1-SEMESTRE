import unittest
import regra_de_negocio.gerenciador_turmas as gt
import json

# Resto do seu código aqui


import sys

sys.path.append(".")


class TesteGerenciadorTurmas(unittest.TestCase):

    def busca_alunos():
# Abrir o arquivo JSON que contém os dados dos alunos
        with open("dados/alunos.json", "r", encoding="utf-8") as f:
            alunos_data = json.load(f)
            return alunos_data
def excluir_aluno(id):
    # Abrir o arquivo JSON que contém os dados dos alunos
    with open("dados/alunos.json", "r", encoding="utf-8") as f:
        alunos_data = json.load(f)

    # Verificar se o ID do aluno existe no dicionário de alunos
    if id in alunos_data:
        # Remover o aluno do dicionário
        aluno_removido = alunos_data.pop(id)

        # Salvar as alterações de volta no arquivo JSON
        with open("dados/alunos.json", "w", encoding="utf-8") as f:
            json.dump(alunos_data, f, indent=4)

        # Retornar o aluno removido como confirmação
        return aluno_removido
    else:
        # Se o ID do aluno não existir, retornar None para indicar que não foi possível encontrar o aluno
        return None
