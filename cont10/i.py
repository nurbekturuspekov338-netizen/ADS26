import sys

def heappush(heap, item):
    heap.append(item)
    i = len(heap) - 1
    while i > 0:
        p = (i - 1) >> 1
        if heap[i] < heap[p]:
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        else:
            break

def heappop(heap):
    top = heap[0]
    last = heap.pop()
    if heap:
        heap[0] = last
        n = len(heap)
        i = 0
        while True:
            l = (i << 1) + 1
            r = l + 1
            smallest = i
            if l < n and heap[l] < heap[smallest]:
                smallest = l
            if r < n and heap[r] < heap[smallest]:
                smallest = r
            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
            else:
                break
    return top

def bfs(n, adj, in_deg):
    heap = []
    for i in range(1, n + 1):
        if in_deg[i] == 0:
            heappush(heap, i)
            
    order = []
    while heap:
        u = heappop(heap)
        order.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                heappush(heap, v)
                
    return order

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    idx = 2
    
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        in_deg[v] += 1
        
    order = bfs(n, adj, in_deg)
    
    if len(order) == n:
        sys.stdout.write("Possible\n")
        sys.stdout.write(" ".join(map(str, order)) + "\n")
    else:
        sys.stdout.write("Impossible\n")

if __name__ == '__main__':
    solve()