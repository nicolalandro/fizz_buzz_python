import sys

from src.fizz_buzzer import FizzBuzzer
from src.number import Number

if __name__ == '__main__':
    fizz_buzzer = FizzBuzzer()
    for i in range(1, int(sys.argv[1]) + 1):
        i_number = Number(i)
        speach_text = fizz_buzzer.speach_text_for(i_number)
        print(speach_text)
