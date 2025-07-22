from fastapi import APIRouter, Form # type: ignore
import mysql.connector # type: ignore
from typing import Annotated

user_router = APIRouter()


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user='root',
  database = "to_do_db"
)

def search_id(email:str):
   curObj = mydb.cursor()
   search_query = "SELECT user_id FROM fake_users where email=%s"

   curObj.execute(search_query,(email,))
   result = curObj.fetchone()
   if result is None:
      return 0
   return result[0]



# search user email
def search_mail(email:str,id:int=0):
  curObj = mydb.cursor()
  search_query = "SELECT user_id FROM fake_users where email=%s and user_id!=%s"

  curObj.execute(search_query,(email,id))
  return(len(curObj.fetchall()))




# # add User

@user_router.post("/user/")
def add_user(name :Annotated[str, Form()],email:Annotated[str, Form()],password:Annotated[str, Form()]):
   curObj = mydb.cursor()
   if search_mail(email)>0:
      return {email:"already Exists"}
   
   query = "INSERT INTO fake_users(name,email,password) VALUES (%s,%s,%s)"
   values= (name,email,password)
   curObj.execute(query,values)
   mydb.commit()
   return {"name":name,"email":email}

#update user
@user_router.put("/user/{email}")
def update_user(name:Annotated[str,Form()],email,new_email:Annotated[str,Form()],password:Annotated[str,Form()]):
   id = search_id(email)
   if id==0:
      return {email:"doesnot exist"}
   if search_mail(email,id)>0:
      return {new_email:"already exists"}
   
   query = "UPDATE fake_users SET name=%s,email=%s,password=%s where user_id=%s"
   values = (name,email,password,id)
   curObj = mydb.cursor()
   curObj.execute(query,values)
   mydb.commit()
   return {f"user_{id}":"Updated"}

#delete user
@user_router.delete("/user/{email}/")
def delete_user(email:str):
   id = search_id(email)
   if id==0:
      return {f"user_{id}":"deosn't exist"}
   
   query = "DELETE FROM fake_users WHERE user_id=%s"
   values = (id,)
   curObj = mydb.cursor()
   curObj.execute(query,values)
   return {f"user_{id}":"Deleted"}
   