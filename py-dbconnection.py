import mysql.connector

#For Localhost
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="py-db1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM persons")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
