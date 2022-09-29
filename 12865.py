import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
obj = []

for _ in range(N):
    obj.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        if obj[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - obj[i-1][0]] + obj[i-1][1])

print(dp[N][K])