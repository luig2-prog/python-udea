import unittest
from main import (
    texto,
    numero_entero,
    numero_decimal,
    valor_booleano,
    lista,
    diccionario,
    tupla,
    conjunto,
    valor_nulo
)

class TestDataTypes(unittest.TestCase):
    def test_texto(self):
        self.assertIsInstance(texto, str)
        self.assertEqual(texto, "Programando en Python")

    def test_numero_entero(self):
        self.assertIsInstance(numero_entero, int)
        self.assertEqual(numero_entero, 123)

    def test_numero_decimal(self):
        self.assertIsInstance(numero_decimal, float)
        self.assertAlmostEqual(numero_decimal, 3.14159)

    def test_valor_booleano(self):
        self.assertIsInstance(valor_booleano, bool)
        self.assertTrue(valor_booleano)

    def test_lista(self):
        self.assertIsInstance(lista, list)
        self.assertEqual(len(lista), 4)
        self.assertEqual(lista[0], 1)
        self.assertEqual(lista[-1], "cuatro")

    def test_diccionario(self):
        self.assertIsInstance(diccionario, dict)
        self.assertEqual(diccionario["clave"], "valor")
        self.assertEqual(diccionario["otro"], 5)

    def test_tupla(self):
        self.assertIsInstance(tupla, tuple)
        self.assertEqual(len(tupla), 3)
        self.assertEqual(tupla[0], 10)
        self.assertEqual(tupla[-1], 30)

    def test_conjunto(self):
        self.assertIsInstance(conjunto, set)
        self.assertEqual(len(conjunto), 3)  # El 3 duplicado se elimina
        self.assertTrue(1 in conjunto)
        self.assertTrue(2 in conjunto)
        self.assertTrue(3 in conjunto)

    def test_valor_nulo(self):
        self.assertIsNone(valor_nulo)

if __name__ == '__main__':
    unittest.main() 