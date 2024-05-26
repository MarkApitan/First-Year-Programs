# A Car That Works - Python
# by CodeChum Admin

# For this problem, you are tasked to create the class Car:

# Class - Car:

# Private Properties:
# color (type: str): Represents the color of the car.
# price (type: float): Holds the price of the car.
# size (type: str): Indicates the size of the car, where 'S' represents small, 'M' represents medium, and 'L' represents large.

# Constructor:
# __init__(self, color: str, price: float, size: str): Initializes the car's color, price, and size properties. The size is standardized to uppercase using size.upper().

# Methods
# Getter Methods:
# get_color(self) -> str: Returns the car's color.
# get_price(self) -> float: Returns the car's price.
# get_size(self) -> str: Returns the car's size.

# Setter Methods:
# set_color(self, color: str) -> None: Sets the car's color to the specified value.
# set_price(self, price: float) -> None: Sets the car's price to the specified value.
# set_size(self, size: str) -> None: Sets the car's size to the specified value. The size should be one of 'S' for small, 'M' for medium, or 'L' for large. Use conversion of lowercase characters to uppercase using size.upper().

# __str__ Method:
# __str__(self) -> str: Returns a formatted string representing the car, following the format "Car (color) - P(price, formatted to two decimal places) - (size descriptor)". The size descriptor is determined based on the size character ('small' for 'S', 'medium' for 'M', and 'large' for 'L').

# Example Strings:
# For a red car priced at 19999.85 and of medium size: "Car (red) - P19999.85 - medium"
# "Car (blue) - P50000.00 - large"

# Define the class Car
class Car:
    # Constructor to initialize the car's color, price, and size properties
    def __init__(self, color:str, price:float, size: str):
        self.__color = color  # Set the color property to the specified value
        self.__price = price  # Set the price property to the specified value
        self.__size = size.upper()  # Set the size property to the specified value, converted to uppercase

    # Getter method to retrieve the car's color
    def get_color(self):
        return self.__color

    # Setter method to set the car's color to the specified value
    def set_color(self, color:str):
        self.__color = color

    # Getter method to retrieve the car's price
    def get_price(self):
        return self.__price

    # Setter method to set the car's price to the specified value
    def set_price(self, price:float):
        self.__price = price

    # Getter method to retrieve the car's size
    def get_size(self):
        return self.__size

    # Setter method to set the car's size to the specified value
    def set_size(self, size:str):
        self.__size = size

    # String representation of the car object
    def __str__(self):
        # Determine the size descriptor based on the size character
        size_descriptor = {'S': 'small', 'M': 'medium', 'L': 'large'}.get(self.__size, 'unknown')

        # Return the formatted string representing the car
        return (f"Car ({self.__color}) - P{self.__price:.2f} - {size_descriptor}")