import sys


class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

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


def kruskal(V, edges):
    edges.sort()
    dsu = DSU(V + 1)
    cost = 0
    count = 0
    for w, a, b in edges:
        if dsu.union(a, b):
            cost += w
            count += 1
            if count == V - 1:
                break
    return cost


data = sys.stdin.read().split()
if data:
    n = int(data[0])
    m = int(data[1])
    x = int(data[2])
    y = int(data[3])

    edges = []
    idx = 4
    min_xy = min(x, y)

    for _ in range(m):
        road_type = data[idx]
        a = int(data[idx + 1])
        b = int(data[idx + 2])
        c = int(data[idx + 3])
        idx += 4

        if road_type == "big":
            w = c * x
        elif road_type == "small":
            w = c * y
        else:  
            w = c * min_xy

        edges.append((w, a, b))

    print(kruskal(n, edges))