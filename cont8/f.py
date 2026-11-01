import sys

data = sys.stdin.read().split()
s = data[0]
q = int(data[1])
n = len(s)

MOD = (1 << 61) - 1
B = 911382323

pw = [1] * (n + 1)
h = [0] * (n + 1)
for i in range(n):
    pw[i + 1] = pw[i] * B % MOD
    h[i + 1] = (h[i] * B + ord(s[i])) % MOD

groups = {}
for j in range(q):
    l = int(data[2 + 2 * j]) - 1
    length = int(data[3 + 2 * j]) - l
    if length not in groups:
        groups[length] = []
    groups[length].append((l, j))

ans = [0] * q
for length, items in groups.items():
    p = pw[length]
    need = {}
    keys = []
    for l, j in items:
        x = (h[l + length] - h[l] * p) % MOD
        keys.append(x)
        need[x] = 0
    hl = h[length:]
    wins = [(a - b * p) % MOD for a, b in zip(hl, h)]
    for x in wins:
        if x in need:
            need[x] += 1
    for k in range(len(items)):
        ans[items[k][1]] = need[keys[k]]

sys.stdout.write("\n".join(map(str, ans)) + "\n")