import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="musaib@12",
)
cursorObject = dataBase.cursor()
try:
    cursorObject.execute("Create DATABASE test_db")
    print("test_db created")
except:
    print("DataBase LAready Exists")