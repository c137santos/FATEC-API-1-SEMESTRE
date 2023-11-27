import regra_de_negocio.gerenciador_turmas as gerenciador_turmas
import regra_de_negocio.global_settings as global_settings
import regra_de_negocio.gerenciador_ciclos as gerenciador_ciclos
import regra_de_negocio.gerenciador_turmas_alunos as gerenciador_turmas_alunos
import regra_de_negocio.gerenciador_notas as gerenciador_notas
import regra_de_negocio.gerenciador_importacao_alunos as gerenciador_importacao_alunos
import regra_de_negocio.gerenciador_alunos as gerenciador_alunos
import regra_de_negocio.gerenciador_relatorios as gerenciador_relatorios


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
            fee = buscar_fee_do_aluno_na_turma(id_turma=id_turma, id_aluno=id_aluno)
            fee_turma.append(fee)
        if len(fee_turma) == 0:
            turmas[id_turma]["fee"] = 0.0
        else:
            media_fee = sum(fee_turma) / len(fee_turma)
            turmas[id_turma]["fee"] = round(media_fee, 2)
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


def buscar_fee_do_aluno_na_turma(id_turma, id_aluno):
    try:
        turma_aluno = gerenciador_turmas_alunos.busca_determinada_turma_do_aluno(
            id_aluno, id_turma
        )
        return turma_aluno["fee"]
    except Exception as e:
        raise Exception(f"Falha na busca do fee: {str(e)}")


def importa_aluno_svc(requisicao, alunos_importados):
    """
    Formato da requisição JSON esperado:
        "turma_id": "1",
        "nome_Turma": "Logica ok!",
        "alunos_importados":
    [{"Nome Completo do Aluno":"valor","Gênero":"valor","Data de Nascimento":"valor"},
    {"Nome Completo do Aluno":"valor","Gênero":"valor","Data de Nascimento":"valor"}]
    """
    try:
        turma_id = requisicao["turma_id"]
        turma_id_str = str(turma_id)
        nome_turma = requisicao["nome_Turma"]
        alunos = gerenciador_alunos.listar_alunos()
        turma_alunos = gerenciador_turmas_alunos.listar_turmas_alunos()
        novos_alunos = gerenciador_importacao_alunos.gravar_alunos_banco(
            alunos, alunos_importados
        )
        gerenciador_importacao_alunos.criar_relacao_turma_aluno(
            turma_id, novos_alunos, turma_alunos
        )
        ciclos = gerenciador_ciclos.listar_ciclos_por_id_turma(turma_id_str)
        gerenciador_notas.adicionar_notas_aluno_turma(
            ciclos, novos_alunos, turma_id_str
        )
        resposta = f"Alunos adicionados a turma {nome_turma}"
        return resposta
    except Exception as e:
        raise Exception(f"Falha ao adicionar alunos por CSV: {str(e)}")


def exportacao_relatorio_turma_svc(id_turma):
    info_turma = gerenciador_turmas.obter_turma(id_turma)
    alunos_da_turma = gerenciador_turmas_alunos.listar_alunos_turma_relatorio(id_turma)
    info_alunos = {}
    lista_ra = []
    for aluno in alunos_da_turma.values():
        if aluno:
            info_alunos[aluno["RA"]] = aluno
            lista_ra.append(aluno["RA"])
    for ra_aluno in lista_ra:
        nota_do_aluno = gerenciador_notas.listar_notas_por_turma_aluno(
            id_turma=id_turma, id_aluno=ra_aluno
        )
        for nota in nota_do_aluno.values():
            nome_do_ciclo = gerenciador_ciclos.obter_ciclo(nota["id_ciclo"])[
                "nome_ciclo"
            ]
            info_alunos[ra_aluno][nome_do_ciclo] = nota["valor"]

    try:
        array_dados_relatorio = gerenciador_relatorios.cria_relatorio_csv(
            info_turma=info_turma, info_alunos=info_alunos
        )
    except Exception as e:
        return f"Problemas com a geração do relatório da turma {info_turma['nome']}, {str(e)}"
    return array_dados_relatorio
