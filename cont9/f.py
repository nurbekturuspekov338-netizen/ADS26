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


def kmp_search(pat: str, text: str) -> list:
    i = 0
    j = 0
    n = len(text)
    m = len(pat)
    p = pl(pat)
    indices = []

    while i < n:
        if text[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                indices.append(i - m + 1)
                j = p[j - 1]
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    return indices


def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return

    text = input_data[0].strip() 
    pat = input_data[1].strip()  

    ans = kmp_search(pat, text)

    print(len(ans))
    if ans:
        print(*ans)


if __name__ == "__main__":
    solve()