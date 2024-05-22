#Two Kinds of Birds - Python
#by CodeChum Admin

#Create a class called Bird with the following details:

 

#Class - Bird:

#Public Properties:
#breed (type: str): Represents the breed of the bird.
#is_nocturnal (type: bool): Indicates whether the bird is nocturnal (active during the night).
#Constructor:
#__init__(self, breed: str = "Unknown", is_nocturnal: bool = False): This constructor can be used in two ways:
#When called with no parameters, it initializes the breed property to "Unknown" and the is_nocturnal property to False.
#When called with parameters, it sets the breed and is_nocturnal

# Start typing your code
# Define a class called Bird
class Bird: 
    # Define a constructor method that takes two parameters: breed and is_nocturnal
    def __init__ (self, breed: str = "Unknown", is_nocturnal: bool = False):
        # Set the breed property of the bird object to the value of the breed parameter
        self.breed = breed
        # Set the is_nocturnal property of the bird object to the value of the is_nocturnal parameter
        self.is_nocturnal = is_nocturnal