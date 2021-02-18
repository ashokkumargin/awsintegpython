import mysql.connector
db_connection = mysql.connector.connect(
  host="awsmysql-1.c66v1kaibbzi.us-east-1.rds.amazonaws.com",
  port="3001",
  user="awsmysql",
  passwd="awsmysql"
)
print(db_connection)
mycursor = db_connection.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)