import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(M)]
dist = [[sys.maxsize for _ in range(N)] for _ in range(M)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

dq = deque()
dq.append((0, 0))
dist[0][0] = 0

while dq:
    py, px = dq.popleft()

    for i in range(4):
        ny, nx = py+dy[i], px+dx[i]
        if 0 <= ny < M and 0 <= nx < N and dist[py][px] + map[ny][nx] < dist[ny][nx]:
            dist[ny][nx] = dist[py][px] + map[ny][nx]
            if map[ny][nx] == 1:    # wall
                dq.append((ny, nx))
            else:   # empty
                dq.appendleft((ny, nx))

print(dist[-1][-1])