# You're going to write an interactive calculator! 
# User input is assumed to be a formula that consist of a number, an operator (at least + and -), 
# and another number, separated by white space (e.g. 1 + 1). 
# Split user input using str.split(), and check whether the resulting list is valid:
# If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception. 
# Try to convert the first and third input to a float (like so: float_value = float(str_value)). 
# Catch any ValueError that occurs, and instead raise a FormulaError.  
# If the second input is not '+' or '-', again raise a FormulaError. 
# If the input is valid, perform the calculation and print out the result. 
# The user is then prompted to provide new input, and so on, until the user enters quit.

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 4 | Problem No. 3 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To define the formula error
def FormulaError(split_equation, operations):
    #Check if the len of equation = 3
    if len(split_equation) == 3:

        #Check if the 2nd input are in operations
        if split_equation[1] not in operations: 
            print("Formula Error! Please enter a valid operation")
            test =  False
        #Check if the 1st and 3rd input is convertible to float
        else:
            try:
                float(split_equation[0])
                float(split_equation[2])
                test =  True
            except ValueError:
                print("Formula Error! Please enter valid integers")
                test = False                
    else:
        print("Formula Error!")
        test = False 
    return test

#Define the re_enter function that will ask the user if they want to input again
def re_enter(end): 
    input_again = input("Do you want to input again? type 'yes' if you want to input again, type 'quit' if no: ")
    if input_again.lower() == "quit":
        print("Thank you!")
        end = True  
    return end    

#Define computations
def computations(operation, float_value1, float_value2, equation, result): 
    #Check the operation, compute, and then print the result
    if operation == "+":
        result = (float_value1 + float_value2)
    elif operation == "-":
        result = (float_value1 - float_value2)
    elif operation == "*" or operation == "x":
        result = (float_value1 * float_value2)    
    elif operation == "/" :
        result = (float_value1 / float_value2)
    print(f"{equation} = {result}")
                            
#Define the main part of the program
def main ():
    #Define Variable
    operations = ['+', '-', '*', 'x', '/']
    end = False
    #Create a loop for the program
    while end != True:
        result = 0
        #Ask the user for the input
        equation = input("Enter an equation: ")
        #Split the input
        split_equation = equation.split(" ")
        #To check if there are errors in the input
        test = FormulaError(split_equation, operations)
        #Check if the input passed and there are no errors
        if test == True:
            #Assigned variables, and then call the computations function, then call the re_enter function to ask the user 
            operation = split_equation[1]
            float_value1=float(split_equation[0])
            float_value2=float(split_equation[2])
            computations(operation, float_value1, float_value2, equation, result)
            end = re_enter(end)
        else:
            end = re_enter(end)
main()