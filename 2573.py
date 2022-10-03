# -*- coding: utf-8 -*-
# pypy3
import sys
from collections import deque

input = sys.stdin.readline

def bfs(y, x):
    melt_list = []
    dq = deque()
    dq.append((y, x))
    visited[y][x] = True

    while dq:
        cur_y, cur_x = dq.popleft()
        melt_count = 0
        for i in range(4):
            next_y, next_x = cur_y + dy[i], cur_x + dx[i]

            if 0 <= next_y < N and 0 <= next_x < M:
                if map[next_y][next_x] == 0:    # sea
                    melt_count += 1
                elif visited[next_y][next_x] == False:  # ice
                    dq.append((next_y, next_x))
                    visited[next_y][next_x] = True

        melt_list.append((cur_y, cur_x, melt_count))    # 녹일 얼음 리스트에 추가.

    for my, mx, mount in melt_list: # melt
        map[my][mx] = max(map[my][mx]-mount, 0)

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

time = 0
while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    iceberg = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            if map[i][j] != 0 and visited[i][j] == False:   # bfs를 한번 실행할 때마다 빙산 하나를 순회.
                iceberg += 1
                if iceberg >= 2:
                    print(time)
                    exit(0)
                else:
                    bfs(i, j)

    if iceberg == 0:
        print(0)
        break

    time += 1