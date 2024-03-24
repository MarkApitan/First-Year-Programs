#Lab Assignment No 2: Problem No. 1
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted:March 24, 2024

#Introduction 
border = ("-----------------------------------------------------------------------------------------------------------------------------------")
print("\nProgram Title: Lab Assignment No 2 | Problem No. 1 \nProgrammed by: Mark Justine L. Apitan")
print(border)

#To define variables
number_list = []
even_list = []
odd_list = []
even_counter = 0
odd_counter = 0

#To get the input from the user about the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

#To create a for loop that will append numbers 1-20 into the number_list
for x in range (start,end+1):
    number_list.append(x)

#To create number.txt, write in it the number_list and then close it
numbers = open("number.txt","w")
numbers.write(str(number_list))
numbers.close()

#To create a for loop that will check every item in the number_list
for x in number_list:
    #To check if the item is even or odd and then append it to odd_list or even_list
    if int(x) % 2 ==0:
        even_list.append(x)
        even_counter += 1
    else:
        odd_list.append(x)
        odd_counter += 1

#To create even,txt. And then write in it the even_list and show the total number of even numbers, and then close it
even = open("even.txt", "w")
even.write(str(even_list))
even.write(f"\nThe total number of even numbers {even_counter}")
even.close

#To create odd.txt. And then write in it the odd_list and show the total number of odd numbers, and then close it
odd = open("odd.txt", "w")
odd.write(str(odd_list))
odd.write(f"\nThe total number of odd numbers {odd_counter}")
odd.close