# -*- coding: utf-8 -*-
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    seq = list(map(int, input().split()))
    graph = [[False for _ in range(n+1)] for _ in range(n+1)]   # 밀집 그래프이기 때문에 배열로 그래프 표현
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
    for _ in range(n):  # 총 팀수인 n반큼 반복. while queue로 하게 되면 len(queue)==0 을 체크하지 못함.
        if len(queue) > 1:  # 등수가 같은 사람이 존재해 확실한 순위를 찾을 수 없는 경우
            gradeflag = True
            break
        if len(queue) == 0: # 다음 등수를 찾을 수 없는 경우, 즉 데이터 일관성이 결여된 경우.
            seqflag = True
            break

        winner = queue.popleft()
        sol.append(winner)
        for i in range(1, n+1):
            if graph[winner][i]:
                degree[i] -= 1
                if degree[i] == 0:  # degree == 0 이면 다음 순번으로 큐에 추가.
                    queue.append(i)

    if gradeflag:
        print("?")
    elif seqflag:
        print("IMPOSSIBLE")
    else:
        print(*sol)