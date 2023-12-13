
#Assign number of attempt
attempts = 3

#This will loop 3 times if the inputted values is incorrect, if the 3 attempts ran out it will exit
while attempts > 0:
    #To get the input from the user
    number=input ("How Many Numbers: ")
    print ("---------------------------------------")

    #To check if the input is a number and has no decimal
    if number.isnumeric()==True and number.isdecimal()==True:
    
        #To Check if the input number is not less than or equal to zero
        if int(number) <=0:
            attempts = attempts-1
            #To display what is the error and how many attempts left
            if attempts > 1:
                print ("Invalid Input! You cannot input numbers less than or equal to 0")
                print ("You have " + str(attempts) + " attempts remaining")
                print ("---------------------------------------")
            if attempts == 1:
                print ("Invalid Input! You cannot input numbers less than or equal to 0")
                print ("You have " + str(attempts) + " attempt remaining")
                print ("---------------------------------------")
            if attempts == 0:
                print ("You ran out of attempts")
                exit()
        #If the input is correct it will break the loop and display thank you message
        else:
            print("Thank you for your cooperation")
            print ("---------------------------------------")
            break
    #If the input is not a number or has a decimal
    else:
        attempts = attempts -1
        #To display what is the error and how many attempts left
        if attempts > 1:
            print ("Invalid Input! Please Input a Number")
            print ("You have " + str(attempts) + " attempts remaining")
            print ("---------------------------------------")
        if attempts == 1:
            print ("Invalid Input! Please Input a Number")
            print ("You have " + str(attempts) + " attempt remaining")
            print ("---------------------------------------")
        if attempts == 0:
            print ("You ran out of attempts")
            exit()