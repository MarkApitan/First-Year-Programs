#Lab Exercise No 1: Problem No. 3
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 9, 2024
border = ("-----------------------------------------------------------------------------------------------------------------------------------")

print("\nProgram Title: Lab Exercise No 1 | Problem No. 3 \nProgrammed by: Mark Justine L. Apitan")
print(border)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
message = input("Enter a message to Cipher: (all uppercase letters, no  spaces) ").upper()
key = input("Enter key to word: (all  uppercase  letters) ").upper()
real_message = message.replace(' ', '')
real_key = key.replace(' ', '')
length_of_message = len(message)

#To turn message into numbers
encrypt_message = []
for letter in real_message:
    index = alphabet.index(letter)
    encrypt_message.append(index)

#To make the lenght of message = lenght of key
new_key = (real_key *((length_of_message//len(real_key))+1))[:length_of_message]

#To turn new key into numbers
encrypt_new_key = []
for letter in new_key:
    index = alphabet.index(letter)
    encrypt_new_key.append(index)

#To get the added values
added_values = []
for number in range(0, length_of_message):
    add = encrypt_message[number] + encrypt_new_key[number]
    added_values.append(add)

#To get the mod values
mod_list = []
for number in (added_values):
    if number >=26:
        mod_value = number-26
        mod_list.append(mod_value)
    else: 
        mod_list.append(number)

#To get the ciphertext
ciphertext = ""
for number in (mod_list):
    ciphertext_value = alphabet[number]
    ciphertext+=ciphertext_value

#To display the output
print (f"Message: {real_message} {encrypt_message}")
print (f"Key: {key} {encrypt_new_key}")
print (f"Add: {added_values}")
print (f"Mod: {mod_list}")
print (f"Ciphertext: {ciphertext}")
print (border)