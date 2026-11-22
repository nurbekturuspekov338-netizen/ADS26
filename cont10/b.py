import sys

def bfs(n, adj, start, end):
    dist = [-1] * n
    dist[start] = 0
    queue = [start]
    head = 0
    
    while head < len(queue):
        u = queue[head]
        head += 1
        
        if u == end:
            return dist[u]
            
        for v in range(n):
            if adj[u][v] == 1 and dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
                
    return -1

def main():
    data=sys.stdin.read().split()
    if not data:
        return
    n=int(data[0])
    adj=[]
    idx=1
    for _ in range(n):
        adj.append([int(x) for x in data[idx:idx+n]])
        idx+=n
        
    start=int(data[idx])-1
    end=int(data[idx+1])-1
    print(bfs(n, adj, start, end))
    
if __name__=="__main__":
    main()