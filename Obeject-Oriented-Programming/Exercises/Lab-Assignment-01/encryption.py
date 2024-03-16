#Lab Exercise No 1: Problem No. 1
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 9, 2024

border = ("-----------------------------------------------------------------------------------------------------------------------------------")

print("\nProgram Title: Lab Exercise No 1 | Problem No. 1 \nProgrammed by: Mark Justine L. Apitan")
print(border)
#To define the encryption key
encryption_key = {"a": "*",
           "e": "&",
           "i": "#",
           "o": "+",
           "u": "!",
           }

#To get the input from the user
message = input("Enter a string to encrypt: ").lower()

#To define the empty string
new_message = ''

#To check every character in the input using for loop
for char in message:

    #To check if the character is in the encryption key
    if char in encryption_key:
         #if yes, it will replace the character with the corresponding value then add it in the empty string/new message
        new_message += encryption_key[char]
        #if no, it will just add the character directly to the empty string/new message
    else:
        new_message += char

#To display the new message
print(f"Encryted String: {new_message}")
print(border)