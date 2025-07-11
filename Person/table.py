import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="musaib@12",
  database = "test_db"
)
cursorObject = dataBase.cursor()


table = "Create Table Person(id int, name varchar(20), email varchar(20),phone_number bigint)"

cursorObject.execute(table)
print("Created Table")

dataBase.commit()
dataBase.close()


    
