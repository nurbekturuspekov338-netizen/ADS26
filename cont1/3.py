import math

def prime(a):
    if a <= 1:
        return "NO"
    
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return "NO" 
            
    return "YES" 

n = int(input())
print(prime(n))