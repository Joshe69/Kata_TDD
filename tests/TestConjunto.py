import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornarNone(self):
        conjunto=Conjunto([])
        self.assertIsNone(conjunto.promedio())