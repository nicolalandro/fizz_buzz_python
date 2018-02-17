import unittest

from src.fizz_buzzer import FizzBuzzer
from src.number import Number
from unittest.mock import MagicMock


class FizzBuzzerTestCase(unittest.TestCase):
    def setUp(self):
        self.number_3 = Number(3)
        self.fizz_buzzer = FizzBuzzer(self.number_3)

    def test_fizz(self):
        number = MagicMock()
        number.is_divisible_for = MagicMock(return_value=True)
        number.__str__.return_value = 'test str'

        self.fizz_buzzer.speach_text_for(number)

        number.is_divisible_for.assert_called_once_with(self.number_3)
        number.__str__.assert_not_called()

    def test_number(self):
        number = MagicMock()
        number.is_divisible_for = MagicMock(return_value=False)
        number.__str__.return_value = 'test str'

        self.fizz_buzzer.speach_text_for(number)

        number.is_divisible_for.assert_called_once_with(self.number_3)
        number.__str__.assert_called_with()


if __name__ == '__main__':
    unittest.main()
