import sys

def is_acyclic(n, adj, in_deg):
    queue = [i for i in range(1, n + 1) if in_deg[i] == 0]
    head = 0
    visited = 0
    
    while head < len(queue):
        u = queue[head]
        head += 1
        visited += 1
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)
                
    return visited == n

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    base_in_deg = [0] * (n + 1)
    idx = 2
    
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        base_in_deg[v] += 1
        
    if is_acyclic(n, adj, base_in_deg[:]):
        print("YES")
        return
        
    for v in range(1, n + 1):
        if base_in_deg[v] > 0:
            deg = base_in_deg[:]
            deg[v] -= 1
            if is_acyclic(n, adj, deg):
                print("YES")
                return
                
    print("NO")

if __name__ == '__main__':
    solve()