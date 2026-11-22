import sys

def bfs(a, b):
    if a == b:
        print(0)
        return

    limit = 20005
    parent = [-1] * limit
    parent[a] = a
    
    queue = [a]
    head = 0
    
    while head < len(queue):
        u = queue[head]
        head += 1
        
        if u == b:
            break
            
        nxt1 = u - 1
        if nxt1 > 0 and parent[nxt1] == -1:
            parent[nxt1] = u
            queue.append(nxt1)
            
        if u < b:
            nxt2 = u * 2
            if nxt2 < limit and parent[nxt2] == -1:
                parent[nxt2] = u
                queue.append(nxt2)
                
    path = []
    curr = b
    while curr != a:
        path.append(curr)
        curr = parent[curr]
        
    path.reverse()
    print(len(path))
    print(*path)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    a = int(data[0])
    b = int(data[1])
    bfs(a, b)

if __name__ == '__main__':
    main()