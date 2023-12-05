#Programming Logic and Design
#Prg4 compute for final grade and turn it into a GPA scale system
#December 5, 2023
#Mark Justine L. Apitan

#This program will compute for the final grade of a student and turn it into a GPA Scale System

#To get the student lecture activities scores/grade
lecture_quiz = float(input("Enter your Lecture Quiz Grade: "))
lecture_assign = float(input("Enter your Lecture Assignment Activity Grade: "))
lecture_project = float(input("Enter your Lecture Project Grade: "))
lecture_recitation = float(input("Enter your Lecture Rectation Grade: "))

#To get the student laboratory activities scores/grade
laboratory_quiz = float(input("Enter your Laboratory Quiz Grade: "))
laboratory_assign = float(input("Enter your Laboratory Assignment Activity Grade: "))
laboratory_project = float(input("Enter your Laboratory Project Grade: "))
laboratory_recitation = float(input("Enter your Laboratory Rectation Grade: "))

#To get the student midterm and final score/grade
midterm = float(input("Enter your Midterm Grade: "))
final = float(input ("Enter your Final Grade: "))

#To compute for the student's final grade
lecture_final = ((lecture_quiz *.25) + (lecture_assign * .15) + (lecture_project * .15) + (lecture_recitation * .10) + (((midterm + final) * .35)/2))
laboratory_final = ((laboratory_quiz *.25) + (laboratory_assign * .15) + (laboratory_project * .15) + (laboratory_recitation * .10) + (((midterm + final) * .35)/2))

gwa = ((lecture_final* .70) + (laboratory_final*.30))

#To turn into a gwa system and display the GWA and the remark whether passed or failed
if gwa > 100 or gwa < 1:
    print ("Error")
elif gwa >= 96.5:
    print ("\nGWA:\033[0;33m 1.00")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
elif gwa >= 93.5:
    print ("\nGWA:\033[0;33m 1.25")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
elif gwa >= 90.5:
    print ("\nGWA:\033[0;33m 1.50")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
elif gwa >= 87.5:
    print ("\nGWA:\033[0;33m 1.75")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
elif gwa >= 84.5:
    print ("\nGWA:\033[0;33m 2.00")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
elif gwa >= 81.5:
    print ("\nGWA:\033[0;33m 2.25")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
elif gwa >= 78.5:
    print ("\nGWA:\033[0;33m 2.50")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
elif gwa >= 75.5:
    print ("\nGWA:\033[0;33m 2.75")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
elif gwa >= 74.5:
    print ("\nGWA:\033[0;33m 3.00")
    print ("\033[0mRemark:\033[0;32m Passed \033[0m")
else:
    print ("\nGWA:\033[0;33m 5.00")
    print ("\033[0mRemark:\033[0;31m Failed \033[0m")