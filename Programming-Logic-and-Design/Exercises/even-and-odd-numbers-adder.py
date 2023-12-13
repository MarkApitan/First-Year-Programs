attempts = 3

while attempts > 0:
    number=input ("How Many Numbers: ")
    print ("---------------------------------------")
    if number.isnumeric()==True and number.isdecimal()==True:
        if int(number) <=0:
            attempts = attempts-1
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
        else:
            break
    else:
        attempts = attempts -1
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