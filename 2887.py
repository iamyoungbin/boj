# -*- coding: utf-8 -*-
import sys
import heapq

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y

    if rank[x] == rank[y]:
        rank[x] += 1

input = sys.stdin.readline

N = int(input())

point = []
parent = [i for i in range(N)]
rank = [1 for _ in range(N)]

for i in range(N):
    x, y, z = map(int, input().split())
    point.append((x, y, z, i))

edge = []
for i in range(3):
    point.sort(key=lambda x:x[i])   # 각 축의 좌표에 따라 오름차 정렬
    for j in range(N-1):
        heapq.heappush(edge, (abs(point[j][i]-point[j+1][i]), point[j][3], point[j+1][3]))  # 각 축 좌표마다 양 옆으로 가장 가까운 두 간선만을 갖게 됨.

sum = 0
accepted = 0
while edge: # kruskal
    w, a, b = heapq.heappop(edge)
    if find(a) != find(b):
        union(a, b)
        sum += w
        accepted += 1

    if accepted == N-1:
        print(sum)
        break