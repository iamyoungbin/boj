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
    if deadline < len(heap):    # ���� ������κ��� �� ���� ������ ���� �����ϴ� ���.
        heapq.heappop(heap)     # �Ŷ�� ���� ���� ���� ���� ��.

print(sum(heap))