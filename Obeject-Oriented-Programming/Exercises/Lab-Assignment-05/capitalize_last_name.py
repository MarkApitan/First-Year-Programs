#Lab Assignment No 5: Problem No. 4
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 24, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 5 | Problem No. 4 \nProgrammed by: Mark Justine L. Apitan")
print(border)

def checker(name, test):
    test = name.isalpha()
    return test
def capitalize_last_name():
    test = True
    name = input("Enter your first name and last name: ")
    split_name = name.split(" ")
    
    if len(split_name) == 2: 
        
        first_name = split_name[0]
        test1 = checker(name = first_name, test=test)
        
        last_name = split_name[1]
        test2 = checker(name = last_name, test=test)
  
        if test1 and test2 == True:
            first_name = first_name[0].upper()+first_name[1:].lower()
                
            last_name = last_name.upper()
                
            name = (f"Name: {first_name} {last_name}")
            print(name)
        else: 
            print("TypeError! Please only enter a string")

    else:
        print("ValueError! Enter 1 first name, and 1 last name")

capitalize_last_name()