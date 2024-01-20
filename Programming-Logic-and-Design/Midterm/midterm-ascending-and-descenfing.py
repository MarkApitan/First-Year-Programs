num1 = (input("Enter First Number: "))
num2 = (input("Enter second number: "))
num3 = (input("Enter third number: "))

letter = input("Enter a letter: ")

def is_int(num1,num2,num3):
    try:
        int(num1)
        int(num2)
        int(num3)
        return True
    except ValueError:
        return False
    
if is_int(num1,num2,num3) == False:
    print("Invalid Input! Please Enter a number")
    exit()
elif letter.lower() == "a":
    n1 = int(num1)
    n2 = int(num2)
    n3 = int(num3)

    if n1 >= n2 and n1 >= n3:
        first = n1
    elif n2 >= n1 and n2 >= n3:
        first = n2
    elif n3 >= n1 and n3 >= n2:
        first = n3
    first = int(first)

    if n1 <= first and n1 >= n3:
        second = n1
    elif n1 <= first and n1 >= n2:
        second = n1
    elif n2 <= first and n2 >= n3:
        second = n2
    elif n2 <= first and n2 >= n1:
        second = n2
    elif n3 <= first and n3 >= n2:
        second = n3
    elif n3 <= first and n3 >= n1:
        second = n3
    second = int(second)

    if n1 <= second:
        third = n1
    elif n2 <= second:
        third = n2
    elif n3 <= second:
        third = n3
    print (f"Ascending Order: {third}, {second}, {first}")
    print (f"Descending Order: {first}, {second}, {third}")
else:
    print("Invalid")
