import sys
from collections import deque

input = sys.stdin.readline

def rain(y, x):
    sum = 0
    flag = True
    dq = deque([x])
    block[y][x] = 1

    while dq:
        cx = dq.popleft()
        sum += 1
        for i in range(2):
            nx = cx + dx[i]

            if 0 <= nx < W and block[y][nx] == 0:
                block[y][nx] = 1
                dq.append(nx)
            elif nx >= W or nx < 0:
                flag = False

    if flag == False:
        # print("False")
        return 0
    else:
        # print("+ {}".format(sum))
        return sum

H, W = map(int, input().split())
block = [[0 for _ in range(W)] for _ in range(H)]

row = list(map(int, input().split()))
for i in range(W):
    for j in range(row[i]):
        block[j][i] = 1

sol = 0
dx = [-1, 1]
for i in range(H):
    # print("{}>>>>>".format(i))
    for j in range(W):
        if block[i][j] == 0:
            sol += rain(i, j)

print(sol)