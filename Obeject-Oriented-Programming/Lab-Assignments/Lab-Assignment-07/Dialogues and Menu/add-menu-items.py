# Lab Exercise No 6
# Programmed by: Mark Justine L. Apitan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: June 15, 2024

from tkinter import *
app = Tk()
app.title("GUI Example 5")
app.geometry("400x400")

my_menu = Menu(app)
app.config(menu=my_menu)

# Create a menu item for "File"
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)

# Create a menu item for "Edit"
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)

# Create a menu item for "About"
about_menu = Menu(my_menu)
my_menu.add_cascade(label="About", menu=about_menu)

app.mainloop()