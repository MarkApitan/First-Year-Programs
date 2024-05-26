from performer import Performer
class Singer(Performer):
    def __init__(self, name:str, age:int, vocal_range:str):
        super().__init__(name,age)
        self.vocal_range = vocal_range
    def get_vocal_range(self):
        return self.vocal_range
    def sing(self):
        print (f"{self.name} is singing with a {self.vocal_range} range.")