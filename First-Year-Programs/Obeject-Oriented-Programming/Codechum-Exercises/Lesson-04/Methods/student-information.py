#Student Information - Python
##by CodeChum Admin

#Implement the class Student with the following public details:

#Class - Student:

#Public Properties:
#id_number (type: int): A unique identifier for the student.
#name (type: str): The name of the student.
#course (type: str): The course the student is enrolled in.
#Methods:
#__str__() -> str: Returns a string representation of the student's information in the format "{id_number} - {name} - {course}".
#validate_info() -> None: Prints the message "Student information is valid." or "Student information is not valid." indicating whether the student's information is valid. Validity criteria include:
#The name should contain only letters.
#The idNumber should be exactly 9 digits long.

# Start typing your code
# Define the class Student
class Student:
    # Initialize the Student object with id_number, name, and course
    def __init__(self, id_number= int, name=str, course= str):
        self.id_number = id_number
        self.name = name
        self.course = course
    
    # Return a string representation of the student's information
    def __str__(self):
        return f"{self.id_number} - {self.name} - {self.course}"
    
    # Validate the student's information
    def validate_info(self):
        # Check if the id_number is exactly 9 digits long
        if len(str(self.id_number)) != 9:
            print ("Student information is not valid.")
        # Check if the name contains only letters
        elif not self.name.replace(" ", "").isalpha():
            print ("Student information is not valid.")
        else:
            print ("Student information is valid.")

# Create an instance of the Student class
student1 = Student(123456789, "John Doe", "Computer Science")
# Validate the student's information
student1.validate_info()