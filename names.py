import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='minor_project'
)

mycursor = db.cursor()

names = [' ', ]  # key in names, start from the second place, leave first empty

mycursor.execute("SELECT * FROM attendance")
allRows = mycursor.fetchall()
for row in allRows:
    names.append(row[1])

for x in range(len(names)):
    print(names[x])

id = len(names)-1
