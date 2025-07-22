from fastapi import APIRouter, Form # type: ignore
import mysql.connector # type: ignore
from typing import Annotated
import json

task_router = APIRouter()


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

# search Task id
def search_task_id(task_name:str):
  query = "SELECT task_id FROM fake_to_dos WHERE task_name = %s"
  cur_obj = mydb.cursor()
  cur_obj.execute(query,(task_name,))
  result = cur_obj.fetchone()
  if result is None:
    return 0
  return result[0]

# // Search user_id

#add task
@task_router.post("/task/{email}/")
def add_task(task_name:Annotated[str,Form()],email):
  user_id = search_id(email)
  if user_id==0:
    return {email:"Doesn't exist"}
  
  cur_obj = mydb.cursor()
  query = "INSERT INTO fake_to_dos (task_name,task_status,user_id)VALUES(%s,0,%s)"
  values = (task_name,user_id)
  cur_obj.execute(query,values)
  mydb.commit()
  return {task_name:"Added"}

#update task status
@task_router.put("/task/{email}/")
def update_task_status(email,status:Annotated[bool,Form()],task_name:Annotated[str,Form()]):
  user_id = search_id(email)
  task_id = search_task_id(task_name)
  if user_id==0:
    return {email:"Doesn't exist"}
  
  if (task_id)==0:
    return {task_name:"Doesn't exist"}
  query = "UPDATE fake_to_dos SET task_status=1 WHERE task_id=%s and user_id = %s"
  values=(task_id,user_id)
  cur_obj = mydb.cursor()
  cur_obj.execute(query,values)
  mydb.commit()

  return {task_id:"UPDATED"}

#update task name
@task_router.put("/task/{email}")
def update_task_name(email,task_name:Annotated[str,Form()],task_new_name:Annotated[str,Form()]):
  user_id = search_id(email)
  task_id = search_task_id(task_name)
  if (user_id)==0:
    return {user_id:"Doesn't exist"}
  
  if (task_id)==0:
    return {task_id:"Doesn't exist"}
  query = "UPDATE fake_to_dos SET task_name=%s WHERE task_id=%s and user_id = %s"
  values=(task_new_name,task_id,user_id)

  cur_obj = mydb.cursor()
  cur_obj.execute(query,values)
  mydb.commit()

  return {task_new_name:"UPDATED"}

#Delete TASk
@task_router.delete("/task/{email}")
def delete_task(email,task_name:Annotated[str,Form()]):
  user_id = search_id(email)
  if (user_id)==0:
    return {f"user_{user_id}":"Doesn't exist"}
  
  task_id = search_task_id(task_name)
  if (task_id)==0:
    return {task_name:"Doesn't exist"}
  query = "DELETE FROM fake_to_dos WHERE task_id=%s and user_id = %s"
  values=(task_id,user_id)

  cur_obj = mydb.cursor()
  cur_obj.execute(query,values)
  mydb.commit()

  return {task_name:"Deleted"}
#get tasks
@task_router.get("/tasks/{email}/")
def get_all_tasks(email):
  user_id = search_id(email)
  if (user_id)==0:
    return {email:"Doesn't exist"}
  
  query = ("SELECT task_id,task_name,task_status FROM fake_to_dos WHERE user_id = %s")
  values= (user_id,)
  cur_obj = mydb.cursor()
  cur_obj.execute(query,values)
  return json.dumps(cur_obj.fetchall())