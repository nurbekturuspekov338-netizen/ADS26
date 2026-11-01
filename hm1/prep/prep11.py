import sys

def lower_bound(arr, target):
    low=0
    high=len(arr)
    while low<high:
        mid=low+(high-low)//2
        if arr[mid]<target:
            low=mid+1
        else:
            high=mid
    return low

def upper_bound(arr, target):
    low=0
    high=len(arr)
    while low<high:
        mid=low+(high-low)//2
        if arr[mid]<=target:
            low=mid+1
        else:
            high=mid
    return low

def diff(arr, target):
    return upper_bound(arr, target)-lower_bound(arr, target)
    


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    a1 = [int(x) for x in data[1 : n + 1]]
    m = int(data[n + 1])
    a2 = [int(x) for x in data[n + 2 : n + 2 + m]]

    # Ensure a1 is sorted for binary search
    a1.sort()

    for i in a2:
        print(diff(a1, i))


if __name__ == "__main__":
    main()