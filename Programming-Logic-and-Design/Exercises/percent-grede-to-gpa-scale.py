#Programming Logic and Design
#Prg4 compute for final grade and turn it into a GPA scale system
#December 5, 2023
#Mark Justine L. Apitan

#This program will compute for the final grade of a student and turn it into a GPA Scale System

#To get student information
first_name = (input("Enter your First Name: "))
last_name = (input("Enter Your Last Name: "))

#To get the student lecture activities scores/grade
print ("\nGood Day, "+ first_name + "! Please enter your grades out of 100")
print ("-------------------------------------------------")
lecture_quiz = float(input("Enter your Lecture Quiz Grade: "))
lecture_assign = float(input("Enter your Lecture Assignment Activity Grade: "))
lecture_project = float(input("Enter your Lecture Project Grade: "))
lecture_recitation = float(input("Enter your Lecture Rectation Grade: "))
lecture_midterm = float(input("Enter your Midterm Grade: "))
lecture_final = float(input ("Enter your Final Grade: "))

#To check if theres an invalid input in lecture inputs, to check if theres value greater than 100 or less than 0
if lecture_quiz >100 or lecture_quiz < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if lecture_assign >100 or lecture_assign < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if lecture_project >100 or lecture_project < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if lecture_recitation >100 or lecture_recitation < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if lecture_midterm >100 or lecture_midterm < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if lecture_final >100 or lecture_final < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
    
#To get the student laboratory activities scores/grade
print ("-------------------------------------------------")
laboratory_quiz = float(input("Enter your Laboratory Quiz Grade: "))
laboratory_assign = float(input("Enter your Laboratory Assignment Activity Grade: "))
laboratory_project = float(input("Enter your Laboratory Project Grade: "))
laboratory_recitation = float(input("Enter your Laboratory Rectation Grade: "))
laboratory_midterm = float(input("Enter your Midterm Grade: "))
laboratory_final = float(input ("Enter your Final Grade: "))

#To check if theres an invalid input in laboratory inputs
if laboratory_quiz >100 or laboratory_quiz < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if laboratory_assign >100 or laboratory_assign < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if laboratory_project >100 or laboratory_project < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if laboratory_recitation >100 or laboratory_recitation < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if laboratory_midterm >100 or laboratory_midterm < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()
if laboratory_final >100 or laboratory_final < 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()

#To compute for the student's final grade, to check if theres value greater than 100 or less than 0
lecture_final = ((lecture_quiz *.25) + (lecture_assign * .15) + (lecture_project * .15) + (lecture_recitation * .10) + (((lecture_midterm + lecture_final)/2)*.35))
laboratory_final = ((laboratory_quiz *.25) + (laboratory_assign * .15) + (laboratory_project * .15) + (laboratory_recitation * .10) + (((laboratory_midterm + laboratory_final)/2)*.35))

gwa = ((lecture_final* .70) + (laboratory_final*.30))

#To check gwa
if gwa > 100 or gwa <= 0:
    print ("-------------------------------------------------")
    print ("\033[0;31mInvalid Input \033[0m")
    exit()

#To display student name
print ("-------------------------------------------------")
print ("Name:",first_name,last_name)

#To turn into a gwa system and display the GWA and the remark whether passed or failed
if gwa >= 96.5:
    print ("GWA:\033[0;33m 1.00")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
    print ("Congratulations,",first_name, "! you passed!!")
elif gwa >= 93.5:
    print ("GWA:\033[0;33m 1.25")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
    print ("Congratulations,",first_name, "! you passed!!")
elif gwa >= 90.5:
    print ("GWA:\033[0;33m 1.50")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
    print ("Congratulations,",first_name, "! you passed!!")
elif gwa >= 87.5:
    print ("GWA:\033[0;33m 1.75")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
    print ("Congratulations,",first_name, "! you passed!!")
elif gwa >= 84.5:
    print ("GWA:\033[0;33m 2.00")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
    print ("Congratulations,",first_name, "! you passed!!")
elif gwa >= 81.5:
    print ("GWA:\033[0;33m 2.25")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
    print ("Congratulations,",first_name, "! you passed!!")
elif gwa >= 78.5:
    print ("GWA:\033[0;33m 2.50")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
    print ("Congratulations,",first_name, "! you passed!!")
elif gwa >= 75.5:
    print ("GWA:\033[0;33m 2.75")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
    print ("Congratulations,",first_name, "! you passed!!")
elif gwa >= 74.5:
    print ("GWA:\033[0;33m 3.00")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
    print ("Congratulations,",first_name, "! you passed!!")
else:
    print ("GWA:\033[0;33m 5.00")
    print ("\033[0mRemark:\033[0;31m Failed \033[0m")