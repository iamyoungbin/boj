import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

virus_inital = []
for i in range(N):
    for j in range(N):
        if world[i][j] != 0:
            virus_inital.append((world[i][j], i, j, 0))
virus_inital.sort(key=lambda x:x[0])

dq = deque(virus_inital)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
while dq:
    virus, y, x, time = dq.popleft()
    if time == S:
        break
    
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        
        if 0 <= ny < N and 0 <= nx < N and world[ny][nx] == 0:
            world[ny][nx] = virus
            dq.append((virus, ny, nx, time+1))
            
print(world[X-1][Y-1])