from fastapi import APIRouter
from modules import Strng

router = APIRouter()


@router.get("/longestsubstr")
async def NonReptStr(string: str)->str:
    l, i = Strng.LargestString(string,len(string))
    return string[i:l+i]