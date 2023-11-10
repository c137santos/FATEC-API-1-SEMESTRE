import csv
import json

def listar_alunos():
    with open("testes/alunos.json", "r", encoding="utf-8") as f:
        alunos = json.load(f)
    return alunos

def _obter_novo_id():
    ids_numericos = [0]
    alunos = listar_alunos()
    for id_str in alunos.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    ids_numericos.sort()
    id_max_int = ids_numericos.pop()
    novo_id = str(id_max_int + 1)
    return novo_id

def _salvar_(alunos):
    dados = json.dumps(alunos, indent=4)
    with open("testes/alunos.json", "w", encoding="utf-8") as arquivo:  # Corrigido o nome do arquivo
        arquivo.write(dados)
        return True

novo_id = _obter_novo_id()


# Obter os alunos existentes
bancoAlunos = listar_alunos()
novo_id = _obter_novo_id()
novos_alunos = {}

with open("testes/novos_alunos.csv", newline='', encoding='utf-8-sig') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')
    
    for aluno in leitor_csv:
        print(aluno)
      
        novos_alunos[novo_id] = {
            "nome": aluno["Nome completo do aluno"],
            "data_nascimento": aluno["Data de Nascimento"],
            "genero": aluno["Genêro"],
            "RA": novo_id
        }
        print(novo_id)
        novo_id = str(int(novo_id) + 1)
    
    for aluno_id, aluno_info in novos_alunos.items():
        bancoAlunos[aluno_id] = aluno_info

# Salvar o banco de dados atualizado
print(novos_alunos)
_salvar_(bancoAlunos)

print("Importação concluída com sucesso.")