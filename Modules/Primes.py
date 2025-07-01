import math

def isPrime(n:int)->bool:
    sq = int(math.sqrt(n))
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,sq+1,2):
        if n%i==0:
            return False
    return True

def summation(n):
    s = 2
    for i in range(3,n,2):
        if isPrime(i):
            s += i
    return s
