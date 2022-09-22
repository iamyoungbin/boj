# -*- coding: utf-8 -*-
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]

sol = [0 for _ in range(4)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

dq = deque()
for i in range(N):
    for j in range(M):
        if map[i][j] == 1 or map[i][j] == 2:
            visited[i][j] = 0
            dq.append((map[i][j], i, j, 0))

while dq:
    type, py, px, pt = dq.popleft()

    if map[py][px] != 3:    # 마을이 여전히 바이러스 1에만 감염되어 있을 경우, 감염마을(진)=> 감염마을
        for i in range(4):
            ny, nx = py+dy[i], px+dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if map[ny][nx] == 0:    # 미감염 마을인 경우 감염마을(진)
                    dq.append((type, ny, nx, pt+1))
                    map[ny][nx] = type
                    visited[ny][nx] = pt+1
                elif map[ny][nx] != type and map[ny][nx] != -1 and map[ny][nx] != 3 and visited[ny][nx] == pt+1:
                    # 감염마을(진)에 다른 바이러스가 감염시키려는 경우.
                    map[ny][nx] = 3

# print("///")
# for m in map:
#     print(*m)
sol = [0 for _ in range(4)]
for i in range(N):
    for j in range(M):
        if map[i][j] != 0 and map[i][j] != -1:
            sol[map[i][j]] += 1
print(*sol[1:])