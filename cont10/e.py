import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
        
    n = int(data[0])
    q = int(data[1])
    
    adj = []
    idx = 2
    for _ in range(n):
        adj.append(data[idx:idx + n])
        idx += n
        
    out = []
    for _ in range(q):
        x = int(data[idx]) - 1
        y = int(data[idx + 1]) - 1
        z = int(data[idx + 2]) - 1
        idx += 3
        
        if adj[x][y] == b'1' and adj[y][z] == b'1' and adj[x][z] == b'1':
            out.append("YES")
        else:
            out.append("NO")
            
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()