# -*- coding: utf-8 -*-
import sys
import heapq

def dijkstra(start, end):
    heap = []
    dist = [sys.maxsize for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        pw, pv = heapq.heappop(heap)

        if visited[pv] == False:
            visited[pv] = True

            for nw, nv in edge[pv]:
                if pw + nw < dist[nv]:
                    dist[nv] = pw + nw
                    heapq.heappush(heap, (dist[nv], nv))

        if False not in visited[1:]:
            break

    if end == 1001: # end == 1001 이면 파티에 참여후 다시 돌아오는 케이스
        for i in range(1, N+1):
            fullDist[i] += dist[i]
    else:
        return dist[end]


N, M, X = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]
fullDist = [0 for _ in range(N+1)]
for _ in range(M):
    v1, v2, w = map(int, sys.stdin.readline().split())
    edge[v1].append((w, v2))

for i in range(1, N+1):
    if i != X:
        fullDist[i] = dijkstra(i, X)

dijkstra(X, 1001)

print(max(fullDist))