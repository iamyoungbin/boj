import sys
import heapq

input = sys.stdin.readline

N = int(input())
degree = [0 for _ in range(N+1)]
weight = [0 for _ in range(N+1)]
time = [0 for _ in range(N+1)]
edge = [[] for _ in range(N+1)]

for i in range(1, N+1):
    l = list(map(int, input().split()))
    weight[i] = l[0]

    for j in range(1, len(l)-1):
        edge[l[j]].append(i)
        degree[i] += 1

heap = []

for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(heap, (weight[i], i))
    
while heap:
    t, pn = heapq.heappop(heap)
    time[pn] = t

    for nn in edge[pn]:
        degree[nn] -= 1

        if degree[nn] == 0:
            heapq.heappush(heap, (t+weight[nn], nn))

for t in time[1:]:
    print(t)