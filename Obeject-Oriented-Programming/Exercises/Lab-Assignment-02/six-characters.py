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

#To check if the input are 6 characters long
if length == 6:
    print("You have entered 6 characters")
elif length > 6:
    print("Error! You have entered greater than 6 characters")
elif length < 6:
    print("Error! You have entered less than 6 characters")

print(border)