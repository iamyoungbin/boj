# -*- coding: utf-8 -*-
import sys
import heapq

input = sys.stdin.readline

N = int(input())
problem = []
for _ in range(N):
    problem.append(tuple(map(int, input().split())))
problem.sort()

heap = []
for deadline, value in problem:
    heapq.heappush(heap, value)
    if deadline < len(heap):    # 현재 데드라인보다 더 많은 문제가 힙에 존재하는 경우.
        heapq.heappop(heap)     # 컵라면 수가 가장 적은 문제 팝.

print(sum(heap))