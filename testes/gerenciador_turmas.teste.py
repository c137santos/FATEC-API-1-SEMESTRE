import unittest

import sys
sys.path.append('.')
import regra_de_negocio.gerenciador_turmas as gt

class TesteGerenciadorTurmas(unittest.TestCase):
    def teste_obter_todos_grupos(self):
        esperado =  {
                        "1": {
                            "nome": "turma1",
                            "professor": "Nadalete",
                            "data_de_inicio":"21/02/2023"
                        },
                        "2": {
                            "nome": "Turma da manhã",
                            "professor": "Gorete",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        turmas = gt.obter_todas_turmas()
        self.assertEqual(esperado, turmas, "verifica a leitura e desserialização do arquivo turmas.json")

    def teste_obter_ultimo_id(self):
        semente =  {
                        "1": {
                            "nome": "turma1",
                            "professor": "Nadalete",
                            "data_de_inicio":"21/02/2023"
                        },
                        "2": {
                            "nome": "Turma da manhã",
                            "professor": "Gorete",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        gt.salvar_turmas(semente)
        esperado = "2"
        ultimoid = gt.obter_ultimo_id()
        self.assertEqual(esperado, ultimoid, "verificao o último id do arquivo turmas.json")
    
    def teste_obter_novo_id(self):
        semente =  {
                        "1": {
                            "nome": "turma1",
                            "professor": "Nadalete",
                            "data_de_inicio":"21/02/2023"
                        },
                        "2": {
                            "nome": "Turma da manhã",
                            "professor": "Gorete",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        gt.salvar_turmas(semente)
        esperado = "3"
        novoid = gt.obter_novo_id()
        self.assertEqual(esperado, novoid, "verifica a inserção de um novo id no arquivo turmas.json") 
    
    def teste_salvar_turmas(self):
        esperado =  {
                        "1": {
                            "nome": "turma1",
                            "professor": "Nadalete",
                            "data_de_inicio":"21/02/2023"
                        },
                        "2": {
                            "nome": "Turma da manhã",
                            "professor": "Gorete",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        gt.salvar_turmas(esperado)
        obtido = gt.obter_todas_turmas()
        self.assertEqual(esperado, obtido, "verifica se a inserção ou remoção foram salvos")

    def teste_remover_turma(self):
        semente =  {
                        "1": {
                            "nome": "turma1",
                            "professor": "Nadalete",
                            "data_de_inicio":"21/02/2023"
                        },
                        "2": {
                            "nome": "Turma da manhã",
                            "professor": "Gorete",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        gt.salvar_turmas(semente)
        gt.remover_turma("2")
        esperado = {
                        "1": {
                            "nome": "turma1",
                            "professor": "Nadalete",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        obtido = gt.obter_todas_turmas()
        self.assertEqual(esperado, obtido, "verifica se a remoção ocorreu")
    
    def teste_inserir_turma(self):
        semente =  {
                        "1": {
                            "nome": "turma1",
                            "professor": "Nadalete",
                            "data_de_inicio":"21/02/2023"
                        },
                        "2": {
                            "nome": "Turma da manhã",
                            "professor": "Gorete",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        gt.salvar_turmas(semente)
        gt.inserir_turma("Turma da noite", "Sabha", "21/02/2023")
        esperado = {
                        "1": {
                            "nome": "turma1",
                            "professor": "Nadalete",
                            "data_de_inicio":"21/02/2023"
                        },
                        "2": {
                            "nome": "Turma da manhã",
                            "professor": "Gorete",
                            "data_de_inicio":"21/02/2023"
                        },
                        "3": {
                            "nome": "Turma da noite",
                            "professor": "Sabha",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        obtido = gt.obter_todas_turmas()
        self.assertEqual(esperado, obtido, "verifica se a inserção ocorreu")
    
    def teste_editar_turmas(self):
        semente =  {
                        "1": {
                            "nome": "turma1",
                            "professor": "Nadalete",
                            "data_de_inicio":"21/02/2023"
                        },
                        "2": {
                            "nome": "Turma da manhã",
                            "professor": "Gorete",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        gt.salvar_turmas(semente)
        esperado = {
                        "1": {
                            "nome": "turma7",
                            "professor": "Nadaleta",
                            "data_de_inicio":"21/03/2023"
                        },
                        "2": {
                            "nome": "Turma da manhã",
                            "professor": "Gorete",
                            "data_de_inicio":"21/02/2023"
                        }
                    }
        gt.editar_turmas("1", "turma7", "Nadaleta", "21/03/2023")
        obtido = gt.obter_todas_turmas()
        self.assertEqual(esperado, obtido, "verificar se as alterações foram salvas")

if __name__ == '__main__':
    unittest.main()