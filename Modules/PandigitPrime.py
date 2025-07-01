from modules import Primes

def isPandigit(n:int)->bool:
    nums = [0]*10
    l = 0
    while n:
        if nums[n%10]>0:
            return False
        nums[n%10]+=1
        n = n//10
        l = l+ 1
    if nums[0]>0:
        return False
    for i in range(1,l+1):
        if nums[i]!=1:
            return False
    return True
def LargestPanPrime(n:int)->int:
    for i in range(n,0,-1):
        if(Primes.isPrime(i) and isPandigit(i)):
            return i
        
    return -1

