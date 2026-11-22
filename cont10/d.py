import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    q = int(data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    INF = 10**9
    dist = [INF] * (n + 1)
    out = []
    
    for _ in range(q):
        t = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        
        if t == 1:
            if dist[v] > 0:
                dist[v] = 0
                queue = [v]
                head = 0
                while head < len(queue):
                    u = queue[head]
                    head += 1
                    nd = dist[u] + 1
                    for nxt in adj[u]:
                        if nd < dist[nxt]:
                            dist[nxt] = nd
                            queue.append(nxt)
        else:
            out.append("-1" if dist[v] == INF else str(dist[v]))
            
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()