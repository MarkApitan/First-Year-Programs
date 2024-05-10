#Anatomy of a Rectangle - Python
#by CodeChum Admin

#A class Rectangle is already defined in the code editor. Complete the class with the following details: 

#Class - Rectangle:

#Implemented Public Properties:
#length (type: float): Represents the length of the rectangle.
#width (type: float): Represents the width of the rectangle.
#Public Method:
#get_area(self) -> float: This method takes no parameters. It calculates the area of the rectangle using the formula Area = length x width and returns the result as a floating-point value.
class Rectangle:
    def __init__(self, length = float, width = float):
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width

rectangle1 = Rectangle(5,10)
print(rectangle1.get_area())

rectangle2 = Rectangle(3,4)
print(rectangle2.get_area())

rectangle3 = Rectangle(2.5,4.5)
print(rectangle3.get_area())