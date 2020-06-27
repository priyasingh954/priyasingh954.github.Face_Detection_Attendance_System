import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='minor_project'
)

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE MINOR_PROJECT")
#mycursor.execute("SHOW TABLES")
#for db1 in mycursor:
#    print(db1)

#mycursor.execute("CREATE TABLE attendance("
#                 "id INT AUTO_INCREMENT PRIMARY KEY, "
#                 "name VARCHAR(20), "
#                 "rollno NUMERIC(7));"
#                 )

#mycursor.execute("DROP TABLE attendance")
#for db1 in mycursor:
#    print(db1)

db.commit()

# mycursor.execute("DELETE FROM attendance WHERE rollno='1112223'")
# db.commit()

db.close()
