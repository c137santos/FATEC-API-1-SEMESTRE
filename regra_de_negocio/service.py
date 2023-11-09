import gerenciador_turmas as gt
import gerenciador_ciclos
import gerenciador_turmas_alunos
import gerenciador_notas


def busca_turmas():  # retorna todas turmas
    turmas_data = gt.busca_turmas()
    return turmas_data


def cria_turma(dados_nova_turma):
    informacoes_turma = gt.criacao_turma(dados_nova_turma)
    quantidade_ciclos = informacoes_turma["quantidade_ciclos"]
    # cria um ciclo padrão para a quantidade de ciclos desejada
    print("\n> Criando os ciclos associados à turma...\n")
    id_nova_turma = informacoes_turma["id_nova_turma"]
    for i in range(quantidade_ciclos):
        ciclo = {}
        ciclo["id_turma"] = id_nova_turma
        ciclo["duracao"] = 15
        ciclo["peso_nota"] = float(i + 1)
        ciclo["numero_ciclo"] = i + 1
        ciclo["prazo_insercao_nota"] = 5
        gerenciador_ciclos.adicionar_ciclo(ciclo)
    # cria as notas para cada aluno adicionado
    print("> Criando as notas dos alunos...\n")
    id_nova_turma_str = str(id_nova_turma)  # precisa mesmo ser str?
    ciclos = gerenciador_ciclos.listar_ciclos_por_id_turma(id_nova_turma_str)
    alunos = gerenciador_turmas_alunos.listar_alunos_turma(id_nova_turma_str)
    for id_aluno in alunos:
        for id_ciclo in ciclos:
            nova_nota = {}
            nova_nota["id_turma"] = id_nova_turma_str
            nova_nota["id_aluno"] = str(id_aluno)
            nova_nota["id_ciclo"] = str(id_ciclo)
            nova_nota["valor"] = 0.0
            nova_nota["fee"] = False
            gerenciador_notas.adicionar_nota(nova_nota)
    return informacoes_turma
