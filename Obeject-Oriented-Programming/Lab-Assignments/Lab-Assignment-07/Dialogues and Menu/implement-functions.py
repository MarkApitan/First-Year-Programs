# Lab Exercise No 6
# Programmed by: Mark Justine L. Apitan
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: June 15, 2024

from tkinter import *
from tkinter import filedialog, messagebox
import os
# Create the main application window
app = Tk()
app.title("GUI Example 5")
app.geometry("400x400")

# Initialize global variables
current_file_path = None
is_text_changed = False

# Function to open a file
def open_file():
    global current_file_path, is_text_changed
    if is_text_changed:
        if not ask_unsaved_changes():
            return
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        text_area.delete(1.0, END)
        text_area.insert(INSERT, content)
        current_file_path = file_path
        is_text_changed = False
        app.title(f"File: {os.path.basename(file_path)}")

# Function to save a file
def save_file():
    global current_file_path, is_text_changed
    if current_file_path:
        with open(current_file_path, 'w') as file:
            content = text_area.get(1.0, END)
            file.write(content)
        is_text_changed = False
        messagebox.showinfo("Info", "File saved successfully")
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = text_area.get(1.0, END)
                file.write(content)
            current_file_path = file_path
            is_text_changed = False
            app.title(f"File: {os.path.basename(file_path)}")
            messagebox.showinfo("Info", "File saved successfully")

# Function to quit the application
def quit_app():
    if is_text_changed:
        if not ask_unsaved_changes():
            return
    app.quit()

# Function to convert the text to uppercase
def convert_to_upper():
    if not current_file_path:
        messagebox.showerror("Error", "No file is open")
        return
    content = text_area.get(1.0, END)
    upper_content = content.upper()
    text_area.delete(1.0, END)
    text_area.insert(INSERT, upper_content)
    is_text_changed = True

# Function to show help information
def show_help():
    messagebox.showinfo("Help", "Just open a file and edit it, then save.")

# Function to show about information
def show_about():
    messagebox.showinfo("About", "This app will edit a file.")

def ask_unsaved_changes():
    return messagebox.askyesno("Unsaved Changes",
                               "You have unsaved changes. Do you want to discard them?")

def on_text_change(event):
    global is_text_changed
    is_text_changed = True

# Create a Text widget for the main content area
text_area = Text(app, wrap='word')
text_area.pack(expand='yes', fill='both')

# Bind text change event to track changes
text_area.bind("<<Modified>>", on_text_change)

# Create the menu bar
my_menu = Menu(app)
app.config(menu=my_menu)

# Create a menu item for "File"
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)

# Add commands to the "File" menu
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)

# Create a menu item for "Edit"
edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Edit", menu=edit_menu)

# Add commands to the "Edit" menu
edit_menu.add_command(label="Convert to upper", command=convert_to_upper)

# Create a menu item for "About"
about_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="About", menu=about_menu)

# Add commands to the "About" menu
about_menu.add_command(label="Help", command=show_help)
about_menu.add_command(label="About", command=show_about)

app.mainloop()
