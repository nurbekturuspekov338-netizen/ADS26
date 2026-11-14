
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
    s = sys.stdin.read().strip()
    if not s:
        return

    n = len(s)
    p = pl(s)
    print(n - p[n - 1])


if __name__ == "__main__":
    solve()