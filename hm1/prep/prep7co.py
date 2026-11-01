import math
n=int(input())
primes=[True]*n
primes[0]=primes[1]=False
for i in range(2, int(math.sqrt(n))):
    if primes[i]:
        for m in range(i*i, n, i):
            primes[m]=False
            
print(primes)
        