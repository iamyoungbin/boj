import sys

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x

        if rank[x] == rank[y]:
            rank[x] += 1


N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

for i in range(1,N+1):
    path = list(map(int, sys.stdin.readline().split()))
    for j in range(len(path)):
        if path[j] == 1:
            union(i, j+1)

plan = list(map(int, sys.stdin.readline().split()))

obj = 0
for obj in range(M-1):
    if(find(plan[obj]) != find(plan[obj+1])):
        print("NO")
        break
    if(obj == M-2):
        print("YES")