# Teste das funções criadas

## Gerenciador de notas

[  ] def calcular_fee(id_aluno, id_turma)

[  ] def listar_notas()

[  ] def listar_notas_por_id_turma(notas, id_turma)

[  ] def listar_notas_por_id_aluno(notas, id_aluno)

[  ] def listar_notas_por_id_ciclo(notas, id_ciclo)

[  ] def listar_notas_por_id_turma_id_aluno(id_turma, id_aluno)

[  ] def adicionar_nota(nova_nota)

[  ] def editar_nota(id_nota_atualizada, nota_atualizada)

[  ] def remover_nota(id_nota)

[  ] def verificar_existencia_nota_por_ciclo(nota)

[  ] def _obter_novo_id_nota()

[  ] def _salvar_notas(ciclos)

[  ] def verificar_edicao_habilitada(notas, id_nota)

[  ] def _obter_prazo_insercao_nota(ciclo, id_turma)

## Gerenciador de ciclos

[  ] def listar_ciclos()

[  ] def listar_ciclos_por_id_turma(id_turma)

[  ] def obter_ciclo(id_ciclo)

[  ] def adicionar_ciclo(ciclo)

[  ] def _obter_novo_id_ciclo()

[  ] def _salvar_ciclos(ciclos)

## Gerenciador de turmas

[  ] def busca_turmas()

[  ] def editar_turma_svc(id, nome, professor, data_de_inicio, duracao_ciclo)

[  ] def criacao_turma(dados_nova_turma)

[  ] def excluir_turma_svc(id)

[  ] def _salvar_turmas(turmas)

[  ] def _obter_novo_id_turma()

## Rotas

[  ] /api/v1/alunos/atualizar/:id

[  ] /api/v1/turmas/listar

[  ] /api/v1/turmas/listar/:id

[  ] /api/v1/turmas/editar/:id

[  ] /api/v1/turmas/criar

[  ] /api/v1/turmas/excluir/:id

[  ] /api/v1/ciclos/listar

[  ] /api/v1/ciclos/listar/:id_turma

[  ] /api/v1/ciclos/criar

[  ] /api/v1/notas/listar

[  ] /api/v1/notas/listar/:id_turma/:id_aluno

[  ] /api/v1/notas/turma/listar/:id

[  ] /api/v1/notas/aluno/listar/:id

[  ] /api/v1/notas/criar

[  ] /api/v1/notas/editar/:id

[  ] /api/v1/notas/excluir/:id