import sys


class DSU:

    def __init__(self, n):
        self.parent = list(range(n))

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
            self.parent[s1] = s2
            return True
        return False


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    segments = []
    idx = 2
    for _ in range(m):
        l = int(data[idx])
        r = int(data[idx + 1])
        c = int(data[idx + 2])
        segments.append((c, l, r))
        idx += 3

    segments.sort()

    dsu = DSU(n + 1)
    nxt = DSU(n + 1)

    total_cost = 0
    edges_used = 0

    for c, l, r in segments:
        curr = nxt.find(l)
        while curr < r:
            if dsu.union(curr, curr + 1):
                total_cost += c
                edges_used += 1
            nxt.union(curr, curr + 1)
            curr = nxt.find(curr)
        if edges_used == n - 1:
            break

    print(total_cost)


if __name__ == "__main__":
    solve()