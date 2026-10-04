import unittest
from main import add, subtract, multiply, divide, is_palindrome

class TestMainFunctions(unittest.TestCase):

    def test_add(self):
        """Тестування функції додавання."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)

    def test_subtract(self):
        """Тестування функції віднімання."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        """Тестування функції множення."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(5, 0), 0)

    def test_divide(self):
        """Тестування функції ділення."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Тестування винятку при діленні на нуль."""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_is_palindrome(self):
        """Тестування перевірки на паліндром."""
        self.assertTrue(is_palindrome("шалаш"))
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))
        self.assertFalse(is_palindrome("python"))

if __name__ == '__main__':
    unittest.main()