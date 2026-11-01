n = int(input())
p = input().split()

res = ""
prev = 0
for i in range(n):
    cur = int(p[i])
    d = cur - prev
    prev = cur
    res += chr(97 + d // (2 ** i))

print(res)