from fastapi import APIRouter

router = APIRouter()

from modules import AmicableSum

@router.get("/amicablesum")
async def AmcableSum(number:int)->int:
    return AmicableSum.amicableSum(number)