import sys

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        if rank[x] >= rank[y]:
            parent[y] = x
            rank[x] += rank[y]
            print(rank[x])
        else:
            parent[x] = y
            rank[y] += rank[x]
            print(rank[y])
    else:
        print(rank[x])

t = int(input())
for _ in range(t):
    F = int(input())
    rank = {}
    parent = {}

    for _ in range(F):
        x, y = sys.stdin.readline().split()
        if x not in parent:
            parent[x] = x
            rank[x] = 1
        if y not in parent:
            parent[y] = y
            rank[y] = 1

        union(x, y)