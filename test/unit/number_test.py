import unittest

from src.number import Number


class NumberTestCase(unittest.TestCase):
    def test_create_number(self):
        number = Number(5)
        self.assertEqual(5, number.value)

    def test_is_divisible_for(self):
        number = Number(5)
        divisible = number.is_divisible_for(Number(5))
        self.assertTrue(divisible)

    def test_is_not_divisible_for(self):
        number = Number(5)
        divisible = number.is_divisible_for(Number(2))
        self.assertFalse(divisible)


if __name__ == '__main__':
    unittest.main()
