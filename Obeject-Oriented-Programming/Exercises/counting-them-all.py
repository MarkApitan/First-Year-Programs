#Lab Exercise No 1: Problem No. 4
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 9, 2024

border = ("-----------------------------------------------------------------------------------------------------------------------------------")

print("\nProgram Title: Lab Exercise No 1 | Problem No. 4 \nProgrammed by: Mark Justine L. Apitan")
print(border)
#To get the user input
user_input = input("Enter a message: ")

#To define the vowels
vowel = ["a", "e", "i", "o", "u"]

#To define the consonants
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

#To define the numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#To define the number of vowels = 0
num_of_vowels = 0

#To define the number of consonants = 0
num_of_consonants = 0

#To define the number of digits = 0
num_of_digits = 0

#To define the number of special characters = 0
num_of_special_charaters = 0

#To define the total number of characters = 0
total = 0

#To check each character in the user input using for loop
for char in user_input.lower():

    #To check if the character is a vowel
    if char in vowel:
        #if yes, it will add one to the variable num_of_vowels
        num_of_vowels += 1
        total+=1
    #to check if the character is a consonant
    elif char in consonants:
        #if yes, it will add one to the variable num_of_consonants
        num_of_consonants += 1
        total+=1
    #To chech if the character is a number
    elif char in numbers:
        #if yes, it will add one to the  variable num_of_digits
        num_of_digits += 1
        total+=1
    #Everthing that was not catch will be count as special characters
    else:
        #it will add one to the variable num_of_special_characters
        num_of_special_charaters += 1
        total+=1

#To display the output
print (f"Number of vowels: {num_of_vowels}")
print (f"Number of consonants: {num_of_consonants}")
print (f"Number of digits: {num_of_digits}")
print (f"Number of Special characters: {num_of_special_charaters}")
print (f"Total number of characters found on the string: {total}")
print(border)