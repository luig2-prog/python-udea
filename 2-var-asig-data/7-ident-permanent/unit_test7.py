import unittest

from main import six, is_compare1, is_compare2, list1, list2, list3, numbers, three

class OperatorsIdentityAndPertenence(unittest.TestCase):
    def test_validate_initial_values(self):
        self.assertIsInstance(list1, list)
        self.assertEqual(list1, [1, 2, 3])
        self.assertIsInstance(list2, list)
        self.assertEqual(list1, [1, 2, 3])
        self.assertIsInstance(list3, list)
        self.assertEqual(list1, [1, 2, 3])

    def test_validate_reference_list1_list3(self):
        self.assertEqual(list1, list3)
        
    def test_validate_identity(self):
        # list1 y list3 deben ser el mismo objeto (misma referencia)
        self.assertTrue(list1 is list3)
        self.assertEqual(is_compare2, True)
        
        # list1 y list2 deben ser objetos diferentes aunque tengan el mismo valor
        self.assertFalse(list1 is list2)
        self.assertEqual(is_compare1, False)
        
    def test_validate_membership(self):
        # Validar que 3 está en la lista numbers
        self.assertTrue(3 in numbers)
        self.assertEqual(three, True)
        
        # Validar que 6 no está en la lista numbers
        self.assertFalse(6 in numbers)
        self.assertEqual(six, False)