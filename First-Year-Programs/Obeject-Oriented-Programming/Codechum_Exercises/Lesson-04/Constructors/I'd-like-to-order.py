#I'd Like to Order... - Python
#by CodeChum Admin

#Create a class called Beverage which has the following details:

#Class - Beverage:

#Public Properties:
#flavor (type: str): Specifies the flavor of the beverage.
#color (type: str): Indicates the color of the beverage.
#Constructors:
#__init__(self, flavor: str = "Unknown", color: str = "Unknown"): This constructor initializes the flavor and color properties to the values passed in these parameters. If no parameters are provided, it uses default values of "Unknown" for both properties.
#Class - Bottle:
#Public Properties:
#mL (type: int): Represents the volume of the bottle in milliliters.
#beverage (type: Beverage): Holds a Beverage object representing the beverage contained in the bottle.
#Constructor:
#__init__(self, mL: int, flavor: str = "Unknown", color: str = "Unknown"): This constructor accepts three parameters: mL (an integer), flavor (a string), and color (a string). It constructs a Beverage object using the flavor and color values and then sets this Beverage object as the value of the beverage property of the Bottle object. If flavor and color are not provided, they default to "Unknown".

# Start typing your code
class Beverage:
    def __init__ (self, flavor: str = "Unknown", color: str = "Unknown"):
        # Initialize the flavor property with the value passed in the flavor parameter
        self.flavor = flavor
        # Initialize the color property with the value passed in the color parameter
        self.color = color

class Bottle:
    def __init__ (self, mL = int, flavor: str = "Unknown", color: str = "Unknown"):
        # Initialize the mL property with the value passed in the mL parameter
        self.mL = mL
        # Create a Beverage object using the flavor and color values
        self.beverage = Beverage(flavor, color)