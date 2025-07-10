from fastapi import FastAPI
from schema import person
import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="musaib@12",
  database = "test_db"
)


app = FastAPI()

# create person
@app.post("/person/")
def create_person(per : person):
    cursorObject = dataBase.cursor()
    query = "INSERT INTO Person (id, name, email, phone_number) VALUES (%s,%s,%s,%s)"
    values = (per.id,per.name,per.email,per.phone_number)
    cursorObject.execute(query,values)
    dataBase.commit()
    return "Person Created"

# View all persons
@app.get("/person/")
def get_all_users():
    cursorObject = dataBase.cursor()
    query = "SELECT * FROM Person"
    cursorObject.execute(query)
    myresult = cursorObject.fetchall()
    return myresult

# update person
@app.put("/person/{per_id}")
def update_person(per_id:int,per:person):
    cursorObject = dataBase.cursor()
    values = (per.name,per.email,per.phone_number,per_id)
    update_query = "UPDATE Person set name = %s,email = %s,phone_number = %s WHERE id = %s"
    cursorObject.execute(update_query,values)
    dataBase.commit()
    return "Person Updated"
# delete Person
@app.delete("/person/{per_id}/")
def  delete_person(per_id:int):
    cursorObject = dataBase.cursor()
    query = "DELETE FROM Person WHERE id = %s"
    v = (per_id,)
    try:
        print("start deleteing")
        cursorObject.execute(query,v)
        print("deleted")
        dataBase.commit()
        return "Person Deleted"
    except:
        return f"person {per_id} doesnot Exist"

