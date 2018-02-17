from src.number import Number


class FizzBuzzer:
    def __init__(self):
        pass

    def speach_text_for(self, number):
        if number.is_disible_for(Number(3)):
            return 'fizz'
        else:
            return str(number)
