# -*- coding: utf-8 -*-
import sys
import heapq

def getDist(x, y):
    dist = ((point[x][0] - point[y][0]) ** 2 + (point[x][1] - point[y][1]) ** 2) ** 0.5

    return dist

def prim(n):
    sum = 0.0
    heapq.heappush(heap, (0, 0))    # ���� 0�� MST�� �ʱ� �������� ����

    while heap:
        w, v = heapq.heappop(heap)

        if selected[v] == False:    # ���� v�� ���� MST�� ���Ե��� �ʾ�����
            selected[v] = True
            sum += w

            for i in range(n):
                if selected[i] == False:    # MST�� ���Ե��� ���� ���� i���� ������� ���� �߰�
                    heapq.heappush(heap, (dist[v][i], i))

        if False not in selected:   # ��� �������� ���õǸ� ����
            break

    return sum

N, M = map(int, input().split())
heap = []
selected = [False for _ in range(N)]
point = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dist = [[getDist(i, j) for j in range(N)] for i in range(N)]

for _ in range(M):
    x, y = map(lambda l: l-1, map(int, sys.stdin.readline().split()))
    # �̹� ���õ� �������� �Ÿ� 0���� ����
    if x != y:
        dist[x][y] = 0
        dist[y][x] = 0

print("{:.2f}".format(prim(N)))
    
"""
test case:
4 2
0 0
0 1
0 2
0 3
1 4
2 3

ans : 1.00

"""