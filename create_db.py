import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="root1234")
print(db)
db.close()