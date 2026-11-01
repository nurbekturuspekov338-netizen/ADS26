try:
    s = input()
except EOFError:
    s = ""

MOD = (1 << 61) - 1
B = 911382323

n = 0
for _ in s:
    n += 1

pw = [1] * (n + 1)
h = [0] * (n + 1)
for i in range(n):
    pw[i + 1] = pw[i] * B % MOD
    h[i + 1] = (h[i] * B + ord(s[i])) % MOD

total = 0
for L in range(1, n + 1):
    seen = set()
    for i in range(n - L + 1):
        seen.add((h[i + L] - h[i] * pw[L]) % MOD)
    total += len(seen)

print(total)