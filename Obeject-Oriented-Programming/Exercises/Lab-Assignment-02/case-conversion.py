#Lab Exercise No 2: Problem No. 5
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 16, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Exercise No 2 | Problem No. 5 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To get the user input
name = input("Enter a name: ")

#To display the outputs
#a. returns the name in lower case
print(f"\nlower case: {name.lower()}")
#b. returns the name in upper case
print(f"UPPER case: {name.upper()}")
#c. returns the name with the first letter as UPPER case and the rest lower 
print(f"Capitalized the first letter: {name[0].upper()}{name[1:].lower()}")

print(border)