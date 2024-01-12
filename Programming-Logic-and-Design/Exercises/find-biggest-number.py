#Helped maica with her assignment :>>
#Assignment: Ask the user to input 3 numbers. Find and print the biggest number using only if-else statement.

# adding window
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title ("Highest Number Finder")
root.geometry ("540x660")
root.resizable (False, False) 
bg_color = "#C1ECEA"

# variables
num1_input = StringVar ()
num2_input = StringVar ()
num3_input = StringVar ()
highest_number = StringVar()

def is_float(num1,num2,num3):
     try:
        float (num1)
        float (num2)
        float (num3)
        return True
     except ValueError:
          return False

def submit():
    num1 = str(num1_input.get())
    num2 = str(num2_input.get())
    num3 = str(num3_input.get())
    
    if is_float(num1,num2,num3) == False:
        messagebox.showerror ("Error.", "Please input a number.")

    elif num1_input.get()==0 or num2_input.get()==0 or num3_input.get()==0:
        messagebox.showerror ("Error.", "Please input a number.")
        
    else:
        n1 = float(num1)
        n2 = float(num2)
        n3 = float(num3)
        if n1 >= n2 and n1 >= n3:
            highest_number.set(num1)
        elif n2 >= n1 and n2 >= n3:
            highest_number.set(num2)
        else:
            highest_number.set(num3)
            
def exit():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

def reset():
    num1_input.set(0)
    num2_input.set(0)
    num3_input.set(0)
    highest_number.set(0)

# creating widgets
# title widget
title = Label (root, text = "Highest Number Finder", font=("STIX", 20, "bold"), fg="#F63392", bg="#C1ECEA", relief=GROOVE, bd=10)
title.pack (fill=X)

# creating widgets

# adding widgets for entry or inputs
# title: input number
input_number=Label(root, text = "Input a Number", font=("STIX", 20, "bold"), fg="#F63392", bg="#EED3E1", relief=GROOVE, bd=7)
input_number.place(x=5, y=55, width=520, height=65)


# for inputting numbers
input_num=LabelFrame(root, bg="#EED3E1", relief=GROOVE, bd=7)
input_num.place(x=5, y=120, width=520, height=240)

number1=Label(input_num, text=" 1st Number:", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
number1.grid(row=1, column=0, padx=20, pady=15)
number1=Entry (input_num, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable = num1_input)
number1.grid (row=1, column=1, padx=20, pady=15)
number2=Label(input_num, text="2nd Number:", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
number2.grid(row=2, column=0, padx=20, pady=15)
number2=Entry (input_num, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable = num2_input)
number2.grid (row=2, column=1, padx=20, pady=15)
number3=Label(input_num, text="3rd Number:", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
number3.grid(row=3, column=0, padx=20, pady=15)
number3=Entry (input_num, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable = num3_input)
number3.grid (row=3, column=1, padx=20, pady=15)

# result
get_result=LabelFrame(root, text = "Highest Number", font=("STIX", 20, "bold"), fg="#F63392", bg="#EED3E1", relief=GROOVE, bd=7)
get_result.place(x=5, y=360, width=520, height=120)

result=Label(get_result, text="Result:", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
result.grid(row=1, column=0, padx=20, pady=15)
result=Entry (get_result, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=highest_number)
result.grid(row=1, column=1, padx=90, pady=15)
# adding buttons

button=Frame(root)
button.place(x=5,y=480, width=515, height=200)

submit_button=Button (button, text="Submit", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", justify=CENTER, width=30, command=submit)
submit_button.grid(row=0, column=0, columnspan=5, padx=1, pady=1)

reset_button=Button (button, text="Reset", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", justify=CENTER, width=30, command = reset)
reset_button.grid(row=1, column=0, columnspan=5, padx=1, pady=1)

exit_button=Button (button, text="Exit", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", justify=CENTER, width=30, command=exit)
exit_button.grid(row=2, column=0, columnspan=5, padx=1, pady=1)
root.mainloop()