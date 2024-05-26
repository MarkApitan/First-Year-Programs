from beverage import Beverage
class Beer(Beverage):
    def __init__(self, volume:int,  is_chilled: bool, alcoholic_content: float):
        super().__init__("Beer", volume, is_chilled)
        self.__alcoholic_content = alcoholic_content
    def get_type(self):
        if self.__alcoholic_content < 0.003:
            return "Flavored"
        elif self.__alcoholic_content <0.06:
            return "Regular"
        else:
            return "Strong"
    def __str__(self):
        parent = super().__str__()
        return f"{parent} ({self.__alcoholic_content *100:.1f}% alcoholic content)"

    def get_alcoholic_content(self):
        return self.__alcoholic_content