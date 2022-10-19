from math import degrees
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
part_type = [True for _ in range(N+1)]
part_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
edge = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y, K = map(int, input().split())
    if part_type[X]:
        part_type[X] = False
    edge[Y].append((K, X))
    degree[X] += 1

dq = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        dq.append(i)
        
while dq:
    cur = dq.popleft()
    
    for number, next in edge[cur]:
        if part_type[cur]:
            part_sum[next][cur] += number
        else:
            for i in range(1, N+1):
                part_sum[next][i] += part_sum[cur][i] * number
            
        degree[next] -= 1
        if degree[next] == 0:
            dq.append(next)  
            
for part in enumerate(part_sum[N], start=1):
    if part[1] > 0:
        print(part[0]-1, part[1])