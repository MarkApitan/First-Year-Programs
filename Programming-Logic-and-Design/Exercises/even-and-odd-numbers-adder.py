#Programming Logic and Design
#Prg5 This program calculates the sum of Even and Odd numbers you input
#December 14, 2023
#Mark Justine L. Apitan

#to define a function that will check if the input is correct
def is_int(num_to_add):
     try:
        int (num_to_add)
        return True
     except ValueError:
        return False

def ordinal(nth_term):

    #Returns ordinal number string from int, e.g. 1, 2, 3 becomes 1st, 2nd, 3rd, etc.
    if nth_term ==11:
        suffix = str('th')
    elif nth_term ==12:
        suffix = str('th')
    elif nth_term ==13:
        suffix = str('th')
    elif nth_term==1 or (nth_term % 10) == 1:
        suffix = str('st')
    elif nth_term==2 or (nth_term % 10) == 2:
        suffix = str('nd')
    elif nth_term==3 or (nth_term % 10) == 3:
        suffix = str('rd')
    elif nth_term >=4 or (nth_term % 10) == 4:
        suffix = str('th')
    return suffix

#Assign border to make my life easier
border = ("\033[1;35m-------------------------------------------------------------------\033[0m")

#Welcome introduction of the program
print (border)
print("\tWelcome to \033[0;32mEVEN\033[0m and \033[0;36mODD\033[0m numbers adder program")
print (border)
print ("This program calculates the sum of EVEN and ODD numbers you input")
print (border)

#This while loop is the main loop of the program. It is for the program to repeat again once we asked the user later if they want to use the program again
while True:

    #To assign values
    even_sum =0
    odd_sum =0
    
    #To loop once the user enter invalid input
    while True:
        #To get the input from the user
        
        how_many_number = input("Enter how many numbers would you like to add: ")
        print (border)

        #To check if the input is a number and has no decimal
        if how_many_number.isnumeric() == True and how_many_number.isdecimal() == True:
            
            #To Check if the input number is not less than or equal to one, I chose one because you cannot add just one number
            if int(how_many_number) <=1:

                #To display what is the error and ask if the user one to re-enter
                print ("\033[0;31mInvalid Input!\033[0m You cannot input numbers less than or equal to 1")
                input_again = input ("Would you like to re-enter? (yes/no):")
                if input_again.lower()=="yes":
                    print (border)
                else:
                    print (border)
                    print ("Thank you for using the Program")
                    print (border)
                    exit()

            #If the input is correct it will break the loop and display a message
            else:
                print("Please enter the " + str(how_many_number) + " numbers")
                print (border)
                break

        #If the input is not a number or has a decimal
        else:
            print ("\033[0;31mInvalid Input!\033[0m Please enter a number")
            input_again = input ("Would you like to re-enter? (yes/no):")

            if input_again.lower()=="yes":
                print (border)
            else:
                print (border)
                print ("Thank you for using the Program")
                print (border)
                exit()

    for number in range (int(how_many_number)):
        while True:            
            nth_term = int(number)+1
            suffix = ordinal(nth_term)
            num_to_add = input("Enter "+ str(nth_term) + suffix + " number: ")

            if is_int(num_to_add)==True:
                if int(num_to_add)%2==0:
                    #To get the sum of all even numbers
                    even_sum=(int(even_sum)+int(num_to_add))
                    break
                else:
                    #To get the sum of all odd numbers
                    odd_sum=(int(odd_sum)+ int(num_to_add))
                    break
            else:
                print (border)
                print ("\033[0;31mInvalid Input!\033[0m Please enter a number")
                input_again = input ("Would you like to re-enter? (yes/no):")

                if input_again.lower()=="yes":
                    print (border)
                else:
                    print (border)
                    print ("Thank you for using the Program")
                    print (border)
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
        print (border)
    else:
        print (border)
        print ("Thank you for using the Program!")
        print (border)
        break