def pow(a, n, m):
    if n == 0:
        return 1 % m
    if n % 2 == 0:
        half = pow(a, n // 2, m)
        return (half * half) % m
    else:
        half = pow(a, n // 2, m)
        return (a * half * half) % m

a, n, m = map(int, input().split())
print(pow(a, n, m))
