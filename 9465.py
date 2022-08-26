 # -*- coding: utf-8 -*-
import sys

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    if n != 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    
    for i in range(2, n):   # case : n > 2
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
        
        # 스티커[0][i] 는 스티커 [1][i-1] 혹은 스티커[1][i-2]를 떼어낸 경우에만 선택될 수 있음.
        # 스티커[0][i-2]의 경우는 스티커[1][i-1]을 떼어낸 케이스에 흡수됨.

    print(max(dp[0][n-1], dp[1][n-1]))