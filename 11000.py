# -*- coding: utf-8 -*-
import sys
import heapq

N = int(input())

room = 0

schedule = []
for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())
    heapq.heappush(schedule, (s, t))    # 먼저 시작하는 수업부터 확인할 수 있도록

room = 1
timestamp = []
while schedule:
    s, t = heapq.heappop(schedule)
    if not timestamp:
        heapq.heappush(timestamp, (t, s))   # timestamp가 수업이 끝나는 시간을 기준으로 하도록 파라메터 설정.
    
    else:
        if s < timestamp[0][0] and room == len(timestamp): # t중 최소치보다 추가될 s가 작은 경우, 즉 새로운 교실이 필요한 경우
            room += 1                                      # 현재 사용중인 교실과 추가될 교실의 수가 같으면 교실 하나 추가
        else:
            heapq.heappop(timestamp)                       # t중 최소치보다 추가될 s가 크거나 같은 경우, 즉 수업을 하나 종료시키면 되는 경우
        
        heapq.heappush(timestamp, (t, s))

print(room)