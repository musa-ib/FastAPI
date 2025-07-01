from fastapi import APIRouter

router = APIRouter()

from modules import triangle


@router.get("/triword")
async def TrianleWord(path:str)->int:
    return triangle.readfile(path)