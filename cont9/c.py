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


def occur(pat, text):
    i = 0
    j = 0
    n = len(text)
    m = len(pat)
    p = pl(pat)
    while i < n:
        if text[i] == pat[j]:  
            i += 1
            j += 1
            if j == m:
                return i-m
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
    return -1

def main():
    s1=input()
    s2=input()
    if len(s1)!=len(s2):
        return -1
    ans=occur(s1, s2+s2)
    print(ans)
    
if __name__=="__main__":
    main()