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


def search(pat, text):
    i = 0
    j = 0
    cnt = 0
    n = len(text)
    m = len(pat)
    p = pl(pat)
    while i < n:
        if text[i] == pat[j]:  
            i += 1
            j += 1
            if j == m:
                cnt += 1
                j = p[j - 1] 
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
    return cnt


d=sys.stdin.read().split()
pat=d[0]; k=int(d[1])
text=d[2]
cnt=search(pat, text)
if cnt>=k:
    print("YES")
else:
    print("NO")