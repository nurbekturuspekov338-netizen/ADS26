import sys

sys.setrecursionlimit(200000)

def count_inversions(arr):
    def merge_sort(a):
        if len(a) <= 1:
            return a, 0
        
        mid = len(a) // 2
        left, left_inv = merge_sort(a[:mid])
        right, right_inv = merge_sort(a[mid:])
        
        merged = []
        i = j = 0
        inversions = left_inv + right_inv
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += len(left) - i
                j += 1
                
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, inversions

    _, total_inversions = merge_sort(arr)
    return total_inversions

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    print(count_inversions(a))

if __name__ == "__main__":
    solve()