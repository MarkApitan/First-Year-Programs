#Lab Exercise No 6
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: June 15, 2024
from tkinter import *
app = Tk()
app.title('GUI Example 3')

# Left frame
left_frame = Frame(app, bd=5, relief="groove")
left_frame.pack(side=LEFT, fill="both", expand=True)

# Right frame
right_frame = Frame(app, bd=5, relief="groove")
right_frame.pack(side=RIGHT, fill="both", expand=True)

# Labels in the left frame
label_a = Label(left_frame, bg='blue', text='A')
label_a.pack(fill="both", expand=True)
label_b = Label(left_frame, text='B')
label_b.pack(fill="both", expand=True)

# Labels in the right frame
label_c = Label(right_frame, text='C')
label_c.pack(fill="both", expand=True)
label_d = Label(right_frame, bg='blue', text='D')
label_d.pack(fill="both", expand=True)

app.mainloop()