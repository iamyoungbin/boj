# -*- coding: utf-8 -*-
import sys
from collections import deque

def cheeseCheck(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        py, px = queue.popleft()
        meltCnt = 0
        for i in range(4):
            ny, nx = py + dy[i], px + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if map[ny][nx] == -1:   # 외부 공기와 닿으면 meltcheck 증가
                    meltCnt += 1
                elif map[ny][nx] != 0 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

        if meltCnt >= 2:    # 2군데 이상 맞닿으면 외부 공기(진)
            map[py][px] = 2


def spread(y, x):   # (y, x)와 맞닿은 내부 공기 집합 외부 공기화
    queue = deque()
    queue.append((y, x))

    while queue:
        py, px = queue.popleft()

        for i in range(4):
            ny, nx = py+dy[i], px+dx[i]

            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == False and map[ny][nx] == 0:
                visited[ny][nx] = True
                map[ny][nx] = -1
                queue.append((ny, nx))


def melt(): # 온전한 치즈 갯수 반환, 녹을 치즈는 외부 공기로 바꾸고 spread를 통해 맞닿은 내부 공기 집합을 외부 공기화.
    cheese = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            if map[i][j] == 1:
                cheese += 1
            elif map[i][j] == 2:
                map[i][j] = -1
                spread(i, j)

    return cheese


N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]   # -1 => outside air, 0 => inside air, 1 = > cheese, 2 => melting cheese

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 초기 바깥 공기 체크
q = deque()
q.append((0, 0))
map[0][0] = -1
while q:
    py, px = q.popleft()

    for i in range(4):
        ny, nx = py + dy[i], px + dx[i]
        if 0 <= ny < N and 0 <= nx < M and map[ny][nx] == 0:
            map[ny][nx] = -1
            q.append((ny, nx))

cnt = 1
while True:
    total = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if map[i][j] == 1 and visited[i][j] == False:
                visited[i][j] == True
                cheeseCheck(i, j)

    if melt() == 0: # 남은 치즈가 없으면
        print(cnt)
        break
    else:
        cnt += 1

    # print("////")
    # for ma in map:
    #     for m in ma:
    #         print("{:3}".format(m), end="")
    #     print()