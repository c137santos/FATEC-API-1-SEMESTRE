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

  
def listar_fee_turmas_svc():
    turmas = gerenciador_turmas.busca_turmas()
    for id_turma in turmas.keys():
        alunos = gerenciador_turmas_alunos.listar_alunos_turma(id_turma)
        fee_turma = []
        for id_aluno in alunos.keys():
            fee = gerenciador_notas._calcular_fee_turma_aluno(id_aluno=id_aluno,id_turma=id_turma)
            fee_turma.append(fee)
        if len(fee_turma) == 0:
            turmas[id_turma]['fee'] = 0.0   
        else:
            media_fee = sum(fee_turma) / len(fee_turma)
            turmas[id_turma]['fee'] = round(media_fee, 2)
    return turmas
  

def excluir_turma_svc(id_turma):
    try:
        gerenciador_turmas.excluir_turma(id_turma)
        gerenciador_turmas_alunos.remover_turma_aluno(id_turma)
        gerenciador_ciclos.excluir_ciclo_da_turma(id_turma)
        gerenciador_notas.excluir_notas_relacionadas_turma(id_turma)
        return {"message": f"Turma {id_turma} Excluida"}
    except Exception as e:
        raise Exception(f"Falha na exclusão de turma: {str(e)}")

def importa_aluno_svc(requisicao, alunos_importados):
    """
    Formato da requisição JSON esperado:
        "turma_id": "1",
        "nome_Turma": "Logica ok!",
        "alunos_importados": 
        [{"Nome completo do aluno":"valor","Genêro":"valor","Data":"valor"},
        {"Nome completo do aluno":"valor","Genêro":"valor","Data":"valor"}]
    """
    try:
        turma_id = requisicao["turma_id"]
        nome_turma = requisicao["nome_Turma"]
        alunos = gerenciador_turmas_alunos.listar_alunos_turma(turma_id)
        turma_alunos = gerenciador_turmas_alunos.listar_turmas_alunos()
        novos_alunos = gerenciador_importacao_alunos.gravar_alunos_banco(alunos, alunos_importados)
        gerenciador_importacao_alunos.criar_relacao_turma_aluno(turma_id, novos_alunos, turma_alunos)
        ciclos = gerenciador_ciclos.listar_ciclos_por_id_turma(turma_id)
        alunos = gerenciador_turmas_alunos.listar_alunos_turma(turma_id)
        gerenciador_notas.adicionar_notas_aluno_turma(ciclos, novos_alunos, turma_id)
        resposta = f"Alunos adicionados a turma {nome_turma}"
        return resposta
    except Exception as e:
        raise Exception(f"Falha ao adicionar alunos por CSV: {str(e)}")