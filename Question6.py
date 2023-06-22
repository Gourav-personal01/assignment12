# python code to connect MySQL to python.
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

# Cursor() Method is used to Instantiates and returns a cursor
# execute() Method is used to execute the given statement by using given parameters.