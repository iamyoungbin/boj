import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())

    dist = [sys.maxsize for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    edge = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        edge[b].append((s, a))

    heap = []
    dist[c] = 0
    heapq.heappush(heap, (dist[c], c))

    time = 0
    zombie = 0
    while heap:
        pt, pn = heapq.heappop(heap)
        if visited[pn] == False:
            visited[pn] = True
            zombie += 1
            time = pt

        for w, nn in edge[pn]:
            if dist[pn] + w < dist[nn]:
                dist[nn] = dist[pn] + w
                heapq.heappush(heap, (dist[nn], nn))

    print(zombie, time)