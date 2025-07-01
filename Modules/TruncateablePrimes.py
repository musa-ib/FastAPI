from modules import Primes

def revNum(n:int)->int:
    rev = 0
    while n>0:
        rev = rev*10 + n%10
        n = n//10
    return rev

def isPrimeRemDigR(n:int)->bool:
    while n>0:
        if Primes.isPrime(n)==False:
            return False
        n = n//10
    return True

def isPrimeRemDigL(n:int)->bool:
    while n>0:
        if Primes.isPrime(n)==False:
            return False
        
        n = revNum(n)
        n = n//10
        n = revNum(n)
    return True

def SumTruncablePrimes()->int:
    s = 0
    cont = 0
    i = 11
    while cont<11:
        if(isPrimeRemDigL(i) and isPrimeRemDigR(i)):
            s = s + i
            cont = cont +1
        i  = i + 2

    return s