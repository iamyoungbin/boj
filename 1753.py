import sys
import heapq

def dijkstra(start):
    heap = []
    visited = [False for _ in range(V+1)]
    visited[0] = True
    dist = [sys.maxsize for _ in range(V+1)]
    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        pd, pv = heapq.heappop(heap)

        if visited[pv] == False:
            visited[pv] = True

            for nd, nv in edge[pv]:
                if pd + nd < dist[nv]:
                    dist[nv] = pd + nd
                    heapq.heappush(heap, (dist[nv], nv))

        if False not in visited:
            break

    for i in dist[1:]:
        if i >= sys.maxsize:
            print("INF")
        else:
            print(i)

V, E = map(int, sys.stdin.readline().split())
start = int(input())
edge = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edge[u].append((w, v))

dijkstra(start)
