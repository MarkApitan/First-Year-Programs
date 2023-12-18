num = input("Enter a Number: ")
index = num.count('-')
 #to check if the inputs are valid
if index ==1:
    float(num)
    if int(num)%2==0:
                    #To get the sum of all even numbers
        print ("even")
    else:
    #To get the sum of all odd numbers
            print ("odd")
else:
    print("Invalid")

def is_float(num):
     try:
        float (num)
        return True
     except ValueError:
          return False
print (is_float(num))