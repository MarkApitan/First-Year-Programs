#Lab Exercise No 2: Problem No. 7
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 16, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Exercise No 2 | Problem No. 7 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To get the input from the user
username = input("Enter a username which has 6 characters: ")

#To define variable
length = len(username)
alpha_checker = username[0:4].isalpha()
digits_checker = username[4:6].isdigit()

#To check if the input are 6 characters long
if length == 6:
    print("You have entered 6 characters")
elif length > 6:
    print("Error! You have entered greater than 6 characters")
elif length < 6:
    print("Error! You have entered less than 6 characters")

#To check 
if alpha_checker == True and digits_checker == True:
    print(f"The first four characters are alpha, and the fifth and sixth characters are digits.")
elif alpha_checker == False and digits_checker == True:
    print(f"The first four characters are NOT alpha, and the fifth and sixth characters are digits.")
elif alpha_checker == True and digits_checker == False:
    print(f"The first four characters are alpha, and the fifth and sixth characters are NOT digits.")
else:
    print(f"The first four characters are NOT alpha, and the fifth and sixth characters are NOT digits.")

print(border)