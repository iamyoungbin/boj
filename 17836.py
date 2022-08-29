import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    time = 10001

    while queue:
        x, y, z = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + 1

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if nx == N-1 and ny == M-1:
                    return min(nz, time)
                elif map[nx][ny] == 2:
                    time = nz + abs(N-1 - nx) + abs(M-1 - ny)
                    visited[nx][ny] = 1
                elif map[nx][ny] == 0:
                    queue.append([nx, ny, nz])
                    visited[nx][ny] = 1

    return time

N, M, T = map(int, input().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = bfs()
if result <= T:
    print(result)
else:
    print("Fail")