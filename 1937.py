import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(y, x):
    if dp[y][x] != 0:
        return dp[y][x]
    dp[y][x] = 1
    
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        
        if 0 <= ny < n and 0 <= nx < n and forest[y][x] < forest[ny][nx]:
            dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
    
    return dp[y][x]

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n+1)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

sol = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            sol = max(sol, dfs(i, j))
                
print(sol)