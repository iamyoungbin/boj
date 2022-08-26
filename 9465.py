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
        
        # ��ƼĿ[0][i] �� ��ƼĿ [1][i-1] Ȥ�� ��ƼĿ[1][i-2]�� ��� ��쿡�� ���õ� �� ����.
        # ��ƼĿ[0][i-2]�� ���� ��ƼĿ[1][i-1]�� ��� ���̽��� �����.

    print(max(dp[0][n-1], dp[1][n-1]))