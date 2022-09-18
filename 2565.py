import sys

input = sys.stdin.readline

num = int(input())
lane = []
dp = [0 for _ in range(num)]

for _ in range(num):
    a, b = map(int, input().split())
    lane.append((a, b))

lane.sort(key=lambda x:x[0])

for i in range(num):
    for j in range(i):
        if lane[i][1] > lane[j][1] and dp[i] < dp[j]:   # 부분수열 dp[j]가 부분수열 dp[i]에 포함될 수 있는 경우
            dp[i] = dp[j]
    dp[i] += 1

print(num - max(dp))    # 전체 전깃줄 - 가장 많은 전깃줄 수 = 없애야 할 전깃줄의 최소 갯수