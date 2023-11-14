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