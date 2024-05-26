#Lab Exercise No 2: Problem No. 9
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 16, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Exercise No 2 | Problem No. 9 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#getting the input from the user
username = input("Enter a username: ")

#Difining Checkers
alpha_checker = username[0:4].isalpha()
digits_checker = username[4:6].isdigit()

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