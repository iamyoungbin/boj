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
        if lane[i][1] > lane[j][1] and dp[i] < dp[j]:   # �κм��� dp[j]�� �κм��� dp[i]�� ���Ե� �� �ִ� ���
            dp[i] = dp[j]
    dp[i] += 1

print(num - max(dp))    # ��ü ������ - ���� ���� ������ �� = ���־� �� �������� �ּ� ����