import unittest 
from two_class import user_name, user_age, user_height, is_currently_student

# 

class TestTwoClass(unittest.TestCase):
    
    def test_username(self):
        self.assertIsInstance(user_name, str)
        self.assertTrue(len(user_name) > 0)

    def test_userage(self):
        self.assertIsInstance(user_age, int)
        self.assertGreaterEqual(user_age, 0)

    def test_user_height(self):
        self.assertIsInstance(user_height, float)
        self.assertGreater(user_height, 0)
        self.assertLess(user_height, 3)

    def test_is_currently_student(self):
        self.assertIsInstance(is_currently_student, bool)

if __name__ == '__main__':
    unittest.main()