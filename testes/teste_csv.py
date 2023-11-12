import csv
import json
import re

def listar_alunos():
    with open("testes/alunos.json", "r", encoding="utf-8") as f:
        alunos = json.load(f)
        return alunos
    
def listar_turma_aluno():
    with open("testes/turmas_alunos.json", "r", encoding="utf-8") as f:
        turmas_alunos = json.load(f)
        return turmas_alunos
    
def ler_csv():
    with open("testes/novos_alunos.csv", newline='', encoding='utf-8-sig') as arquivo_csv:
        leitor_csv = list(csv.DictReader(arquivo_csv, delimiter=';'))
        verifica_csv(leitor_csv)
        return leitor_csv
    
def valida_nome(nome):
    # Verifica se o nome contém apenas letras e espaços
    return bool(re.match(r'^[A-Za-z\s]+$', nome))

def valida_genero(genero):
    # Verifica se o gênero contém apenas letras
    return bool(re.match(r'^[A-Za-z]+$', genero))

def valida_data(data):
    # Verifica se a data está no formato dd/mm/aaaa
    return bool(re.match(r'^\d{2}/\d{2}/\d{4}$', data))

def verifica_csv(leitor_csv):
    # Verifica se a primeira linha contém os cabeçalhos esperados
    cabecalhos_esperados = ["Nome completo do aluno", "Genêro", "Data de Nascimento"]
    if leitor_csv.fieldnames != cabecalhos_esperados:
        raise ValueError("Cabeçalhos do CSV não correspondem aos esperados.")

    # Verifica cada linha do CSV
    for aluno in leitor_csv:
        # Verifica se todos os campos estão presentes e não são vazios
        if not aluno["Nome completo do aluno"] or not aluno["Genêro"] or not aluno["Data de Nascimento"]:
            raise ValueError("Campos incompletos no CSV.")

        # Verifica se o nome e o gênero contêm apenas letras
        if not valida_nome(aluno["Nome completo do aluno"]):
            raise ValueError(f"Nome inválido em: {aluno['Nome completo do aluno']}")

        if not valida_genero(aluno["Genêro"]):
            raise ValueError(f"Gênero inválido em: {aluno['Genêro']}")

        # Verifica se a data está no formato correto
        if not valida_data(aluno["Data de Nascimento"]):
            raise ValueError(f"Data inválida em: {aluno['Data de Nascimento']}")

    print("CSV verificado com sucesso!")


def _obter_novo_id(entidade):
    ids_numericos = [0]
    for id_str in entidade.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    ids_numericos.sort()
    id_max_int = ids_numericos.pop()
    novo_id = str(id_max_int + 1)
    return novo_id

def _salvar_alunos(alunos):
    dados = json.dumps(alunos, indent=4)
    with open("testes/alunos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
    return True

def _salvar_turma_alunos(turmas_alunos):
    dados = json.dumps(turmas_alunos, indent=4)
    with open("testes/turmas_alunos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
    return True
    
def criar_relacao_turma_aluno(turma_id, novos_alunos):
    turmas_alunos = listar_turma_aluno()
    novo_id =_obter_novo_id(turmas_alunos)
    for aluno_id in novos_alunos.keys():
        turmas_alunos[novo_id] = {
            "id_turma": turma_id,
            "id_aluno": aluno_id
        }
        novo_id = str(int(novo_id) + 1)
    _salvar_turma_alunos(turmas_alunos)

turma_id = "1"

def gravar_banco(turma_id, alunos):
    bancoAlunos = listar_alunos()
    novo_id = _obter_novo_id(alunos)
    novos_alunos = {}
    leitor_csv = ler_csv()

    for aluno in leitor_csv:
        novos_alunos[novo_id] = {
            "nome": aluno["Nome completo do aluno"],
            "data_nascimento": aluno["Data de Nascimento"],
            "genero": aluno["Genêro"],
            "RA": novo_id
        }
        
        novo_id = str(int(novo_id) + 1)
    criar_relacao_turma_aluno(turma_id, novos_alunos)
    print(novos_alunos)
    for aluno_id, aluno_info in novos_alunos.items():
        bancoAlunos[aluno_id] = aluno_info
    _salvar_alunos(bancoAlunos)

gravar_banco(turma_id, listar_alunos())
print("Importação concluída com sucesso.")