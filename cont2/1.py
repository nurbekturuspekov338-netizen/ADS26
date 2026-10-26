t = int(input())

for _ in range(t):
    n = int(input())
    stream = input().split()
    
    counts = {}         
    order = []         
    first_idx = 0       
    result = []

    for char in stream:
        
        counts[char] = counts.get(char, 0) + 1
        
       
        if counts[char] == 1:
            order.append(char)
            
        
        while first_idx < len(order) and counts[order[first_idx]] > 1:
            first_idx += 1
            
        
        if first_idx < len(order):
            result.append(order[first_idx])
        else:
            result.append("-1")
            
    print(" ".join(result))