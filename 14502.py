# -*- coding: utf-8 -*-
import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

def spread():   # bfs. 바이러스 확산.
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
empty = []  # 빈 공간의 좌표들을 모을 리스트
virus = []  # 기존 바이러스의 좌표들을 모을 리스트
for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            empty.append((i, j))
        elif map[i][j] == 2:
            virus.append((i, j))

sol = -1
for com in combinations(empty, 3):  # 벽 좌표중에서 3개를 조합하여 벽세우기
    temp = deepcopy(map)
    for y, x in com:
        temp[y][x] = 1

    spread()
    sol = max(sol, get_area())

print(sol)