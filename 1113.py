# -*- coding: utf-8 -*-
import sys
from collections import deque

def bfs(y, x, lvl):
    mount = 0
    flag = True
    queue = deque()
    map[y][x] = lvl+1   # �ش� ���� �湮 ó��
    queue.append((y, x))

    while queue:
        py, px = queue.popleft()
        mount += 1

        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:  # ������ �ܰ��� ������ flag=False�� �Ͽ� �ѷ��� �߰����� ����.
                flag = False
            elif map[ny][nx] == lvl:
                queue.append((ny, nx))
                map[ny][nx] = lvl+1

    if flag == True:
        return mount
    else:
        return 0

input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(N)]

sum = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for w in range(1, 9):
    for i in range(N):
        for j in range(M):
            if map[i][j] == w:
                sum += bfs(i, j, w)

print(sum)