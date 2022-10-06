import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
degree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    degree[B] += 1
    graph[A].append(B)

dq = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        dq.append(i)
        
while dq:
    previous = dq.popleft()
    print(previous, end=" ")
    
    for vertex in graph[previous]:
        degree[vertex] -= 1
        if degree[vertex] == 0:
            dq.append(vertex)