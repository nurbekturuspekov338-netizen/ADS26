import sys


def pl(s: str):
    j = 0
    i = 1
    n = len(s)
    p = [0] * n
    while i < n:
        if s[j] == s[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    return p


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    idx = 1
    out = []

    for _ in range(t):
        s = input_data[idx]
        k = int(input_data[idx + 1])
        idx += 2

        n = len(s)
        overlap = pl(s)[-1]
        ans = n + (k - 1) * (n - overlap)
        out.append(str(ans))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()