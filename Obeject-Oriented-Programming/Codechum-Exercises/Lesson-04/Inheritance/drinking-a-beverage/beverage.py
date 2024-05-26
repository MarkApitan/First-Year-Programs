class Beverage:
    def __init__(self, name:str, volume:int, is_chilled:bool):
        self.__name = name
        self.__volume = volume
        self.__is_chilled = is_chilled
    def is_empty(self):
        return self.__volume == 0
    def __str__(self):
        chilled_status = "is still chilled" if self.__is_chilled else "is not chilled anymore"
        return f"{self.__name} ({self.__volume}mL) {chilled_status}"

    def get_name(self):
        return self.__name
    def get_volume(self):
        return self.__volume
    def get_is_chilled(self):
        return self.__is_chilled