import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def Test_conjunto_vacio_retornarnone(self):
        conjunto=Conjunto([])
        self.assertIsNone(conjunto.promedio())