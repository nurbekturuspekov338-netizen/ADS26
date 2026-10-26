def fmax(arr):
    max=0
    for i in range(len(arr)):
        if i==0:
            max=arr[i]
        else:
            if max<arr[i]:
                max=arr[i]
                
    return max

n=list(map(int, input().split()))
print(fmax(n))
            
        