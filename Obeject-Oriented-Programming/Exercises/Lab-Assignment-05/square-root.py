#Lab Assignment No 5: Problem No. 1
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 24, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 5 | Problem No. 1 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To import math module
import math

#Open and write a file
sqrt = open("sqrt_results.txt","w")

def main ():
    #define variables
    end = False
    counter = 0
    #To make a loop
    while end != True:
        #Get the user input
        number = (input("Enter a number to square root: "))
        #To try, get, and write the results
        try:
            result = round(math.sqrt(int(number)), 2)
            if counter ==0: 
                sqrt.write(f"The square root of {number} is {result}")
                counter+=1
            else:
                sqrt.write(f"\nThe square root of {number} is {result}")
        #To catch the ValueError
        except ValueError:
            print("Error! Please Enter a valid number")
        #To ask the user if they want to input again
        input_again = input("Do you want to input again? [y/n]: ")
        if input_again.lower() == 'n':
            print("Thank you!")
            end = True
        elif input_again.lower() == 'y':
            continue
        else:
            print("Invalid Input! The program will exit.")
            end = True
main()
sqrt.close