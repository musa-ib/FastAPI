from fastapi import APIRouter
from modules import cal

router = APIRouter()

@router.get("/sum")
def sum(a:int,b:int)->int:
    return cal.sum(a,b)

@router.get("/Div")
def Divsion(a:int,b:int)->float|str:
    try:
        return a/b
    except:
        return"Zero Div"