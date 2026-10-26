import math

def factors(num):
    f=[]
    n=2
    while n*n<=num:
        if num%n==0:
            f.append(n)
            num=num//n
        else:
            n+=1
    if num>1:
        f.append(num)
    print(*f)

n=int(input())
factors(n)
            
            
            
        