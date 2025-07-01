from fastapi import APIRouter

router = APIRouter()

from modules import Primes
@router.get("/prime_sums")
def sums(number:int)->int:
    return Primes.summation(number)