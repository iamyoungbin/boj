# -*- coding: utf-8 -*-
import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

minh = []
for _ in range(N):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(minh, (m, v))

bag = [int(sys.stdin.readline()) for _ in range(K)]
bag.sort()  # 가방 크기를 오름차순 정렬

maxh = []
sum = 0
for i in bag:
    while minh and i >= minh[0][0]: # 가방 무게보다 작은 무게의 보석들(minh)을 모두 maxh 에 넣음
        m, v = heapq.heappop(minh)
        heapq.heappush(maxh, (-v, v))

    if maxh:
        sum += heapq.heappop(maxh)[1] # maxh의 최상위 인덱스 값은 현재 혹은 이후의 가방에 들어갈 수 있는 보석들 중 가장 높은 가치의 보석

print(sum)