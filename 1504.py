import sys
import heapq

def dijkstra(start, end):
    heap = []
    visited = [False for _ in range(N+1)]
    dist = [sys.maxsize for _ in range(N+1)]
    visited[0] = True

    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        pd, pv = heapq.heappop(heap)

        if visited[pv] == False:
            visited[pv] = True

            for w, nv in edge[pv]:
                if dist[pv] + w < dist[nv]:
                    dist[nv] = dist[pv] + w
                    heapq.heappush(heap, (dist[nv], nv))

        if False not in visited:
            break

    return dist[end]

N, E = map(int, input().split())
edge = [[] for _ in range(N+1)]
for _ in range(E):
    v1, v2, w = map(int, sys.stdin.readline().split())
    edge[v1].append((w, v2))
    edge[v2].append((w, v1))

wp1, wp2 = map(int, sys.stdin.readline().split())

dist1 = dijkstra(1, wp1) + dijkstra(N, wp2) + dijkstra(wp1, wp2)
dist2 = dijkstra(1, wp2) + dijkstra(N, wp1) + dijkstra(wp1, wp2)
dist3 = dijkstra(1, wp1) + dijkstra(N, wp1) + dijkstra(wp1, wp2)*2
dist4 = dijkstra(1, wp2) + dijkstra(N, wp2) + dijkstra(wp1, wp2)*2
fullDist = min(dist1, dist2, dist3, dist4)

if fullDist >= sys.maxsize:
    print("-1")
else:
    print(fullDist)