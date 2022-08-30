import sys
import heapq

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if(rank[x] < rank[y]):
        parent[x] = y
    else:
        parent[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1

def kruskal(heap, n):
    sum = 0
    acceptedEdge = 0

    while acceptedEdge < n-1:
        edge = heapq.heappop(heap)

        if find(edge[1]) != find(edge[2]):
            union(edge[1], edge[2])
            sum += edge[0]
            acceptedEdge += 1

    return sum

N = int(input())
M = int(input())
heap = []
parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (z, x, y))

print(kruskal(heap, N))