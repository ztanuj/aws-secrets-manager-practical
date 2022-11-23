import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.ckhkluatkbwl.ap-south-1.rds.amazonaws.com",
  user="admin",
  password="Temp1234",
  database="testdb"
)

mycursor = mydb.cursor() 

mycursor.execute("SELECT * FROM Persons")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

