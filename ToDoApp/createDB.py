import mysql.connector # type: ignore
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user='root'
)
cursorObject = mydb.cursor()
try:
  cursorObject.execute("CREATE DATABASE to_do_db")
  print("DataBase Created")
except:
  print("DataBase Already Exists")