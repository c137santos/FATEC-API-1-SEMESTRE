import unittest
import regra_de_negocio.gerenciador_turmas as gt

import sys

sys.path.append(".")


class TesteGerenciadorTurmas(unittest.TestCase):
    def teste_salvar_turmas(self):
        turmas = {
            "1": {
                "nome": "turma1",
                "professor": "Nadalete",
                "data_de_inicio": "21/02/2023",
            },
            "2": {
                "nome": "Turma da manhã",
                "professor": "Gorete",
                "data_de_inicio": "21/02/2023",
            },
        }
        obtido = gt._salvar_turmas(turmas)
        esperado = True
        self.assertEqual(
            esperado, obtido, "verifica se a inserção ou remoção foram salvos"
        )

    def teste_editar_turma_existente(self):
        esperado = True
        obtido = gt.editar_turma("1", "turma7", "Nadaleta", "21/03/2023")
        self.assertEqual(esperado, obtido, "verificar se as alterações foram salvas")

    def teste_editar_turma_nao_existente(self):
        esperado = False
        obtido = gt.editar_turma("2", "turma7", "Nadaleta", "21/03/2023")
        self.assertEqual(esperado, obtido, "verificar se as alterações foram salvas")


if __name__ == "__main__":
    unittest.main()
