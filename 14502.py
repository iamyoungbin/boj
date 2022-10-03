# -*- coding: utf-8 -*-
import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

def spread():   # bfs. ���̷��� Ȯ��.
    dq = deque()
    for vy, vx in virus:
        dq.append((vy, vx))

    while dq:
        cy, cx = dq.popleft()

        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]

            if 0 <= ny < N and 0 <= nx < M and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                dq.append((ny, nx))

def get_area():
    area = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                area += 1

    return area

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
empty = []  # �� ������ ��ǥ���� ���� ����Ʈ
virus = []  # ���� ���̷����� ��ǥ���� ���� ����Ʈ
for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            empty.append((i, j))
        elif map[i][j] == 2:
            virus.append((i, j))

sol = -1
for com in combinations(empty, 3):  # �� ��ǥ�߿��� 3���� �����Ͽ� �������
    temp = deepcopy(map)
    for y, x in com:
        temp[y][x] = 1

    spread()
    sol = max(sol, get_area())

print(sol)