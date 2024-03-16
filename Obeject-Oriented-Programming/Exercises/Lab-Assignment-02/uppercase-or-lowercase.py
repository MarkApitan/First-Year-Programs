#Lab Exercise No 2: Problem No. 6
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: March 16, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Exercise No 2 | Problem No. 6 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#to get the input from the user
letter = input("Enter a letter: ")

#defining variables
upper = letter.upper()
lower = letter.lower()

if letter == upper:
    print(f"The letter '{letter}' is in upper case")
elif letter == lower:
    print(f"The letter '{letter}' is in lower case")

print(border)