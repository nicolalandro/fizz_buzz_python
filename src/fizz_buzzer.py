from src.number import Number


class FizzBuzzer:
    def __init__(self, number_3=Number(3)):
        self.number_3 = number_3

    def speach_text_for(self, number):
        if number.is_divisible_for(self.number_3):
            return 'fizz'
        else:
            return str(number)
