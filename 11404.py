import sys

def floyd():
    for m in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                weight[i][j] = min(weight[i][j], weight[i][m] + weight[m][j])

input = sys.stdin.readline

N = int(input())
M = int(input())

weight = [[sys.maxsize if i!=j else 0 for i in range(N+1)] for j in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    weight[u][v] = min(weight[u][v], w)

floyd()

for row in weight[1:]:
    for value in row[1:]:
        if value == sys.maxsize:
            print("0", end=" ")
        else:
            print(value, end=" ")
    print()