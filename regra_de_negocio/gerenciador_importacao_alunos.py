import json
import re


def valida_nome(nome):
    if not nome.strip():
        raise ValueError("Nome do aluno não pode estar vazio.")
    if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome):
        raise ValueError(f"Apenas letras no nome: {nome.title()}")


def valida_genero(nome, genero):
    if not genero.strip():
        raise ValueError(f"Gênero do aluno {nome.title()} não pode estar vazio.")
    generos_validos = [
        "Homem cis",
        "Mulher cis",
        "Homem trans",
        "Mulher trans",
        "Gênero neutro",
        "Não binário",
    ]
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", genero):
        raise ValueError(f"Apenas letras no gênero: {genero}")
    if genero not in generos_validos:
        raise ValueError(f"Aluno {nome.title()} está com gênero inválido: {genero}")


def valida_data(nome, data):
    if not data.strip():
        raise ValueError(f"Data de nascimento do aluno {nome.title()} não pode estar vazia.")
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
        raise ValueError(f"Aluno {nome.title()} está com a data inválida: {data}")


def verifica_importacao(arquivoImportadoJson):
    importado_json = json.loads(arquivoImportadoJson)
    """
    Modelo esperado:
    [{"Nome Completo do Aluno":"valor","Gênero":"valor","Data de Nascimento":"valor"},
    {"Nome Completo do Aluno":"valor","Gênero":"valor","Data de Nascimento":"valor"}]
    """
    erros = []
    cabecalhos_esperados = ["Nome Completo do Aluno", "Gênero", "Data de Nascimento"]

    if not importado_json:
        return {"sucesso": False, "erros": ["O CSV está vazio."]}

    # Obtendo os cabeçalhos do primeiro aluno
    cabecalhos_obtidos = list(importado_json[0].keys())
    print("Cabeçalhos obtidos:", cabecalhos_obtidos)

    if cabecalhos_obtidos != cabecalhos_esperados:
        return {
            "sucesso": False,
            "erros": [
                f"Cabeçalhos esperados: {cabecalhos_esperados}. Cabeçalhos obtidos: {cabecalhos_obtidos}"
            ],
        }

    for aluno in importado_json:
        try:
            valida_nome(aluno["Nome Completo do Aluno"])
        except ValueError as e:
            erros.append(str(e))

        try:
            valida_genero(aluno["Nome Completo do Aluno"], aluno["Gênero"])
        except ValueError as e:
            erros.append(str(e))

        try:
            valida_data(aluno["Nome Completo do Aluno"], aluno["Data de Nascimento"])
        except ValueError as e:
            erros.append(str(e))

    if erros:
        return {"sucesso": False, "erros": erros}
    else:
        print("JSON verificado com sucesso!")
        return {"sucesso": True}


def _obter_novo_id(entidade):
    ids_numericos = [0]
    for id_str in entidade.keys():
        id_int = int(id_str)
        ids_numericos.append(id_int)
    ids_numericos.sort()
    id_max_int = ids_numericos.pop()
    novo_id = str(id_max_int + 1)
    return novo_id


def gravar_alunos_banco(alunos, alunos_importados):
    novo_id = _obter_novo_id(alunos)
    novos_alunos = {}
    for aluno in alunos_importados:
        novos_alunos[novo_id] = {
            "nome": aluno["Nome Completo do Aluno"].title(),
            "genero": aluno["Gênero"],
            "data_nascimento": aluno["Data de Nascimento"],
            "RA": novo_id,
        }

        novo_id = str(int(novo_id) + 1)
    for aluno_id, aluno_info in novos_alunos.items():
        alunos[aluno_id] = aluno_info
    _salvar_alunos(alunos)
    return novos_alunos


def _salvar_alunos(alunos):
    dados = json.dumps(alunos, indent=4, ensure_ascii=False)
    with open("dados/alunos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
    return True


def _salvar_turma_alunos(turmas_alunos):
    dados = json.dumps(turmas_alunos, indent=4)
    with open("dados/turmas_alunos.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(dados)
    return True


def criar_relacao_turma_aluno(turma_id, novos_alunos, turmas_alunos):
    novo_id = _obter_novo_id(turmas_alunos)
    for aluno_id in novos_alunos.keys():
        turmas_alunos[novo_id] = {
            "id_turma": turma_id,
            "id_aluno": aluno_id,
            "fee": 0.0
        }
        novo_id = str(int(novo_id) + 1)
    _salvar_turma_alunos(turmas_alunos)

