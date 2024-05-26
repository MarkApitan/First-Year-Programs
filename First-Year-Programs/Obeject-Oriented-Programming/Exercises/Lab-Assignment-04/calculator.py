# Create a Simple App Calculator
# 1. The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
# 2. The application will ask the user for two numbers
# 3. Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

#Introduction 
border = ("-"*80)
print(f"{border}\nProgram Title: Lab Assignment No 3 | Problem No. 1 \nProgrammed by: Mark Justine L. Apitan\n{border}")

#assigned values for operators
operators = ['1', '2', '3', '4']

#Define the choices and the end_of_program variable for the control of the loop
choices = ['y', 'n']
end_of_program = False

#define a function that will create a message, symbol, and operation depending on the input of the use
def message(operator):
    mess1 = ''
    mess2 = ''
    operation = ''
    symbol = ''
    if operator == '1':
        mess1 = "Enter the first number to add: "
        mess2 = "Enter the second number to add: "
        operation = "add"
        symbol = "+"
    elif operator == '2':
        mess1 = "Enter the minuend: "
        mess2 = "Enter the subtrahend: "
        operation = 'subtract'
        symbol = "-"
    elif operator == '3':
        mess1 = "Enter the multiplicand: "
        mess2 = "Enter the multiplier: "
        operation = 'multiply'
        symbol = "x"
    elif operator == '4':
        mess1 = "Enter the dividend: "
        mess2 = "Enter the divisor: "
        operation= "divide"
        symbol = "/"
    return mess1, mess2, operation, symbol

#define a function that will compute for the result
def computations(num1, num2):
    result = 0
    if operator == '1':
        result = (num1+num2)
    elif operator == '2':
        result = (num1-num2)
    elif operator == '3':
        result = (num1*num2)
    elif operator == '4':
        result = (num1/num2)
    return round(result,2)

#Create the loop
while end_of_program == False:
    #Define variables
    num1 = 0
    num2 = 0
    result = 0
    mess1 = ''
    mess2 = ''
    operation = ''
    symbol = ''
    #Print instructions for the user
    print(f"\t\t\tWelcome to Phyton Calculator\n{border}")
    print("Type a number from 1 to 4 to choose an operation: \n[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division")
    try:
        #To get the what operator the user wants
        operator = input("\nEnter the number corresponding to the operation you want to perform: ")
        print(border)

        #To check if the operator is valid
        if operator not in operators:
            print("ERROR! Invalid input. Please enter value 1-4")
            print(border)
            end_of_program = True
        #To Get the numbers from the users
        else:
            mess1, mess2, operation, symbol = message(operator)
            print(f"Please enter the numbers you would like to {operation} ")
            num1 = float(input(f"{mess1}"))
            num2 = float(input(f"{mess2}"))
            print (border)
        #To print the result
            result = computations(num1, num2)
            print (f"{num1} {symbol} {num2} = {result}")
            print (f"Total: {result}")
            print(border)
    #To catch the errors
    except ValueError as x:
        print("ERROR! Please Enter a number")
    except ZeroDivisionError as x:
        print("ERROR! You can not divide by zero")
    #To ask the user if they want to try again
    while True:
        choice = input("Do you want to try again? (y/n): ").lower()
        if choice not in choices:
            print("PLease enter 'y' or 'n'")
        else:
            break
    if choice == 'y':
        print(border)
        end_of_program=False
    elif choice == 'n':
        print(border)
        print("Thank you!")
        print(border)
        end_of_program = True