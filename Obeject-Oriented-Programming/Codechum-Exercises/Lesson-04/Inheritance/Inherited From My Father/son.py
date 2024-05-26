from father import Father
class Son (Father):
    def __init__(self, name = "Unknown", age:int = 0):
        super().__init__(name, age)

    def introduce_with_style(self, n):
        for line in range(n):
            print(" " * (n-1) + "I am your son")
            n-=1