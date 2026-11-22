import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        adj[x].append(y)
        adj[y].append(x)
        
    visited = [False] * (n + 1)
    children = [0] * (n + 1)
    big_fam = 0
    
    for start in range(1, n + 1):
        if not visited[start]:
            visited[start] = True
            big_fam += 1
            children[start] = len(adj[start])
            
            queue = [start]
            head = 0
            
            while head < len(queue):
                u = queue[head]
                head += 1
                
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        children[v] = len(adj[v]) - 1
                        if children[v] > children[u]:
                            big_fam += 1
                        queue.append(v)
                        
    print(big_fam)

if __name__ == '__main__':
    solve()