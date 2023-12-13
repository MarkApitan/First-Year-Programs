
#Assign number of attempt
border = ("-------------------------------------------------------------------")

#Welcome introduction of the program
print (border)
print("\tWelcome to EVEN and ODD numbers adder program")
print (border)
print ("This program calculates the sum of EVEN and ODD numbers you input")
#This while loop is for the program to repeat again once we asked the user later if they want to use the program again
while True:
    even_sum =0
    odd_sum =0
    attempts = 4
    attempts_2 = 4
    #This will loop 3 times if the inputted values is incorrect, if the 3 attempts ran out it will exit the program
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
                    print ("Invalid Input! You cannot input numbers less than or equal to 0")
                    print ("You have " + str(attempts) + " attempts remaining")
                    print (border)
                elif attempts == 1:
                    print ("Invalid Input! You cannot input numbers less than or equal to 0")
                    print ("You have " + str(attempts) + " attempt remaining")
                    print (border)
                elif attempts == 0:
                    print ("You ran out of attempts")
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
                print ("Invalid Input! Please Input a Number")
                print ("You have " + str(attempts) + " attempts remaining")
                print (border)
            elif attempts == 1:
                print ("Invalid Input! Please Input a Number")
                print ("You have " + str(attempts) + " attempt remaining")
                print (border)
            elif attempts == 0:
                print ("You ran out of attempts")
                exit()

    for x in range(int(number)):
        while attempts_2>0:
            num = input("Enter a Number: ")
            if num.isnumeric()==True and num.isdecimal()==True:
                if int(num)%2==0:
                    even_sum=(int(even_sum)+int(num))
                    break
                else:
                    odd_sum=(int(odd_sum)+ int(num))
                    break
            else:
                attempts_2=attempts_2-1
                if attempts_2 > 1:
                    print (border)
                    print ("Invalid Input! Please Input a Number")
                    print ("You have " + str(attempts_2) + " attempts remaining")
                    print (border)
                elif attempts_2 == 1:
                    print (border)
                    print ("Invalid Input! Please Input a Number")
                    print ("You have " + str(attempts_2) + " attempt remaining")
                    print (border)
                elif attempts_2 == 0:
                    print (border)
                    print ("You ran out of attempts")
                    exit()
    print (border)
    print ("The total sum of even numbers is " + str(even_sum))
    print ("The total sum of all odd numbers are " + str(odd_sum))

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