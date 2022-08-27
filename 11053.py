N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:   # dp[i]가 부분수열에 포함될 수 있으면
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))