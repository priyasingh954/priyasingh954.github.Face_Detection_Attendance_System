# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:34:45 2020

@author: KIIT
"""

import cv2
import datetime
# import numpy as np
# import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('D:/AAAproject/trainer/trainer.yml')  # load trained model
cascadePath = "D:/AAAproject/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX


import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='minor_project'
)

mycursor = db.cursor()

names = [' ', ]  # key in names, start from the second place, leave first empty

# update names array
mycursor.execute("SELECT * FROM attendance")
allRows = mycursor.fetchall()
for row in allRows:
    names.append(row[1])

# just to check if the names array is being appended or not
# for x in range(len(names)):
#    print(names[x])

id = len(names)-1  # total nos of ids in the table

# Taking current date
now = datetime.datetime.now()
date_to = str(str(now.day)+(now.strftime("%B")+str(now.year)))
# print(date_to)


col = ["id", "name", "rollno", ]  # column array
flag = 0
mycursor.execute("SHOW COLUMNS FROM attendance")
for ch in mycursor:
    if date_to == ch[0]:
        flag = flag+1
        break
    else:
        flag = 0

if flag == 0:
    # Adding new column as current date
    sql = "ALTER TABLE attendance ADD %s VARCHAR(10)"
    value = date_to
    mycursor.execute(sql % value)
    col.append(date_to)
    cmd = "UPDATE attendance SET %s = 'A'"
    values = date_to
    mycursor.execute(cmd % values)


db.commit()
db.close()


present = set()  # ids that are captured whilst recognition are termed as present, set cuz unique elements


# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:

    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if confidence < 100:
            present.add(id)
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()

##################################


# putting P in front of the ids that are present
def put_present():
    db1 = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='minor_project'
    )

    cursor = db1.cursor()
    print(present)
    for i in present:

        cmd_p = "UPDATE attendance SET %s = 'P' WHERE id = %d"
        val = (date_to, i)
        cursor.execute(cmd_p % val)

    db1.commit()
    db1.close()


put_present()
