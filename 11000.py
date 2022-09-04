# -*- coding: utf-8 -*-
import sys
import heapq

N = int(input())

room = 0

schedule = []
for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())
    heapq.heappush(schedule, (s, t))    # ���� �����ϴ� �������� Ȯ���� �� �ֵ���

room = 1
timestamp = []
while schedule:
    s, t = heapq.heappop(schedule)
    if not timestamp:
        heapq.heappush(timestamp, (t, s))   # timestamp�� ������ ������ �ð��� �������� �ϵ��� �Ķ���� ����.
    
    else:
        if s < timestamp[0][0] and room == len(timestamp): # t�� �ּ�ġ���� �߰��� s�� ���� ���, �� ���ο� ������ �ʿ��� ���
            room += 1                                      # ���� ������� ���ǰ� �߰��� ������ ���� ������ ���� �ϳ� �߰�
        else:
            heapq.heappop(timestamp)                       # t�� �ּ�ġ���� �߰��� s�� ũ�ų� ���� ���, �� ������ �ϳ� �����Ű�� �Ǵ� ���
        
        heapq.heappush(timestamp, (t, s))

print(room)