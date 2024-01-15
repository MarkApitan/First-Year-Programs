#Programming Logic and Design
#Prg6 Shape maker using loop
#January 13, 2023
#Mark Justine L. Apitan
rows = int(4)
border = ("\033[1;35m-----------------------------------------------------\033[0m")
#Welcoe introduction of the program
print(border)
print("\tWelcome to \033[0;32mShape Maker\033[0m program!")
print(border)

#Outer loop of the program so that it will keep running until the user says no in the try again variable
while True:
    #To get the input from the user
    choice = input("Pick a number from 1-4: ")
    print(border)
    
    #to print First shape if the user type 1
    if choice == '1':
        print ("You Picked: ") 
        #To print the top part of the first shape 
        for column in range(rows+1):
            for star in range (column):
                print ('*', end= " ")
            print()  
        #To print the reverse part of the first shape
        for column in range(rows+1):
            for star in range (column, rows+1):
                print ('*', end= " ")
            print()
        print()
    
    #To print second shape if the user type 2
    elif choice == '2':
        print ("You Picked: ")  
        #To print the top part of the second shape 
        for column in range (rows+1):
            for space in range (column, rows+1):
                print (' ', end= " ")
            for star in range (column):
                print ('*', end= " ")
            print()

        #To print the reverse part of the second shape
        for column in range (rows+1):
            for space in range (column):
                print (' ', end= " ")
            for star in range (column, rows+1):
                print ('*', end= " ")
            print() 
        print()

    #To print third shape if the user type 3
    elif choice == '3':
        print ("You Picked: ") 
        #To print the top part of the third shape     
        for column in range (rows+1):
            for star in range (column):
                print ('*', end= " ")
            for space in range (column, rows):
                print (' ', end= " ")
            for space in range (column, rows+1):
                print (' ', end= " ")
            for star in range (column):
                print ('*', end= " ")
            print()
        #To print the middle part of the third shape
        print ('* '*((rows*2)+1))

        #To print the reverse part of the third shape
        for column in range (rows+1):
            for star in range (column, rows):
                print ('*', end= " ")
            for space in range (column +1):
                print (' ', end= " ")
            for space in range (column):
                print (' ', end= " ")
            for star in range (column, rows):
                print ('*', end= " ")
            print()
    #To print exit if the user type 4
    elif choice == '4':
        print ("You picked EXIT!")
    #Print invalid if the user type anything else
    else: 
        print ("\033[0;31mInvalid Input!\033[0m Please enter no. 1-4")     
    print(border)

    #To ask the user if they want to input again
    try_again = input ("Do you want to input again? (yes/no): ") 
    
    if try_again.lower() == "yes":
        print (border)
        print("\tWelcome back to \033[0;32mShape Maker\033[0m program!")
        print (border)
    else:
        print (border)
        print ("\033[0;33mThank you for using the Program!\033[0m")
        print (border)
        break     