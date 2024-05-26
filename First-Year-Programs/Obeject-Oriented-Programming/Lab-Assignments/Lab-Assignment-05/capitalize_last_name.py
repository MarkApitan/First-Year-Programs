# Define a function capitalize_last_name() that accepts as argument a string with a (single) first and a (single) last name, 
# and returns a string in which only the first letter of the first name is uppercase, whereas all letters of the last name are uppercase; 
# in otherwords, 'marisa tomei' becomes 'Marisa TOMEI'. 
# (Tip: use str.split() to split a str into separate words.)
# If something other than a str object is passed as an argument, the function should raise a TypeError. 
# (Tip: you can use isistance() to check whether an object is of a particular type.) 
# If the str does not consist of exactly two words, the function should raise a ValueError.

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 4 | Problem No. 4 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To define checker that will check if all the characters in the string are letters
def checker(name, test):
    test = name.isalpha()
    return test
def capitalize_last_name(name):
    test = True
    #Split the name
    split_name = name.split(" ")
    try:
        #Check if there are exactly 2 strings
        if len(split_name) == 2: 
            #Check the first name and last name
            first_name = split_name[0]
            test1 = checker(name = first_name, test=test) 
            last_name = split_name[1]
            test2 = checker(name = last_name, test=test)
    
            if test1 and test2 == True:
                # Capitalize the first name and make the last name uppercase
                first_name = first_name[0].upper()+first_name[1:].lower() 
                last_name = last_name.upper()
                #Display the name
                name = (f"Name: {first_name} {last_name}")
                print(name)
            #Raise the Errors
            else: 
                raise TypeError("Please only enter a string")
        else:
            raise ValueError("Enter 1 first name, and 1 last name")
    #Handle the Type Error
    except TypeError as e:
        print (f"TypeError! {e}")
    # Handle ValueError
    except ValueError as e:
        print (f"ValueError! {e}")
    
name = input("Enter your first name and last name: ")
capitalize_last_name(name)