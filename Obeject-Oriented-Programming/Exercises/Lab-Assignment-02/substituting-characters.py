#Lab Exercise No 2: Problem No. 11
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 16, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Exercise No 2 | Problem No. 11 \nProgrammed by: Mark Justine L. Apitan")
print(border)
#To get input from the user
data = input("Enter whatever your like: ").lower()
#To define new string
new_data = ""
#To check all characters
for character in data:

    #To check and replace the vowels
    if character == 'a':
        new_data +='e'
    elif character == 'e':
        new_data += 'i'
    elif character == 'i':
        new_data += 'o'
    elif character == 'o':
        new_data += 'u'
    elif character == 'u':
        new_data += 'a'

    #To check for s
    elif character == 's':
        new_data += '$'
    
    #To check numbers 1-4
    elif character == "1" or character == "2" or character == "3" or character == "4":

        new_character = int(character) *2
        new_data += str(new_character)   
    else:
        new_data+= character

#To make the first character uppercase
new_data2 = new_data[0].upper()+new_data[1:].lower()
print(f"\nNew string: {new_data2}")

print(border)