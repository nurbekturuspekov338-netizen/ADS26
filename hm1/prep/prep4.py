import sys

def bs(arr, t):
    low=0
    high=len(arr)
    while low<high:
        mid=low+(high-low)//2
        if arr[mid]==t:
            return "YES"
        elif arr[mid]>t:
            high=mid
        else:
            low=mid+1
    return "NO"

def main():
    data=sys.stdin.read().split()
    if data:
        n=int(data[0])
        a1=[int(x) for x in data[1:n+1]]
        m=int(data[n+1])
        a2=[int(x) for x in data[n+2: n+2+m]]
        for i in a2:
            print(bs(a1, i))
if __name__=="__main__":
    main()