# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10 ** 7)

def solve(n):
    visited[n] = True

    for v in edge[n]:
        if visited[v] == False:
            solve(v)
            dp[1][n] += min(dp[0][v], dp[1][v]) # n이 얼리 어답터이면 자식 노드가 어떤 타입이든 상관없음.
            dp[0][n] += dp[1][v]    # n이 얼리 어답터이면 자식 노드들은 모두 얼리 어답터여야 함.

    dp[1][n] += 1

input = sys.stdin.readline

N = int(input())
edge = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dp = [[0 for _ in range(N+1)] for _ in range(2)]  # 0 => nonalready, 1 => already
for _ in range(N-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

solve(1)

print(min(dp[0][1], dp[1][1]))