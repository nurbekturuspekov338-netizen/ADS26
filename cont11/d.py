import sys


def prim(n, matrix):
    INF = 10**9
    used = [False] * n
    min_e = [INF] * n
    min_e[0] = 0
    total_cost = 0

    for _ in range(n):
        v = -1
        for i in range(n):
            if not used[i] and (v == -1 or min_e[i] < min_e[v]):
                v = i

        used[v] = True
        total_cost += min_e[v]

        for to in range(n):
            if not used[to] and matrix[v][to] < min_e[to]:
                min_e[to] = matrix[v][to]

    return total_cost


data = sys.stdin.read().split()
if data:
    n = int(data[0])
    matrix = []
    idx = 1
    for _ in range(n):
        row = [int(x) for x in data[idx : idx + n]]
        matrix.append(row)
        idx += n

    print(prim(n, matrix))