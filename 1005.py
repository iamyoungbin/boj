import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    edge = [[] for _ in range(N+1)]
    degree = [0 for _ in range(N+1)]
    for _ in range(K):
        u, v = map(int, input().split())
        edge[u].append(v)
        degree[v] += 1
    
    obj = int(input())

    heap = []
    for i in range(1, N+1):
        if degree[i] == 0:
            heapq.heappush(heap, (time[i], i))
        
    while heap:
        pt, pn = heapq.heappop(heap)
        if pn == obj:
            print(pt)
            break
        
        for nn in edge[pn]:
            degree[nn] -= 1
            if degree[nn] == 0:
                heapq.heappush(heap, (pt+time[nn], nn))