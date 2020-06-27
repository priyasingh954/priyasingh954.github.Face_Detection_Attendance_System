import mysql.connector
import datetime

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='minor_project'
)

mycursor = db.cursor()

now = datetime.datetime.now()
date_to = str(str(now.day)+(now.strftime("%B")+str(now.year)))
# print(date_to)


col = []  # column array
mycursor.execute("SHOW COLUMNS FROM attendance")
for yo in mycursor:
    col.append(yo[0])
    # print(yo[0])

for i in range(len(col)):
    # print(col[i], end=" ")
    print("%-10s" % col[i], end=" ")

mycursor.execute("SELECT * FROM attendance")
allRows = mycursor.fetchall()


for row in allRows:
    print("\n")
    eachrow = []  # taking row element to put in this array

    for j in range(len(col)):
        eachrow.append(row[j])

    for i in range(len(eachrow)):
        print("%-10s" % eachrow[i], end=" ")


db.commit()
db.close()
