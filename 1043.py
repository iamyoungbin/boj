import sys

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x in witness and y in witness:
        return
    elif x in witness:
        parent[y] = x
    elif y in witness:
        parent[x] = y
    elif x >= y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())
witness = list(map(int, sys.stdin.readline().split()))[1:]
party = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(M)]
parent = [i for i in range(N+1)]

cnt = 0

for p in party:
    for i in range(0, len(p)-1):
        union(p[i], p[i+1])      

for p in party:
    for i in range(len(p)):
        if find(p[i]) in witness:
            break
        if i == len(p)-1:
            cnt += 1

print(cnt)