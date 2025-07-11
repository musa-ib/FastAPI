from fastapi import FastAPI 
from users import user_router
from to_dos import task_router

app = FastAPI()
app.include_router(user_router)
app.include_router(task_router)

