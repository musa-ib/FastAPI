from fastapi import APIRouter
from modules import PandigitPrime

router = APIRouter()

@router.get("/LarPanPrime/")
def LarPanPrime(number:int)->int:
    return PandigitPrime.LargestPanPrime(number)
