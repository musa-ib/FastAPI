from fastapi import FastAPI,UploadFile,HTTPException,File,Query
from datetime import date
import pandas as pd
import os ,shutil ,json
from typing import Annotated
app = FastAPI()

date = date.today()
date = str(date)
direc = "Files/"+date



def find_file(direc_path,file_name):
    for root,dirs,files in os.walk(direc_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None




@app.post("/files")
def upload_files(files :list[UploadFile]):

    files_list = []
    for file in files:
        if not file.filename.endswith((".csv",".xls")):
            continue
            # raise HTTPException(
            #      status_code=400,
            #     detail="Only CSV or Excel files are allowed."
            # )
        try:
            os.mkdir("Files")
        except FileExistsError:
            print("FIles Directory Already Exists")

        try:
            os.mkdir(direc)
            print(f"Folder '{date}' created successfully.")
        except FileExistsError:
            print(f"Folder '{date}' already exists.")

        full_path = os.path.join(direc,file.filename)


        with open(full_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)
        files_list.append(file.filename)
    return json.dumps(files_list)
        

@app.post("/upload/")
def upload_file(fil: UploadFile=File(...)):

    if not fil.filename.endswith((".csv",".xls")):
            raise HTTPException(
                 status_code=400,
                detail="Only CSV or Excel files are allowed."
            )
    try:
        os.mkdir("Files")
    except FileExistsError:
        print("FIles Directory Already Exists")

    try:
        os.mkdir(direc)
        print(f"Folder '{date}' created successfully.")
    except FileExistsError:
        print(f"Folder '{date}' already exists.")

    full_path = os.path.join(direc,fil.filename)
    try:
        with open(full_path, 'wb') as f:
            shutil.copyfileobj(fil.file, f)
    except FileExistsError:
        print("file already exists")
        
    return {"Uploaded File":fil.filename}

@app.get("/files/")
def get_all_files():
    path= "Files/"
    file_list = []
    for _,_,files in os.walk(path):
        if files:
            file_list.append(files)
    return json.dumps(file_list)


@app.get("/file/")
def GetFile(file_name:str):
    path = "Files/"
    file_path = find_file(path,file_name)
    if not file_path:
        return {file_name:"Does not Exist"}

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    a = df.head(2)
    print(a)
    a = a.to_json()
    return a
     


if __name__=="__main__":
    import uvicorn
    uvicorn.run("uploadFile:app",reload=True)