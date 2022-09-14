# -*- coding: utf-8 -*-
import sys
from collections import deque

def bfs():
    dq = deque()
    if map[0][0] == 0:
        dist[0][0][0] = 0
    else:
        dist[1][0][0] = 1
        dist[0][0][0] = 1
    dq.append((0, 0, 0))

    while dq:
        py, px, pt = dq.popleft()
        rt = 1 if pt != 1 else 0

        for i in range(4):  # 상하좌우
            ny, nx = py+dy[i], px+dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                nt = map[ny][nx]

                if pt == nt and dist[pt][py][px] + 1 < dist[rt][ny][nx]:    # 서로 같은 방향의 경우
                    dist[rt][ny][nx] = dist[pt][py][px] + 1
                    dq.append((ny, nx, rt))
                elif pt != nt and dist[pt][py][px] < dist[nt][ny][nx]:      # 서로 다른 방향의 경우
                    dist[nt][ny][nx] = dist[pt][py][px]
                    dq.appendleft((ny, nx, nt))

        if pt == 0:     # '\'
            for i in range(2):
                ny, nx = py+ddy[i], px+ddx[i]

                if 0 <= ny < N and 0 <= nx < M:
                    nt = map[ny][nx]

                    if pt == nt and dist[pt][py][px] < dist[nt][ny][nx]:    # 서로 같은 방향
                        dist[nt][ny][nx] = dist[pt][py][px]
                        dq.appendleft((ny, nx, pt))
                    elif rt == nt and dist[pt][py][px] + 1 < dist[pt][ny][nx]:  # 서로 다른 방향
                        dist[pt][ny][nx] = dist[pt][py][px] + 1
                        dq.append((ny, nx, pt))

        else:   # '/'
            for i in range(2, 4):
                ny, nx = py+ddy[i], px+ddx[i]

                if 0 <= ny < N and 0 <= nx < M:
                    nt = map[ny][nx]

                    if pt == nt and dist[pt][py][px] < dist[nt][ny][nx]:    # 서로 같은 방향
                        dist[nt][ny][nx] = dist[pt][py][px]
                        dq.appendleft((ny, nx, nt))
                    elif rt == nt and dist[pt][py][px] + 1 < dist[pt][ny][nx]:  # 서로 다른 방향
                        dist[pt][ny][nx] = dist[pt][py][px] + 1
                        dq.append((ny, nx, pt))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
ddy = [-1, 1, 1, -1]
ddx = [-1, 1, -1, 1]

N, M = map(int, sys.stdin.readline().split())

map = [list(map(lambda x: 0 if x=='\\' else 1, sys.stdin.readline().rstrip())) for _ in range(N)]
dist = [[[sys.maxsize for _ in range(M)] for _ in range(N)] for _ in range(2)]

bfs()

if dist[0][N-1][M-1] == sys.maxsize:
    print("NO SOLUTION")
else:
    print(dist[0][N-1][M-1])

# print("//////")
# for a in dist:
#     for b in a:
#         for c in b:
#             print("{:5}".format(c), end=" ")
#         print()

"""
test case:

7 7
\/\/\//
\/\////
\//\//\
\/\////
\//\//\
\/\////
\/\////

ans : 2
"""