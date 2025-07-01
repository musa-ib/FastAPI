from fastapi import APIRouter
from modules import TruncateablePrimes

router = APIRouter()

@router.get("/TruncateablePrimes")
def sumTruncateablePrimes():
    return TruncateablePrimes.SumTruncablePrimes()