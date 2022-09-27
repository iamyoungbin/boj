# -*- coding: utf-8 -*-
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    seq = list(map(int, input().split()))
    graph = [[False for _ in range(n+1)] for _ in range(n+1)]   # ���� �׷����̱� ������ �迭�� �׷��� ǥ��
    degree = [0 for _ in range(n+1)]

    for i in range(n-1):
        for j in range(i+1, n):
            graph[seq[i]][seq[j]] = True
            degree[seq[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            degree[a] += 1
            degree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            degree[a] -= 1
            degree[b] += 1

    queue = deque()
    for i in range(1, n+1):
        if degree[i] == 0:
            queue.append(i)

    gradeflag = False
    seqflag = False
    sol = []
    for _ in range(n):  # �� ������ n��ŭ �ݺ�. while queue�� �ϰ� �Ǹ� len(queue)==0 �� üũ���� ����.
        if len(queue) > 1:  # ����� ���� ����� ������ Ȯ���� ������ ã�� �� ���� ���
            gradeflag = True
            break
        if len(queue) == 0: # ���� ����� ã�� �� ���� ���, �� ������ �ϰ����� �Ῡ�� ���.
            seqflag = True
            break

        winner = queue.popleft()
        sol.append(winner)
        for i in range(1, n+1):
            if graph[winner][i]:
                degree[i] -= 1
                if degree[i] == 0:  # degree == 0 �̸� ���� �������� ť�� �߰�.
                    queue.append(i)

    if gradeflag:
        print("?")
    elif seqflag:
        print("IMPOSSIBLE")
    else:
        print(*sol)