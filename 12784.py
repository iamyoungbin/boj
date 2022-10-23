import sys
from collections import deque

def dfs(node, weight):
    dp[node] = weight
    sum = 0
    
    for w, e in edge[node]:
        if dp[e] == -1:
            dfs(e, w)
            sum += dp[e]
    
    if sum != 0 and sum < dp[node]:
        dp[node] = sum

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    edge = [[] for _ in range(N+1)]
    dp = [-1 for _ in range(N+1)]
    for _ in range(M):
        u, v, d = map(int, input().split())
        edge[u].append((d, v))
        edge[v].append((d, u))
        
    dfs(1, sys.maxsize)
    if M != 0:
        print(dp[1])
    else:
        print(0)