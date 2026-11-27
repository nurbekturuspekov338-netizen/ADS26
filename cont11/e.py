import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[i] != root:
            nxt = self.parent[i]
            self.parent[i] = root
            i = nxt
        return root

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1
            return True
        return False

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        v = int(data[idx])
        u = int(data[idx + 1])
        idx += 2
        if v > u:
            adj[u].append(v)
        elif u > v:
            adj[v].append(u)

    dsu = DSU(n + 1)
    ans = [0] * n
    components = 0

    for i in range(n, 0, -1):
        ans[i - 1] = components
        components += 1
        for u in adj[i]:
            if dsu.union(i, u):
                components -= 1

    sys.stdout.write("\n".join(map(str, ans)) + "\n")

if __name__ == "__main__":
    solve()