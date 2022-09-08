import sys
import heapq

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1

def kruskal(n):
    selectEdge = 0
    fullWeight = 0
    while heap:
        w, u, v = heapq.heappop(heap)
        if find(u) != find(v):
            union(u, v)
            fullWeight += w
            selectEdge += 1

    if selectEdge == n-1:
        return fullWeight
    else:
        return -1

input = sys.stdin.readline

N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
rank = [1 for i in range(N+1)]
heap = []
total = 0
for _ in range(M):
    u, v, w = map(int, input().split())
    total += w
    heapq.heappush(heap, (w, u, v))

sol = kruskal(N)

if sol == -1:
    print(sol)
else:
    print(total - sol)