#Lab Assignment No 2: Problem No. 4
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 24, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 2 | Problem No. 4 \nProgrammed by: Mark Justine L. Apitan")
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