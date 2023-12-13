
#Assign number of attempt
attempts = 4

#This will loop 3 times if the inputted values is incorrect, if the 3 attempts ran out it will exit the program
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
            elif attempts == 1:
                print ("Invalid Input! You cannot input numbers less than or equal to 0")
                print ("You have " + str(attempts) + " attempt remaining")
                print ("---------------------------------------")
            elif attempts == 0:
                print ("You ran out of attempts")
                exit()
        #If the input is correct it will break the loop and display thank you message
        else:
            print("Thank you for your cooperation")
            print ("---------------------------------------")
            break
    #If the input is not a number or has a decimal
    else:
        attempts=attempts-1
        #To display what is the error and how many attempts left
        if attempts > 1:
            print ("Invalid Input! Please Input a Number")
            print ("You have " + str(attempts) + " attempts remaining")
            print ("---------------------------------------")
        elif attempts == 1:
            print ("Invalid Input! Please Input a Number")
            print ("You have " + str(attempts) + " attempt remaining")
            print ("---------------------------------------")
        elif attempts == 0:
            print ("You ran out of attempts")
            exit()

attempts_2 = 4
even_sum=0
odd_sum=0
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
                print ("Invalid Input! Please Input a Number")
                print ("You have " + str(attempts_2) + " attempts remaining")
                print ("---------------------------------------")
            elif attempts_2 == 1:
                print ("Invalid Input! Please Input a Number")
                print ("You have " + str(attempts_2) + " attempt remaining")
                print ("---------------------------------------")
            elif attempts_2 == 0:
                print ("You ran out of attempts")
                exit()
    
print ("The total sum of even numbers is " + str(even_sum))
print ("The total sum of all odd numbers are " + str(odd_sum))