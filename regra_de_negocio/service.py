import regra_de_negocio.gerenciador_turmas as gerenciador_turmas
import regra_de_negocio.global_settings as global_settings
import regra_de_negocio.gerenciador_ciclos as gerenciador_ciclos
import regra_de_negocio.gerenciador_turmas_alunos as gerenciador_turmas_alunos
import regra_de_negocio.gerenciador_notas as gerenciador_notas
import regra_de_negocio.gerenciador_importacao_alunos as gerenciador_importacao_alunos


def busca_turmas():  # retorna todas turmas
    turmas_data = gerenciador_turmas.busca_turmas()
    return turmas_data


def cria_turma(dados_nova_turma):
    resposta = gerenciador_turmas.criacao_turma(dados_nova_turma)
    info_global_settings = global_settings.read_global_settings()
    id_nova_turma_str = str(resposta["id_nova_turma"])
    # cria ciclos para a turma
    gerenciador_ciclos.cria_ciclos_pra_turma(id_nova_turma_str, info_global_settings)
    # cria notas para o aluno
    ciclos = gerenciador_ciclos.listar_ciclos_por_id_turma(id_nova_turma_str)
    alunos = gerenciador_turmas_alunos.listar_alunos_turma(id_nova_turma_str)
    gerenciador_notas.adicionar_notas_aluno_turma(ciclos, alunos, id_nova_turma_str)
    return resposta

def importa_aluno_svc(requisicao, alunos_importados):
    """
    Formato da requisição JSON esperado:
        "turma_id": "1",
        "nome_Turma": "Logica ok!",
        "alunos_importados": 
        [{"Nome completo do aluno":"valor","Genêro":"valor","Data":"valor"},
        {"Nome completo do aluno":"valor","Genêro":"valor","Data":"valor"}]
    """
    turma_id = requisicao.get("turma_id")
    nome_turma = requisicao.get("nome_Turma")
    alunos = gerenciador_turmas_alunos.listar_alunos_turma(turma_id)
    turma_alunos = gerenciador_turmas_alunos.listar_turmas_alunos()
    novos_alunos = gerenciador_importacao_alunos.gravar_alunos_banco(alunos, alunos_importados)
    gerenciador_importacao_alunos.criar_relacao_turma_aluno(turma_id, novos_alunos, turma_alunos)
    ciclos = gerenciador_ciclos.listar_ciclos_por_id_turma(turma_id)
    alunos = gerenciador_turmas_alunos.listar_alunos_turma(turma_id)
    gerenciador_notas.adicionar_notas_aluno_turma(ciclos, novos_alunos, turma_id)
    resposta = f"Alunos adicionados a turma {nome_turma}"
    return resposta
    

