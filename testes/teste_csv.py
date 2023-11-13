import csv
import json
import re
import os
   
def ler_csv(endereco_arquivo):
    with open(endereco_arquivo, newline='', encoding='utf-8-sig') as arquivo_csv:
        importado_csv = csv.DictReader(arquivo_csv, delimiter=';')
        importado_csv_lista = list(importado_csv)
        return importado_csv_lista, importado_csv
    
def valida_nome(nome):
    if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome):
        raise ValueError(f"Apenas letras no nome: {nome.title()}")

def valida_genero(nome, genero):
    generos_validos = [
        "Homem cis",
        "Mulher Cis",
        "Homem trans",
        "Mulher Trans",
        "Gênero neutro",
        "Não-binário",
    ]
    if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', genero):
        raise ValueError(f"Apenas letras no gênero: {genero}")
    if genero not in generos_validos:
            raise ValueError(f"Aluno {nome.title()} está com gênero inválido: {genero}")

def valida_data(nome, data):
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
        raise ValueError(f"Aluno {nome.title()} está com a data inválida: {data}")

def verifica_csv(importado_csv, importado_csv_lista):
    erros = []
    cabecalhos_esperados = ["Nome completo do aluno", "Genêro", "Data de Nascimento"]
    cabecalhos_obtidos = importado_csv.fieldnames
    print("Cabeçalhos obtidos:", cabecalhos_obtidos)

    if cabecalhos_obtidos != cabecalhos_esperados:
        for i, cabecalho_esperado in enumerate(cabecalhos_esperados):
            if len(cabecalhos_esperados) == len(cabecalhos_obtidos) :
                cabecalho_obtido = cabecalhos_obtidos[i]
                if cabecalho_esperado != cabecalho_obtido:
                    erros.append(f"Cabeçalho esperado: {cabecalho_esperado}, obtido: {cabecalho_obtido}")
                    cabecalhos_esperados[i] = cabecalhos_obtidos[i]
                    """Troca o cabeçalho esperado para testar as informacoes dos aluno"""
            else:
                erros.append(f"Cabeçalhos esperados: {cabecalhos_esperados}. Cabeçalhos lidos: {cabecalhos_obtidos}")
                return {"sucesso": False, "erros": erros}
    
    for aluno in importado_csv_lista:
        try:
            valida_nome(aluno[cabecalhos_esperados[0]])
        except ValueError as e:
            erros.append(str(e))

        try:
            valida_genero(aluno[cabecalhos_esperados[0]], aluno[cabecalhos_esperados[1]])
        except ValueError as e:
            erros.append(str(e))

        try:
            valida_data(aluno[cabecalhos_esperados[0]], aluno[cabecalhos_esperados[2]])
        except ValueError as e:
            erros.append(str(e))

    if erros:
        return {"sucesso": False, "erros": erros}
    else:
        print("CSV verificado com sucesso!")
        return {"sucesso": True}


def listar_alunos():
    with open("testes/alunos.json", "r", encoding="utf-8") as f:
        alunos = json.load(f)
        return alunos
    
def listar_turma_aluno():
    with open("testes/turmas_alunos.json", "r", encoding="utf-8") as f:
        turmas_alunos = json.load(f)
        return turmas_alunos

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
    
def gravar_banco(alunos, importado_csv_lista):
    novo_id = _obter_novo_id(alunos)
    novos_alunos = {}

    for aluno in importado_csv_lista:
        novos_alunos[novo_id] = {
            "nome": aluno["Nome completo do aluno"],
            "genero": aluno["Genêro"],
            "data_nascimento": aluno["Data de Nascimento"],
            "RA": novo_id
        }
        
        novo_id = str(int(novo_id) + 1)
    print(novos_alunos)
    for aluno_id, aluno_info in novos_alunos.items():
        alunos[aluno_id] = aluno_info
    return novos_alunos
    

def criar_relacao_turma_aluno(turma_id, novos_alunos):
    turmas_alunos = listar_turma_aluno()
    novo_id =_obter_novo_id(turmas_alunos)
    for aluno_id in novos_alunos.keys():
        turmas_alunos[novo_id] = {
            "id_turma": turma_id,
            "id_aluno": aluno_id
        }
        novo_id = str(int(novo_id) + 1)

def deletar_arquivo_importado(endereco_arquivo):
    os.remove(endereco_arquivo)


def realizar_importacao():
    endereco_arquivo = "importacao/novos_alunos.csv"
    importado_csv_lista, importado_csv = ler_csv(endereco_arquivo)
    resultado_verificacao = verifica_csv(importado_csv, importado_csv_lista)
    if not resultado_verificacao["sucesso"]:
        print(resultado_verificacao["erros"])
        return resultado_verificacao["erros"]
    else:
        turma_id = "1"
        alunos = listar_alunos()
        turma_alunos = listar_turma_aluno()
        novos_alunos = gravar_banco(alunos, importado_csv_lista)
        criar_relacao_turma_aluno(turma_id, novos_alunos)
        _salvar_alunos(alunos)
        _salvar_turma_alunos(turma_alunos)
        deletar_arquivo_importado(endereco_arquivo)
        print("CSV verificado com sucesso!")
        print(novos_alunos)
        return novos_alunos
    
realizar_importacao()
