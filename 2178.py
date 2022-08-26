#pypy3
import sys
from collections import deque

def bfs(map, visited):
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0 <= nx < N and 0 <= ny < M and map[nx][ny] == 1 and visited[nx][ny] == 0):
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

bfs(map, visited)

print(visited[N-1][M-1])