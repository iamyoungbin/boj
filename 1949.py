import sys
sys.setrecursionlimit(10**5)    # ���� ����Ʈ dfs�� �����Ͽ����Ƿ� n<=10000 �� ��, �ð����⵵ O(n+e) = O(10000+9999)�� �����Ƿ�

def sol(n):
    great = 0   # �̹� ��忡�� ��� ������ ������ ����� ���� ��������� dp ��
    nongreat = 0    # �̹� ��忡�� ��� ������ �������� ���� ����� ���� ������ dp ��
    visited[n] = True

    for i in edge[n]:
        if visited[i] == False:
            sol(i)
            great += dp[0][i]   # ��� ������ ������ ���, �̿� ������ ��� �Ϲ� �����̿��� ��.
            nongreat += max(dp[0][i], dp[1][i]) # ��� ������ �������� ���� ���, �̿� ������ � �����̵� ��� ����

    dp[0][n] = nongreat
    dp[1][n] = great + node[n]  # ��� ������ ��� �ش� ������ �ֹ� ���� ����.

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