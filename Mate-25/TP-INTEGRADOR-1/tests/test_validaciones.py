import unittest
from src.validaciones import validar_binario, validar_decimal

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




class TestValidarBinario(unittest.TestCase):

    def test_valido_sin_ceros_a_la_izquierda(self):
        self.assertEqual(validar_binario("1010"), 10)
        self.assertEqual(validar_binario("1"), 1)
        self.assertEqual(validar_binario("0"), 0)

    def test_valido_con_espacios(self):
        self.assertEqual(validar_binario("  1011  "), 11)

    def test_vacio(self):
        with self.assertRaises(ValueError) as e:
            validar_binario("")
        self.assertEqual(str(e.exception), "No se ingresó ningún valor")

    def test_no_binario(self):
        with self.assertRaises(ValueError) as e:
            validar_binario("1021")
        self.assertEqual(str(e.exception), "Debe ser un número binario")

        with self.assertRaises(ValueError):
            validar_binario("abc")

    def test_ceros_a_la_izquierda(self):
        with self.assertRaises(ValueError) as e:
            validar_binario("00101")
        self.assertEqual(str(e.exception), "El número no debe tener ceros a la izquierda")

    def test_cero_valido(self):
        self.assertEqual(validar_binario("0"), 0)  # Cero sí puede tener ceros a la izquierda

    def test_solo_espacios(self):
        with self.assertRaises(ValueError) as e:
            validar_binario("   ")
        self.assertEqual(str(e.exception), "No se ingresó ningún valor")


if __name__ == "__main__":
    unittest.main()