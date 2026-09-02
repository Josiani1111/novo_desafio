import unittest

from unittest.mock import patch

from src.utils import ler_idade, ler_id, ler_nome, ler_cidade


class TestUtils(unittest.TestCase):

    @patch("builtins.input", return_value="30")
    def test_ler_idade(self, input_mock):
        resultado = ler_idade()
        self.assertEqual(resultado, 30)

    @patch("builtins.input", return_value="10")
    def test_ler_id(self, input_mock):
        resultado = ler_id()
        self.assertEqual(resultado, 10)

    @patch("builtins.input", return_value="josiani")
    def test_ler_nome(self, input_mock):
        resultado = ler_nome()
        self.assertEqual(resultado, "Josiani")

    @patch("builtins.input", return_value="ribeirao preto")
    def test_ler_cidade(self, input_mock):
        resultado = ler_cidade()
        self.assertEqual(resultado, "Ribeirao Preto")

    @patch("builtins.input", side_effect=["-5", "30"])
    def test_ler_idade_invalida(self, input_mock):
        resultado = ler_idade()
        self.assertEqual(resultado, 30)

    @patch("builtins.input", side_effect=["0", "10"])
    def test_ler_id_invalido(self, input_mock):
        resultado = ler_id()
        self.assertEqual(resultado, 10)

    @patch("builtins.input", side_effect=["", "josiani"])
    def test_ler_nome_vazio(self, input_mock):
        resultado = ler_nome()
        self.assertEqual(resultado, "Josiani")

    @patch("builtins.input", side_effect=["", "ribeirao preto"])
    def test_ler_cidade_vazia(self, input_mock):
        resultado = ler_cidade()
        self.assertEqual(resultado, "Ribeirao Preto")


if __name__ == "__main__":
    unittest.main()