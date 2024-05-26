from number import Number
class WholeNumber(Number):
    def __init__(self, value: int):
        super().__init__(value)

    def multiply(self, whole_number: 'WholeNumber'):
        new_value = self.get_value() * whole_number.get_value()
        self.set_value(new_value)

    def __str__(self):
        return str(self.get_value())