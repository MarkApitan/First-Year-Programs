#Lab Exercise No 6
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: June 15, 2024

from tkinter import *

app = Tk()
app.title("GUI Example 4")
app.geometry("500x500")

def key_press(event):
    # Print the character that was pressed
    print(f"{event.char} pressed")

def get_coordinates(event):
    # Print the coordinates of the mouse click
    print(f"Mouse clicked at x = {event.x} y = {event.y}")

def create_square(event):
    global color, filling
    # Create a square at the mouse click position
    my_canvas.create_rectangle(event.x, event.y, event.x + 100, event.y + 100, outline='black', fill=filling)
    print("s key pressed")

def create_circle(event):
    global color, filling
    
    radius = 50
    # Create a circle at the mouse click position
    my_canvas.create_oval(event.x - radius, event.y - radius, event.x + radius, event.y + radius, outline='black', fill=filling)
    print("c key pressed")

def set_filled(event):
    global color, filling
    
    # Set the filling color to the current color
    filling = color
    print("F key pressed")

def set_unfilled(event):
    global filling  
    # Set the filling color to blue
    filling = 'blue'
    print("f key pressed")

def set_yellow(event):
    global color
    # Set the color to yellow
    color = 'yellow'
    print("y key pressed")

def set_red(event):
    global color
    # Set the color to red
    color = 'red'
    print("r key pressed")

color = 'blue'
filling = 'blue'
my_canvas = Canvas(app, width=500, height=500, bg="blue")
my_canvas.pack()
my_canvas.focus_set()

#

app.bind("<KeyPress-s>", create_square)
app.bind("<KeyPress-c>", create_circle)
app.bind("<KeyPress-F>", set_filled)
app.bind("<KeyPress-f>", set_unfilled)
app.bind("<KeyPress-y>", set_yellow)
app.bind("<KeyPress-r>", set_red)
app.bind("<Button-1>", get_coordinates)
app.bind("<KeyPress>", key_press)

app.mainloop()