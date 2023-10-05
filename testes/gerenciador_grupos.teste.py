import unittest

import sys
sys.path.append('.')
import regra_de_negocio.gerenciador_grupos as gt

class TesteGerenciadorGrupos(unittest.TestCase):
    def teste_obter_todos_grupos(self):
        esperado =  {
                        "1":{
                                "grupo":1
                        },
                        "2":{
                                "grupo":2
                        }
                    }
        erro, grupos = gt.obter_todos_grupos()
        self.assertEqual(esperado, grupos, "verifica a leitura e desserialização do arquivo grupos.json")

    def teste_obter_ultimo_id(self):
        semente =  {
                        "1":{
                                "grupo":1
                        },
                        "2":{
                                "grupo":2
                        }
                    }
        gt.salvar_grupos(semente)
        esperado = "2"
        ultimoid = gt.obter_ultimo_id()
        self.assertEqual(esperado, ultimoid, "verificao o último id do arquivo grupos.json")
    
    def teste_obter_novo_id(self):
        semente =  {
                        "1":{
                                "grupo":1
                        },
                        "2":{
                                "grupo":2
                        }
                    }
        gt.salvar_grupos(semente)
        esperado = "3"
        novoid = gt.obter_novo_id()
        self.assertEqual(esperado, novoid, "verifica a inserção de um novo id no arquivo grupos.json") 
    
    def teste_salvar_grupos(self):
        esperado =  {
                        "1":{
                                "grupo":1
                        },
                        "2":{
                                "grupo":2
                        }
                    }
        gt.salvar_grupos(esperado)
        erro, obtido = gt.obter_todos_grupos()
        self.assertEqual(esperado, obtido, "verifica se a inserção ou remoção foram salvos")

    def teste_remover_grupo(self):
        semente =  {
                        "1":{
                                "grupo":1
                        },
                        "2":{
                                "grupo":2
                        }
                    }
        gt.salvar_grupos(semente)
        gt.remover_grupo("2")
        esperado = {
                        "1":{
                                "grupo":1
                        }
                    }
        erro, obtido = gt.obter_todos_grupos()
        self.assertEqual(esperado, obtido, "verifica se a remoção ocorreu")
    
    def teste_inserir_grupo(self):
        semente = {
                       "1":{
                               "grupo":1
                       },
                       "2":{
                               "grupo":2
                       }
                  }
        gt.salvar_grupos(semente)
        gt.inserir_grupo("bee", 3)
        esperado = {
                        "1":{
                                "grupo":1
                        },
                        "2":{
                                "grupo":2
                        },
                        "3":{
                                "grupo":"bee"
                        }
                    }
        erro, obtido = gt.obter_todos_grupos()
        self.assertEqual(esperado, obtido, "verifica se a inserção ocorreu")
    
    def teste_editar_grupos(self):
        semente =  {
                        "1":{
                                "grupo":"bee"
                        },
                        "2":{
                                "grupo":"abelha"
                        }
                    }
        gt.salvar_grupos(semente)
        esperado = {
                        "1":{
                                "grupo":"bee"
                        },
                        "2":{
                                "grupo":"cat"
                        }
                    }
        gt.editar_grupos("2", "cat")
        erro, obtido = gt.obter_todos_grupos()
        self.assertEqual(esperado, obtido, "verificar se as alterações foram salvas")

if __name__ == '__main__':
    unittest.main()