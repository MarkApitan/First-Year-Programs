#Making a Smoothie - Python
#by CodeChum Admin

#A class named Blender is provided, which represents a blender. The class has the following details to implement:

#Class - Blender:

#Public Methods:
#blend(fruit1: str = None, fruit2: str = None, n: int = 1)
#This method accepts three parameters, fruit1, fruit2, and n, with default values of None and 1.
#If no fruits are provided (both fruit1 and fruit2 are None), it prints "There's nothing to blend here, boss."
#If fruit1 and fruit2 are provided, it prints "Blending {fruit1} and {fruit2}, boss."
#If n is greater than 1, it repeats the message for n times, each on a new line.

# Define a class named Blender
class Blender:
    # Define a method named blend with three parameters: fruit1, fruit2, and n
    def blend(self, fruit1: str = None, fruit2: str = None, n: int = 1):
        # Check if no fruits are provided
        if fruit1 is None and fruit2 is None:
            print("There's nothing to blend here, boss.")
        # Check if both fruit1 and fruit2 are provided
        elif fruit1 is not None and fruit2 is not None:
            # Repeat the message for n times
            for i in range(n):
                print(f"Blending {fruit1} and {fruit2}, boss.")

# Create an instance of the Blender class
blender = Blender()

# Call the blend method with no fruits provided
blender.blend()

# Call the blend method with "Apple" and "Banana" as fruits
blender.blend("Apple", "Banana", 1)

# Call the blend method with "Pineapple" and "Grapes" as fruits, and repeat the message 3 times
blender.blend("Pineapple", "Grapes", 3)
