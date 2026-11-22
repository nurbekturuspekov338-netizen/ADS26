import sys

def bfs(grid, n, m, sr, sc):
    grid[sr][sc] = '0'
    queue = [(sr, sc)]
    head = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while head < len(queue):
        r, c = queue[head]
        head += 1
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1':
                grid[nr][nc] = '0'
                queue.append((nr, nc))

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    grid = [list(row) for row in data[2:2 + n]]
    
    islands = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '1':
                islands += 1
                bfs(grid, n, m, r, c)
                
    print(islands)

if __name__ == '__main__':
    solve()