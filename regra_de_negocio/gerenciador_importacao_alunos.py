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