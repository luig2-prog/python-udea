import unittest
from unittest.mock import patch
import io
from main import starting_price, discount_value, discount_percentage, final_price

class TestPriceCalculation(unittest.TestCase):

    def test_validate_initial_price(self):
        """Validar valores iniciales"""
        self.assertEqual(starting_price, 50)
        self.assertEqual(discount_percentage, 10)

    def test_validate_discount_value(self):
        """Validar el calculo del descuento"""
        self.assertEqual(discount_value, 5)

    def test_validate_final_price(self):
        """Validar precio final"""
        self.assertEqual(final_price, 45)

    def test_print_final_price(self):
        """Validar que se imprima el valor final"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            print(final_price)
            self.assertEqual(fake_output.getvalue().strip(), '45.0')

if __name__ == '__main__':
    unittest.main()