import sys

def bfs():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    m = int(data[0])
    n = int(data[1])
    size = m * n
    
    grid = [int(x) for x in data[2:2 + size]]
    
    queue = []
    mushrooms = 0
    for i in range(size):
        val = grid[i]
        if val == 2:
            queue.append(i)
        elif val == 1:
            mushrooms += 1
            
    if mushrooms == 0:
        print(0)
        return
        
    head = 0
    minutes = -1
    
    while head < len(queue):
        level_end = len(queue)
        minutes += 1
        while head < level_end:
            pos = queue[head]
            head += 1
            
            up = pos - n
            if up >= 0 and grid[up] == 1:
                grid[up] = 2
                mushrooms -= 1
                queue.append(up)
                
            down = pos + n
            if down < size and grid[down] == 1:
                grid[down] = 2
                mushrooms -= 1
                queue.append(down)
                
            if pos % n > 0:
                left = pos - 1
                if grid[left] == 1:
                    grid[left] = 2
                    mushrooms -= 1
                    queue.append(left)
                    
            if pos % n < n - 1:
                right = pos + 1
                if grid[right] == 1:
                    grid[right] = 2
                    mushrooms -= 1
                    queue.append(right)
                    
    print(minutes if mushrooms == 0 else -1)

if __name__ == '__main__':
    bfs()