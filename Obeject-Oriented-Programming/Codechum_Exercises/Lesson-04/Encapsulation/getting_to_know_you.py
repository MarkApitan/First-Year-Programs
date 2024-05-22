# Getting to Know You - Python
# by CodeChum Admin

# A class Person with attributes is already defined in the code editor:

# Class - Person:

# Attributes (Already implemented):
# name (type: str): The name of the person.
# age (type: int): The age of the person.
# gender (type: str): The gender of the person, represented as 'M' (Male) or 'F' (Female).

# Getters and Setters:
# get_name(self) -> str: Returns the value of the name attribute.
# set_name(self, name: str) -> None: Sets the name attribute to the provided value.
# get_age(self) -> int: Returns the value of the age attribute.
# set_age(self, age: int) -> None: Sets the age attribute to the provided value, with possible validations if required (e.g., age should be positive).
# get_gender(self) -> str: Returns the value of the gender attribute.
# set_gender(self, gender: str) -> None: Sets the gender attribute to the provided value, ensuring it is either 'M' (Male) or 'F' (Female).

class Person:
    # Initialize the Person class with name, age, and gender attributes
    def __init__(self, name = None, age = 0, gender = None):
        self.name = name  # Name of the person, default is None
        self.age = age  # Age of the person, default is 0
        self.gender = gender  # Gender of the person, default is None

    # Method to get the name of the person
    def get_name(self):
        return self.name

    # Method to set the name of the person
    def set_name (self, name: str):
        self.name = name

    # Method to get the age of the person
    def get_age (self):
        return self.age

    # Method to set the age of the person
    def set_age (self, age: int):
        self.age = age

    # Method to get the gender of the person
    def get_gender (self):
        return self.gender

    # Method to set the gender of the person
    def set_gender (self, gender:str):
        self.gender = gender