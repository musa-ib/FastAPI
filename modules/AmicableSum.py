import math

def DivSum(n:int)->int:
    if n==1:
        return 0
    divSum = 1
    sq = math.ceil(math.sqrt(n))
    if sq*sq==n:
        divSum += sq
    for i in range(2,sq):
        if n%i==0:
            divSum = divSum + i + n//i

    return divSum


def amicableSum(n:int)->int:
    l = [0]*n
    sum = 0
    for i in range(2,n):
        if l[i]==0:
            a = DivSum(i)
            b = DivSum(a)
            if a<n and b<n and i==b and a!=b:
                l[a] = 1
                l[b] = 1

    for i in range(n):
        if l[i]==1:
            sum+=i
    return sum
