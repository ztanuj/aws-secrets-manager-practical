import mysql.connector
import boto3
import json

client = boto3.client('secretsmanager')

response = client.get_secret_value(
    SecretId='dev/myapp/secret'
)

secretDict = json.loads(response['SecretString'])

mydb = mysql.connector.connect(
  host=secretDict['host'],
  user=secretDict['username'],
  password=secretDict['password'],
  database=secretDict['dbname']
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Persons")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

