from beverage import Beverage
class Water (Beverage):
    def __init__(self, volume:int, is_chilled:bool, type:str):
        super().__init__("Water", volume, is_chilled)
        if type not in ["Purified", "Regular", "Distilled"]:
            self.__type = "Regular"
        else:
            self.__type = type
    def get_type(self):
        return self.__type