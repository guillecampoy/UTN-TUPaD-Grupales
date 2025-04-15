import unittest
from src.validaciones import validar_decimal

class TestValidarDecimal(unittest.TestCase):

    def test_numero_valido(self):
        self.assertEqual(validar_decimal("42"), 42)

    def test_numero_con_espacios(self):
        self.assertEqual(validar_decimal("   123   "), 123)

    def test_valor_vacio(self):
        with self.assertRaises(ValueError):
            validar_decimal("")

    def test_valor_con_letras(self):
        with self.assertRaises(ValueError):
            validar_decimal("12abc")

    def test_valor_con_simbolos(self):
        with self.assertRaises(ValueError):
            validar_decimal("@42!")

    def test_numero_negativo(self):
        with self.assertRaises(ValueError):
            validar_decimal("-5")

    def test_numero_con_ceros_a_izquierda(self):
        with self.assertRaises(ValueError):
            validar_decimal("00025")

if __name__ == '__main__':
    unittest.main()
