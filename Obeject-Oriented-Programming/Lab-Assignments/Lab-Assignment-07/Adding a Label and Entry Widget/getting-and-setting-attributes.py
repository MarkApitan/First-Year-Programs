# Import the tkinter package
#	Note in Python 3 it is all lowercase
from tkinter import *

# This method is called when the button is pressed
def clicked():
    current_label = label.cget("text")
    if current_label == "Text is displayed here":
        label.config(text="You changed the text")
    else:
        label.config(text="Text is displayed here")
    
# Create a main frame with
#	-- a title
#	-- size 200 by 200 pixels
app = Tk()
app.title("GUI Example 2.1") 
app.geometry('200x200')
# Create the button with
#	-- suitable text
#	-- a command to call when the button is pressed

button1 = Button(app, text="Copy Text", command=clicked)

# Make the button visible at the bottom of the frame
button1.pack(pady=5)

label = Label(app, text="Text is displayed here")
label.pack(pady=10)
# Start the application running
app.mainloop()