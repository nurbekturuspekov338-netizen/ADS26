import random
import sys

def lpar(a):
    n=len(a)
    p=a[-1]
    i=0
    for j in range(n-1):
        if a[j] < p:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[-1] = a[-1], a[i + 1]
    return a


def main():
    data=sys.stdin.read().split()
    n=int(data[0])
    a=[int(x) for x in data[1:n+1]]
    par=lpar(a)
    print(*(par))
    
if __name__=="__main__":
    main()
        