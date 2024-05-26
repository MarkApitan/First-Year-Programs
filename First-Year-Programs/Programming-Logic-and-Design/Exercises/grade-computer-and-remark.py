#Programming Logic and Design
#Prg3 Final Grade Computer abd determine whether the student passed or failed
#November 26, 2023
#Mark Justine L. Apitan

#This program will compute for the final grade of a student and determine whether the student passed or failed

#To get the student's lecture grade and lab grade

lecture = float(input("Enter your Lecture Grade: "))
lab = float(input("Enter your Laboratoy Grade: "))

#To compute for the final grade

final = ((lecture * .70) + (lab * .30))

#To display the student's final grade and round of to 2 decimal places, and check whether the student passed or failed
#Added color for final grade and remark, yellow for final grade, green for passed, and red for failed

if final >= 75:
    print ("\nFinal Grade:\033[0;33m", round(final, 2))
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
else:
    print ("\nFinal Grade:\033[0;33m", round(final, 2))
    print ("\033[0mRemark:\033[0;31m Failed \033[0m")
