import sys

def is_less(row1, row2):
    sum1, elem1 = row1
    sum2, elem2 = row2
    if sum1 != sum2:
        return sum1 > sum2  
    return elem1 < elem2    

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if is_less(left[i], right[j]) or not is_less(right[j], left[i]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    rows = []
    idx = 2
    for _ in range(n):
        row = [int(x) for x in input_data[idx:idx + m]]
        idx += m
        rows.append((sum(row), row))
    
    sorted_rows = merge_sort(rows)
    
    for _, row in sorted_rows:
        print(*(row))

if __name__ == '__main__':
    main()