# Dog Breeds - Python
# by CodeChum Admin

# Implement the class Dog with the following details:

# Class - Dog:

# Properties:
# breed (type: str): The breed of the dog.
# bark_count (type: int): A counter to keep track of the number of times the dog has barked, initialized to 0.

# Methods:
# Getter and Setter for breed:
# get_breed(self) -> str: Returns the breed of the dog.
# set_breed(self, breed: str) -> None: Sets the breed of the dog to the given breed.

# Getter for barkCount:
# get_bark_count(self) -> int: Returns the bark count.

# has_barked_a_lot(self) -> bool: Returns True if bark_count has reached 100 or more. This method checks whether the dog has barked a significant number of times.

# bark(self, n: int) -> None: Simulates the dog barking n times. It prints "Woof" n times (each on a new line) and adds n to the current bark_count. This method allows the dog to bark multiple times and updates the bark counter accordingly.

# Class Dog:
class Dog:
    def __init__(self, breed:str):
        # Initialize the breed property with the given breed
        self.__breed = breed
        # Initialize the bark_count property to 0
        self.__bark_count = 0

    # Getter for breed
    def get_breed (self):
        # Return the breed of the dog
        return self.__breed

    # Setter for breed
    def set_breed (self, breed:str):
        # Set the breed of the dog to the given breed
        self.__breed = breed

    # Getter for bark_count
    def get_bark_count(self):
        # Return the bark count of the dog
        return self.__bark_count

    # Check if the dog has barked a lot
    def has_barked_a_lot(self):
        # Return True if the bark count is 100 or more, otherwise return False
        return self.__bark_count >= 100

    # Simulate the dog barking n times
    def bark (self, n:int):
        # Print "Woof" n times
        for i in range(n):
            print("Woof")
        # Add n to the current bark_count
        self.__bark_count+=n