# Getting a Cat - Python
# by CodeChum Admin

# Create a class called Cat in another file with the following properties:

# Class - Cat:

# Properties:
# name (type: str): Represents the name of the cat.
# color (type: str): Indicates the color of the cat.
# gender (type: str): Holds the gender of the cat, represented by 'M' (Male) or 'F' (Female).

# Constructor:
# __init__(self, name: str, color: str, gender: str): This constructor takes three parameters: name, color, and gender. It assigns these values to their respective properties within the class.

# Define a class called Cat
class Cat:
    # Define the constructor method
    def __init__(self, name: str, color: str, gender: str):
        # Assign the value of the 'name' parameter to the 'name' property
        self.name = name
        # Assign the value of the 'color' parameter to the 'color' property
        self.color = color
        # Assign the value of the 'gender' parameter to the 'gender' property
        self.gender = gender