from number import Number
class DecimalNumber(Number):
    def __init__(self, value:int, decimal_places:int):
        super().__init__(value)
        self.__decimal_places = decimal_places
        self.__value = value

    def get_decimal_places(self):
        return self.__decimal_places
    def set_decimal_places(self, decimal_places):
        self.__decimal_places = decimal_places

    def multiply(self, decimal_number: 'DecimalNumber'):
        self.__value *= decimal_number.__value
        self.__decimal_places  += decimal_number.__decimal_places

    def __str__(self):
        return f"0.{self.__value:0{self.__decimal_places}d}"