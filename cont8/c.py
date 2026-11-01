import sys

data = sys.stdin.read().split()
MOD = (1 << 61) - 1
B = 911382323

pos = 0
out = []
while pos < len(data):
    N = int(data[pos])
    pos += 1
    if N == 0:
        break
    pats = data[pos:pos + N]
    pos += N
    text = data[pos]
    pos += 1
    n = len(text)

    pw = [1] * 71
    for i in range(1, 71):
        pw[i] = pw[i - 1] * B % MOD

    h = [0] * (n + 1)
    for i in range(n):
        h[i + 1] = (h[i] * B + ord(text[i])) % MOD

    byLen = {}
    ph = []
    for idx in range(N):
        p = pats[idx]
        x = 0
        for ch in p:
            x = (x * B + ord(ch)) % MOD
        ph.append(x)
        L = len(p)
        if L not in byLen:
            byLen[L] = []
        byLen[L].append(idx)

    freq = [0] * N
    for L in byLen:
        if L > n:
            continue
        pl = pw[L]
        wins = [(a - b * pl) % MOD for a, b in zip(h[L:], h)]
        done = {}
        for idx in byLen[L]:
            x = ph[idx]
            if x not in done:
                done[x] = wins.count(x)
            freq[idx] = done[x]

    best = 0
    for f in freq:
        if f > best:
            best = f
    out.append(str(best))
    for idx in range(N):
        if freq[idx] == best:
            out.append(pats[idx])

sys.stdout.write("\n".join(out) + "\n")