import unittest
from src.convertidor import decimal_binario

class TestDecimalBinario(unittest.TestCase):
    def test_decimal_valido(self):
        self.assertEqual(decimal_binario("10"), "1010")
        self.assertEqual(decimal_binario("0"), "0")
        self.assertEqual(decimal_binario("255"), "11111111")

    def test_decimal_negativo(self):
        with self.assertRaises(ValueError):
            decimal_binario("-10")

if __name__ == "__main__":
    unittest.main()