import sys

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    d = [int(x) for x in data[1 : n + 1]]
    print(sum(d) + (n - 2) * min(d))