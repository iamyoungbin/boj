import sys
sys.setrecursionlimit(10**5)    # 인접 리스트 dfs로 구현하였으므로 n<=10000 일 때, 시간복잡도 O(n+e) = O(10000+9999)를 가지므로

def sol(n):
    great = 0   # 이번 노드에서 우수 마을에 선정될 경우의 이전 노드들까지의 dp 값
    nongreat = 0    # 이번 노드에서 우수 마을로 선정되지 않을 경우의 이전 노드들의 dp 값
    visited[n] = True

    for i in edge[n]:
        if visited[i] == False:
            sol(i)
            great += dp[0][i]   # 우수 마을에 선정될 경우, 이웃 노드들이 모두 일반 마을이여야 함.
            nongreat += max(dp[0][i], dp[1][i]) # 우수 마을에 선정되지 않을 경우, 이웃 노드들이 어떤 마을이든 상관 없음

    dp[0][n] = nongreat
    dp[1][n] = great + node[n]  # 우수 마을인 경우 해당 마을의 주민 수를 합함.

input = sys.stdin.readline

N = int(input())
node = [0] + list(map(int, input().split()))
visited = [False for _ in range(N+1)]
dp = [[0 for _ in range(N+1)] for _ in range(2)]
edge = [[] for _ in range(N+1)]

for _ in range(N-1):
    v, u = map(int, input().split())
    edge[v].append(u)
    edge[u].append(v)

sol(1)

print(max(dp[0][1], dp[1][1]))