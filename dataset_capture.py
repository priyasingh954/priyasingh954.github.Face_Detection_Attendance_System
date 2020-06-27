# Import OpenCV2 for image processing
import cv2
import os
face_id = 0


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


# ----------------------------------------------

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
    # inserting name and rollno into table
    sql = "insert into attendance(name, rollno)" \
          "values('%s','%s')"
    values = (e1.get(), e2.get())
    mycursor.execute(sql % values)
    db.commit()

    print("details inserted successfully!!!")
    print("Press Quit and the camera will take your pictures in a few seconds")

    # fetch id from table
    sql1 = "select id from attendance where rollno=%d"
    values = int(e2.get())
    mycursor.execute(sql1 % values)
    global face_id
    face = mycursor.fetchone()
    face_id = face[0]
    # print(face_id)


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

# ------------------------------------------------
# Start capturing video
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('D:/AAAproject/haarcascade_frontalface_default.xml')

# Initialize sample face image
count = 0

assure_path_exists("D:/AAAproject/faces/faces.")

# Start looping
while True:

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x, y, w, h) in faces:
        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("D:/AAAproject/faces/faces." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count >= 30:
        print("Successfully Captured")
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
