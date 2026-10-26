import sys

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    
    L = [0] * n1
    R = [0] * n2

    
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    while i < n1 and j < n2:
        if len(L[i]) <= len(R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def main():
    data=sys.stdin.read().splitlines()
    if not data:
        return
    n=int(data[0].strip())
    
    for i in range(1, n+1):
        words=data[i].split()
        mergeSort(words, 0, len(words)-1)
        print(*words)      
        
if __name__ == "__main__":
    main()
    