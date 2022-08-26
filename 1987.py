import sys

def dfs(y, x, cnt):
    max = cnt

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < R and 0 <= nx < C and map[ny][nx] not in collection:
            collection.add(map[ny][nx])
            temp = dfs(ny, nx, cnt+1)
            if(temp > max):
                max = temp
            collection.remove(map[ny][nx])  # backtracking

    return max

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
collection = set()

R, C = list(map(int, input().split()))
map = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

collection.add(map[0][0])
sol = dfs(0, 0, 1)

print(sol)