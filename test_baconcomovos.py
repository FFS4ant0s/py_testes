"""
TDD - test driven development (Desenvolvimento dirigido a teste

Red
Parte 1 -> Criar o teste e ver falhar 

Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar meu código
"""
import unittest
from baconcomovos import bacon_com_ovos

class TestBancoComOvos(unittest.TestCase):
    def test_bancon_com_ovos_error_se_nao_for_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"'
                     )

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"'
                     )
                
    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 15, 18, 21)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"'
                     )


unittest.main(verbosity=2)