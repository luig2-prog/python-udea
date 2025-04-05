# Unit testing module, provides us with tools to create unit test
import unittest
from two_class import user_name, user_age, user_height, is_currently_student

# Create a class that heredate from unittest.TestCase
# That class containt all us test methods 
class TestTwoClass(unittest.TestCase):
    def test_user_name(self):
        self.assertIsInstance(user_name, str)
        self.assertTrue(len(user_name) > 0)

    def test_user_age(self):
        self.assertIsInstance(user_age, int)
        self.assertGreaterEqual(user_age, 0)

    def test_user_height(self):
        self.assertIsInstance(user_height, float)
        self.assertGreater(user_height, 0)
        self.assertLess(user_height, 3)  # Valid range for human height in meters

    def test_is_currently_student(self):
        self.assertIsInstance(is_currently_student, bool)

if __name__ == '__main__':
    unittest.main() 