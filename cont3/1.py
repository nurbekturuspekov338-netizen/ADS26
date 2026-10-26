import sys

def binary_search(arr: list[int], target: int) -> str:
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return "Yes"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return "No"

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        values = [int(x) for x in input_data[1:n+1]]
        
        values.sort()
        
        target = int(input_data[n+1]) if len(input_data) > n + 1 else 0
        print(binary_search(values, target))

if __name__ == "__main__":
    main()
    
    
        
            