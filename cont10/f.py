import sys

def bfs(n, adj, s, f):
    if s == f:
        return True
    visited = [False] * (n + 1)
    visited[s] = True
    queue = [s]
    head = 0
    
    while head < len(queue):
        u = queue[head]
        head += 1
        
        if u == f:
            return True
            
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                
    return False

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    s = int(data[idx])
    f = int(data[idx + 1])
    
    print("YES" if bfs(n, adj, s, f) else "NO")

if __name__ == '__main__':
    solve()