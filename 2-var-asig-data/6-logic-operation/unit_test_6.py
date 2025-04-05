import io
import unittest
from unittest.mock import patch
from main_6 import not_knows_how_to_drive, can_enter_event, can_to_drive, has_license, has_regular, has_vip, knows_how_to_drive

class LogicOperationTest(unittest.TestCase):
    """Validamos los valores iniciales"""
    def test_initial_values(self):
        self.assertIsInstance(has_license, bool)
        self.assertEqual(has_license, True)
        self.assertIsInstance(knows_how_to_drive, bool)
        self.assertIsInstance(has_vip, bool)
        self.assertEqual(has_vip, True)
        self.assertIsInstance(has_regular, bool)
        self.assertEqual(has_regular, False)
        self.assertIsInstance(can_enter_event, bool)
    
    def test_validate_can_to_drive(self):
        """Validar si el usuario puede manejar"""
        self.assertIsInstance(can_to_drive, bool)
        self.assertEqual(can_to_drive, False)

    def test_validate_enter_event(self):
        """Validar que el usuario pueda ingresar al evento"""
        self.assertIsInstance(can_enter_event, bool)
        self.assertEqual(can_enter_event, True)

    def test_validate_not_knows_how_to_drive(self):
        """Validar que el usuario pueda conducir"""
        self.assertIsInstance(not_knows_how_to_drive, bool)
        self.assertEqual(not_knows_how_to_drive, True)

    def test_prints(self):
        """Validar que se impriman los valores"""
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            print(can_to_drive)
            print(can_enter_event)
            print(not_knows_how_to_drive)
            self.assertEqual(fake_output.getvalue().strip(), 'False\nTrue\nTrue')