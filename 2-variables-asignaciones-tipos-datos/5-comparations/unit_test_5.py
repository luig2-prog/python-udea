import io
import unittest
from unittest.mock import patch
from main import is_minor, can_vote, permitted_age, user_age


class ComparationTest(unittest.TestCase):
    def test_validate_initial_values(self):
        """Validams los valores iniciales"""
        self.assertEqual(permitted_age, 18)
        self.assertEqual(user_age, 20)

    def test_user_age_comparate_permitted_age(self):
        """Validamos que user_age sea mayor o igual a permitted_age"""
        self.assertGreaterEqual(user_age, permitted_age, "Es mayor")

    def test_user_can_vote(self):
        """Validar que el usuari pueda vota"""
        self.assertTrue(can_vote, "Puede votar!")

    def test_user_is_minot(self):
        """Validar que el usuario sea menor"""
        self.assertLess(is_minor, permitted_age, "El usuario es menos")

    def test_print_can_vote(self):
        """Validar que se imprima el valor de si puede votar"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            print(can_vote)
            self.assertEqual(fake_output.getvalue().strip(), 'True')


if __name__ == '__main__':
    unittest.main()