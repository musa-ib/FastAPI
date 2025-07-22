import mysql.connector # type: ignore
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user='root',
  database = "to_do_db"
)
cursorObject = mydb.cursor()

#Create USERS TABLE
try:
  cursorObject.execute("CREATE TABLE fake_users (user_id int NOT NULL AUTO_INCREMENT,name varchar(20),email varchar(20),password varchar(20), PRIMARY KEY (user_id))")
except:
  print("Table Already Exists")


# Create To Dos Table
try:
  cursorObject.execute("CREATE TABLE fake_to_dos (task_id int NOT NULL AUTO_INCREMENT,task_name varchar(30),task_status BOOLEAN,user_id int, PRIMARY KEY (task_id), FOREIGN KEY (user_id) REFERENCES fake_users(user_id))")
except:
  print("Table Already Exists")

mydb.commit()