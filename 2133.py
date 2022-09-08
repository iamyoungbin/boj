# -*- coding: utf-8 -*-
N = int(input())

if N == 0:
    print("1")
elif N % 2 == 1:
    print("0")
else:
    dp = [0 for _ in range(N+1)]
    dp[2] = 3

    for i in range(4, N+1, 2):
        dp[i] = dp[i-2]*3   # 기존타일 + 일반타일(3가지) ... 순방향 특수타일은 이전 dp를 통해 계산됨.
        for j in range(i-4, 0, -2): # 역방향 특수타일 계산 n-4,4 / n-6,6 / n-8,8 / ... / 2, n-2
            dp[i] += dp[j]*2
        dp[i] += 2  # 모든 타일을 사용한 특수타일 계산
    
    print(dp[N])