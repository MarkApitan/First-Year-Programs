
#get the input

attempts = 3

#check if input is a number, and has no decimal
while attempts >0 :
    number = input("How many numbers? ")
    if number.isnumeric()==True and number.isdecimal()==True:
        if number <=0:
            attempts = attempts -1
            #magdagdag ng message
        #isip if may mga invalid inputs pa
    else:
        attempts = attempts -1
        if attempts > 1:
            print ("\nInvalid Input! Please Input a Number")
            print ("You have " + str(attempts) + " attempts remaining")
            print ("---------------------------------------")
        if attempts == 1:
            print ("\nInvalid Input! Please Input a Number")
            print ("You have " + str(attempts) + " attempt remaining")
            print ("---------------------------------------")
        if attempts == 0:
            print ("You ran out of attempts")
            exit()


