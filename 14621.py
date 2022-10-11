import sys
import heapq

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        
    if rank[x] == rank[y]:
        rank[x] += 1

input = sys.stdin.readline

N, M = map(int, input().split())
sex = input().split()
heap = []
parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]
edge_sum = 0
for _ in range(M):
    u, v, d = map(int, input().split())
    if sex[u-1] != sex[v-1]:
        heapq.heappush(heap, (d, u, v))
        edge_sum += 1
      
if edge_sum < N-1:
    print(-1)
else:
    accepted_edge = 0
    sol = 0
    while heap and accepted_edge < N-1:
        weight, vertex1, vertex2 = heapq.heappop(heap)
        
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            sol += weight
            accepted_edge += 1
    
    if accepted_edge == N-1:   
        print(sol)
    else:
        print(-1)