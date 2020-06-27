from tkinter import *


def generate_report():
    import display


def add_student():
    import dataset_capture
    import train


def take_attendance():
    import recognisation


topWindow = Tk()

# topWindow.eval('tk::PlaceWindow %s center' % topWindow.winfo_pathname(topWindow.winfo_id()))

l1 = Label(topWindow, text="ADMIN")

b1 = Button(topWindow, text='Generate Report', command=generate_report)
b2 = Button(topWindow, text='Add Student', command=add_student)
b3 = Button(topWindow, text='Take Attendance', command=take_attendance)
b4 = Button(topWindow, text='Exit', command=topWindow.quit)

l1.grid(row=0, column=0, sticky=W)

b1.grid(row=3, column=0, sticky=W, pady=5)
b2.grid(row=4, column=0, sticky=W, pady=5)
b3.grid(row=5, column=0, sticky=W, pady=5)
b4.grid(row=6, column=0, sticky=W, pady=5)

topWindow.mainloop()
