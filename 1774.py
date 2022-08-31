# -*- coding: utf-8 -*-
import sys
import heapq

def getDist(x, y):
    dist = ((point[x][0] - point[y][0]) ** 2 + (point[x][1] - point[y][1]) ** 2) ** 0.5

    return dist

def prim(n):
    sum = 0.0
    heapq.heappush(heap, (0, 0))    # 정점 0을 MST의 초기 정점으로 선택

    while heap:
        w, v = heapq.heappop(heap)

        if selected[v] == False:    # 정점 v가 아직 MST에 포함되지 않았으면
            selected[v] = True
            sum += w

            for i in range(n):
                if selected[i] == False:    # MST에 포함되지 않은 정점 i들을 대상으로 힙에 추가
                    heapq.heappush(heap, (dist[v][i], i))

        if False not in selected:   # 모든 정점들이 선택되면 종료
            break

    return sum

N, M = map(int, input().split())
heap = []
selected = [False for _ in range(N)]
point = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dist = [[getDist(i, j) for j in range(N)] for i in range(N)]

for _ in range(M):
    x, y = map(lambda l: l-1, map(int, sys.stdin.readline().split()))
    # 이미 선택된 정점들을 거리 0으로 설정
    if x != y:
        dist[x][y] = 0
        dist[y][x] = 0

print("{:.2f}".format(prim(N)))
    
"""
test case:
4 2
0 0
0 1
0 2
0 3
1 4
2 3

ans : 1.00

"""