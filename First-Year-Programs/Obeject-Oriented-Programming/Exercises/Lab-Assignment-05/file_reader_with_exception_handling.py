# Write a program that reads the contents of a text file and implements error handling using try-except-finally block
# to handle exceptions such as "FileNotFoundError" and "IOError". 
# Print the contents of the file or display appropriate error messages 
# if any of these exceptions occur during file handling.

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 4 | Problem No. 2 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To read and close the file
try:
    with open("sqrt_results", "r") as file:  # Open the file in read mode
        contents = file.read()  # Read the contents of the file
        print(f"Contents: {contents}")  # Print the contents 
        file.close
#To handle the errors
except FileNotFoundError:
    print("FileNotFoundError: File not found!")
except IOError:
    print("IOError: File not found!")
#To print the closing statement of the program
finally:
    print("Program will exit. Thank you!")