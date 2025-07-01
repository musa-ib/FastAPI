def factorial(n:int)->int:
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

fact = [1]*10

def sum_fact(n):
    s = 0
    while n>0:
        if(fact[n%10]==1):
            fact[n%10] = factorial(n%10)
        s = s + fact[n%10]
        n = n//10
    return s

def curioSum(n:int)->int:
    s = 0
    for i in range(3,n):
        if i == sum_fact(i):
            s = s + i
    return s