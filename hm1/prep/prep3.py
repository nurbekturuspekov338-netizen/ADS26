import sys

def check_min_heap():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [0] + [int(x) for x in input_data[1:n + 1]]
    
    is_heap = True
    for i in range(1, n + 1):
        left = 2 * i
        right = 2 * i + 1
        
        if left <= n and a[i] > a[left]:
            is_heap = False
            break
            
        if right <= n and a[i] > a[right]:
            is_heap = False
            break
            
    if is_heap:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    check_min_heap()