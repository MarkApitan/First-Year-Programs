#Complex Calculator - Python
#by CodeChum Admin

#Implement the class called ComplexCalculator with the following details:

 

#Class - ComplexCalculator:

#Public Methods:
#get_square_root(number: int) -> float: Returns the square root of number as a floating-point number. If number is negative, it returns 0.
#get_factorial(number: int) -> int: Computes and returns the factorial of number as an integer. If number is negative, it returns 0.
#get_sum(number1: int, number2: int) -> float: Returns the sum of number1 and number2 as a floating-point number.
#get_product(number1: int, number2: int) -> float: Returns the product of number1 and number2 as a floating-point number.
#get_difference(number1: int, number2: int) -> float: Returns the difference between number1 and number2 as a floating-point number.
#get_quotient(number1: int, number2: int) -> float: Returns the quotient when number1 is divided by number2 as a floating-point number. In cases of infinite or invalid divisions (like division by zero), it returns 0.

# Class definition for ComplexCalculator
class ComplexCalculator:
    # Method to calculate the square root of a number
    def get_square_root(self, number = int):
        # Check if the number is negative
        if number < 0:
            return 0
        else: 
            return number ** 0.5
            
    # Method to calculate the factorial of a number
    def get_factorial (self, number = int):
        # Check if the number is negative
        if number < 0:
            return 0
        else:
            factorial = 1
            # Calculate the factorial using a loop
            for i in range (1, number +1):
                factorial *= i
            return factorial

    # Method to calculate the sum of two numbers
    def get_sum (self, number1 = int, number2 = int ):
        return number1 + number2

    # Method to calculate the product of two numbers
    def get_product (self, number1 = int, number2 = int):
        return number1 * number2

    # Method to calculate the difference between two numbers
    def get_difference (self, number1 = int, number2 = int):
        return number1 - number2

    # Method to calculate the quotient of two numbers
    def get_quotient (self, number1 = int, number2 = int):
        try:
            return number1/number2
        except ZeroDivisionError:
            return 0