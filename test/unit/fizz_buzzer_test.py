import unittest

from src.fizz_buzzer import FizzBuzzer
from src.number import Number


class FizzBuzzerTestCase(unittest.TestCase):
    def setUp(self):
        self.fizz_buzzer = FizzBuzzer()

    def test_number(self):
        number = Number(2)
        speach_text = self.fizz_buzzer.speach_text_for(number)
        self.assertEqual('2', speach_text)

    def test_fizz(self):
        number = Number(3)
        speach_text = self.fizz_buzzer.speach_text_for(number)
        self.assertEqual('fizz', speach_text)


if __name__ == '__main__':
    unittest.main()
