#pypy3
import sys
from collections import deque

def bfs(y, x):
    visited[y][x] = True
    queue = deque()
    queue.append((y, x))
    sum = 0
    linked = []
    
    while queue:
        cy, cx = queue.popleft()
        sum += populatoin[cy][cx]
        linked.append((cy ,cx))
        
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == False and L <= abs(populatoin[cy][cx] - populatoin[ny][nx]) <= R and abs(populatoin[cy][cx] - populatoin[ny][nx]) != 0:
                queue.append((ny, nx))
                visited[ny][nx] = True
    
    if len(linked) == 1:
        return 0
    else:
        for y, x in linked:
            populatoin[y][x] = sum // len(linked)
        return 1       

input = sys.stdin.readline
N, L, R = map(int, input().split())
populatoin = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
sol = 0
while True:
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                cnt += bfs(i, j)
    
    # for p in populatoin:
    #     print(*p)
    # print("//")
                
    if cnt == 0:
        break
    else:
        sol += 1
        
print(sol)