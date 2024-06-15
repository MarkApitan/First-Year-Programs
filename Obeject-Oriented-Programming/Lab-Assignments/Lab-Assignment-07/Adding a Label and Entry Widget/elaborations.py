#Lab Exercise No 6
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: June 15, 2024

# Import the Tkinter package
#	Note in Python 3 it is all lowercase
from tkinter import *

# This method is called when the button is pressed
def clicked():
    input_text = enter.get()
    if input_text == "":
        button1.config(bg = 'red')
    else:
        button1.config(bg = 'white')
        label.config(text=input_text)

# Create a main frame with
#	-- a title
#	-- size 200 by 200 pixels
app = Tk()
app.title("GUI Example 2.2") 
app.geometry('200x200')

# Create the button with
#	-- suitable text
#	-- a command to call when the button is pressed
enter = Entry(app)
enter.pack(pady=10)

button1 = Button(app, text="Copy Text", bg = 'white',  command=clicked)

# Make the button visible at the bottom of the frame
button1.pack(pady=5)

label = Label(app, text="Text is displayed here")
label.pack(pady=10)

# Start the application running
app.mainloop()