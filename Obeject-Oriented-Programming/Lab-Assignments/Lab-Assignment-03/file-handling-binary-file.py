# Write a Python program that read a binary file containing the name of 20 students together with their GWA.  
# The program will output the name of the student who got the highest GWA (including the GWA).

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 3 | Problem No. 4 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To import pickle
import pickle

#To read the binary file
with open('gwa.bin', 'rb') as read:

    student1 = pickle.load(read)
#To get the highest GWA
highest_gwa = min(student1, key = student1.get)
#To print the name of the student with the Gwa
print("The student with highest GWA: ")
print(f"Name: {highest_gwa}") 
print("GWA: {student1[highest_gwa]}")