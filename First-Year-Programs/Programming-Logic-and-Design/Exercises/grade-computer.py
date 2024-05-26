#Programming Logic and Design
#Prg2 Final Grade Computer
#November 26, 2023
#Mark Justine L. Apitan

#This program will compute for the final grade of a student

#To get the student's lecture grade and lab grade

lecture = float(input("Enter your Lecture Grade: "))
lab = float(input("Enter your Laboratoy Grade: "))

#To compute for the final grade

final = ((lecture * .70) + (lab * .30))

#To display the student's final grade and round of to 2 decimal places
#Added yellow color for final grade

print ("\nYour Final Grade is\033[0;33m", round(final, 2), "\033[0m")
