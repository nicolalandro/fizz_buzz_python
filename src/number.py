class Number:
    def __init__(self, int_number):
        self.value = int_number

    def is_disible_for(self, n):
        return self.value % n.value == 0

    def __str__(self):
        return str(self.value)
