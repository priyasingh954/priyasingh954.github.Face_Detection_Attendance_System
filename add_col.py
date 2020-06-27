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
print(date_to)

#mycursor.execute("ALTER TABLE attendance ADD "+date_to+" VARCHAR(7)")

#sql = "ALTER TABLE attendance ADD %s VARCHAR(10)"
#values = date_to
#date_to = input("enter date: ")
#values = date_to
#mycursor.execute(sql % values)


sql = "ALTER TABLE attendance DROP COLUMN %s"
values = date_to
mycursor.execute(sql % values)

#mycursor.execute("SELECT * FROM attendance")
#all_rows = mycursor.fetchall()
#cmd = "UPDATE attendance SET %s = 'None'"
#value = date_to
#mycursor.execute(cmd % value)

#mycursor.execute("SHOW COLUMNS FROM attendance")
#for yo in mycursor:
#    print(yo[0])

db.commit()
db.close()
