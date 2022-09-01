import sys
import heapq

def dijkstra(start, end):
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        w, n = heapq.heappop(heap)

        if visited[n] == False:
            visited[n] = True
            for nw, nn in edge[n]:
                if dist[n] + nw < dist[nn]:
                    dist[nn] = dist[n] + nw
                    heapq.heappush(heap, (dist[nn], nn))

        if False not in visited:
            break

    return dist[end]

N = int(input())    
edge = [[] for _ in range(N)]
dist = [sys.maxsize for _ in range(N)]
visited = [False for _ in range(N)]

M = int(input())
for _ in range(M):
    c1, c2, w = map(int, sys.stdin.readline().split())
    edge[c1-1].append([w, c2-1])

start, end = map(lambda x:x-1, map(int, sys.stdin.readline().split()))

print(dijkstra(start, end))