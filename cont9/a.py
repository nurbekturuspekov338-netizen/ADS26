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


def contains(pat: str, text: str, p: list) -> bool:
    i = 0
    j = 0
    n = len(text)
    m = len(pat)
    while i < n:
        if text[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
    return False


def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return

    a = input_data[0].strip()
    b = input_data[1].strip()

    p = pl(b)

    k = (len(b) + len(a) - 1) // len(a)

    if contains(b, a * k, p):
        print(k)
    elif contains(b, a * (k + 1), p):
        print(k + 1)
    else:
        print(-1)


if __name__ == "__main__":
    solve()