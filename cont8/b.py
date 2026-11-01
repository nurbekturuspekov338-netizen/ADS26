s1 = input()
s2 = input()
t = input()

MOD = (1 << 61) - 1
B = 911382323



n1 = len(s1)
n2 = len(s2)
m = len(t)

pw = [1] * (m + 1)
for i in range(1, m + 1):
    pw[i] = pw[i - 1] * B % MOD

def prefix(s, n):
    h = [0] * (n + 1)
    for i in range(n):
        h[i + 1] = (h[i] * B + ord(s[i])) % MOD
    return h

h1 = prefix(s1, n1)
h2 = prefix(s2, n2)

ht = 0
for i in range(m):
    ht = (ht * B + ord(t[i])) % MOD

n = n1
if n2 < n:
    n = n2

count = 0
for i in range(n - m + 1):
    x1 = (h1[i + m] - h1[i] * pw[m]) % MOD
    x2 = (h2[i + m] - h2[i] * pw[m]) % MOD
    if x1 == ht and x2 == ht:
        count += 1

print(count)