import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="runoob_db"
)
 
mycursor = mydb.cursor()
 
# create the database
mycursor.execute("CREATE DATABASE runoob_db")

# mycursor.execute("CREATE TABLE holidays (id INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(255), name VARCHAR(255), type VARCHAR(255), iso_date VARCHAR(255), description VARCHAR(255))")

mycursor.execute("SHOW DATABASES")
 
for x in mycursor:
  print(x)
