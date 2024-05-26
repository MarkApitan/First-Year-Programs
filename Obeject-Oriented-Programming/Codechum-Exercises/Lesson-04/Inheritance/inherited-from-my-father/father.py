from person import Person
class Father (Person):
    def __init__(self, name: str, age:int):
        super().__init__(name, age, 'M')
    def introduce_with_style(self, n:int):
        for line in range(n):
            print(" "*line + "I am your father")