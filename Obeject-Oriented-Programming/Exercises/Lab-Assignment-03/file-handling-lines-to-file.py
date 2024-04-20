# Write a method in python to write multiple line of text contents into a text file mylife.txt. 

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 3 | Problem No. 3 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To define variables
end_of_program = False
line_counter = 0

#To open and create mylife.txt
new_line = open("mylife.txt","w")

#To create a loop that will keep on running until the user input end it
while end_of_program != True:
    #To get the input from the user
    line = input("Enter line: ")
    if line_counter == 0:
        #To write the line in mylife.txt
        new_line.write(f"Enter line: {line}")
        line_counter +=1
    else:
        new_line.write(f"\nEnter line: {line}")
        line_counter +=1
    
    #To ask the user if hs/she will write more lines
    input_again = input("Are there more lines y/n? ").lower()

    #To check the input
    if input_again == "y":
        new_line.write(f"\nAre there more lines y/n? {input_again}")
        end_of_program = False
    else:
        new_line.write(f"\nAre there more lines y/n? {input_again}")
        end_of_program = True

#To close mylife.txt
new_line.close()