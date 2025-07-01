from fastapi import APIRouter

router = APIRouter()

from modules import curious


@router.get("/Curious_Number/")
def CuriosSum(number:int)->int:
    return curious.curioSum(number)