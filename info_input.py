import mysql.connector
from tkinter import *


def show():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='minor_project'
    )

    mycursor = db.cursor()
    sql = "insert into attendance(name, rollno)" \
          "values('%s','%s')"

    values = (e1.get(), e2.get())

    mycursor.execute(sql % values)

    db.commit()

    print("details inserted successfully!!!")

    # fetch id from table
    sql1 = "select id from attendance where rollno=%d"
    values = int(e2.get())
    mycursor.execute(sql1 % values)
    face_id = mycursor.fetchone()
    print(face_id)
    print(type(face_id))


topWindow = Tk()

# topWindow.eval('tk::PlaceWindow %s center' % topWindow.winfo_pathname(topWindow.winfo_id()))

l1 = Label(topWindow, text="Enter Name")
l2 = Label(topWindow, text="Enter Roll No.")

e1 = Entry(topWindow)
e2 = Entry(topWindow)


b1 = Button(topWindow, text='Quit', command=topWindow.quit)
b2 = Button(topWindow, text='Save', command=show)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0, sticky=W)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1.grid(row=8, column=0, pady=10)
b2.grid(row=8, column=1, pady=10)

topWindow.mainloop()
