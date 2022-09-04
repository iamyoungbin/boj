# -*- coding: utf-8 -*-
import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

minh = []
for _ in range(N):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(minh, (m, v))

bag = [int(sys.stdin.readline()) for _ in range(K)]
bag.sort()  # ���� ũ�⸦ �������� ����

maxh = []
sum = 0
for i in bag:
    while minh and i >= minh[0][0]: # ���� ���Ժ��� ���� ������ ������(minh)�� ��� maxh �� ����
        m, v = heapq.heappop(minh)
        heapq.heappush(maxh, (-v, v))

    if maxh:
        sum += heapq.heappop(maxh)[1] # maxh�� �ֻ��� �ε��� ���� ���� Ȥ�� ������ ���濡 �� �� �ִ� ������ �� ���� ���� ��ġ�� ����

print(sum)