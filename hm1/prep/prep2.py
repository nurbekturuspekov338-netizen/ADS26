import sys

def lower_bound(arr, target):
    low=0
    high=len(arr)
    while low<high:
        mid=low+(high-low)//2
        if arr[mid]>=target:
            high=mid
        else:
            low=mid+1
    return low

def main():
    data=sys.stdin.read().split()
    n=int(data[0])
    a1=[int(x) for x in data[1:n+1]]
    m=int(data[n+1])
    a2=[int(x) for x in data[n+2: n+2+m]]
    for i in a2:
        idx=lower_bound(a1, i)
        if idx==n:
            print(-1)
        else:
            print(idx+1)
            
if __name__=="__main__":
    main()