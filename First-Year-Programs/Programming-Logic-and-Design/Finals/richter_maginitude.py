def is_float(magnitude):
     try:
        float (magnitude)
        return True
     except ValueError:
        return False
     
end_of_program = False
while end_of_program == False:

    magnitude = input("Enter Richter Magnitude value: ")

    if is_float(magnitude) == True:
        magnitude = float(magnitude)
        if magnitude >= 9.0:
            print ("Causes unbelievable damage")
        elif magnitude >=8.0 and magnitude <9.0:
            print ("Causes Major Distruction")
        elif magnitude >=7.0 and magnitude <8.0:
            print ("Causes damage to most buildings")
        elif magnitude >=6.0 and magnitude <7.0:
            print ("Causes damage to well-built structures")
        elif magnitude >=5.0 and magnitude <6.0:
            print ("Causes damage to poorly  constructed building")
        elif magnitude >=4.0 and magnitude <5.0:
            print ("Damage done to weak buildings")
        elif magnitude >=2.0 and magnitude <4.0:
            print ("Very rarely causes damage")
        elif magnitude >=1.0 and magnitude <2.0:
            print ("Microearthquakes not felt or rarely felt")
        else:
            print ("Invalid! you can't input negative values")
        input_again = input("Do you want to use the program again? (y/n): ")
        if input_again.lower() == "y":
            print ("Welcome back to the program!")
            end_of_program = False
        else: 
            print ("Thank you for using the program!")
            end_of_program = True
    else:
        print ("Invalid input.")
        end_of_program = True