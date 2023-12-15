#Programming Logic and Design
#Prg5 This program calculates the sum of Even and Odd numbers you input
#December 14, 2023
#Mark Justine L. Apitan

#Assign border to make my life easier
border = ("\033[1;33m-------------------------------------------------------------------\033[0m")

#Welcome introduction of the program
print (border)
print("\tWelcome to \033[0;32mEVEN\033[0m and \033[0;36mODD\033[0m numbers adder program")
print (border)
print ("This program calculates the sum of EVEN and ODD numbers you input")

#This while loop is for the program to repeat again once we asked the user later if they want to use the program again
while True:
    #To assign values
    even_sum =0
    odd_sum =0
    attempts = 4
    attempts_2 = 4
    #This will loop 4 times if the inputted values is incorrect, if the 4 attempts ran out it will exit the program
    while attempts > 0:
        #To get the input from the user
        print (border)
        number=input ("Enter how many numbers would you like to add: ")
        print (border)

        #To check if the input is a number and has no decimal
        if number.isnumeric()==True and number.isdecimal()==True:
            
            #To Check if the input number is not less than or equal to one, I chose one because you cannot add just one number
            if int(number) <=1:
                attempts = attempts-1
                #To display what is the error and how many attempts left
                if attempts > 1:
                    print ("\033[0;31mInvalid Input!\033[0m You cannot input numbers less than or equal to 0")
                    print ("You have " + str(attempts) + " attempts remaining")
                elif attempts == 1:
                    print ("\033[0;31mInvalid Input!\033[0m You cannot input numbers less than or equal to 0")
                    print ("You have " + str(attempts) + " attempt remaining")
                elif attempts == 0:
                    print ("\033[0;31mYou ran out of attempts\033[0m")
                    exit()
            #If the input is correct it will break the loop and display a message
            else:
                print("Please enter the " + str(number) + " numbers")
                print (border)
                break
        #If the input is not a number or has a decimal
        else:
            attempts=attempts-1
            #To display what is the error and how many attempts left
            if attempts > 1:
                print ("\033[0;31mInvalid Input!\033[0m Please Input a Number")
                print ("You have " + str(attempts) + " attempts remaining")
            elif attempts == 1:
                print ("\033[0;31mInvalid Input!\033[0m Please Input a Number")
                print ("You have " + str(attempts) + " attempt remaining")
            elif attempts == 0:
                print ("\033[0;31mYou ran out of attempts\033[0m")
                exit()
    #To loop n times the user inputted
    for x in range(int(number)):
        #This will loop 4 times if the inputted values are invalid, if the 4 attempts ran out it will exit the program
        while attempts_2>0:
            #to get the inputs
            num = input("Enter a Number: ")
            #to check if the inputs are valid
            if num.isnumeric()==True and num.isdecimal()==True:
                if int(num)==0:
                    attempts_2=attempts_2-1
                    if attempts_2 > 1:
                        print (border)
                        print ("\033[0;31mInvalid Input!\033[0m You cannot input zero")
                        print ("You have " + str(attempts_2) + " attempts remaining")
                        print (border)
                    elif attempts_2 == 1:
                        print (border)
                        print ("\033[0;31mInvalid Input!\033[0m You cannot input zero")
                        print ("You have " + str(attempts_2) + " attempt remaining")
                        print (border)
                    elif attempts_2 == 0:
                        print (border)
                        print ("\033[0;31mYou ran out of attempts\033[0m")
                        exit()
                #to check if the input are odd or even
                if int(num)%2==0:
                    #To get the sum of all even numbers
                    even_sum=(int(even_sum)+int(num))
                    break
                else:
                    #To get the sum of all odd numbers
                    odd_sum=(int(odd_sum)+ int(num))
                    break
            else:
                attempts_2=attempts_2-1
                if attempts_2 > 1:
                    print (border)
                    print ("\033[0;31mInvalid Input!\033[0m Please Input a Number")
                    print ("You have " + str(attempts_2) + " attempts remaining")
                    print (border)
                elif attempts_2 == 1:
                    print (border)
                    print ("\033[0;31mInvalid Input!\033[0m Please Input a Number")
                    print ("You have " + str(attempts_2) + " attempt remaining")
                    print (border)
                elif attempts_2 == 0:
                    print (border)
                    print ("\033[0;31mYou ran out of attempts\033[0m")
                    exit()
    #To display the sum
    print (border)
    print ("The total sum of even numbers is " + str(even_sum))
    print ("The total sum of all odd numbers are " + str(odd_sum))

    #To ask the user if they want to use the program again
    print (border)
    try_again = input ("Do you want to use the program again? (yes/no): ") 
    
    if try_again.lower() == "yes":
        print (border)
        print("\tWelcome back to EVEN and ODD numbers adder program")
    else:
        print (border)
        print ("Thank you for using the Program")
        print (border)
        break