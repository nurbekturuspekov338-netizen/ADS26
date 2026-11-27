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
    dsu = DSU(V)
    cost = 0
    count = 0
    for w, x, y in edges:
        if dsu.union(x, y):
            cost += w
            count += 1
            if count == V - 1:
                break
    return cost


data = sys.stdin.read().split()
if data:
    n = int(data[0])
    d = [int(x) for x in data[1 : n + 1]]

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((d[i] + d[j], i, j))

    print(kruskal(n, edges))