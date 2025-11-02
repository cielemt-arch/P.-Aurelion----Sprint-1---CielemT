import unittest
from unittest.mock import patch
import sys
import os
import pandas as pd

# Asegurar que el path del proyecto esté en sys.path para importar aurelion
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import aurelion


class TestMainIntegration(unittest.TestCase):

    def setUp(self):
        # Crear datos simulados mínimos para las funciones que usan DataFrames
        detalle_ventas = pd.DataFrame({'importe': [100.0, 200.0, 300.0]})
        productos = pd.DataFrame({'categoria': ['Alimentos'] * 83 + ['Limpieza'] * 17})
        clientes = pd.DataFrame({'ciudad': ['Quito', 'Quito', 'Guayaquil']})

        self.datos_sim = {
            'detalle_ventas': detalle_ventas,
            'productos': productos,
            'clientes': clientes,
        }

    def test_main_recorrido_opcion_2_y_salir(self):
        # Simula: 'hola' (no numérico), '' (vacío), '7' (fuera de rango), '2' (válido), '5' (salir)
        entradas = iter(['hola', '', '7', '2', '5'])

        def input_fn(prompt=""):
            try:
                return next(entradas)
            except StopIteration:
                # Si nos quedamos sin entradas, lanzar EOFError similar a input() en stdin cerrado
                raise EOFError()

        # Llamar a main con datos simulados y función de entrada inyectada
        aurelion.main(datos=self.datos_sim, input_fn=input_fn)


if __name__ == '__main__':
    unittest.main()
