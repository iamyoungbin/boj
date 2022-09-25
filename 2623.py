import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]

for _ in range(M):
    singerlist = list(map(int, input().split()))
    for i in range(1, singerlist[0]):
        if singerlist[i+1] not in edge[singerlist[i]]:
            edge[singerlist[i]].append(singerlist[i+1])
            degree[singerlist[i+1]] += 1

dq= deque()
for i in range(1, N+1):
    if degree[i] == 0:
        dq.append(i)

sol = []
while dq:
    pn = dq.popleft()
    sol.append(pn)

    for nn in edge[pn]:
        degree[nn] -= 1
        if degree[nn] == 0:
            dq.append(nn)
    
if len(sol) == N:
    for singer in sol:
        print(singer)
else:
    print(0)