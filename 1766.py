import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

degree = [0 for _ in range(N+1)]
seq = [[] for _ in range(N+1)]

for _ in range(M):
    f, e = map(int, input().split())
    seq[f].append(e)
    degree[e] += 1

heap = []
for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    solve = heapq.heappop(heap)
    print(solve, end=" ")

    for np in seq[solve]:
        if degree[np] == 1:
            heapq.heappush(heap, np)
        else:
            degree[np] -= 1