import json
import re

def teste(requisicao, alunos_importados):
    turma_id = requisicao.get("turma_id")
    nome_turma = requisicao.get("nome_Turma")

    print(alunos_importados)

    # Iterar sobre os alunos e acessar os valores
    for aluno in alunos_importados:
        nome_completo = aluno['Nome completo do aluno']
        genero = aluno['Genêro']
        data_nascimento = aluno['Data de Nascimento']

        # Faça o que quiser com os valores, por exemplo, imprimir
        print(f"turma ID: {turma_id}, nome_turma: {nome_turma}, Nome: {nome_completo}, Gênero: {genero}, Data de Nascimento: {data_nascimento}")

def valida_nome(nome):
    if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome):
        raise ValueError(f"Apenas letras no nome: {nome.title()}")

def valida_genero(nome, genero):
    generos_validos = [
        "Homem cis",
        "Mulher cis",
        "Homem trans",
        "Mulher trans",
        "Gênero neutro",
        "Não binário",
    ]
    if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', genero):
        raise ValueError(f"Apenas letras no gênero: {genero}")
    if genero not in generos_validos:
            raise ValueError(f"Aluno {nome.title()} está com gênero inválido: {genero}")

def valida_data(nome, data):
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
        raise ValueError(f"Aluno {nome.title()} está com a data inválida: {data}")

def verifica_importacao(arquivoImportadoJson):
    erros = []
    cabecalhos_esperados = ["Nome completo do aluno", "Genêro", "Data de Nascimento"]

    # Convertendo a string JSON para um objeto Python
    try:
        importado_json = json.loads(arquivoImportadoJson)
    except json.JSONDecodeError:
        return {"sucesso": False, "erros": ["Erro ao decodificar JSON."]}

    if not isinstance(importado_json, list):
        return {"sucesso": False, "erros": ["O JSON deve representar uma lista de alunos."]}

    if not importado_json:
        return {"sucesso": False, "erros": ["O JSON está vazio."]}

    # Obtendo os cabeçalhos do primeiro aluno (assumindo que todos têm a mesma estrutura)
    cabecalhos_obtidos = list(importado_json[0].keys())
    print("Cabeçalhos obtidos:", cabecalhos_obtidos)

    if cabecalhos_obtidos != cabecalhos_esperados:
        return {"sucesso": False, "erros": [f"Cabeçalhos esperados: {cabecalhos_esperados}. Cabeçalhos obtidos: {cabecalhos_obtidos}"]}

    for aluno in importado_json:
        try:
            valida_nome(aluno["Nome completo do aluno"])
        except ValueError as e:
            erros.append(str(e))

        try:
            valida_genero(aluno["Nome completo do aluno"], aluno["Genêro"])
        except ValueError as e:
            erros.append(str(e))

        try:
            valida_data(aluno["Nome completo do aluno"], aluno["Data de Nascimento"])
        except ValueError as e:
            erros.append(str(e))

    if erros:
        return {"sucesso": False, "erros": erros}
    else:
        print("JSON verificado com sucesso!")
        return {"sucesso": True}