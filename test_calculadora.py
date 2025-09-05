import unittest
from calculadora import somar

class TestCalculadora(unittest.TestCase):
    """
    Suíte de testes para o módulo da calculadora.
    """
    def test_soma_positivos(self):
        """
        Verifica se a função 'somar' opera corretamente com números positivos.
        """
        self.assertEqual(somar(5, 3), 8)
