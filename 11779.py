import sys
import heapq

def dijkstra(start, end):
    dist = [sys.maxsize for _ in range(n+1)]
    parent = [0 for _ in range(n+1)]
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    parent[start] = start

    while heap:
        pw, pn = heapq.heappop(heap)

        if pw > dist[pn]:
            continue
        for nw, nn in edge[pn]:
            if pw + nw < dist[nn]:
                dist[nn] = pw + nw
                parent[nn] = pn
                heapq.heappush(heap, (dist[nn], nn))
        
    seq = []
    temp = end
    while temp != start:
        seq.append(temp)
        temp = parent[temp]

    seq.append(start)
    seq.reverse()

    print(dist[end])
    print(len(seq))
    print(*seq)

input = sys.stdin.readline

n = int(input())
m = int(input())

edge = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    edge[u].append((w, v))

start, end = map(int, input().split())

dijkstra(start, end)