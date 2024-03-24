#Lab Assignment No 2: Problem No. 4
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 24, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 2 | Problem No. 4 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To define the lists
integer_list = []
even_list = []
double_list = []
odd_list = []
triple_list = []

#To get the input from the user about the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

#To create a for loop that will append numbers into the integer_list
for x in range (start,end+1):
    integer_list.append(x)

#To create integer.txt, write in it the integer_list and then close it
integer = open("integer.txt","w")
integer.write(str(integer_list))
integer.close()

#To create a for loop that will check each item in the integer list
for x in integer_list:
    #To check if the item is even or odd
    if int(x) % 2 ==0:
        #To double the even numbers and append it to double_list
        even_list.append(x)
        double_x = x ** 2
        double_list.append(double_x)
    else:
        #To tripple the odd numbers and append it to triple_list
        odd_list.append(x)
        triple_x = x ** 3
        triple_list.append(triple_x)
        
#To create double.txt, write in it the double_list and then close it
double = open("double.txt", "w")
double.write(str(even_list))
double.write(str(f"\n{double_list}"))
double.close

#To create triple.txt, write in it the triple_list and then close it
triple = open("triple.txt", "w")
triple.write(str(odd_list))
triple.write(str(f"\n{triple_list}"))
triple.close