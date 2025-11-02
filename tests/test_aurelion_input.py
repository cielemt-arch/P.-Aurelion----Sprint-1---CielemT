import unittest
from unittest.mock import patch

import sys
import os

# Asegurar que el path del proyecto esté en sys.path para importar aurelion
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import aurelion


class TestLeerOpcionMenu(unittest.TestCase):

    def test_inputs_no_numericos_y_valido(self):
        # Simula: 'hola' (no numérico), '' (vacío), '7' (fuera de rango), '2' (válido)
        entradas = ['hola', '', '7', '2']
        with patch('builtins.input', side_effect=entradas):
            resultado = aurelion.leer_opcion_menu()
            self.assertEqual(resultado, 2)

    def test_input_directo_valido(self):
        with patch('builtins.input', return_value='3'):
            resultado = aurelion.leer_opcion_menu()
            self.assertEqual(resultado, 3)

    def test_espacios_alrededor(self):
        with patch('builtins.input', return_value='  4  '):
            resultado = aurelion.leer_opcion_menu()
            self.assertEqual(resultado, 4)


if __name__ == '__main__':
    unittest.main()
